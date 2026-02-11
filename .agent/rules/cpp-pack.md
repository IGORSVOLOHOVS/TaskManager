---
trigger: model_decision
description: Правила упаковки проекта в redistributable архив (tar.gz, zip) и Windows установщик (.exe) со всеми зависимостями.
---

Ты — Release Engineer. Твоя задача — настроить создание **полностью автономных пакетов** (standalone packages), которые можно распаковать/установить и запустить на чистой машине без установки Conan или компиляторов.

## 1. Стратегия Упаковки (CPack)

В конец `CMakeLists.txt` необходимо добавить конфигурацию CPack.

**Критические требования:**
1. **Bundle Libraries:** Все динамические библиотеки (`.so`, `.dll`), от которых зависит проект (включая те, что притянул Conan), должны лежать рядом с бинарником или в папке `lib/`.
2. **RPATH:** Бинарник должен быть собран с `$ORIGIN` (Linux) или `@executable_path` (macOS), чтобы он искал библиотеки в своей папке.
3. **Generators:** Поддержка `TGZ` (Linux/macOS), `ZIP` (Windows portable), и `NSIS` (Windows installer).

## 2. CMake Конфигурация

Добавь следующий блок в конец `CMakeLists.txt`:

```cmake
# --- PACKAGING (CPack) ---

# 1. Install RPATH settings (Make binary find libs in ./lib or ./)
set(CMAKE_INSTALL_RPATH "$ORIGIN;$ORIGIN/../lib")
set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)

# 2. Install targets (используй РЕАЛЬНОЕ имя исполняемого файла из add_executable)
install(TARGETS <executable_name>
    DESTINATION bin 
    COMPONENT runtime
)

# 3. Install Runtime Dependencies (Get DLLs/SOs from Conan/System)
# Используем file(GET_RUNTIME_DEPENDENCIES) - требует CMake 3.21+
install(CODE "
    file(GET_RUNTIME_DEPENDENCIES
        EXECUTABLES $<TARGET_FILE:<executable_name>>
        RESOLVED_DEPENDENCIES_VAR _r_deps
        UNRESOLVED_DEPENDENCIES_VAR _u_deps
        DIRECTORIES \${CMAKE_BINARY_DIR}/lib
    )
    foreach(_file \${_r_deps})
        file(INSTALL 
            DESTINATION \"\${CMAKE_INSTALL_PREFIX}/lib\" 
            TYPE SHARED_LIBRARY 
            FILES \"\${_file}\"
        )
    endforeach()
    message(STATUS \"Packed dependencies: \${_r_deps}\")
")

# 4. Install Assets/Config (if any)
# Пример: install(FILES config.json DESTINATION etc COMPONENT config)

# 5. CPack Setup - Общие настройки
set(CPACK_PACKAGE_NAME ${PROJECT_NAME})
set(CPACK_PACKAGE_VENDOR "MyCompany")
set(CPACK_PACKAGE_VERSION_MAJOR 0)
set(CPACK_PACKAGE_VERSION_MINOR 1)
set(CPACK_PACKAGE_VERSION_PATCH 0)
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Краткое описание проекта")
set(CPACK_PACKAGE_DESCRIPTION "Полное описание проекта")
set(CPACK_PACKAGE_INSTALL_DIRECTORY "${PROJECT_NAME}")
set(CPACK_GENERATOR "TGZ;ZIP;NSIS") # TGZ для Linux/macOS, ZIP для portable, NSIS для Windows installer
set(CPACK_PACKAGE_FILE_NAME "${PROJECT_NAME}-${CPACK_PACKAGE_VERSION_MAJOR}.${CPACK_PACKAGE_VERSION_MINOR}.${CPACK_PACKAGE_VERSION_PATCH}-${CMAKE_SYSTEM_NAME}-${CMAKE_SYSTEM_PROCESSOR}")

# 6. NSIS-specific settings (Windows Installer)
set(CPACK_NSIS_MODIFY_PATH ON)
set(CPACK_NSIS_ENABLE_UNINSTALL_BEFORE_INSTALL ON)
set(CPACK_NSIS_DISPLAY_NAME "${PROJECT_NAME} ${CPACK_PACKAGE_VERSION_MAJOR}.${CPACK_PACKAGE_VERSION_MINOR}")
set(CPACK_NSIS_PACKAGE_NAME "${PROJECT_NAME}")
set(CPACK_NSIS_HELP_LINK "https://github.com/yourusername/yourproject")
set(CPACK_NSIS_URL_INFO_ABOUT "https://github.com/yourusername/yourproject")
set(CPACK_NSIS_CONTACT "your.email@example.com")
set(CPACK_NSIS_MENU_LINKS
    "bin/<executable_name>.exe" "${PROJECT_NAME}"
)

include(CPack)
```

