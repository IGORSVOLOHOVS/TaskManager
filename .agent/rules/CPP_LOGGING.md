# CPP_LOGGING.md - Structured Logging Standards

> **MANDATORY:** Pure functions inside the `core/` directory MUST NOT log anything to console, file, or network.

## 1. Architectural Boundaries
- **Core (Functional):** Returning `std::expected` is the ONLY way errors are propagated. Logging is a side-effect. Pure logic does not have side effects.
- **Shell (Imperative):** The `shell/` is responsible for unpacking `std::expected` and logging the failure.

## 2. Structured Logging
Use a high-performance structured logging library (e.g., `spdlog` or `fmt::format` wrappers).
- Never use generic `std::cout << ... << std::endl;` for application-level logs.
- Use log levels aggressively: `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `CRITICAL`.

### Bad Example (Core Level Logging):
```cpp
// BAD: Core function doing I/O
std::expected<int, std::string> calculate() {
    spdlog::info("Calculating...");
    return 42;
}
```

### Good Example (Shell Level Logging):
```cpp
// GOOD: Core returns data, Shell logs it
auto result = calculate();
if (!result) {
    spdlog::error("Calculation failed: {}", result.error());
} else {
    spdlog::info("Result: {}", *result);
}
```

## 3. Formats
Logs should ideally support JSON serialization for Splunk / ELK stacks when running in production containers, while falling back to colored console output for local debugging.
