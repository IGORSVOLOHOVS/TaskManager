---
trigger: "/benchmark-python"
description: "Workflow for running Python benchmarks using pytest-benchmark."
---

# Workflow: Python Benchmarking

**Context**: The user wants to measure the performance of their Python code.

## Steps
1. Identify the target functions or modules to benchmark.
2. Run benchmarks using `pytest`:
   ```bash
   pytest --benchmark-only
   ```
3. If specific benchmarks are requested, use the `-k` filter:
   ```bash
   pytest -k "test_benchmark" --benchmark-only
   ```
4. Analysis:
   - Compare results with baseline if available.
   - Use `@python-specialist` to suggest optimizations based on slow execution paths.
5. Report the results to the user in a table format.
