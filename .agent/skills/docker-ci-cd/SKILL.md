---
name: docker-ci-cd
description: C++ CI/CD, CMake setup, Packaging via CPack, and Docker multi-stage builds.
---

# C++ Docker & CI/CD Patterns

> "Reliable delivery starts with a clean environment."

## 1. Multi-Stage Docker Builds
Use multi-stage builds to optimize the final image size and separate build-time dependencies from the runtime environment.

### Builder Stage:
- **Build Image:** Contains compilers (gcc/clang), CMake, Conan, and development libraries.
- **Workflow:** Run `cmake .. && cmake --build .` inside this container.

### Final Stage:
- **Runtime Image:** Stripped-down image (like Alpine or Debian Slim) with only the binary and necessary runtime libraries.
- **Outcome:** Minimal surface area for security and smaller distribution size.

---

## 2. Automated CI Pipelines
Standardize with Git Hooks or GitHub Actions/GitLab CI.

### Mandatory Steps:
1. **Lint:** Run `clang-tidy` and `cppcheck` (`CPP_STATIC_ANALYSIS.md`).
2. **Build:** Test compilation on multiple platforms (Linux/Clang/GCC).
3. **Test:** Run all `doctest` cases (`CPP_TESTING.md`).
4. **Coverage:** Generate and store coverage reports (`CPP_TEST_COVERAGE.md`).
5. **Pack:** Generate artifacts via CPack (`/pack` workflow).

---

## 3. Environment Isolation
Never let host-machine quirks affect the build.

### Tools:
- **Dev Containers:** Use `.devcontainer.json` for consistent IDE experience.
- **CMake Presets:** Ensure every developer uses the same compiler flags.

---

## 4. Best Practices
- **Pin Versions:** Always use specific tags for base images (e.g., `gcc:13.2` instead of `latest`).
- **No Secrets in Images:** Use Docker Secrets or environment variables at runtime.
- **Clean Layers:** Chain commands (`apt update && apt install && rm -rf ...`) to keep layers small.

---

## 5. Anti-Patterns
- **Copying Entire Repo:** Never copy `.git` or `build/` into the Docker context.
- **Running as Root:** Always create a non-privileged user to run the final binary.
