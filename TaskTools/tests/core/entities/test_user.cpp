
// tests/core/entities/test_user.cpp
#include "core/entities/user.hpp"
#include <gtest/gtest.h>

using namespace core::entities;

TEST(UserEntityTest, CanBeCreatedAndRead) {
    User user(101, "Test User");

    EXPECT_EQ(user.getId(), 101);
    EXPECT_EQ(user.getName(), "Test User");
}

TEST(UserEntityTest, GettersReturnMutableReferences) {
    User user(102, "Initial Name");

    // Получаем изменяемую ссылку и меняем значение
    user.getName() = "Updated Name";

    EXPECT_EQ(user.getName(), "Updated Name");
}

TEST(UserEntityTest, CanBeMoved) {
    User user1(103, "Movable User");
    User user2 = std::move(user1);

    // Проверяем, что данные переместились в user2
    EXPECT_EQ(user2.getId(), 103);
    EXPECT_EQ(user2.getName(), "Movable User");
}