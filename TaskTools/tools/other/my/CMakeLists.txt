set(my_src
    my.cpp 
) 
set(my_hdr
    my.hpp
    
    structures.hpp
    interfaces.hpp 
)

add_library(${PROJECT_NAME}_my STATIC ${my_src} ${my_hdr})
target_precompile_headers(${PROJECT_NAME}_my PRIVATE ../pch.hpp)
target_include_directories(${PROJECT_NAME}_my PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/..)

install(TARGETS ${PROJECT_NAME}_my DESTINATION lib)
install(FILES ${my_hdr} DESTINATION include/my)
