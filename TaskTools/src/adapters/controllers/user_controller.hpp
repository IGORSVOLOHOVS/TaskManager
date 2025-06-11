// src/adapters/controllers/user_controller.hpp
#pragma once

#include "core/use_cases/create_user.hpp"
#include "pch.hpp"

namespace adapters::controllers {

// Контроллер - точка входа для внешних запросов (например, от UI или CLI).
// Преобразует входные данные и вызывает соответствующий use case.
class UserController {
public:
    explicit UserController(std::unique_ptr<core::use_cases::CreateUser> createUserUseCase);
    ~UserController();

    UserController(const UserController &) = delete;
    UserController &operator=(const UserController &) = delete;
    UserController(UserController &&) noexcept;
    UserController &operator=(UserController &&) noexcept;

    // Обрабатывает запрос на создание пользователя
    void handleCreateUserRequest(int id, const std::string &name);

private:
    struct Impl;
    std::unique_ptr<Impl> pimpl;
};

}  // namespace adapters::controllers
