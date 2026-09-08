"""Factory methods for reusable booking test data."""

from api.models.booking import Booking


def create_valid_booking(
    firstname="John", lastname="Smith", totalprice=100, depositpaid=True,
    checkin="2026-01-01", checkout="2026-01-05", additionalneeds="Breakfast"
):
    return Booking(firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds)


def create_booking_with_breakfast():
    return create_valid_booking(additionalneeds="Breakfast")


def create_booking_without_deposit():
    return create_valid_booking(depositpaid=False)


def create_booking_with_high_price():
    return create_valid_booking(totalprice=10000)


def create_updated_booking():
    return create_valid_booking(
        firstname="Robert", lastname="Wilson", totalprice=350,
        depositpaid=False, checkin="2026-10-01", checkout="2026-10-07",
        additionalneeds="Lunch"
    )
