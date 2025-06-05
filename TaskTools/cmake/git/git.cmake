find_program(GIT_EXECUTABLE git)
if(GIT_EXECUTABLE AND CLANG_FORMAT_EXECUTABLE)
    execute_process(
        COMMAND ${GIT_EXECUTABLE} checkout -b dev
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        RESULT_VARIABLE GIT_SWITCH_RESULT
        OUTPUT_QUIET ERROR_QUIET
    )
    execute_process(
        COMMAND ${GIT_EXECUTABLE} init .
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        RESULT_VARIABLE GIT_INIT_RESULT
        OUTPUT_QUIET ERROR_QUIET
    )
    execute_process(
        COMMAND ${GIT_EXECUTABLE} add .
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        RESULT_VARIABLE GIT_ADD_RESULT
        OUTPUT_QUIET ERROR_QUIET
    )
    execute_process(
        COMMAND ${GIT_EXECUTABLE} commit -m "Auto-commit: Formatted code during CMake configuration"
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        RESULT_VARIABLE GIT_COMMIT_RESULT
        OUTPUT_QUIET ERROR_QUIET
    )
elseif(CLANG_FORMAT_EXECUTABLE)
    message(STATUS "Git not found. Skipping auto-commit.")
endif()