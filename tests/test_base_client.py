from api.clients.response_handler import ResponseHandler

def test_get_booking(client):
    """
    Verify that BaseClient can send a GET request.
    """

    response = client.get("/booking",
                          params={"firstname": "John"})

    assert response.status_code == 200

    response_data = ResponseHandler.get_json(response)

    assert isinstance(response_data, list)

def test_post_booking(client):
    booking_data = {
        "firstname": "Test",
        "lastname": "User",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-08-27",
            "checkout": "2026-08-30"
        },
        "additionalneeds": "Breakfast"
    }

    response = client.post(
        "/booking",
        json=booking_data
    )

    assert response.status_code == 200