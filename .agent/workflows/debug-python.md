---
trigger: "/debug-python"
description: "Workflow for debugging Python code using PDB and log analysis."
---

# Workflow: Python Debugging

**Context**: The user is experiencing a bug, crash, or unexpected behavior in Python.

## Steps
1. **Identify the Symptom**: Analyze the traceback or error message.
2. **Reproduce**: Run the script to confirm the failure.
3. **Traceback Analysis**:
   - Use `rich.traceback` or standard traceback analysis to identify the failing line.
4. **Interactive Debugging**:
   - Suggest inserting `breakpoint()` at the suspicious location.
   - Run the script and guide the user through PDB commands (`n`, `s`, `c`, `p`).
5. **Logging**:
   - Check if the application has logging enabled.
   - Suggest increasing log level to `DEBUG`.
6. **Apply Fix**: Once identified, propose the fix and verify via `/test-coverage-python` or standard `pytest`.
