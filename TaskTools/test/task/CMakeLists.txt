cmake_minimum_required(VERSION 3.20)
project(test_task CXX)

# Добавляем путь к собственным исходным файлам
file(GLOB_RECURSE TASK_TEST_SOURCES
    "src/*.cpp"
    "src/*.c"
    "src/*.cxx"
    "src/*.cc"
    "src/*.h"
    "src/*.hpp"
)

# Создаем исполняемый файл (или библиотеку)
add_executable(${PROJECT_NAME} ${SOURCES})

# Линковка с библиотеками
target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_SOURCE_DIR}/src ${FetchContent_INCLUDE_DIRS} ${FetchContent_TEST_INCLUDE_DIRS}) 
target_link_libraries(${PROJECT_NAME} PRIVATE ${FetchContent_LIBS} ${FetchContent_TEST_LIBS})
