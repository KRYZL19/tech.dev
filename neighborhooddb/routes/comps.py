from fastapi import APIRouter, HTTPException, Query
from models.schemas import CompsResponse, TrendResponse, TrendPoint, InvestmentScoreRequest, InvestmentScoreResponse
from data.demographic_index import get_zipcode_data, generate_historical_data

router = APIRouter(prefix="/api/v1", tags=["comps"])


@router.get("/comps/{zipcode}", response_model=CompsResponse)
def get_comps(zipcode: str):
    """Get real estate comps data for a zipcode."""
    data = get_zipcode_data(zipcode)
    if not data:
        raise HTTPException(status_code=404, detail=f"Zipcode {zipcode} not found in database")
    
    return CompsResponse(
        zipcode=zipcode,
        median_home_price=data["median_home_price"],
        median_rent_monthly=data["median_rent"],
        price_per_sqft=data["price_per_sqft"],
        days_on_market_avg=data["days_on_market"],
        inventory_months=data["inventory_months"],
        year_over_year_change_pct=data["yoy_change"]
    )


@router.get("/trend/{zipcode}", response_model=TrendResponse)
def get_trend(zipcode: str, years: int = Query(default=5, ge=1, le=20)):
    """Get historical price trend for a zipcode."""
    data = get_zipcode_data(zipcode)
    if not data:
        raise HTTPException(status_code=404, detail=f"Zipcode {zipcode} not found in database")
    
    historical = generate_historical_data(zipcode, years)
    
    appreciation_avg = sum(p["appreciation_rate"] for p in historical) / len(historical) if historical else 0
    annual_rent = data["median_rent"] * 12
    rental_yield = (annual_rent / data["median_home_price"]) * 100 if data["median_home_price"] > 0 else 0
    
    return TrendResponse(
        zipcode=zipcode,
        years_requested=years,
        historical_data=[TrendPoint(**p) for p in historical],
        appreciation_rate_avg=round(appreciation_avg, 2),
        rental_yield=round(rental_yield, 2)
    )


@router.post("/investment/score", response_model=InvestmentScoreResponse)
def get_investment_score(request: InvestmentScoreRequest):
    """Calculate investment score for a property."""
    data = get_zipcode_data(request.zipcode)
    if not data:
        raise HTTPException(status_code=404, detail=f"Zipcode {request.zipcode} not found in database")
    
    # Calculate investment metrics
    annual_rent = data["median_rent"] * 12
    annual_expenses_pct = 0.35  # 35% for taxes, insurance, maintenance, vacancy
    annual_expenses = request.purchase_price * annual_expenses_pct
    noi = annual_rent - annual_expenses
    
    cap_rate = (noi / request.purchase_price) * 100 if request.purchase_price > 0 else 0
    
    down_payment = request.purchase_price * (request.down_payment_pct / 100)
    loan_amount = request.purchase_price - down_payment
    # Simplified: 7% interest, 30-year amortization
    if loan_amount > 0:
        monthly_rate = 0.07 / 12
        num_payments = 360
        monthly_mortgage = loan_amount * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
        annual_debt_service = monthly_mortgage * 12
    else:
        annual_debt_service = 0
    
    annual_cash_flow = noi - annual_debt_service
    cash_on_cash = (annual_cash_flow / down_payment) * 100 if down_payment > 0 else 0
    
    break_even_rent = int((annual_expenses + annual_debt_service) / 12)
    
    # Vacancy assumption based on days on market
    vacancy_rate = min((data["days_on_market"] / 365) * 100, 15)
    
    return InvestmentScoreResponse(
        zipcode=request.zipcode,
        purchase_price=request.purchase_price,
        down_payment_pct=request.down_payment_pct,
        cap_rate=round(cap_rate, 2),
        cash_on_cash_return=round(cash_on_cash, 2),
        break_even_rent=break_even_rent,
        vacancy_rate_assumption=round(vacancy_rate, 1)
    )
