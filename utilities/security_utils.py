"""Utilities for protecting secrets in logs and test reports."""

SENSITIVE_KEYS = {
    "password", "token", "authorization", "cookie", "access_token",
    "refresh_token", "api_key", "secret"
}


def sanitize_payload(data):
    """Return a recursively sanitized copy of JSON-like data."""
    if isinstance(data, dict):
        return {
            key: "***MASKED***" if str(key).lower() in SENSITIVE_KEYS
            else sanitize_payload(value)
            for key, value in data.items()
        }
    if isinstance(data, list):
        return [sanitize_payload(item) for item in data]
    return data


def sanitize_headers(headers):
    """Return headers with sensitive header values masked."""
    return sanitize_payload(dict(headers or {}))
