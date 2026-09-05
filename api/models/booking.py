"""
Booking request model.
"""

from dataclasses import dataclass


@dataclass
class Booking:
    """
    Represents booking data used by the Booking API.
    """

    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    checkin: str
    checkout: str
    additionalneeds: str

    def to_dict(self):
        """
        Convert the booking model into the API request format.

        :return: Dictionary representation of the booking
        """

        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "totalprice": self.totalprice,
            "depositpaid": self.depositpaid,
            "bookingdates": {
                "checkin": self.checkin,
                "checkout": self.checkout
            },
            "additionalneeds": self.additionalneeds
        }