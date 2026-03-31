---
description: Workflow for generating test coverage via CTest, lcov, or OpenCppCoverage.
---

# Test Coverage Workflow

1. **Verify Doctest Setup**: Ensure all `tests/*.cpp` files use `#include <doctest/doctest.h>`.
2. **Execute Script**: Run the unified coverage script:
   ```bash
   python3 .agent/scripts/run_test_coverage.py
   ```
3. **Analyze Output**: If it's Linux, the script will execute `lcov` and `genhtml`. On Windows, it invokes `OpenCppCoverage`.
4. **Report**: Read the summary line from the script's stdout or parse the `index.html` structure to inform the user of exactly which files are lacking line coverage. 
5. Emphasize testing the `core/` functions strictly, while mocking components interacting with the `shell/`.
