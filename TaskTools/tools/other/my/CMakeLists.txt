cmake_minimum_required(VERSION 3.20)
project(my C CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(my_src
    my.cpp 
) 
set(my_hdr
    my.hpp 
)

add_library(my STATIC ${my_src} ${my_hdr})
target_link_libraries(my tools)