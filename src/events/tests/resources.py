TEST_LATITUDES_OK = [
    {"timestamp": "2023-10-01T10:00:00", "position": 34.0522},
    {"timestamp": "2023-10-01T10:10:00", "position": 35.1234},
    {"timestamp": "2023-10-01T10:20:00", "position": 36.2456},
    {"timestamp": "2023-10-01T10:30:00", "position": 37.3245},
    {"timestamp": "2023-10-01T10:40:00", "position": 38.4321},
    {"timestamp": "2023-10-01T10:50:00", "position": 39.5567},
]


TEST_LATITUDES_INVALID_DATETIME = [
    {"timestamp": "adasdasdasdas", "position": 34.0522},
]


TEST_LATITUDES_INVALID_POSITION = [
    {"timestamp": "2023-10-01T10:00:00", "position": "dsa"},
]


TEST_LONGITUDES_OK = [
    {"timestamp": "2023-10-01T10:00:00", "position": -118.2437},
    {"timestamp": "2023-10-01T10:10:00", "position": -117.2437},
    {"timestamp": "2023-10-01T10:20:00", "position": -116.2437},
    {"timestamp": "2023-10-01T10:30:00", "position": -115.2437},
    {"timestamp": "2023-10-01T10:40:00", "position": -114.2437},
    {"timestamp": "2023-10-01T10:50:00", "position": -113.2437},
]


TEST_LONGITUDES_INVALID_DATETIME = [
    {"timestamp": "adasdasdasdas", "position": -118.2437},
]


TEST_LONGITUDES_INVALID_POSITION = [
    {"timestamp": "2023-10-01T10:00:00", "position": "dasdas"},
]


TEST_EVENTS_OK = [
    {
        "occurrence_time": "2023-10-01T10:15:00",
        "event_name": "System Startup",
        "event_identifier": "E001",
        "severity": "Info"
    },
    {
        "occurrence_time": "2023-10-01T10:35:00",
        "event_name": "Navigation Calibration",
        "event_identifier": "E002",
        "severity": "Info"
    },
    {
        "occurrence_time": "2023-10-01T10:50:00",
        "event_name": "Warning Light On",
        "event_identifier": "E003",
        "severity": "Warning"
    },
]


TEST_EVENTS_INVALID_DATETIME = [
    {
        "occurrence_time": "adasdasdasdas",
        "event_name": "System Startup",
        "event_identifier": "E001",
        "severity": "Info"
    },
    {
        "occurrence_time": "2023-10-01T10:35:00",
        "event_name": "Navigation Calibration",
        "event_identifier": "E002",
        "severity": "Info"
    }
]
