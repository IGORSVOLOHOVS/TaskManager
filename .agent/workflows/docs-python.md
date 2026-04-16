---
trigger: "/docs-python"
description: "Generate Python documentation HTML using pdoc."
---

# Workflow: Generate Python Documentation

**Context**: The user has requested to generate HTML documentation for the Python codebase.

## Steps
1. Execute the documentation script:
   `python3 .agent/scripts/docs_python.py`
2. Point the user to the generated `docs/` directory and suggest opening `docs/index.html` in their browser.
