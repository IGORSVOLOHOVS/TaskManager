---
trigger: always_on
---

# GEMINI.md - Antigravity Polyglot Kit (C++ & Python)

> This file defines how the AI behaves in this workspace.

---

## CRITICAL: AGENT & SKILL PROTOCOL (START HERE)

> **MANDATORY:** You MUST read the appropriate agent file and its rules BEFORE performing any implementation. This is the highest priority rule.

### 1. Modular Loading Protocol

Agent activated → Check frontmatter "skills:" or context → Read Agent Rules → Apply All.
- **Rule Priority:** P0 (GEMINI.md) > P1 (Agent .md) > P2 (Workflow .md). All rules are binding.

### 2. Enforcement Protocol

1. **When agent is activated:**
    - ✅ Activate: Read Rules → Check Frontmatter → Load Workflows if needed → Apply All.
2. **Forbidden:** Never skip reading agent rules or workflow instructions. "Read → Understand → Apply" is mandatory.

---

## 📥 REQUEST CLASSIFIER (STEP 1)

**Before ANY action, classify the request:**

| Request Type     | Trigger Keywords                           | Action                      |
| ---------------- | ------------------------------------------ | --------------------------- |
| **QUESTION**     | "what is", "how does", "explain"           | Text Response               |
| **SURVEY/INTEL** | "analyze", "list files", "overview"        | Session Intel (No File)     |
| **SIMPLE CODE**  | "fix", "add", "change" (single file)       | Inline Edit                 |
| **COMPLEX CODE** | "build", "create", "implement", "refactor" | **{task-slug}.md Required** |
| **SYSTEM ARCH**  | "design", "architecture", "c4"             | **{task-slug}.md Required** |
| **SLASH CMD**    | /create, /build, /debug, /lint-python      | Command-specific flow       |

---

## 🤖 INTELLIGENT AGENT ROUTING (STEP 2 - AUTO)

**ALWAYS ACTIVE: Before responding to ANY request, automatically analyze and select the best agent(s) (C++ or Python).**

### Auto-Selection Protocol

1. **Analyze (Silent)**: Detect context (C++, Python, Architecture, DevOps, Debugging) from user request and file extensions being edited.
2. **Select Agent(s)**: Choose the most appropriate specialist(s) from `.agent/agents/` (e.g. `@cpp-specialist` or `@python-specialist`).
3. **Inform User**: Concisely state which expertise is being applied.
4. **Apply**: Generate response using the selected agent's persona.

### Response Format (MANDATORY)

When auto-applying an agent, inform the user:

```markdown
🤖 **Applying knowledge of `@[agent-name]`...**

[Continue with specialized response]
```

---

## TIER 0: UNIVERSAL RULES (Always Active)

### 🧹 Clean C++23 Code (When editing .cpp / .hpp)
**ALL code MUST follow `CPP_FUNCTIONAL_CORE.md`. No exceptions.**
- **Code**: Functional Core, Imperative Shell. `std::expected` for monads.
- **Testing**: Mandatory `doctest` tests for all logic.

### 🐍 Clean Python 3.10+ Code (When editing .py)
**ALL code MUST follow `PYTHON_CLEAN_CODE.md`. No exceptions.**
- **Code**: Strict type hints (`mypy --strict`), Ruff defaults.
- **Testing**: Pytest, fixtures, parametrization.

### 🌳 Git Workflow (Commits & Branches)
**ALL version control MUST follow `GIT_WORKFLOW.md`. No exceptions.**
- **Commits**: `action(scope): English desc.` (period at the end is mandatory).
- **Branches**: `main`, `test`, `dev`, `feat/*`, `bugfix/*`.

### 🗺️ System Map Read
> 🔴 **MANDATORY:** Understand the structure of `.agent/`
- Agents: `.agent/agents/`
- Rules: `.agent/rules/`
- Workflows: `.agent/workflows/`
- Scripts: `.agent/scripts/`

---

## TIER 1: CODE RULES (When Writing Code)

### 🛑 Socratic Gate

**For complex requests, STOP and ASK first:**

| Request Type            | Required Action                                                   |
| ----------------------- | ----------------------------------------------------------------- |
| **New Feature / Build** | ASK minimum 3 strategic architecture questions based on ISO 25010 |
| **Full Orchestration**  | **STOP** subagents until user confirms plan details               |

### 🏁 Final Checklist Protocol

**Trigger:** When the user says "final checks", "verify", or similar phrases.

If the project is largely Python: Run: `python3 .agent/scripts/verify_all_python.py`
If the project is C++: Run: `python3 .agent/scripts/verify_all.py`

> 🔴 **Agents can invoke ANY script** via `python3 .agent/scripts/<script>.py`
