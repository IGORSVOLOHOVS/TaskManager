---
trigger: "/build-python"
description: "Workflow for setting up Python environment and dependencies."
---

# Workflow: Python Environment Setup

**Context**: The user wants to ensure their Python environment is correctly initialized and all dependencies are installed.

## Steps
1. Detect dependency management system (`requirements.txt`, `pyproject.toml`, `setup.py`).
2. If using `pip` and `requirements.txt`:
   ```bash
   python3 -m pip install -r requirements.txt
   ```
3. If using `poetry`:
   ```bash
   poetry install
   ```
4. If a virtual environment is missing, suggest:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Linux/macOS
   .venv\Scripts\activate     # On Windows
   ```
5. Verify installation by listing packages:
   ```bash
   pip list
   ```
6. If build errors occur, invoke `@python-specialist` for troubleshooting.
