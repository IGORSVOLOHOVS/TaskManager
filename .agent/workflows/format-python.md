---
trigger: "/format-python"
description: "Run Ruff to automatically format Python code."
---

# Workflow: Format Python Code

**Context**: The user has requested to format the Python codebase.

## Steps
1. Execute the `ruff format` using our wrapper script:
   `python3 .agent/scripts/format_python.py`
2. Report the files changed and confirm execution was successful.
