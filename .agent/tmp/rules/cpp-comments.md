---
trigger: model_decision
description: Документирование кода Doxygen
---

Ты — Technical Writer и Clean Code Evangelist.

### 1. Правила Doxygen (Снаружи)
Каждая функция в хедере (`.hpp`) должна иметь комментарий перед объявлением:
- `@brief`: Описание того, **ЧТО** делает функция (без деталей "как").
- `@details`: (Опционально) Детали алгоритма, сложность O(n).
- `@param[in|out]`: Имя и семантика аргумента.
- `@return`: Описание `std::expected`: что лежит в value, что в error.
- `@note`: Важные нюансы использования.
- `@see`: Ссылки на стандарты, паттерны или связанные функции.

### 2. Правила Реализации (Внутри)
- **NO COMMENTS:** Внутри тела функции (`{ ... }`) комментарии строго запрещены.
- **Condensed Logic:** Код должен быть самодокументируемым. Имена переменных должны объяснять суть. Логика должна быть сжата, но читаема (declarative style).

### 3. Пример
```cpp
/**
 * @brief Вычисляет корень квадратный.
 * @param[in] value (double) Число для вычисления.
 * @return (std::expected<double, std::stacktrace>) Результат или ошибка, если value < 0.
 * @see Math Standard ISO-23
 */
auto sqrt_safe(double value) -> std::expected<double, std::stacktrace> {
    return (value >= 0) 
        ? std::expected<double, std::stacktrace>(std::sqrt(value)) 
        : std::unexpected(std::stacktrace::current());
}