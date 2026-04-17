---
description: Workflow for running clang-tidy and cppcheck over the codebase.
---

# /static-analyze

When requested to run static analysis or if resolving warnings:

1. **Adopt Rules**: Read `@[.agent/rules/CPP_STATIC_ANALYSIS.md]`.
2. **Execution**: Run the Python wrapper to invoke `clang-tidy` across all source files.
// turbo-all
```bash
python3 .agent/scripts/run_static_analysis.py
```
3. **Analyze Output**: If there are warnings, you must address them immediately.
4. **Refactor**: Fix `bugprone-*`, `performance-*`, and `modernize-*` issues. Do not use `NOLINT` unless absolutely necessary.
5. **Verify**: Ensure the pipeline is clean after adjustments.
