set(sources 
    time.cpp 
    logger.cpp 
    parser.cpp
) 
set(headers 
    time.hpp 
    logger.hpp 
    parser.hpp
    thread_pool.h

    tools.hpp
)

add_library(${PROJECT_NAME}_tools STATIC ${sources} ${headers})
target_link_libraries(${PROJECT_NAME}_tools PUBLIC ws2_32)

