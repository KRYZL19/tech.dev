"""Balance calculation routes — LSI, saturation index, water balance."""
from fastapi import APIRouter, Query
from models.schemas import (
    BalanceCheckRequest, BalanceCheckResponse, Recommendation,
    SaturationRequest, SaturationResponse, CSIStatus, BalanceStatus
)
from data.pool_types import (
    TEMP_FACTORS_F, alkalinity_factor, calcium_factor,
    CHLORINE_DEMAND_CURVES, LSI_BALANCED_MIN, LSI_BALANCED_MAX, RECOMMENDED
)
import math

router = APIRouter(prefix="/balance", tags=["balance"])


def get_temp_factor(temp_f: float) -> float:
    """Interpolate temperature factor for LSI."""
    temps = sorted(TEMP_FACTORS_F.keys())
    if temp_f <= temps[0]:
        return TEMP_FACTORS_F[temps[0]]
    if temp_f >= temps[-1]:
        return TEMP_FACTORS_F[temps[-1]]
    for i in range(len(temps) - 1):
        if temps[i] <= temp_f <= temps[i + 1]:
            t1, t2 = temps[i], temps[i + 1]
            f1, f2 = TEMP_FACTORS_F[t1], TEMP_FACTORS_F[t2]
            return f1 + (f2 - f1) * (temp_f - t1) / (t2 - t1)
    return 1.0


def calculate_lsi(ph: float, alkalinity_ppm: float, calcium_hardness_ppm: float,
                  temp_f: float) -> float:
    """
    Calculate Langelier Saturation Index (LSI).
    SI = pH + TF + AF + CF - HF
    HF (hardness factor) ≈ 12.1 at 68°F baseline, adjusted here to 12.0 for simplicity.
    """
    tf = get_temp_factor(temp_f)
    af = alkalinity_factor(alkalinity_ppm)
    cf = calcium_factor(calcium_hardness_ppm)
    hf = 12.1  # constant reference point
    si = ph + tf + af + cf - hf
    return round(si, 3)


def get_fci_demand_multiplier(cya_ppm: float) -> tuple:
    """Return chlorine demand multiplier and note based on CYA level."""
    for (low, high), (mult, note) in CHLORINE_DEMAND_CURVES.items():
        if low <= cya_ppm < high:
            return mult, note
    return 4.0, "CRITICAL: FCI doubles demand overnight"


def lsi_balance_status(si: float) -> BalanceStatus:
    """Determine water balance status from LSI value."""
    if si < -1.0:
        return BalanceStatus.SEVERE_CORROSIVE
    if si < LSI_BALANCED_MIN:
        return BalanceStatus.CORROSIVE
    if si > 1.0:
        return BalanceStatus.SEVERE_SCALE
    if si > LSI_BALANCED_MAX:
        return BalanceStatus.SCALE_FORMING
    return BalanceStatus.BALANCED


def csi_status_from_si(si: float) -> CSIStatus:
    if si < LSI_BALANCED_MIN:
        return CSIStatus.CORROSIVE
    if si > LSI_BALANCED_MAX:
        return CSIStatus.SCALE_FORMING
    return CSIStatus.BALANCED


