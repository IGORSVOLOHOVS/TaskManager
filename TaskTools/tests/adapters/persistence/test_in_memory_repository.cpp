// tests/adapters/persistence/test_in_memory_repository.cpp
#include <gtest/gtest.h>

// Включаем cpp-файл, чтобы протестировать реализацию.
// Это один из подходов для тестирования без экспорта класса.
#include "adapters/persistence/in_memory_user_repository.cpp"

using namespace adapters::persistence;
using namespace core::entities;

class InMemoryRepositoryTest : public ::testing::Test {
protected:
    std::unique_ptr<core::use_cases::IUserRepository> repo;

    void SetUp() override {
        // Каждый тест получает свежий экземпляр репозитория
        repo = createUserRepository();
    }
};

TEST_F(InMemoryRepositoryTest, AddAndFindUser) {
    User user(1, "Test User");
    // Передаем копию имени, так как user будет перемещен
    std::string name = user.getName();

    repo->addUser(std::move(user));

    auto foundUserOpt = repo->findUserById(1);

    ASSERT_TRUE(foundUserOpt.has_value());
    EXPECT_EQ(foundUserOpt->getId(), 1);
    EXPECT_EQ(foundUserOpt->getName(), name);
}

TEST_F(InMemoryRepositoryTest, FindNonExistentUser) {
    auto foundUserOpt = repo->findUserById(999);
    ASSERT_FALSE(foundUserOpt.has_value());
}

TEST_F(InMemoryRepositoryTest, OverwriteExistingUser) {
    repo->addUser(User(5, "First Version"));
    repo->addUser(User(5, "Second Version"));

    auto foundUserOpt = repo->findUserById(5);

    ASSERT_TRUE(foundUserOpt.has_value());
    EXPECT_EQ(foundUserOpt->getName(), "Second Version");
}