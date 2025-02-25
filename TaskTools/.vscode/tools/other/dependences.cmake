cmake_minimum_required(VERSION 3.5)

set(FetchContent_INCLUDE_DIRS "")
set(FetchContent_LIBS "")
set(FetchContent_MAKE_AVAILABLE "")

# Install dependencies
# include (FetchContent)
# find_package(benchmark QUIET)
# if(NOT benchmark_FOUND)
#     FetchContent_Declare(
#     benchmark
#     GIT_REPOSITORY https://github.com/google/benchmark.git
#     GIT_TAG        main
#     )
#     list(APPEND FetchContent_MAKE_AVAILABLE benchmark)
#     list(APPEND FetchContent_INCLUDE_DIRS ${benchmark_SOURCE_DIR}/include)
#     list(APPEND FetchContent_LIBS benchmark::benchmark)
# endif()

# FetchContent_MakeAvailable(${FetchContent_MAKE_AVAILABLE})


# Python wrapper
if(SWIG_PYTHON)
    set(SWIG_DIRECTOR_NORTTI on)
    set(SWIG_USE_TARGET_INCLUDE_DIRECTORIES on)
    find_package(SWIG REQUIRED)
    include(${SWIG_USE_FILE}) 

    find_package(PythonLibs)
    include_directories(${PYTHON_INCLUDE_PATH} ${FetchContent_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR}/include)
    set_source_files_properties(${CMAKE_CURRENT_SOURCE_DIR}/subsrc/wrapper.i PROPERTIES CPLUSPLUS ON ${PYTHON_INCLUDE_PATH} ${FetchContent_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR}/include)
    message("PYTHON_LIBRARIES: ${CMAKE_CURRENT_SOURCE_DIR}/subsrc/wrapper.i PROPERTIES CPLUSPLUS ON USE_TARGET_INCLUDE_DIRECTORIES ON INCLUDE_DIRECTORIES ${PYTHON_INCLUDE_PATH} ${FetchContent_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR}/include)")
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

# CSharp wrapper
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

if(DOCUMENTATION)
    find_package(Doxygen)
    if(NOT DOXYGEN_FOUND)
        message(FATAL_ERROR "Doxygen not found, please install it to generate the documentation")
    endif()
    find_package(LATEX OPTIONAL_COMPONENTS PDFLATEX)
    if(NOT LATEX_PDFLATEX_FOUND)
        message("PDFLaTeX not found. PDF documentation will not be generated.")
    endif()

    add_custom_target(Doxygen ALL
        COMMAND ${DOXYGEN_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        COMMENT "Generating API documentation with Doxygen"
        VERBATIM)

    if(LATEX_PDFLATEX_FOUND)
        add_custom_command(
            OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/docs/latex/refman.pdf
            COMMAND make
            WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/docs/latex
            DEPENDS Doxygen
            COMMENT "Generating PDF documentation with LaTeX"
        )

        add_custom_target(DoxygenPDF ALL
            DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/docs/latex/refman.pdf
            COMMENT "PDF documentation is available at ${DOXYGEN_OUTPUT_DIR}/latex/refman.pdf"
        )
    endif()
endif()
