---
trigger: "/test-coverage-python"
description: "Run Pytest with coverage and output an HTML report."
---

# Workflow: Python Test Coverage

**Context**: The user wants to run tests for their Python code and identify uncovered logic.

## Steps
1. Execute the test runner python script:
   `python3 .agent/scripts/run_pytest_coverage.py`
2. Evaluate the stdout. If there are failing tests, use `@debugger` or `@python-specialist` to provide a root cause analysis path.
3. Inform the user of the final coverage percentage and point them to the `htmlcov/index.html` report.
