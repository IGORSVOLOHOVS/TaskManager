# Antigravity C++ Kit Skills Catalog

This document provides a map of all available "Skills" in the `.agent/skills/` directory. Each skill is a collection of instructions and patterns designed to guide the AI agents in specific domains.

---

## 🏗️ Architecture & Planning

| Skill | Description | Path |
|-------|-------------|------|
| **architecture-25010** | Enforces ISO/IEC 25010:2023 quality attribute scenarios. | `architecture-25010/` |
| **architecture** | ADR documentation, trade-off analysis, and pattern selection. | `architecture/` |
| **plan-writing** | Framework for breaking down work into verifiable tasks. | `plan-writing/` |
| **cpp-functional-core** | Focuses on Functional Core and Imperative Shell separation. | `cpp-functional-core/` |

---

## 🛠️ C++ Engineering & Build

| Skill | Description | Path |
|-------|-------------|------|
| **cmake-build-system** | Advanced CMake patterns, modules, and target management. | `cmake-build-system/` |
| **memory-management** | Rules for smart pointers, zero-copy, and memory safety. | `memory-management/` |
| **clean-code** | Universal C++ coding standards: SRP, DRY, KISS, YAGNI. | `clean-code/` |
| **bash-linux** | Essential terminal patterns for Linux environment automation. | `bash-linux/` |

---

## 🧪 Quality & Testing

| Skill | Description | Path |
|-------|-------------|------|
| **testing-and-coverage** | Doctest scenarios and coverage analysis using lcov. | `testing-and-coverage/` |
| **tdd-workflow** | The Red-Green-Refactor cycle and AAA testing pattern. | `tdd-workflow/` |
| **performance-profiling** | Profiling via nanobench, Valgrind, and perf tools. | `performance-profiling/` |
| **systematic-debugging** | 4-phase root cause analysis and verification process. | `systematic-debugging/` |
| **code-review-checklist** | Guidelines for reviewing C++ code for quality and security. | `code-review-checklist/` |

---

## 🛡️ Security & DevOps

| Skill | Description | Path |
|-------|-------------|------|
| **vulnerability-scanner** | Catching UB/Leaks using ASan, UBSan, and cppcheck. | `vulnerability-scanner/` |
| **docker-ci-cd** | Multi-stage Docker builds and automated CI pipelines. | `docker-ci-cd/` |

---

> **Note to Agents:** Always read the `SKILL.md` file within the relevant directory before performing significant work in that domain.
