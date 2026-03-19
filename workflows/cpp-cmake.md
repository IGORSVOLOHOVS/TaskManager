---
name: cpp-cmake
description: Инициализация CMakeLists.txt
---
Создай интерактивный Task List со следующими шагами и начни выполнение:
1. [ ] Настроить базовые требования (cmake_minimum_required, project, cxx_std 23) `@[.agents/rules/cpp-cmake.md]`
2. [ ] Настроить `target_compile_features` и директории `target_include_directories`
3. [ ] Прописать зависимости, подтягиваемые из Conan (например `find_package`) `@[.agents/rules/cpp-package.md]`
4. [ ] Добавить флаги `-Wall -Wextra -Wpedantic`
5. [ ] Запустить конфигурацию проекта и отловить/исправить ошибки `cmake -B build`
