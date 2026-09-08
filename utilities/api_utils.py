"""Allure evidence helpers used by the API client layer."""

import json
import allure

from utilities.security_utils import sanitize_headers, sanitize_payload


def _attach_json_or_text(data, name):
    sanitized = sanitize_payload(data)
    if isinstance(sanitized, (dict, list)):
        allure.attach(
            json.dumps(sanitized, indent=4, default=str),
            name=name,
            attachment_type=allure.attachment_type.JSON,
        )
    else:
        allure.attach(
            str(sanitized), name=name,
            attachment_type=allure.attachment_type.TEXT,
        )


def attach_request(method, url, headers=None, payload=None, params=None):
    """Attach a sanitized API request to the current Allure test."""
    allure.attach(method.upper(), name="HTTP Method", attachment_type=allure.attachment_type.TEXT)
    allure.attach(url, name="Request URL", attachment_type=allure.attachment_type.TEXT)
    _attach_json_or_text(sanitize_headers(headers), "Request Headers")
    if params:
        _attach_json_or_text(params, "Query Parameters")
    if payload is not None:
        _attach_json_or_text(payload, "Request Payload")


def attach_response(response):
    """Attach a sanitized API response to the current Allure test."""
    allure.attach(
        str(response.status_code), name="Status Code",
        attachment_type=allure.attachment_type.TEXT,
    )
    _attach_json_or_text(sanitize_headers(response.headers), "Response Headers")
    try:
        _attach_json_or_text(response.json(), "Response Body")
    except ValueError:
        allure.attach(
            response.text, name="Response Body",
            attachment_type=allure.attachment_type.TEXT,
        )


def attach_request_payload(payload):
    """Backward-compatible helper for attaching a sanitized request payload."""
    _attach_json_or_text(payload, "Request Payload")
