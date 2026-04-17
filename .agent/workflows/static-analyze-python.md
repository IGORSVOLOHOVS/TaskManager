---
trigger: "/static-analyze-python"
description: "Run comprehensive static analysis including security checks (Bandit) and deep linting."
---

# Workflow: Python Static Analysis

**Context**: The user wants a deep dive into code quality, including security vulnerabilities and complex type analysis.

## Steps
1. **Linting & Types**: Run standard linting (Ruff/Mypy) via `/lint-python`.
2. **Security Scan**: Run `Bandit` to find common security issues:
   ```bash
   bandit -r src/
   ```
3. **Complexity Analysis**: Run `Radon` or `Xenon` to check cyclomatic complexity:
   ```bash
   radon cc src/ -a
   ```
4. **Report**:
   - Highlight any security vulnerabilities for immediate fix.
   - List high-complexity functions as candidates for refactoring via `/refactor-python`.
5. **Guidance**: Use `@python-specialist` for deep analysis of identified issues.
