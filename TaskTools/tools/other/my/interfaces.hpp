#pragma once

#include "structures.hpp"

namespace my{
    class IMy {
    public:
        virtual ~IMy() = default;

        // ------------------------------------ [ Type Definitions ] --------------------------------
        using Void = std::expected<void, std::string>;

        // ------------------------------------ [ Getters/Setters ] -----------------------------------
        virtual MyData          GetData() const = 0;
        virtual MyData&         GetDataRef() = 0;
        virtual const MyData&   GetDataRef() const = 0;

        virtual IMy&             SetData(const MyData& data) = 0;
        virtual IMy&             SetData(MyData&& data) = 0;

        // ------------------------------------ [ Methods ] ------------------------------------
        virtual Void           DoSomething(DoSomethingParametrs settings) = 0;
    };
}