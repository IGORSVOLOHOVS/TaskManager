# 🧠 C++ Agent Rules (TaskManager)

> **Централизованное хранилище контекстных правил (.cursorrules) для AI-агентов.**

Этот репозиторий содержит эталонные инструкции для LLM (Cursor, Windsurf, Copilot), которые превращают AI в Senior C++ инженера. Правила охватывают архитектуру, тестирование, сборку и документацию в соответствии со стандартами ISO/IEC 25010 и C++23.

---

## 📥 Скачать Правила

Всегда актуальная версия правил (ZIP-архив). Ссылка не меняется при обновлениях.

[![Download Rules](https://img.shields.io/badge/Download-Latest_Rules.zip-blue?style=for-the-badge&logo=archive)](https://github.com/IGORSVOLOHOVS/TaskManager/releases/download/latest/agent_rules.zip)

**Прямая ссылка:**
`https://github.com/IGORSVOLOHOVS/TaskManager/releases/download/latest/agent_rules.zip`

---

## 🚀 Как использовать

1. **Скачайте архив** по ссылке выше.
2. Распакуйте содержимое в папку `.agent/rules/` (или `.cursor/rules/`) в корне вашего проекта.
3. Добавьте ссылки на эти файлы в ваш `.cursorrules` или системный промпт.

### Пример `.cursorrules`
```markdown
# Project Context
@.agent/rules/architecture.md
@.agent/rules/cpp-style.md
@.agent/rules/cpp-test.md

```

---

## 📚 Состав пакета (Catalog)

Архив включает следующие модули знаний:

### 🏗️ Architecture & Design

* **`architecture.md`** — Принятие технических решений (ADR), ISO 25010 аттрибуты качества, C4 Model.
* **`requirements.md`** — Формализация требований (StRS, SyRS, SRS) по ISO 29148.
* **`func-core-inter-shell.md`** — Архитектурный стиль "Functional Core, Imperative Shell".

### 🛠️ C++ Engineering (C++23)

* **`cpp-project.md`** — Инициализация проекта с нуля (Full Setup).
* **`cpp-cmake.md`** — Современный CMake 3.25+ (Presets, Targets).
* **`cpp-package.md`** — Управление зависимостями через Conan 2.0.
* **`cpp-refactor.md`** — Идиомы C++20/23 (Concepts, Ranges, Monads).
* **`cpp-comments.md`** — Документирование кода (Doxygen) и чистота реализации.

### 🧪 QA & Testing

* **`cpp-test.md`** — Unit-тестирование (doctest).
* **`cpp-test-coverage.md`** — Анализ покрытия кода (lcov, OpenCppCoverage).
* **`cpp-benchmark.md`** — Микробенчмарки (ankerl::nanobench).
* **`cpp-static-analyze.md`** — Конфигурация Clang-Tidy и Clangd.

### 🚢 DevOps & Delivery

* **`cpp-ci-cd.md`** — Локальные Git Hooks и пайплайны.
* **`cpp-docker.md`** — Оптимизированные Dockerfile (Multi-stage).
* **`cpp-pack.md`** — Создание инсталлеров (CPack: DEB, ZIP, NSIS).
* **`update-v2.yml`** — Пример GitHub Actions для релизов.

### 🌐 Special Domains

* **`cpp-qt.md`** — Разработка Desktop GUI на Qt 6.
* **`cpp-web.md`** — Микросервисы на Crow + HTMX.
* **`random.md`** — Генератор идей для Pet-проектов.

---

## 🔄 Автоматизация (Pipeline)

Обновление правил происходит автоматически через GitHub Actions.
При каждом пуше в ветку `task_manager_v2`:

1. Собирается ZIP-архив из папки `.agent/rules`.
2. Тег `latest` переносится на текущий коммит.
3. Архив `agent_rules.zip` перезаливается в релиз `latest`.

---

### 🚀 Настройка Google Antigravity (Workflow)

#### 🧠 Модели (Выбор вычислительной мощности)
* **Gemini 3.1 Pro (High):** Фаза 2 (Анализ). Применяется для проектирования сложной архитектуры, реверс-инжиниринга и задач с высокой ценой ошибки. Выделяет максимум ресурсов на глубокие рассуждения.
* **Gemini 3.1 Pro (Low):** Фаза 3 (Созидание). Оптимальный баланс для написания основной бизнес-логики, рефакторинга и создания тестов.
* **Gemini 3 Flash:** Рутина. Делегирование скучной механики: форматирование, boilerplate-код, быстрые точечные правки.

#### ⚙️ Режимы работы (Уровень автономности)
* **Planning:** Фазы 1 и 2 (Исследование и Анализ). Агент изучает проект, генерирует план и согласовывает архитектуру до изменения кода. Идеально для разработки фич с нуля.
* **Fast:** Фаза 3 (Созидание). Прямое выполнение без циклов планирования. Подходит для изолированных задач, запуска скриптов и фикса локализованных багов.

#### 🎯 Контекст (Управление вниманием агента)
* **Files & Directories:** Строго ограниченный доступ только к файлам текущего скоупа.
* **Rules & Code Context:** Глобальные правила проекта (например, стандарты Doxygen-комментирования).
* **Terminal:** Анализ логов сборки и падающих тестов напрямую.
* **MCP Servers:** Интеграция с внешней инфраструктурой и БД для выполнения реальных запросов из IDE.

---

License: MIT
