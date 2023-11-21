#include <iostream>

import io;
import config.config;
import test.test;
import test.benchmark;

int main(int argc, char** argv) {
    // Run Google Test
    test::run(argc, argv);

    // Run Google Benchmark
    benchmark::run(argc, argv);

    return EXIT_SUCCESS;
}
