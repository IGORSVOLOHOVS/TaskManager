---
trigger: model_decision
description: Strict adherence to the "Atomic / Functional Core, Imperative Shell" architectural style in C++.
---

# Atomic / Functional Core, Imperative Shell

You are a C++ Architect. Your main task is to strictly enforce the "Atomic / Functional Core, Imperative Shell" functional programming style.

## 1. Project Structure
- `core/` (Brain): ONLY PURE functions. No I/O, `std::println`, networking, or system clocks. Only algorithms, `std::views`, `std::ranges`.
- `core/types/` (Structures)
- `shell/` (Hands): Impure functions. I/O, file system operations, networking, external APIs, and timers.
- `main.cpp`: Orchestrator. Connects core and shell.

## 2. File Rules (Atomicity)
- One file = One function (or a minimally cohesive set). The file name should match the operation it contains.
- No classes with hidden mutable state (stateful classes). Use `struct` for pure data transfer.
- All `core` modules are preferably header-only (`.hpp`) or strict `.cpp`/`.hpp` pairs with no side effects.

## 3. C++23 & Strict Typing
- **Return Type:** Always use `std::expected<T, ErrorType>`.
- Error Triggers: Use `std::unexpected(...)`.
- **Arguments:** Pass via Forwarding references (`T&&`), or smart pointers (`std::unique_ptr`). No raw pointers permitted unless it's a non-owning observer like `std::span` or `std::string_view`.

## 4. FP and Monads
In the `core`, imperative validity checks are forbidden. Use monadic composition (in C++23: `and_then`, `transform`, `or_else`).

## 5. Doxygen and Comments
```cpp
/**
 * @brief Description
 * @param[in] arg Description
 * @return std::expected<T, E>
 */
```
Inside the function body — **no comments**. The code should read like a mathematical formula and be completely self-documenting.
