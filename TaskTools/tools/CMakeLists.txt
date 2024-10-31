cmake_minimum_required(VERSION 3.20)
project(tools C CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

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

add_library(tools STATIC ${sources} ${headers})
target_link_libraries(tools PUBLIC ws2_32)

