#include "parser.hpp"


namespace tools {
    std::string Parser::Parse(const std::string& key, std::string default_value)
    {
        static std::fstream yaml; // Initialize yaml here
        yaml.open("config.yaml", std::ios::in); 
        if (!yaml.is_open()) 
        {
            // If file doesn't exist, create it (empty)
            std::ofstream outFile("config.yaml");
            outFile.close(); 
            yaml.open("config.yaml", std::ios::in); // Re-open in input mode
        }

        std::string line;
        bool wasKeyFound = false;
        while (std::getline(yaml, line)) 
        {
            // Check if the key is present at the beginning of the line (to avoid partial matches)
            if (line.find(key + ":") == 0)  
            {
                wasKeyFound = true;
                yaml.close(); 
                // Extract the value after the colon and any leading/trailing whitespace
                size_t colonPos = line.find(":");
                std::string value = line.substr(colonPos + 1);
                value.erase(0, value.find_first_not_of(" \t")); // Remove leading whitespace
                value.erase(value.find_last_not_of(" \t") + 1); // Remove trailing whitespace

                return value;
            }
        }
        if (!wasKeyFound)
        {
            yaml.close(); 
            Save(key, default_value); // Save the default value for the key
            return default_value;
        }

        return "";
    }

    void Parser::Save(const std::string& key, const std::string& value) 
    {
        static std::fstream yaml; // Initialize yaml here
        // Temporary file to store the modified content
        const std::string tempFileName = "config.yaml.tmp"; 

        yaml.open("config.yaml", std::ios::in);
        if (!yaml.is_open()) 
        {
            // If the file doesn't exist, create it with the new key-value pair
            std::ofstream outFile("config.yaml");
            outFile << key << ": " << value << "\n";
            outFile.close();
            return; // No need to read and modify further
        }

        std::ofstream tempFile(tempFileName);
        std::string line;
        bool keyFound = false;
        while (std::getline(yaml, line)) 
        {
            if (line.find(key + ":") == 0) 
            {
                tempFile << key << ": " << value << "\n";
                keyFound = true;
            }
            else 
            {
                tempFile << line << "\n";
            }
        }

        if (!keyFound) 
        {
            // If the key wasn't found, append it at the end
            tempFile << key << ": " << value << "\n";
        }

        yaml.close();
        tempFile.close();

        // Replace the original file with the modified one
        std::remove("config.yaml");        
        std::rename(tempFileName.c_str(), "config.yaml"); 
    }
} 
