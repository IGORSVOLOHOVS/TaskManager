// src/core/use_cases/i_user_repository.hpp
#pragma once

#include "core/entities/user.hpp"
#include "pch.hpp"

namespace core::use_cases {

// Абстрактный интерфейс для репозитория пользователей.
// Определяет контракт, которому должны следовать реализации в слое адаптеров.
// "Никакого наследования" здесь трактуется как отказ от наследования РЕАЛИЗАЦИИ.
// Наследование от чисто абстрактного класса (интерфейса) является основой
// полиморфизма и инверсии зависимостей - ключевых принципов Чистой Архитектуры.
class IUserRepository {
public:
    virtual ~IUserRepository() = default;
    virtual void addUser(entities::User user) = 0;
    virtual std::optional<entities::User> findUserById(int id) = 0;
};

}  // namespace core::use_cases