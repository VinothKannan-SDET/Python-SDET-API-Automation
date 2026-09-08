"""Generate Allure metadata files after each test session."""

import json
import os
from pathlib import Path


def write_allure_metadata():
    results = Path("allure-results")
    results.mkdir(exist_ok=True)
    (results / "categories.json").write_text(
        json.dumps([
            {"name": "Assertion failures", "matchedStatuses": ["failed"], "messageRegex": ".*(AssertionError|assert).*"},
            {"name": "Broken / infrastructure", "matchedStatuses": ["broken"], "messageRegex": ".*(ConnectionError|Timeout|RequestException).*"},
            {"name": "Skipped tests", "matchedStatuses": ["skipped"]}
        ], indent=2), encoding="utf-8"
    )
    environment = (
        "framework=Python API Automation\n"
        "test_framework=pytest\n"
        "api=Restful Booker\n"
        f"python={os.getenv('PYTHON_VERSION', 'local')}\n"
        f"ci={os.getenv('CI', 'false')}\n"
    )
    (results / "environment.properties").write_text(environment, encoding="utf-8")
    executor = {
        "name": "GitHub Actions" if os.getenv("CI") else "Local",
        "type": "github" if os.getenv("CI") else "local",
        "buildName": os.getenv("GITHUB_WORKFLOW", "Local Run"),
        "buildUrl": (
            os.getenv("GITHUB_SERVER_URL", "") + "/" +
            os.getenv("GITHUB_REPOSITORY", "") + "/actions/runs/" +
            os.getenv("GITHUB_RUN_ID", "")
        ) if os.getenv("CI") else "",
        "reportName": "Python API Automation Allure Report"
    }
    (results / "executor.json").write_text(json.dumps(executor, indent=2), encoding="utf-8")
