#pragma once

#include "../interfaces.hpp"

namespace task{
    class My: public IMy
    {
        struct Impl; std::unique_ptr<Impl> pImpl;
        // ------------------------------------ [ Private Methods ] --------------------------------
    public:
        // ------------------------------------ [ Type Definitions ] --------------------------------


        // ------------------------------------ [ Constructors ] ------------------------------------


        // ------------------------------------ [ Getters/Setters ] -----------------------------------


        // ------------------------------------ [ Methods ] ------------------------------------
        static My& GetInstance(std::shared_ptr<SharedData> sharedData = nullptr, std::shared_ptr<Interfaces> interfaces = nullptr);
    };
}
