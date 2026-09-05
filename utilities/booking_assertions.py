"""
Domain-specific assertions for Booking API responses.
"""

from utilities.assertions import (
    assert_status_code,
    assert_json_field_exists,
    assert_nested_json_value
)


def assert_booking_created(response):
    """
    Validate that a booking creation response is successful.

    :param response: API response
    """

    assert_status_code(response, 200)

    response_data = response.json()

    assert_json_field_exists(response_data, "bookingid")
    assert_json_field_exists(response_data, "booking")


def assert_booking_details(response, expected_data):
    """
    Validate booking details against expected booking data.

    :param response: API response
    :param expected_data: Expected booking data
    """

    response_data = response.json()

    assert_nested_json_value(
        response_data,
        "booking.firstname",
        expected_data["firstname"]
    )

    assert_nested_json_value(
        response_data,
        "booking.lastname",
        expected_data["lastname"]
    )

    assert_nested_json_value(
        response_data,
        "booking.totalprice",
        expected_data["totalprice"]
    )

    assert_nested_json_value(
        response_data,
        "booking.depositpaid",
        expected_data["depositpaid"]
    )