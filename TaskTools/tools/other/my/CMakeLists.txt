set(my_src
    my.cpp 
) 
set(my_hdr
    my.hpp
)

add_library(${PROJECT_NAME}_my STATIC ${my_src} ${my_hdr})
target_link_libraries(${PROJECT_NAME}_my PRIVATE libs_dependencies)

install(TARGETS ${PROJECT_NAME}_my DESTINATION lib)
install(FILES ${my_hdr} DESTINATION include/my)
