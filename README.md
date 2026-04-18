# Antigravity Polyglot Kit (C++ & Python)

> Professional AI Agent templates for Modern C++23 & Python 3.10+ Development

<div align="center">
    <img src="https://img.shields.io/badge/C%2B%2B-23-blue?style=for-the-badge&logo=c%2B%2B" alt="C++23" />
    <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python 3.10+" />
    <img src="https://img.shields.io/badge/Architecture-Functional%20Core-green?style=for-the-badge" alt="Functional Core" />
    <img src="https://img.shields.io/badge/AI-Agentic%20Coding-orange?style=for-the-badge" alt="Agentic Coding" />
</div>

---

## 🚀 Quick Setup

The fastest way to bootstrap a new project is using the consolidated installer:

### 1. Install the CLI (One-time)
Download and run the installer from the [latest release](https://github.com/IGORSVOLOHOVS/antigravity-kit-cpp/releases/latest/download/install_github.py):
```bash
python3 install_github.py --install
```

### 2. Initialize a Project
In any project directory, run:
```bash
ai-init
```

Alternatively, you can run the installer without flags to initialize the current directory:
```bash
python3 install_github.py
```

### ⚠️ Important Note on `.gitignore`
If you are using AI-powered editors like **Cursor** or **Windsurf**, do **NOT** add the `.agent/` folder to your `.gitignore`. This ensures the IDE can index the workflows and rules, making slash commands (like `/build`, `/refactor`) visible in the chat suggestions.

---

## 📚 What's Included

| Component        | Count | Description                                                                   |
| ---------------- | ----- | ----------------------------------------------------------------------------- |
| **Agents**       | 11    | Specialist AI personas (Architect, C++ Specialist, Python Specialist, etc.)   |
| **Skills**       | 18    | Domain-specific knowledge (CMake, TDD, Pytest, Ruff, Security, etc.)          |
| **Workflows**    | 24    | Slash command procedures for dev automation (C++ & Python)                    |
| **Rules**        | 19    | Architectural & coding standards (CPP_FUNCTIONAL_CORE, PYTHON_CLEAN_CODE etc.)|
| **Prompts**      | 7     | Reusable instruction templates for complex multi-step operations               |
| **Modern C++**   | 23    | **C++23 Standalone** (std::expected, Ranges, Concepts, Monads)                |
| **Python**       | 3.10+ | **Strict Typings & Sec** (ruff, mypy, uv, pytest, bandit, vulture)            |

---

## 🤖 Usage: Using Agents

**No need to mention agents explicitly!** The system automatically detects and applies the right specialist(s) based on your request and the file types you are editing:

```
You: "Implement a thread-safe message queue using std::variant"
AI: 🤖 Applying @cpp-specialist + @systems-architect...

You: "Create an async API client using httpx"
AI: 🤖 Applying @python-specialist...

You: "Where is the memory leak in this loop?"
AI: 🤖 Using @debugger for systematic ASan analysis...
```

**Benefits:**
- ✅ **Zero learning curve** - just describe the technical problem.
- ✅ **Always expert responses** - grounded in C++ and Python architecture rules.
- ✅ **Transparent** - the system shows which specialized knowledge is active.

---

## ⚡ Usage: Using Workflows

Invoke automated procedures with slash commands:

### C++ Workflows
| Command                   | Description                                                |
| ------------------------- | ---------------------------------------------------------- |
| `/build-cpp`              | Compile the project using CMake and Presets                |
| `/test-coverage-cpp`      | Run C++ doctest and generate LCOV coverage reports         |
| `/benchmark-cpp`          | Run nanobench performance micro-benchmarks                 |
| `/refactor-cpp`           | Convert legacy code to Functional Core C++23               |
| `/plan-architecture-cpp`  | Generate ISO 25010 compliant C4 architecture               |
| `/static-analyze-cpp`     | Run Clang-Tidy and CppCheck static analysis                |
| `/pack-cpp`               | Build release artifacts (DEB, ZIP, NSIS) via CPack         |
| `/docs-cpp`               | Generate Doxygen and Mermaid.js documentation              |
| `/debug-cpp`              | Systematic debugging of crashes and UB                     |
| `/init-project-cpp`       | Bootstrap a new C++ project from template                  |
| `/optimize-cpp`           | Profile CPU and Memory bottlenecks (perf/valgrind)         |

### Python Workflows
| Command                   | Description                                                |
| ------------------------- | ---------------------------------------------------------- |
| `/build-python`           | Set up Python environment and install dependencies (uv)    |
| `/format-python`          | Auto-format Python code using Ruff                         |
| `/lint-python`            | Check Python code using Ruff, Mypy, Vulture, Bandit        |
| `/test-coverage-python`   | Run pytest sweeps and generate HTML coverage report        |
| `/docs-python`            | Generate HTML documentation from docstrings using pdoc     |
| `/debug-python`           | Systematic Python debugging using PDB and log analysis     |
| `/benchmark-python`       | Run Python performance benchmarks with pytest-benchmark    |
| `/refactor-python`        | Refactor legacy Python code to modern, clean patterns      |
| `/plan-architecture-python` | Generate ISO 25010 compliant architecture for Python     |
| `/static-analyze-python`  | Run Bandit, Vulture, and Radon for deep security analysis  |
| `/optimize-python`        | Profile and optimize Python performance bottlenecks        |
| `/pack-python`            | Build Python distribution artifacts (Wheels, sdist)        |
| `/init-project-python`    | Bootstrap a new Python project with uv, Ruff, Mypy         |

Example:
```
/refactor-cpp this class to use std::expected instead of exceptions
/lint-python all files in the src/ directory
/test-coverage-python
/benchmark-cpp after optimizing the hot path
```

---

## 💡 Custom Prompts

Custom prompts are automated templates located in `.agent/prompts/`. They help standardize complex operations by providing predefined instructions that you can invoke manually.

**How to use:** Reference the prompt file using `@` (e.g., `@git-deploy.md`) and ask the agent to follow it.

| Prompt | Description |
| ------ | ----------- |
| `plan-tools-capabilities.md` | Enhances implementation plans with a detailed checklist of used Agents, Rules, and Skills. |
| `git-deploy.md` | Standardizes commit/push following `GIT_WORKFLOW.md` conventions. |
| `verify.md` | Critically evaluates if the previous step was performed correctly and according to standards. |
| `extract-context.md` | Synthesizes a high-density session summary for transferring context to a new window. |
| `split-task-by-context.md` | Decomposes a large plan into independent sub-tasks for parallel multi-window execution. |
| `init-workflow-prompts.md` | Meta-prompt: generates a `workflow_prompts/` directory with 25 professional lifecycle prompts. |
| `optimize-prompt.md` | Transforms any rough draft prompt into a high-density, expert-level professional instruction. |

---

## 🛠️ Internal Scripts (Automation)

The kit includes a suite of Python automation wrappers located in `.agent/scripts/`:

**C++ Scripts:**
- `verify_all.py` — The ultimate verification tool (Format -> Lint -> Build -> Test)
- `run_benchmarks.py`, `run_static_analysis.py`, etc.

**Python Scripts:**
- `format_python.py` — Runs `uv run ruff format`
- `lint_python.py` — Runs Ruff, Mypy, Bandit, Vulture, and Radon
- `run_pytest_coverage.py` — Generates pytest htmlcov stats
- `docs_python.py` — Generates API reference via pdoc
- `verify_all_python.py` — Ultimate verification (Format -> Lint -> Test)

---

## 🗺️ Standards & Rules

The AI strictly follows 19 structured rule files for both C++ and Python. All rules are located in `.agent/rules/`.

**C++ Rules:** `CPP_ARCHITECTURE`, `CPP_BENCHMARK`, `CPP_CI_CD_DOCKER`, `CPP_CLEAN_ARCH`, `CPP_CONCURRENCY`, `CPP_CQRS`, `CPP_DDD`, `CPP_DOD`, `CPP_FUNCTIONAL_CORE`, `CPP_LOGGING`, `CPP_STATIC_ANALYSIS`, `CPP_TDD`, `CPP_TESTING`

**Python Rules:** `PYTHON_ARCHITECTURE`, `PYTHON_CLEAN_CODE`, `PYTHON_PACKAGE_MANAGEMENT`, `PYTHON_TESTING`

**Universal Rules:** `GEMINI` (P0 system rules), `GIT_WORKFLOW` (commits & branching)

---

## License

MIT © IGORSVOLOHOVS
