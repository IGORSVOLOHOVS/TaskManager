---
trigger: "/pack-python"
description: "Workflow for generating Python distribution artifacts (Wheels, Source Distributions)."
---

# Workflow: Package Python Project

**Context**: The user wants to package their Python code for distribution or deployment.

## Steps
1. **Metadata Check**: Ensure `pyproject.toml` or `setup.py` has correct versioning and description.
2. **Build Distribution**:
   ```bash
   python3 -m build
   ```
3. **Verify Artifacts**: Check `dist/` directory for `.whl` and `.tar.gz` files.
4. **Linting Check**: Use `twine check` on the artifacts:
   ```bash
   twine check dist/*
   ```
5. **Pre-release Checklist**:
   - Updates `CHANGELOG.md`.
   - Ensure all tests pass via `/test-coverage-python`.
6. **Deploy (Optional)**: If configured, suggest `twine upload` or `poetry publish`.
