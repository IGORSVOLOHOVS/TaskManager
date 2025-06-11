find_program(CLANG_FORMAT_EXECUTABLE clang-format)
if(CLANG_FORMAT_EXECUTABLE)
    file(GLOB_RECURSE
        ALL_CXX_FILES
        RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}"
        "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp"
        "${CMAKE_CURRENT_SOURCE_DIR}/src/*.hpp"
        "${CMAKE_CURRENT_SOURCE_DIR}/tests/*.cpp"
        "${CMAKE_CURRENT_SOURCE_DIR}/include/*.hpp"
    )
    foreach(SOURCE_FILE ${ALL_CXX_FILES})
        execute_process(
            COMMAND ${CLANG_FORMAT_EXECUTABLE} -i ${SOURCE_FILE}
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        )
    endforeach()
    message(STATUS "Auto-formatting C/C++ files with clang-format.")
else()
    message(WARNING "clang-format not found. Skipping auto-formatting.")
endif()