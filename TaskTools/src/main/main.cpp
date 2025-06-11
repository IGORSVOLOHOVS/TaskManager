// src/main/main.cpp
// Это самый внешний слой (Frameworks & Drivers).
// Его единственная задача - собрать (скомпоновать) приложение.

#include "adapters/controllers/user_controller.hpp"
#include "adapters/persistence/in_memory_user_repository.cpp"  // Включаем cpp для фабрики
#include "core/use_cases/create_user.hpp"
#include "pch.hpp"

// --- Composition Root ---
// Здесь происходит создание всех объектов и внедрение зависимостей (DI).
// main ничего не знает о бизнес-логике, он только знает, как
// соединить компоненты вместе.

int main() {
    spdlog::set_level(spdlog::level::info);
    spdlog::info("Application starting...");

    // 1. Создаем зависимость самого нижнего уровня - репозиторий.
    // Мы используем фабричную функцию, чтобы не зависеть от конкретного класса.
    auto userRepository = adapters::persistence::createUserRepository();

    // 2. Создаем Use Case и внедряем в него репозиторий.
    auto createUserUseCase = std::make_unique<core::use_cases::CreateUser>(std::move(userRepository));

    // 3. Создаем контроллер и внедряем в него Use Case.
    auto userController = std::make_unique<adapters::controllers::UserController>(std::move(createUserUseCase));

    // 4. Симулируем внешний запрос (например, от пользователя в CLI).
    spdlog::info("--- Simulating first request ---");
    userController->handleCreateUserRequest(1, "Igor Volokhov");

    spdlog::info("--- Simulating second request ---");
    userController->handleCreateUserRequest(2, "John Doe");

    spdlog::info("--- Simulating invalid request ---");
    userController->handleCreateUserRequest(3, "");

    spdlog::info("Application finished.");
    return 0;
}
