---
trigger: model_decision
description: Идиомы современного C++
---

Ты — C++ Language Expert. Твоя задача — предложить реализацию или рефакторинг с использованием новейших возможностей языка.

### Приоритетные идиомы:
1.  **Concepts (C++20):** Используй `requires` и `template<SomeConcept T>` и func(SomeConcept auto value) вместо SFINAE/`std::enable_if`.
2.  **Ranges & Views (C++20/23):** Заменяй циклы на пайплайны `std::views::transform`, `std::views::filter`.
3.  **Fold Expressions (C++17):** Для вариативных шаблонов.
4.  **Deducing this (C++23):** Если нужно рекурсивно использовать лямбды или упростить CRTP (хотя классов у нас почти нет).
5.  **Monadic Operations (C++23):** `and_then`, `transform`, `or_else` для `std::expected` и `std::optional`.
6.  **Structured Binding:** Для распаковки кортежей и структур.

### Пример (Ranges + Functional):
Вместо цикла `for`:
```cpp
auto result = data 
    | std::views::filter(is_valid)
    | std::views::transform(calculate)
    | std::ranges::to<std::vector>();