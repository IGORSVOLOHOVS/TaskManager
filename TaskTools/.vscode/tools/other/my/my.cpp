#include "my.hpp"
namespace task{
    // ------------------------------------ [ Type Definitions ] --------------------------------
    struct My::Impl{ std::shared_ptr<SharedData> sharedData; std::shared_ptr<Interfaces> interfaces; };


    // ------------------------------------ [ Constructors ] ------------------------------------


    // ------------------------------------ [ Getters/Setters ] -----------------------------------


    // ------------------------------------ [ Methods ] ------------------------------------
    My& My::GetInstance(std::shared_ptr<SharedData> sharedData, std::shared_ptr<Interfaces> interfaces) { static My instance; instance.pImpl->sharedData = sharedData; instance.pImpl->interfaces = interfaces; return instance; }
}
