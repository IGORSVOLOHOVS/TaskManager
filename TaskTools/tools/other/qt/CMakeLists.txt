cmake_minimum_required(VERSION 3.20)
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
  project(taskd LANGUAGES C CXX VERSION 1.0.0)
else()
  project(task LANGUAGES C CXX VERSION 1.0.0)
endif()

# ---------------------------- [ Initialization ] -------------------------------
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_INSTALL_PREFIX ${CMAKE_SOURCE_DIR}/${PROJECT_NAME}-${CMAKE_BUILD_TYPE}-${CMAKE_SYSTEM_NAME}-${CMAKE_CXX_COMPILER_ID}-${CMAKE_CXX_COMPILER_VERSION})

#----------------------------- [ external dependencies ] -------------------------
find_package(Qt6 REQUIRED COMPONENTS Quick)

add_subdirectory(libs)
add_libs_dependency(libs_dependencies)
target_link_libraries(libs_dependencies PUBLIC
    Qt6::Quick
)
target_precompile_headers(libs_dependencies PRIVATE 
  ${CMAKE_SOURCE_DIR}/pch.hpp
  ${CMAKE_SOURCE_DIR}/structures.hpp
  ${CMAKE_SOURCE_DIR}/interfaces.hpp
)

# ---------------------------- [ Add subdirectories ] -----------------------------------------

# ---------------------------- [ .exe ] -----------------------------------------
qt_add_executable(main main.cpp task.hpp)
target_link_libraries(main PUBLIC
    libs_dependencies
)
qt_add_qml_module(main
    URI untitled1
    VERSION 1.0
    QML_FILES
        Main.qml
        SOURCES backend.hpp backend.cpp
)


# ---------------------------- [ Install ] --------------------------------------
install(TARGETS main RUNTIME DESTINATION bin LIBRARY DESTINATION lib ARCHIVE DESTINATION lib)
install(FILES task.hpp interfaces.hpp structures.hpp pch.hpp backend.hpp Main.qml DESTINATION include)
install(FILES fonts/Roboto-Regular.ttf DESTINATION fonts)

