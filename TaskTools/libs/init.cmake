set(CMAKE_INSTALL_PREFIX ${CMAKE_SOURCE_DIR}/${PROJECT_NAME}-${CMAKE_BUILD_TYPE}-${CMAKE_SYSTEM_NAME}-${CMAKE_CXX_COMPILER_ID}-${CMAKE_CXX_COMPILER_VERSION})

if (WIN64 OR WIN32)
  if(NOT DEFINED TASK_COMPILER)
    set(TASK_COMPILER "MSVC")
  endif()
else()
  if(NOT DEFINED TASK_COMPILER)
    set(TASK_COMPILER "GCC")
  endif()
endif()

if(NOT DEFINED CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "Release")
endif()

# find Ninja
find_program(NINJA_PROGRAM ninja)
if(NINJA_PROGRAM)
  set(CMAKE_MAKE_PROGRAM "${NINJA_PROGRAM}")
  set(CMAKE_GENERATOR "Ninja")
endif()

find_program(CCACHE_PROGRAM ccache)
if(CCACHE_PROGRAM)
  set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE "${CCACHE_PROGRAM}")
  set_property(GLOBAL PROPERTY RULE_LAUNCH_LINK "${CCACHE_PROGRAM}")
endif()

if(TASK_COMPILER STREQUAL "MSVC")
  set(CMAKE_CXX_COMPILER "cl")
  set(CMAKE_C_COMPILER "cl")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
  set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE}")
  set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG}")
  set(CMAKE_CXX_FLAGS_MINSIZEREL "${CMAKE_CXX_FLAGS_MINSIZEREL}")
  set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "${CMAKE_CXX_FLAGS_RELWITHDEBINFO}")
elseif(TASK_COMPILER STREQUAL "Clang")
  set(CMAKE_CXX_COMPILER "clang++")
  set(CMAKE_C_COMPILER "clang")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
  set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE}")
  set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG}")
  set(CMAKE_CXX_FLAGS_MINSIZEREL "${CMAKE_CXX_FLAGS_MINSIZEREL}")
  set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "${CMAKE_CXX_FLAGS_RELWITHDEBINFO}")
elseif(TASK_COMPILER STREQUAL "GCC")
  set(CMAKE_CXX_COMPILER "g++")
  set(CMAKE_C_COMPILER "gcc")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
  set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE}")
  set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG}")
  set(CMAKE_CXX_FLAGS_MINSIZEREL "${CMAKE_CXX_FLAGS_MINSIZEREL}")
  set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "${CMAKE_CXX_FLAGS_RELWITHDEBINFO}")
elseif(TASK_COMPILER STREQUAL "Emscripten")
  set(CMAKE_CXX_COMPILER "em++")
  set(CMAKE_C_COMPILER "emcc")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
  set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE}")
  set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG}")
  set(CMAKE_CXX_FLAGS_MINSIZEREL "${CMAKE_CXX_FLAGS_MINSIZEREL}")
  set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "${CMAKE_CXX_FLAGS_RELWITHDEBINFO}")
elseif(TASK_COMPILER STREQUAL "MinGW")
  set(CMAKE_CXX_COMPILER "g++")
  set(CMAKE_C_COMPILER "gcc")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
  set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE}")
  set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG}")
  set(CMAKE_CXX_FLAGS_MINSIZEREL "${CMAKE_CXX_FLAGS_MINSIZEREL}")
  set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "${CMAKE_CXX_FLAGS_RELWITHDEBINFO}")
elseif(TASK_COMPILER STREQUAL "Intel")
  # rm .\CMakeCache.txt; rm -r .\CMakeFiles\; cmake ..; cmake --build .; .\Debug\main.exe
  set(CMAKE_CXX_COMPILER "icpx")
  set(CMAKE_C_COMPILER "icx")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
  set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE}")
  set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG}")
  set(CMAKE_CXX_FLAGS_MINSIZEREL "${CMAKE_CXX_FLAGS_MINSIZEREL}")
  set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "${CMAKE_CXX_FLAGS_RELWITHDEBINFO}")
elseif(TASK_COMPILER STREQUAL "Cling")
  set(CMAKE_CXX_COMPILER "cling")
  set(CMAKE_C_COMPILER "cling")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
  set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE}")
  set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG}")
  set(CMAKE_CXX_FLAGS_MINSIZEREL "${CMAKE_CXX_FLAGS_MINSIZEREL}")
  set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "${CMAKE_CXX_FLAGS_RELWITHDEBINFO}")
endif()

message(STATUS "")
message(STATUS "  Platform: ${CMAKE_SYSTEM_NAME} Architecture: ${CMAKE_SYSTEM_PROCESSOR}")
message(STATUS "  Compiler: ${CMAKE_CXX_COMPILER} standard: c++${CMAKE_CXX_STANDARD}")
message(STATUS "  Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "  Cache: ${CCACHE_PROGRAM}")
message(STATUS "  Install prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "  Generator: ${CMAKE_GENERATOR}")
message(STATUS "  C++ flags: ${CMAKE_CXX_FLAGS}")
message(STATUS "  C++ flags (release): ${CMAKE_CXX_FLAGS_RELEASE}")
message(STATUS "  C++ flags (debug): ${CMAKE_CXX_FLAGS_DEBUG}")
message(STATUS "  C++ flags (minsize): ${CMAKE_CXX_FLAGS_MINSIZEREL}")
message(STATUS "  C++ flags (reldeb): ${CMAKE_CXX_FLAGS_RELWITHDEBINFO}")
message(STATUS "")
