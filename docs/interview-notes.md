# Senior SDET Interview Notes

## Why `requests.Session()`?

It provides reusable HTTP connection/session behavior and a single place for common client configuration.

## Why `BaseClient`?

To centralize transport concerns such as HTTP verbs, URL construction, timeout handling, logging and reporting. Domain clients should not duplicate this plumbing.

## Why `BookingClient`?

It represents booking business operations and hides endpoint construction from tests.

## How do you prevent test dependency?

Stateful CRUD tests create their own records and capture the generated booking ID from the create response.

## How do you support parallel execution?

Tests avoid shared mutable state and hardcoded booking IDs. The suite is validated with pytest-xdist.

## Why schema validation?

A 200 response only proves the HTTP request succeeded. JSON Schema also verifies response structure and data types.

## Why BDD?

BDD expresses important business behavior in a readable Given/When/Then format while pytest-bdd keeps the scenarios in the pytest execution ecosystem.

## How do you protect secrets?

Credentials come from environment variables. Request/response headers and payloads are sanitized before Allure attachment.

## How does CI reporting work?

pytest creates Allure result files. The CI workflow generates the static Allure HTML report, preserves prior history when available, uploads JUnit/Allure artifacts and deploys the HTML site to GitHub Pages.

## What would you add next in a real enterprise product?

- Service virtualization for unavailable dependencies
- Consumer/provider contract testing across microservices
- Performance and reliability suites
- OpenTelemetry/observability integration
- Dockerized execution
- Risk-based environment promotion gates
