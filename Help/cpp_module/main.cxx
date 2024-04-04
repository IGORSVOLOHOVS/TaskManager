import io;
import config.config;
import test.test;
import test.benchmark;

int main(int argc, char** argv) {
    // Configure program
    config::parser();

    // Run Google Test
    test::run(argc, argv);

    // Run Google Benchmark
    benchmark::run(argc, argv);
}

