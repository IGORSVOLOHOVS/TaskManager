---
description: Workflow for building the C++ project using CMake.
---

# Build Workflow

1. Analyze if the user wants a Debug or Release build. Default to Debug if unspecified.
2. Run standard CMake configuration:
   ```bash
   cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
   ```
3. Copy `compile_commands.json` to the root directory for LSP functioning if needed:
   ```bash
   cp build/compile_commands.json .
   ```
4. Build the project using the python script or native cmake:
   ```bash
   cmake --build build -j $(nproc)
   ```
5. If the build fails, invoke the `cpp-specialist` or `debugger` to correct the compilation errors.
