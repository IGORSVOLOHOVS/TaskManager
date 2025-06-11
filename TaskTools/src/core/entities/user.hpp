#pragma once

#include "pch.hpp"  // PCH

namespace core::entities {

class User {
public:
    // Конструктор принимает ID и имя
    User(int id, std::string name);
    // Деструктор необходим для PIMPL с unique_ptr
    ~User();

    // Запрещаем копирование, разрешаем перемещение
    User(const User &) = delete;
    User &operator=(const User &) = delete;
    User(User &&) noexcept;
    User &operator=(User &&) noexcept;

    // Геттеры, возвращающие изменяемые ссылки
    int &getId();
    const int &getId() const;  // const-версия

    std::string &getName();
    const std::string &getName() const;  // const-версия

private:
    // PIMPL идиома: скрываем детали реализации
    struct Impl;
    std::unique_ptr<Impl> pimpl;
};

}  // namespace core::entities