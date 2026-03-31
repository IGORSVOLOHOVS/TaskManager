---
name: cmake-build-system
description: Advanced CMake patterns, modules, and target management.
---

# Modern CMake Build System

> "Stop thinking in files; start thinking in targets."

## 1. Target-Based Architecture
Every action in CMake should revolve around targets (`add_library`, `add_executable`).

### Key Commands:
- `target_include_directories(my_target PUBLIC/PRIVATE path)`
- `target_link_libraries(my_target PUBLIC/PRIVATE dependency)`
- `target_compile_features(my_target PUBLIC cxx_std_23)`

---

## 2. CMake Presets
Use `CMakePresets.json` at the root of the project to standardize build environments across all developers and CI/CD pipelines.

### Configure Presets:
- **Default:** Standard debug build with sanitizers.
- **Release:** Optimized build for performance.
- **Coverage:** Build with flags for `lcov` or `OpenCppCoverage`.

---

## 3. Dependency Management (Conan / CPM)
Prefer automated dependency management over manually managing `.a` or `.so` files.

- **Conan 2.0:** Use `conanfile.py` or `conanfile.txt` for large enterprise dependencies.
- **CPM / FetchContent:** Use for header-only or small libraries (like `doctest` or `nanobench`).

---

## 4. Best Practices
1. **No Absolute Paths:** Use `${CMAKE_CURRENT_SOURCE_DIR}` to keep the build portable.
2. **Export Compile Commands:** Set `CMAKE_EXPORT_COMPILE_COMMANDS=ON` to enable `clangd` and modern IDE features.
3. **Out-of-Source Build:** Never run `cmake .` — always use a separate `build/` directory.

---

## 5. Anti-Patterns
- **`include_directories()`** (Global) — use `target_include_directories()` instead.
- **`link_libraries()`** (Global) — use `target_link_libraries()` instead.
- **`add_definitions()`** — use `target_compile_definitions()` instead.

> **Rule:** If a setting is needed only for one target, use `PRIVATE`. If it's needed for anyone linking to that target, use `PUBLIC`.
