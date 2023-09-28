#include <iostream>

int main(){
    std::cout << "Hello world!" << std::endl;
    return 0;
}
// -----------------------------------------------------BENCHMARK--------------------------------

// #include "test.h"

// BENCHMARK_MAIN();
// int main(){
//     return 0;
// }

// -----------------------------------------------------TEST--------------------------------


// #include "test.h"

// int main(){
//     test::test_functions();
//     test::test_classes();
//     test::test_structs();

//     return 0;
// }



// -----------------------------------------------------EMSCRIPTEN функция--------------------------------



// #include "emscripten/emscripten.h"

// extern "C" EMSCRIPTEN_KEEPALIVE
// int add(int a, int b) {
//   return a + b;
// };



// -----------------------------------------------------EMSCRIPTEN класс--------------------------------
// #include <emscripten/bind.h>
// #include <sqlite3.h>
// #include <string>

// using namespace emscripten;

// class SQLiteWrapper {
// public:
//     SQLiteWrapper() {
//         sqlite3_open(":memory:", &db);
//         const char *sql = "CREATE TABLE fields (id INT, value TEXT);";
//         sqlite3_exec(db, sql, 0, 0, 0);
//     }

//     void saveData(std::string value) {
//         std::string sql = "INSERT INTO fields (id, value) VALUES (" + std::to_string(id++) + ", '" + value + "');";
//         sqlite3_exec(db, sql.c_str(), 0, 0, 0);
//     }

//     std::string getLastData(){
//         std::string sql = "SELECT value FROM fields WHERE id = " + std::to_string(id - 1) + ";";
//         sqlite3_stmt *stmt;
//         sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, NULL);
//         sqlite3_step(stmt);
//         std::string value = std::string((char *)sqlite3_column_text(stmt, 0));
//         sqlite3_finalize(stmt);
//         return value;
//     }

// private:
//     static int id; 
//     sqlite3 *db;
// };

// // Define the static member variable here
// int SQLiteWrapper::id = 0;

// EMSCRIPTEN_BINDINGS(SQLiteWrapper_module) {
//     class_<SQLiteWrapper>("SQLiteWrapper")
//         .constructor<>()
//         .function("saveData", &SQLiteWrapper::saveData)
//         .function("getLastData", &SQLiteWrapper::getLastData, allow_raw_pointers());
// }
