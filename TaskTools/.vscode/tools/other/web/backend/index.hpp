#pragma once
#include <expected>
#include <string>

#include <emscripten/bind.h>

using namespace emscripten;

namespace idx{
    extern std::string INDEX_GLOBAL_CONST;

    struct IndexData{
        friend bool operator<=>(const IndexData& lhs, const IndexData& rhs) noexcept;
    };

    class IndexInit{
    public:
        IndexInit() noexcept;
        ~IndexInit() noexcept;

        IndexData  idx_d_       =  {};
    };

    class Index: private IndexInit
    {
    public:
        // ------------------------------------ [ Type Definitions ] --------------------------------
        using IndexExp = std::expected<void, std::string>;



        // ------------------------------------ [ Constructors ] ------------------------------------
        Index() noexcept;
        ~Index() noexcept;

        Index(const Index& obj) noexcept;
        Index(Index&& obj) noexcept;
        Index& operator=(const Index& obj) noexcept;
        Index& operator=(Index&& obj) noexcept;

        Index(const IndexData& data) noexcept;
        Index(IndexData&& data) noexcept;
        Index& operator=(const IndexData& data) noexcept;
        Index& operator=(IndexData&& data) noexcept;



        // ------------------------------------ [ Getters/Setters ] -----------------------------------
        IndexData          GetData() const noexcept;
        IndexData&         GetDataRef() noexcept;
        const IndexData&   GetDataRef() const noexcept;

        Index&             SetData(const IndexData& data) noexcept;
        Index&             SetData(IndexData&& data) noexcept;



        // ------------------------------------ [ Methods ] ------------------------------------
        void           DoSomething();
    };
}

// ------------------------------------ [ Emscripten Bindings ] ------------------------------------
EMSCRIPTEN_BINDINGS(Index){
    class_<idx::Index>("Index")
        .constructor<>()
        .function("DoSomething", &idx::Index::DoSomething)
        ;
}