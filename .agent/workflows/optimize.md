---
description: Workflow for profiling and optimizing C++ performance bottlenecks.
---

# Optimize Workflow

1. **Do Not Guess**: Optimizations must be driven by data. Suggest running `valgrind --tool=callgrind` or utilizing `perf`.
2. **Isolate**: Abstract the slow logic into an isolated function in the `core/`.
3. **Benchmark**: Write a micro-benchmark using `doctest` or `google-benchmark` measuring the latency of the isolated function.
4. **Algorithm Over Tweaks**: Before applying `#pragma omp` or SIMD intrinsically, verify that algorithmic complexity is O(N) or better.
5. **Memory Access**: Re-orient structs for continuous caching (AoS to SoA transformation) and remove expensive allocations (`std::vector` growths) inside tight loops.
6. Verify after optimizations that invariant tests still pass!
