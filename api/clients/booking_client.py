"""Booking-specific API client."""

import allure

from api.clients.auth_headers import token_header
from api.endpoints.booking_endpoints import BOOKING, booking_by_id


class BookingClient:
    """Encapsulates booking domain endpoints without HTTP plumbing."""

    def __init__(self, client):
        self.client = client

    @allure.step("Get all bookings")
    def get_all_bookings(self, params=None):
        return self.client.get(BOOKING, params=params)

    @allure.step("Get booking by ID: {booking_id}")
    def get_booking(self, booking_id):
        return self.client.get(booking_by_id(booking_id))

    @allure.step("Create booking")
    def create_booking(self, booking_data):
        return self.client.post(BOOKING, json=booking_data)

    @allure.step("Update booking: {booking_id}")
    def update_booking(self, booking_id, booking_data, token):
        return self.client.put(
            booking_by_id(booking_id), json=booking_data,
            headers=token_header(token)
        )

    @allure.step("Partially update booking: {booking_id}")
    def patch_booking(self, booking_id, booking_data, token):
        return self.client.patch(
            booking_by_id(booking_id), json=booking_data,
            headers=token_header(token)
        )

    @allure.step("Delete booking: {booking_id}")
    def delete_booking(self, booking_id, token):
        return self.client.delete(
            booking_by_id(booking_id), headers=token_header(token)
        )
