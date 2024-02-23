#pragma once
#include <iostream>
#include <fstream>
#include <string>

#include <yaml-cpp/yaml.h>

namespace config
{
    int VAL1 = 1;
    int VAL2 = 2;
    int VAL3 = 3;

    const char* DEFAULT_CONFIG_PATH = "config.yaml";
    void create(const std::string& path) {
        YAML::Emitter out;
        out << YAML::BeginMap;
        out << YAML::Key << "VAL1" << YAML::Value << VAL1;
        out << YAML::Key << "VAL2" << YAML::Value << VAL2;
        out << YAML::Key << "VAL3" << YAML::Value << VAL3;
        out << YAML::EndMap;

        std::ofstream outFile(path);
        outFile << out.c_str();

        std::cout << "File created at " << path << std::endl;
    }

    void parser(const std::string& path = DEFAULT_CONFIG_PATH) {
        // check if file exist
        std::ifstream file(path);
        if (!file.is_open()) {
            std::cout << "File not found, creating by default..." << std::endl;
            create(path);
        }else{
            std::cout << "File found, parsing..." << std::endl;
        }

        try {
            YAML::Node config = YAML::LoadFile(path);
            if (config["VAL1"]) {
                VAL1 = config["VAL1"].as<int>();
            }
            if (config["VAL2"]) {
                VAL2 = config["VAL2"].as<int>();
            }
            if (config["VAL3"]) {
                VAL3 = config["VAL3"].as<int>();
            }

            std::cout << "VAL1: " << VAL1 << " VAL2: " << VAL2 << " VAL3: " << VAL3 << std::endl;
            std::cout << "Parse complete." << std::endl;
        } catch (const YAML::Exception& e) {
            std::cerr << "Error: " << e.what() << "\n";
        }
    }

} // namespace config
