cmake_minimum_required(VERSION 3.28)
project(project CXX)

set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD 20)

find_package(benchmark REQUIRED)
find_package(yaml-cpp REQUIRED)
find_package(gtest REQUIRED)

# include modules
include(modules.cmake)
add_module_library(modules_lib
    test/test.ixx
    test/benchmark.ixx
    config/config.ixx
    io.ixx
)

# link libraries
target_link_libraries(modules_lib PUBLIC yaml-cpp::yaml-cpp benchmark::benchmark gtest::gtest)

# Create the main executable
add_executable(main main.cxx)
target_link_libraries(main modules_lib)
