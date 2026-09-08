# Test Strategy

## Test pyramid for this API framework

### Smoke
Fast checks for API availability and critical authentication/booking behavior.

### Regression
The complete functional API suite, including CRUD, chaining and important validation paths.

### Negative
Invalid IDs, invalid payloads, invalid credentials and unauthorized mutations.

### Contract
JSON Schema validation verifies that successful API responses maintain the expected structure and data types.

### BDD
Business-readable Given/When/Then scenarios demonstrate behavior-focused acceptance coverage.

## Test isolation

Stateful tests create their own booking records and use the returned booking ID. Tests should not depend on another test's execution order.

## Data strategy

Factories create valid domain objects. Dedicated datasets cover invalid and boundary conditions. This separates test intent from payload construction.

## CI strategy

The regression suite runs in parallel. JUnit XML is retained for CI consumers and Allure HTML is published as a browsable report.

## Risk-based priorities

1. Authentication and authorization
2. CRUD correctness and persistence
3. Contract/schema integrity
4. Invalid input handling
5. Health/availability
6. Reporting and diagnostics

## Exit criteria

- Required marker suites pass.
- No known test-isolation failures under xdist.
- Allure report generated.
- Secrets are absent from report/log attachments.
- CI artifacts are available for failures.
