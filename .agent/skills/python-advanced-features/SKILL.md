---
name: python-advanced-features
description: Explains core Pythonic concepts like generators, decorators, context managers, and asyncio.
---

# Advanced Python Features

As an AI, you should utilize modern, professional Python features to produce concise and highly performant code.

## 1. Generators (`yield`)
Whenever a function returns a sequence of items and we only need to iterate over them once, use generators (`yield`) instead of collecting them in a list. This reduces memory footprint.

## 2. Context Managers (`with`)
Any resource acquisition (files, network connections, locks, temporary directories) MUST use `with` context managers. If you are building a custom resource, implement `__enter__` and `__exit__`.

## 3. Decorators
Use decorators to wrap reusable logic (timing, logging, authentication, retries). Use `functools.wraps` on the inner wrapper function to preserve the metadata of the decorated function.

## 4. Asyncio
When writing network-bound code, leverage `asyncio`, `aiohttp`, or `httpx`. Mark functions with `async def` and use `await` on I/O. Remember that CPU-bound operations inside async functions will block the event loop; offload them to `asyncio.to_thread`.
