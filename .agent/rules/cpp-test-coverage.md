---
trigger: model_decision
description: Настройка инструментария для анализа покрытия кода (Code Coverage) и генерации HTML-отчетов (Cross-platform: Windows/Linux).
---

Ты — QA Automation Lead. Твоя задача — внедрить автоматизированный анализ покрытия кода (Code Coverage).

### 1. CMake Конфигурация
В `CMakeLists.txt` необходимо добавить флаги компиляции и кастомную цель `coverage`.

**Правила:**
1.  **Linux/GCC/Clang:** Флаги `--coverage` добавляются **только** в режиме `Debug`.
2.  **Windows/MSVC:** Флаги не требуются, но нужны PDB файлы (стандартно в Debug). Используется `OpenCppCoverage`.
3.  Создай цель `coverage`, которая вызывает Python-скрипт через найденный интерпретатор.

**Пример (CMake):**
```cmake
# 1. Coverage Flags (Linux Only)
if(NOT MSVC)
    if(CMAKE_BUILD_TYPE STREQUAL "Debug")
        add_compile_options(--coverage)
        add_link_options(--coverage)
    endif()
endif()

# 2. Find Python
find_package(Python COMPONENTS Interpreter REQUIRED)

# 3. Custom target
add_custom_target(coverage
    COMMAND ${Python_EXECUTABLE} scripts/run_test_coverage.py
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "🚀 Running tests and generating HTML coverage report..."
)
```

### 2. Скрипт scripts/run_test_coverage.py
Создай кросс-платформенный скрипт.

**Требования к скрипту:**
1.  **Windows:**
    *   Используй `OpenCppCoverage`.
    *   Если не найден в PATH, проверь `C:\Program Files\OpenCppCoverage\OpenCppCoverage.exe`.
    *   Найди все `test_*.exe` в папке сборки (`build/**/test_*.exe`).
    *   Запусти каждый тест отдельно, генерируя `.cov` файлы.
    *   Объедини отчеты (merge) в единый HTML.
2.  **Linux:**
    *   Используй `lcov` и `genhtml`.
    *   `lcov --zerocounters` -> `ctest` -> `lcov --capture` -> `lcov --remove` -> `genhtml`.
3.  **Фильтрация:** Исключи системные файлы, зависимости и тесты.

**Код Скрипта (Reference Implementation):**

```python
import os
import subprocess
import sys
import platform
import shutil
import glob

# Config
BUILD_DIR = "build"
OUTPUT_DIR = "docs/coverage-report"
INFO_FILE = "coverage.info"
FILTERED_FILE = "coverage_filtered.info"

def run_command(command, fail_message):
    print(f"[Exec] Executing: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"[Error] {fail_message}")
        sys.exit(1)

def run_windows_coverage():
    print("[Windows] Verify OpenCppCoverage...")
    
    executable = "OpenCppCoverage"
    
    # Check for OpenCppCoverage
    if shutil.which("OpenCppCoverage") is None:
        default_path = r"C:\Program Files\OpenCppCoverage\OpenCppCoverage.exe"
        if os.path.exists(default_path):
            executable = f'"{default_path}"'
            print(f"[Info] Found OpenCppCoverage at: {default_path}")
        else:
            print("[Error] OpenCppCoverage not found in PATH.")
            print("   Please install it: https://github.com/OpenCppCoverage/OpenCppCoverage/releases")
            print("   Or via choco: choco install opencppcoverage")
            sys.exit(1)

    # Clean previous report
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)

    # Find test executables (recursively in build folder)
    test_exes = glob.glob(os.path.join(BUILD_DIR, "**", "test_*.exe"), recursive=True)
    
    if not test_exes:
        print(f"[Error] No test executables found in {BUILD_DIR}. Did you build the project?")
        sys.exit(1)

    print(f"[Info] Found {len(test_exes)} test executables.")

    cov_files = []
    for i, test_exe in enumerate(test_exes):
        cov_file = f"coverage_{i}.cov"
        cov_files.append(cov_file)
        
        print(f"[Exec] Running coverage for {os.path.basename(test_exe)}...")
        
        # Run test individually
        cmd = (
            f"{executable} "
            f"--export_type binary:{cov_file} "
            f"--sources {os.getcwd()} "
            f"--modules * " 
            f"-- {test_exe}"
        )
        run_command(cmd, f"Coverage failed for {test_exe}")

    # Merge reports
    print("[Info] Merging coverage reports...")
    merge_args = " ".join([f"--input_coverage {cov}" for cov in cov_files])
    
    cmd = (
        f"{executable} "
        f"{merge_args} "
        f"--export_type html:{OUTPUT_DIR} "
        f"--sources {os.getcwd()} "
        f"--modules * " 
    )
    run_command(cmd, "Failed to merge coverage reports")
    
    # Cleanup .cov files
    for cov in cov_files:
        if os.path.exists(cov):
            os.remove(cov)
            
    print(f"[Success] Open {OUTPUT_DIR}/index.html to view results.")

def run_linux_coverage():
    print("[Linux] Detected Linux/Unix. Using lcov/genhtml...")

    if subprocess.call("which lcov", shell=True, stdout=subprocess.DEVNULL) != 0:
        print("[Error] lcov not found. Please install it (apt-get install lcov).")
        sys.exit(1)

    run_command(f"lcov --directory {BUILD_DIR} --zerocounters", "Failed to reset counters")

    print("[Info] Running CTest...")
    run_command(f"cd {BUILD_DIR} && ctest --output-on-failure", "Tests failed! Coverage aborted.")

    print("[Info] Capturing coverage data...")
    run_command(f"lcov --directory {BUILD_DIR} --capture --output-file {INFO_FILE} --ignore-errors mismatch", "Failed to capture coverage")

    print("[Info] Filtering data...")
    # Filter system, deps, and tests
    run_command(
        f"lcov --remove {INFO_FILE} '/usr/*' '*/_deps/*' '*/tests/*' --output-file {FILTERED_FILE} --ignore-errors unused",
        "Failed to filter coverage data"
    )

    print(f"[Info] Generating HTML report to {OUTPUT_DIR}...")
    run_command(
        f"genhtml {FILTERED_FILE} --output-directory {OUTPUT_DIR} --legend --demangle-cpp",
        "Failed to generate HTML"
    )

    print(f"[Success] Open {OUTPUT_DIR}/index.html to view results.")

def main():
    if platform.system() == "Windows":
        run_windows_coverage()
    else:
        run_linux_coverage()

if __name__ == "__main__":
    main()
```