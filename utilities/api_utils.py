import json

import allure


def attach_response(response):
    """
    Attach API response details to the Allure report.

    :param response: requests.Response object
    """

    allure.attach(
        str(response.status_code),
        name="Status Code",
        attachment_type=allure.attachment_type.TEXT
    )

    try:
        response_body = response.json()

        allure.attach(
            str(response_body),
            name="Response Body",
            attachment_type=allure.attachment_type.JSON
        )

    except ValueError:
        allure.attach(
            response.text,
            name="Response Body",
            attachment_type=allure.attachment_type.TEXT
        )

def attach_request_payload(payload):
    """
    Attach request payload to Allure.

    :param payload: Request JSON payload
    """

    allure.attach(
        json.dumps(
            payload,
            indent=4
        ),
        name="Request Payload",
        attachment_type=allure.attachment_type.JSON
    )