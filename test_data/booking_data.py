"""
Reusable booking test data.
"""

from test_data.booking_factory import create_valid_booking


VALID_BOOKING_DATA = create_valid_booking().to_dict()

VALID_BOOKING_DATA_2 = create_valid_booking(
    firstname="David",
    lastname="Brown",
    totalprice=250,
    depositpaid=False,
    checkin="2025-02-01",
    checkout="2025-02-05",
    additionalneeds="Lunch"
).to_dict()

INVALID_BOOKING_DATA = {
    "firstname": "John"
}