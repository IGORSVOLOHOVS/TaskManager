# Meta-Prompt: Initialize Full Project Workflow Prompts

**Task**: Generate a professional directory structure `workflow_prompts/` containing 25+ specialized prompts for every stage of the software development lifecycle.

**Instructions**:
1. Create the `workflow_prompts/` directory in the current workspace root.
2. Create each of the following files with their respective content.

---

### 1. Requirements Analysis
**File**: `workflow_prompts/01-requirements.md`
**Content**:
# Prompt: Requirement Extraction & ISO 25010 Profiling
Analyze the user request and extract functional and non-functional requirements. Profile the software based on ISO 25010 Quality Characteristics (Performance, Reliability, Security, Maintainability).

---

### 2. Architecture ADR
**File**: `workflow_prompts/02-adr.md`
**Content**:
# Prompt: Architectural Decision Record (ADR)
Document a critical architectural decision using the MADR template. Explain the context, options considered, and the final justification based on quality attribute trade-offs.

---

### 3. C4 Modeling
**File**: `workflow_prompts/03-c4-modeling.md`
**Content**:
# Prompt: C4 System Modeling
Create Mermaid.js diagrams for C4 Level 1 (System Context), Level 2 (Container), and Level 3 (Component). Focus on boundaries and communication protocols.

---

### 4. Technical Skeleton
**File**: `workflow_prompts/04-skeleton.md`
**Content**:
# Prompt: Technical Skeleton & Config
Generate the project structure and primary configuration files (CMakeLists.txt or pyproject.toml). Ensure strict linting and build standards are initialized.

---

### 5. Domain Modeling (DDD)
**File**: `workflow_prompts/05-ddd-modeling.md`
**Content**:
# Prompt: Domain-Driven Design Modeling
Identify Value Objects, Entities, and Aggregates. Define the Ubiquitous Language and Bounded Contexts for the core domain.

---

### 6. API & Contract Design
**File**: `workflow_prompts/06-api-contracts.md`
**Content**:
# Prompt: API & Contract Design
Design the public interface/API. Focus on header-only definitions (C++) or abstract base classes (Python) to establish strict contracts before implementation.

---

### 7. Containerization & CI
**File**: `workflow_prompts/07-docker-ci.md`
**Content**:
# Prompt: Docker & CI Pipeline
Create a multi-stage Dockerfile and a GitHub Actions / GitLab CI pipeline. Focus on reproducible builds and automated quality gates.

---

### 8. Testing Infrastructure
**File**: `workflow_prompts/08-testing-infra.md`
**Content**:
# Prompt: Testing Infrastructure Setup
Configure the testing framework (doctest or pytest). Set up mock objects, test fixtures, and coverage measurement tools.

---

### 9. Functional Core Implementation
**File**: `workflow_prompts/09-functional-core.md`
**Content**:
# Prompt: Atomic Functional Core
Implement the core business logic as a set of pure, stateless functions. Avoid side effects and ensure maximum testability.

---

### 10. Monadic Error Handling
**File**: `workflow_prompts/10-monadic-errors.md`
**Content**:
# Prompt: Monadic Error Flow
Integrate `std::expected` (C++) or Result patterns (Python) into the logic. Ensure all error paths are handled explicitly without exceptions.

---

### 11. Concurrency & State
**File**: `workflow_prompts/11-concurrency-state.md`
**Content**:
# Prompt: Concurrency & Message Passing
Implement state management using the Actor Model or Message Passing. Avoid shared-state mutexes in favor of thread isolation.

---

### 12. Imperative Shell Adapters
**File**: `workflow_prompts/12-imperative-shell.md`
**Content**:
# Prompt: Imperative Shell & Adapters
Implement adapters for external systems (Database, Network, File System). Ensure isolation from the Functional Core.

---

### 13. Observability & Logging
**File**: `workflow_prompts/13-observability.md`
**Content**:
# Prompt: Structured Logging & Telemetry
Integrate structured logging and performance telemetry. Ensure every major event is traceable and measurable.

---

### 14. Performance Baselines
**File**: `workflow_prompts/14-perf-baselines.md`
**Content**:
# Prompt: Performance Budgeting
Establish performance budgets and baselines for critical paths using micro-benchmarking tools (nanobench or pytest-benchmark).

---

### 15. Algorithmic Optimization
**File**: `workflow_prompts/15-optimization.md`
**Content**:
# Prompt: High-Performance Honing
Analyze and optimize critical paths for cache locality, SIMD utilization, or algorithmic complexity.

---

### 16. Security Audit
**File**: `workflow_prompts/16-security-audit.md`
**Content**:
# Prompt: Comprehensive Security Audit
Run static and dynamic security scans (Bandit, Sanitizers). Audit for common vulnerabilities (OWASP, Buffer Overflows, Python Injection).

---

### 17. Tech Debt & Code Smells
**File**: `workflow_prompts/17-lint-cleanup.md`
**Content**:
# Prompt: Technical Debt & Smells Audit
Identify and resolve code smells, duplication, and technical debt. Ensure strict adherence to the project's Clean Code rules.

---

### 18. Language Modernization
**File**: `workflow_prompts/18-modernization.md`
**Content**:
# Prompt: Language Standard Upgrade
Verify that the codebase fully utilizes the latest language features (C++23 Ranges/Concepts or Python 3.12+ type features).

---

### 19. Automated Documentation
**File**: `workflow_prompts/19-docs-auto.md`
**Content**:
# Prompt: Automated API Documentation
Generate professional API documentation (Doxygen or pdoc). Ensure all public interfaces are fully documented with examples.

---

### 20. Manual Craftsmanship (README)
**File**: `workflow_prompts/20-readme-crafting.md`
**Content**:
# Prompt: User-Centric Documentation
Write high-quality READMEs, Tutorials, and Installation guides. Focus on the user experience and clear onboarding.

---

### 21. Integrated Validation
**File**: `workflow_prompts/21-validation.md`
**Content**:
# Prompt: Full Validation Sweep
Run the complete verification suite (Format -> Lint -> Test -> Build). Ensure zero regressions before merging.

---

### 22. Standards Compliance
**File**: `workflow_prompts/22-compliance.md`
**Content**:
# Prompt: Licensing & Standards Audit
Audit for license compliance (OSS scanners) and adherence to industry standards (MISRA, PEP8, ISO).

---

### 23. Distribution & Packaging
**File**: `workflow_prompts/23-packaging.md`
**Content**:
# Prompt: Distribution Artifact Generation
Configure packaging (Conan, CPack, or Wheels). Build and verify final distributable artifacts.

---

### 24. Release Automation
**File**: `workflow_prompts/24-release-prep.md`
**Content**:
# Prompt: Release & Changelog Automation
Generate a detailed changelog and release notes. Automate version tagging and deployment notifications.

---

### 25. Final Handover (Brain)
**File**: `workflow_prompts/25-handoff.md`
**Content**:
# Prompt: Final Project Handoff
Perform a deep "Brain Extraction" of the entire project status. Provide a comprehensive summary for the next maintenance session.

---

**Completion**: Once all files are created, provide a table summarizing the 25 stages.
