---
trigger: "/init-project-python"
description: "Workflow for bootstrapping a new Python project."
---

# Workflow: Initialize Python Project

**Context**: The user wants to start a new Python project or module with standard best practices.

## Steps
1. **Structure Creation**: Create recommended directory layout:
   ```bash
   mkdir src tests docs
   touch src/__init__.py tests/__init__.py
   ```
2. **Setup Dependencies**: Create `pyproject.toml` or `requirements.txt`.
3. **Initialize Git**:
   ```bash
   git init
   # Add standard .gitignore for Python
   ```
4. **Tooling Setup**:
   - Configure `ruff` for linting and formatting.
   - Configure `mypy` for strict type checking.
5. **Initial Script**: Create a basic `main.py` or entry point.
6. **Next Steps**: Advise the user to run `/build-python` to install tools.
