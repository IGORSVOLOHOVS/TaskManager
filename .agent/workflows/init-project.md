---
description: Workflow for bootstrapping a new C++ project.
---

# Init Project Workflow

1. Create a root `CMakeLists.txt` enforcing C++23.
2. Create directory structures: `src/core/`, `src/shell/`, `tests/`, `docs/`.
3. Set up the testing framework by downloading or creating a `FetchContent` entry for `doctest` in `tests/CMakeLists.txt`.
4. Initialize a `.clang-format` file with a standard format (e.g., Google or LLVM but with an 100 character width).
5. Initialize a `.clang-tidy` config explicitly enabling `modernize-*`, `cppcoreguidelines-*`, `bugprone-*`, and `performance-*`.
6. Run `python .agent/scripts/format.py` and `python .agent/scripts/lint.py` to ensure the skeleton is cleanly initialized.
