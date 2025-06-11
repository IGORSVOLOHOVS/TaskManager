// src/adapters/persistence/in_memory_user_repository.cpp
#include "core/use_cases/i_user_repository.hpp"
#include "pch.hpp"

#include <map>
#include <vector>

namespace adapters::persistence {

// Конкретная реализация репозитория, которая хранит данные в памяти.
// Эта реализация ничего не знает о use cases, которые её используют,
// она только следует контракту интерфейса IUserRepository.
class InMemoryUserRepository final : public core::use_cases::IUserRepository {
public:
    InMemoryUserRepository() { spdlog::info("InMemoryUserRepository created."); }

    void addUser(core::entities::User user) override {
        int id = user.getId();
        if (m_users.count(id)) {
            spdlog::warn("User with id {} already exists. Overwriting.", id);
        } else {
            spdlog::info("Adding user with id {} to repository.", id);
        }
        // std::map требует, чтобы ключ был const, поэтому мы не можем просто переместить
        // user. Вместо этого, мы перемещаем user в map, который создаст свою копию ключа и значения.
        m_users.insert_or_assign(id, std::move(user));
    }

    std::optional<core::entities::User> findUserById(int id) override {
        auto it = m_users.find(id);
        if (it != m_users.end()) {
            spdlog::info("User with id {} found.", id);
            // Возвращаем копию, чтобы не нарушать инкапсуляцию хранилища
            // Для этого у User должен быть конструктор копирования, но мы его удалили.
            // Поэтому создадим нового юзера с теми же данными.
            // Это компромисс из-за "нет копирования". В реальном проекте
            // Entity могут быть копируемыми.
            return core::entities::User(it->second.getId(), it->second.getName());
        }
        spdlog::warn("User with id {} not found.", id);
        return std::nullopt;
    }

private:
    std::map<int, core::entities::User> m_users;
};

// Фабричная функция для сокрытия конкретного типа реализации от main
// Возвращает уникальный указатель на интерфейс.
std::unique_ptr<core::use_cases::IUserRepository> createUserRepository() {
    return std::make_unique<InMemoryUserRepository>();
}

}  // namespace adapters::persistence
