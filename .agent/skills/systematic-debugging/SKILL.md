---
name: systematic-debugging
description: 4-phase systematic debugging methodology for C++. Root cause analysis for segfaults, UB, and memory leaks.
---

# C++ Systematic Debugging

> "If you can't reproduce it, you can't fix it."

## Phase 1: Reproduce (RED)
Before any code change, create a minimal reproduction case.
- **Unit Test:** Prefer a new `doctest` case in `tests/`.
- **Input Data:** Isolate the exact input that triggers the failure.
- **Environment:** Check if it's compiler-specific or OS-specific.

## Phase 2: Isolate (ASAN/UBSAN)
Narrow down the source of the crash or logic error.
1. **Sanitizers:** Compile with `-fsanitize=address,undefined`.
2. **Backtrace:** Use `gdb` or `lldb` to find the exact line of failure.
3. **Variable Inspection:** Check for `nullptr`, out-of-bounds, or uninitialized variables.

## Phase 3: Understand (Root Cause)
Don't just fix the symptom (e.g., adding a null check). Find out *why* the pointer was null.
- **Ownership:** Who owns the object? Is there a Use-After-Free?
- **Logic:** Does the state machine match the requirements?
- **Concurrency:** Is there a race condition? (Use `-fsanitize=thread`).

## Phase 4: Fix & Verify (GREEN)
Apply the fix and verify it across all environments.
- **Verification:** The reproduction test MUST pass.
- **Regression:** Run the full test suite (`python .agent/scripts/run_test_coverage.py`).
- **Review:** Use `code-review-checklist` to ensure the fix follows Clean Code standards.

## Debugging Tools
- **GDB/LLDB:** Core dump analysis and breakpoints.
- **Valgrind:** Deep memory leak and cache-line analysis.
- **ASan/UBSan:** Instant feedback on memory/logic errors at runtime.
