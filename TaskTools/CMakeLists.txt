
cmake_minimum_required(VERSION 3.23)
project(Task LANGUAGES CXX VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_EXTENSIONS OFF) # Отключаем расширения GNU, используем чистый стандарт
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include(cmake/flags/flags.cmake)
include(cmake/format/format.cmake)
include(cmake/git/git.cmake)
include(cmake/targets.cmake)

file(GLOB LIB_SOURCES "src/*.cpp")
list(FILTER LIB_SOURCES EXCLUDE REGEX ".*/main\.cpp$")

add_library(${PROJECT_NAME} STATIC ${LIB_SOURCES})
target_include_directories(${PROJECT_NAME} PUBLIC src extern) # Делаем src и extern доступными для тех, кто линкует lib_imp
target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_23)
target_precompile_headers(${PROJECT_NAME} PRIVATE "${PROJECT_SOURCE_DIR}/extern/pch.hpp") 

find_package(spdlog REQUIRED)
target_link_libraries(${PROJECT_NAME} PUBLIC spdlog::spdlog)


option("${PROJECT_NAME}TestsFlag" "Build tests" ON)
option("${PROJECT_NAME}ExampleFlag" "Build examples" ON)
option("${PROJECT_NAME}DataFlag" "Build tests" OFF)

if(${PROJECT_NAME}TestsFlag)
  enable_testing()
  find_package(GTest REQUIRED CONFIG) # Используем CONFIG для поиска gtest-config.cmake от Conan

  file(GLOB TEST1_SOURCES "tests/*.cpp")
  list(FILTER TEST1_SOURCES EXCLUDE REGEX ".*/main_test\.cpp$")
  add_executable(${PROJECT_NAME}Main ${GTEST_RUNNER_SOURCES} ${TEST1_SOURCES})
  target_link_libraries(${PROJECT_NAME}Main PRIVATE ${PROJECT_NAME} GTest::gtest GTest::gtest_main)
  target_include_directories(${PROJECT_NAME}Main PRIVATE src tests) # Добавляем tests в пути для тестов
  target_compile_features(${PROJECT_NAME}Main PRIVATE cxx_std_23)

  add_test(NAME ${PROJECT_NAME}Main COMMAND ${PROJECT_NAME}Main)
endif()

if(${PROJECT_NAME}ExampleFlag)
  add_subdirectory(example)
endif()

if(${PROJECT_NAME}DataFlag)
  include(cmake/structs/structs.cmake)
endif()

if(CMAKE_BUILD_TYPE STREQUAL "Release")
  include(cmake/python/swig.cmake)
endif()

