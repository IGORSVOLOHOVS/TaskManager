---
trigger: "/optimize-python"
description: "Workflow for profiling and optimizing Python performance bottlenecks."
---

# Workflow: Python Performance Optimization

**Context**: The user wants to speed up their Python application or reduce resource usage.

## Steps
1. **Profiling**: Identify bottlenecks using `cProfile`:
   ```bash
   python3 -m cProfile -s cumulative main.py
   ```
2. **Line Profiling**: If a specific function is slow, use `line_profiler`:
   ```bash
   # Requires @profile decorator and kernprof
   kernprof -l -v main.py
   ```
3. **Memory Profiling**: If memory usage is high, use `memory_profiler`.
4. **Identify Slow Paths**:
   - I/O bound? Suggest `asyncio` or threading.
   - CPU bound? Suggest `numpy`, `multiprocessing`, or `Cython`.
5. **Implement Fixes**: Refactor code and re-run benchmarks via `/benchmark-python`.
6. **Verify Results**: Compare before/after metrics.
