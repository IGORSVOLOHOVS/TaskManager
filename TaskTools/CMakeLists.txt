cmake_minimum_required(VERSION 3.20)
project(task LANGUAGES C CXX VERSION 1.0.0)

# ---------------------------- [ Initialization ] -------------------------------

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_INSTALL_PREFIX ${CMAKE_SOURCE_DIR}/${PROJECT_NAME}-${CMAKE_BUILD_TYPE}-${CMAKE_SYSTEM_NAME}-${VERSION})

if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    set(CMAKE_CXX_FLAGS_DEBUG   "${CMAKE_CXX_FLAGS_DEBUG} -O0 -g -ggdb -D_DEBUG")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Ofast -march=native -g -ggdb -DNDEBUG")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -pg")
elseif(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    set(CMAKE_CXX_FLAGS_DEBUG   "${CMAKE_CXX_FLAGS_DEBUG} -O0 -g -ggdb -D_DEBUG")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Ofast -march=native -g -ggdb -DNDEBUG")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -pg")
elseif(CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
endif()

# ---------------------------- [ libs ] -------------------------------

# Everything looking for libraries(to add PATH)
# vcpkg integrate install + triplet
# choco install
# sudo apt install
# conan install
# FetchContent CPM

#---[ Add subdirectories ]--- (do not delete this comment)
add_subdirectory(tools)

# ---------------------------- [ .exe ] -------------------------------

set(source 
    task.cpp
)
set(header
    task/task.hpp
)

add_executable(task ${source} ${header})
target_link_libraries(${PROJECT_NAME} PUBLIC tools)

# ---------------------------- [ Doxygen ] ----------------------------

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
  COMMENT "Generating API documentation with Doxygen"

  COMMAND ${CMAKE_COMMAND} -E echo "Opening the browser..."
  COMMAND chrome ${CMAKE_BINARY_DIR}/documentation/html/index.html
)
