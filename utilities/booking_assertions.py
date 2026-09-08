"""Domain-specific assertions for Booking API responses."""

from utilities.assertions import assert_status_code, assert_json_field_exists, assert_nested_json_value


def assert_booking_created(response):
    assert_status_code(response, 200)
    data = response.json()
    assert_json_field_exists(data, "bookingid")
    assert_json_field_exists(data, "booking")


def assert_created_booking_details(response, expected_data):
    """Validate POST /booking response shape."""
    data = response.json()
    for field in ("firstname", "lastname", "totalprice", "depositpaid"):
        assert_nested_json_value(data, f"booking.{field}", expected_data[field])
    assert_nested_json_value(data, "booking.bookingdates.checkin", expected_data["bookingdates"]["checkin"])
    assert_nested_json_value(data, "booking.bookingdates.checkout", expected_data["bookingdates"]["checkout"])


def assert_booking_details(response, expected_data):
    """Validate GET/PUT/PATCH booking object response shape."""
    data = response.json()
    for field in ("firstname", "lastname", "totalprice", "depositpaid"):
        assert_nested_json_value(data, field, expected_data[field])
    assert_nested_json_value(data, "bookingdates.checkin", expected_data["bookingdates"]["checkin"])
    assert_nested_json_value(data, "bookingdates.checkout", expected_data["bookingdates"]["checkout"])
