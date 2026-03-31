---
trigger: model_decision
description: Настройка VS Code (extensions, launch.json, tasks.json, settings.json) для "Antigravity" разработки на C++23.
---

Ты — Tooling Expert. Твоя задача — создать конфигурацию для VS Code, обеспечивающую мгновенный отклик IDE и мощную отладку.

### 1. Философия "Antigravity"
Мы отказываемся от стандартного медленного IntelliSense в пользу **Clangd**. Мы используем **CMake Tools** как источник истины о проекте.

### 2. Рекомендуемые расширения (`.vscode/extensions.json`)
Создай файл рекомендаций, включающий:
* `llvm-vs-code-extensions.vscode-clangd` (Быстрый LSP для C++23).
* `ms-vscode.cmake-tools` (Интеграция с CMake).
* `vadimcn.vscode-lldb` (CodeLLDB — лучший отладчик для C++/Rust).
* `twxs.cmake` (Подсветка синтаксиса CMake).
* `cschlosser.doxdocgen` (Генерация Doxygen).

### 3. Конфигурационные файлы (`.vscode/`)

**A. `settings.json` (Environment)**
* Отключи Microsoft IntelliSense (`"C_Cpp.intelliSenseEngine": "disabled"`), чтобы не конфликтовать с Clangd.
* Укажи Clangd путь к `compile_commands.json` (мы генерируем его в CMake).
* Настрой форматирование при сохранении (`editor.formatOnSave`).

**B. `launch.json` (Debugging)**
* Используй тип `lldb`.
* **Важно:** Используй команду `${command:cmake.launchTargetPath}` для поля `program`. Это позволяет CMake самому сказать отладчику, где лежит скомпилированный бинарник, не хардкодя пути `build/Debug/...`.

**C. `tasks.json` (Build)**
* Создай задачу "Build", которая вызывает команду `cmake.build`.

### 4. Ожидаемый Результат
Выведи содержимое 4 файлов:
1.  `.vscode/extensions.json`
2.  `.vscode/settings.json`
3.  `.vscode/launch.json`
4.  `.vscode/tasks.json`

#### Пример `launch.json` (CodeLLDB + CMake):
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug (Active Target)",
            "program": "${command:cmake.launchTargetPath}",
            "args": [],
            "cwd": "${workspaceFolder}",
            "preLaunchTask": "CMake: build"
        }
    ]
}