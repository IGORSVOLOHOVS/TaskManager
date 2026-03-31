# Antigravity C++ Kit

> Professional AI Agent templates for Modern C++23 Development

<div align="center">
    <img src="https://img.shields.io/badge/C%2B%2B-23-blue?style=for-the-badge&logo=c%2B%2B" alt="C++23" />
    <img src="https://img.shields.io/badge/Architecture-Functional%20Core-green?style=for-the-badge" alt="Functional Core" />
    <img src="https://img.shields.io/badge/AI-Agentic%20Coding-orange?style=for-the-badge" alt="Agentic Coding" />
</div>

---

## 🚀 Quick Setup

The fastest way to bootstrap a new project is using the consolidated installer:

### 1. Install the CLI (One-time)
Download and run the installer from the [latest release](https://github.com/IGORSVOLOHOVS/TaskManager/releases/latest/download/install_github.py):
```bash
python3 install_github.py --install
```

### 2. Initialize a Project
In any C++ project directory, run:
```bash
cpp-ai-init
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
| **Agents**    | 10    | Specialist AI personas (Architect, C++ Specialist, Security, etc.)  |
| **Skills**    | 15    | Domain-specific knowledge (CMake, Memory Management, TDD, etc.)      |
| **Workflows** | 11    | Slash command procedures for dev automation                         |
| **Modern C++**| 23    | **C++23 Standalone** (std::expected, Ranges, Concepts, Monads)      |

---

## 🤖 Usage: Using Agents

**No need to mention agents explicitly!** The system automatically detects and applies the right specialist(s) based on your request:

```
You: "Implement a thread-safe message queue using std::variant"
AI: 🤖 Applying @cpp-specialist + @systems-architect...

You: "Benchmark this sorting algorithm"
AI: 🤖 Using @performance-optimizer with nanobench...

You: "Where is the memory leak in this loop?"
AI: 🤖 Using @debugger for systematic ASan analysis...
```

**Benefits:**
- ✅ **Zero learning curve** - just describe the technical problem.
- ✅ **Always expert responses** - grounded in `CPP_FUNCTIONAL_CORE.md` standards.
- ✅ **Transparent** - the system shows which specialized knowledge is active.

---

## ⚡ Usage: Using Workflows

Invoke automated procedures with slash commands:

| Command             | Description                                           |
| ------------------- | ----------------------------------------------------- |
| `/build`            | Compile the project using CMake and Presets           |
| `/test-coverage`    | Run doctest and generate LCOV coverage reports        |
| `/benchmark`        | Run nanobench performance micro-benchmarks            |
| `/refactor`         | Convert legacy code to Functional Core C++23          |
| `/plan-architecture`| Generate ISO 25010 compliant C4 architecture          |
| `/static-analyze`   | Run Clang-Tidy and CppCheck static analysis           |
| `/pack`             | Build release artifacts (DEB, ZIP, NSIS) via CPack    |
| `/docs`             | Generate Doxygen and Mermaid.js documentation         |
| `/debug`            | Systematic debugging of crashes and UB                |
| `/init-project`     | Bootstrap a new C++ project from template             |
| `/optimize`         | Profile CPU and Memory bottlenecks (perf/valgrind)    |

Example:
```
/refactor this class to use std::expected instead of exceptions
/benchmark the performance of the matrix multiplication function
/test-coverage for the core math library
```

---

## 🛠️ Internal Scripts (Automation)

The kit includes a suite of Python automation wrappers located in `.agent/scripts/`:

- `verify_all.py` — The ultimate verification tool (Format -> Lint -> Build -> Test).
- `run_test_coverage.py` — Automated LCOV/OpenCppCoverage generator.
- `run_benchmarks.py` — Locates and executes all `bench_` targets.
- `run_static_analysis.py` — Parallelized Clang-Tidy runner.

---

## 🗺️ Standards & Rules

The AI strictly follows the **Atomic / Functional Core, Imperative Shell** architectural style.
Every code change is verified against:
- `CPP_FUNCTIONAL_CORE.md`
- `CPP_ARCHITECTURE.md`
- `CPP_MEMORY_MANAGEMENT.md`
- `CPP_TDD.md`

---

## License

MIT © IGORSVOLOHOVS
