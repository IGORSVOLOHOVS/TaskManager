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

| Component     | Count | Description                                                         |
| ------------- | ----- | ------------------------------------------------------------------- |
| **Agents**    | 11    | Specialist AI personas (Architect, C++ Specialist, Python Specialist, etc.)  |
| **Skills**    | 18    | Domain-specific knowledge (CMake, TDD, Pytest, Ruff etc.)      |
| **Workflows** | 15    | Slash command procedures for dev automation                         |
| **Modern C++**| 23    | **C++23 Standalone** (std::expected, Ranges, Concepts, Monads)      |
| **Python**    | 3.10+ | **Strict Typings & Sec** (ruff, mypy, uv, pytest, bandit, vulture)  |

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

### Global & C++ Workflows
| Command             | Description                                           |
| ------------------- | ----------------------------------------------------- |
| `/build`            | Compile the project using CMake and Presets           |
| `/test-coverage`    | Run C++ doctest and generate LCOV coverage reports        |
| `/benchmark`        | Run nanobench performance micro-benchmarks            |
| `/refactor`         | Convert legacy code to Functional Core C++23          |
| `/plan-architecture`| Generate ISO 25010 compliant C4 architecture          |
| `/static-analyze`   | Run Clang-Tidy and CppCheck static analysis           |
| `/pack`             | Build release artifacts (DEB, ZIP, NSIS) via CPack    |
| `/docs`             | Generate Doxygen and Mermaid.js documentation         |
| `/debug`            | Systematic debugging of crashes and UB                |
| `/init-project`     | Bootstrap a new C++ project from template             |
| `/optimize`         | Profile CPU and Memory bottlenecks (perf/valgrind)    |

### Python Workflows
| Command                 | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| `/format-python`        | Auto-format Python code using Ruff                    |
| `/lint-python`          | Check Python code using Ruff, Mypy, Vulture, Bandit   |
| `/test-coverage-python` | Run pytest sweeps and generate HTML coverage report   |
| `/docs-python`          | Generate HTML documentation from docstrings using pdoc|

Example:
```
/refactor this class to use std::expected instead of exceptions
/lint-python all files in the src/ directory
/test-coverage-python
```

---

## 💡 Custom Prompts

Custom prompts are automated templates located in `.agent/prompts/`. They help standardize complex operations by providing predefined instructions that you can invoke manually.

**How to use:** Reference the prompt file using `@` (e.g., `@git-deploy.md`) and ask the agent to follow it.

| Prompt | Description |
| ------ | ----------- |
| `plan-tools-capabilities.md` | Enhances implementation plans with a detailed checklist of used Agents, Rules, and Skills. |
| `git-deploy.md` | Standardizes the commit and push process following the development workflow. |
| `verify.md` | Critically evaluates if the previous step was performed correctly and according to standards. |
| `extract-window-brain.md` | Summarizes the current session's state, decisions, and progress for context transfer. |
| `split-by-context.md` | Decomposes a large plan into independent sub-tasks for parallel multi-window execution. |
| `init-workflow-prompts.md` | Meta-prompt that generates a `workflow_prompts/` directory with 25+ professional lifecycle prompts. |
| `optimize-prompt.md` | Professional Prompt Engineer tool that transforms simple requests into high-density, expert-level prompts. |

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

The AI strictly follows structured architectural styles for both C++ and Python.
Check `.agent/rules/` for all rules, including `CPP_FUNCTIONAL_CORE.md` and `PYTHON_CLEAN_CODE.md`.

---

## License

MIT © IGORSVOLOHOVS
