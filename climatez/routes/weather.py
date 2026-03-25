"""Weather routes for CLIMATEZ API."""

from datetime import datetime
from fastapi import APIRouter, HTTPException, status

from data.climate_normals import get_city_data
from models.schemas import (
    ClimateNormalsResponse,
    FrostDatesResponse,
    PrecipitationResponse,
    MonthlyPrecipitation,
)


router = APIRouter(prefix="/api/v1", tags=["weather"])


def _parse_frost_date(date_str: str | None) -> int | None:
    """Parse frost date string (MM-DD) to day of year."""
    if date_str is None:
        return None
    try:
        month, day = date_str.split("-")
        dt = datetime.strptime(f"2024-{month}-{day}", "%Y-%m-%d")
        return dt.timetuple().tm_yday
    except (ValueError, AttributeError):
        return None


def _day_of_year_to_mmdd(doy: int) -> str:
    """Convert day of year to MM-DD format."""
    dt = datetime.strptime(f"2024-{doy}", "%Y-%j")
    return dt.strftime("%m-%d")


def _calculate_growing_season(last_frost: int | None, first_frost: int | None) -> int:
    """Calculate growing season days from frost day-of-year values."""
    if last_frost is None or first_frost is None:
        return 365 if (last_frost is None and first_frost is None) else 0
    if first_frost < last_frost:
        return 0
    return first_frost - last_frost


@router.get("/normals/{zipcode}", response_model=ClimateNormalsResponse)
async def get_climate_normals(zipcode: str):
    """Get 30-year climate normals for a zip code.
    
    Returns heating/cooling degree days, growing season length,
    average precipitation, snowfall, and humidity.
    """
    if len(zipcode) != 5 or not zipcode.isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Zip code must be 5 digits"
        )
    
    data = get_city_data(zipcode)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No climate data found for zip code {zipcode}"
        )
    
    return ClimateNormalsResponse(
        zipcode=zipcode,
        city=data["city"],
        state=data["state"],
        lat=data["lat"],
        lon=data["lon"],
        heating_dd=data["heating_dd"],
        cooling_dd=data["cooling_dd"],
        growing_days=data["growing_days"],
        avg_precip_inches=data["avg_precip_inches"],
        avg_snow_inches=data["avg_snow_inches"],
        humidity_pct=data["humidity_pct"],
    )


@router.get("/frost-dates/{zipcode}", response_model=FrostDatesResponse)
async def get_frost_dates(zipcode: str):
    """Get frost date history for a zip code.
    
    Returns average last spring frost, first fall frost,
    and total growing season days.
    """
    if len(zipcode) != 5 or not zipcode.isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Zip code must be 5 digits"
        )
    
    data = get_city_data(zipcode)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No climate data found for zip code {zipcode}"
        )
    
    last_spring = data["last_spring_frost"]
    first_fall = data["first_fall_frost"]
    
    last_spring_doy = _parse_frost_date(last_spring)
    first_fall_doy = _parse_frost_date(first_fall)
    
    growing_days = _calculate_growing_season(last_spring_doy, first_fall_doy)
    
    return FrostDatesResponse(
        zipcode=zipcode,
        city=data["city"],
        state=data["state"],
        avg_last_spring_frost=last_spring,
        avg_first_fall_frost=first_fall,
        growing_season_days=growing_days,
        has_frost=last_spring is not None,
    )


@router.get("/precipitation/{zipcode}/annual", response_model=PrecipitationResponse)
async def get_annual_precipitation(zipcode: str):
    """Get monthly precipitation averages for a zip code.
    
    Returns monthly breakdown with wettest and driest months.
    """
    if len(zipcode) != 5 or not zipcode.isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Zip code must be 5 digits"
        )
    
    data = get_city_data(zipcode)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No climate data found for zip code {zipcode}"
        )
    
    monthly_data = data["monthly_precip"]
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    monthly = [
        MonthlyPrecipitation(
            month=i + 1,
            month_name=month_names[i],
            precip_inches=monthly_data[i]
        )
        for i in range(12)
    ]
    
    max_precip = max(monthly_data)
    min_precip = min(monthly_data)
    wettest_idx = monthly_data.index(max_precip)
    driest_idx = monthly_data.index(min_precip)
    
    return PrecipitationResponse(
        zipcode=zipcode,
        city=data["city"],
        state=data["state"],
        annual_total_inches=sum(monthly_data),
        monthly=monthly,
        wettest_month=month_names[wettest_idx],
        wettest_inches=max_precip,
        driest_month=month_names[driest_idx],
        driest_inches=min_precip,
    )
