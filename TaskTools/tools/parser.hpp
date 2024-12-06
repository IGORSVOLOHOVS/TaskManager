#pragma once

#include "../task.hpp"

namespace tools
{
    class Parser
    {
    public:
        static std::string Parse(const std::string& key, std::string default_value = "");
        static void Save(const std::string& key, const std::string& value);
    };
}
