#include "test.hpp"
#include "benchmark.hpp"

int main(int argc, char** argv) {
    // Configure program
    config::parser();

    // Run Google Test
    test::run();

    // Run Google Benchmark
    benchmark::run();
}