cmake_minimum_required(VERSION 3.5)

include (FetchContent)
set(FetchContent_TEST_MAKE_AVAILABLE "")
set(FetchContent_TEST_INCLUDE_DIRS "")
set(FetchContent_TEST_LIBS "")

# if benchmark not found
found_package(benchmark QUIET)
if(NOT benchmark_FOUND)
    FetchContent_Declare(
    benchmark
    GIT_REPOSITORY https://github.com/google/benchmark.git
    GIT_TAG        main
    )
    list(APPEND FetchContent_TEST_MAKE_AVAILABLE benchmark)
    list(APPEND FetchContent_TEST_INCLUDE_DIRS ${benchmark_SOURCE_DIR}/include)
    list(APPEND FetchContent_TEST_LIBS benchmark::benchmark)
endif()

# if gtest not found
found_package(gtest QUIET)
if(NOT gtest_FOUND)
    FetchContent_Declare(
    gtest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG        main
    )
    list(APPEND FetchContent_TEST_MAKE_AVAILABLE gtest)
    list(APPEND FetchContent_TEST_INCLUDE_DIRS ${gtest_SOURCE_DIR}/googletest/include)
    list(APPEND FetchContent_TEST_LIBS gtest)
endif()
    
# if yaml-cpp not found
found_package(yaml-cpp QUIET)
if(NOT yaml-cpp_FOUND)
    FetchContent_Declare(
    yaml-cpp
    GIT_REPOSITORY https://github.com/jbeder/yaml-cpp.git
    GIT_TAG        master
    )
    list(APPEND FetchContent_TEST_MAKE_AVAILABLE yaml-cpp)
    list(APPEND FetchContent_TEST_INCLUDE_DIRS ${yaml-cpp_SOURCE_DIR}/include)
    list(APPEND FetchContent_TEST_LIBS yaml-cpp::yaml-cpp)
endif()

FetchContent_MakeAvailable(${FetchContent_TEST_MAKE_AVAILABLE})