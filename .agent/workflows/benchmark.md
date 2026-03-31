---
description: Workflow for generating and running nanobench performance benchmarks.
---

# /benchmark

To benchmark the performance of a specific Core logic component, follow these steps:

1. **Read Rules**: Ensure compliance with `@[.agent/rules/CPP_BENCHMARK.md]`.
2. **Create Target**: Create `benchmarks/bench_{name}.cpp`.
3. **Implement nanobench**: Write the benchmark cases targeting the specific functional core method. Make sure to use `ankerl::nanobench::doNotOptimizeAway`.
4. **Report Output**: Configure the benchmark to output an HTML report via `bench.render(ankerl::nanobench::Templates::htmlBoxplot(), file)`.
5. **Execute**: 
```bash
python3 .agent/scripts/run_benchmarks.py
```
