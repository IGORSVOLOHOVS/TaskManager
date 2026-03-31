# CPP_TESTING.md - C++ Testing & Coverage Standards

> **MANDATORY:** 100% Core coverage via `doctest`. AAA pattern strictly enforced.

## 1. Doctest Framework
Every component in the functional core must have an associated test file in `tests/` utilizing single-header `<doctest/doctest.h>`.

## 2. AAA Pattern
Separate tests logically:
- **Arrange:** Set up the deterministic inputs and mocks (if testing the shell).
- **Act:** Execute the function.
- **Assert:** Validate output against expectations.

Example with Subcases:
```cpp
#include <doctest/doctest.h>
#include "my_core_logic.hpp"

TEST_CASE("Validate Business Logic") {
    // Arrange
    int initial_state = 5;

    SUBCASE("Happy Path") {
        // Act
        auto res = process_data(initial_state, true);
        // Assert
        REQUIRE(res.has_value());
        CHECK(res.value() == 10);
    }

    SUBCASE("Error Path") {
        // Act
        auto res = process_data(initial_state, false);
        // Assert
        REQUIRE(!res.has_value());
        CHECK(res.error() == "Invalid Flag");
    }
}
```

## 3. Monadic Checks
Since the architecture relies on `std::expected` or `std::optional`, do not just `CHECK(res.value() == X)`. Always `REQUIRE(res.has_value())` first to prevent accidental `bad_expected_access` exceptions during testing.

## 4. Coverage Metrics
To ensure code paths are hit, utilize Python wrappers (like `run_test_coverage.py`) that hook into `lcov` (Linux) or `OpenCppCoverage` (Windows) to generate HTML coverage graphs. Merging PRs with dropped coverage is an automatic rejection.
