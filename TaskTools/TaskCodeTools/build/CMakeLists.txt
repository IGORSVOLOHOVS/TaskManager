# cmake .. -G "MinGW Makefiles" && cmake --build . && make && ./test_cmake.exe
cmake_minimum_required(VERSION 3.20)
project(test_cmake CXX)

# For MinGW,VCPKG_PATH и CMAKE_TOOLCHAIN_FILE можно убрать
if (MINGW)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -static-libgcc -static-libstdc++")
endif()

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

# Указываем директории с заголовочными файлами и библиотеками из vcpkg(C:\msys64\mingw64\include)
include_directories(
    ${VCPKG_PATH}/installed/x64-windows/include
)

# C:\msys64\mingw64\lib
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

# классная вещь CMake заменит @PROJECT_VERSION_MAJOR@ и @PROJECT_VERSION_MINOR@ на соответствующие значения переменных и создаст файл config.h
# set(Tutorial_VERSION_MAJOR 1) set(Tutorial_VERSION_MINOR 0) configure_file(TutorialConfig.h.in TutorialConfig.h)
# классная вещь Эта команда включает в себя другой CMakeLists.txt файл из указанной поддиректории
# add_subdirectory(source_dir [binary_dir] [EXCLUDE_FROM_ALL])
# классная вещь, флаги компиляции без всякой херни
# target_compile_options(my_app PRIVATE -std=c++20)
# Команда option в CMake используется для объявления кэш-переменных с типом BOOL для if(USE_MY_LIB) elseif(USE_MY_LIB2) else() endif()
# option(USE_MY_LIB "Use my own library" ON)
# копирует my_app в папку bin
# add_executable(my_app main.cpp) install(TARGETS my_app RUNTIME DESTINATION bin)
# message
# message("This is an external configuration.")
# Включение предустановленного модуля для поиска библиотеки ZLIB
# include(FindZLIB)

# Создаем исполняемый файл (или библиотеку)
add_executable(${PROJECT_NAME} ${SOURCES} ${HEADERS})

# Если вам нужно собрать статическую библиотеку вместо исполняемого файла:
# add_library(${PROJECT_NAME} STATIC ${SOURCES} ${HEADERS})

# Линковка с библиотеками из vcpkg C:\msys64\mingw64\bin
target_link_libraries(${PROJECT_NAME} PRIVATE
    # Укажите библиотеки из vcpkg, которые вам нужны
#    library1
#    library2
    # ...
    libcurl
)

# Если вы собираете статическую библиотеку, линкуйте ее так: C:\msys64\mingw64\lib
target_link_libraries(${PROJECT_NAME} PRIVATE
#     library1
#     library2
#     # ...
    libcurl
)
