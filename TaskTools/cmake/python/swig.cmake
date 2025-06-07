set(CMP0148 OLD)

find_package(Threads REQUIRED)
find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})

find_package(PythonInterp 3.13 REQUIRED)
find_package(PythonLibs 3.13 REQUIRED)
include_directories(${PYTHON_INCLUDE_PATH})

set_property(SOURCE ${CMAKE_CURRENT_SOURCE_DIR}/cmake/python/task.i PROPERTY CPLUSPLUS ON)
swig_add_library(TaskAPI
    TYPE SHARED
    LANGUAGE python
    OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}
    SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/cmake/python/task.i
)
swig_link_libraries(TaskAPI PUBLIC 
    Task
    ${CMAKE_THREAD_LIBS_INIT} 
    ${PYTHON_LIBRARIES}
)
target_include_directories(TaskAPI PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/source ${PYTHON_INCLUDE_PATH})

set_target_properties(TaskAPI PROPERTIES OUTPUT_NAME TaskAPI)
set_target_properties(TaskAPI PROPERTIES SWIG_USE_TARGET_INCLUDE_DIRECTORIES TRUE)
set_target_properties(TaskAPI PROPERTIES USE_SWIG_DEPENDENCIES TRUE)
set_target_properties(TaskAPI PROPERTIES SWIG_FLAGS "-c++ -std=c++23 -threads -doxygen -includeall -flatstaticmethod -fastproxy -extranative -builtin  -castmode -py3")

# remove ${CMAKE_CURRENT_BINARY_DIR}/WaamAPIPYTHON_wrap.cxx
file(REMOVE ${CMAKE_CURRENT_BINARY_DIR}/WaamAPIPYTHON_wrap.cxx)
