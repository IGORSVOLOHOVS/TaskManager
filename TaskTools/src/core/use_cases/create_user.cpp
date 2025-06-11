// src/core/use_cases/create_user.cpp
#include "core/use_cases/create_user.hpp"
#include "core/entities/user.hpp"

namespace core::use_cases {

struct CreateUser::Impl {
    std::unique_ptr<IUserRepository> userRepository;
};

CreateUser::CreateUser(std::unique_ptr<IUserRepository> userRepo)
    : pimpl{std::make_unique<Impl>(Impl{std::move(userRepo)})} {
    if (!pimpl->userRepository) {
        throw std::invalid_argument("User repository cannot be null.");
    }
}

CreateUser::~CreateUser() = default;
CreateUser::CreateUser(CreateUser &&) noexcept = default;
CreateUser &CreateUser::operator=(CreateUser &&) noexcept = default;

void CreateUser::execute(int id, const std::string &name) {
    spdlog::info("Use case 'CreateUser' executed for id={}", id);
    // 1. Валидация входных данных
    if (name.empty()) {
        spdlog::error("User name cannot be empty.");
        throw std::invalid_argument("User name cannot be empty.");
    }

    // 2. Создание сущности
    entities::User newUser(id, name);

    // 3. Использование репозитория для сохранения
    pimpl->userRepository->addUser(std::move(newUser));
    spdlog::info("User with id={} successfully passed to repository.", id);
}

}  // namespace core::use_cases
