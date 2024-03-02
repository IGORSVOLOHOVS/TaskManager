#pragma once
#include <iostream>
#include <fstream>
#include <string>

#include <yaml-cpp/yaml.h>

YAML::Node ARG;

bool RUNTEST1 = false;
bool RUNTEST2 = false;

namespace config
{
    const char* DEFAULT_CONFIG_PATH = "./test.yaml";
    void parser()
    {
        try
        {
            std::ifstream file(DEFAULT_CONFIG_PATH);
            if (!file.is_open())
            {
                throw std::runtime_error("File not found: " + std::string(DEFAULT_CONFIG_PATH));
            }

            YAML::Node config = YAML::LoadFile(DEFAULT_CONFIG_PATH);
            ARG = config["arguments"];

            RUNTEST1 = config["tests"]["test1"].as<bool>();
            RUNTEST2 = config["tests"]["test2"].as<bool>();

            std::cout << "Parsed config file: " << DEFAULT_CONFIG_PATH << "\n";
        }
        catch (const YAML::Exception &e)
        {
            std::cerr << "Error: " << e.what() << "\n";
        }
    }

} // namespace config
