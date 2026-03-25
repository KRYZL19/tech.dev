"""Dosing calculation routes — chlorine, pH, chloramine breakpoint."""
from fastapi import APIRouter
from models.schemas import (
    ChlorineDoseRequest, ChlorineDoseResponse,
    PHAdjustRequest, PHAdjustResponse,
    ChloramineConvertRequest, ChloramineConvertResponse
)
from data.pool_types import (
    CHLORINE_DEMAND_CURVES, CHLORINE_TYPES,
    PH_RAISE_SODA_ASH, PH_LOWER_MURIATIC
)

router = APIRouter(prefix="/dose", tags=["dosing"])


def get_fci_multiplier(cya_ppm: float) -> tuple:
    """Return (multiplier, note, is_fci_alert) for CYA level."""
    for (low, high), (mult, note) in CHLORINE_DEMAND_CURVES.items():
        if low <= cya_ppm < high:
            return mult, note, cya_ppm > 150
    return 4.0, "CRITICAL: FCI doubles demand overnight", True


def chlorine_ppm_to_oz(ppm: float, gallons: float, avail_cl: float) -> float:
    """
    Convert desired ppm increase to ounces of product.
    Formula: oz = (ppm × gallons × 8.34) / (avail_cl_pct × 1,000,000) × 16
             = (ppm × gallons × 8.34 × 16) / (avail_cl_pct × 1,000,000)
    """
    if avail_cl <= 0:
        return 0.0
    # ppm × gal × 8.34 lb/gal = ppm-gallons in pounds
    # divide by 1,000,000 to get fraction
    # divide by avail_cl to account for product strength
    # multiply by 16 to convert lbs to oz
    oz = (ppm * gallons * 8.34 * 16) / (avail_cl * 1_000_000)
    return round(oz, 2)


def dose_chlorine(gallons: float, current_ppm: float, target_ppm: float,
                  chlorine_type: str, cya_ppm: float = 0) -> ChlorineDoseResponse:
    """Calculate chlorine dose with FCI-adjusted demand."""
    ppm_needed = max(0, target_ppm - current_ppm)
    prod = CHLORINE_TYPES.get(chlorine_type, CHLORINE_TYPES["liquid"])

    base_oz = chlorine_ppm_to_oz(ppm_needed, gallons, prod["avail氯"])

    mult, note, fci_alert = get_fci_multiplier(cya_ppm)
    adjusted_oz = round(base_oz * mult, 2)

    # Cost estimate (cost_per_lb * weight in lbs)
    # oz / 16 = lbs
    cost = round(adjusted_oz / 16 * prod["cost_per_lb"], 2)

    return ChlorineDoseResponse(
        oz_needed=adjusted_oz,
        cost_estimate=cost,
        demand_multiplier=mult,
        fci_adjusted=fci_alert,
        fci_note=note if fci_alert else None
    )


@router.post("/chlorine", response_model=ChlorineDoseResponse)
async def dose_chlorine_endpoint(req: ChlorineDoseRequest):
    """
    Calculate chlorine dose needed to reach target ppm.
    For FCI/CYA-aware dosing, use /dose/chlorine-adjusted instead.
    """
    ppm_needed = max(0, req.target_ppm - req.current_chlorine_ppm)
    prod = CHLORINE_TYPES.get(req.chlorine_type.value, CHLORINE_TYPES["liquid"])

    base_oz = chlorine_ppm_to_oz(ppm_needed, req.pool_gallons, prod["avail氯"])
    oz_needed = round(base_oz, 2)
    cost = round(oz_needed / 16 * prod["cost_per_lb"], 2)

    return ChlorineDoseResponse(
        oz_needed=oz_needed,
        cost_estimate=cost,
        demand_multiplier=1.0,
        fci_adjusted=False,
        fci_note="Pass cya_ppm to /dose/chlorine-adjusted for FCI-aware dosing"
    )


@router.post("/chlorine-adjusted", response_model=ChlorineDoseResponse)
async def dose_chlorine_adjusted(
    pool_gallons: float,
    current_chlorine_ppm: float,
    target_ppm: float,
    chlorine_type: str,
    cya_ppm: float = 0,
):
    """Chlorine dose WITH FCI/CYA adjustment. Use this for FCI-aware dosing."""
    return dose_chlorine(
        gallons=pool_gallons,
        current_ppm=current_chlorine_ppm,
        target_ppm=target_ppm,
        chlorine_type=chlorine_type,
        cya_ppm=cya_ppm
    )


@router.post("/ph", response_model=PHAdjustResponse)
async def adjust_ph(req: PHAdjustRequest):
    """
    Calculate chemical needed to adjust pH.
    Raises pH: Sodium Carbonate (Soda Ash) — ~6 oz per 10k gal per 0.2 pH rise
    Lowers pH: Muriatic Acid (32%) — ~16 oz per 10k gal per 0.2 pH drop
    """
    ph_diff = req.target_ph - req.current_ph

    if abs(ph_diff) < 0.01:
        return PHAdjustResponse(
            sodium_carbonate_oz=None,
            muriatic_acid_oz=None,
            chemical_direction="none",
            gallons_affected=req.pool_gallons
        )

    direction = "raise" if ph_diff > 0 else "lower"

    # Scale factor: chemical per 10k gallons per 0.2 pH
    scale = req.pool_gallons / 10000

    if direction == "raise":
        # pH too low — add soda ash
        oz_per_0p2 = PH_RAISE_SODA_ASH * scale
        pH_steps = abs(ph_diff) / 0.2
        total_oz = round(oz_per_0p2 * pH_steps, 2)
        return PHAdjustResponse(
            sodium_carbonate_oz=total_oz,
            muriatic_acid_oz=None,
            chemical_direction=direction,
            gallons_affected=req.pool_gallons
        )
    else:
        # pH too high — add muriatic acid
        oz_per_0p2 = PH_LOWER_MURIATIC * scale
        pH_steps = abs(ph_diff) / 0.2
        total_oz = round(oz_per_0p2 * pH_steps, 2)
        return PHAdjustResponse(
            sodium_carbonate_oz=None,
            muriatic_acid_oz=total_oz,
            chemical_direction=direction,
            gallons_affected=req.pool_gallons
        )


@router.post("/chloramine", response_model=ChloramineConvertResponse)
async def breakpoint_chloramine(req: ChloramineConvertRequest):
    """
    Breakpoint chlorination calculator.
    Rule: Add chlorine at 10x the combined chlorine (chloramine) level
    to reach breakpoint and break apart chloramines.
    """
    return calc_breakpoint(req)


def calc_breakpoint(req: ChloramineConvertRequest) -> ChloramineConvertResponse:
    """Shared breakpoint chlorination logic."""
    combined_cl = req.combined_chloramine_ppm
    breakpoint_ppm = round(combined_cl * 10, 2)
    oz_per_10k = round(breakpoint_ppm * 1.3, 2)
    if combined_cl < 0.5:
        stage_note = "Combined chlorine is low. Regular maintenance chlorination sufficient."
    elif combined_cl < 1.0:
        stage_note = "Combined chlorine detectable. Maintain free chlorine above 1.5 ppm."
    elif combined_cl < 2.0:
        stage_note = "Combined chlorine elevated. Consider breakpoint dosing if chlorine demand is met."
    else:
        stage_note = "High combined chlorine. Breakpoint chlorination recommended. Add 10x dose overnight with pool circulated."
    return ChloramineConvertResponse(
        breakpoint_dose_ppm=breakpoint_ppm,
        volume_to_add_oz=oz_per_10k,
        stage_note=stage_note
    )
