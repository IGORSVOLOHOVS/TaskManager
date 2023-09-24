#include "test.h"
// #include "emscripten/emscripten.h"

// extern "C" EMSCRIPTEN_KEEPALIVE
// int add(int a, int b) {
//   return a + b;
// }
//BENCHMARK_MAIN();

int main(){
    test::test_functions();
    test::test_classes();
    test::test_structs();

    return 0;
}