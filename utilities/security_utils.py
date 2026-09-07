SENSITIVE_KEYS = {
    "password",
    "token",
    "authorization",
    "access_token",
    "refresh_token",
}


def sanitize_payload(data):
    """
    Recursively mask sensitive values before logging
    or attaching API data to reports.
    """

    if isinstance(data, dict):
        sanitized = {}

        for key, value in data.items():
            if key.lower() in SENSITIVE_KEYS:
                sanitized[key] = "***MASKED***"
            else:
                sanitized[key] = sanitize_payload(value)

        return sanitized

    if isinstance(data, list):
        return [sanitize_payload(item) for item in data]

    return data