cmake_minimum_required(VERSION 3.20)
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
  project(taskd LANGUAGES C CXX VERSION 1.0.0)
else()
  project(task LANGUAGES C CXX VERSION 1.0.0)
endif()

# ---------------------------- [ Initialization ] -------------------------------
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_INSTALL_PREFIX ${CMAKE_SOURCE_DIR}/${PROJECT_NAME}-${CMAKE_BUILD_TYPE}-${CMAKE_SYSTEM_NAME}-${CMAKE_CXX_COMPILER_ID}-${CMAKE_CXX_COMPILER_VERSION})

#----------------------------- [ external dependencies ] -------------------------
add_subdirectory(libs)
add_libs_dependency(libs_dependencies)
target_precompile_headers(libs_dependencies PRIVATE 
  ${CMAKE_SOURCE_DIR}/pch.hpp
  ${CMAKE_SOURCE_DIR}/structures.hpp
  ${CMAKE_SOURCE_DIR}/interfaces.hpp
)

# ---------------------------- [ Add subdirectories ] -----------------------------------------

# ---------------------------- [ .lib ] ----------------------------------------
add_library(${PROJECT_NAME} STATIC main.cpp task.hpp)
target_link_libraries(${PROJECT_NAME} PUBLIC 
  libs_dependencies
)

# ---------------------------- [ .exe ] -----------------------------------------
add_executable(main main.cpp)
target_link_libraries(main PRIVATE ${PROJECT_NAME})

# ---------------------------- [ Install ] --------------------------------------
install(TARGETS ${PROJECT_NAME} RUNTIME DESTINATION bin LIBRARY DESTINATION lib ARCHIVE DESTINATION lib)
install(TARGETS main RUNTIME DESTINATION bin LIBRARY DESTINATION lib ARCHIVE DESTINATION lib)
install(FILES task.hpp interfaces.hpp structures.hpp pch.hpp DESTINATION include)

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
