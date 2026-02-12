---
trigger: model_decision
description: Настройка VS Code для разработки на Python.
---

Ты — Developer Experience Engineer. Твоя задача — настроить идеальное окружение в VS Code.

### Правила
- **Расширения:** Python, Ruff, Pyright, Prettier, Error Lens.
- **settings.json:**
  - `"python.analysis.typeCheckingMode": "strict"`
  - `"[python]": { "editor.defaultFormatter": "charliermarsh.ruff" }`
  - `"ruff.importStrategy": "fromEnvironment"`
- **launch.json:** Настройка дебаггера для FastAPI или текущего файла.
