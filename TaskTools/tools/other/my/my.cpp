#include "my.hpp"

// ------------------------------------ [ Type Definitions ] --------------------------------
std::string my::MY_GLOBAL_CONST = tools::Parser::Parse("MY_GLOBAL_CONST", "default_value");

// ------------------------------------ [ Constructors ] ------------------------------------
my::MyInit::MyInit() noexcept {}
my::MyInit::~MyInit() noexcept {}

bool operator<=>(const my::MyData& lhs, const my::MyData& rhs) noexcept { return true; }

my::My::My() noexcept: MyInit() {}
my::My::~My() noexcept {}

my::My::My(const My& obj) noexcept { my_d_ = obj.my_d_; }
my::My::My(My&& obj) noexcept { my_d_ = std::move(obj.my_d_); }
my::My& my::My::operator=(const My& obj) noexcept { my_d_ = obj.my_d_; return *this; }
my::My& my::My::operator=(My&& obj) noexcept { my_d_ = std::move(obj.my_d_); return *this; }

my::My::My(const MyData& data) noexcept: MyInit() { my_d_ = data; }
my::My::My(MyData&& data) noexcept: MyInit() { my_d_ = std::move(data); }
my::My& my::My::operator=(const MyData& data) noexcept { my_d_ = data; return *this; }
my::My& my::My::operator=(MyData&& data) noexcept { my_d_ = std::move(data); return *this; }



// ------------------------------------ [ Getters/Setters ] -----------------------------------
my::MyData          my::My::GetData() const noexcept { return my_d_; }
my::MyData&         my::My::GetDataRef() noexcept { return my_d_; }
const my::MyData&   my::My::GetDataRef() const noexcept { return my_d_; }

my::My&             my::My::SetData(const MyData& data) noexcept { my_d_ = data; return *this; }
my::My&             my::My::SetData(MyData&& data) noexcept { my_d_ = std::move(data); return *this; }



// ------------------------------------ [ Methods ] ------------------------------------
my::My::MyExp           my::My::DoSomething() noexcept { return {}; }