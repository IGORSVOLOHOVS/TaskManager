cmake_minimum_required(VERSION 3.20)
project(task CXX)

# Устанавливаем стандарт C++ на C++20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(benchmark REQUIRED)
find_package(yaml-cpp REQUIRED)
find_package(gtest REQUIRED)
find_package(pybind11 REQUIRED)  # Добавление pybind11

# Создание Python модуля из module/main.cpp и include/custom_include.hpp
pybind11_add_module(py${PROJECT_NAME} src/main.cpp)
target_include_directories(py${PROJECT_NAME} PRIVATE ${CMAKE_SOURCE_DIR}/include)
target_link_libraries(py${PROJECT_NAME} PRIVATE benchmark::benchmark yaml-cpp::yaml-cpp gtest::gtest)

# copy task.py to build directory
configure_file(${CMAKE_SOURCE_DIR}/task.py ${CMAKE_BINARY_DIR}/task.py COPYONLY)