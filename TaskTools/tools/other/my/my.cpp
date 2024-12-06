#include "my.hpp"

// ------------------------------------ [ Type Definitions ] --------------------------------
std::string my::MY_GLOBAL_CONST = "";

// ------------------------------------ [ Constructors ] ------------------------------------
my::MyInit::MyInit() {}
my::MyInit::~MyInit() {}

bool my::MyData::operator<=>(const my::MyData& other) { return true; }

my::My::My(): MyInit(), IMy() {}
my::My::~My() {}


// ------------------------------------ [ Getters/Setters ] -----------------------------------
my::MyData          my::My::GetData() const  { return data_; }
my::MyData&         my::My::GetDataRef()  { return data_; }
const my::MyData&   my::My::GetDataRef() const  { return data_; }

my::My&             my::My::SetData(const MyData& data)  { data_ = data; return *this; }
my::My&             my::My::SetData(MyData&& data)  { data_ = std::move(data); return *this; }



// ------------------------------------ [ Methods ] ------------------------------------
my::My::Void           my::My::DoSomething(DoSomethingParametrs settings) { return {}; }