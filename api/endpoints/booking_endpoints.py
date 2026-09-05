"""
Booking API endpoint definitions.
"""


BOOKING = "/booking"


def booking_by_id(booking_id):
    """
    Build the endpoint for a specific booking.

    :param booking_id: Booking identifier
    :return: Booking endpoint path
    """
    return f"{BOOKING}/{booking_id}"