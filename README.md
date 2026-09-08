# Python API Automation Framework — Senior SDET Portfolio

> A production-style API automation framework built with Python, pytest, Requests, pytest-bdd, JSON Schema, Allure and GitHub Actions.

## 1. What this project demonstrates

- Layered API automation architecture
- Reusable HTTP client using `requests.Session`
- Domain clients for authentication and booking APIs
- API chaining with dynamically created booking IDs
- Positive, negative, boundary and contract testing
- JSON Schema validation
- Data factories and domain models
- BDD with pytest-bdd
- Centralized, secret-safe Allure request/response evidence
- Parallel execution with pytest-xdist
- CI/CD with GitHub Actions
- HTML Allure report generation and GitHub Pages deployment
- Test strategy, architecture and interview documentation

## 2. API under test

RESTful Booker: `https://restful-booker.herokuapp.com`

| Area | Endpoint | Coverage |
|---|---|---|
| Health | GET /ping | Smoke |
| Authentication | POST /auth | Positive + negative + BDD |
| Booking | GET /booking | Positive + filters |
| Booking | GET /booking/{id} | Positive + negative |
| Booking | POST /booking | Positive + boundary + negative + schema |
| Booking | PUT /booking/{id} | Positive + negative |
| Booking | PATCH /booking/{id} | Positive + negative |
| Booking | DELETE /booking/{id} | Positive + negative |

## 3. Architecture

```text
Tests / BDD scenarios
        |
        v
Domain test data + assertions
        |
        v
AuthClient / BookingClient
        |
        v
BaseClient (requests.Session)
        |
        +--> Allure evidence + secret sanitization
        |
        v
RESTful Booker API
```

See [`docs/architecture.md`](docs/architecture.md).

## 4. Project structure

```text
api/
  clients/       # HTTP and domain clients
  endpoints/     # Endpoint definitions
  models/        # Domain models
config/           # Framework configuration
features/         # Gherkin scenarios
schemas/          # JSON Schema contracts
test_data/        # Factories and reusable datasets
tests/            # pytest test suite
utilities/        # assertions, logging, reporting, security
docs/             # architecture, strategy, interview notes
.github/workflows/ # CI/CD
```

## 5. Configuration and secrets

Create `.env` locally:

```env
AUTH_USERNAME=your_username
AUTH_PASSWORD=your_password
```

Never commit `.env`. CI reads `AUTH_USERNAME` and `AUTH_PASSWORD` from GitHub Secrets.

## 6. Install

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 7. Test execution

```powershell
# Full suite
pytest -v

# Regression
pytest -m regression -v

# Smoke
pytest -m smoke -v

# Negative
pytest -m negative -v

# Contract
pytest -m contract -v

# BDD
pytest -m bdd -v

# Parallel
pytest -m regression -n 2 --dist=loadfile -v
```

## 8. Reporting

Pytest creates raw Allure results in `allure-results/`. Locally, generate an HTML report with the Allure CLI:

```powershell
allure generate allure-results -o allure-report --clean
allure open allure-report
```

In GitHub Actions the workflow generates the HTML report and deploys it to GitHub Pages.

## 9. Allure evidence

Each API call captures:

- HTTP method
- URL
- sanitized request headers
- query parameters
- sanitized request payload
- status code
- response headers
- sanitized response body

The framework also generates `categories.json`, `environment.properties` and `executor.json`.

## 10. Test strategy

The suite is organized using `smoke`, `regression`, `negative`, `contract` and `bdd` markers. Tests create their own data wherever state could otherwise leak between scenarios.

See [`docs/test-strategy.md`](docs/test-strategy.md).

## 11. Senior-level design decisions

1. Keep HTTP transport in `BaseClient`.
2. Keep business endpoint behavior in domain clients.
3. Keep test data out of step definitions.
4. Validate both HTTP behavior and response contracts.
5. Generate dynamic IDs instead of relying on shared fixed data.
6. Sanitize secrets before logs and reports.
7. Make the suite parallel-safe before enabling xdist.
8. Publish actionable test evidence from CI.

## 12. Portfolio status

This repository is designed as an SDET portfolio demonstration of API automation architecture, test strategy, BDD, reporting, security and CI/CD rather than as a collection of repetitive test cases.
