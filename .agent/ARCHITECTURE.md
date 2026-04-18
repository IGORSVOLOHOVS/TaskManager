# Antigravity Kit — Agent Architecture

> This repository is powered by a polyglot multi-agent AI system for professional **C++23** and **Python 3.10+** development.

---

## 🗺️ System Map

```
.agent/
├── ARCHITECTURE.md          ← You are here
├── AGENT_FLOW.md            ← Full agent flow diagram & workflow lifecycle
├── mcp_config.json          ← MCP tool configuration
│
├── agents/      (11 files)  ← AI personas, each specializing in a distinct domain
├── rules/       (19 files)  ← Enforced coding & architectural standards
├── skills/      (18 dirs)   ← Domain-specific knowledge modules
├── workflows/   (24 files)  ← Slash command step-by-step procedures
├── prompts/     (7 files)   ← Reusable instruction templates for complex operations
├── scripts/                 ← Automation scripts for linting, testing, and coverage
└── templates/               ← Scaffold templates for new files and components
```

---

## 🤖 Agents (`agents/`)

11 specialist personas. The system auto-selects based on request domain:

| Agent | Specialty |
| :---- | :-------- |
| `cpp-specialist` | C++23 logic, build system, CMake |
| `python-specialist` | Python 3.10+, type safety, packaging |
| `systems-architect` | ISO 25010, C4 diagrams, ADRs |
| `performance-optimizer` | Profiling, nanobench, data-oriented design |
| `security-auditor` | Memory safety, sanitizers, Bandit |
| `debugger` | Systematic crash analysis, ASan/UBSan |
| `qa-automation-engineer` | TDD, doctest, pytest, coverage |
| `documentation-writer` | Doxygen, pdoc, Mermaid diagrams |
| `project-planner` | ISO 25010 planning, task decomposition |
| `orchestrator` | Multi-agent coordination and sub-tasking |
| `code-archaeologist` | Legacy code analysis and migration |

---

## 📏 Rules (`rules/`)

19 binding rule files. All are enforced automatically by the active agent.

**C++ Rules (13):**
`CPP_ARCHITECTURE` · `CPP_BENCHMARK` · `CPP_CI_CD_DOCKER` · `CPP_CLEAN_ARCH` · `CPP_CONCURRENCY` · `CPP_CQRS` · `CPP_DDD` · `CPP_DOD` · `CPP_FUNCTIONAL_CORE` · `CPP_LOGGING` · `CPP_STATIC_ANALYSIS` · `CPP_TDD` · `CPP_TESTING`

**Python Rules (4):**
`PYTHON_ARCHITECTURE` · `PYTHON_CLEAN_CODE` · `PYTHON_PACKAGE_MANAGEMENT` · `PYTHON_TESTING`

**Universal Rules (2):**
`GEMINI` (P0 — system-wide agent behavior) · `GIT_WORKFLOW` (commits & branching)

---

## 🧠 Skills (`skills/`)

18 domain-specific knowledge modules loaded on demand:

`architecture` · `architecture-25010` · `bash-linux` · `clean-code` · `cmake-build-system` · `code-review-checklist` · `cpp-functional-core` · `docker-ci-cd` · `memory-management` · `performance-profiling` · `plan-writing` · `pytest-workflow` · `python-advanced-features` · `python-static-analysis` · `systematic-debugging` · `tdd-workflow` · `testing-and-coverage` · `vulnerability-scanner`

---

## ⚡ Workflows (`workflows/`)

24 slash-command procedures (12 C++ · 12 Python):

**C++:** `/build-cpp` · `/test-coverage-cpp` · `/benchmark-cpp` · `/refactor-cpp` · `/plan-architecture-cpp` · `/static-analyze-cpp` · `/pack-cpp` · `/docs-cpp` · `/debug-cpp` · `/init-project-cpp` · `/optimize-cpp`

**Python:** `/build-python` · `/format-python` · `/lint-python` · `/test-coverage-python` · `/benchmark-python` · `/refactor-python` · `/plan-architecture-python` · `/static-analyze-python` · `/pack-python` · `/docs-python` · `/debug-python` · `/init-project-python` · `/optimize-python`

---

## 📋 Prompts (`prompts/`)

7 reusable instruction templates for complex operations:

| Prompt | Description |
| :----- | :---------- |
| `git-deploy.md` | Stage → Commit → Push following `GIT_WORKFLOW.md` |
| `verify.md` | Critically audit the previous step against standards |
| `extract-context.md` | Synthesize high-density session summary for context transfer |
| `split-task-by-context.md` | Decompose a large plan into parallel independent sub-tasks |
| `plan-tools-capabilities.md` | Enhance plans with Agents/Rules/Skills checklist |
| `optimize-prompt.md` | Transform rough drafts into expert-level prompts |
| `init-workflow-prompts.md` | Generate a full `workflow_prompts/` library (25 prompts) |

---

## ⚙️ Execution Flow

```
1. ROUTING
   User request → classified in GEMINI.md (P0 rules)
   → auto-selects agent from agents/
   → loads relevant skills from skills/

2. EXECUTION
   Agent pulls rules from rules/
   → follows procedures from workflows/ (or prompts/)
   → applies domain standards (CPP_FUNCTIONAL_CORE / PYTHON_CLEAN_CODE)

3. VERIFICATION
   C++    → python3 .agent/scripts/verify_all.py
              (clang-format, clang-tidy, CMake, doctest, LCOV, nanobench, ASan)

   Python → python3 .agent/scripts/verify_all_python.py
              (ruff format, ruff check, mypy --strict, pytest --cov, bandit)

4. DELIVERY
   Present changes → provide rationale → suggest next steps
```

---

**Last Updated**: 2026-04-18
**Version**: 2.0.0
