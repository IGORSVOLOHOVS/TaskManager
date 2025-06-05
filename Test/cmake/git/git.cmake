find_program(GIT_EXECUTABLE git)
if(GIT_EXECUTABLE AND CLANG_FORMAT_EXECUTABLE)
    execute_process(
        COMMAND ${GIT_EXECUTABLE} add .
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        RESULT_VARIABLE GIT_ADD_RESULT
        OUTPUT_QUIET ERROR_QUIET
    )
    if(GIT_ADD_RESULT EQUAL 0)
        execute_process(
            COMMAND ${GIT_EXECUTABLE} commit -m "Auto-commit: Formatted code during CMake configuration"
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
            RESULT_VARIABLE GIT_COMMIT_RESULT
            OUTPUT_QUIET ERROR_QUIET
        )
        if(GIT_COMMIT_RESULT EQUAL 0)
            message(STATUS "Auto-committed formatted files.")
        elseif(NOT GIT_COMMIT_RESULT MATCHES "nothing to commit")
                message(WARNING "Git commit failed. Result: ${GIT_COMMIT_RESULT}")
        else()
                message(STATUS "No changes to commit after formatting.")
        endif()
    else()
        message(WARNING "Git add failed. Skipping auto-commit. Result: ${GIT_ADD_RESULT}")
    endif()
elseif(CLANG_FORMAT_EXECUTABLE)
    message(STATUS "Git not found. Skipping auto-commit.")
endif()