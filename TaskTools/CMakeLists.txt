cmake_minimum_required(VERSION 3.20)
project(task LANGUAGES C CXX VERSION 1.0.0)

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


set(source task.cpp)

#---[ Add subdirectories ]--- (do not delete this comment)
add_subdirectory(tools)

add_executable(task ${source})
target_link_libraries(${PROJECT_NAME} PUBLIC tools)

# include(InstallRequiredSystemLibraries)
# include(CMakePackageConfigHelpers)
# include(CPack)

# install(DIRECTORY include/ DESTINATION include)
# install(TARGETS ${PROJECT_NAME} ${PROJECT_NAME}d
#     LIBRARY DESTINATION lib
#     ARCHIVE DESTINATION lib
#     RUNTIME DESTINATION bin
# )
# install(FILES 
#     "${PROJECT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
#     "${PROJECT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
#     DESTINATION lib/cmake/${PROJECT_NAME}
# )

# file(WRITE ${PROJECT_NAME}Config.cmake.in "@PACKAGE_INIT@
# include(CMakeFindDependencyMacro)
# # ����� ������������
# #find_dependency(���_�����������)
# set(${PROJECT_NAME}_FOUND TRUE)
# set(${PROJECT_NAME}_INCLUDE_DIRS include)
# set(${PROJECT_NAME}_LIBRARIES ${PROJECT_NAME}d) # ����������� ��� ������ ������� ��� ����������
# ")
# configure_package_config_file(
#     "${PROJECT_SOURCE_DIR}/${PROJECT_NAME}Config.cmake.in" # ������ ����������������� �����
#     "${PROJECT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
#     INSTALL_DESTINATION lib/cmake/${PROJECT_NAME}
# )
# write_basic_package_version_file(
#     "${PROJECT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
#     VERSION ${PROJECT_VERSION}
#     COMPATIBILITY SameMajorVersion
# )
