// src/core/use_cases/create_user.hpp
#pragma once

#include "core/use_cases/i_user_repository.hpp"
#include "pch.hpp"

namespace core::use_cases {

// Вариант использования: Создание пользователя.
// Оркестрирует бизнес-логику, используя сущности и интерфейсы.
class CreateUser {
public:
    // Зависимость внедряется через конструктор (Dependency Injection)
    explicit CreateUser(std::unique_ptr<IUserRepository> userRepo);
    ~CreateUser();

    CreateUser(const CreateUser &) = delete;
    CreateUser &operator=(const CreateUser &) = delete;
    CreateUser(CreateUser &&) noexcept;
    CreateUser &operator=(CreateUser &&) noexcept;

    // Основной метод, выполняющий бизнес-логику
    void execute(int id, const std::string &name);

private:
    struct Impl;
    std::unique_ptr<Impl> pimpl;
};

}  // namespace core::use_cases