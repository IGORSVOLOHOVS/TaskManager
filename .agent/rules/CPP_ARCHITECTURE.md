---
trigger: model_decision
description: Architectural standards enforcing ISO/IEC 25010:2023, Quality Attribute Scenarios, C4 Diagramming, and ADRs.
---

# C++ Architecture Standards

When designing the architecture of a C++ application, you must strictly follow standards based on ISO/IEC 25010:2023.

## 1. Quality Attributes (ISO 25010)

For any significant architectural change, you must evaluate its impact across the 9 attributes:
- Functional Suitability
- Performance Efficiency (critically important for C++)
- Compatibility
- Usability
- Reliability (memory safety, race conditions)
- Security (buffer overflows, ASan)
- Maintainability (Functional Core)
- Portability (Cross-platform CMake)
- Safety

## 2. C4 Model (Mermaid JS)

Document components using C4 diagrams in Mermaid:
1. **System Context**
2. **Container**
3. **Component**
4. **Code / Class Diagram**

*All blocks in Mermaid must avoid special characters unless quoted.*

## 3. Architecture Decision Records (ADR)

For every technological choice, create an ADR in the MADR format:
1. **Context and Problem Statement**
2. **Decision Drivers**
3. **Considered Options**
4. **Decision Outcome**
5. **Pros and Cons Analysis** (MANDATORY: An ISO 25010 Matrix for all options 9x3)
6. **References**

Your tone should be analytical, proving the choice through numbers (benchmark measurements, latency, O(n) complexity) and facts.
