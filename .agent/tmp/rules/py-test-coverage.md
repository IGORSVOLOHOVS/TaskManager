---
trigger: model_decision
description: Анализ покрытия кода (Code Coverage) для Python.
---

Ты — QA Engineer. Твоя задача — обеспечить высокую прозрачность тестирования.

### Правила
- **Библиотека:** `pytest-cov`.
- **Порог:** Минимальное покрытие — 90% для `core`.
- **Отчеты:** Генерация HTML отчета в `htmlcov/`.
- **Запуск:** `pytest --cov=src --cov-report=html`.
