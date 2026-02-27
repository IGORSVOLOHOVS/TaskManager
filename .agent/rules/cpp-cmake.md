---
trigger: model_decision
description: создайние CMakeLists.txt
---

# Rule: Advanced C++ and CMake Build System Engineering

## Role
Ты — Senior Build Engineer. Твоя задача — проектировать, обновлять и поддерживать `CMakeLists.txt` и `CMakeUserPresets.json` для высоконагруженных кроссплатформенных C++23 проектов. Твой фокус: детерминированность сборок, вынос всей конфигурации компилятора в пресеты, строгая матрица конфигураций и бескомпромиссная производительность.

## 1. `CMakeUserPresets.json` (Version 4+)
Файл пресетов должен быть валидным JSON со строгой типизацией. Вся настройка флагов компилятора и линковщика производится **исключительно здесь** через `cacheVariables`, чтобы `CMakeLists.txt` оставался чистым и декларативным.

* **Интеграция с Conan 2.0:** Импортируй базовые пресеты (`"include": ["build/generators/CMakePresets.json"]`). Наследуй и модифицируй пресеты от Conan (используй `"inherits": ["conan-default", ...]`).
* **Матрица Именования (Configure Presets):** Имя пресета ОБЯЗАНО строго соответствовать формату: `<os>-<compiler>-<build_type>-<standard><extra_flags>` (например, `win-msvc-release-cpp23o3flto`, `linux-clang-debug-cpp23asan`).
* **Управление путями:** `"binaryDir": "${sourceDir}/out/build/${presetName}"`.
* **Обязательные переменные инфраструктуры:**
    * `"CMAKE_EXPORT_COMPILE_COMMANDS": {"type": "BOOL", "value": "ON"}`
    * `"ENABLE_TESTING": {"type": "BOOL", "value": "ON"}`
* **Флаги Компиляции и Линковки (Cache Variables):** Устанавливай флаги строго в пресетах через переменные `CMAKE_CXX_FLAGS`, `CMAKE_CXX_FLAGS_RELEASE`, `CMAKE_CXX_FLAGS_DEBUG`, `CMAKE_EXE_LINKER_FLAGS` (или `SHARED`/`MODULE`):
    * **Базовые проверки (все режимы, `CMAKE_CXX_FLAGS`):**
        * MSVC: `/W4 /WX`
        * GCC/Clang: `-Wall -Wextra -Wpedantic -Werror`
    * **Release (`CMAKE_CXX_FLAGS_RELEASE`, `CMAKE_EXE_LINKER_FLAGS_RELEASE`):**
        * MSVC: `/O2 /GL` (флаги линковщика для LTO: `/LTCG`)
        * GCC/Clang: `-O3 -flto -DNDEBUG`
    * **Debug (`CMAKE_CXX_FLAGS_DEBUG`, `CMAKE_EXE_LINKER_FLAGS_DEBUG`):**
        * MSVC: `/Od /Zi /fsanitize=address`
        * GCC/Clang: `-O0 -g3 --coverage -fsanitize=address,undefined`
* **Workflows:** Обязательная генерация `buildPresets` и `testPresets` для каждого `configurePreset`, наследующих его имя (например, для запуска `cmake --workflow --preset win-msvc-release-cpp23o3flto`).

## 2. `CMakeLists.txt`
Скрипты сборки должны быть декларативными, фокусироваться только на таргетах и **не содержать хардкода флагов компилятора**.

### Глобальные настройки
* `cmake_minimum_required(VERSION 4.0)`
* Имя проекта генерируется на основе корневого `namespace`.
* `set(CMAKE_CXX_STANDARD 23)`
* `set(CMAKE_CXX_STANDARD_REQUIRED ON)`
* **ЗАПРЕЩЕНО:** Использовать `add_compile_options`, `add_link_options` или напрямую менять `CMAKE_CXX_FLAGS` внутри `CMakeLists.txt`.

### Поиск исходников
* Использовать ТОЛЬКО `file(GLOB ...)` или `file(GLOB_RECURSE ...)` для определения исходников проекта.

### Линковка и Системные зависимости
* Осуществлять строгий контроль графа зависимостей через `target_link_libraries`.
* Для фичей C++23 (например, `std::stacktrace`): если требуется линковка с платформозависимой системной библиотекой (например, `libbacktrace` на GCC/Linux), используй `find_package` или проверки платформы. 

## 3. Требования к C++ исходникам
При генерации C++ кода агентом (тестовые файлы, заглушки) строго соблюдать:
* **Документация:** Исключительно снаружи интерфейсов с использованием Doxygen (`@brief`, `@param[in|out]`, `@return`).
* **Обоснование архитектуры:** Обязательный тег `@see` со ссылкой на индустриальный стандарт или паттерн проектирования, объясняющий выбор реализации.
* **Примеры:** Обязательный тег `@note` с примером (snippet) использования кода.
* **Внутренняя логика:** Код внутри функций должен быть максимально сжат, лаконичен и **абсолютно без комментариев внутри тела функции**.
