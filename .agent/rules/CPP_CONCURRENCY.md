---
trigger: model_decision
description: Concurrency architecture for C++. Message Passing and Actor Model over raw shared-state mutex patterns.
---

# CPP_CONCURRENCY.md — Concurrency Architecture (Actor / CSP Model)

> **MANDATORY:** Raw `std::mutex` is BANNED from `core/` layer. Shared mutable state is the root of all concurrency bugs. Channels and Actors are constrained via Concepts.

## 🧠 Core Principle: Share Memory by Communicating, Not Communicate by Sharing Memory

## 📬 Channel Concept — Type-Safe Message Pipes
```cpp
// Concept: anything that can act as a typed channel
template<typename T, typename MsgType>
concept Channel = requires(T ch, MsgType m) {
    { ch.send(std::move(m)) } -> std::same_as<void>;
    { ch.receive()          } -> std::same_as<MsgType>;
};

// Concept: anything that can receive (subscribe-only side)
template<typename T, typename MsgType>
concept Sender = requires(T ch, MsgType m) {
    { ch.send(std::move(m)) } -> std::same_as<void>;
};
```

## 🔒 Concrete Channel Implementation (Shell Layer)
```cpp
template<typename T>
class BoundedChannel {
public:
    void send(T msg) {
        std::unique_lock lock(m_mutex);
        m_cv_full.wait(lock, [&]{ return m_queue.size() < m_capacity; });
        m_queue.push(std::move(msg));
        m_cv_empty.notify_one();
    }

    T receive() {
        std::unique_lock lock(m_mutex);
        m_cv_empty.wait(lock, [&]{ return !m_queue.empty(); });
        T msg = std::move(m_queue.front());
        m_queue.pop();
        m_cv_full.notify_one();
        return msg;
    }

private:
    std::queue<T>           m_queue;
    std::mutex              m_mutex;
    std::condition_variable m_cv_empty, m_cv_full;
    std::size_t             m_capacity{64};
};
// Verify it satisfies the concept:
static_assert(Channel<BoundedChannel<int>, int>);
```

## 🎭 Actor — Concept-Constrained Message Handler
```cpp
// Concept: anything that can act as a message handler
template<typename T, typename MsgType>
concept MessageHandler = requires(T actor, MsgType msg) {
    { actor.handle(std::move(msg)) } -> std::same_as<void>;
};

// Generic Actor runner — works for any type satisfying both Concepts
template<typename MsgType, Channel<MsgType> Ch, MessageHandler<MsgType> Handler>
void run_actor(Ch& inbox, Handler& handler) {
    while (true) {
        auto msg = inbox.receive();
        handler.handle(std::move(msg));
    }
}

// Concrete actor — plain struct, no base class, no virtual
struct PricingHandler {
    using Msg = std::variant<PriceUpdateMsg, ShutdownMsg>;

    void handle(Msg msg) noexcept {
        std::visit([&](auto&& m) { process(m); }, std::move(msg));
    }

private:
    void process(PriceUpdateMsg m) noexcept { m_last_price = m.price; }
    void process(ShutdownMsg)     noexcept  { std::exit(0); }

    double m_last_price = 0.0;
};
// Compile-time verification:
static_assert(MessageHandler<PricingHandler, PricingHandler::Msg>);
```

## Rules
1. **Core logic functions must be pure** — no shared mutable state → no data race possible.
2. **Shell layer handles thread lifecycles.** Spawn `std::jthread` in `main.cpp` only.
3. **Prefer `std::jthread`** (C++20) over `std::thread` — guaranteed join on scope exit.
4. **Use `std::atomic` for simple counters only.** For composite state, use Concept-constrained Channels.
5. **`static_assert` every Channel and Handler** against its Concept to catch regressions at compile time.

## Anti-Patterns
- Protecting a class with `std::mutex` accessed by 10 threads simultaneously (duct-tape concurrency).
- Storing shared state in `static` variables accessed concurrently.
- Locking two mutexes in different orders across threads (guaranteed deadlock).
- Using `virtual` for Actor dispatch — `std::variant` + `std::visit` is zero-overhead.
