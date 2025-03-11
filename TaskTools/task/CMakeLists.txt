file(GLOB_RECURSE SOURCES "*.cpp" "*.cxx" "*.c")
file(GLOB_RECURSE HEADERS "*.hpp" "*.hxx" "*.h")

add_library(${PROJECT_NAME} STATIC ${HEADERS} ${SOURCES})
target_link_libraries(${PROJECT_NAME} PUBLIC libs)
target_include_directories(${PROJECT_NAME} PUBLIC .)

install(TARGETS ${PROJECT_NAME} DESTINATION ${CMAKE_INSTALL_PREFIX}/lib)
install(FILES ${HEADERS} DESTINATION ${CMAKE_INSTALL_PREFIX}/include/task)
