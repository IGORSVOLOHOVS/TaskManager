# 🛠️ C++ Interactive Build System (Jupyter)

> **A modern, Python-driven environment for building, testing, benchmarking, and analyzing C++23 projects.**

Note: Этот репозиторий теперь использует автономных агентов (agents) для автоматизации задач внутри ноутбука и CI-пайплайна — см. раздел "Agents" ниже. Ok

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

* **Agents:** Некоторые этапы (скачивание зависимостей, генерация артефактов, обновление релизов) теперь выполняются агентами — автономными скриптами/процессами, которыми управляет `builder.ipynb` и CI.

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


# 🛠️ TaskManager — интерактивная система сборки для C++ (Notebook-first)

> Современный, интерактивный рабочий процесс для разработки C++23-проектов через Jupyter-ноутбук.

Ключевая идея: весь цикл разработки (зависимости → сборка → тесты → покрытие → бенчмарки → отчёты) управляется из единого `builder.ipynb`, а рутинные шаги автоматизируются автономными агентами (agents) в ноутбуке и в CI.

**Кратко:** интерактивно, воспроизводимо и удобно для TDD/benchmark-driven разработки.

**Преимущества:**
- **Интерактивность:** логи, тесты и отчёты видны прямо в ноутбуке.
- **Автоматизация:** агенты выполняют скачивание зависимостей, генерацию артефактов и публикацию релизов.
- **Унифицированный пайплайн:** форматирование, статический анализ, сборка и бенчмарки управляются централизованно.

**Короткий обзор возможностей**
- **C++23-ready:** флаги компилятора настроены на `-std=c++23`.
- **Тесты:** интеграция с `doctest` (TDD-поток).
- **Покрытие:** HTML-отчёты через `lcov`.
- **Бенчмарки:** микропрофилирование через `nanobench` с HTML-выходом.
- **Качество кода:** `clang-format`, `clang-tidy`, `doxygen`.
- **Агенты:** автономные обработчики задач для CI и локального запуска (см. раздел "Agents").

**Структура репозитория (ожидаемая)**

```text
.
├── builder.ipynb        # Основной ноутбук — оркестратор и контроллер агентов
├── src/                 # Исходники C++
├── include/             # Заголовки и внешние зависимости
├── build/               # Артефакты сборки
├── docs/                # Сгенерированные документы
├── .github/workflows/   # CI: workflow'ы, включая update-v2.yml
└── .clang-format
```

**Требования (Ubuntu/Debian пример)**

`sudo apt install g++ scons lcov clang-format clang-tidy doxygen graphviz python3-pip`
`pip install notebook`

**Быстрый старт**

1) Клонируйте репозиторий:

```bash
git clone https://github.com/IGORSVOLOHOVS/TaskManager.git
cd TaskManager
```

2) Откройте билд-ноутбук:

```bash
jupyter notebook builder.ipynb
```

3) Запустите секции ноутбука:
- Инициализация (создание директорий, загрузка зависимостей)
- Pipeline (lint → build → test → benchmark)
- Coverage / Docs (генерация отчётов)

**CI / релизы**

- Workflow [/.github/workflows/update-v2.yml](.github/workflows/update-v2.yml) автоматически обновляет тег `v2.0.0` и загружает `builder.ipynb` в релиз. CI работает в агентной модели: часть задач выполняется локально в ноутбуке, часть — как автономные шаги в Actions.

**Agents**

- **Что это:** лёгкие автономные компоненты (скрипты/процессы), которыми управляет `builder.ipynb` или CI, чтобы выполнять повторяемые задачи без ручного вмешательства.
- **Где используются:** скачивание зависимостей, генерация бинарников/документации, публикация релизов, сбор и публикация артефактов.
- **Как запускать:** через ячейки ноутбука или через CI-скрипты; агенты могут быть реализованы на Python (скрипты в ноутбуке) или как GitHub Actions шаги.

**Планы — Python-версия (Roadmap)**

- В ближайших релизах появится аналогичный интерактивный `builder.ipynb` для Python-проектов с теми же агентами:
    - управление виртуальными окружениями/зависимостями (`venv` / `pip` / `poetry`)
    - запуск тестов (`pytest`) и генерация покрытия (`coverage` / `lcov` через `pytest-cov`)
    - сбор документов (`Sphinx`) и публикация артефактов
    - шаблон `python/builder.ipynb` и пример CI для Python-агентов

Если хотите, могу сразу добавить минимальный шаблон `python/builder.ipynb` для старта.

**Контрибьюция**

- Открывайте PR в ветку `task_manager_v2`.
- Перед PR запустите ноутбук и проверьте, что ключевые секции (init → build → test) выполняются локально.

**Лицензия**
- MIT (см. LICENSE)

---

Если нужно, могу:
- добавить минимальный `python/builder.ipynb`-шаблон;
- обновить `builder.ipynb`, чтобы явно показывать команды запуска агентов;
- подготовить CI-шаблон для Python-агентов.
