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
add_executable(task main.cxx)
target_link_libraries(task modules_lib)

# clang

# [settings]
# arch=x86_64
# build_type=Release
# compiler=clang
# compiler.cppstd=20
# compiler.version=17
# compiler.libcxx=libstdc++11
# compiler.runtime=dynamic
# compiler.runtime_type=Release
# compiler.runtime_version=v143
# os=Windows
# [conf]
# tools.env.virtualenv:powershell=True

# msvc

# [settings]
# arch=x86_64
# build_type=Release
# compiler=msvc
# compiler.cppstd=20
# compiler.version=193
# compiler.runtime=dynamic
# compiler.runtime_type=Release
# os=Windows
# [conf]
# tools.env.virtualenv:powershell=True

# gcc

# [settings]
# arch=x86_64
# build_type=Release
# compiler=gcc
# compiler.cppstd=20
# compiler.version=13.2
# compiler.libcxx=libstdc++11
# compiler.threads=win32
# compiler.exception=seh
# os=Windows
# [conf]
# tools.env.virtualenv:powershell=True
