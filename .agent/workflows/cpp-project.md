---
name: cpp-project
description: Разворачивает инфраструктуру проекта C++ (Conan, CMake, Git Hooks)
---
Создай интерактивный Task List со следующими шагами и начни выполнение:
1. [ ] Определить структуру директорий проекта в соответствии с `@[.agents/rules/architecture.md]`
2. [ ] Инициализировать зависимости через `conanfile.txt`, следуя инструкциям из `@[.agents/rules/cpp-package.md]`
3. [ ] Настроить систему сборки `CMakeLists.txt` с поддержкой C++23, как описано в `@[.agents/rules/cpp-cmake.md]`
4. [ ] Настроить конфигурацию статического анализатора и `compile_commands.json` по `@[.agents/rules/cpp-static-analyze.md]`
5. [ ] Создать `Dockerfile` для окружения с поддержкой требуемых инструментов разработки согласно `@[.agents/rules/cpp-docker.md]`
6. [ ] Сгенерировать скрипты для локального CI/CD, включая `pre-commit` и `pre-push` хуки `@[.agents/rules/cpp-ci-cd.md]`
7. [ ] Подготовить `README.md` и настроить генерацию документации Doxygen `@[.agents/rules/cpp-documentation.md]`
8. [ ] Убедиться в готовности проекта, собрав его локально через CMake
