---
trigger: "/plan-architecture-python"
description: "Workflow for analyzing requirements and generating ISO 25010 compliant C4 architecture for Python."
---

# Workflow: Python Architecture Planning

**Context**: The user wants to design or refactor a Python system, ensuring it meets quality requirements.

## Steps
1. **Requirements Gathering**:
   - Use `@architecture` or `@architecture-25010` skills.
   - Define Functional and Non-functional requirements.
2. **System Decomposition**:
   - Identify modules, services, and external dependencies.
3. **Draft C4 Diagrams**:
   - Create Mermaid diagrams (System, Container, Component).
4. **Technology Stack Selection**:
   - Choose frameworks (FastAPI, Flask, Django, etc.).
   - Define data persistence strategies (SQLAlchemy, Tortoise ORM).
5. **Quality Attribute Scenarios (ISO 25010)**:
   - Analyze reliability, performance efficiency, and maintainability.
6. **ADR Generation**: Document architectural decisions in `docs/adr/`.
