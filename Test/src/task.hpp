#pragma once

#include <pch.hpp>

// --- GoF Pattern Combinations & Snippet Index ---
//
// Common Combinations:
// - Abstract Factory + Factory Method: Factories often use Factory Methods.
// - Builder + Composite: Builder can construct complex Composite trees.
// - Command + Memento: Command can use Memento for undo/redo.
// - Composite + Iterator: Iterator traverses a Composite.
// - Composite + Visitor: Visitor performs operations on a Composite.
// - Decorator + Adapter: Decorator adds functionality, Adapter changes interface.
// - Strategy + State: Both manage behavior based on context.
// - Template Method + Factory Method: Template Method can call Factory Methods.
//
// Snippet Prefixes (GoF):
//   Creational:
//     gof_singleton          (Singleton)
//     gof_factory_method     (Factory Method)
//     gof_abstract_factory   (Abstract Factory)
//     gof_builder            (Builder)
//     gof_prototype          (Prototype)
//   Structural:
//     gof_adapter            (Adapter)
//     gof_bridge             (Bridge)
//     gof_composite          (Composite)
//     gof_decorator          (Decorator)
//     gof_facade             (Facade)
//     gof_flyweight          (Flyweight)
//     gof_proxy              (Proxy)
//   Behavioral:
//     gof_chain_of_responsibility (Chain of Responsibility)
//     gof_command            (Command)
//     gof_interpreter        (Interpreter)
//     gof_iterator           (Iterator)
//     gof_mediator           (Mediator)
//     gof_memento            (Memento)
//     gof_state              (State)
//     gof_strategy           (Strategy)
//     gof_template_method    (Template Method)
//     gof_visitor            (Visitor)
//
// Utility Snippets:
//     task_5constructors     (Default/Copy/Move Constructors/Assignment & Destructor)
//     task_u                 (std::unique_ptr<Type>)
//     task_s                 (std::shared_ptr<Type>)
//     task_r                 (std::vector<double>)
//     task_i                 (std::vector<int>)
//     task_str               (std::vector<std::string>)
//
// Function Definition Snippets:
//     task_func_rnd_vec_double (Function: Generate Random Doubles Vector)
//     task_func_rnd_vec_int    (Function: Generate Random Integers Vector)
//     task_func_rnd_vec_str    (Function: Generate Random Strings Vector)
//     task_func_measure_time   (Function: Measure execution time of a lambda)
//     task_func_sleep_ms       (Function: Sleep for milliseconds)
//     task_func_logger         (Function: Simple Logger)
//
// Notes:
// - Assumes C++17+ for some features like [[nodiscard]] and std::make_unique.
// - Most patterns returning objects now use std::unique_ptr for ownership management.
// - Remember to #include necessary headers like <memory>, <vector>, <string>, <iostream>, etc.
// - For C++23 specific features, ensure your compiler (e.g., GCC 13+, Clang 17+) supports them.

// Requires: <iostream>, <string>, <chrono>, <iomanip> (for std::put_time), <ctime> (for std::time_t, std::tm,
// std::localtime) Note on std::localtime: Not thread-safe on all platforms without _r or _s versions. For
// cross-platform thread-safe time formatting, consider a library or more complex handling.
void appLogger(const std::string &id, const std::string &type, const std::string &message) {
    auto now_sys_clock = std::chrono::system_clock::now();
    std::time_t now_time_t = std::chrono::system_clock::to_time_t(now_sys_clock);
    std::tm time_info_buf;
    // Platform-specific localtime_s or localtime_r for thread safety
#if defined(_WIN32) || defined(_WIN64)
    localtime_s(&time_info_buf, &now_time_t);
#else
    localtime_r(&now_time_t, &time_info_buf);  // POSIX
#endif
    std::cout << "[" << id << "] " << std::put_time(&time_info_buf, "%Y-%m-%d %H:%M:%S") << " [" << type
              << "]: " << message << std::endl;
}

// Requires: <chrono>, <functional>, <iostream>, <string>
template <typename Func>
void measureTime(const std::string &operationName, Func operation) {
    auto start = std::chrono::high_resolution_clock::now();
    operation();
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> duration = end - start;
    std::cout << operationName << " took: " << duration.count() << " ms\n";
}

class Target {
public:
    virtual ~Target() = default;
    virtual void request() = 0;
};
class Adaptee {
public:
    void specificRequest() { /* Adaptee's specific behavior */ }
};
class Adapter : public Target {
public:
    Adapter(std::shared_ptr<Adaptee> adaptee) : adaptee_(adaptee) {}
    void request() override {
        if (adaptee_)
            adaptee_->specificRequest();
    }

private:
    std::shared_ptr<Adaptee> adaptee_;
};

// Example usage:
#include <iostream>
#include <memory>
// Target interface for a modern logger
class ModernLogger {
public:
    virtual ~ModernLogger() = default;
    virtual void logMessage(const std::string &message) = 0;
};
// Adaptee: an old logging library with a different interface
class OldLogger {
public:
    void writeEntry(const char *entry) { std::cout << "OldLogger: " << entry << std::endl; }
};
// Adapter to make OldLogger compatible with ModernLogger interface
class LoggerAdapter : public ModernLogger {
private:
    std::shared_ptr<OldLogger> oldLogger_;

public:
    LoggerAdapter(std::shared_ptr<OldLogger> logger) : oldLogger_(logger) {}
    void logMessage(const std::string &message) override {
        if (oldLogger_)
            oldLogger_->writeEntry(message.c_str());
    }
};
// Client code that expects a ModernLogger
void clientCode(ModernLogger &logger) { logger.logMessage("This is a test message."); }
int main() {
    auto oldLoggerInstance = std::make_shared<OldLogger>();
    LoggerAdapter adapter(oldLoggerInstance);
    clientCode(adapter);
    return 0;
}