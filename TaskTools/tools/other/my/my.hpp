#pragma once

#include "interfaces.hpp"

namespace my{
    class MyInit{
    public:
        MyInit();
        ~MyInit();

        MyData  data_       =  {};
    };


    class My: private MyInit, public IMy
    {
    public:
        // ------------------------------------ [ Type Definitions ] --------------------------------
        using Void = std::expected<void, std::string>;

        // ------------------------------------ [ Constructors ] ------------------------------------
        My();
        ~My();

        // ------------------------------------ [ Getters/Setters ] -----------------------------------
        MyData          GetData() const override;
        MyData&         GetDataRef() override;
        const MyData&   GetDataRef() const override;

        My&             SetData(const MyData& data) override;
        My&             SetData(MyData&& data) override;



        // ------------------------------------ [ Methods ] ------------------------------------
        Void           DoSomething(DoSomethingParametrs settings) override;
    };
}

