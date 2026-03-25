"""FCC equipment certification lookup routes."""
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1", tags=["equipment"])

# Sample equipment certifications
EQUIPMENT_DB = {
    "FCC-EQ-001": {
        "fcc_id": "FCC-EQ-001",
        "device_type": "Amateur Radio Transceiver",
        "brand": "Icom",
        "model": "IC-7300",
        "frequencies_mhz": ["1.8-2.0", "3.5-4.0", "7.0-7.3", "10.1-10.15", "14.0-14.35",
                           "18.068-18.168", "21.0-21.45", "24.89-24.99", "28.0-29.7",
                           "50.0-54.0", "144.0-148.0", "420.0-450.0"],
        "max_power_w": 100.0,
        "emission_modes": ["SSB", "CW", "FM", "AM", "RTTY", "PSK31", "FT8"],
        "status": "Granted",
    },
    "FCC-EQ-002": {
        "fcc_id": "FCC-EQ-002",
        "device_type": "Amateur Radio Transceiver",
        "brand": "Kenwood",
        "model": "TS-890S",
        "frequencies_mhz": ["1.8-2.0", "3.5-4.0", "7.0-7.3", "10.1-10.15", "14.0-14.35",
                           "18.068-18.168", "21.0-21.45", "24.89-24.99", "28.0-29.7"],
        "max_power_w": 200.0,
        "emission_modes": ["SSB", "CW", "FM", "AM", "RTTY", "PSK31"],
        "status": "Granted",
    },
    "FCC-EQ-003": {
        "fcc_id": "FCC-EQ-003",
        "device_type": "Amateur Radio Transceiver",
        "brand": "Yaesu",
        "model": "FTdx101MP",
        "frequencies_mhz": ["1.8-2.0", "3.5-4.0", "7.0-7.3", "10.1-10.15", "14.0-14.35",
                           "18.068-18.168", "21.0-21.45", "24.89-24.99", "28.0-29.7"],
        "max_power_w": 200.0,
        "emission_modes": ["SSB", "CW", "FM", "AM", "RTTY", "PSK31", "FT8"],
        "status": "Granted",
    },
    "FCC-EQ-004": {
        "fcc_id": "FCC-EQ-004",
        "device_type": "Handheld Transceiver",
        "brand": "Icom",
        "model": "IC-705",
        "frequencies_mhz": ["1.8-2.0", "3.5-4.0", "7.0-7.3", "14.0-14.35", "21.0-21.45",
                           "28.0-29.7", "50.0-54.0", "144.0-148.0", "420.0-450.0"],
        "max_power_w": 10.0,
        "emission_modes": ["SSB", "CW", "FM", "AM", "FT8", "FT4"],
        "status": "Granted",
    },
    "FCC-EQ-005": {
        "fcc_id": "FCC-EQ-005",
        "device_type": "Amateur Radio Transceiver",
        "brand": "FlexRadio",
        "model": "Flex6700",
        "frequencies_mhz": ["0.1-54.0", "70.0-108.0", "135.0-138.0", "160.0-162.0",
                           "216.0-260.0", "400.0-470.0"],
        "max_power_w": 100.0,
        "emission_modes": ["SSB", "CW", "FM", "AM", "RTTY", "PSK31", "FT8", "FT4", "DIGITAL"],
        "status": "Granted",
    },
    "FCC-EQ-006": {
        "fcc_id": "FCC-EQ-006",
        "device_type": "VHF/UHF Mobile Transceiver",
        "brand": "Icom",
        "model": "ID-5100A",
        "frequencies_mhz": ["144.0-148.0", "420.0-450.0"],
        "max_power_w": 50.0,
        "emission_modes": ["FM", "D-Star"],
        "status": "Granted",
    },
    "FCC-EQ-007": {
        "fcc_id": "FCC-EQ-007",
        "device_type": "HF/VHF/UHF Mobile Transceiver",
        "brand": "Yaesu",
        "model": "FT-991A",
        "frequencies_mhz": ["1.8-2.0", "3.5-4.0", "7.0-7.3", "10.1-10.15", "14.0-14.35",
                           "18.068-18.168", "21.0-21.45", "24.89-24.99", "28.0-29.7",
                           "50.0-54.0", "144.0-148.0", "420.0-450.0"],
        "max_power_w": 100.0,
        "emission_modes": ["SSB", "CW", "FM", "AM", "RTTY", "PSK31", "FT8", "C4FM"],
        "status": "Granted",
    },
    "FCC-EQ-008": {
        "fcc_id": "FCC-EQ-008",
        "device_type": "Handheld Transceiver",
        "brand": "Yaesu",
        "model": "FT-70DR",
        "frequencies_mhz": ["144.0-148.0", "420.0-450.0"],
        "max_power_w": 5.0,
        "emission_modes": ["FM", "C4FM", "DN"],
        "status": "Granted",
    },
    "FCC-EQ-009": {
        "fcc_id": "FCC-EQ-009",
        "device_type": "Handheld Transceiver",
        "brand": "Kenwood",
        "model": "TH-D74A",
        "frequencies_mhz": ["144.0-148.0", "420.0-450.0"],
        "max_power_w": 5.0,
        "emission_modes": ["FM", "AM", "SSB", "D-Star"],
        "status": "Granted",
    },
    "FCC-EQ-010": {
        "fcc_id": "FCC-EQ-010",
        "device_type": "HF Transceiver",
        "brand": "Elecraft",
        "model": "K4",
        "frequencies_mhz": ["1.8-2.0", "3.5-4.0", "7.0-7.3", "10.1-10.15", "14.0-14.35",
                           "18.068-18.168", "21.0-21.45", "24.89-24.99", "28.0-29.7"],
        "max_power_w": 100.0,
        "emission_modes": ["SSB", "CW", "FM", "AM", "RTTY", "PSK31", "FT8", "FT4"],
        "status": "Granted",
    },
    "FCC-EQ-011": {
        "fcc_id": "FCC-EQ-011",
        "device_type": "VHF FM Repeater",
        "brand": "Motorola",
        "model": "GR1225",
        "frequencies_mhz": ["144.0-148.0"],
        "max_power_w": 45.0,
        "emission_modes": ["FM"],
        "status": "Granted",
    },
    "FCC-EQ-012": {
        "fcc_id": "FCC-EQ-012",
        "device_type": "UHF FM Repeater",
        "brand": "Motorola",
        "model": "GR1225",
        "frequencies_mhz": ["420.0-450.0"],
        "max_power_w": 40.0,
        "emission_modes": ["FM"],
        "status": "Granted",
    },
    "FCC-EQ-013": {
        "fcc_id": "FCC-EQ-013",
        "device_type": "HF Linear Amplifier",
        "brand": "Ameritron",
        "model": "AL-80B",
        "frequencies_mhz": ["1.8-2.0", "3.5-4.0", "7.0-7.3", "10.1-10.15", "14.0-14.35",
                           "18.068-18.168", "21.0-21.45", "24.89-24.99", "28.0-29.7"],
        "max_power_w": 1200.0,
        "emission_modes": ["SSB", "CW", "RTTY", "DIGITAL"],
        "status": "Granted",
    },
    "FCC-EQ-014": {
        "fcc_id": "FCC-EQ-014",
        "device_type": "VHF/UHF Yagi Antenna",
        "brand": "M2 Antenna",
        "model": "6M7JY",
        "frequencies_mhz": ["50.0-54.0"],
        "max_power_w": 1500.0,
        "emission_modes": ["SSB", "CW", "FM"],
        "status": "Granted",
    },
    "FCC-EQ-015": {
        "fcc_id": "FCC-EQ-015",
        "device_type": "SDR Receiver",
        "brand": "Airspy",
        "model": "HF+ Discovery",
        "frequencies_mhz": ["0.1-31.0", "60.0-260.0", "300.0-380.0"],
        "max_power_w": 0.0,
        "emission_modes": ["RX Only"],
        "status": "Granted",
    },
}


@router.get("/equipment/{fcc_id}")
async def get_equipment(fcc_id: str):
    """Look up an FCC equipment certification by ID."""
    eq = EQUIPMENT_DB.get(fcc_id.upper())
    if not eq:
        raise HTTPException(status_code=404, detail=f"Equipment {fcc_id} not found")
    return eq


@router.get("/equipment")
async def list_equipment():
    """List all equipment certifications."""
    return {"count": len(EQUIPMENT_DB), "equipment": list(EQUIPMENT_DB.values())}
