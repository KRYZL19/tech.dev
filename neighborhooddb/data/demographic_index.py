"""
Demographic index for 100 zip codes across major metros.
Data is realistic but synthetic for demonstration.
"""

ZIPCODE_DATA = {
    # NYC Metro
    "10001": {"metro": "NYC", "population": 26500, "median_age": 35.2, "median_income": 125000, "housing_ownership_rate": 0.28, "school_rating": 7.2, "crime_index": 45.0, "median_home_price": 850000, "median_rent": 3200, "price_per_sqft": 950, "days_on_market": 45, "inventory_months": 3.2, "yoy_change": 5.2},
    "10002": {"metro": "NYC", "population": 82000, "median_age": 34.1, "median_income": 52000, "housing_ownership_rate": 0.22, "school_rating": 6.1, "crime_index": 52.0, "median_home_price": 720000, "median_rent": 2800, "price_per_sqft": 820, "days_on_market": 38, "inventory_months": 2.8, "yoy_change": 4.8},
    "10003": {"metro": "NYC", "population": 56000, "median_age": 33.5, "median_income": 115000, "housing_ownership_rate": 0.30, "school_rating": 7.5, "crime_index": 38.0, "median_home_price": 920000, "median_rent": 3500, "price_per_sqft": 1050, "days_on_market": 42, "inventory_months": 3.0, "yoy_change": 5.5},
    "10004": {"metro": "NYC", "population": 3200, "median_age": 42.0, "median_income": 225000, "housing_ownership_rate": 0.45, "school_rating": 8.5, "crime_index": 28.0, "median_home_price": 1800000, "median_rent": 5500, "price_per_sqft": 1400, "days_on_market": 65, "inventory_months": 4.5, "yoy_change": 6.2},
    "10010": {"metro": "NYC", "population": 30000, "median_age": 36.8, "median_income": 142000, "housing_ownership_rate": 0.35, "school_rating": 7.8, "crime_index": 32.0, "median_home_price": 1050000, "median_rent": 3800, "price_per_sqft": 1100, "days_on_market": 40, "inventory_months": 3.1, "yoy_change": 5.8},
    "10011": {"metro": "NYC", "population": 52000, "median_age": 37.2, "median_income": 165000, "housing_ownership_rate": 0.38, "school_rating": 8.0, "crime_index": 30.0, "median_home_price": 1350000, "median_rent": 4200, "price_per_sqft": 1200, "days_on_market": 48, "inventory_months": 3.5, "yoy_change": 6.0},
    "11201": {"metro": "NYC", "population": 56000, "median_age": 35.5, "median_income": 135000, "housing_ownership_rate": 0.40, "school_rating": 7.6, "crime_index": 35.0, "median_home_price": 950000, "median_rent": 3400, "price_per_sqft": 980, "days_on_market": 44, "inventory_months": 3.3, "yoy_change": 5.4},
    "11211": {"metro": "NYC", "population": 85000, "median_age": 32.0, "median_income": 78000, "housing_ownership_rate": 0.25, "school_rating": 6.5, "crime_index": 48.0, "median_home_price": 780000, "median_rent": 2900, "price_per_sqft": 850, "days_on_market": 35, "inventory_months": 2.5, "yoy_change": 7.2},
    "11215": {"metro": "NYC", "population": 67000, "median_age": 34.5, "median_income": 118000, "housing_ownership_rate": 0.42, "school_rating": 7.4, "crime_index": 36.0, "median_home_price": 890000, "median_rent": 3100, "price_per_sqft": 920, "days_on_market": 41, "inventory_months": 3.0, "yoy_change": 5.6},
    "11377": {"metro": "NYC", "population": 89000, "median_age": 36.2, "median_income": 62000, "housing_ownership_rate": 0.35, "school_rating": 6.8, "crime_index": 42.0, "median_home_price": 580000, "median_rent": 2400, "price_per_sqft": 620, "days_on_market": 50, "inventory_months": 3.8, "yoy_change": 4.2},

    # LA Metro
    "90001": {"metro": "LA", "population": 92000, "median_age": 29.5, "median_income": 48000, "housing_ownership_rate": 0.38, "school_rating": 5.8, "crime_index": 62.0, "median_home_price": 520000, "median_rent": 2100, "price_per_sqft": 420, "days_on_market": 55, "inventory_months": 4.2, "yoy_change": 3.8},
    "90012": {"metro": "LA", "population": 35000, "median_age": 38.0, "median_income": 58000, "housing_ownership_rate": 0.32, "school_rating": 6.2, "crime_index": 58.0, "median_home_price": 620000, "median_rent": 2500, "price_per_sqft": 510, "days_on_market": 48, "inventory_months": 3.5, "yoy_change": 4.1},
    "90024": {"metro": "LA", "population": 12000, "median_age": 42.5, "median_income": 185000, "housing_ownership_rate": 0.35, "school_rating": 8.8, "crime_index": 25.0, "median_home_price": 1650000, "median_rent": 4800, "price_per_sqft": 1150, "days_on_market": 72, "inventory_months": 5.5, "yoy_change": 6.5},
    "90028": {"metro": "LA", "population": 28000, "median_age": 34.0, "median_income": 72000, "housing_ownership_rate": 0.18, "school_rating": 5.5, "crime_index": 68.0, "median_home_price": 680000, "median_rent": 2700, "price_per_sqft": 680, "days_on_market": 42, "inventory_months": 3.2, "yoy_change": 4.5},
    "90034": {"metro": "LA", "population": 58000, "median_age": 35.8, "median_income": 98000, "housing_ownership_rate": 0.30, "school_rating": 6.8, "crime_index": 45.0, "median_home_price": 850000, "median_rent": 3100, "price_per_sqft": 780, "days_on_market": 38, "inventory_months": 2.8, "yoy_change": 5.2},
    "90046": {"metro": "LA", "population": 45000, "median_age": 36.5, "median_income": 88000, "housing_ownership_rate": 0.28, "school_rating": 6.5, "crime_index": 52.0, "median_home_price": 790000, "median_rent": 2950, "price_per_sqft": 720, "days_on_market": 40, "inventory_months": 3.0, "yoy_change": 4.8},
    "90210": {"metro": "LA", "population": 22000, "median_age": 44.0, "median_income": 320000, "housing_ownership_rate": 0.65, "school_rating": 9.2, "crime_index": 18.0, "median_home_price": 4200000, "median_rent": 12000, "price_per_sqft": 2200, "days_on_market": 95, "inventory_months": 8.0, "yoy_change": 7.5},
    "90402": {"metro": "LA", "population": 8500, "median_age": 43.5, "median_income": 245000, "housing_ownership_rate": 0.55, "school_rating": 8.8, "crime_index": 22.0, "median_home_price": 2800000, "median_rent": 8500, "price_per_sqft": 1800, "days_on_market": 85, "inventory_months": 7.2, "yoy_change": 6.8},
    "90405": {"metro": "LA", "population": 27000, "median_age": 37.2, "median_income": 105000, "housing_ownership_rate": 0.35, "school_rating": 7.2, "crime_index": 40.0, "median_home_price": 920000, "median_rent": 3400, "price_per_sqft": 850, "days_on_market": 44, "inventory_months": 3.4, "yoy_change": 5.3},
    "90401": {"metro": "LA", "population": 12000, "median_age": 39.0, "median_income": 135000, "housing_ownership_rate": 0.42, "school_rating": 7.5, "crime_index": 35.0, "median_home_price": 1100000, "median_rent": 3900, "price_per_sqft": 950, "days_on_market": 50, "inventory_months": 3.8, "yoy_change": 5.7},

    # Chicago Metro
    "60601": {"metro": "Chicago", "population": 32000, "median_age": 38.5, "median_income": 135000, "housing_ownership_rate": 0.38, "school_rating": 7.8, "crime_index": 32.0, "median_home_price": 520000, "median_rent": 2800, "price_per_sqft": 420, "days_on_market": 55, "inventory_months": 4.0, "yoy_change": 3.5},
    "60602": {"metro": "Chicago", "population": 15000, "median_age": 40.0, "median_income": 148000, "housing_ownership_rate": 0.42, "school_rating": 8.0, "crime_index": 28.0, "median_home_price": 580000, "median_rent": 3100, "price_per_sqft": 460, "days_on_market": 52, "inventory_months": 3.8, "yoy_change": 3.8},
    "60611": {"metro": "Chicago", "population": 28000, "median_age": 39.2, "median_income": 155000, "housing_ownership_rate": 0.40, "school_rating": 8.2, "crime_index": 30.0, "median_home_price": 620000, "median_rent": 3400, "price_per_sqft": 480, "days_on_market": 48, "inventory_months": 3.5, "yoy_change": 4.0},
    "60614": {"metro": "Chicago", "population": 45000, "median_age": 35.0, "median_income": 125000, "housing_ownership_rate": 0.45, "school_rating": 7.6, "crime_index": 35.0, "median_home_price": 550000, "median_rent": 2700, "price_per_sqft": 430, "days_on_market": 42, "inventory_months": 3.0, "yoy_change": 3.6},
    "60622": {"metro": "Chicago", "population": 52000, "median_age": 32.0, "median_income": 92000, "housing_ownership_rate": 0.38, "school_rating": 6.8, "crime_index": 48.0, "median_home_price": 420000, "median_rent": 2200, "price_per_sqft": 380, "days_on_market": 38, "inventory_months": 2.8, "yoy_change": 4.2},
    "60647": {"metro": "Chicago", "population": 78000, "median_age": 31.5, "median_income": 85000, "housing_ownership_rate": 0.32, "school_rating": 6.2, "crime_index": 52.0, "median_home_price": 380000, "median_rent": 2000, "price_per_sqft": 350, "days_on_market": 35, "inventory_months": 2.5, "yoy_change": 4.5},
    "60657": {"metro": "Chicago", "population": 65000, "median_age": 34.0, "median_income": 115000, "housing_ownership_rate": 0.42, "school_rating": 7.2, "crime_index": 38.0, "median_home_price": 480000, "median_rent": 2500, "price_per_sqft": 400, "days_on_market": 40, "inventory_months": 2.9, "yoy_change": 3.9},
    "60610": {"metro": "Chicago", "population": 42000, "median_age": 36.5, "median_income": 142000, "housing_ownership_rate": 0.40, "school_rating": 7.5, "crime_index": 34.0, "median_home_price": 560000, "median_rent": 2900, "price_per_sqft": 440, "days_on_market": 45, "inventory_months": 3.2, "yoy_change": 3.7},
    "60201": {"metro": "Chicago", "population": 38000, "median_age": 33.0, "median_income": 138000, "housing_ownership_rate": 0.48, "school_rating": 8.5, "crime_index": 25.0, "median_home_price": 620000, "median_rent": 3200, "price_per_sqft": 460, "days_on_market": 50, "inventory_months": 3.6, "yoy_change": 4.1},
    "60615": {"metro": "Chicago", "population": 48000, "median_age": 28.0, "median_income": 72000, "housing_ownership_rate": 0.30, "school_rating": 6.5, "crime_index": 55.0, "median_home_price": 320000, "median_rent": 1800, "price_per_sqft": 290, "days_on_market": 60, "inventory_months": 4.5, "yoy_change": 2.8},

    # Houston Metro
    "77001": {"metro": "Houston", "population": 42000, "median_age": 30.5, "median_income": 52000, "housing_ownership_rate": 0.42, "school_rating": 5.8, "crime_index": 58.0, "median_home_price": 280000, "median_rent": 1600, "price_per_sqft": 180, "days_on_market": 65, "inventory_months": 4.8, "yoy_change": 4.2},
    "77002": {"metro": "Houston", "population": 18000, "median_age": 38.0, "median_income": 125000, "housing_ownership_rate": 0.35, "school_rating": 7.2, "crime_index": 42.0, "median_home_price": 420000, "median_rent": 2400, "price_per_sqft": 320, "days_on_market": 55, "inventory_months": 4.0, "yoy_change": 4.8},
    "77004": {"metro": "Houston", "population": 32000, "median_age": 32.0, "median_income": 68000, "housing_ownership_rate": 0.38, "school_rating": 6.0, "crime_index": 55.0, "median_home_price": 310000, "median_rent": 1800, "price_per_sqft": 220, "days_on_market": 58, "inventory_months": 4.2, "yoy_change": 4.0},
    "77005": {"metro": "Houston", "population": 25000, "median_age": 35.5, "median_income": 155000, "housing_ownership_rate": 0.52, "school_rating": 8.0, "crime_index": 30.0, "median_home_price": 580000, "median_rent": 2900, "price_per_sqft": 380, "days_on_market": 48, "inventory_months": 3.5, "yoy_change": 5.5},
    "77006": {"metro": "Houston", "population": 28000, "median_age": 34.0, "median_income": 138000, "housing_ownership_rate": 0.40, "school_rating": 7.5, "crime_index": 38.0, "median_home_price": 520000, "median_rent": 2700, "price_per_sqft": 360, "days_on_market": 45, "inventory_months": 3.2, "yoy_change": 5.2},
    "77007": {"metro": "Houston", "population": 38000, "median_age": 35.0, "median_income": 125000, "housing_ownership_rate": 0.45, "school_rating": 7.3, "crime_index": 36.0, "median_home_price": 480000, "median_rent": 2600, "price_per_sqft": 340, "days_on_market": 42, "inventory_months": 3.0, "yoy_change": 5.0},
    "77008": {"metro": "Houston", "population": 45000, "median_age": 33.5, "median_income": 95000, "housing_ownership_rate": 0.48, "school_rating": 6.8, "crime_index": 44.0, "median_home_price": 380000, "median_rent": 2100, "price_per_sqft": 280, "days_on_market": 50, "inventory_months": 3.6, "yoy_change": 4.6},
    "77024": {"metro": "Houston", "population": 35000, "median_age": 40.0, "median_income": 175000, "housing_ownership_rate": 0.58, "school_rating": 8.2, "crime_index": 28.0, "median_home_price": 720000, "median_rent": 3500, "price_per_sqft": 420, "days_on_market": 55, "inventory_months": 4.0, "yoy_change": 5.8},
    "77027": {"metro": "Houston", "population": 15000, "median_age": 42.0, "median_income": 195000, "housing_ownership_rate": 0.50, "school_rating": 8.5, "crime_index": 26.0, "median_home_price": 850000, "median_rent": 4200, "price_per_sqft": 480, "days_on_market": 62, "inventory_months": 4.5, "yoy_change": 6.2},
    "77094": {"metro": "Houston", "population": 12000, "median_age": 36.0, "median_income": 145000, "housing_ownership_rate": 0.55, "school_rating": 7.8, "crime_index": 32.0, "median_home_price": 620000, "median_rent": 3100, "price_per_sqft": 380, "days_on_market": 52, "inventory_months": 3.8, "yoy_change": 5.4},

    # Phoenix Metro
    "85001": {"metro": "Phoenix", "population": 48000, "median_age": 32.0, "median_income": 52000, "housing_ownership_rate": 0.45, "school_rating": 5.5, "crime_index": 58.0, "median_home_price": 320000, "median_rent": 1700, "price_per_sqft": 240, "days_on_market": 45, "inventory_months": 3.5, "yoy_change": 5.2},
    "85003": {"metro": "Phoenix", "population": 42000, "median_age": 30.0, "median_income": 48000, "housing_ownership_rate": 0.40, "school_rating": 5.2, "crime_index": 65.0, "median_home_price": 280000, "median_rent": 1500, "price_per_sqft": 210, "days_on_market": 50, "inventory_months": 3.8, "yoy_change": 4.8},
    "85004": {"metro": "Phoenix", "population": 18000, "median_age": 38.5, "median_income": 85000, "housing_ownership_rate": 0.32, "school_rating": 6.5, "crime_index": 55.0, "median_home_price": 380000, "median_rent": 1900, "price_per_sqft": 280, "days_on_market": 48, "inventory_months": 3.5, "yoy_change": 5.0},
    "85006": {"metro": "Phoenix", "population": 52000, "median_age": 31.0, "median_income": 55000, "housing_ownership_rate": 0.42, "school_rating": 5.8, "crime_index": 60.0, "median_home_price": 310000, "median_rent": 1650, "price_per_sqft": 230, "days_on_market": 42, "inventory_months": 3.2, "yoy_change": 5.5},
    "85007": {"metro": "Phoenix", "population": 35000, "median_age": 32.5, "median_income": 50000, "housing_ownership_rate": 0.38, "school_rating": 5.5, "crime_index": 62.0, "median_home_price": 290000, "median_rent": 1550, "price_per_sqft": 220, "days_on_market": 48, "inventory_months": 3.6, "yoy_change": 4.9},
    "85012": {"metro": "Phoenix", "population": 22000, "median_age": 40.0, "median_income": 92000, "housing_ownership_rate": 0.35, "school_rating": 7.0, "crime_index": 48.0, "median_home_price": 420000, "median_rent": 2100, "price_per_sqft": 310, "days_on_market": 52, "inventory_months": 3.8, "yoy_change": 5.1},
    "85013": {"metro": "Phoenix", "population": 38000, "median_age": 34.0, "median_income": 72000, "housing_ownership_rate": 0.40, "school_rating": 6.2, "crime_index": 52.0, "median_home_price": 350000, "median_rent": 1850, "price_per_sqft": 265, "days_on_market": 46, "inventory_months": 3.4, "yoy_change": 5.3},
    "85016": {"metro": "Phoenix", "population": 45000, "median_age": 36.0, "median_income": 82000, "housing_ownership_rate": 0.48, "school_rating": 6.5, "crime_index": 46.0, "median_home_price": 380000, "median_rent": 2000, "price_per_sqft": 280, "days_on_market": 44, "inventory_months": 3.2, "yoy_change": 5.4},
    "85020": {"metro": "Phoenix", "population": 52000, "median_age": 35.5, "median_income": 78000, "housing_ownership_rate": 0.50, "school_rating": 6.8, "crime_index": 44.0, "median_home_price": 360000, "median_rent": 1900, "price_per_sqft": 270, "days_on_market": 42, "inventory_months": 3.0, "yoy_change": 5.6},
    "85021": {"metro": "Phoenix", "population": 58000, "median_age": 34.5, "median_income": 68000, "housing_ownership_rate": 0.45, "school_rating": 6.0, "crime_index": 50.0, "median_home_price": 340000, "median_rent": 1800, "price_per_sqft": 255, "days_on_market": 44, "inventory_months": 3.2, "yoy_change": 5.2},

    # Austin Metro
    "78701": {"metro": "Austin", "population": 28000, "median_age": 35.0, "median_income": 145000, "housing_ownership_rate": 0.38, "school_rating": 7.8, "crime_index": 35.0, "median_home_price": 620000, "median_rent": 2800, "price_per_sqft": 480, "days_on_market": 35, "inventory_months": 2.5, "yoy_change": 8.5},
    "78702": {"metro": "Austin", "population": 42000, "median_age": 32.0, "median_income": 85000, "housing_ownership_rate": 0.42, "school_rating": 6.5, "crime_index": 48.0, "median_home_price": 480000, "median_rent": 2200, "price_per_sqft": 420, "days_on_market": 32, "inventory_months": 2.2, "yoy_change": 9.2},
    "78703": {"metro": "Austin", "population": 35000, "median_age": 38.0, "median_income": 165000, "housing_ownership_rate": 0.50, "school_rating": 8.5, "crime_index": 28.0, "median_home_price": 780000, "median_rent": 3400, "price_per_sqft": 560, "days_on_market": 38, "inventory_months": 2.8, "yoy_change": 7.8},
    "78704": {"metro": "Austin", "population": 48000, "median_age": 34.0, "median_income": 125000, "housing_ownership_rate": 0.45, "school_rating": 7.2, "crime_index": 38.0, "median_home_price": 580000, "median_rent": 2600, "price_per_sqft": 460, "days_on_market": 34, "inventory_months": 2.4, "yoy_change": 8.8},
    "78705": {"metro": "Austin", "population": 22000, "median_age": 24.0, "median_income": 45000, "housing_ownership_rate": 0.15, "school_rating": 7.0, "crime_index": 42.0, "median_home_price": 420000, "median_rent": 2000, "price_per_sqft": 400, "days_on_market": 30, "inventory_months": 2.0, "yoy_change": 10.5},
    "78717": {"metro": "Austin", "population": 32000, "median_age": 36.5, "median_income": 138000, "housing_ownership_rate": 0.55, "school_rating": 8.0, "crime_index": 30.0, "median_home_price": 550000, "median_rent": 2500, "price_per_sqft": 420, "days_on_market": 36, "inventory_months": 2.6, "yoy_change": 8.2},
    "78731": {"metro": "Austin", "population": 28000, "median_age": 42.0, "median_income": 185000, "housing_ownership_rate": 0.60, "school_rating": 8.8, "crime_index": 25.0, "median_home_price": 850000, "median_rent": 3800, "price_per_sqft": 520, "days_on_market": 42, "inventory_months": 3.0, "yoy_change": 7.5},
    "78741": {"metro": "Austin", "population": 58000, "median_age": 30.0, "median_income": 72000, "housing_ownership_rate": 0.35, "school_rating": 6.0, "crime_index": 52.0, "median_home_price": 380000, "median_rent": 1850, "price_per_sqft": 340, "days_on_market": 28, "inventory_months": 1.8, "yoy_change": 11.2},
    "78745": {"metro": "Austin", "population": 62000, "median_age": 33.0, "median_income": 92000, "housing_ownership_rate": 0.48, "school_rating": 6.8, "crime_index": 42.0, "median_home_price": 420000, "median_rent": 2050, "price_per_sqft": 360, "days_on_market": 30, "inventory_months": 2.0, "yoy_change": 9.5},
    "78758": {"metro": "Austin", "population": 52000, "median_age": 32.5, "median_income": 82000, "housing_ownership_rate": 0.42, "school_rating": 6.5, "crime_index": 46.0, "median_home_price": 390000, "median_rent": 1950, "price_per_sqft": 330, "days_on_market": 32, "inventory_months": 2.2, "yoy_change": 9.8},

    # Denver Metro
    "80202": {"metro": "Denver", "population": 22000, "median_age": 38.0, "median_income": 135000, "housing_ownership_rate": 0.35, "school_rating": 7.5, "crime_index": 42.0, "median_home_price": 580000, "median_rent": 2700, "price_per_sqft": 480, "days_on_market": 40, "inventory_months": 2.8, "yoy_change": 6.2},
    "80203": {"metro": "Denver", "population": 32000, "median_age": 34.0, "median_income": 98000, "housing_ownership_rate": 0.28, "school_rating": 6.8, "crime_index": 52.0, "median_home_price": 480000, "median_rent": 2300, "price_per_sqft": 420, "days_on_market": 35, "inventory_months": 2.4, "yoy_change": 7.0},
    "80204": {"metro": "Denver", "population": 45000, "median_age": 32.0, "median_income": 72000, "housing_ownership_rate": 0.35, "school_rating": 6.0, "crime_index": 58.0, "median_home_price": 420000, "median_rent": 2050, "price_per_sqft": 380, "days_on_market": 32, "inventory_months": 2.2, "yoy_change": 7.5},
    "80205": {"metro": "Denver", "population": 38000, "median_age": 33.5, "median_income": 88000, "housing_ownership_rate": 0.40, "school_rating": 6.5, "crime_index": 50.0, "median_home_price": 450000, "median_rent": 2200, "price_per_sqft": 400, "days_on_market": 34, "inventory_months": 2.4, "yoy_change": 7.2},
    "80206": {"metro": "Denver", "population": 28000, "median_age": 42.0, "median_income": 185000, "housing_ownership_rate": 0.55, "school_rating": 8.5, "crime_index": 28.0, "median_home_price": 920000, "median_rent": 3800, "price_per_sqft": 580, "days_on_market": 48, "inventory_months": 3.5, "yoy_change": 5.8},
    "80209": {"metro": "Denver", "population": 35000, "median_age": 38.5, "median_income": 145000, "housing_ownership_rate": 0.52, "school_rating": 7.8, "crime_index": 32.0, "median_home_price": 680000, "median_rent": 3000, "price_per_sqft": 500, "days_on_market": 42, "inventory_months": 3.0, "yoy_change": 6.5},
    "80210": {"metro": "Denver", "population": 42000, "median_age": 36.0, "median_income": 155000, "housing_ownership_rate": 0.50, "school_rating": 8.2, "crime_index": 30.0, "median_home_price": 750000, "median_rent": 3200, "price_per_sqft": 520, "days_on_market": 44, "inventory_months": 3.2, "yoy_change": 6.8},
    "80211": {"metro": "Denver", "population": 48000, "median_age": 34.5, "median_income": 115000, "housing_ownership_rate": 0.45, "school_rating": 7.0, "crime_index": 40.0, "median_home_price": 550000, "median_rent": 2600, "price_per_sqft": 450, "days_on_market": 38, "inventory_months": 2.6, "yoy_change": 7.2},
    "80212": {"metro": "Denver", "population": 35000, "median_age": 35.5, "median_income": 105000, "housing_ownership_rate": 0.48, "school_rating": 6.8, "crime_index": 42.0, "median_home_price": 520000, "median_rent": 2450, "price_per_sqft": 430, "days_on_market": 36, "inventory_months": 2.5, "yoy_change": 7.4},
    "80301": {"metro": "Denver", "population": 28000, "median_age": 40.0, "median_income": 168000, "housing_ownership_rate": 0.55, "school_rating": 8.8, "crime_index": 25.0, "median_home_price": 820000, "median_rent": 3500, "price_per_sqft": 540, "days_on_market": 46, "inventory_months": 3.4, "yoy_change": 6.0},

    # Seattle Metro
    "98101": {"metro": "Seattle", "population": 25000, "median_age": 38.0, "median_income": 155000, "housing_ownership_rate": 0.32, "school_rating": 8.0, "crime_index": 42.0, "median_home_price": 720000, "median_rent": 3200, "price_per_sqft": 620, "days_on_market": 40, "inventory_months": 2.8, "yoy_change": 5.5},
    "98102": {"metro": "Seattle", "population": 28000, "median_age": 38.5, "median_income": 185000, "housing_ownership_rate": 0.42, "school_rating": 8.5, "crime_index": 32.0, "median_home_price": 920000, "median_rent": 3800, "price_per_sqft": 680, "days_on_market": 45, "inventory_months": 3.2, "yoy_change": 5.2},
    "98103": {"metro": "Seattle", "population": 52000, "median_age": 35.0, "median_income": 145000, "housing_ownership_rate": 0.48, "school_rating": 8.0, "crime_index": 34.0, "median_home_price": 780000, "median_rent": 3100, "price_per_sqft": 600, "days_on_market": 38, "inventory_months": 2.6, "yoy_change": 5.8},
    "98105": {"metro": "Seattle", "population": 45000, "median_age": 34.0, "median_income": 138000, "housing_ownership_rate": 0.45, "school_rating": 8.2, "crime_index": 35.0, "median_home_price": 750000, "median_rent": 3000, "price_per_sqft": 580, "days_on_market": 36, "inventory_months": 2.5, "yoy_change": 6.0},
    "98107": {"metro": "Seattle", "population": 32000, "median_age": 35.5, "median_income": 128000, "housing_ownership_rate": 0.40, "school_rating": 7.5, "crime_index": 38.0, "median_home_price": 680000, "median_rent": 2850, "price_per_sqft": 560, "days_on_market": 34, "inventory_months": 2.4, "yoy_change": 6.2},
    "98109": {"metro": "Seattle", "population": 28000, "median_age": 37.0, "median_income": 165000, "housing_ownership_rate": 0.38, "school_rating": 8.0, "crime_index": 36.0, "median_home_price": 850000, "median_rent": 3500, "price_per_sqft": 640, "days_on_market": 42, "inventory_months": 3.0, "yoy_change": 5.6},
    "98112": {"metro": "Seattle", "population": 22000, "median_age": 42.0, "median_income": 225000, "housing_ownership_rate": 0.58, "school_rating": 9.0, "crime_index": 25.0, "median_home_price": 1200000, "median_rent": 4800, "price_per_sqft": 780, "days_on_market": 55, "inventory_months": 4.0, "yoy_change": 4.8},
    "98115": {"metro": "Seattle", "population": 58000, "median_age": 36.5, "median_income": 152000, "housing_ownership_rate": 0.52, "school_rating": 8.2, "crime_index": 32.0, "median_home_price": 800000, "median_rent": 3300, "price_per_sqft": 610, "days_on_market": 40, "inventory_months": 2.8, "yoy_change": 5.9},
    "98117": {"metro": "Seattle", "population": 48000, "median_age": 35.0, "median_income": 135000, "housing_ownership_rate": 0.50, "school_rating": 7.8, "crime_index": 35.0, "median_home_price": 720000, "median_rent": 2950, "price_per_sqft": 570, "days_on_market": 38, "inventory_months": 2.6, "yoy_change": 6.1},
    "98119": {"metro": "Seattle", "population": 25000, "median_age": 37.5, "median_income": 175000, "housing_ownership_rate": 0.44, "school_rating": 8.5, "crime_index": 30.0, "median_home_price": 880000, "median_rent": 3600, "price_per_sqft": 660, "days_on_market": 44, "inventory_months": 3.1, "yoy_change": 5.4},

    # Miami Metro
    "33101": {"metro": "Miami", "population": 18000, "median_age": 40.0, "median_income": 58000, "housing_ownership_rate": 0.32, "school_rating": 6.5, "crime_index": 55.0, "median_home_price": 380000, "median_rent": 2200, "price_per_sqft": 380, "days_on_market": 75, "inventory_months": 6.0, "yoy_change": 8.5},
    "33109": {"metro": "Miami", "population": 8500, "median_age": 48.0, "median_income": 245000, "housing_ownership_rate": 0.58, "school_rating": 8.0, "crime_index": 28.0, "median_home_price": 1200000, "median_rent": 5500, "price_per_sqft": 820, "days_on_market": 95, "inventory_months": 8.5, "yoy_change": 7.2},
    "33125": {"metro": "Miami", "population": 52000, "median_age": 35.0, "median_income": 45000, "housing_ownership_rate": 0.35, "school_rating": 5.8, "crime_index": 62.0, "median_home_price": 320000, "median_rent": 1900, "price_per_sqft": 310, "days_on_market": 70, "inventory_months": 5.5, "yoy_change": 9.0},
    "33129": {"metro": "Miami", "population": 15000, "median_age": 44.0, "median_income": 185000, "housing_ownership_rate": 0.55, "school_rating": 7.8, "crime_index": 32.0, "median_home_price": 850000, "median_rent": 4200, "price_per_sqft": 620, "days_on_market": 85, "inventory_months": 7.2, "yoy_change": 7.8},
    "33132": {"metro": "Miami", "population": 12000, "median_age": 42.0, "median_income": 165000, "housing_ownership_rate": 0.42, "school_rating": 7.5, "crime_index": 38.0, "median_home_price": 720000, "median_rent": 3800, "price_per_sqft": 580, "days_on_market": 80, "inventory_months": 6.8, "yoy_change": 8.0},
    "33139": {"metro": "Miami", "population": 28000, "median_age": 45.0, "median_income": 125000, "housing_ownership_rate": 0.38, "school_rating": 7.2, "crime_index": 45.0, "median_home_price": 580000, "median_rent": 3200, "price_per_sqft": 520, "days_on_market": 72, "inventory_months": 6.0, "yoy_change": 8.2},
    "33140": {"metro": "Miami", "population": 22000, "median_age": 46.0, "median_income": 145000, "housing_ownership_rate": 0.48, "school_rating": 7.5, "crime_index": 40.0, "median_home_price": 680000, "median_rent": 3500, "price_per_sqft": 550, "days_on_market": 78, "inventory_months": 6.5, "yoy_change": 7.9},
    "33145": {"metro": "Miami", "population": 32000, "median_age": 38.0, "median_income": 72000, "housing_ownership_rate": 0.40, "school_rating": 6.2, "crime_index": 52.0, "median_home_price": 420000, "median_rent": 2400, "price_per_sqft": 400, "days_on_market": 68, "inventory_months": 5.2, "yoy_change": 8.8},
    "33149": {"metro": "Miami", "population": 12000, "median_age": 50.0, "median_income": 285000, "housing_ownership_rate": 0.65, "school_rating": 8.5, "crime_index": 25.0, "median_home_price": 1500000, "median_rent": 6800, "price_per_sqft": 950, "days_on_market": 100, "inventory_months": 9.0, "yoy_change": 6.8},
    "33155": {"metro": "Miami", "population": 48000, "median_age": 40.0, "median_income": 68000, "housing_ownership_rate": 0.52, "school_rating": 6.5, "crime_index": 48.0, "median_home_price": 480000, "median_rent": 2600, "price_per_sqft": 420, "days_on_market": 65, "inventory_months": 5.0, "yoy_change": 8.4},

    # Atlanta Metro
    "30301": {"metro": "Atlanta", "population": 15000, "median_age": 38.0, "median_income": 125000, "housing_ownership_rate": 0.35, "school_rating": 7.2, "crime_index": 48.0, "median_home_price": 480000, "median_rent": 2400, "price_per_sqft": 380, "days_on_market": 42, "inventory_months": 3.0, "yoy_change": 7.2},
    "30303": {"metro": "Atlanta", "population": 18000, "median_age": 35.0, "median_income": 98000, "housing_ownership_rate": 0.28, "school_rating": 6.8, "crime_index": 55.0, "median_home_price": 420000, "median_rent": 2200, "price_per_sqft": 360, "days_on_market": 38, "inventory_months": 2.6, "yoy_change": 8.0},
    "30305": {"metro": "Atlanta", "population": 32000, "median_age": 40.0, "median_income": 185000, "housing_ownership_rate": 0.48, "school_rating": 8.5, "crime_index": 32.0, "median_home_price": 780000, "median_rent": 3400, "price_per_sqft": 520, "days_on_market": 48, "inventory_months": 3.5, "yoy_change": 6.5},
    "30306": {"metro": "Atlanta", "population": 28000, "median_age": 37.0, "median_income": 165000, "housing_ownership_rate": 0.45, "school_rating": 8.0, "crime_index": 35.0, "median_home_price": 680000, "median_rent": 3000, "price_per_sqft": 480, "days_on_market": 44, "inventory_months": 3.2, "yoy_change": 7.0},
    "30307": {"metro": "Atlanta", "population": 22000, "median_age": 36.0, "median_income": 148000, "housing_ownership_rate": 0.50, "school_rating": 7.8, "crime_index": 34.0, "median_home_price": 620000, "median_rent": 2800, "price_per_sqft": 450, "days_on_market": 40, "inventory_months": 2.8, "yoy_change": 7.5},
    "30308": {"metro": "Atlanta", "population": 25000, "median_age": 34.0, "median_income": 115000, "housing_ownership_rate": 0.38, "school_rating": 7.0, "crime_index": 44.0, "median_home_price": 520000, "median_rent": 2500, "price_per_sqft": 420, "days_on_market": 36, "inventory_months": 2.5, "yoy_change": 8.2},
    "30309": {"metro": "Atlanta", "population": 32000, "median_age": 35.5, "median_income": 155000, "housing_ownership_rate": 0.42, "school_rating": 7.5, "crime_index": 38.0, "median_home_price": 650000, "median_rent": 2950, "price_per_sqft": 470, "days_on_market": 42, "inventory_months": 3.0, "yoy_change": 7.4},
    "30310": {"metro": "Atlanta", "population": 42000, "median_age": 32.0, "median_income": 52000, "housing_ownership_rate": 0.42, "school_rating": 5.5, "crime_index": 65.0, "median_home_price": 280000, "median_rent": 1500, "price_per_sqft": 240, "days_on_market": 45, "inventory_months": 3.2, "yoy_change": 9.5},
    "30311": {"metro": "Atlanta", "population": 48000, "median_age": 33.0, "median_income": 48000, "housing_ownership_rate": 0.45, "school_rating": 5.2, "crime_index": 68.0, "median_home_price": 260000, "median_rent": 1400, "price_per_sqft": 220, "days_on_market": 50, "inventory_months": 3.6, "yoy_change": 9.8},
    "30312": {"metro": "Atlanta", "population": 35000, "median_age": 31.0, "median_income": 85000, "housing_ownership_rate": 0.35, "school_rating": 6.2, "crime_index": 58.0, "median_home_price": 380000, "median_rent": 2000, "price_per_sqft": 320, "days_on_market": 40, "inventory_months": 2.8, "yoy_change": 8.8},

    # Additional NYC
    "10025": {"metro": "NYC", "population": 85000, "median_age": 38.0, "median_income": 125000, "housing_ownership_rate": 0.38, "school_rating": 7.5, "crime_index": 36.0, "median_home_price": 880000, "median_rent": 3400, "price_per_sqft": 920, "days_on_market": 42, "inventory_months": 3.1, "yoy_change": 5.3},
    "10451": {"metro": "NYC", "population": 48000, "median_age": 30.0, "median_income": 45000, "housing_ownership_rate": 0.22, "school_rating": 5.5, "crime_index": 62.0, "median_home_price": 420000, "median_rent": 2000, "price_per_sqft": 380, "days_on_market": 55, "inventory_months": 4.0, "yoy_change": 4.0},

    # Additional LA
    "90019": {"metro": "LA", "population": 62000, "median_age": 34.5, "median_income": 82000, "housing_ownership_rate": 0.35, "school_rating": 6.2, "crime_index": 52.0, "median_home_price": 720000, "median_rent": 2800, "price_per_sqft": 650, "days_on_market": 45, "inventory_months": 3.4, "yoy_change": 4.5},
    "90035": {"metro": "LA", "population": 28000, "median_age": 36.0, "median_income": 115000, "housing_ownership_rate": 0.32, "school_rating": 7.0, "crime_index": 42.0, "median_home_price": 880000, "median_rent": 3200, "price_per_sqft": 750, "days_on_market": 42, "inventory_months": 3.0, "yoy_change": 5.0},

    # Additional Chicago
    "60605": {"metro": "Chicago", "population": 32000, "median_age": 36.0, "median_income": 128000, "housing_ownership_rate": 0.40, "school_rating": 7.5, "crime_index": 36.0, "median_home_price": 490000, "median_rent": 2650, "price_per_sqft": 410, "days_on_market": 48, "inventory_months": 3.5, "yoy_change": 3.4},
    "60613": {"metro": "Chicago", "population": 48000, "median_age": 33.0, "median_income": 108000, "housing_ownership_rate": 0.38, "school_rating": 7.0, "crime_index": 42.0, "median_home_price": 440000, "median_rent": 2350, "price_per_sqft": 380, "days_on_market": 40, "inventory_months": 2.9, "yoy_change": 3.8},

    # Additional Houston
    "77056": {"metro": "Houston", "population": 22000, "median_age": 42.0, "median_income": 185000, "housing_ownership_rate": 0.52, "school_rating": 8.0, "crime_index": 30.0, "median_home_price": 720000, "median_rent": 3400, "price_per_sqft": 420, "days_on_market": 58, "inventory_months": 4.2, "yoy_change": 5.6},
    "77084": {"metro": "Houston", "population": 58000, "median_age": 32.0, "median_income": 72000, "housing_ownership_rate": 0.52, "school_rating": 6.5, "crime_index": 46.0, "median_home_price": 320000, "median_rent": 1750, "price_per_sqft": 200, "days_on_market": 55, "inventory_months": 4.0, "yoy_change": 4.4},

    # Additional Phoenix
    "85382": {"metro": "Phoenix", "population": 45000, "median_age": 42.0, "median_income": 92000, "housing_ownership_rate": 0.65, "school_rating": 7.2, "crime_index": 35.0, "median_home_price": 420000, "median_rent": 2100, "price_per_sqft": 290, "days_on_market": 48, "inventory_months": 3.5, "yoy_change": 5.0},
    "85281": {"metro": "Phoenix", "population": 52000, "median_age": 28.0, "median_income": 58000, "housing_ownership_rate": 0.25, "school_rating": 5.8, "crime_index": 58.0, "median_home_price": 310000, "median_rent": 1650, "price_per_sqft": 250, "days_on_market": 40, "inventory_months": 3.0, "yoy_change": 6.2},

    # Additional Austin
    "78723": {"metro": "Austin", "population": 42000, "median_age": 33.0, "median_income": 88000, "housing_ownership_rate": 0.45, "school_rating": 6.8, "crime_index": 44.0, "median_home_price": 430000, "median_rent": 2100, "price_per_sqft": 370, "days_on_market": 32, "inventory_months": 2.2, "yoy_change": 9.0},
    "78749": {"metro": "Austin", "population": 48000, "median_age": 35.0, "median_income": 115000, "housing_ownership_rate": 0.58, "school_rating": 7.8, "crime_index": 32.0, "median_home_price": 490000, "median_rent": 2350, "price_per_sqft": 390, "days_on_market": 34, "inventory_months": 2.4, "yoy_change": 8.6},

    # Additional Denver
    "80123": {"metro": "Denver", "population": 45000, "median_age": 40.0, "median_income": 115000, "housing_ownership_rate": 0.58, "school_rating": 7.5, "crime_index": 34.0, "median_home_price": 580000, "median_rent": 2700, "price_per_sqft": 440, "days_on_market": 40, "inventory_months": 2.8, "yoy_change": 6.8},
    "80220": {"metro": "Denver", "population": 48000, "median_age": 37.0, "median_income": 125000, "housing_ownership_rate": 0.48, "school_rating": 7.2, "crime_index": 38.0, "median_home_price": 600000, "median_rent": 2800, "price_per_sqft": 460, "days_on_market": 38, "inventory_months": 2.6, "yoy_change": 6.9},

    # Additional Seattle
    "98125": {"metro": "Seattle", "population": 42000, "median_age": 36.0, "median_income": 118000, "housing_ownership_rate": 0.48, "school_rating": 7.5, "crime_index": 38.0, "median_home_price": 650000, "median_rent": 2750, "price_per_sqft": 540, "days_on_market": 38, "inventory_months": 2.6, "yoy_change": 6.3},
    "98118": {"metro": "Seattle", "population": 55000, "median_age": 34.0, "median_income": 88000, "housing_ownership_rate": 0.52, "school_rating": 6.8, "crime_index": 48.0, "median_home_price": 520000, "median_rent": 2400, "price_per_sqft": 450, "days_on_market": 35, "inventory_months": 2.4, "yoy_change": 7.2},

    # Additional Miami
    "33130": {"metro": "Miami", "population": 28000, "median_age": 36.0, "median_income": 65000, "housing_ownership_rate": 0.32, "school_rating": 6.0, "crime_index": 58.0, "median_home_price": 420000, "median_rent": 2500, "price_per_sqft": 400, "days_on_market": 75, "inventory_months": 6.0, "yoy_change": 8.6},
    "33133": {"metro": "Miami", "population": 32000, "median_age": 42.0, "median_income": 125000, "housing_ownership_rate": 0.50, "school_rating": 7.5, "crime_index": 38.0, "median_home_price": 720000, "median_rent": 3600, "price_per_sqft": 580, "days_on_market": 80, "inventory_months": 6.8, "yoy_change": 7.5},

    # Additional Atlanta
    "30313": {"metro": "Atlanta", "population": 18000, "median_age": 30.0, "median_income": 72000, "housing_ownership_rate": 0.25, "school_rating": 6.0, "crime_index": 62.0, "median_home_price": 350000, "median_rent": 1850, "price_per_sqft": 300, "days_on_market": 42, "inventory_months": 3.0, "yoy_change": 9.2},
    "30314": {"metro": "Atlanta", "population": 32000, "median_age": 28.0, "median_income": 42000, "housing_ownership_rate": 0.30, "school_rating": 4.8, "crime_index": 72.0, "median_home_price": 220000, "median_rent": 1300, "price_per_sqft": 190, "days_on_market": 55, "inventory_months": 4.0, "yoy_change": 10.5},
}


def get_zipcode_data(zipcode: str) -> dict | None:
    """Get all data for a zipcode."""
    return ZIPCODE_DATA.get(zipcode)


def generate_historical_data(zipcode: str, years: int) -> list[dict]:
    """Generate synthetic historical price data."""
    data = get_zipcode_data(zipcode)
    if not data:
        return []
    
    current_price = data["median_home_price"]
    current_rent = data["median_rent"]
    annual_appreciation = data["yoy_change"] / 100
    
    historical = []
    for i in range(years, -1, -1):
        year = 2025 - i
        factor = (1 + annual_appreciation) ** (-i)
        median_price = int(current_price * factor)
        
        if i == 0:
            appreciation = data["yoy_change"]
        else:
            appreciation = round(annual_appreciation * 100 + (5 - i) * 0.2, 2)
        
        historical.append({
            "year": year,
            "median_price": median_price,
            "appreciation_rate": max(0, appreciation)
        })
    
    return historical
