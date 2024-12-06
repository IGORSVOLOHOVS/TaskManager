#pragma once

#include "../pch.hpp"

namespace my{
    extern std::string MY_GLOBAL_CONST;

    struct MyData{
        bool operator<=>(const MyData& other);
    };

    struct DoSomethingParametrs{
    };
}