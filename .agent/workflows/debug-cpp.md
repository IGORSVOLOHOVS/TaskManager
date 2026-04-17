---
description: Workflow for debugging C++ crashes and undefined behavior.
---

# Debug Workflow

1. **Information Gathering**: Is it a Segfault, Race Condition, or memory leak? 
2. **Re-build with Sanitizers**: If no clear indication, modify the CMake configuration (`add_compile_options(-fsanitize=address -fsanitize=undefined)`) and rebuild.
3. **Execute**: Run the exact test or main binary that caused the crash.
4. **Analyze Traces**: Analyze the sanitizer output, mapping memory allocations back to source lines. Pay attention to `std::move` operations on resources that are subsequently accessed (Use-After-Move).
5. **Fix & Verify**: After fixing the C++ file, rebuild, run tests again to verify the crash is resolved, and remove the sanitizer flags if moving to Release caching.
