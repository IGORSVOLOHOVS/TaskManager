---
trigger: model_decision
description: Clean / Hexagonal Architecture for C++. Core domain has zero dependency on external frameworks, databases, or UI.
---

# CPP_CLEAN_ARCH.md — Clean / Hexagonal Architecture

> **MANDATORY:** The `core/` domain must NEVER `#include` anything from Qt, database drivers, network libraries, or any framework header. Ports are **Concepts**, not virtual base classes.

## 🎯 Dependency Rule
Dependencies flow **inward only**. The innermost layer (Core Domain) knows nothing about the outer layers:

```
┌─────────────────────────────────┐
│      Frameworks / IO / UI       │  ← Qt, REST, DB drivers
│  ┌───────────────────────────┐  │
│  │   Interface Adapters      │  │  ← Concrete Repos, Controllers
│  │  ┌─────────────────────┐  │  │
│  │  │  Application Use    │  │  │  ← Use Cases (template on Concepts)
│  │  │     Cases           │  │  │
│  │  │  ┌───────────────┐  │  │  │
│  │  │  │ Core Domain   │  │  │  │  ← Entities, Value Objects, Concepts
│  │  │  └───────────────┘  │  │  │
│  │  └─────────────────────┘  │  │
│  └───────────────────────────┘  │
└─────────────────────────────────┘
```

## 🔌 Ports as Concepts — Zero Virtual Overhead
Instead of a pure virtual `IUserRepository`, define a **Concept** in `core/`:

```cpp
// core/ports/user_repository.hpp — Port (no includes of any framework!)
#pragma once
#include <expected>
#include "core/domain/user.hpp"

// The "interface" is a compile-time Concept — no vtable, no heap allocation
template<typename Repo>
concept UserRepositoryConcept = requires(Repo r, UserId id, const User& u) {
    { r.find_by_id(id) } -> std::same_as<std::expected<User, std::string>>;
    { r.save(u)         } -> std::same_as<std::expected<void, std::string>>;
};
```

## 🧩 Use Cases — Templated on Concepts
Use cases live in `core/use_cases/` and are **template functions** constrained by Concepts:

```cpp
// core/use_cases/update_email.hpp
#pragma once
#include "core/ports/user_repository.hpp"
#include "core/domain/email.hpp"

template<UserRepositoryConcept Repo>
std::expected<void, std::string>
update_user_email(Repo& repo, UserId id, Email new_email) noexcept {
    auto user = repo.find_by_id(id);
    if (!user) return std::unexpected(user.error());
    user->change_email(std::move(new_email));
    return repo.save(*user);
}
```

## 🧱 Adapters — Satisfy the Concept in the Shell
The concrete implementation sits in `shell/` and knows about the DB — but the core does not know it exists:

```cpp
// shell/adapters/sqlite_user_repository.hpp
#pragma once
#include <sqlite3.h>                         // framework dep stays in shell
#include "core/ports/user_repository.hpp"    // only the Concept is imported

class SqliteUserRepository {  // NO base class needed!
public:
    std::expected<User, std::string> find_by_id(UserId id) const noexcept;
    std::expected<void, std::string> save(const User& u) noexcept;
// Concept check at instantiation: static_assert(UserRepositoryConcept<SqliteUserRepository>);
};
```

## 🧪 Testability via Concept-Satisfying Mocks
```cpp
// tests/mocks/mock_user_repository.hpp
struct MockUserRepository {
    std::expected<User, std::string> find_by_id(UserId) const noexcept {
        return User{ .name = "Test User" }; // deterministic, no DB
    }
    std::expected<void, std::string> save(const User&) noexcept { return {}; }
};
// Verifies at compile time that the mock satisfies the port:
static_assert(UserRepositoryConcept<MockUserRepository>);
```

## Directory Layout
```
src/
  core/
    domain/      ← Entities, Value Objects, Concepts (zero framework deps)
    ports/       ← Concept definitions (UserRepositoryConcept, etc.)
    use_cases/   ← Template functions constrained by Concepts
  shell/
    adapters/    ← Concrete implementations (SQLite, HTTP, Qt UI)
    main.cpp     ← Composition Root: wires concrete types into template use cases
```

## Anti-Patterns
- `#include <QObject>` or `#include <sqlite3.h>` inside `core/`.
- Using `virtual` + vtables when a Concept delivers the same contract with zero runtime cost.
- Skipping `static_assert(MyConcept<MyAdapter>)` — always verify adapters satisfy ports.
