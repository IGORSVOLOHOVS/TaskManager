#include <iostream>
#include <format>
#include <vector>
#include <functional> 

#include <fstream>
#include <regex>

template <typename T> concept Argument = requires(T t){{std::cout << t};};
template <typename T> concept Container = requires(T t){{t.begin()};{t.end()};};

template <Argument Argument = std::string> Argument read(std::string&& msg = "Enter a value: ", std::function<bool(Argument)> check = nullptr) {
    Argument x;
    while (true)
    {
        std::cout<<msg;
        std::cin>>x;
        if(std::cin.fail()){
            std::cin.clear();
            std::cin.ignore(1000, '\n');
            std::cout<<"Invalid input: The input must be of type " <<typeid(Argument).name()<<"\n";
        }else if(check && !check(x)){
            std::cout<<"Invalid input: The input must satisfy the condition\n";
        }else{
            return x;
        }
    }
    throw std::runtime_error("Unreachable code");    
}
template <Argument Argument = std::string> std::vector<Argument> read(const size_t n = 0,std::string&& msg = "{}/{}:", std::function<bool(Argument)> check = nullptr) {
    std::vector<Argument> c;
    for (size_t i = 0; i < n; i++) {
        c.push_back(read<Argument>(std::vformat(msg, std::make_format_args(i + 1, n)), check));
    }
    return c;
}

template <Argument... Argument> void write(std::string delimiter, Argument &&...args) {
    ((std::cout << args << delimiter), ...);
}
template <Container C = std::vector<std::string>> void write(const C &t, std::string delimiter) {
    for (const auto &e : t) {
        write(delimiter, e);
    }
    write("\n");
}

void replace(const std::string& where, const std::regex& what, const std::string& on) {
    std::ifstream f_in(where);
    std::ofstream f_out(where + ".replaced");
    
    std::string line;
    std::string new_line; 
    while (std::getline(f_in, line)) {
        new_line = std::regex_replace(line, what, on);
        f_out << new_line << std::endl;
    }
    
    f_in.close();
    f_out.close();
}

std::vector<std::string> grep(const std::string& where, const std::regex& what) {
    std::ifstream f_in(where);
    std::vector<std::string> result;
    
    std::string line;
    while (std::getline(f_in, line)) {
        if (std::regex_search(line, what)) {
            result.push_back(line);
        }
    }
    
    f_in.close();
    return result;
}
