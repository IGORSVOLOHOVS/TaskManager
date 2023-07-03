#mkdir build
#cd build
#cmake .. -G "Visual Studio 16 2019" -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local
#cmake --build .

cmake_minimum_required(VERSION 3.0.0)
project(new_project VERSION 0.1.0)

set(CMAKE_TOOLCHAIN_FILE "C:/vcpkg/vcpkg/scripts/buildsystems/vcpkg.cmake" CACHE STRING "")

include(CTest)
enable_testing()

file(GLOB TARGET_SRC "./src/*.cpp" )
file(GLOB TARGET_HEADERS "./include/*.h")

add_executable(main ${TARGET_SRC} ${TARGET_HEADERS})

# Добавление пути к динамическим библиотекам
link_directories(${CMAKE_SOURCE_DIR}/bin)

# Добавление динамических библиотек к исполняемому файлу
target_link_libraries(main PUBLIC lib1 lib2 lib3)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)


