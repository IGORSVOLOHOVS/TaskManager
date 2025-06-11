// tests/core/use_cases/test_create_user.cpp
#include <gmock/gmock.h>  // Для моков
#include <gtest/gtest.h>

#include "core/use_cases/create_user.hpp"
#include "core/use_cases/i_user_repository.hpp"

using namespace core::use_cases;
using namespace core::entities;
using ::testing::_;
using ::testing::A;
using ::testing::Property;

// Создаем Mock-объект репозитория для изоляции теста Use Case
class MockUserRepository : public IUserRepository {
public:
    MOCK_METHOD(void, addUser, (User user), (override));
    MOCK_METHOD(std::optional<User>, findUserById, (int id), (override));
};

TEST(CreateUserUseCaseTest, ExecuteSuccessfully) {
    auto mockRepo = std::make_unique<MockUserRepository>();

    // Ожидаем, что метод addUser будет вызван ровно 1 раз
    // с объектом User, у которого id=1 и name="Test"
    EXPECT_CALL(*mockRepo, addUser(A<User>())).Times(1).WillOnce([](User user) {
        EXPECT_EQ(user.getId(), 1);
        EXPECT_EQ(user.getName(), "Test");
    });

    CreateUser createUserUseCase(std::move(mockRepo));

    // Выполняем use case
    createUserUseCase.execute(1, "Test");
}

TEST(CreateUserUseCaseTest, ThrowsOnEmptyName) {
    auto mockRepo = std::make_unique<MockUserRepository>();

    // Не ожидаем вызова addUser
    EXPECT_CALL(*mockRepo, addUser(_)).Times(0);

    CreateUser createUserUseCase(std::move(mockRepo));

    // Проверяем, что выбрасывается исключение std::invalid_argument
    ASSERT_THROW(createUserUseCase.execute(2, ""), std::invalid_argument);
}

TEST(CreateUserUseCaseTest, ThrowsOnNullRepository) {
    // Проверяем, что конструктор бросает исключение при передаче nullptr
    ASSERT_THROW(CreateUser(nullptr), std::invalid_argument);
}