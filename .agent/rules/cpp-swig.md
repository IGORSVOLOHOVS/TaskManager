**Role:** Act as a Senior C++ Interop Developer and SWIG Expert.
**Task:** Generate a professional-grade SWIG interface file (`.i`) to wrap the provided C++ code for **[INSERT TARGET LANGUAGE HERE, e.g., Python/Java/C#]**.
**Input C++ Code:**
```cpp
[INSERT YOUR C++ HEADER OR CODE HERE]
```

**Requirements & Best Practices:**
1. **Module Definition:** Use `%module(directors="1") module_name` if cross-language polymorphism (overriding virtual functions in the target language) is likely needed.
2. **Standard Library Support:** Explicitly include and instantiate necessary STL typemaps (e.g., `%include "std_string.i"`, `%include "std_vector.i"`). Ensure `std::string` maps to the target language's native string type and `std::vector` maps to a native list/array.
3. **Exception Handling:** Use `%exception` to catch standard C++ exceptions (`std::exception`) and rethrow them as native errors in the target language.
4. **C++23 `std::expected` Support:** SWIG does not natively support `std::expected`. You MUST create custom `%typemap(out)` rules to check `.has_value()`. If false, throw a target language exception (e.g., `PyExc_RuntimeError` in Python) with the error message. If true, return the value.
5. **Smart Pointers:** If the code uses `std::shared_ptr` or `std::unique_ptr`, use `%include "std_shared_ptr.i"` (or equivalent) and declare the template specializations strictly.
6. **Memory Management:** Ensure ownership is clear. Use `%newobject` if a function returns a pointer that the target language should own and garbage collect.
7. **Code Style & Documentation:**
* Enable Doxygen translation (`%include "doxygen.i"` or `-doxygen` flag usage notes) so C++ comments appear in the target language IDEs.
* Keep the `.i` file clean. Use `%{ #include "..." %}` blocks for necessary C++ headers.

**CMake Best Practices for SWIG:**
* **Header-Only Libraries:** If your core C++ logic is header-only, define it as an `INTERFACE` library in CMake (`add_library(core INTERFACE)`). This prevents linker errors when SWIG tries to link against it.
* **Finding Python:** Use `find_package(Python3 COMPONENTS Interpreter Development REQUIRED)` and explicitly include `${Python3_INCLUDE_DIRS}`.
* **C++ Property:** Set `set_property(SOURCE my_interface.i PROPERTY CPLUSPLUS ON)`.
* **Linking:** Link the SWIG module target against both the C++ logic library (e.g., `core`) and Python (`Python3::Python`).

**Output:**
* The complete `example.i` file content.
* A snippet of the `CMakeLists.txt` configuration required to build the module.
