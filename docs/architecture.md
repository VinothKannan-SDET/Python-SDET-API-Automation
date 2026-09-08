# Framework Architecture

## Layers

### Test layer
`tests/` and `features/` express business scenarios and expected behavior.

### Data layer
`test_data/` owns reusable factories and datasets. This prevents test payload duplication.

### Domain client layer
`AuthClient` and `BookingClient` expose domain-specific operations such as `create_booking()` and `update_booking()`.

### Transport layer
`BaseClient` owns `requests.Session`, URL construction, timeout, common HTTP methods and centralized Allure evidence.

### Contract layer
`schemas/` contains JSON Schema definitions used by contract tests.

### Utility layer
Assertions, configuration, logging, security sanitization and Allure metadata live in `utilities/`.

## Request flow

```text
pytest test
  -> BookingClient
  -> BaseClient
  -> requests.Session
  -> REST API
  -> response
  -> BaseClient evidence
  -> assertions/schema validation
```

## Why this design?

- Tests remain readable.
- Endpoint knowledge is centralized.
- Transport changes do not require editing every test.
- Test data is reusable.
- Reporting/security behavior is consistent across APIs.
- The architecture can grow to additional domain clients without creating a monolithic client.

## Parallel execution

Tests use dynamically created records for stateful CRUD flows. This avoids dependence on a shared booking ID and makes xdist execution safer.
