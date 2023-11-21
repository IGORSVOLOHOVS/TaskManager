cmake_minimum_required(VERSION 3.28)
project(project CXX)

set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD 20)

find_package(benchmark REQUIRED)
find_package(yaml-cpp REQUIRED)
find_package(gtest REQUIRED)


# Create a static library 'module'
add_library(modules_lib STATIC)
target_sources(modules_lib
PUBLIC
FILE_SET CXX_MODULES FILES
    "test/test.ixx"
    "test/benchmark.ixx"
    "config/config.ixx"
    "io.ixx"
)

# link libraries
target_link_libraries(modules_lib PUBLIC yaml-cpp::yaml-cpp benchmark::benchmark gtest::gtest)

# Create the main executable
add_executable(main main.cxx)
target_link_libraries(main modules_lib)


# conan remove yaml-cpp/0.8.0
# Remove-Item -Path "*.cmake*", "*.ps1", "*.bat", "*.json" -Recurse -Force
# rm -r build

# run powershell with admin
# Set-ExecutionPolicy RemoteSigned
# conan install . --build=missing --output-folder build -c tools.env.virtualenv:powershell=True
# cmake --preset conan-release OR cmake --preset conan-default
# cmake --build --preset conan-release
# .\build\build\generators\conanbuild.ps1
# .\build\build\generators\conanrun.ps1
# .\build\build\Release\main.exe
