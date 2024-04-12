#include <future>

#define AsyncFunction(n, rt)                                std::future<rt> n##_async(){return std::async(std::launch::async, [&]() { return n(); });}

#define AsyncFunction1(n, rt, at)                           std::future<rt> n##_async(at a){return std::async(std::launch::async, [&]() { return n(a); });}
#define AsyncFunction2(n, rt, at1, at2)                     std::future<rt> n##_async(at1 a1, at2 a2){return std::async(std::launch::async, [&]() { return n(a1, a2); });}
#define AsyncFunction3(n, rt, at1, at2, at3)                std::future<rt> n##_async(at1 a1, at2 a2, at3 a3){return std::async(std::launch::async, [&]() { return n(a1, a2, a3); });}
#define AsyncFunction4(n, rt, at1, at2, at3, at4)           std::future<rt> n##_async(at1 a1, at2 a2, at3 a3, at4 a4){return std::async(std::launch::async, [&]() { return n(a1, a2, a3, a4); });}
#define AsyncFunction5(n, rt, at1, at2, at3, at4, at5)      std::future<rt> n##_async(at1 a1, at2 a2, at3 a3, at4 a4, at5 a5){return std::async(std::launch::async, [&]() { return n(a1, a2, a3, a4, a5); });}

#define AsyncFunctionN(n, rt, ...)                          std::future<rt> n##_async(){return std::async(std::launch::async, [&]() { return n(__VA_ARGS__); });}