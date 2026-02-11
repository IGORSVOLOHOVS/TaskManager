---
trigger: model_decision
description: Создание бенчмарков производительности для выбранного файла с использованием ankerl::nanobench и HTML
---

Ты — Performance Engineer. Твоя задача — написать код для замера производительности функции.

### 1. Инструментарий
- Библиотека: `#include <nanobench.h>` (ankerl::nanobench).
- Формат вывода: Генерация HTML отчета.

### 2. Структура Файла (`benchmarks/bench_function_name.cpp`)
- Создай отдельный бинарник или цель для бенчмарка.
- Используй `ankerl::nanobench::Bench`.
- Обязательно "трогай" результаты, чтобы оптимизатор не выкинул код (`ankerl::nanobench::doNotOptimizeAway`).

### 3. Логика
Поскольку функции возвращают `std::expected`:
- В цикле бенчмарка вызывай функцию.
- Генерируй HTML отчет в файл `docs/benchmark-report/benchmark_report_{name_of_method}.html`.
- script/run_benchmarks.html открывает все бенчмарки у которых начинается имя benchmark_report_*.html

### 4. Шаблон Кода
```cpp
#define ANKERL_NANOBENCH_IMPLEMENT
#include <nanobench.h>
#include <fstream>
#include "..."

int main() {
    using namespace ankerl::nanobench;
    Bench bench;

    bench.title("Benchmark: function_name")
         .unit("ops")
         .warmup(100)
         .relative(true);

    bench.run("Case 1: Typical Input", [&] {
        auto result = function_name(typical_input);
        doNotOptimizeAway(result);
    });

    // Генерация HTML
    std::ofstream file("function_name_report.html");
    bench.render(Templates::htmlBoxplot(), file);
}