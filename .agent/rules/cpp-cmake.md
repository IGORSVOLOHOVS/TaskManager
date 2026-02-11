---
trigger: model_decision
description: создайние CMakeLists.txt
---

Ты — Build Engineer. Твоя задача — создать или обновить `CMakeLists.txt`.

### 1. Глобальные настройки
- **CMake Version:** `cmake_minimum_required(VERSION 4.0)` (или новее).
- **Project:** Название проекта из `namespace`.
- **Standard:** `set(CMAKE_CXX_STANDARD 23)`, `set(CMAKE_CXX_STANDARD_REQUIRED ON)`.
- **Compile Commands:** `set(CMAKE_EXPORT_COMPILE_COMMANDS ON)` (для LSP).

### 2. Поиск файлов
- ИСПОЛЬЗУЙ `file(GLOB ...)` для поиска исходников, как требует заказчик.
- Пример: `file(GLOB CORE_SOURCES "core/*.cpp")`.

### 3. Флаги Компиляции
Настрой флаги в зависимости от типа сборки (`CMAKE_BUILD_TYPE`):
- **Release:**
  - `-O3` (Максимальная оптимизация).
  - `-flto` (Link Time Optimization).
  - `-DNDEBUG`.
- **Debug:**
  - `-O0` (Без оптимизации).
  - `-g` (Отладочная информация).
  - `--coverage` (Для gcov/lcov).
  - `-fsanitize=address,undefined` (Желательно, но опционально).

### 4. Линковка
- Не забудь слинковать библиотеки если есть.
- Для `std::stacktrace` может потребоваться линковка с системной библиотекой (например, `-lstdc++_libbacktrace` на GCC), добавь проверку или комментарий об этом.