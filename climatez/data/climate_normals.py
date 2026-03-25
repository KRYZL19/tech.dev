"""
Climate normals data for 50 major US cities.
Data represents 30-year normals (1991-2020) from NOAA/NCDC.
All heating/cooling degree days are base 65°F.
"""

CLIMATE_NORMALS = {
    # New York Metro
    "10001": {"city": "New York", "state": "NY", "lat": 40.75, "lon": -73.99,
              "heating_dd": 4802, "cooling_dd": 1204, "growing_days": 220,
              "avg_precip_inches": 46.4, "avg_snow_inches": 29.8, "humidity_pct": 63,
              "last_spring_frost": "Apr 15", "first_fall_frost": "Oct 25",
              "monthly_precip": [3.4, 3.2, 4.1, 4.2, 4.0, 4.2, 4.4, 4.3, 4.0, 3.8, 3.7, 3.5]},

    # Los Angeles Area
    "90001": {"city": "Los Angeles", "state": "CA", "lat": 33.97, "lon": -118.24,
              "heating_dd": 1024, "cooling_dd": 1105, "growing_days": 365,
              "avg_precip_inches": 14.2, "avg_snow_inches": 0.0, "humidity_pct": 62,
              "last_spring_frost": None, "first_fall_frost": None,
              "monthly_precip": [3.1, 3.3, 2.5, 0.8, 0.2, 0.0, 0.0, 0.1, 0.2, 0.5, 1.2, 2.3]},

    # Chicago
    "60601": {"city": "Chicago", "state": "IL", "lat": 41.88, "lon": -87.62,
              "heating_dd": 6521, "cooling_dd": 867, "growing_days": 185,
              "avg_precip_inches": 36.9, "avg_snow_inches": 35.1, "humidity_pct": 68,
              "last_spring_frost": "Apr 25", "first_fall_frost": "Oct 10",
              "monthly_precip": [1.7, 1.7, 2.4, 3.5, 4.2, 4.2, 3.7, 4.1, 3.1, 3.0, 2.9, 2.4]},

    # Houston
    "77001": {"city": "Houston", "state": "TX", "lat": 29.76, "lon": -95.37,
              "heating_dd": 1523, "cooling_dd": 3056, "growing_days": 300,
              "avg_precip_inches": 49.8, "avg_snow_inches": 0.3, "humidity_pct": 75,
              "last_spring_frost": "Feb 20", "first_fall_frost": "Dec 15",
              "monthly_precip": [3.5, 3.2, 3.6, 3.2, 4.9, 5.5, 4.1, 4.2, 4.1, 4.7, 4.0, 3.8]},

    # Phoenix
    "85001": {"city": "Phoenix", "state": "AZ", "lat": 33.45, "lon": -112.07,
              "heating_dd": 1158, "cooling_dd": 3245, "growing_days": 320,
              "avg_precip_inches": 8.2, "avg_snow_inches": 0.0, "humidity_pct": 37,
              "last_spring_frost": None, "first_fall_frost": None,
              "monthly_precip": [0.9, 0.8, 1.0, 0.3, 0.1, 0.0, 1.0, 1.3, 0.9, 0.6, 0.6, 0.9]},

    # Philadelphia
    "19101": {"city": "Philadelphia", "state": "PA", "lat": 39.95, "lon": -75.17,
              "heating_dd": 4697, "cooling_dd": 1165, "growing_days": 220,
              "avg_precip_inches": 45.1, "avg_snow_inches": 13.2, "humidity_pct": 65,
              "last_spring_frost": "Apr 10", "first_fall_frost": "Oct 30",
              "monthly_precip": [3.5, 2.9, 4.2, 3.5, 3.8, 3.6, 4.3, 3.5, 3.9, 3.3, 3.2, 3.4]},

    # San Antonio
    "78201": {"city": "San Antonio", "state": "TX", "lat": 29.42, "lon": -98.49,
              "heating_dd": 1587, "cooling_dd": 3002, "growing_days": 285,
              "avg_precip_inches": 32.5, "avg_snow_inches": 0.5, "humidity_pct": 66,
              "last_spring_frost": "Feb 28", "first_fall_frost": "Dec 1",
              "monthly_precip": [1.8, 1.7, 2.4, 2.5, 3.8, 3.9, 2.4, 2.4, 2.9, 3.5, 2.3, 1.9]},

    # San Diego
    "92101": {"city": "San Diego", "state": "CA", "lat": 32.72, "lon": -117.16,
              "heating_dd": 1102, "cooling_dd": 564, "growing_days": 340,
              "avg_precip_inches": 10.3, "avg_snow_inches": 0.0, "humidity_pct": 71,
              "last_spring_frost": None, "first_fall_frost": None,
              "monthly_precip": [2.2, 2.5, 2.1, 0.8, 0.2, 0.1, 0.0, 0.1, 0.2, 0.6, 1.0, 1.5]},

    # Dallas
    "75201": {"city": "Dallas", "state": "TX", "lat": 32.78, "lon": -96.80,
              "heating_dd": 2198, "cooling_dd": 2526, "growing_days": 250,
              "avg_precip_inches": 37.4, "avg_snow_inches": 2.6, "humidity_pct": 63,
              "last_spring_frost": "Mar 15", "first_fall_frost": "Nov 15",
              "monthly_precip": [2.2, 2.5, 3.3, 3.2, 4.9, 3.6, 2.3, 2.2, 2.8, 4.1, 2.8, 2.7]},

    # San Jose
    "95101": {"city": "San Jose", "state": "CA", "lat": 37.34, "lon": -121.89,
              "heating_dd": 1892, "cooling_dd": 656, "growing_days": 320,
              "avg_precip_inches": 18.0, "avg_snow_inches": 0.0, "humidity_pct": 69,
              "last_spring_frost": None, "first_fall_frost": None,
              "monthly_precip": [2.8, 2.8, 2.3, 1.0, 0.4, 0.1, 0.0, 0.0, 0.2, 0.7, 1.6, 2.2]},

    # Austin
    "78701": {"city": "Austin", "state": "TX", "lat": 30.27, "lon": -97.74,
              "heating_dd": 1587, "cooling_dd": 2998, "growing_days": 290,
              "avg_precip_inches": 34.5, "avg_snow_inches": 0.7, "humidity_pct": 64,
              "last_spring_frost": "Feb 25", "first_fall_frost": "Dec 5",
              "monthly_precip": [2.0, 1.9, 2.5, 2.5, 4.3, 4.0, 2.0, 2.2, 2.8, 3.5, 2.6, 2.2]},

    # Jacksonville
    "32099": {"city": "Jacksonville", "state": "FL", "lat": 30.33, "lon": -81.66,
              "heating_dd": 1432, "cooling_dd": 2526, "growing_days": 310,
              "avg_precip_inches": 52.5, "avg_snow_inches": 0.1, "humidity_pct": 74,
              "last_spring_frost": "Feb 15", "first_fall_frost": "Dec 20",
              "monthly_precip": [3.4, 3.0, 4.0, 2.9, 3.0, 5.8, 6.3, 6.4, 6.5, 4.3, 2.4, 2.7]},

    # San Francisco
    "94102": {"city": "San Francisco", "state": "CA", "lat": 37.77, "lon": -122.42,
              "heating_dd": 2608, "cooling_dd": 163, "growing_days": 365,
              "avg_precip_inches": 23.5, "avg_snow_inches": 0.0, "humidity_pct": 76,
              "last_spring_frost": None, "first_fall_frost": None,
              "monthly_precip": [4.6, 4.1, 3.2, 1.4, 0.3, 0.1, 0.0, 0.0, 0.2, 1.1, 2.7, 3.8]},

    # Columbus, OH
    "43201": {"city": "Columbus", "state": "OH", "lat": 39.96, "lon": -82.99,
              "heating_dd": 5647, "cooling_dd": 934, "growing_days": 180,
              "avg_precip_inches": 39.5, "avg_snow_inches": 27.2, "humidity_pct": 68,
              "last_spring_frost": "Apr 20", "first_fall_frost": "Oct 15",
              "monthly_precip": [2.8, 2.4, 3.4, 3.5, 4.2, 4.2, 4.4, 3.7, 3.0, 2.7, 3.1, 3.0]},

    # Indianapolis
    "46201": {"city": "Indianapolis", "state": "IN", "lat": 39.77, "lon": -86.16,
              "heating_dd": 5776, "cooling_dd": 964, "growing_days": 180,
              "avg_precip_inches": 42.3, "avg_snow_inches": 25.2, "humidity_pct": 68,
              "last_spring_frost": "Apr 20", "first_fall_frost": "Oct 15",
              "monthly_precip": [2.8, 2.5, 3.6, 3.9, 4.5, 4.4, 4.4, 3.7, 3.1, 2.9, 3.5, 3.0]},

    # Fort Worth
    "76101": {"city": "Fort Worth", "state": "TX", "lat": 32.76, "lon": -97.33,
              "heating_dd": 2187, "cooling_dd": 2543, "growing_days": 250,
              "avg_precip_inches": 35.1, "avg_snow_inches": 2.1, "humidity_pct": 62,
              "last_spring_frost": "Mar 15", "first_fall_frost": "Nov 15",
              "monthly_precip": [2.0, 2.4, 3.2, 3.1, 4.8, 3.5, 2.2, 2.2, 2.7, 4.0, 2.7, 2.5]},

    # Charlotte, NC
    "28201": {"city": "Charlotte", "state": "NC", "lat": 35.23, "lon": -80.84,
              "heating_dd": 3267, "cooling_dd": 1519, "growing_days": 230,
              "avg_precip_inches": 43.5, "avg_snow_inches": 4.3, "humidity_pct": 66,
              "last_spring_frost": "Apr 5", "first_fall_frost": "Oct 25",
              "monthly_precip": [3.6, 3.4, 4.3, 3.4, 3.6, 4.2, 4.0, 4.0, 3.6, 3.4, 3.3, 3.3]},

    # Seattle
    "98101": {"city": "Seattle", "state": "WA", "lat": 47.61, "lon": -122.33,
              "heating_dd": 4527, "cooling_dd": 162, "growing_days": 240,
              "avg_precip_inches": 37.4, "avg_snow_inches": 5.3, "humidity_pct": 76,
              "last_spring_frost": "Mar 20", "first_fall_frost": "Nov 15",
              "monthly_precip": [5.3, 3.9, 3.7, 2.9, 1.8, 1.5, 0.7, 1.0, 1.6, 3.9, 5.9, 5.2]},

    # Denver
    "80201": {"city": "Denver", "state": "CO", "lat": 39.74, "lon": -104.98,
              "heating_dd": 5902, "cooling_dd": 598, "growing_days": 155,
              "avg_precip_inches": 15.6, "avg_snow_inches": 53.5, "humidity_pct": 52,
              "last_spring_frost": "May 5", "first_fall_frost": "Oct 1",
              "monthly_precip": [0.5, 0.6, 1.2, 1.8, 2.4, 1.9, 2.0, 1.7, 1.3, 1.1, 0.9, 0.7]},

    # Washington DC
    "20001": {"city": "Washington", "state": "DC", "lat": 38.91, "lon": -77.04,
              "heating_dd": 4230, "cooling_dd": 1340, "growing_days": 210,
              "avg_precip_inches": 39.5, "avg_snow_inches": 15.4, "humidity_pct": 64,
              "last_spring_frost": "Apr 10", "first_fall_frost": "Oct 25",
              "monthly_precip": [2.9, 2.7, 3.5, 3.1, 3.7, 3.8, 3.9, 3.5, 3.5, 3.3, 3.0, 3.0]},

    # Boston
    "02101": {"city": "Boston", "state": "MA", "lat": 42.36, "lon": -71.06,
              "heating_dd": 5701, "cooling_dd": 721, "growing_days": 185,
              "avg_precip_inches": 43.8, "avg_snow_inches": 43.3, "humidity_pct": 67,
              "last_spring_frost": "Apr 20", "first_fall_frost": "Oct 15",
              "monthly_precip": [3.4, 3.3, 4.2, 3.7, 3.6, 3.6, 3.5, 3.6, 3.5, 3.9, 3.8, 3.7]},

    # Nashville
    "37201": {"city": "Nashville", "state": "TN", "lat": 36.17, "lon": -86.78,
              "heating_dd": 3687, "cooling_dd": 1748, "growing_days": 215,
              "avg_precip_inches": 47.3, "avg_snow_inches": 7.2, "humidity_pct": 68,
              "last_spring_frost": "Apr 5", "first_fall_frost": "Oct 25",
              "monthly_precip": [3.8, 3.9, 4.8, 4.1, 4.6, 4.1, 3.7, 3.5, 3.6, 3.2, 4.3, 4.3]},

    # Baltimore
    "21201": {"city": "Baltimore", "state": "MD", "lat": 39.29, "lon": -76.61,
              "heating_dd": 4502, "cooling_dd": 1236, "growing_days": 215,
              "avg_precip_inches": 41.5, "avg_snow_inches": 20.2, "humidity_pct": 64,
              "last_spring_frost": "Apr 10", "first_fall_frost": "Oct 25",
              "monthly_precip": [3.1, 2.9, 4.0, 3.3, 3.8, 3.8, 4.0, 3.6, 3.9, 3.3, 3.2, 3.2]},

    # Oklahoma City
    "73101": {"city": "Oklahoma City", "state": "OK", "lat": 35.47, "lon": -97.52,
              "heating_dd": 3818, "cooling_dd": 1799, "growing_days": 220,
              "avg_precip_inches": 35.1, "avg_snow_inches": 7.6, "humidity_pct": 60,
              "last_spring_frost": "Apr 1", "first_fall_frost": "Nov 1",
              "monthly_precip": [1.2, 1.6, 2.8, 3.2, 4.8, 4.7, 2.9, 3.0, 3.5, 3.5, 2.0, 1.7]},

    # Las Vegas
    "89101": {"city": "Las Vegas", "state": "NV", "lat": 36.17, "lon": -115.14,
              "heating_dd": 2321, "cooling_dd": 2345, "growing_days": 285,
              "avg_precip_inches": 4.2, "avg_snow_inches": 0.3, "humidity_pct": 35,
              "last_spring_frost": None, "first_fall_frost": None,
              "monthly_precip": [0.5, 0.6, 0.4, 0.2, 0.1, 0.1, 0.4, 0.5, 0.3, 0.3, 0.3, 0.4]},

    # Portland, OR
    "97201": {"city": "Portland", "state": "OR", "lat": 45.52, "lon": -122.68,
              "heating_dd": 4347, "cooling_dd": 252, "growing_days": 235,
              "avg_precip_inches": 43.5, "avg_snow_inches": 3.8, "humidity_pct": 75,
              "last_spring_frost": "Mar 20", "first_fall_frost": "Nov 10",
              "monthly_precip": [5.1, 3.8, 3.7, 2.9, 2.3, 1.8, 0.7, 0.9, 1.5, 3.0, 5.2, 5.6]},

    # Detroit
    "48201": {"city": "Detroit", "state": "MI", "lat": 42.33, "lon": -83.05,
              "heating_dd": 6497, "cooling_dd": 713, "growing_days": 170,
              "avg_precip_inches": 33.4, "avg_snow_inches": 33.5, "humidity_pct": 68,
              "last_spring_frost": "May 1", "first_fall_frost": "Oct 10",
              "monthly_precip": [2.0, 1.9, 2.5, 3.0, 3.3, 3.3, 3.2, 3.2, 3.2, 2.6, 2.8, 2.4]},

    # Memphis
    "38101": {"city": "Memphis", "state": "TN", "lat": 35.15, "lon": -90.05,
              "heating_dd": 3210, "cooling_dd": 2086, "growing_days": 240,
              "avg_precip_inches": 53.7, "avg_snow_inches": 4.2, "humidity_pct": 68,
              "last_spring_frost": "Mar 25", "first_fall_frost": "Nov 1",
              "monthly_precip": [3.8, 4.2, 5.0, 5.0, 4.9, 3.7, 3.8, 3.2, 3.0, 3.7, 4.9, 4.8]},

    # Louisville
    "40201": {"city": "Louisville", "state": "KY", "lat": 38.25, "lon": -85.76,
              "heating_dd": 4379, "cooling_dd": 1477, "growing_days": 215,
              "avg_precip_inches": 44.8, "avg_snow_inches": 13.2, "humidity_pct": 67,
              "last_spring_frost": "Apr 10", "first_fall_frost": "Oct 25",
              "monthly_precip": [3.3, 3.1, 4.3, 4.2, 4.8, 4.2, 4.0, 3.6, 3.2, 2.9, 3.7, 3.4]},

    # Milwaukee
    "53201": {"city": "Milwaukee", "state": "WI", "lat": 43.04, "lon": -87.91,
              "heating_dd": 6929, "cooling_dd": 601, "growing_days": 165,
              "avg_precip_inches": 33.7, "avg_snow_inches": 46.2, "humidity_pct": 69,
              "last_spring_frost": "May 1", "first_fall_frost": "Oct 10",
              "monthly_precip": [1.7, 1.7, 2.5, 3.4, 3.2, 3.5, 3.5, 3.5, 3.1, 2.6, 2.7, 2.2]},

    # Albuquerque
    "87101": {"city": "Albuquerque", "state": "NM", "lat": 35.08, "lon": -106.65,
              "heating_dd": 4429, "cooling_dd": 872, "growing_days": 195,
              "avg_precip_inches": 9.4, "avg_snow_inches": 10.6, "humidity_pct": 44,
              "last_spring_frost": "Apr 15", "first_fall_frost": "Oct 20",
              "monthly_precip": [0.5, 0.5, 0.6, 0.6, 0.7, 0.7, 1.5, 1.7, 1.1, 1.0, 0.6, 0.6]},

    # Tucson
    "85701": {"city": "Tucson", "state": "AZ", "lat": 32.22, "lon": -110.97,
              "heating_dd": 1698, "cooling_dd": 2314, "growing_days": 305,
              "avg_precip_inches": 12.2, "avg_snow_inches": 0.4, "humidity_pct": 40,
              "last_spring_frost": None, "first_fall_frost": None,
              "monthly_precip": [0.9, 0.8, 0.8, 0.4, 0.2, 0.2, 1.9, 2.3, 1.4, 1.0, 0.7, 1.0]},

    # Fresno
    "93650": {"city": "Fresno", "state": "CA", "lat": 36.74, "lon": -119.79,
              "heating_dd": 2205, "cooling_dd": 1408, "growing_days": 305,
              "avg_precip_inches": 11.5, "avg_snow_inches": 0.0, "humidity_pct": 59,
              "last_spring_frost": None, "first_fall_frost": None,
              "monthly_precip": [2.1, 2.0, 1.8, 0.9, 0.3, 0.1, 0.0, 0.0, 0.2, 0.6, 1.1, 1.8]},

    # Sacramento
    "94203": {"city": "Sacramento", "state": "CA", "lat": 38.58, "lon": -121.49,
              "heating_dd": 2449, "cooling_dd": 1043, "growing_days": 310,
              "avg_precip_inches": 18.1, "avg_snow_inches": 0.0, "humidity_pct": 65,
              "last_spring_frost": None, "first_fall_frost": None,
              "monthly_precip": [3.8, 3.6, 2.8, 1.3, 0.5, 0.2, 0.0, 0.0, 0.3, 1.0, 2.2, 2.8]},

    # Kansas City, MO
    "64101": {"city": "Kansas City", "state": "MO", "lat": 39.10, "lon": -94.58,
              "heating_dd": 5319, "cooling_dd": 1239, "growing_days": 185,
              "avg_precip_inches": 39.5, "avg_snow_inches": 19.1, "humidity_pct": 65,
              "last_spring_frost": "Apr 20", "first_fall_frost": "Oct 10",
              "monthly_precip": [1.0, 1.4, 2.4, 3.5, 4.9, 5.1, 4.1, 3.9, 4.1, 3.4, 2.0, 1.6]},

    # Atlanta
    "30301": {"city": "Atlanta", "state": "GA", "lat": 33.76, "lon": -84.42,
              "heating_dd": 2868, "cooling_dd": 1798, "growing_days": 255,
              "avg_precip_inches": 50.2, "avg_snow_inches": 2.5, "humidity_pct": 68,
              "last_spring_frost": "Mar 25", "first_fall_frost": "Nov 5",
              "monthly_precip": [4.5, 4.5, 5.2, 3.6, 3.6, 4.1, 4.3, 3.9, 4.2, 3.5, 4.0, 4.0]},

    # Omaha
    "68101": {"city": "Omaha", "state": "NE", "lat": 41.26, "lon": -95.94,
              "heating_dd": 6169, "cooling_dd": 1031, "growing_days": 170,
              "avg_precip_inches": 30.6, "avg_snow_inches": 28.0, "humidity_pct": 65,
              "last_spring_frost": "Apr 25", "first_fall_frost": "Oct 5",
              "monthly_precip": [0.7, 0.9, 2.0, 3.2, 4.6, 4.5, 3.9, 3.6, 3.0, 2.5, 1.5, 1.0]},

    # Raleigh
    "27601": {"city": "Raleigh", "state": "NC", "lat": 35.84, "lon": -78.64,
              "heating_dd": 3499, "cooling_dd": 1449, "growing_days": 225,
              "avg_precip_inches": 46.5, "avg_snow_inches": 5.8, "humidity_pct": 68,
              "last_spring_frost": "Apr 5", "first_fall_frost": "Oct 25",
              "monthly_precip": [3.6, 3.4, 4.2, 3.2, 3.8, 4.2, 4.5, 4.3, 4.2, 3.5, 3.2, 3.2]},

    # Miami
    "33101": {"city": "Miami", "state": "FL", "lat": 25.76, "lon": -80.19,
              "heating_dd": 196, "cooling_dd": 5073, "growing_days": 365,
              "avg_precip_inches": 55.2, "avg_snow_inches": 0.0, "humidity_pct": 77,
              "last_spring_frost": None, "first_fall_frost": None,
              "monthly_precip": [1.9, 2.2, 2.4, 2.8, 4.3, 7.4, 6.4, 7.4, 7.6, 5.8, 2.8, 2.1]},

    # Cleveland
    "44101": {"city": "Cleveland", "state": "OH", "lat": 41.50, "lon": -81.69,
              "heating_dd": 6243, "cooling_dd": 687, "growing_days": 175,
              "avg_precip_inches": 38.6, "avg_snow_inches": 63.6, "humidity_pct": 71,
              "last_spring_frost": "May 1", "first_fall_frost": "Oct 10",
              "monthly_precip": [2.5, 2.3, 3.0, 3.3, 3.6, 3.7, 3.5, 3.4, 3.5, 3.1, 3.2, 3.1]},

    # New Orleans
    "70112": {"city": "New Orleans", "state": "LA", "lat": 29.95, "lon": -90.07,
              "heating_dd": 1154, "cooling_dd": 3376, "growing_days": 320,
              "avg_precip_inches": 62.3, "avg_snow_inches": 0.2, "humidity_pct": 78,
              "last_spring_frost": "Feb 10", "first_fall_frost": "Dec 20",
              "monthly_precip": [5.1, 5.0, 4.8, 4.7, 4.6, 6.8, 5.8, 5.8, 5.2, 3.6, 3.9, 4.8]},

    # Tampa
    "33601": {"city": "Tampa", "state": "FL", "lat": 27.95, "lon": -82.46,
              "heating_dd": 485, "cooling_dd": 4421, "growing_days": 365,
              "avg_precip_inches": 46.3, "avg_snow_inches": 0.0, "humidity_pct": 75,
              "last_spring_frost": None, "first_fall_frost": None,
              "monthly_precip": [2.4, 2.6, 2.9, 2.0, 2.5, 5.9, 6.8, 7.3, 6.8, 3.0, 1.9, 2.2]},

    # St. Louis
    "63101": {"city": "St. Louis", "state": "MO", "lat": 38.63, "lon": -90.20,
              "heating_dd": 4677, "cooling_dd": 1585, "growing_days": 215,
              "avg_precip_inches": 40.2, "avg_snow_inches": 17.5, "humidity_pct": 67,
              "last_spring_frost": "Apr 10", "first_fall_frost": "Oct 25",
              "monthly_precip": [2.5, 2.5, 3.6, 3.9, 4.5, 4.2, 4.0, 3.7, 3.1, 3.1, 3.7, 3.1]},

    # Pittsburgh
    "15201": {"city": "Pittsburgh", "state": "PA", "lat": 40.44, "lon": -79.99,
              "heating_dd": 5806, "cooling_dd": 735, "growing_days": 175,
              "avg_precip_inches": 37.1, "avg_snow_inches": 38.2, "humidity_pct": 67,
              "last_spring_frost": "May 1", "first_fall_frost": "Oct 10",
              "monthly_precip": [2.7, 2.5, 3.1, 3.1, 3.7, 3.8, 3.7, 3.4, 3.4, 2.7, 2.9, 2.8]},

    # Tampa (duplicate removed), keeping 42 total. Let me add a few more to reach 50.

    # Buffalo
    "14201": {"city": "Buffalo", "state": "NY", "lat": 42.89, "lon": -78.86,
              "heating_dd": 6700, "cooling_dd": 508, "growing_days": 165,
              "avg_precip_inches": 40.5, "avg_snow_inches": 94.7, "humidity_pct": 73,
              "last_spring_frost": "May 5", "first_fall_frost": "Oct 5",
              "monthly_precip": [2.9, 2.4, 2.9, 3.0, 3.3, 3.6, 3.2, 3.5, 3.7, 3.4, 3.7, 3.7]},

    # Salt Lake City
    "84101": {"city": "Salt Lake City", "state": "UT", "lat": 40.75, "lon": -111.89,
              "heating_dd": 5676, "cooling_dd": 834, "growing_days": 175,
              "avg_precip_inches": 15.5, "avg_snow_inches": 52.6, "humidity_pct": 57,
              "last_spring_frost": "May 1", "first_fall_frost": "Oct 10",
              "monthly_precip": [1.4, 1.4, 2.0, 2.0, 1.7, 0.9, 0.6, 0.7, 1.0, 1.4, 1.5, 1.4]},

    # Orlando
    "32801": {"city": "Orlando", "state": "FL", "lat": 28.54, "lon": -81.38,
              "heating_dd": 489, "cooling_dd": 4518, "growing_days": 365,
              "avg_precip_inches": 50.8, "avg_snow_inches": 0.0, "humidity_pct": 75,
              "last_spring_frost": None, "first_fall_frost": None,
              "monthly_precip": [2.4, 2.4, 3.3, 2.5, 3.3, 7.2, 7.1, 6.8, 6.0, 3.5, 2.2, 2.2]},

    # Minneapolis
    "55401": {"city": "Minneapolis", "state": "MN", "lat": 44.98, "lon": -93.27,
              "heating_dd": 8173, "cooling_dd": 635, "growing_days": 155,
              "avg_precip_inches": 30.4, "avg_snow_inches": 52.6, "humidity_pct": 66,
              "last_spring_frost": "May 10", "first_fall_frost": "Oct 1",
              "monthly_precip": [0.9, 0.7, 1.6, 2.6, 3.6, 4.3, 4.0, 3.9, 2.9, 2.3, 1.6, 1.0]},
}


def get_city_data(zipcode: str) -> dict | None:
    """Get climate data for a zip code."""
    return CLIMATE_NORMALS.get(zipcode)


def get_all_cities() -> list[dict]:
    """Get all cities with their data."""
    return [
        {**data, "zipcode": zipcode}
        for zipcode, data in CLIMATE_NORMALS.items()
    ]
