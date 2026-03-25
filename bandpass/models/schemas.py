from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class RoomTreatmentLevel(str, Enum):
    treated = "treated"
    partial = "partial"
    untreated = "untreated"


class SpeakerType(str, Enum):
    bookshelf = "bookshelf"
    studio_monitor = "studio_monitor"
    tower = "tower"
    soundbar = "soundbar"


class EQFilter(BaseModel):
    frequency_hz: float = Field(..., description="Center frequency in Hz")
    gain_db: float = Field(..., description="Gain in decibels")
    q_factor: float = Field(..., description="Q factor for the filter")


class RoomMode(BaseModel):
    frequency_hz: float = Field(..., description="Mode frequency in Hz")
    mode_type: str = Field(..., description="axial, tangential, or oblique")
    dimensions: str = Field(..., description="Which dimensions contribute")
    severity: str = Field(..., description="mild, moderate, severe")
    recommendation: str = Field(..., description="Treatment recommendation")


class FirstReflectionCorrection(BaseModel):
    frequency_hz: float = Field(..., description="Affected frequency")
    panel_location: str = Field(..., description="Wall/ceiling/floor")
    recommended_treatment: str = Field(..., description="Treatment type")
    eq_suggestion_hz: Optional[float] = Field(None, description="EQ frequency if helpful")


class RoomEQInput(BaseModel):
    room_volume_cubic_ft: float = Field(..., gt=0, le=10000, description="Room volume in cubic feet")
    listening_distance_ft: float = Field(..., gt=0, le=30, description="Listening distance in feet")
    speaker_type: SpeakerType = Field(..., description="Type of speakers")
    room_treatment_level: RoomTreatmentLevel = Field(..., description="Room treatment level")


class RoomEQOutput(BaseModel):
    recommended_eq_settings: list[EQFilter]
    room_mode_predictions: list[RoomMode]
    first_reflection_corrections: list[FirstReflectionCorrection]


class SpeakerProfileInput(BaseModel):
    speaker_manufacturer: str = Field(..., description="Manufacturer name")
    speaker_model: str = Field(..., description="Model name")
    listening_distance_ft: float = Field(..., gt=0, le=30, description="Listening distance in feet")


class FrequencyPoint(BaseModel):
    frequency_hz: float
    spl_db: float


class BassBoostRecommendation(BaseModel):
    frequency_hz: float
    boost_db: float
    reason: str


class SpeakerProfileOutput(BaseModel):
    frequency_response_curve: list[FrequencyPoint]
    recommended_xover_hz: int
    bass_boost_recommendations: list[BassBoostRecommendation]


class FilterInfo(BaseModel):
    filter_type: str
    description: str
    typical_use_cases: list[str]
    recommended_q_range: str
    recommended_gain_range: str


class RoomModesInput(BaseModel):
    length_ft: float = Field(..., gt=0, le=100, alias="length_ft")
    width_ft: float = Field(..., gt=0, le=100, alias="width_ft")
    height_ft: float = Field(..., gt=0, le=20, alias="height_ft")
