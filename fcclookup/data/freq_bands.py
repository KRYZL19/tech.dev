"""Amateur radio band definitions (160m through 23cm)."""

BANDS = {
    "160m": {
        "name": "160 Meters",
        "start_mhz": 1.8,
        "end_mhz": 2.0,
        "bandwidth_khz": 200,
        "allocations": {
            "usa": {
                "type": "Amateur Secondary",
                "privileges": {
                    "Novice": [],
                    "Technician": [],
                    "General": ["1800-2000 kHz"],
                    "Extra": ["1800-2000 kHz"],
                },
            }
        },
    },
    "80m": {
        "name": "80 Meters",
        "start_mhz": 3.5,
        "end_mhz": 4.0,
        "bandwidth_khz": 500,
        "allocations": {
            "usa": {
                "type": "Amateur Primary",
                "privileges": {
                    "Novice": ["3700-3750 kHz"],
                    "Technician": ["3525-3600 kHz"],
                    "General": ["3525-3750 kHz"],
                    "Extra": ["3500-4000 kHz"],
                },
            }
        },
    },
    "40m": {
        "name": "40 Meters",
        "start_mhz": 7.0,
        "end_mhz": 7.3,
        "bandwidth_khz": 300,
        "allocations": {
            "usa": {
                "type": "Amateur Primary",
                "privileges": {
                    "Novice": ["7100-7150 kHz"],
                    "Technician": ["7025-7125 kHz"],
                    "General": ["7025-7300 kHz"],
                    "Extra": ["7000-7300 kHz"],
                },
            }
        },
    },
    "20m": {
        "name": "20 Meters",
        "start_mhz": 14.0,
        "end_mhz": 14.35,
        "bandwidth_khz": 350,
        "allocations": {
            "usa": {
                "type": "Amateur Primary",
                "privileges": {
                    "Novice": [],
                    "Technician": [],
                    "General": ["14025-14350 kHz"],
                    "Extra": ["14000-14350 kHz"],
                },
            }
        },
    },
    "15m": {
        "name": "15 Meters",
        "start_mhz": 21.0,
        "end_mhz": 21.45,
        "bandwidth_khz": 450,
        "allocations": {
            "usa": {
                "type": "Amateur Primary",
                "privileges": {
                    "Novice": [],
                    "Technician": [],
                    "General": ["21025-21450 kHz"],
                    "Extra": ["21000-21450 kHz"],
                },
            }
        },
    },
    "10m": {
        "name": "10 Meters",
        "start_mhz": 28.0,
        "end_mhz": 29.7,
        "bandwidth_khz": 1700,
        "allocations": {
            "usa": {
                "type": "Amateur Primary",
                "privileges": {
                    "Novice": ["28025-28375 kHz"],
                    "Technician": ["28025-29700 kHz"],
                    "General": ["28025-29700 kHz"],
                    "Extra": ["28000-29700 kHz"],
                },
            }
        },
    },
    "6m": {
        "name": "6 Meters",
        "start_mhz": 50.0,
        "end_mhz": 54.0,
        "bandwidth_khz": 4000,
        "allocations": {
            "usa": {
                "type": "Amateur Primary",
                "privileges": {
                    "Novice": [],
                    "Technician": ["500-540 MHz (some limits)"],
                    "General": ["500-540 MHz"],
                    "Extra": ["500-540 MHz"],
                },
            }
        },
    },
    "2m": {
        "name": "2 Meters",
        "start_mhz": 144.0,
        "end_mhz": 148.0,
        "bandwidth_khz": 4000,
        "allocations": {
            "usa": {
                "type": "Amateur Primary",
                "privileges": {
                    "Novice": ["144-148 MHz"],
                    "Technician": ["144-148 MHz"],
                    "General": ["144-148 MHz"],
                    "Extra": ["144-148 MHz"],
                },
            }
        },
    },
    "70cm": {
        "name": "70 Centimeters",
        "start_mhz": 420.0,
        "end_mhz": 450.0,
        "bandwidth_khz": 30000,
        "allocations": {
            "usa": {
                "type": "Amateur Primary",
                "privileges": {
                    "Novice": [],
                    "Technician": ["420-450 MHz"],
                    "General": ["420-450 MHz"],
                    "Extra": ["420-450 MHz"],
                },
            }
        },
    },
    "23cm": {
        "name": "23 Centimeters",
        "start_mhz": 1240.0,
        "end_mhz": 1300.0,
        "bandwidth_khz": 60000,
        "allocations": {
            "usa": {
                "type": "Amateur Secondary",
                "privileges": {
                    "Novice": [],
                    "Technician": [],
                    "General": ["1240-1300 MHz"],
                    "Extra": ["1240-1300 MHz"],
                },
            }
        },
    },
}

# License classes in order of privileges
LICENSE_CLASSES = ["Novice", "Technician", "General", "Extra"]

# Common ISM and公共服务频段 (for interference checks)
ISM_BANDS = [
    {"name": "2.4 GHz ISM", "start_mhz": 2400.0, "end_mhz": 2500.0},
    {"name": "5.8 GHz ISM", "start_mhz": 5725.0, "end_mhz": 5875.0},
]
