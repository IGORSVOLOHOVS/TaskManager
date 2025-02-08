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

# ---------------------------- [ .lib ] ----------------------------------------
add_library(${PROJECT_NAME} STATIC main.cpp task.hpp)
target_link_libraries(${PROJECT_NAME} PUBLIC 
  libs_dependencies
)

# ---------------------------- [ Add subdirectories ] -----------------------------------------

# ---------------------------- [ .exe ] -----------------------------------------
add_executable(main main.cpp)
target_link_libraries(main PRIVATE ${PROJECT_NAME})

# ---------------------------- [ Install ] --------------------------------------
install(TARGETS ${PROJECT_NAME} RUNTIME DESTINATION bin LIBRARY DESTINATION lib ARCHIVE DESTINATION lib)
install(TARGETS main RUNTIME DESTINATION bin LIBRARY DESTINATION lib ARCHIVE DESTINATION lib)
install(FILES task.hpp interfaces.hpp structures.hpp pch.hpp DESTINATION include)

