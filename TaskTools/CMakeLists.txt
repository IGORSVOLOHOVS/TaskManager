cmake_minimum_required(VERSION 3.20)
project(task CXX)

# Устанавливаем стандарт C++ на C++20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(benchmark REQUIRED)
find_package(yaml-cpp REQUIRED)
find_package(gtest REQUIRED)

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

# Создаем исполняемый файл (или библиотеку)
add_executable(${PROJECT_NAME} ${SOURCES} ${HEADERS})

# Линковка с библиотеками
target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_SOURCE_DIR}/include)
target_link_libraries(${PROJECT_NAME} PRIVATE benchmark::benchmark yaml-cpp::yaml-cpp gtest::gtest)

# Установка исполняемых файлов, заголовочных файлов, лицензии и README
install(TARGETS ${PROJECT_NAME} DESTINATION bin)

install(DIRECTORY ${benchmark_BIN_DIRS_RELEASE} DESTINATION .)
install(DIRECTORY ${yaml-cpp_BIN_DIRS_RELEASE} DESTINATION .)
install(DIRECTORY ${gtest_BIN_DIRS_RELEASE} DESTINATION .)

install(FILES ${HEADERS} DESTINATION include)

install(FILES ${CMAKE_SOURCE_DIR}/LICENSE.txt DESTINATION .)
install(FILES ${CMAKE_SOURCE_DIR}/README.md DESTINATION .)
install(FILES ${CMAKE_SOURCE_DIR}/icon.ico DESTINATION .)



# Настройка CPack
set(CPACK_PACKAGE_NAME "${PROJECT_NAME}")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Template project for C++")
set(CPACK_PACKAGE_VERSION "1.0.0")
set(CPACK_PACKAGE_INSTALL_DIRECTORY "${PROJECT_NAME}")
set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_SOURCE_DIR}/LICENSE.txt")
set(CPACK_RESOURCE_FILE_README "${CMAKE_SOURCE_DIR}/README.md")
set(CPACK_GENERATOR "NSIS")
set(CPACK_DESKTOP_SHORTCUTS "task") 
set(CPACK_NSIS_MUI_ICON "${CMAKE_SOURCE_DIR}/icon.ico")
set(CPACK_NSIS_MUI_UNIICON "${CMAKE_SOURCE_DIR}/icon.ico")
set(CPACK_NSIS_MODIFY_PATH ON)

# Создание ярлыка на рабочем столе
set(CPACK_NSIS_CREATE_ICONS_EXTRA
    "CreateShortCut '$DESKTOP\\\\${CPACK_PACKAGE_NAME}.lnk' '$INSTDIR\\\\bin\\\\${PROJECT_NAME}.exe' '' '$INSTDIR\\\\icon.ico'")
set(CPACK_NSIS_DELETE_ICONS_EXTRA
    "Delete '$DESKTOP\\\\${CPACK_PACKAGE_NAME}.lnk'")
set(CPACK_NSIS_EXECUTABLES_DIRECTORY bin)

include(CPack)

# cmake_minimum_required(VERSION 3.28)
# project(project CXX)

# set(CMAKE_CXX_EXTENSIONS OFF)
# set(CMAKE_CXX_STANDARD 20)

# find_package(benchmark REQUIRED)
# find_package(yaml-cpp REQUIRED)
# find_package(gtest REQUIRED)

# # Автоматически добавляем все .hpp файлы из папки include
# file(GLOB HEADERS "include/*.hpp")

# # Указываем папку для header файлов
# include_directories(${CMAKE_SOURCE_DIR}/include)

# # Автоматически добавляем все .cpp файлы из папки src
# file(GLOB SOURCES "src/*.cpp")

# add_library(custom_include STATIC ${SOURCES} ${HEADERS})

# # Связываем библиотеки с нашим приложением
# target_link_libraries(custom_include PUBLIC benchmark::benchmark yaml-cpp::yaml-cpp gtest::gtest)

# # Создаем исполняемый файл
# add_executable(main main.cpp)

# # Связываем библиотеки с нашим приложением
# target_link_libraries(main PUBLIC custom_include)




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
