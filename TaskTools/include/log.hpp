#pragma once

#include <iostream>
#include <format>
#include <vector>
#include <functional> 

#include <fstream>
#include <regex>

#include <chrono>

#include <future>

#define LOG_AVAILABLE 1

// parralel.hpp
#define AsyncFunction(n, rt)                                std::future<rt> n##_async(){return std::async(std::launch::async, [&]() { return n(); });}

#define AsyncFunction1(n, rt, at)                           std::future<rt> n##_async(at a){return std::async(std::launch::async, [&]() { return n(a); });}
#define AsyncFunction2(n, rt, at1, at2)                     std::future<rt> n##_async(at1 a1, at2 a2){return std::async(std::launch::async, [&]() { return n(a1, a2); });}
#define AsyncFunction3(n, rt, at1, at2, at3)                std::future<rt> n##_async(at1 a1, at2 a2, at3 a3){return std::async(std::launch::async, [&]() { return n(a1, a2, a3); });}
#define AsyncFunction4(n, rt, at1, at2, at3, at4)           std::future<rt> n##_async(at1 a1, at2 a2, at3 a3, at4 a4){return std::async(std::launch::async, [&]() { return n(a1, a2, a3, a4); });}
#define AsyncFunction5(n, rt, at1, at2, at3, at4, at5)      std::future<rt> n##_async(at1 a1, at2 a2, at3 a3, at4 a4, at5 a5){return std::async(std::launch::async, [&]() { return n(a1, a2, a3, a4, a5); });}

#define AsyncFunctionN(n, rt, ...)                          std::future<rt> n##_async(){return std::async(std::launch::async, [&]() { return n(__VA_ARGS__); });}


template <typename T> concept Argument = requires(T t){{std::cout << t};};
template <typename T> concept Container = requires(T t){{t.begin()};{t.end()};};


class Log
{
public:
    Log() = default;
    Log(int argc, char **argv)
    {
        int count = 0;
        for (int i = 1; i < argc; i++)
        {
            if (std::string(argv[i]) == "--version" || std::string(argv[i]) == "-v")
            {
                version();
                count++;
            }
            else if (std::string(argv[i]) == "--help" || std::string(argv[i]) == "-h")
            {
                help();
                count++;
            }
            else
            {
                throw std::invalid_argument("Invalid option: " + std::string(argv[i]));
            }
        }
    }

    void operator()(const std::string& message = "") {
        #if LOG_AVAILABLE
            auto end = std::chrono::system_clock::now();

            auto timeMs = std::chrono::time_point_cast<std::chrono::milliseconds>(end);
            auto sinceEpochMs = timeMs.time_since_epoch();
            std::time_t timeT = std::chrono::system_clock::to_time_t(end);
            std::tm timeTm;
            localtime_s(&timeTm, &timeT);

            auto durationNs = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);
            auto hours = std::chrono::duration_cast<std::chrono::hours>(durationNs);
            auto minutes = std::chrono::duration_cast<std::chrono::minutes>(durationNs - hours);
            auto seconds = std::chrono::duration_cast<std::chrono::seconds>(durationNs - hours - minutes);
            auto milliseconds = std::chrono::duration_cast<std::chrono::milliseconds>(durationNs - hours - minutes - seconds);
            auto microseconds = std::chrono::duration_cast<std::chrono::microseconds>(durationNs - hours - minutes - seconds - milliseconds);
            auto remainingNs = (durationNs - hours - minutes - seconds - milliseconds - microseconds).count();

            std::ostringstream oss;
            oss << "[ LOG " << std::setw(7) << id << " ] ["
                << std::put_time(&timeTm, "%H:%M:%S") << '.' << std::setw(3) << std::setfill('0') << sinceEpochMs.count() % 1000 << "ms - "
                << std::setw(3) << std::setfill(' ') << hours.count() << "h "
                << std::setw(3) << std::setfill(' ') << minutes.count() << "m "
                << std::setw(3) << std::setfill(' ') << seconds.count() << "s "
                << std::setw(3) << std::setfill(' ') << milliseconds.count() << "ms "
                << std::setw(3) << std::setfill(' ') << microseconds.count() << "us "
                << std::setw(3) << std::setfill(' ') << remainingNs << "ns] " 
                << message << '\n';
            std::cout << oss.str(); 

            id++;
            start = std::chrono::system_clock::now();
        #endif
    }

    // io.hpp
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
    template <Argument Argument = std::string> std::vector<Argument> read_n(const size_t n = 0,std::string&& msg = "{}/{}:", std::function<bool(Argument)> check = nullptr) {
        std::vector<Argument> c;
        size_t current = 0;
        for (size_t i = 0; i < n; i++) {
            c.push_back(read<Argument>(std::vformat(msg, std::make_format_args(++current, n)), check));
        }
        return c;
    }

    template <Argument... Argument> void write(std::string delimiter, Argument &&...args) {
        ((std::cout << args << delimiter), ...);
    }
    template <Container C = std::vector<std::string>> void write_n(const C &t, std::string delimiter) {
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

private:
    void version() const
    {
        std::cout << "Version 1.0.0\n";
    }
    void help() const
    {
        std::cout << "Usage: ./main [OPTION]...\n";
        std::cout << "Options:\n";
        std::cout << "  -h, --help\t\t\tDisplay this information\n";
        std::cout << "  -v, --version\t\t\tDisplay the version\n";
    }

    uint64_t id = 0;
    std::chrono::time_point<std::chrono::system_clock> start;
};
