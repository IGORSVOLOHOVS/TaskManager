#include "test.hpp"
#include "benchmark.hpp"
#include "stopwatch.hpp"

int main(int argc, char** argv) {
    stopwatch::Stopwatch w;
    

    // Configure program
    w.start();
    config::parser();
    std::cout << "Elapsed: " << w.lap<stopwatch::ns>() << " milliseconds." << std::endl;

    // Run Google Test
    w.start();
    test::run();
    std::cout << "Elapsed: " << w.lap<stopwatch::ns>() << " milliseconds." << std::endl;

    // Run Google Benchmark
    w.start();
    benchmark::run();
    std::cout << "Elapsed: " << w.lap<stopwatch::ns>() << " milliseconds." << std::endl;

    return 0;
}
