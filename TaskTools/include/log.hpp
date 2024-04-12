#pragma once

#include <iostream>

class Log
{
public:
    explicit Log(int argc, char **argv)
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
};
