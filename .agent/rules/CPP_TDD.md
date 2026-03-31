---
trigger: model_decision
description: Test-Driven Development methodology for C++. The test always comes before the implementation.
---

# CPP_TDD.md — Test-Driven Development

> **MANDATORY:** No implementation code may be written until a failing test exists that proves the requirement.

## 🔴 Red Phase — Write a Failing Test First
Before writing any logic, define the expected behavior as a `doctest` test case:
```cpp
#include <doctest/doctest.h>
#include "calculator.hpp" // doesn't exist yet — that's intentional

TEST_CASE("Calculator: add two positive integers") {
    auto result = add(3, 4);
    REQUIRE(result.has_value());
    CHECK(result.value() == 7);
}
```
The file **must not compile** initially. That is the "Red" signal.

## 🟢 Green Phase — Write the Minimum Code to Pass
Write only enough production code to make the test pass. No extras, no "future-proofing":
```cpp
// core/calculator.hpp
#pragma once
#include <expected>

[[nodiscard]] constexpr
std::expected<int, std::string> add(int a, int b) noexcept {
    return a + b;
}
```

## 🔵 Refactor Phase — Clean Up Without Changing Behavior
Once green, apply Concepts to constrain template parameters at compile time:
```cpp
template<typename T>
concept Numeric = std::integral<T> || std::floating_point<T>;

template<Numeric T>
[[nodiscard]] constexpr
std::expected<T, std::string> add(T a, T b) noexcept {
    return a + b;
}
```
Re-run tests — they must stay green.

## Rules for Agents
1. **Never write `src/` code before `tests/` code.** This is a hard block.
2. **One failing test per feature increment.** Don't accumulate 10 tests before going green.
3. **Test boundaries, not implementation details.** Test what the function *returns*, not *how* it computes it.
4. **Concepts over `static_assert`** for cleaner error messages at constraint sites.

## Anti-Patterns
- Writing the implementation and then retrofitting tests to match it ("TAD" — Test-After Development).
- Using unconstrained templates (`template<typename T>`) when a Concept can enforce the intent.
