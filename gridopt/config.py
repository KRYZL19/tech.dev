from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "GRIDOPT"
    version: str = "1.0.0"
    description: str = "Time-of-Use energy tariff API for developers"

    class Config:
        env_prefix = "GRIDOPT_"


settings = Settings()
