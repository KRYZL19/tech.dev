from pydantic import BaseModel, Field
from typing import Optional


class VINDecodeRequest(BaseModel):
    vin: str = Field(..., min_length=17, max_length=17, description="17-character Vehicle Identification Number")


class VINDecodeResponse(BaseModel):
    make: str
    model: str
    year: int
    engine_cc: int
    hp: int
    wet_weight_kg: int
    frame_type: str
    country: str
    plant: str
    sequential_number: str
    vin: str


class VINValidateRequest(BaseModel):
    vin: str = Field(..., min_length=17, max_length=17, description="17-character Vehicle Identification Number")


class VINValidateResponse(BaseModel):
    valid_format: bool
    check_digit_correct: bool
    country_of_origin: str
    year_char: str
    vin: str


class ModelSpecsResponse(BaseModel):
    make: str
    model: str
    year: int
    engine_cc: int
    hp: int
    wet_weight_kg: int
    frame_type: str
    country: str
