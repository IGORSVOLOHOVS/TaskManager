cmake_minimum_required(VERSION 3.20)
project(task CXX)

# Устанавливаем стандарт C++ на C++20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE TRUE)


set(FETCH_INSTALL ON)
if(FETCH_INSTALL)
    option(SWIG_PYTHON "Build python bindings" ON)
    option(SWIG_JAVA "Build java bindings" OFF)
    option(SWIG_CSHARP "Build csharp bindings" OFF)
    
    include(dependences.cmake)
endif()

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
target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_SOURCE_DIR}/include ${FetchContent_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME} PRIVATE ${FetchContent_LIBS})

# Установка исполняемых файлов, заголовочных файлов, лицензии и README
install(TARGETS ${PROJECT_NAME} DESTINATION .)

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
    "CreateShortCut '$DESKTOP\\\\${CPACK_PACKAGE_NAME}.lnk' '$INSTDIR\\\\${PROJECT_NAME}.exe' '' '$INSTDIR\\\\icon.ico'")
set(CPACK_NSIS_DELETE_ICONS_EXTRA
    "Delete '$DESKTOP\\\\${CPACK_PACKAGE_NAME}.lnk'")
set(CPACK_NSIS_EXECUTABLES_DIRECTORY bin)

include(CPack)