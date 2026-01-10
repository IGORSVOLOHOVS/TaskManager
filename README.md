# 🛠️ C++ Interactive Build System (Jupyter)

> **A modern, Python-driven environment for building, testing, benchmarking, and analyzing C++23 projects.**

[![C++ Standard](https://img.shields.io/badge/C%2B%2B-23-blue.svg?logo=c%2B%2B)](https://isocpp.org/)
[![Build System](https://img.shields.io/badge/Build-Jupyter%20%2B%20SCons-orange)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 📖 Overview

This project demonstrates a **Notebook-First** approach to C++ development. Instead of relying solely on complex CLI build systems like CMake or Makefiles, the entire development lifecycle—dependency management, compilation, testing, coverage analysis, and documentation—is orchestrated through a single Jupyter Notebook (`builder.ipynb`).

This approach allows for:
* **Interactive Feedback:** See build logs, test results, and coverage reports immediately within the notebook.
* **Unified Pipeline:** A single script handles formatting, linting, building, and benchmarking.
* **Zero-Boilerplate:** The notebook generates the necessary project structure and configuration files on the fly.

## ✨ Features

* **C++23 Ready:** Configured for the latest standard (`-std=c++23`) using GCC/Clang.
* **Automated Dependency Management:** Automatically downloads header-only libraries (e.g., `doctest`, `nanobench`).
* **TDD Pipeline:** Runs unit tests before benchmarks. If tests fail, execution stops.
* **Code Coverage:** Generates HTML coverage reports using `lcov` with branch coverage support.
* **Performance Benchmarking:** Integrated `nanobench` for micro-benchmarking with HTML output.
* **Code Quality:**
    * **Formatting:** Auto-formats code using `clang-format` (Google Style).
    * **Linting:** Static analysis via `clang-tidy`.
    * **Documentation:** Auto-generates UML and API docs via `Doxygen`.

## 📂 Project Structure

The `builder.ipynb` script automatically maintains the following structure:

```text
.
├── builder.ipynb       # 🧠 The Build System & Runner
├── src/                # 📝 Source files (.cpp)
├── include/            # 📦 Header files (.h) & Dependencies
├── build/              # ⚙️ Artifacts (Binaries, Object files)
├── docs/               # 📚 Generated Doxygen documentation
├── .clang-format       # 🎨 Style configuration
└── .clang-tidy         # 🧹 Linter configuration

```

## 🚀 Getting Started

### Prerequisites

Ensure you have the following tools installed on your Linux system:

* **Python 3.10+** (with `jupyter` installed)
* **C++ Compiler:** `g++` (GCC 13+) or `clang++`
* **Build Tools:** `scons`
* **Analysis Tools:** `lcov`, `clang-format`, `clang-tidy`, `doxygen`, `graphviz`

```bash
# Ubuntu/Debian example
sudo apt install g++ scons lcov clang-format clang-tidy doxygen graphviz python3-pip
pip install notebook

```

### Usage

1. **Clone the repository:**
```bash
git clone [https://github.com/your-username/your-repo.git](https://github.com/your-username/your-repo.git)
cd your-repo

```


2. **Open the Builder:**
```bash
jupyter notebook builder.ipynb

```


3. **Run the Pipeline:**
* Execute the initialization cells to set up the directory structure.
* Run the **Pipeline** cell to build, test, and benchmark the code.
* Run the **Coverage** cell to view the code coverage report.
* Run the **Docs** cell to generate and view Doxygen documentation.



## 📊 Workflow Visualization

The `builder.ipynb` implements the following logic:

1. **Setup:** Check compiler version & download dependencies.
2. **Lint & Format:** Enforce style guidelines.
3. **Build:** Compile with `SCons` (Debug/Release/Coverage modes).
4. **Test:** Run `doctest` unit tests.
5. **Benchmark:** If tests pass, run `nanobench`.
6. **Report:** Open HTML results for Coverage and Benchmarks.
