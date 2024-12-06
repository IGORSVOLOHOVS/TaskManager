cmake_minimum_required(VERSION 3.20)
project(task LANGUAGES C CXX VERSION 1.0.0)

# ---------------------------- [ Initialization ] -------------------------------
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_INSTALL_PREFIX ${CMAKE_SOURCE_DIR}/${PROJECT_NAME}-${CMAKE_BUILD_TYPE}-${CMAKE_SYSTEM_NAME}-${CMAKE_CXX_COMPILER_ID}-${CMAKE_CXX_COMPILER_VERSION})

# ---------------------------- [ libs ] -------------------------------
function(import_add lib_name folder)
  add_library(${lib_name} STATIC IMPORTED)
  set_target_properties(${lib_name} PROPERTIES
    IMPORTED_LOCATION "${folder}/lib/${lib_name}.lib"
  )
  target_include_directories(${lib_name} INTERFACE "${folder}/include")
endfunction()

#---[ Add subdirectories ]--- (do not delete this comment)
add_subdirectory(tools)

# ---------------------------- [ .exe ] -----------------------------------------
add_executable(${PROJECT_NAME} main.cpp task.hpp)
target_precompile_headers(${PROJECT_NAME} PRIVATE pch.hpp)
target_link_libraries(${PROJECT_NAME} PUBLIC ${PROJECT_NAME}_tools)

# ---------------------------- [ Install ] --------------------------------------
install(TARGETS ${PROJECT_NAME} DESTINATION bin)
install(FILES pch.hpp task.hpp DESTINATION include)


# ---------------------------- [ Doxygen ] ---------------------------------------
find_package(Doxygen)
set(DOXYFILE_PROJECT_NAME "Task")
set(DOXYFILE_PROJECT_BRIEF "The templates for tasks")
set(DOXYFILE_PROJECT_VERSION "1.0.0")
set(DOXYFILE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/documentation")
set(DOXYFILE_SOURCE_DIRS "${CMAKE_CURRENT_SOURCE_DIR}")
set(DOXYFILE_GENERATE_LATEX NO) # Disable LaTeX generation
set(DOXYFILE_HTML_STYLESHEET "${CMAKE_CURRENT_SOURCE_DIR}/tools/other/Doxyfile.css")
configure_file(tools/other/Doxyfile.in ${CMAKE_BINARY_DIR}/Doxyfile @ONLY)

add_custom_target(documentation
  COMMAND doxygen ${CMAKE_BINARY_DIR}/Doxyfile
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
  COMMAND chrome ${CMAKE_BINARY_DIR}/documentation/html/index.html
)

# ---------------------------- [ CPack ] -----------------------------------------
include(InstallRequiredSystemLibraries)

set(CPACK_PACKAGE_VERSION ${VERSION})
set(CPACK_PACKAGE_NAME ${PROJECT_NAME})
set(CPACK_RESOURCE_FILE_README "${CMAKE_CURRENT_SOURCE_DIR}/tools/other/README.md")
set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/tools/other/LICENSE.txt")
set(CPACK_NSIS_MUI_ICON "${CMAKE_CURRENT_SOURCE_DIR}/tools/other/icon.ico")

include(CPack)
