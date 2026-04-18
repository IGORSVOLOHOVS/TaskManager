# 🔄 Agent Flow Architecture (C++ & Python)

> **Antigravity Kit** - Professional AI Agent Workflow Documentation

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
│  • Identify domain (C++, Python, Architecture, DevOps)          │
│  • Detect complexity (simple, medium, complex)                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                ┌────────────┴──────────────┐
                │                           │
                ▼                           ▼
    ┌───────────────────┐      ┌────────────────────────┐
    │  PROMPT TEMPLATE  │      │   WORKFLOW COMMAND     │
    │  (.agent/prompts) │      │   (Slash Command)      │
    └─────────┬─────────┘      └──────────┬─────────────┘
              │                           │
              ▼                           ▼
    ┌───────────────────┐      ┌────────────────────────┐
    │ git-deploy        │      │ C++ Workflows          │
    │ verify            │      │  /build-cpp            │
    │ extract-context   │      │  /test-coverage-cpp    │
    │ split-task-by-    │      │  /benchmark-cpp        │
    │   context         │      │  /refactor-cpp         │
    │ plan-tools-       │      │  /plan-architecture-cpp│
    │   capabilities    │      │  /debug-cpp            │
    │ optimize-prompt   │      │  /static-analyze-cpp   │
    │ init-workflow-    │      │  /optimize-cpp         │
    │   prompts         │      │                        │
    └─────────┬─────────┘      │ Python Workflows       │
              │                │  /build-python         │
              │                │  /lint-python          │
              │                │  /test-coverage-python │
              │                │  /benchmark-python     │
              │                │  /refactor-python      │
              │                │  /debug-python         │
              │                │  /static-analyze-python│
              │                │  /optimize-python      │
              │                └──────────┬─────────────┘
              │                           │
              └────────────┬──────────────┘
                           │
                           ▼
          ┌─────────────────────────────────────┐
          │       AGENT INITIALIZATION          │
          │  • Load agent persona/role          │
          │  • Load required skills             │
          │  • Apply domain rules (C++ / Python)│
          └──────────────┬──────────────────────┘
                         │
                         ▼
          ┌─────────────────────────────────────┐
          │      SKILL LOADING PROTOCOL         │
          │                                     │
          │  1. Read SKILL.md                   │
          │  2. Apply Memory/Safety Patterns    │
          │  3. Setup Build / Lint Environment  │
          │  4. Apply Testing Paradigms         │
          └──────────────┬──────────────────────┘
                         │
                         ▼
          ┌─────────────────────────────────────┐
          │         TASK EXECUTION              │
          │                                     │
          │  C++: Functional Core, STL/Ranges   │
          │  Python: Strict types, Ruff, Mypy   │
          │  • Apply domain rules               │
          │  • Run local validations            │
          └──────────────┬──────────────────────┘
                         │
                         ▼
          ┌─────────────────────────────────────┐
          │      VALIDATION LAYER               │
          │                                     │
          │  C++ (verify_all.py):              │
          │  • clang-format / clang-tidy        │
          │  • CMake Presets / doctest          │
          │  • LCOV / nanobench / Sanitizers    │
          │                                     │
          │  Python (verify_all_python.py):     │
          │  • Ruff format + lint               │
          │  • Mypy strict                      │
          │  • Pytest + coverage HTML           │
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
│    "Add Mypy strict validation to all modules"              │
│                                                             │
│ B. Slash Command                                            │
│    "/refactor-cpp feature: use std::expected"               │
│    "/lint-python all files in src/"                         │
│    "/benchmark-cpp after optimizing the hot path"           │
│                                                             │
│ C. Prompt Template                                          │
│    @[git-deploy.md] → stage, commit, push per GIT_WORKFLOW  │
│    @[verify.md]    → audit last step against standards      │
│    @[extract-context.md] → synthesize session summary       │
│                                                             │
│ D. Domain-Specific Request                                  │
│    "Optimize memory usage"  → performance-optimizer         │
│    "Audit security"         → security-auditor              │
│    "Fix CMake build"        → cpp-specialist                │
│    "Fix Mypy errors"        → python-specialist             │
└─────────────────────────────────────────────────────────────┘
```

#### Socratic Gate Protocol

Before implementation, the agent must verify:

- **New C++ Logic** → How does this affect the **Functional Core**?
- **New Python Logic** → Does this satisfy **strict Mypy** and **Ruff** rules?
- **Optimization** → Do we have a **nanobench** / **pytest-benchmark** baseline?
- **Bug Fix** → Can we reproduce it with a **doctest** / **pytest** case first?

### 2️⃣ **Agent Selection Matrix**

| Domain | Primary Agent | Key Skills Loaded |
| :--- | :--- | :--- |
| **System Design** | `systems-architect` | architecture, architecture-25010 |
| **C++ Logic/Algorithm** | `cpp-specialist` | cpp-functional-core, clean-code |
| **C++ Build/CI-CD** | `cpp-specialist` | cmake-build-system, docker-ci-cd |
| **Python Logic/API** | `python-specialist` | clean-code, python-static-analysis |
| **Python Packaging** | `python-specialist` | python-static-analysis, pytest-workflow |
| **Memory/Safety** | `security-auditor` | memory-management, vulnerability-scanner |
| **Performance** | `performance-optimizer` | performance-profiling |
| **Debugging** | `debugger` | systematic-debugging |
| **Testing** | `qa-automation-engineer` | testing-and-coverage, tdd-workflow |
| **Documentation** | `documentation-writer` | plan-writing |
| **Planning** | `project-planner` | plan-writing, architecture |
| **Orchestration** | `orchestrator` | all agents as subagents |

### 3️⃣ **Skill Loading Protocol**

Agents automatically load skills based on the technical context:

1. **Detection**: "Memory leak" → Trigger `memory-management`.
2. **Retrieval**: Load `.agent/skills/memory-management/SKILL.md`.
3. **Application**: Apply Ownership rules (Rule of Zero), prevent raw `new`/`delete`.
4. **Validation**: Suggest running ASan via `/debug-cpp`.

---

## ⚡ Workflow Command Lifecycle

### `/build-cpp`
1. Detect **CMakePresets**.
2. Run `cmake --build` in parallel.
3. Report compilation errors with direct links to lines.

### `/test-coverage-cpp`
1. Build with **Coverage** flags.
2. Run **doctest** binary.
3. Generate **LCOV/HTML** report.
4. Identify uncovered branches in `src/core`.

### `/refactor-cpp`
1. Analyze legacy pattern (e.g., exceptions).
2. Propose **std::expected** or **Ranges** migration.
3. Ensure **Functional Core** purity is maintained.
4. Verify no performance regressions via `/benchmark-cpp`.

### `/lint-python`
1. Run **Ruff** (format check + lint).
2. Run **Mypy** `--strict`.
3. Run **Vulture** for dead code.
4. Run **Bandit** for security issues.

### `/test-coverage-python`
1. Run **pytest** with `--cov`.
2. Generate **HTML** coverage report.
3. Fail if coverage drops below threshold.

---

## 🗂️ Prompt Template Reference

Reusable instruction templates in `.agent/prompts/`:

| Prompt | Purpose |
| :----- | :------ |
| `git-deploy.md` | Stage → Commit (GIT_WORKFLOW pattern) → Push |
| `verify.md` | Critically audit the previous step against standards |
| `extract-context.md` | Synthesize session state for context transfer |
| `split-task-by-context.md` | Decompose plan into parallel sub-tasks |
| `plan-tools-capabilities.md` | Enhance plans with Agents/Rules/Skills checklist |
| `optimize-prompt.md` | Transform rough drafts into expert-level prompts |
| `init-workflow-prompts.md` | Generate a full `workflow_prompts/` library (25 prompts) |

---

## 🛡️ Validation & Quality Gates

Every code modification must pass through the **Verification Pipeline**:

### C++

| Gate | Tool | Action |
| :--- | :--- | :--- |
| **Style** | `clang-format` | Enforce consistent code style |
| **Lint** | `clang-tidy` | Catch common C++ bugs and smells |
| **Safety** | `Sanitizers (ASan/UBSan)` | Detect memory and UB violations |
| **Logic** | `doctest` | Run unit tests for functional core |
| **Perf** | `nanobench` | Prevent micro-benchmark regressions |

### Python

| Gate | Tool | Action |
| :--- | :--- | :--- |
| **Format** | `ruff format` | Enforce consistent code style |
| **Lint** | `ruff check` | Catch style and logic issues |
| **Types** | `mypy --strict` | Enforce full type safety |
| **Security** | `bandit` | Detect common security vulnerabilities |
| **Logic** | `pytest` | Run unit and integration tests |
| **Coverage** | `pytest-cov` | Ensure coverage thresholds are met |

---

## 🎓 Best Practices

- **Core First (C++)**: Always implement logic in `src/core` before hooking it up to the `shell`.
- **Types First (Python)**: Annotate all functions before implementation; run `mypy --strict` continuously.
- **Test First**: Use `/refactor-cpp` or `/refactor-python` with the `tdd-workflow` skill.
- **Plan First**: Use `/plan-architecture-cpp` or `/plan-architecture-python` before large refactors.
- **Deploy**: Always use `@[git-deploy.md]` for consistent commits following `GIT_WORKFLOW.md`.

---

**Last Updated**: 2026-04-18
**Version**: 2.0.0
