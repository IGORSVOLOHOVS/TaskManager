cmake_minimum_required(VERSION 3.20)
project(task CXX)


set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE TRUE)


option(SWIG_PYTHON "Build python bindings" OFF)
option(SWIG_CSHARP "Build csharp bindings" OFF)
option(DOCUMENTATION "Build documentation" ON)

include(dependences.cmake)


file(GLOB_RECURSE SOURCES
    "src/*.cpp"
    "src/*.c"
    "src/*.cxx"
    "src/*.cc"
    "include/*.h"
    "include/*.hpp"
)


add_executable(${PROJECT_NAME} ${SOURCES})
target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_SOURCE_DIR}/include ${FetchContent_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME} PRIVATE ${FetchContent_LIBS})

# CTest
enable_testing()
add_subdirectory(test)


# CPack
install(TARGETS ${PROJECT_NAME} DESTINATION .)
install(FILES ${CMAKE_SOURCE_DIR}/LICENSE.txt DESTINATION .)
install(FILES ${CMAKE_SOURCE_DIR}/README.md DESTINATION .)
install(FILES ${CMAKE_SOURCE_DIR}/icon.ico DESTINATION .)
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
set(CPACK_NSIS_CREATE_ICONS_EXTRA    "CreateShortCut '$DESKTOP\\\\${CPACK_PACKAGE_NAME}.lnk' '$INSTDIR\\\\${PROJECT_NAME}.exe' '' '$INSTDIR\\\\icon.ico'")
set(CPACK_NSIS_DELETE_ICONS_EXTRA    "Delete '$DESKTOP\\\\${CPACK_PACKAGE_NAME}.lnk'")
set(CPACK_NSIS_EXECUTABLES_DIRECTORY bin)

include(CPack)