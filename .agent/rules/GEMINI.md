---
trigger: always_on
---

# GEMINI.md - Antigravity C++ Kit

> This file defines how the AI behaves in this C++ workspace.

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
| **SLASH CMD**    | /create, /build, /debug                    | Command-specific flow       |

---

## 🤖 INTELLIGENT AGENT ROUTING (STEP 2 - AUTO)

**ALWAYS ACTIVE: Before responding to ANY request, automatically analyze and select the best C++ agent(s).**

### Auto-Selection Protocol

1. **Analyze (Silent)**: Detect domains (C++ Core, Architecture, DevOps, Debugging) from user request.
2. **Select Agent(s)**: Choose the most appropriate specialist(s) from `.agent/agents/`.
3. **Inform User**: Concisely state which expertise is being applied.
4. **Apply**: Generate response using the selected agent's persona.

### Response Format (MANDATORY)

When auto-applying an agent, inform the user:

```markdown
🤖 **Applying knowledge of `@[agent-name]`...**

[Continue with specialized response]
```

---

## TIER 0: UNIVERSAL C++ RULES (Always Active)

### 🧹 Clean C++23 Code (Global Mandatory)

**ALL code MUST follow `CPP_FUNCTIONAL_CORE.md`. No exceptions.**

- **Code**: Functional Core, Imperative Shell. `std::expected` for monads. Constexpr where possible.
- **Testing**: Mandatory `doctest` tests for all logic. Follow `cpp-test.md` logic.
- **Performance**: Move semantics (`std::move`, `T&&`), smart pointers (`std::unique_ptr`). No raw pointers unless observer.

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

**Trigger:** When the user says "final checks", "çalıştır tüm testleri", "verify", or similar phrases.

Run: `python3 .agent/scripts/verify_all.py`

**Priority Execution Order in CI:**
1. **Format** (`format.py`) → 2. **Lint** (`lint.py`) → 3. **Build** (`build.py`) → 4. **Test & Coverage** (`run_test_coverage.py`)

**Available Scripts:**

| Script                     | When to Use         |
| -------------------------- | ------------------- |
| `format.py`                | Fix code style      |
| `lint.py`                  | Static analysis     |
| `build.py`                 | Compiling via CMake |
| `run_test_coverage.py`     | Running doctest + lcov / OpenCppCoverage |
| `verify_all.py`            | Ultimate verification |

> 🔴 **Agents can invoke ANY script** via `python3 .agent/scripts/<script>.py`
