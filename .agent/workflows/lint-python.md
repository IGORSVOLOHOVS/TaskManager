---
trigger: "/lint-python"
description: "Run Ruff and Mypy to catch structural and type errors."
---

# Workflow: Lint Python Code

**Context**: The user has asked to lint the Python codebase, ensuring all types are valid and structural PEP-8 violations are caught.

## Steps
1. Execute the python lint script:
   `python3 .agent/scripts/lint_python.py`
2. Present the warnings or errors to the user.
3. Suggest fixes for the errors encountered. Use `@python-specialist` to propose the correct type hint or structure.
