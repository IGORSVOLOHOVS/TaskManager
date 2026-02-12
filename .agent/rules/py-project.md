---
trigger: model_decision
description: Инициализация Python проекта с использованием uv, ruff и современной структуры.
---

Ты — Python Project Lead. Твоя задача — инициализировать проект с нуля по принципу "Functional Core, Imperative Shell".

### Строгая Последовательность Инициализации

**1. Инструментарий (из py-package.md)**
- Используй `uv` для управления зависимостями.
- Создай `pyproject.toml` с настройками `ruff` и `pyright`.

**2. Структура Директорий**
- Создай `src/core`, `src/shell`, `tests`, `docs`, `scripts`.

**3. Статический Анализ (из py-static-analyze.md)**
- Настрой `.ruff.toml` для форматирования и линтинга.
- Настрой `pyrightconfig.json` для строгой типизации.

**4. Документация (из py-documentation.md)**
- Создай `README.md` с описанием архитектуры.
- Создай `docs/index.md` для MkDocs.

**5. Локальный CI/CD (из py-ci-cd.md)**
- Создай `.pre-commit-config.yaml`.
