# 🔄 Agent Flow Architecture (C++)

> **Antigravity C++ Kit** - Professional AI Agent Workflow Documentation

---

## 📊 Overview Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER REQUEST                             │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    REQUEST CLASSIFICATION                        │
│  • Analyze intent (build, debug, benchmark, refactor, etc.)     │
│  • Identify domain (core-logic, systems-arch, performance)      │
│  • Detect complexity (simple, medium, complex)                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
                ▼                         ▼
    ┌───────────────────┐      ┌──────────────────┐
    │ WORKFLOW COMMAND  │      │  DIRECT AGENT    │
    │  (Slash Command)  │      │  ASSIGNMENT      │
    └─────────┬─────────┘      └────────┬─────────┘
              │                         │
              ▼                         ▼
    ┌───────────────────┐      ┌──────────────────┐
    │ /build            │      │ Agent Selection  │
    │ /test-coverage    │      │ Based on Domain  │
    │ /benchmark        │      │                  │
    │ /refactor         │      │ • core-logic     │
    │ /plan-arch        │      │ • systems-arch   │
    │ /debug            │      │ • performance    │
    │ /static-analyze   │      │ • build-devops   │
    │ /optimize         │      │ • security       │
    └─────────┬─────────┘      └────────┬─────────┘
              │                         │
              └────────────┬────────────┘
                           │
                           ▼
          ┌─────────────────────────────────────┐
          │       AGENT INITIALIZATION          │
          │  • Load agent persona/role          │
          │  • Load required skills             │
          │  • Apply Functional Core rules      │
          └──────────────┬──────────────────────┘
                         │
                         ▼
          ┌─────────────────────────────────────┐
          │      SKILL LOADING PROTOCOL         │
          │                                      │
          │  1. Read SKILL.md (C++ Standards)   │
          │  2. Apply Memory Safety Patterns    │
          │  3. Setup Build Environment         │
          │  4. Apply Testing Paradigms         │
          └──────────────┬──────────────────────┘
                         │
                         ▼
          ┌─────────────────────────────────────┐
          │         TASK EXECUTION              │
          │                                      │
          │  • Analyze C++23 codebase           │
          │  • Apply Functional Core purity     │
          │  • Generate STL/Range-based code    │
          │  • Run local validations            │
          └──────────────┬──────────────────────┘
                         │
                         ▼
          ┌─────────────────────────────────────┐
          │      VALIDATION LAYER               │
          │                                      │
          │  Verification (verify_all.py):      │
          │  • Format (clang-format)            │
          │  • Static Analysis (clang-tidy)     │
          │  • Compilation (CMake Presets)      │
          │  • Test Suite (doctest)             │
          │  • Coverage Analysis (LCOV)         │
          │  • Benchmarks (nanobench)           │
          │  • Sanitizers (ASan/UBSan)          │
          └──────────────┬──────────────────────┘
                         │
                         ▼
          ┌─────────────────────────────────────┐
          │         RESULT DELIVERY             │
          │  • Present changes to user          │
          │  • Provide technical rationale      │
          │  • Suggest next optimization steps  │
          └─────────────────────────────────────┘
```

---

## 🎯 Detailed Agent Workflow

### 1️⃣ **Request Entry Points**

```
User Input Types:
┌─────────────────────────────────────────────────────────────┐
│ A. Natural Language Request                                 │
│    "Implement a thread-safe cache with TTL"                 │
│                                                              │
│ B. Slash Command                                            │
│    "/refactor feature: use std::expected instead of catch"  │
│                                                              │
│ C. Domain-Specific Request                                  │
│    "Optimize memory usage" → performance-optimizer          │
│    "Audit security" → security-auditor                      │
│    "Fix CMake build" → cpp-specialist                       │
└─────────────────────────────────────────────────────────────┘
```

#### Socratic Gate Protocol (C++)

Before implementation, the agent must verify:

- **New Logic** → How does this affect the **Functional Core**?
- **Optimization** → Do we have a **nanobench** baseline?
- **Bug Fix** → Can we reproduce it with a **doctest** case?

### 2️⃣ **Agent Selection Matrix**

| Domain | Primary Agent | Key Skills Loaded |
| :--- | :--- | :--- |
| **System Design** | `systems-architect` | architecture, architecture-25010 |
| **Logic/Algorithm** | `cpp-specialist` | cpp-functional-core, clean-code |
| **Build/CI-CD** | `cpp-specialist` | cmake-build-system, docker-ci-cd |
| **Memory/Safety** | `security-auditor` | memory-management, vulnerability-scanner |
| **Optimization** | `perf-optimizer` | performance-profiling, cpp-dod |
| **Debugging** | `debugger` | systematic-debugging |
| **Testing** | `qa-automation` | testing-and-coverage, tdd-workflow |
| **Documentation** | `doc-writer` | plan-writing |

### 3️⃣ **Skill Loading Protocol**

Agents automatically load skills based on the technical context:

1. **Detection**: User mentions "Memory leak" → Trigger `memory-management`.
2. **Retrieval**: Load `.agent/skills/memory-management/SKILL.md`.
3. **Application**: Apply Ownership rules (Rule of Zero) and prevent raw `new`/`delete`.
4. **Validation**: Suggest running `ASan` via the `/debug` workflow.

---

## ⚡ Workflow Command Lifecycle

### `/build`
1. Detect **CMakePresets**.
2. Run `cmake --build` in parallel.
3. Report compilation errors with direct links to lines.

### `/test-coverage`
1. Build with **Coverage** flags.
2. Run **doctest** binary.
3. Generate **LCOV/HTML** report.
4. Identify uncovered branches in `src/core`.

### `/refactor`
1. Analyze legacy pattern (e.g., exceptions).
2. Propose **std::expected** or **Ranges** migration.
3. Ensure **Functional Core** purity is maintained.
4. Verify no performance regressions via `/benchmark`.

---

## 🛡️ Validation & Quality Gates

Every code modification must pass through the **Verification Pipeline**:

| Gate | Tool | Action |
| :--- | :--- | :--- |
| **Style** | `clang-format` | Enforce consistent code style |
| **Lint** | `clang-tidy` | Catch common C++ bugs and smells |
| **Safety** | `Sanitizers` | Detect ASan/UBSan violations at runtime|
| **Logic** | `doctest` | Run unit tests for functional core |
| **Perf** | `nanobench` | Prevent micro-benchmark regressions |

---

## 🎓 Best Practices

- **Core First**: Always implement logic in `src/core` before hooking it up to the `shell`.
- **Test First**: Use `/refactor` with the `tdd-workflow` skill to ensure tests grow with the code.
- **Plan First**: Use `/plan-architecture` to visualize C4 diagrams before large refactors.

---

**Last Updated**: 2026-03-31
**Version**: 1.0.0
