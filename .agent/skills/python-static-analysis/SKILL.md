---
name: python-static-analysis
description: Instructions for utilizing Ruff and Mypy for static analysis.
---

# Python Static Analysis

Python is a dynamic language, so we enforce correctness and style using two powerful tools:

## 1. Ruff (Fast Linter & Formatter)
Ruff replaces Flake8, Black, Isort, and many others.
- Always run `ruff format .` to organize the source code structure.
- Always run `ruff check .` to catch style issues, unused imports, or bad practices.
- For AI auto-fixes, you can use `ruff check --fix .`.

## 2. Mypy (Static Type Checker)
- Run `mypy --strict .` to catch type inconsistencies early.
- You must annotate all function parameters and return types using Python 3.10+ unions (`|`) and generics (`dict`, `list` instead of `typing.Dict`, `typing.List`).
- If you run into strict errors because an external untyped library is used, use `# type: ignore` with extreme prejudice and caution, adding a comment explaining why it is safe.
