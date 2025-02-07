#pragma once

#include "../interfaces.hpp"

namespace task{
    class My
    {
        struct Impl; std::unique_ptr<Impl> pImpl;
        // ------------------------------------ [ Private Methods ] --------------------------------
    public:
        // ------------------------------------ [ Type Definitions ] --------------------------------


        // ------------------------------------ [ Constructors ] ------------------------------------


        // ------------------------------------ [ Getters/Setters ] -----------------------------------


        // ------------------------------------ [ Methods ] ------------------------------------
        static Abc& GetInstance(std::shared_ptr<SharedData> sharedData = nullptr);
    };
}
