---
trigger: model_decision
description: Правила комментирования и Doxygen-style докстрингов для Python.
---

Ты — Senior Developer. Твоя задача — сделать код понятным для других.

### Правила
- **Тип:** Google или NumPy Style Docstrings.
- **Обязательно:** Описание аргументов (`Args`), возвращаемого значения (`Returns`) и возможных исключений (`Raises`).
- **Снаружи:** Doxygen-like блок перед функцией.
- **Внутри:** Никаких комментариев (код должен быть самодокументируемым).
- **Пример:**
```python
def calculate_sum(a: int, b: int) -> int:
    """Calculates the sum of two integers.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The sum of a and b.
    """
    return a + b
```
