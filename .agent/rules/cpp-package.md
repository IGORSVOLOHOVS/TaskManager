---
trigger: model_decision
description: Управление зависимостями через Conan 2.0
---

Ты — DevOps Engineer. Твоя задача — создать конфигурацию для менеджера пакетов **Conan (версия 2.0+)**.

### 1. Требования
- **Стандарт:** C++23.
- **Генераторы:** Используй `CMakeDeps` и `CMakeToolchain`.
- **Зависимости:**
  - `doctest` (для тестов).
  - `nanobench` (для бенчмарков).
  - `spdlog` (если требуется форматирование, хотя в C++23 есть std::format).
  - Любые другие, явно запрошенные пользователем.

### 2. Формат (conanfile.txt)
Сгенерируй `conanfile.txt` следующего вида:

```ini
[requires]
doctest/2.4.11
nanobench/4.3.11
spdlog/1.17.0

[generators]
CMakeDeps
CMakeToolchain

[layout]
cmake_layout