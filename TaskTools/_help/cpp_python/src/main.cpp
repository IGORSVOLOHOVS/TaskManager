#include <custom_include.hpp>

#include <pybind11/pybind11.h>

#if PY_VERSION_HEX < 0x03000000
#define MyPyText_AsString PyString_AsString
#else
#define MyPyText_AsString PyUnicode_AsUTF8
#endif

namespace py = pybind11;

void run_test(py::object pyargv11) {
    int argc = 0;
    std::unique_ptr<char*[]> argv;

    // convert input list to C/C++ argc/argv
    PyObject* pyargv = pyargv11.ptr();
    if (PySequence_Check(pyargv)) {
        Py_ssize_t sz = PySequence_Size(pyargv);
        argc = (int)sz;
        argv = std::unique_ptr<char*[]>{new char*[sz]};
        for (Py_ssize_t i = 0; i < sz; ++i) {
            PyObject* item = PySequence_GetItem(pyargv, i);
            argv[i] = (char*)MyPyText_AsString(item);
            Py_DECREF(item);
            if (!argv[i] || PyErr_Occurred()) {
                argv = nullptr;
                break;
            }
        }
    }

    // bail if failed to convert
    if (!argv) {
        std::cerr << "argument is not a sequence of strings" << std::endl;
        return;
    }

    // call the closed function with the proper types
    test::run(argc, argv.get());
}

void run_benchmark(py::object pyargv11) {
    int argc = 0;
    std::unique_ptr<char*[]> argv;

    // convert input list to C/C++ argc/argv
    PyObject* pyargv = pyargv11.ptr();
    if (PySequence_Check(pyargv)) {
        Py_ssize_t sz = PySequence_Size(pyargv);
        argc = (int)sz;
        argv = std::unique_ptr<char*[]>{new char*[sz]};
        for (Py_ssize_t i = 0; i < sz; ++i) {
            PyObject* item = PySequence_GetItem(pyargv, i);
            argv[i] = (char*)MyPyText_AsString(item);
            Py_DECREF(item);
            if (!argv[i] || PyErr_Occurred()) {
                argv = nullptr;
                break;
            }
        }
    }

    // bail if failed to convert
    if (!argv) {
        std::cerr << "argument is not a sequence of strings" << std::endl;
        return;
    }

    // call the closed function with the proper types
    benchmark::run(argc, argv.get());
}

PYBIND11_MODULE(pytask, m) {
    m.doc() = "pybind11 benchmark plugin"; // optional module docstring

    m.def("run_benchmark", &run_benchmark, "A function which runs benchmark");


    m.def("run_test", &run_test, "A function which runs test");


    m.def("create", &config::create, "A function which creates config");
    m.def("parser", &config::parser, "A function which parses config");
}



