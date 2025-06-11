// src/core/entities/user.cpp
#include "core/entities/user.hpp"

namespace core::entities {

// Детали реализации скрыты в .cpp файле
struct User::Impl {
    int id;
    std::string name;
};

User::User(int id, std::string name) : pimpl{std::make_unique<Impl>(Impl{id, std::move(name)})} {
    spdlog::info("User created: id={}, name='{}'", pimpl->id, pimpl->name);
}

// Деструктор должен быть здесь, где Impl является полным типом
User::~User() = default;

// Реализация перемещающих конструктора и оператора
User::User(User &&) noexcept = default;
User &User::operator=(User &&) noexcept = default;

// Реализация геттеров
int &User::getId() { return pimpl->id; }
const int &User::getId() const { return pimpl->id; }

std::string &User::getName() { return pimpl->name; }
const std::string &User::getName() const { return pimpl->name; }

}  // namespace core::entities