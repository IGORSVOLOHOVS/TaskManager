set(LIBS_FOR_SWIG_PYTHON my)
set(LIBS_FOR_SWIG_CSHARP my)

find_package(Threads REQUIRED)
find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})

add_subdirectory(python)
add_subdirectory(csharp)