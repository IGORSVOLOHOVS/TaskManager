---
name: cpp-functional-core
description: Functional Core, Imperative Shell architectural style in C++.
---

# Functional Core, Imperative Shell (C++)

> "Core for calculation; Shell for action."

## 1. The Functional Core (src/core)
The core contains only deterministic, side-effect-free logic.

### Rules:
- **Purity:** No console I/O, no database access, no network calls.
- **Immutability:** Prefer returning data structures rather than modifying in-place.
- **Monads:** Use `std::expected<T, E>` or `std::optional<T>` instead of throwing exceptions.
- **Constexpr:** Mark functions as `constexpr` wherever possible.

---

## 2. The Imperative Shell (src/shell)
The shell manages all external communication and state mutation.

### Rules:
- **Unpacking:** It calls the core, receives `std::expected`, and decides what to do with errors (log, retry, or exit).
- **Communication:** This is the only place where `spdlog`, `sqlite3`, or any I/O lives.
- **Initialization:** Sets up threads and resources before handing execution to the core.

---

## 3. Benefits of Separation
- **Testability:** The Core can be 100% covered via simple unit tests without mocks.
- **Understandability:** Logic is separated from the "noise" of hardware and third-party APIs.
- **Reliability:** Errors are handled explicitly via the type system, not implicitly via exceptions.

---

## 4. Directory Structure
```
src/
  core/           ← Pure logic (Functional)
    logic.hpp     ← Logic using std::expected
    types.hpp     ← Domain data structures
  shell/          ← External communication (Imperative)
    main.cpp      ← The entry point
    logger.cpp    ← High-level logging
    db_store.cpp  ← The implementation for SQL
```
---

## 5. Anti-Patterns
- **Logging in Core:** Never `#include <spdlog/spdlog.h>` in `src/core`.
- **Catching in Core:** Never use `try/catch` in pure logic.
- **Global State:** Core must not change any global or static variables.
