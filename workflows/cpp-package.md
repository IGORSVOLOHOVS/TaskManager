---
name: cpp-package
description: Зависимости Conan
---
Создай интерактивный Task List со следующими шагами и начни выполнение:
1. [ ] Создать `conanfile.txt` в корне проекта
2. [ ] Определить список нужных пакетов и генераторы (CMakeDeps, CMakeToolchain) `@[.agents/rules/cpp-package.md]`
3. [ ] Настроить профиль Conan (`conan profile detect`) под C++23
4. [ ] Запустить команду инсталляции `conan install . -b missing`
5. [ ] Интегрировать сгенерированные файлы интеграции (toolchain) в CMake-сборку `@[.agents/rules/cpp-cmake.md]`
