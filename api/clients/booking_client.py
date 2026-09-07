import allure

from api.clients.auth_headers import token_header
from api.endpoints.booking_endpoints import booking_by_id, BOOKING
from utilities.api_utils import attach_request_payload, attach_response


class BookingClient:
    """
    Client containing booking-specific API operations.
    """
    def __init__(self, client):
        """
        Initialize BookingClient.

        :param client: BaseClient instance
        """
        self.client = client

    @allure.step("Get all bookings")
    def get_all_bookings(self):
        return self.client.get(BOOKING)

    @allure.step("Get booking by ID: {booking_id}")
    def get_booking(self, booking_id):
        """
        Retrieve a booking using booking ID.

        :param booking_id: Booking ID
        :return: API response
        """
        return self.client.get(booking_by_id(booking_id))

    # @allure.step("Create a new booking")
    # def create_booking(self, booking_data):
    #     """
    #     Create a new booking.
    #
    #     :param booking_data: Booking request payload
    #     :return: API response
    #     """
    #     attach_request_payload(booking_data)
    #
    #     response = self.client.post(BOOKING, json=booking_data)
    #
    #     attach_response(response)
    #
    #     return response

    @allure.step("Create booking")
    def create_booking(self, booking_data):
        return self.client.post(
            BOOKING,
            json=booking_data
        )

    @allure.step("Update booking: {booking_id}")
    def update_booking(self, booking_id, booking_data, token):
        """
        Fully update an existing booking.

        :param booking_id: Booking ID
        :param booking_data: Complete booking payload
        :param token: Authentication token
        :return: API response
        """

        return self.client.put(
            booking_by_id(booking_id),
            json=booking_data,
            headers=token_header(token)
        )

    @allure.step("Partially update booking: {booking_id}")
    def patch_booking(self, booking_id, booking_data, token):
        """
        Partially update an existing booking.

        :param booking_id: Booking ID
        :param booking_data: Fields to update
        :param token: Authentication token
        :return: API response
        """

        return self.client.patch(
            booking_by_id(booking_id),
            json=booking_data,
            headers=token_header(token)
        )

    @allure.step("Delete booking: {booking_id}")
    def delete_booking(self, booking_id, token):
        """
        Delete an existing booking.

        :param booking_id: Booking ID
        :param token: Authentication token
        :return: API response
        """

        return self.client.delete(
            booking_by_id(booking_id),
            headers=token_header(token)
        )