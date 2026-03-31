---
name: testing-and-coverage
description: Doctest scenarios and coverage analysis using lcov.
---

# C++ Testing & Coverage Framework

> "If it's not tested, it's already broken."

## 1. Doctest Framework
Every component must have an associated test file in `tests/` using the single-header `<doctest/doctest.h>`.

### Test Case Structure:
```cpp
#include <doctest/doctest.h>
#include "my_core_logic.hpp"

TEST_CASE("Validate Business Logic") {
    // Arrange
    int input = 42;

    SUBCASE("Success Path") {
        // Act
        auto res = process_data(input);
        // Assert
        REQUIRE(res.has_value());
        CHECK(res.value() == 10);
    }
}
```

---

## 2. AAA Pattern
Separate tests logically for clarity:
- **Arrange:** Set up deterministic inputs.
- **Act:** Execute the function under test.
- **Assert:** Validate output against the expected value.

---

## 3. Test Coverage (LCOV / GCov)
To ensure all code paths are reached, use the automated coverage wrapper.

### Commands:
```bash
python3 .agent/scripts/run_test_coverage.py
```
- **Targets:** 100% coverage for all files in `src/core/`.
- **Exclusions:** Tests should not cover third-party libraries or boilerplate `main.cpp`.

---

## 4. Best Practices
- **No Side Effects:** Tests must not depend on global state or external files.
- **Deterministic:** Given the same input, a test MUST always produce the same result.
- **Unit vs Integration:** Core tests must be pure unit tests (CPU only). Shell tests managing I/O belong in separate "Integration" scenarios.

---

## 5. Anti-Patterns
- **Catching Exceptions in Tests:** Let the test framework catch failures.
- **Ignoring Edge Cases:** Only testing the "Happy Path".
- **Hidden Coverage:** Deleting lines of code only because they are hard to test.

> **Rule:** If a function is hard to test, it is likely too complex. Refactor into smaller, pure functions first!
