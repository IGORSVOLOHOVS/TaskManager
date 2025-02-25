add_executable(backend index.cpp index.hpp)
target_link_options(backend PRIVATE "SHELL: -s MODULARIZE=1 -s DEMANGLE_SUPPORT=1 --bind")
