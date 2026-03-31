---
description: Workflow for generating release artifacts using Conan and CPack.
---

# /pack

When the user requests to build a release package or installer, execute the following steps:

1. **Validate Build**: Ensure the application compiles without errors in Release mode.
2. **Run CPack**: Trigger the packaging mechanism using CMake/CPack.
// turbo-all
```bash
cd build
cpack -G DEB
cpack -G ZIP
```
3. **Confirm Output**: Verify that the package artifacts (e.g., `.deb`, `.tar.gz`, `.zip` or `.exe`) were successfully generated in the build directory.
