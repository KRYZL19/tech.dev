"""Pydantic schemas for CARBONCALC API."""

from pydantic import BaseModel, Field
from typing import Literal, Optional


# --- Shipping --- #

class ShipCarbonRequest(BaseModel):
    distance_nm: float = Field(..., gt=0, description="Distance in nautical miles")
    cargo_tons: float = Field(..., gt=0, description="Cargo weight in metric tons")
    vessel_type: Literal["container", "bulk", "roro"] = Field(
        default="container", description="Type of vessel"
    )


class ShipCarbonResponse(BaseModel):
    co2_kg: float = Field(..., description="CO2 emissions in kilograms")
    co2_tons: float = Field(..., description="CO2 emissions in metric tons")
    comparison_vs_truck_kg: float = Field(
        ..., description="Same shipment by heavy truck in kg CO2"
    )
    savings_vs_truck_pct: float = Field(
        ..., description="Emissions savings vs truck (%)"
    )


# --- Truck --- #

class TruckCarbonRequest(BaseModel):
    distance_km: float = Field(..., gt=0, description="Distance in kilometers")
    cargo_kg: float = Field(..., gt=0, description="Cargo weight in kilograms")
    fuel_type: Literal["diesel", "lng", "electric"] = Field(
        default="diesel", description="Fuel type"
    )
    truck_type: Literal["standard", "heavy"] = Field(
        default="standard", description="Truck type"
    )


class TruckCarbonResponse(BaseModel):
    co2_kg: float = Field(..., description="CO2 emissions in kilograms")
    fuel_liters: Optional[float] = Field(
        None, description="Estimated diesel fuel consumed (liters)"
    )


# --- Offset --- #

class OffsetTreesRequest(BaseModel):
    co2_kg: float = Field(..., gt=0, description="CO2 to offset in kilograms")


class OffsetTreesResponse(BaseModel):
    co2_kg: float = Field(..., description="CO2 to offset in kg")
    trees_needed: float = Field(..., description="Trees needed (fractional OK)")
    trees_rounded_up: int = Field(..., description="Trees needed (rounded up)")
    cost_at_15_per_tree_usd: float = Field(..., description="Cost at $15/tree in USD")
    years_to_offset: float = Field(
        ..., description="Years for natural sequestration at 21kg/tree/year"
    )


# --- Supply Chain --- #

class ShipmentItem(BaseModel):
    type: Literal["container_ship", "bulk_carrier", "roro_vessel",
                   "truck_diesel", "truck_lng", "aviation_short", "aviation_long"]
    distance: float = Field(..., gt=0, description="Distance (nm for ships, km for others)")
    cargo: float = Field(..., gt=0, description="Cargo weight (tons)")


class SupplyChainSummaryRequest(BaseModel):
    shipments: list[ShipmentItem] = Field(..., min_length=1)


class SupplyChainSummaryResponse(BaseModel):
    total_co2_kg: float
    total_co2_tons: float
    offset_cost_usd: float = Field(
        ..., description="Cost to offset all emissions at $15/tree"
    )
    carbon_intensity: float = Field(
        ..., description="kg CO2 per ton-km (lower is better)"
    )
    breakdown: list[dict] = Field(..., description="Per-shipment CO2 breakdown")


# --- Health --- #

class HealthResponse(BaseModel):
    status: str = "ok"
    version: str = "1.0.0"
