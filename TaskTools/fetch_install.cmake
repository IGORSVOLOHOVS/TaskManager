cmake_minimum_required(VERSION 3.5)

include (FetchContent)
set(BENCHMARK_ENABLE_TESTING OFF)
FetchContent_Declare(
  gtest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        main
)
FetchContent_Declare(
  benchmark
  GIT_REPOSITORY https://github.com/google/benchmark.git
  GIT_TAG        main
)
FetchContent_Declare(
  yaml-cpp
  GIT_REPOSITORY https://github.com/jbeder/yaml-cpp.git
  GIT_TAG        master
)
FetchContent_MakeAvailable(benchmark gtest yaml-cpp)

set(FetchContent_INCLUDE_DIRS 
    ${yaml-cpp_SOURCE_DIR}/include 
    ${gtest_SOURCE_DIR}/googletest/include 
    ${benchmark_SOURCE_DIR}/include
)

set(FetchContent_LIBS
    yaml-cpp::yaml-cpp 
    benchmark::benchmark 
    gtest
)