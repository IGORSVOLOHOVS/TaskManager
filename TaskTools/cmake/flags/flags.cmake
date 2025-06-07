if(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    # Common flags for all build types
    # add_compile_options(-Wall -Wextra -Wpedantic -Wmacro-redefined)

    # Устанавливаем стандартные типы сборок
    set(CMAKE_CXX_FLAGS_DEBUG "-g -O0 -fno-omit-frame-pointer")
    set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG -march=native -pipe") # Убрал -ffast-math как базовый
    set(CMAKE_EXE_LINKER_FLAGS_RELEASE "-flto")
endif()

# --- Опции для включения дополнительного функционала ---
option(ENABLE_SANITIZERS "Enable Address and Undefined Behavior sanitizers (Debug only)" OFF)
option(ENABLE_COVERAGE "Enable code coverage instrumentation (Debug only)" ON)


if(ENABLE_SANITIZERS AND ENABLE_COVERAGE)
    message(FATAL_ERROR "Sanitizers and Code Coverage cannot be enabled at the same time.")
endif()

if(ENABLE_SANITIZERS)
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -fsanitize=address,undefined")
endif()

# Логика для покрытия кода
if(ENABLE_COVERAGE)
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -fprofile-instr-generate -fcoverage-mapping")
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
