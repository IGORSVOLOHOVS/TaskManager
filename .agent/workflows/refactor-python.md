---
trigger: "/refactor-python"
description: "Workflow for refactoring legacy Python code into modern, maintainable patterns."
---

# Workflow: Python Refactoring

**Context**: The user wants to improve existing Python code without changing its external behavior.

## Steps
1. **Safety First**: Ensure test coverage is high via `/test-coverage-python`.
2. **Identify Smells**:
   - Long methods, deep nesting, or repetitive logic.
3. **Apply Modern Python Patterns**:
   - Use `dataclasses` for data structures.
   - Replace manual loops with list comprehensions or generators where appropriate.
   - Apply type hints for better LSP support and static analysis.
4. **Execution**:
   - Refactor in small, incremental steps.
   - Run tests after each step.
5. **Validation**:
   - Re-run `/lint-python` and `/test-coverage-python`.
6. **Documentation**: Update docstrings and comments to reflect changes.
