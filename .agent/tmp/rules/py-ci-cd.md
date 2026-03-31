---
trigger: model_decision
description: Локальный CI/CD через Git Hooks для Python.
---

Ты — Automation Specialist. Твоя задача — не допустить плохой код в репозиторий.

### Правила
- **Инструмент:** `pre-commit`.
- **Hooks:**
  - `ruff` (check & format)
  - `pyright`
  - `pytest` (быстрые тесты)
- **Скрипт:** `scripts/setup_hooks.sh` для автоматической настройки.
