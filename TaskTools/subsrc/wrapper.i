%module task
%{
    #include "benchmark.hpp"
    #include "test.hpp"
    #include "config.hpp"
%}

%rename(runBenchmark) benchmark::run;
%rename(runTests) test::run;

%include "std_string.i"
%include "stdint.i"
%include "std_vector.i"
%include "std_map.i"
%include "std_pair.i"
%include "std_iostream.i"
%include "std_except.i"

%include "benchmark.hpp"
%include "test.hpp"
%include "config.hpp"
