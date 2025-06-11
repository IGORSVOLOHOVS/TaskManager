// src/adapters/presenters/user_presenter.hpp
#pragma once

#include "core/entities/user.hpp"
#include "pch.hpp"

namespace adapters::presenters {

// Presenter отвечает за преобразование данных из формата, удобного для
// use case (т.е. Entity), в формат, удобный для отображения (View).
class UserPresenter {
public:
    // В данном простом примере - статический метод, возвращающий строку
    static std::string format(const core::entities::User &user) {
        return "User Details: [ID: " + std::to_string(user.getId()) + ", Name: '" + user.getName() + "']";
    }
};

}  // namespace adapters::presenters
