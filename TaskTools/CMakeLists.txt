# cmake .. -G "MinGW Makefiles" && cmake --build . && make && ./test_cmake.exe
cmake_minimum_required(VERSION 3.20)
project(task CXX)

# Устанавливаем стандарт C++ на C++20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Проверяем и создаем директории bin, lib, include, src
file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/include)
file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/src)

# берем переменные с конфигурационного файла
include(CMakeConfig.cmake)

# Добавляем путь к собственным исходным файлам
file(GLOB_RECURSE SOURCES
    "src/*.cpp"
    "src/*.c"
    "src/*.cxx"
    "src/*.cc"
)

# Добавляем путь к заголовочным файлам
file(GLOB_RECURSE HEADERS
    "include/*.h"
    "include/*.hpp"
)

# Подключение библиотек и заголовков
include_directories(${INCLUDE_DIRS})
link_directories(${LIB_DIRS})

# Создаем исполняемый файл (или библиотеку)
add_executable(${PROJECT_NAME} ${SOURCES} ${HEADERS})

# Линковка с библиотеками
target_link_libraries(${PROJECT_NAME} PRIVATE ${LINK_LIBS})

# устанавливаем
install(TARGETS ${PROJECT_NAME} DESTINATION ${CMAKE_BINARY_DIR}/bin)
install(FILES ${HEADERS} DESTINATION ${CMAKE_BINARY_DIR}/include)
install(FILES ${LINK_LIBS} DESTINATION ${CMAKE_BINARY_DIR}/lib)
