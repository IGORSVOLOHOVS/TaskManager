file(GLOB_RECURSE SOURCES "*.cpp" "*.cxx" "*.c")

add_library(${PROJECT_NAME} STATIC task.hpp ${SOURCES})
target_link_libraries(${PROJECT_NAME} PUBLIC libs)
target_include_directories(${PROJECT_NAME} PUBLIC .)

install(TARGETS ${PROJECT_NAME} DESTINATION ${CMAKE_INSTALL_PREFIX}/lib)
install(FILES task.hpp DESTINATION ${CMAKE_INSTALL_PREFIX}/include/task)
