#include <custom_include.hpp>

int main(int argc, char** argv) {
    // Configure program
    config::parser();

    // Run Google Test
    test::run();

    // Run Google Benchmark
    benchmark::run();

    getchar();
}