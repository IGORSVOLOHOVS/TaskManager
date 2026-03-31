---
description: Workflow for refactoring legacy code into modern C++23 functional core.
---

# /refactor

Execute the following steps to refactor the provided code snippet or file:

1. **Analyze Original Intent**: Understand what the legacy code is attempting to do (e.g., parsing, logic, state mutation).
2. **Apply Functional Core Rule**: Separate the side-effects (Imperative Shell) from the pure logic (Functional Core) strictly following `@[.agent/rules/CPP_FUNCTIONAL_CORE.md]`.
3. **Upgrade Idioms**: Use C++23 features (`std::ranges`, `std::views`, `constexpr`, `std::expected` instead of exceptions).
4. **Enforce Memory Safety**: Remove all raw pointers (`new`/`delete`) and replace them with `std::unique_ptr`, `std::span`, or `std::string_view`.
5. **Verify Style & Sanity**: Ask for the User's approval and instruct them that tests should be written via `@[.agent/workflows/test-coverage.md]`.
