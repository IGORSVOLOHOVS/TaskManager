#pragma once

#include <expected>
#include <string>

#include "../task/task.hpp"

namespace my{
    extern std::string MY_GLOBAL_CONST;

    struct MyData{
        friend bool operator<=>(const MyData& lhs, const MyData& rhs) noexcept;
    };

    class MyInit{
    public:
        MyInit() noexcept;
        ~MyInit() noexcept;

        MyData  my_d_       =  {};
    };

    class My: private MyInit
    {
    public:
        // ------------------------------------ [ Type Definitions ] --------------------------------
        using MyExp = std::expected<void, std::string>;



        // ------------------------------------ [ Constructors ] ------------------------------------
        My() noexcept;
        ~My() noexcept;

        My(const My& obj) noexcept;
        My(My&& obj) noexcept;
        My& operator=(const My& obj) noexcept;
        My& operator=(My&& obj) noexcept;

        My(const MyData& data) noexcept;
        My(MyData&& data) noexcept;
        My& operator=(const MyData& data) noexcept;
        My& operator=(MyData&& data) noexcept;



        // ------------------------------------ [ Getters/Setters ] -----------------------------------
        MyData          GetData() const noexcept;
        MyData&         GetDataRef() noexcept;
        const MyData&   GetDataRef() const noexcept;

        My&             SetData(const MyData& data) noexcept;
        My&             SetData(MyData&& data) noexcept;



        // ------------------------------------ [ Methods ] ------------------------------------
        MyExp           DoSomething() noexcept;
    };
}

