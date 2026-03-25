"""Frequency allocation and band routes."""
from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from data.freq_bands import BANDS, LICENSE_CLASSES, ISM_BANDS
from models.schemas import FrequencyInfo, BandInfo

router = APIRouter(prefix="/api/v1", tags=["frequency"])


def find_band_for_freq(mhz: float) -> Optional[tuple[str, dict]]:
    """Find which amateur band contains the given frequency."""
    for band_key, band_data in BANDS.items():
        if band_data["start_mhz"] <= mhz <= band_data["end_mhz"]:
            return band_key, band_data
    return None


def get_power_limit(mhz: float, license_class: str) -> float:
    """Return max power limit in watts for a frequency and license class."""
    if mhz >= 420.0:
        return 1500.0  # UHF
    elif mhz >= 144.0:
        return 1500.0  # VHF
    elif mhz >= 50.0:
        return 1500.0  # 6m
    elif mhz >= 29.7:
        return 200.0  # 10m
    elif mhz >= 21.0:
        return 200.0  # 15m
    elif mhz >= 14.0:
        return 200.0  # 20m
    elif mhz >= 7.0:
        return 200.0  # 40m
    elif mhz >= 3.5:
        return 200.0  # 80m
    else:
        return 100.0  # 160m


@router.get("/frequency/{mhz}", response_model=FrequencyInfo)
async def get_frequency(mhz: float):
    """Look up frequency details, band, and power limits."""
    if mhz <= 0 or mhz > 13000:
        raise HTTPException(status_code=400, detail="Frequency out of supported range")

    result = find_band_for_freq(mhz)

    if result:
        band_key, band_data = result
        alloc = band_data["allocations"]["usa"]
        return FrequencyInfo(
            mhz=mhz,
            band=band_key,
            band_name=band_data["name"],
            allocation_type=alloc["type"],
            license_class="General",
            power_limit_w=get_power_limit(mhz, "General"),
            notes=f"Part 97 amateur service. {alloc['type']}.",
        )

    # Not in amateur bands
    return FrequencyInfo(
        mhz=mhz,
        band=None,
        band_name=None,
        allocation_type="Non-Amateur",
        license_class="N/A",
        power_limit_w=0.0,
        notes="Not within amateur radio bands.",
    )


@router.get("/bands/amateur", response_model=list[BandInfo])
async def get_amateur_bands():
    """Get the full amateur band chart by license class."""
    result = []
    for band_key, band_data in BANDS.items():
        alloc = band_data["allocations"]["usa"]
        result.append(BandInfo(
            band=band_key,
            name=band_data["name"],
            start_mhz=band_data["start_mhz"],
            end_mhz=band_data["end_mhz"],
            allocation_type=alloc["type"],
            privileges={cls: alloc["privileges"].get(cls, []) for cls in LICENSE_CLASSES},
        ))
    return result


@router.post("/interference/check")
async def check_interference(
    mhz: float = Query(...),
    location: str = Query(...),
):
    """Check for potential interference sources at a frequency and location."""
    sources = []

    # Check ISM band overlap
    for ism in ISM_BANDS:
        if ism["start_mhz"] <= mhz <= ism["end_mhz"]:
            sources.append({
                "type": "ISM Band",
                "name": ism["name"],
                "description": "Unlicensed ISM equipment may cause interference",
                "severity": "Medium",
            })

    # Check FM broadcast overlap (88-108 MHz)
    if 88.0 <= mhz <= 108.0:
        sources.append({
            "type": "FM Broadcast",
            "name": "FM Broadcast Band",
            "description": "Commercial FM broadcast. High-power transmitters.",
            "severity": "High",
        })

    # Check aviation (108-137 MHz)
    if 108.0 <= mhz <= 137.0:
        sources.append({
            "type": "Aviation",
            "name": "Airband",
            "description": "Aviation communications. Protected band.",
            "severity": "Critical",
        })

    # Check cellular (698-806 MHz)
    if 698.0 <= mhz <= 806.0:
        sources.append({
            "type": "Commercial Cellular",
            "name": "700 MHz Cellular",
            "description": "LTE/5G cellular service. Potential interference.",
            "severity": "Medium",
        })

    # Amateur-specific advice
    if 144.0 <= mhz <= 148.0:
        sources.append({
            "type": "Amateur Satellite",
            "name": "UoSAT Oscar",
            "description": "Satellite downlinks active in this band.",
            "severity": "Low",
        })

    if not sources:
        sources.append({
            "type": "None Identified",
            "name": "Clear Frequency",
            "description": "No common interference sources identified.",
            "severity": "None",
        })

    advice = (
        "Use FM for local simplex. Use SSB/CW for weak-signal modes. "
        "Consider a bandpass filter if interference persists."
    )
    if any(s["severity"] in ("High", "Critical") for s in sources):
        advice = (
            "WARNING: This frequency is shared with high-power licensed services. "
            "Amateur operation is secondary and must not cause interference."
        )

    return {
        "mhz": mhz,
        "location": location,
        "interference_sources": sources,
        "advice": advice,
    }
