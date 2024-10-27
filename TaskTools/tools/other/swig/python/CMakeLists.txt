find_package(PythonLibs 3 REQUIRED)
find_package(PythonInterp ${PYTHONLIBS_VERSION_STRING} REQUIRED)
include_directories(${PYTHON_INCLUDE_PATH})

set_property(SOURCE swig.i PROPERTY CPLUSPLUS ON)
swig_add_library(swig_python
    TYPE SHARED
    LANGUAGE python
    OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}
    SOURCES swig.i
)
swig_link_libraries(swig_python PUBLIC ${LIBS_FOR_SWIG_PYTHON} ${CMAKE_THREAD_LIBS_INIT} ${PYTHON_LIBRARIES})
target_include_directories(swig_python PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../.. ${PYTHON_INCLUDE_PATH})

set_target_properties(swig_python PROPERTIES OUTPUT_NAME swig_python)
set_target_properties(swig_python PROPERTIES SWIG_USE_TARGET_INCLUDE_DIRECTORIES TRUE)
set_target_properties(swig_python PROPERTIES USE_SWIG_DEPENDENCIES TRUE)
set_target_properties(swig_python PROPERTIES SWIG_FLAGS "-c++ -std=c++23 -w0 -m64 -debug-tm")