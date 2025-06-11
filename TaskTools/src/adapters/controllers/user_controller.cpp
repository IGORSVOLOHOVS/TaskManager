// src/adapters/controllers/user_controller.cpp
#include "adapters/controllers/user_controller.hpp"

namespace adapters::controllers {

struct UserController::Impl {
    std::unique_ptr<core::use_cases::CreateUser> createUserUseCase;
};

UserController::UserController(std::unique_ptr<core::use_cases::CreateUser> createUserUseCase)
    : pimpl{std::make_unique<Impl>(Impl{std::move(createUserUseCase)})} {
    if (!pimpl->createUserUseCase) {
        throw std::invalid_argument("CreateUser use case cannot be null.");
    }
}

UserController::~UserController() = default;
UserController::UserController(UserController &&) noexcept = default;
UserController &UserController::operator=(UserController &&) noexcept = default;

void UserController::handleCreateUserRequest(int id, const std::string &name) {
    try {
        spdlog::info("Controller handling request to create user '{}'", name);
        pimpl->createUserUseCase->execute(id, name);
        // Здесь мог бы быть вызов Presenter для форматирования ответа
    } catch (const std::exception &e) {
        spdlog::error("Error in create user request: {}", e.what());
        // Обработка ошибки, передача во View
    }
}

}  // namespace adapters::controllers
