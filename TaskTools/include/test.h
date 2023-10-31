#include <benchmark/benchmark.h>
#include <cassert>
#include <iostream>
#include <string>
#include <functional>

static void BM_StringCreation(benchmark::State& state) {
  for (auto _ : state)
    std::string empty_string;
}
// Register the function as a benchmark
BENCHMARK(BM_StringCreation);

// Define another benchmark
static void BM_StringCopy(benchmark::State& state) {
  std::string x = "hello";
  for (auto _ : state)
    std::string copy(x);
}
BENCHMARK(BM_StringCopy);

//BENCHMARK_MAIN();

namespace test{

    void test_functions(){
        uint8_t number = 0;

        std::cout << "Test " << number++ << ": " << "test_functions" << std::endl;
        {            
            assert(1 == 1 && "1 == 1");
            assert(2 == 2 && "2 == 2");
            assert(3 == 3 && "3 == 3");
        }

        std::cout << "Test " << number++ << ": " << "test_classes" << std::endl;
        {
            assert(1 == 1 && "1 == 1");
            assert(2 == 2 && "2 == 2");
            assert(3 == 3 && "3 == 3");
        }
    }
    void test_classes(){
        assert(1 == 1);
    }
    void test_structs(){
        assert(1 == 1);
    }
}

void call_func_n(std::function<void()> func, int n) {
    for (int i = 0; i < n; i++) {
        func();
    }
}