def generate_recommendations(
    chlorine_ppm: float, ph: float, alkalinity_ppm: float,
    calcium_hardness_ppm: float, stabilizer_ppm: float,
    si: float, balance_status: BalanceStatus
) -> list:
    """Generate prioritized recommendations based on current pool chemistry."""
    recs = []

    # Chlorine
    if chlorine_ppm < RECOMMENDED["chlorine"][0]:
        deficit = RECOMMENDED["chlorine"][0] - chlorine_ppm
        recs.append(Recommendation(
            parameter="chlorine",
            current=round(chlorine_ppm, 2),
            target=f"{RECOMMENDED['chlorine'][0]}-{RECOMMENDED['chlorine'][1]} ppm",
            action=f"Add chlorine to raise by ~{deficit:.1f} ppm. Consider CYA level — if above 150ppm, demand doubles.",
            priority="high" if chlorine_ppm < 0.5 else "medium"
        ))
    elif chlorine_ppm > RECOMMENDED["chlorine"][1] * 2:
        recs.append(Recommendation(
            parameter="chlorine",
            current=round(chlorine_ppm, 2),
            target=f"{RECOMMENDED['chlorine'][0]}-{RECOMMENDED['chlorine'][1]} ppm",
            action="Chlorine critically high — do not add more. Allow to UV/chlorinate down or dilute.",
            priority="critical"
        ))

    # pH
    if ph < RECOMMENDED["ph"][0]:
        recs.append(Recommendation(
            parameter="pH",
            current=round(ph, 2),
            target=f"{RECOMMENDED['ph'][0]}-{RECOMMENDED['ph'][1]}",
            action="Add sodium carbonate (soda ash) to raise pH. Use ~6 oz per 10k gallons per 0.2 pH.",
            priority="high"
        ))
    elif ph > RECOMMENDED["ph"][1]:
        recs.append(Recommendation(
            parameter="pH",
            current=round(ph, 2),
            target=f"{RECOMMENDED['ph'][0]}-{RECOMMENDED['ph'][1]}",
            action="Add muriatic acid to lower pH. Use ~16 oz (32%) per 10k gallons per 0.2 pH.",
            priority="high"
        ))

    # Alkalinity
    if alkalinity_ppm < RECOMMENDED["alkalinity"][0]:
        recs.append(Recommendation(
            parameter="alkalinity",
            current=round(alkalinity_ppm, 1),
            target=f"{RECOMMENDED['alkalinity'][0]}-{RECOMMENDED['alkalinity'][1]} ppm",
            action="Add sodium bicarbonate to raise alkalinity. Target 80-120 ppm.",
            priority="medium"
        ))
    elif alkalinity_ppm > RECOMMENDED["alkalinity"][1]:
        recs.append(Recommendation(
            parameter="alkalinity",
            current=round(alkalinity_ppm, 1),
            target=f"{RECOMMENDED['alkalinity'][0]}-{RECOMMENDED['alkalinity'][1]} ppm",
            action="Aerate to drive CO2 off and naturally lower alkalinity, or dilute with fresh water.",
            priority="medium"
        ))

    # Calcium Hardness
    if calcium_hardness_ppm < RECOMMENDED["calcium_hardness"][0]:
        recs.append(Recommendation(
            parameter="calcium_hardness",
            current=round(calcium_hardness_ppm, 1),
            target=f"{RECOMMENDED['calcium_hardness'][0]}-{RECOMMENDED['calcium_hardness'][1]} ppm",
            action="Add calcium chloride to raise CH. Target 200-400 ppm.",
            priority="low"
        ))
    elif calcium_hardness_ppm > RECOMMENDED["calcium_hardness"][1]:
        recs.append(Recommendation(
            parameter="calcium_hardness",
            current=round(calcium_hardness_ppm, 1),
            target=f"{RECOMMENDED['calcium_hardness'][0]}-{RECOMMENDED['calcium_hardness'][1]} ppm",
            action="Dilute with low-CH water to reduce calcium hardness and prevent scaling.",
            priority="high"
        ))

    # CYA (stabilizer) — critical if over 150
    if stabilizer_ppm > 150:
        recs.append(Recommendation(
            parameter="stabilizer_cya",
            current=round(stabilizer_ppm, 1),
            target="30-50 ppm",
            action="CRITICAL: CYA above 150ppm. Chlorine effectiveness drops 75%+. Dilution required — drain and refill 50%+ of pool volume.",
            priority="critical"
        ))
    elif stabilizer_ppm > 100:
        recs.append(Recommendation(
            parameter="stabilizer_cya",
            current=round(stabilizer_ppm, 1),
            target="30-50 ppm",
            action="CYA high — chlorine demand is significantly elevated. Consider partial dilution.",
            priority="high"
        ))
    elif stabilizer_ppm < RECOMMENDED["cya"][0]:
        recs.append(Recommendation(
            parameter="stabilizer_cya",
            current=round(stabilizer_ppm, 1),
            target=f"{RECOMMENDED['cya'][0]}-{RECOMMENDED['cya'][1]} ppm",
            action="Add cyanuric acid (CYA) stabilizer to protect chlorine from UV degradation. Target 30-50 ppm.",
            priority="medium"
        ))

    # LSI / balance status
    if balance_status in (BalanceStatus.SEVERE_CORROSIVE, BalanceStatus.SEVERE_SCALE):
        recs.append(Recommendation(
            parameter="saturation_index",
            current=round(si, 3),
            target=f"{LSI_BALANCED_MIN} to {LSI_BALANCED_MAX}",
            action=f"Water is {balance_status.value.replace('_', ' ')}. Address immediately — risk of surface etching or scaling damage.",
            priority="critical"
        ))
    elif balance_status in (BalanceStatus.CORROSIVE, BalanceStatus.SCALE_FORMING):
        recs.append(Recommendation(
            parameter="saturation_index",
            current=round(si, 3),
            target=f"{LSI_BALANCED_MIN} to {LSI_BALANCED_MAX}",
            action=f"Water is slightly {balance_status.value.replace('_', ' ')}. Adjust pH or alkalinity.",
            priority="medium"
        ))

    return recs


@router.post("/check", response_model=BalanceCheckResponse)
async def check_balance(req: BalanceCheckRequest):
    """
    Full water balance check with LSI, FCI alert, and prioritized recommendations.
    """
    si = calculate_lsi(req.ph, req.alkalinity_ppm, req.calcium_hardness_ppm, req.temp_f)
    balance_status = lsi_balance_status(si)

    demand_mult, fci_note = get_fci_demand_multiplier(req.stabilizer_ppm)
    fci_alert = req.stabilizer_ppm > 150

    recs = generate_recommendations(
        chlorine_ppm=req.chlorine_ppm,
        ph=req.ph,
        alkalinity_ppm=req.alkalinity_ppm,
        calcium_hardness_ppm=req.calcium_hardness_ppm,
        stabilizer_ppm=req.stabilizer_ppm,
        si=si,
        balance_status=balance_status
    )

    return BalanceCheckResponse(
        saturation_index=si,
        balance_status=balance_status,
        recommendations=recs,
        fci_alert=fci_alert,
        fci_note=fci_note if fci_alert else None
    )


@router.get("/saturation", response_model=SaturationResponse)
async def saturation_index(
    ph: float = Query(..., ge=0, le=14),
    alkalinity: float = Query(..., ge=0),
    calcium_hardness: float = Query(..., ge=0),
    temp: float = Query(..., ge=32, le=120),
    cya: float = Query(..., ge=0),
):
    """
    Calculate Langelier Saturation Index (LSI) from individual parameters.
    CYA is noted but LSI calculation focuses on pH/alkalinity/calcium/temperature.
    """
    tf = get_temp_factor(temp)
    af = alkalinity_factor(alkalinity)
    cf = calcium_factor(calcium_hardness)
    # HF adjusted for actual temp
    si = ph + tf + af + cf - 12.1
    si = round(si, 3)

    csi_status = csi_status_from_si(si)

    return SaturationResponse(
        si_value=si,
        csi_status=csi_status,
        ph_factor=round(ph, 2),
        temp_factor=round(tf, 2),
        alk_factor=round(af, 3),
        calcium_factor_val=round(cf, 3),
    )
