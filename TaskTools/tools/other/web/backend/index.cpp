#include "index.hpp"

#include <iostream>

// ------------------------------------ [ Type Definitions ] --------------------------------
std::string idx::INDEX_GLOBAL_CONST = "dasdsad";//tools::Parser::Parse("INDEX_GLOBAL_CONST", "default_value");

// ------------------------------------ [ Constructors ] ------------------------------------
idx::IndexInit::IndexInit() noexcept {}
idx::IndexInit::~IndexInit() noexcept {}

bool operator<=>(const idx::IndexData& lhs, const idx::IndexData& rhs) noexcept { return true; }

idx::Index::Index() noexcept: IndexInit() {}
idx::Index::~Index() noexcept {}

idx::Index::Index(const Index& obj) noexcept { idx_d_ = obj.idx_d_; }
idx::Index::Index(Index&& obj) noexcept { idx_d_ = std::move(obj.idx_d_); }
idx::Index& idx::Index::operator=(const Index& obj) noexcept { idx_d_ = obj.idx_d_; return *this; }
idx::Index& idx::Index::operator=(Index&& obj) noexcept { idx_d_ = std::move(obj.idx_d_); return *this; }

idx::Index::Index(const IndexData& data) noexcept: IndexInit() { idx_d_ = data; }
idx::Index::Index(IndexData&& data) noexcept: IndexInit() { idx_d_ = std::move(data); }
idx::Index& idx::Index::operator=(const IndexData& data) noexcept { idx_d_ = data; return *this; }
idx::Index& idx::Index::operator=(IndexData&& data) noexcept { idx_d_ = std::move(data); return *this; }



// ------------------------------------ [ Getters/Setters ] -----------------------------------
idx::IndexData          idx::Index::GetData() const noexcept { return idx_d_; }
idx::IndexData&         idx::Index::GetDataRef() noexcept { return idx_d_; }
const idx::IndexData&   idx::Index::GetDataRef() const noexcept { return idx_d_; }

idx::Index&             idx::Index::SetData(const IndexData& data) noexcept { idx_d_ = data; return *this; }
idx::Index&             idx::Index::SetData(IndexData&& data) noexcept { idx_d_ = std::move(data); return *this; }



// ------------------------------------ [ Methods ] ------------------------------------
void           idx::Index::DoSomething() { 
    std::cout << "DoSomething" << std::endl;
}