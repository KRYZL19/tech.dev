from fastapi import APIRouter, HTTPException
from models.schemas import DemographicsResponse
from data.demographic_index import get_zipcode_data

router = APIRouter(prefix="/api/v1", tags=["demographics"])


@router.get("/demographics/{zipcode}", response_model=DemographicsResponse)
def get_demographics(zipcode: str):
    """Get demographic data for a zipcode."""
    data = get_zipcode_data(zipcode)
    if not data:
        raise HTTPException(status_code=404, detail=f"Zipcode {zipcode} not found in database")
    
    return DemographicsResponse(
        zipcode=zipcode,
        population=data["population"],
        median_age=data["median_age"],
        median_income=data["median_income"],
        housing_ownership_rate=data["housing_ownership_rate"],
        school_rating_out_of_10=data["school_rating"],
        crime_index=data["crime_index"]
    )
