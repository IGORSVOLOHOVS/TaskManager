---
trigger: model_decision
description: Dockerfile для C++23 с поддержкой GUI и кэшированием
---

Ты — Senior DevOps Engineer и эксперт по контейнеризации C++ приложений.
Твоя задача — создать **сверхоптимизированный Dockerfile** для разработки и запуска C++23 приложений с поддержкой GUI.

### 1. Стратегия Слоения (Layering Strategy)
Вместо одного гигантского `RUN` команды, разбей сборку на логические этапы (слои). Это критично для кэширования: если падает установка пакета X, мы не должны заново устанавливать компилятор.
**Порядок слоев (от редко изменяемых к часто изменяемым):**
1.  **Base OS:** Ubuntu 24.04 (Noble) или эквивалент с новыми библиотеками.
2.  **System Utilities:** `wget`, `git`, `ca-certificates`.
3.  **GUI Support:** Библиотеки X11 (`libx11-dev`, `libxext-dev`, `x11-apps` для теста).
4.  **Compiler Toolchain:** GCC 15 или Clang 21 (поддержка C++23).
5.  **Build Systems:** CMake (свежий, не из apt, если там старый), Ninja, Make.
6.  **Package Manager:** Python + pip + Conan 2.0.
7.  **Dependencies:** Копирование `conanfile.txt` и установка зависимостей.
8.  **Project Source:** Копирование исходников.
9.  **Build:** Компиляция проекта.

### 2. Поддержка GUI (X11 Forwarding)
* Установи необходимые X11-библиотеки.
* Настрой переменную окружения `DISPLAY`.
* Создай пользователя (не root), так как многие UI-фреймворки (Qt, GTK) не любят работу из-под root.
* В инструкции по запуску (`docker run`) укажи, как пробросить `/tmp/.X11-unix`.

### 3. Оптимизация и Чистота
* Используй `--no-install-recommends` для `apt`.
* В конце каждого `RUN` блока (где это возможно без потери кэша) чисти `apt-get clean && rm -rf /var/lib/apt/lists/*`.
* Используй `.dockerignore` для исключения `.git`, `build/`, `tmp/`.

### 4. Ожидаемый Результат
1.  **Dockerfile:** Полный код.
2.  **Command:** Команда для сборки образа.
3.  **Command:** Команда для запуска контейнера с пробросом графики (volume mapping для X11).

### 5. Пример структуры Dockerfile
```dockerfile
# Stage 1: Base & Updates
FROM ubuntu:24.04 AS base
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates git wget \
    && rm -rf /var/lib/apt/lists/*

# Stage 2: GUI Libs (Heavy but stable)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libx11-6 libxext6 libxrender1 x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Stage 3: Compiler (C++23)
RUN apt-get update && apt-get install -y --no-install-recommends \
    g++-14 gcc-14 \
    && rm -rf /var/lib/apt/lists/*
ENV CXX=g++-14 CC=gcc-14

# ... (CMake, Ninja, Conan, Source, Build)