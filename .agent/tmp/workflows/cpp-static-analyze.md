---
name: cpp-static-analyze
description: Настройка clangd
---
Создай интерактивный Task List со следующими шагами и начни выполнение:
1. [ ] Включить `CMAKE_EXPORT_COMPILE_COMMANDS=ON` в CMake `@[.agents/rules/cpp-static-analyze.md]`
2. [ ] Создать файл настройки `.clangd` с фильтрацией предупреждений
3. [ ] Интегрировать `clang-tidy` проверки напрямую в `.clangd`
4. [ ] Выполнить перезапуск сервера clangd и профиксить подсвеченные баги
