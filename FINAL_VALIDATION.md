# Final Validation Guide

## 1. Prerequisites

- Python 3.13+
- Git
- An API account/credentials for the RESTful Booker authentication endpoint
- Node.js/npm only if you want to generate the Allure HTML report locally

## 2. Configure credentials

Copy `.env.example` to `.env` and set:

```env
AUTH_USERNAME=your_username
AUTH_PASSWORD=your_password
```

Do not commit `.env`.

## 3. Create the virtual environment

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 4. Validate collection

```powershell
pytest --collect-only -q
```

The framework is designed for approximately 39 total pytest executions, including the 7 BDD scenarios.

## 5. Run the suites

```powershell
pytest -m smoke -v
pytest -m regression -v
pytest -m negative -v
pytest -m contract -v
pytest -m bdd -v
pytest -n 2 --dist=loadfile -v
```

## 6. Generate the local HTML Allure report

Install the CLI once:

```powershell
npm install -g allure-commandline@2.35.1
```

Run:

```powershell
pytest -m regression
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## 7. GitHub Actions setup

Add repository secrets:

- `AUTH_USERNAME`
- `AUTH_PASSWORD`

The workflow runs regression tests in parallel, generates JUnit and Allure results, builds HTML, preserves Allure history and publishes the report to the `gh-pages` branch.

One-time GitHub Pages configuration:

**Settings → Pages → Build and deployment → Source → Deploy from a branch → `gh-pages` / root**.

Expected report URL:

```text
https://<github-user>.github.io/<repository-name>/
```

## 8. What was validated before packaging

- Python source compilation: passed
- Workflow YAML parsing: passed
- Security sanitizer smoke check: passed
- Estimated full collection: 39 executions
- Empty legacy `step_definitions` directory removed
- Duplicate legacy booking feature removed
- Authentication BDD added
- Allure request/response evidence centralized in `BaseClient`
- Allure HTML generation + GitHub Pages workflow added
