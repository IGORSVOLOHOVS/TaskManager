# AntigravityCppKit Architecture

This repository is powered by a multi-agent AI system specifically designed for modern C++23 development.

## 🗺️ System Map

- **`.agent/rules/`**: Global rules enforced by the AI across the workspace. Start by reading `GEMINI.md`.
  - `CPP_ARCHITECTURE.md`: Enforcement of ISO 25010 Quality Attributes and C4 Modeling.
  - `CPP_FUNCTIONAL_CORE.md`: Enforcement of the "Functional Core, Imperative Shell" design style.
- **`.agent/agents/`**: Personas for the AI. Each agent specializes in a distinct area of C++ development (e.g., `cpp-specialist`, `systems-architect`, `qa-automation-engineer`).
- **`.agent/workflows/`**: Established step-by-step processes for planning, building, testing, and debugging C++ applications.
- **`.agent/scripts/`**: Automation scripts for linting, formatting, and coverage, which the agents use to verify code quality.

## Execution Flow

1. **Routing**: A user request is classified in `GEMINI.md` and routed to the correct agent in `agents/`.
2. **Execution**: The agent pulls rules from `rules/` and follows procedures from `workflows/`.
3. **Verification**: Before concluding, the agent runs `scripts/verify_all.py` (or specific scripts like `run_test_coverage.py`) to guarantee code correctness via CMake/CTest.
