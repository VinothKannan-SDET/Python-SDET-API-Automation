# API Test Coverage Matrix

| Capability | Positive | Negative | Contract | BDD | Parallel-safe |
|---|---:|---:|---:|---:|---:|
| Health | Yes | - | - | - | Yes |
| Authentication | Yes | Yes | - | Yes | Yes |
| Create booking | Yes | Yes | Yes | Yes | Yes |
| Retrieve booking | Yes | Yes | Yes | Yes | Yes |
| Update booking | Yes | Yes | - | Yes | Yes |
| Patch booking | Yes | Yes | - | - | Yes |
| Delete booking | Yes | Yes | - | Yes | Yes |
| Filtering | Yes | - | - | - | Yes |
| Boundary data | Yes | - | - | - | Yes |

The framework intentionally targets meaningful risk coverage rather than maximizing test count with duplicate scenarios.

Current target: approximately 39 full pytest executions, including BDD scenarios.
