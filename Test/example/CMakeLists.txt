function(add_example NAME)
  add_executable("${NAME}" "${NAME}.cpp")
  target_link_libraries("${NAME}" PRIVATE WaamAPI)
  target_compile_features("${NAME}" PRIVATE cxx_std_23)
endfunction()

add_example(empty_example)


