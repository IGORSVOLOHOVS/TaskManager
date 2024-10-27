# find_package(CSharp REQUIRED)

set_property(SOURCE swig.i PROPERTY CPLUSPLUS ON)
swig_add_library(swig_csharp
    TYPE SHARED
    LANGUAGE csharp
    OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}
    SOURCES swig.i
)
swig_link_libraries(swig_csharp PUBLIC ${LIBS_FOR_SWIG_CSHARP} ${CMAKE_THREAD_LIBS_INIT})
target_include_directories(swig_csharp PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../..)

set_target_properties(swig_csharp PROPERTIES OUTPUT_NAME swig_csharp)
set_target_properties(swig_csharp PROPERTIES SWIG_USE_TARGET_INCLUDE_DIRECTORIES TRUE)
set_target_properties(swig_csharp PROPERTIES USE_SWIG_DEPENDENCIES TRUE)
set_target_properties(swig_csharp PROPERTIES SWIG_FLAGS "-c++ -std=c++23 -w0 -m64 -debug-tm")