%module task
%{
    #include "io.hpp"
%}

%include "std_string.i"
%include "std_vector.i"

%typemap(out, fragment="SWIG_From_std_string") std::string&& {
  $result = SWIG_From_std_string(*$1);
}
%typemap(in, fragment="SWIG_AsVal_std_string") std::string&& (std::string temp) {
  int res = SWIG_AsVal_std_string($input, &temp);
  $1 = &temp;
}
%typemap(out, fragment="SWIG_From_double") double&& {
  $result = SWIG_From_double(*$1);
}
%typemap(in, fragment="SWIG_AsVal_double") double&& (double temp) {
  int res = SWIG_AsVal_double($input, &temp);
  $1 = &temp;
}


%include "io.hpp"

%template(read_num) read<double>;
%template(read_str) read<std::string>;
%template(read_vec_l) readContainer<std::vector<double>>;
%template(read_vec_s) readContainer<std::vector<std::string>>;

%template(write_num) write<double>;
%template(write_str) write<std::string>;
%template(write_vec_l) writeContainer<std::vector<double>>;
%template(write_vec_s) writeContainer<std::vector<std::string>>;
