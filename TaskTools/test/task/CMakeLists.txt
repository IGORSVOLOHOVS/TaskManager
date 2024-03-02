cmake_minimum_required(VERSION 3.20)
project(test_task CXX)


file(GLOB_RECURSE TASK_TEST_SOURCES
    "src/*.cpp"
    "src/*.c"
    "src/*.cxx"
    "src/*.cc"
    "src/*.h"
    "src/*.hpp"
)


add_executable(${PROJECT_NAME} ${TASK_TEST_SOURCES})
target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/src ${FetchContent_INCLUDE_DIRS} ${FetchContent_TEST_INCLUDE_DIRS}) 
target_link_libraries(${PROJECT_NAME} PRIVATE ${FetchContent_LIBS} ${FetchContent_TEST_LIBS})
file(COPY test.yaml DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/test)

add_test(NAME ${PROJECT_NAME} COMMAND ${PROJECT_NAME})
