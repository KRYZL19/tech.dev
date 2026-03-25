from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "GRIDOPT API"
    version: str = "1.0.0"
    description: str = "Energy Tariff & Optimization API"
    api_prefix: str = "/api/v1"

    # Rate limiting (calls per month)
    rate_limit_free: int = 500
    rate_limit_dev: int = 10_000
    rate_limit_pro: int = 100_000

    # Carbon intensity API (EIA pattern)
    carbon_api_base: str = "https://api.eia.gov/v2"


settings = Settings()
