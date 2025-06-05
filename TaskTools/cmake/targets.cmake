find_package(Git QUIET)
find_package(Doxygen QUIET)

set(GIT_TARGET_REPO_NAME "Task" CACHE STRING "Имя для создаваемого/настраиваемого репозитория")
set(GIT_TARGET_REMOTE_URL "git@github.com:IGORSVOLOHOVS/${GIT_TARGET_REPO_NAME}.git" CACHE STRING "URL удаленного репозитория")

add_custom_target(git_remote
    COMMAND "${GIT_EXECUTABLE}" init
    COMMAND "${GIT_EXECUTABLE}" remote show origin > /dev/null 2>&1 || "${GIT_EXECUTABLE}" remote add origin "${GIT_TARGET_REMOTE_URL}"
    WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}"
    VERBATIM
)

add_custom_target(git_push
    COMMAND "${GIT_EXECUTABLE}" push
    WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}"
    VERBATIM
)

if(NOT CPACK_PACKAGE_NAME AND PROJECT_NAME)
    set(CPACK_PACKAGE_NAME "${PROJECT_NAME}")
endif()
if(NOT CPACK_PACKAGE_VERSION AND PROJECT_VERSION)
    set(CPACK_PACKAGE_VERSION "${PROJECT_VERSION}")
elseif(NOT CPACK_PACKAGE_VERSION)
    set(CPACK_PACKAGE_VERSION "0.1.0")
endif()
set(CPACK_GENERATOR "ZIP")

include(CPack)

set(CPACK_ARCHIVE_BASENAME "${CPACK_PACKAGE_NAME}-${CPACK_PACKAGE_VERSION}")
set(CPACK_ARCHIVE_EXTENSION ".zip")
set(CPACK_ARCHIVE_FULLNAME "${CMAKE_CURRENT_BINARY_DIR}/${CPACK_ARCHIVE_BASENAME}${CPACK_ARCHIVE_EXTENSION}")

add_custom_command(
    OUTPUT "${CPACK_ARCHIVE_FULLNAME}"
    COMMAND "${CMAKE_CPACK_COMMAND}" -G ZIP
    WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
    VERBATIM
)

add_custom_target(cpack_do_package
    DEPENDS "${CPACK_ARCHIVE_FULLNAME}"
    VERBATIM
)

set(RELEASE_TAG "v${CPACK_PACKAGE_VERSION}" CACHE STRING "Тег для релиза (например, v1.0.0)")

add_custom_target(git_release
    DEPENDS cpack_do_package
    COMMAND "${GIT_EXECUTABLE}" tag -f -a "${RELEASE_TAG}" -m "Release ${RELEASE_TAG}"
    COMMAND "${GIT_EXECUTABLE}" push origin "${RELEASE_TAG}" --force
    COMMAND gh release create "${RELEASE_TAG}" "${CPACK_ARCHIVE_FULLNAME}" --title "Release ${RELEASE_TAG}" --notes "Automated release for version ${RELEASE_TAG}." --repo IGORSVOLOHOVS/${GIT_TARGET_REPO_NAME}
    WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}"
    VERBATIM
)

add_custom_target(doxygen
    COMMAND "${DOXYGEN_EXECUTABLE}" Doxyfile
    WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}"
    VERBATIM
)

add_custom_target(clean_it
    COMMAND "${CMAKE_COMMAND}" --build "${CMAKE_CURRENT_BINARY_DIR}" --target clean
    WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
    VERBATIM
)