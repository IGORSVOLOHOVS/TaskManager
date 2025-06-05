if(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    # Common flags for all build types
    add_compile_options(-Wall -Wextra -Wpedantic -Wmacro-redefined)

    # Debug flags
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -fsanitize=address,undefined -fno-omit-frame-pointer")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -O3 -DNDEBUG -march=native -flto")
    
    set(CMAKE_EXE_LINKER_FLAGS "-flto")
endif()

message(STATUS "------------------------------------------")
message(STATUS "  Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "  Compiler Path: ${CMAKE_CXX_COMPILER}")
message(STATUS "  Global CXX Flags: [ ${CMAKE_CXX_FLAGS} ]")
message(STATUS "  Debug CXX Flags: [ ${CMAKE_CXX_FLAGS_DEBUG} ]")
message(STATUS "  Release CXX Flags: [ ${CMAKE_CXX_FLAGS_RELEASE} ]")
# message(STATUS "  RelWithDebInfo CXX Flags: [ ${CMAKE_CXX_FLAGS_RELWITHDEBINFO} ]")
# message(STATUS "  MinSizeRel CXX Flags: [ ${CMAKE_CXX_FLAGS_MINSIZEREL} ]")
# message(STATUS "  Executable Linker Flags: [ ${CMAKE_EXE_LINKER_FLAGS} ]")
# message(STATUS "  Shared Library Linker Flags: [ ${CMAKE_SHARED_LINKER_FLAGS} ]")
# message(STATUS "  Module Linker Flags: [ ${CMAKE_MODULE_LINKER_FLAGS} ]")
message(STATUS "------------------------------------------")
