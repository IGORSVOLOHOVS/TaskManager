---
name: memory-management
description: Rules for smart pointers, zero-copy, and memory safety.
---

# C++ Memory Management & Safety

> "Own what you create; borrow what you need."

## 1. The Rule of Zero Heap
Prefer stack-based allocation and deterministic object lifetimes over `new` and `delete`.

---

## 2. Smart Pointers (C++23)
- **`std::unique_ptr`:** Default for ownership. Use `std::make_unique<T>()`.
- **`std::shared_ptr`:** Only for truly shared ownership where lifetime is unpredictable. Use `std::make_shared<T>()`.
- **`std::weak_ptr`:** For breaking circular dependencies.

---

## 3. Borrowing (No-Copy)
Minimize data duplication across the system.
- **`std::string_view`:** Lightweight, non-owning reference to a string constant or buffer.
- **`std::span<T>`:** View over a contiguous sequence of objects (like an array or vector).
- **References:** Pass by `const T&` by default unless you need to modify the data.

---

## 4. RAII (Resource Acquisition Is Initialization)
Resources (memory, file handles, locks) must be bound to object lifetimes.
- Never use a raw pointer to "own" a resource.
- Cleanup must happen automatically in the destructor.

---

## 5. Memory Safety Checklist
- [ ] No `new` or `delete` in the codebase.
- [ ] No raw pointer arithmetic.
- [ ] No returning references to local temporary objects.
- [ ] Use `std::move` only when ownership transfer is intentional.
- [ ] Verify all paths with AddressSanitizer (`ASan`) to ensure no leaks or buffer overflows.

---

## 6. Anti-Patterns
- **`std::shared_ptr` as default:** It adds reference-counting overhead and can hide architectural flaws.
- **Dangling References:** Passing a reference to a lambda that outlives the scope.
- **Manual Management:** Forgetting to free memory or doing it twice.

> **Rule:** If a pointer is just an observer (no ownership), it's a raw pointer or a reference. If it's an owner, it's a smart pointer.
