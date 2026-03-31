---
description: Workflow for analyzing requirements and generating ISO 25010 compliant C4 architecture.
---

# Plan Architecture Workflow

1. Research the codebase by using `grep_search` and `list_dir`. Identify core structures.
2. Draft an implementation plan. 
3. If new foundational classes or libraries are introduced, create a new file in `docs/architecture/decisions/` mapping the alternatives you considered using the MADR template outlined in `CPP_ARCHITECTURE.md`.
4. Create a comprehensive C4 `System Context` and `Container` diagram in Mermaid.js format in `docs/architecture/c4.md`.
5. Present the plan to the user using the Socratic Gate (checking for Edge Cases and Trade-offs).
6. Proceed only after explicit user approval.
