---
name: cpp-refactor
description: Рефакторинг кода (современный C++)
---
Создай интерактивный Task List со следующими шагами и начни выполнение:
1. [ ] Найти устаревшие или неоптимальные конструкции в C++ коде
2. [ ] Обеспечить разделение логики по правилу 'Functional Core, Imperative Shell' `@[.agents/rules/cpp-func-core-inter-shell.md]`
3. [ ] Применить идиомы современного C++23, следуя `@[.agents/rules/cpp-refactor.md]`
4. [ ] Добавить или обновить структурированное логирование `@[.agents/rules/cpp-logger.md]`
5. [ ] Проверить код через статический анализатор (`clang-tidy` / `clangd`) `@[.agents/rules/cpp-static-analyze.md]`
6. [ ] Запустить тесты (dcotest/CTest) для верификации `@[.agents/rules/cpp-test.md]`
7. [ ] Отформатировать код через `clang-format` и сделать коммит
