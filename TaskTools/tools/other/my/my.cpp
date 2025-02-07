#include "my.hpp"
namespace task{
    // ------------------------------------ [ Type Definitions ] --------------------------------
    struct My::Impl{ std::shared_ptr<SharedData> sharedData; };


    // ------------------------------------ [ Constructors ] ------------------------------------


    // ------------------------------------ [ Getters/Setters ] -----------------------------------


    // ------------------------------------ [ Methods ] ------------------------------------
    My& My::GetInstance(std::shared_ptr<SharedData> sharedData){ static My instance; instance.pImpl->sharedData = sharedData; return instance; }
}
