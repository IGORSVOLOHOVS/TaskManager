# https://github.com/IGORSVOLOHOVS/Easy_CMakefile
cmake_minimum_required(VERSION 3.20)
project(test_cmake CXX)

# Переменная VCPKG_PATH
set(VCPKG_PATH "C:/Users/User/.clion-vcpkg/vcpkg")

# Указываем путь к файлу CMakeLists.txt для vcpkg
set(CMAKE_TOOLCHAIN_FILE ${VCPKG_PATH}/scripts/buildsystems/vcpkg.cmake)

# Устанавливаем стандарт C++ на C++20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(-DCURL_STATICLIB=ON)


# Проверяем и создаем директории bin, lib, include, src
file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/include)
file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/src)

# Указываем директории с заголовочными файлами и библиотеками из vcpkg
include_directories(
    ${VCPKG_PATH}/installed/x64-windows/include
)

link_directories(
    ${VCPKG_PATH}/installed/x64-windows/lib
)

# Добавляем путь к собственным исходным файлам (cpp)
file(GLOB_RECURSE SOURCES
    "src/*.cpp"
)

# Добавляем путь к заголовочным файлам (h)
file(GLOB_RECURSE HEADERS
    "include/*.h"
)

# Создаем исполняемый файл (или библиотеку)
add_executable(${PROJECT_NAME} ${SOURCES} ${HEADERS})

# Если вам нужно собрать статическую библиотеку вместо исполняемого файла:
# add_library(${PROJECT_NAME} STATIC ${SOURCES} ${HEADERS})

# Линковка с библиотеками из vcpkg
target_link_libraries(${PROJECT_NAME} PRIVATE
    # Укажите библиотеки из vcpkg, которые вам нужны
#    library1
#    library2
    # ...
    libcurl
)

# Если вы собираете статическую библиотеку, линкуйте ее так:
target_link_libraries(${PROJECT_NAME} PRIVATE
#     library1
#     library2
#     # ...
    libcurl
)