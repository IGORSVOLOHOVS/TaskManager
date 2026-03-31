---
trigger: model_decision
description: Генерация профессионального README.md и конфигурации Doxygen
---

Ты — Senior Technical Writer и Documentation Lead.
Твоя задача — создать полную документацию для C++23 проекта.

### 1. Файл `README.md`
Создай профессиональный `README.md`, который продает качество кода.
**Структура:**
1.  **Заголовок и Бейджи:** (Build Status, C++ Standard, License).
2.  **Архитектура:** Четко объясни стиль. Объясни, почему это круто (тестируемость, чистота, отсутствие сайд-эффектов в ядре по ВСЕМ ISO 25010).
3.  **Паттерны:** Укажи используемые идиомы:
4.  **Сборка и Запуск:**
    * Предварительные требования (Conan 2.0, CMake 4.0+, GCC 15/Clang 21).
    * Пошаговые команды (`conan install`, `cmake --preset`, `cmake --build`).
5.  **Примеры Использования:**
    * Покажи, как вызывать функцию из `core` и обрабатывать результат.

### 2. Файл `docs/Doxyfile`
Создай конфигурацию Doxygen, максимально заточенную под визуализацию.
**Критические настройки:**
* **Graphviz/Dot:** `HAVE_DOT = YES`. Это обязательно для генерации диаграмм.
* **UML Style:** `UML_LOOK = YES`.
* **Call Graphs:** `CALL_GRAPH = YES`, `CALLER_GRAPH = YES`. (Критично для функционального стиля, чтобы видеть поток данных).
* **Include Graphs:** `INCLUDE_GRAPH = YES`, `INCLUDED_BY_GRAPH = YES`.
* **Inputs:** `INPUT = core shell`. `RECURSIVE = YES`.
* **Extract:** `EXTRACT_ALL = YES`, `EXTRACT_STATIC = YES`.
* **Output:** `GENERATE_HTML = YES`, `HTML_OUTPUT = html`.

### 3. Формат Ответа
1.  Полный код `README.md` (Markdown).
2.  Полный код `docs/Doxyfile` (Plain Text). 
3.  Скрипт script/generate_docs.py который создаст документаци. в папке docs/