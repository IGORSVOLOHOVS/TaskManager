/* File: WaamAPI.i */
%module TaskAPI

%feature("autodoc", "3");

%{
%}

%include <typemaps.i>
%include <std_string.i>
%include <std_vector.i>
%include <std_array.i>
%include <std_map.i>
%include <std_iostream.i>
%include <std_shared_ptr.i>
%include <std_unique_ptr.i>
%include <stdint.i>
%include <std_deque.i>
%include <std_except.i> 

%template(StringVector) std::vector<std::string>;



