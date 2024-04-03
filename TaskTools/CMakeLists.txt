cmake_minimum_required(VERSION 3.20)
project(task CXX)


set(CMAKE_CXX_STANDARD                  23)
set(CMAKE_CXX_STANDARD_REQUIRED         ON)
set(CMAKE_POSITION_INDEPENDENT_CODE     TRUE)


option(SWIG_PYTHON      "Build python bindings" OFF)
option(SWIG_CSHARP      "Build csharp bindings" OFF)
option(WEB              "Build web version"     OFF)
option(DOCUMENTATION    "Build documentation"   OFF)
option(TESTS            "Build tests"           OFF)

include(dependences.cmake)


set(SOURCES
    src/main.cpp
)


add_library(${PROJECT_NAME}d                    SHARED ${SOURCES})
target_include_directories(${PROJECT_NAME}d     PUBLIC ${CMAKE_SOURCE_DIR}/include ${FetchContent_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME}d          PUBLIC ${FetchContent_LIBS})


add_executable(${PROJECT_NAME}                         ${SOURCES})
target_link_libraries(${PROJECT_NAME}           PUBLIC ${PROJECT_NAME}d)

# CWeb
if(WEB) # emcmake cmake -B build && cmake --build build && python3 -m http.server --directory web
    set_target_properties(${PROJECT_NAME} PROPERTIES
        SUFFIX      ".js" 
        LINK_FLAGS  "--bind -s EXPORTED_RUNTIME_METHODS=['ccall','cwrap'] -s MODULARIZE=1 -s ENVIRONMENT=web"
        RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/web
    )
    file(COPY ${CMAKE_SOURCE_DIR}/subsrc/index.html DESTINATION ${CMAKE_SOURCE_DIR}/web)
else()
    set_target_properties(${PROJECT_NAME} PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin
    )
endif()


# CTest
if (TESTS)
    enable_testing()
    add_subdirectory(test)
endif()


# CPack
install(TARGETS ${PROJECT_NAME} DESTINATION .)
install(FILES ${CMAKE_SOURCE_DIR}/LICENSE.txt DESTINATION .)
install(FILES ${CMAKE_SOURCE_DIR}/README.md DESTINATION .)
install(FILES ${CMAKE_SOURCE_DIR}/images/icon.ico DESTINATION .)

set(CPACK_PACKAGE_NAME                      "${PROJECT_NAME}")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY       "Template project for C++")
set(CPACK_PACKAGE_VERSION                   "1.0.0")
set(CPACK_PACKAGE_INSTALL_DIRECTORY         "${PROJECT_NAME}")
set(CPACK_RESOURCE_FILE_LICENSE             "${CMAKE_SOURCE_DIR}/LICENSE.txt")
set(CPACK_RESOURCE_FILE_README              "${CMAKE_SOURCE_DIR}/README.md")
set(CPACK_GENERATOR                         "NSIS")
set(CPACK_DESKTOP_SHORTCUTS                 "task") 
set(CPACK_NSIS_MUI_ICON                     "${CMAKE_SOURCE_DIR}/images/icon.ico")
set(CPACK_NSIS_MUI_UNIICON                  "${CMAKE_SOURCE_DIR}/images/icon.ico")
set(CPACK_NSIS_MODIFY_PATH                  ON)
set(CPACK_NSIS_CREATE_ICONS_EXTRA           "CreateShortCut '$DESKTOP\\\\${CPACK_PACKAGE_NAME}.lnk' '$INSTDIR\\\\${PROJECT_NAME}.exe' '' '$INSTDIR\\\\images\\\\icon.ico'")
set(CPACK_NSIS_DELETE_ICONS_EXTRA           "Delete '$DESKTOP\\\\${CPACK_PACKAGE_NAME}.lnk'")
set(CPACK_NSIS_EXECUTABLES_DIRECTORY        bin)

include(CPack)
