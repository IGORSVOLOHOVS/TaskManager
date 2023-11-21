// config.ixx
module;

#include <yaml-cpp/yaml.h>
#include <iostream>
#include <fstream>
#include <string>

export module config.config;

namespace config
{
    export int VAL1;
    export int VAL2;
    export int VAL3;

    void create(const std::string& path) {
        std::ifstream file(path);
        if (!file) {
            // Файл не существует, создаем новый
            YAML::Emitter out;
            out << YAML::BeginMap;
            out << YAML::Key << "VAL1" << YAML::Value << VAL1;
            out << YAML::Key << "VAL2" << YAML::Value << VAL2;
            out << YAML::Key << "VAL3" << YAML::Value << VAL3;
            out << YAML::EndMap;

            std::ofstream outFile(path);
            outFile << out.c_str();
        }
    }

    export void parser(const std::string& path) {
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
        } catch (const YAML::Exception& e) {
            std::cerr << "Ошибка при чтении YAML файла: " << e.what() << "\nСоздание нового файла...\n";
            create(path);  // Вызываем функцию create для создания файла
        }
    }

} // namespace config


