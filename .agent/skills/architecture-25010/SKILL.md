---
name: architecture-25010
description: Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. Use when making architecture decisions or analyzing system design.
---

# ISO/IEC 25010 Architecture Framework

> "The quality of a system is the degree to which the system satisfies the stated and implied needs of its stakeholders."

## 1. Quality Attribute Scenarios (The 9 Axes)
When designing a system, evaluate each decision against these quality characteristics:

1. **Functional Suitability:** Does it provide the required functions?
2. **Performance Efficiency:** Response times, throughput, and resource usage.
3. **Compatibility:** Coexistence and interoperability with other systems.
4. **Usability:** Efficiency, satisfaction, and accessibility for users.
5. **Reliability:** Availability, fault tolerance, and recoverability.
6. **Security:** Confidentiality, integrity, non-repudiation, and accountability.
7. **Maintainability:** Modularity, reusability, analyzability, and testability.
8. **Portability:** Adaptability, installability, and replaceability.
9. **Efficiency:** Resource utilization (especially memory and CPU).

---

## 2. Architectural Decision Records (ADR)
Document every major decision to capture the rationale and trade-offs.

### Structure:
- **Title:** [Decision Title]
- **Status:** [Proposed / Accepted / Superseded]
- **Context:** [Problem and background]
- **Decision:** [Selected approach]
- **Rationale:** [Why we chose this (referencing ISO 25010)]
- **Trade-offs:** [What we sacrifice (e.g., Performance for Maintainability)]
- **Consequences:** [Follow-up actions]

---

## 3. Pattern Selection (C++)
Choose patterns that maximize the 9 quality axes:

- **Performance:** Use `CPP_DOD.md` (Data-Oriented Design) and `CPP_BENCHMARK.md`.
- **Maintainability:** Use `CPP_CLEAN_ARCH.md` and `CPP_FUNCTIONAL_CORE.md`.
- **Security:** Use `CPP_STATIC_ANALYSIS.md` and `vulnerability-scanner`.
- **Reliability:** Use `CPP_TESTING.md` and `CPP_TEST_COVERAGE.md`.

---

## 4. Hierarchy Of Needs
1. **Correctness** (Functional Suitability)
2. **Safety** (Security/Reliability)
3. **Clarity** (Maintainability)
4. **Performance** (Efficiency)

> **Rule:** Never sacrifice Correctness or Safety for Performance without a proven bottleneck and a documented trade-off.
