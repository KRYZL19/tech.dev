from pydantic import BaseModel
from typing import Optional


class DemographicsResponse(BaseModel):
    zipcode: str
    population: int
    median_age: float
    median_income: int
    housing_ownership_rate: float
    school_rating_out_of_10: float
    crime_index: float


class CompsResponse(BaseModel):
    zipcode: str
    median_home_price: int
    median_rent_monthly: int
    price_per_sqft: float
    days_on_market_avg: int
    inventory_months: float
    year_over_year_change_pct: float


class TrendPoint(BaseModel):
    year: int
    median_price: int
    appreciation_rate: float


class TrendResponse(BaseModel):
    zipcode: str
    years_requested: int
    historical_data: list[TrendPoint]
    appreciation_rate_avg: float
    rental_yield: float


class InvestmentScoreRequest(BaseModel):
    zipcode: str
    purchase_price: int
    down_payment_pct: float


class InvestmentScoreResponse(BaseModel):
    zipcode: str
    purchase_price: int
    down_payment_pct: float
    cap_rate: float
    cash_on_cash_return: float
    break_even_rent: int
    vacancy_rate_assumption: float
