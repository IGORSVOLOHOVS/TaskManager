cmake_minimum_required(VERSION 3.20)
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
  project(taskd LANGUAGES C CXX VERSION 1.0.0)
else()
  project(task LANGUAGES C CXX VERSION 1.0.0)
endif()

# ---------------------------- [ Initialization ] -------------------------------
set(CMAKE_CXX_STANDARD 23)
include(libs/init.cmake)

#----------------------------- [ external dependencies ] -------------------------
add_subdirectory(libs)
add_libs(libs)

# ---------------------------- [ .lib ] ----------------------------------------
add_subdirectory(task)

# ---------------------------- [ .exe ] -----------------------------------------
add_executable(main main.cpp)
target_link_libraries(main PRIVATE ${PROJECT_NAME})

# ---------------------------- [ Install ] --------------------------------------
install(TARGETS main DESTINATION ${CMAKE_INSTALL_PREFIX}/bin)
