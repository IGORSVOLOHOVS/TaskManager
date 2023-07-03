// Copy A Directory?
#include <iostream>
#include <string>
#include <fstream>
#include <filesystem>
//#include <regex>
#include <windows.h>           // for windows

using namespace std;

const std::string DIR_NAME = "../Task";
const std::string TASK_TOOLS_PATH = "TaskTools/";
const std::string COUNTER_PATH = "../ManagerCounter.txt";

std::string counter = "";
//std::regex REGEX_COUNTER("Task([0-9]+)");

//std::smatch m;

int GetTaskNumber(const std::string& folder_name){
    return std::stoi(folder_name.substr(4,std::string::npos));
}

int PathCreatingCounterWithoutFile(){
    // iterate by all folders names in current folder
    int counter = 0;
    for (const auto& folder : std::filesystem::directory_iterator(".")) {
        if(folder.path().string().find_first_of("Task") == 0){
             // counter up by 1
            counter++;

            // find digit in the folder name Task1
            if (counter != GetTaskNumber(folder.path().string())){
                return counter;
            }
        }     
    }

    return 1;
}

int PathCreatingCounterWithFile(){
    int counter = 0;
    std::ifstream counter_file(COUNTER_PATH, ios::binary);

    if(counter_file.is_open()){
       counter_file >> counter;
       counter_file.close();

       std::cout << "Old counter is: " << counter << std::endl;

       std::fstream counter_file_repen(COUNTER_PATH,ios::out | ios::trunc | ios::binary);
       if(counter_file_repen.is_open()){      
            std::cout << "New counter is: " << ++counter << std::endl;    

            counter_file_repen << counter;
            counter_file_repen.close();

            std::cout << "New counter was added!" << std::endl;
       }
       else{
            std::cerr << "In " << COUNTER_PATH << "reopen ----> ERROR!" << std::endl;
            throw;
        }
    }
    else{
        std::cerr << "In " << COUNTER_PATH << "open ----> ERROR!" << std::endl;
        throw;
    }

    return counter;
}

int main(int argc, char* argv[]){
    const std::string full_dir_name = DIR_NAME + std::to_string(PathCreatingCounterWithoutFile());

    filesystem::create_directory(full_dir_name);
    filesystem::copy(TASK_TOOLS_PATH, full_dir_name, std::filesystem::copy_options::recursive);

    std::cout << "All is OK!" << std::endl;

    Sleep(1000);

    return 0;
}
// open in C:\Users\Admin\Desktop\TaskManager\ManagerProject\build\Debug>
// cd .. && cmake .. && cmake --build . 