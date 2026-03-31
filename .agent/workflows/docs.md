---
description: Workflow for generating C++ architecture documentation and Mermaid diagrams.
---

# /docs

When instructed to generate documentation:

1. **Roles and Duties**: Adopt the persona from `@[.agent/agents/documentation-writer.md]`.
2. **Scan Code**: Read the recent additions to the `core/` headers.
3. **Doxygen Gen**: Ensure valid `/// @brief`, `/// @param`, and `/// @return` tags are present in header files.
4. **ADR Generation**: Discuss with the user if a new Architecture Decision Record is needed.
5. **Mermaid Context**: Generate C4 component diagrams within `docs/architecture/` showing the relationship between the `shell` boundary and the `core` logic.
