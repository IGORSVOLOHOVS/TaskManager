cmake_minimum_required(VERSION 3.20)

project(Task LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_INSTALL_PREFIX ${CMAKE_CURRENT_SOURCE_DIR})

add_subdirectory(backend)


# copy backend files
install(TARGETS backend
        RUNTIME DESTINATION web
        LIBRARY DESTINATION web
        ARCHIVE DESTINATION web)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/backend/backend.wasm DESTINATION web)

# copy frontend files
install(FILES frontend/index.html DESTINATION web)

