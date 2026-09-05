INVALID_BOOKING_DATA = {
    "firstname": "John"
}

MISSING_FIRSTNAME_DATA = {
    "lastname": "Smith",
    "totalprice": 200,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2025-01-01",
        "checkout": "2025-01-05"
    }
}

INVALID_PRICE_DATA = {
    "firstname": "John",
    "lastname": "Smith",
    "totalprice": "INVALID",
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2025-01-01",
        "checkout": "2025-01-05"
    }
}