**ВАЖНО:** Замени `<executable_name>` на реальное имя исполняемого файла из `add_executable()`.

## 3. Правильная последовательность команд

### Проблемы, которые были найдены:
1. ❌ **Неправильно:** `cmake --preset release` (preset может не существовать)
2. ❌ **Неправильно:** `cpack -C Release` из корня проекта (не найдет CPackConfig.cmake)
3. ❌ **Неправильно:** Использование `${PROJECT_VERSION_MAJOR}` без определения версии в `project()`

### ✅ Правильная последовательность:

```powershell
# 1. Установить зависимости через Conan (ОБЯЗАТЕЛЬНО Release mode)
conan install . --output-folder=build --build=missing -s build_type=Release

# 2. Сконфигурировать CMake (используй СУЩЕСТВУЮЩИЙ preset из CMakeUserPresets.json)
cmake --preset conan-default -DCMAKE_BUILD_TYPE=Release

# 3. Собрать проект в Release mode
cmake --build build/build --config Release

# 4. Перейти в build-директорию и создать пакеты
cd build/build

# Создать ZIP архив (portable)
cpack -C Release -G ZIP

# Создать Windows установщик (требует NSIS)
cpack -C Release -G NSIS

# Или создать все форматы сразу
cpack -C Release
```

### Результат:
- `<ProjectName>-0.1.0-Windows-AMD64.zip` - портативный архив
- `<ProjectName>-0.1.0-Windows-AMD64.exe` - Windows установщик (если NSIS установлен)
- `<ProjectName>-0.1.0-Linux-x86_64.tar.gz` - архив для Linux

## 4. Требования для Windows установщика

**NSIS должен быть установлен:**
```powershell
# Установка через Chocolatey
choco install nsis

# Или скачать с https://nsis.sourceforge.io/Download
```

CPack автоматически найдет NSIS, если он в PATH.

## 5. Проверка результата

```powershell
# Проверить размер установщика
Get-Item "*.exe" | Select-Object Name, @{Name="Size (MB)";Expression={[math]::Round($_.Length/1MB, 2)}}

# Извлечь ZIP для проверки
Expand-Archive -Path "*.zip" -DestinationPath "C:\temp\test" -Force

# Проверить структуру
tree /F C:\temp\test
```

**Ожидаемая структура:**
```
<ProjectName>-0.1.0-Windows-AMD64/
├── bin/
│   └── <executable>.exe
└── lib/
    ├── spdlog.dll
    ├── vcruntime140.dll
    └── ... (другие DLL)
```

## 6. Типичные ошибки и решения


### Ошибка: "Cannot find NSIS"
**Причина:** NSIS не установлен или не в PATH.
**Решение:** Установи NSIS через `choco install nsis` или скачай с официального сайта.

### Проблема: Системные DLL (kernel32.dll, ntdll.dll) включены в пакет
**Причина:** `file(GET_RUNTIME_DEPENDENCIES)` включает все зависимости.
**Решение:** Это нормально, системные DLL не повредят (они игнорируются на целевой системе).

## 7. Документация

Создай `docs/packaging.md` с инструкциями для пользователей:
- Как собрать пакет (для разработчиков)
- Как установить приложение (для конечных пользователей)
- Структура пакета
- Troubleshooting