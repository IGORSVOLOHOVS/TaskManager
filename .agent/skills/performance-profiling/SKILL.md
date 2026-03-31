---
name: performance-profiling
description: C++ Performance profiling principles. Measurement via nanobench, memory profiling with Valgrind, and CPU analysis with perf.
allowed-tools: Read, Glob, Grep, Bash
---

# C++ Performance Profiling

> Measure, analyze, optimize - in that order.

## 1. Micro-benchmarking (nanobench)

**Mandatory:** Use `ankerl::nanobench` for high-precision timing of core algorithms.

### Key Rules
- **Warmup:** Always include a warmup phase to stabilize CPU frequency.
- **Do Not Optimize Away:** Use `ankerl::nanobench::doNotOptimizeAway(result)` to prevent the compiler from skipping the code.
- **Relative Comparison:** Benchmark multiple implementations relatively to see the delta.

### Benchmark Snippet
```cpp
#define ANKERL_NANOBENCH_IMPLEMENT
#include <nanobench.h>

void profile_algorithm() {
    ankerl::nanobench::Bench bench;
    bench.title("Compute Algorithm")
         .relative(true);

    bench.run("Fast Path", [&] {
        auto res = core_logic_fast();
        ankerl::nanobench::doNotOptimizeAway(res);
    });
}
```

---

## 2. Memory Profiling (Valgrind Massif)

Use Massif to track heap allocation over time and find the "high-water mark".

### Command
```bash
valgrind --tool=massif ./my_executable
ms_print massif.out.<pid>
```

### Analysis
- Look for `detailed` snapshots to see exactly which line allocated the most memory.
- Identify "peaks" and see if they can be reduced by using stack-based buffers or object pools.

---

## 3. CPU Profiling (Perf / Callgrind)

### Perf (Linux)
```bash
perf record -g ./my_executable
perf report
```
- Focus on the "Hot Functions" (functions taking >5% of CPU).

### Callgrind (Visual Analysis)
```bash
valgrind --tool=callgrind ./my_executable
kcachegrind callgrind.out.<pid>
```
- Analyze the call graph to find expensive branches.

---

## 4. Optimization Priorities (C++)

| Priority | Action | Impact |
|----------|--------|--------|
| 1 | Remove Heap Allocations from Loops | High |
| 2 | Improve Cache Locality (DOD) | High |
| 3 | Use `string_view` / `span` (no copy) | Medium |
| 4 | Devirtualization (Concepts/CRTP) | Medium |
| 5 | SIMD / Multi-threading | Extreme (but complex) |

---

## 5. Anti-Patterns

| ❌ Don't | ✅ Do |
|----------|-------|
| Guess at bottlenecks | Profile with `perf` or `nanobench` |
| Micro-optimize non-hot code | Focus on the top 3 functions in `perf report` |
| Ignore cache misses | Use DOD to keep data contiguous |
| Use `std::endl` in loops | Use `\n` to avoid unnecessary flushes |

---

> **Remember:** The fastest code is code that doesn't run. Remove complexity before micro-optimizing.
