import os, urllib.request

def project_tdd_setup(project_name):
    # --- Настройка путей ---
    root_dir = os.path.abspath(project_name)
    src_dir = os.path.join(root_dir, "src")
    inc_dir = os.path.join(root_dir, "include")
    doctest_dir = os.path.join(inc_dir, "doctest")
    
    cpp_filename = "core.cpp"
    cpp_path = os.path.join(src_dir, cpp_filename)
    
    print(f"🚀 Initializing project: {project_name}")

    # 1. Создание структуры папок
    for d in [root_dir, src_dir, inc_dir, doctest_dir]:
        os.makedirs(d, exist_ok=True)
        print(f"📂 Created: {d}")

    # 2. Скачивание библиотек (Header-only)
    libs = {
        os.path.join(doctest_dir, "doctest.h"): "https://raw.githubusercontent.com/doctest/doctest/master/doctest/doctest.h",
        os.path.join(inc_dir, "nanobench.h"): "https://raw.githubusercontent.com/martinus/nanobench/master/src/include/nanobench.h"
    }

    print("⬇️ Downloading dependencies...")
    for path, url in libs.items():
        if not os.path.exists(path):
            try:
                print(f"   Fetching {os.path.basename(path)}...")
                urllib.request.urlretrieve(url, path)
            except Exception as e:
                print(f"❌ Error downloading {os.path.basename(path)}: {e}")
                print("   ⚠️ Please download manually and place in include folder.")

    # 3. Генерация .clang-format
    clang_format_content = """---
Language:        Cpp
BasedOnStyle:    Google
IndentWidth:     4
ColumnLimit:     120
SortIncludes:    true
FixNamespaceComments: true
AlignAfterOpenBracket: Align
AllowShortFunctionsOnASingleLine: Empty
BreakBeforeBraces: Attach
...
"""
    with open(os.path.join(root_dir, ".clang-format"), "w") as f:
        f.write(clang_format_content)
    print("✨ Generated .clang-format")

    # 4. Генерация .clang-tidy
    clang_tidy_content = """---
Checks:          'clang-diagnostic-*,clang-analyzer-*,bugprone-*,modernize-*,performance-*,readability-*,portability-*,-modernize-use-trailing-return-type'
WarningsAsErrors: '*'
CheckOptions:
  - key:             readability-identifier-naming.ClassCase
    value:           CamelCase
...
"""
    with open(os.path.join(root_dir, ".clang-tidy"), "w") as f:
        f.write(clang_tidy_content)
    print("🧹 Generated .clang-tidy")

    # 5. Генерация C++23 Core File (Самодостаточный, БЕЗ PCH)
    # Обрати внимание: IMPLEMENTATION макросы определены прямо здесь.
    cpp_content = f"""/**
 * @file {cpp_filename}
 * @brief Single-file C++23 Project Skeleton (No PCH).
 * Contains pure functions, doctest unit tests, and nanobench benchmarks.
 */

// ============================================================================
// STANDARD INCLUDES
// ============================================================================
#include <iostream>
#include <numeric>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <ranges>
#include <expected>
#include <concepts>
#include <fstream>
#include <memory>
#include <optional>

// ============================================================================
// LIBRARIES (Implementation + Interface)
// ============================================================================

#define DOCTEST_CONFIG_IMPLEMENT
#include <doctest/doctest.h>

#define ANKERL_NANOBENCH_IMPLEMENT
#include <nanobench.h>

/// @brief Standard result type for error handling without exceptions.
template<typename T>
using Result = std::expected<T, std::string>;

// ============================================================================
// PURE FUNCTIONAL LOGIC (Level 2: Analysis)
// ============================================================================

/**
 * @brief Calculates the factorial of a non-negative integer using recursion.
 * @tparam T An integral type (int, long, size_t).
 * @param[in] n The number to calculate factorial for.
 * @return Result<T> The factorial value or error if n < 0.
 */
template<std::integral T>
[[nodiscard]] constexpr Result<T> calculate_factorial(T n) noexcept {{
    return (n < 0) ? std::unexpected("Negative input") : Result<T>((n <= 1) ? 1 : n * calculate_factorial(n - 1).value());
}}

/**
 * @brief Filters a collection of numbers based on a predicate.
 * Uses C++20/23 ranges to create a filtered view and materialize it.
 * @param[in] input Vector of integers.
 * @return std::vector<int> A new vector containing only even numbers.
 */
[[nodiscard]] std::vector<int> filter_evens(const std::vector<int>& input) {{
    auto v = input | std::views::filter([](int n){{ return n % 2 == 0; }});
    return std::vector<int>(v.begin(), v.end());
}}

/**
 * @brief Approximates the square root using the Newton-Raphson method.
 * @param[in] x Input value.
 * @param[in] iterations Number of refinement steps.
 * @return double Approximated square root.
 */
[[nodiscard]] constexpr double newton_sqrt(double x, int iterations) noexcept {{
    double g = x / 2.0;
    for(int i=0; i<iterations; ++i) g = (g + x/g) / 2.0;
    return g;
}}

// ============================================================================
// TESTS (Level 3: Creation/Verification)
// ============================================================================

TEST_CASE("Factorial Functionality") {{
    SUBCASE("Happy Path") {{
        CHECK(calculate_factorial(0).value() == 1);
        CHECK(calculate_factorial(1).value() == 1);
        CHECK(calculate_factorial(5).value() == 120);
    }}
    SUBCASE("Edge Cases") {{
        CHECK(calculate_factorial(10).value() > 0); 
    }}
    SUBCASE("Error States") {{
        CHECK(!calculate_factorial(-1).has_value());
        CHECK(calculate_factorial(-5).error() == "Negative input");
    }}
}}

TEST_CASE("Filter Evens Functionality") {{
    SUBCASE("Happy Path") {{
        std::vector<int> in = {{1, 2, 3, 4, 5, 6}};
        auto res = filter_evens(in);
        CHECK(res.size() == 3);
        CHECK(res[0] == 2);
        CHECK(res[2] == 6);
    }}
    SUBCASE("Edge Cases") {{
        CHECK(filter_evens({{}}).empty());
        CHECK(filter_evens({{1, 3, 5}}).empty());
    }}
}}

TEST_CASE("Newton Sqrt Functionality") {{
    CHECK(doctest::Approx(newton_sqrt(25.0, 10)) == 5.0);
    CHECK(doctest::Approx(newton_sqrt(2.0, 10)) == 1.41421356);
}}

// ============================================================================
// BENCHMARKS & EXECUTION
// ============================================================================

void run_benchmarks() {{
    ankerl::nanobench::Bench bench;
    bench.title("Pure Function Benchmarks")
         .unit("ops")
         .warmup(100)
         .relative(true);

    bench.run("Factorial(20)", [] {{
        ankerl::nanobench::doNotOptimizeAway(calculate_factorial(20));
    }});

    std::vector<int> v(1000);
    std::iota(v.begin(), v.end(), 0);
    bench.run("FilterEvens(1000)", [&] {{
        ankerl::nanobench::doNotOptimizeAway(filter_evens(v));
    }});

    bench.run("NewtonSqrt(1M)", [] {{
        ankerl::nanobench::doNotOptimizeAway(newton_sqrt(12345.6789, 20));
    }});

    std::ofstream file("benchmarks.html");
    if (file.is_open()) {{
        bench.render(ankerl::nanobench::templates::htmlBoxplot(), file);
        std::cout << "[Bench] Output written to benchmarks.html\\n";
    }}
}}

int main(int argc, char** argv) {{
    std::cout << "[System] Running Tests...\\n";
    
    doctest::Context context;
    context.applyCommandLine(argc, argv);
    int test_result = context.run();

    if (context.shouldExit()) return test_result;

    if (test_result == 0) {{
        std::cout << "[System] Tests Passed. Running Benchmarks...\\n";
        run_benchmarks();
        
        std::cout << "[System] Opening results...\\n";
        std::system("xdg-open benchmarks.html || open benchmarks.html || echo 'Open benchmarks.html manually'");
    }} else {{
        std::cout << "[System] Tests Failed. Skipping Benchmarks.\\n";
    }}

    return test_result;
}}
"""
    with open(cpp_path, "w") as f:
        f.write(cpp_content)
    print(f"📄 Generated C++ Core: {cpp_path}")
    print("\n✅ Setup Complete! Now you can compile directly.")