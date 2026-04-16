---
name: pytest-workflow
description: TDD and advanced testing features using the pytest framework.
---

# Pytest Workflow

## Core Principles
1. **Red, Green, Refactor**: Always write tests to fail first. Ensure they fail for the *right reason*.
2. **Setup, Act, Assert (Given, When, Then)**: Structure every test block visually this way.

## Advanced Pytest Usage
- **Fixtures (`@pytest.fixture`)**: Use for dependency injection into tests. Prefer fixtures over globals or setup/teardown methods. Use `yield` inside the fixture to perform teardown after the test runs.
- **Parametrization (`@pytest.mark.parametrize`)**: To run the same test logic over diverse input/output combinations. Do not write loops inside tests if parametrization solves it cleanly.
- **Mocking (`pytest-mock` / `mocker`)**: Use the `mocker` fixture to patch expensive or external dependencies. e.g. `mocker.patch("my_module.my_func")`.
- **Exceptions (`pytest.raises`)**: Assert that a block of code throws exactly the expected exception by using `with pytest.raises(ExpectedException):`.
