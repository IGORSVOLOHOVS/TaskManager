---
name: cpp-qt
description: Создание desktop-приложения на Qt6
---
Создай интерактивный Task List со следующими шагами и начни выполнение:
1. [ ] Определить структуру приложения (Model-View) с использованием функционального ядра `@[.agents/rules/cpp-qt.md]`
2. [ ] Настроить пути `find_package(Qt6 COMPONENTS Widgets)` в CMakeLists `@[.agents/rules/cpp-cmake.md]`
3. [ ] Синтезировать базовое окно на основе модульного QDockWidgets или QMainWindow
4. [ ] Связать логику слотов и сигналов и вызвать CMake для генерации MOC/UIC/RCC файлов
5. [ ] Собрать и запустить графическое приложение
