cmake_minimum_required(VERSION 3.5)

include (FetchContent)
set(BENCHMARK_ENABLE_TESTING OFF)
FetchContent_Declare(
  gtest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        main
)
FetchContent_Declare(
  benchmark
  GIT_REPOSITORY https://github.com/google/benchmark.git
  GIT_TAG        main
)
FetchContent_Declare(
  yaml-cpp
  GIT_REPOSITORY https://github.com/jbeder/yaml-cpp.git
  GIT_TAG        master
)
FetchContent_MakeAvailable(benchmark gtest yaml-cpp)

set(FetchContent_INCLUDE_DIRS 
    ${yaml-cpp_SOURCE_DIR}/include 
    ${gtest_SOURCE_DIR}/googletest/include 
    ${benchmark_SOURCE_DIR}/include
)

set(FetchContent_LIBS
    yaml-cpp::yaml-cpp 
    benchmark::benchmark 
    gtest
)

# swig python
if(SWIG_PYTHON)
    set(SWIG_USE_TARGET_INCLUDE_DIRECTORIES on)
    find_package(SWIG REQUIRED)
    include(${SWIG_USE_FILE}) 

    find_package(PythonLibs)
    include_directories(${PYTHON_INCLUDE_PATH} ${FetchContent_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR}/include)
    set_source_files_properties(subsrc/wrapper.i PROPERTIES CPLUSPLUS ON USE_TARGET_INCLUDE_DIRECTORIES on INCLUDE_DIRECTORIES ${PYTHON_INCLUDE_PATH} ${FetchContent_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR}/include)
    swig_add_library(taskl 
        TYPE SHARED 
        LANGUAGE python
        OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/python
        SOURCES subsrc/wrapper.i
    )
    swig_link_libraries(taskl ${PYTHON_LIBRARIES} ${FetchContent_LIBS})
    # move the generated taskl file to the ${CMAKE_CURRENT_BINARY_DIR}/python
    set_target_properties(_taskl PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/python)
    file(COPY subsrc/test.py DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/python)
endif()

# swig java
if(SWIG_JAVA)
    find_package(SWIG REQUIRED)
    include(${SWIG_USE_FILE}) 

    find_package(Java)
    include(UseJava)
    include_directories(${Java_INCLUDE_PATH} ${FetchContent_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR}/include)
    set_source_files_properties(subsrc/wrapper.i PROPERTIES CPLUSPLUS ON)
    swig_add_library(ltask 
        TYPE SHARED 
        LANGUAGE java
        OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/java
        SOURCES subsrc/wrapper.i
    )
    swig_link_libraries(ltask ${Java_LIBRARIES} ${FetchContent_LIBS})
    target_include_directories(ltask PUBLIC ${Java_INCLUDE_PATH} ${FetchContent_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR}/include)
endif()

# swig csharp
if(SWIG_CSHARP)
    find_package(SWIG REQUIRED)
    include(${SWIG_USE_FILE}) 

    find_package(Mono)
    include_directories(${Mono_INCLUDE_PATH} ${FetchContent_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR}/include)
    set_source_files_properties(subsrc/wrapper.i PROPERTIES CPLUSPLUS ON)
    swig_add_library(ltask 
        TYPE SHARED 
        LANGUAGE csharp
        OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/csharp
        SOURCES subsrc/wrapper.i
    )
    swig_link_libraries(ltask ${Mono_LIBRARIES} ${FetchContent_LIBS})
    target_include_directories(ltask PUBLIC ${Mono_INCLUDE_PATH} ${FetchContent_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR}/include)
endif()