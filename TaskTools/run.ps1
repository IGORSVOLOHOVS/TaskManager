# Удаляем каталог build, если он существует
if (Test-Path -Path "build") {
    Remove-Item -Recurse -Force "build"
}

# Устанавливаем политику выполнения для запуска скриптов
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Выполняем установку зависимостей через Conan
conan install . --deployer=full_deploy --build=missing --output-folder build -c tools.env.virtualenv:powershell=True 

# Запускаем CMake с заданным пресетом
cmake --preset conan-default

# Выполняем скрипты сборки и запуска, сгенерированные Conan
& ".\build\build\generators\conanbuild.ps1"
& ".\build\build\generators\conanrun.ps1"

# Собираем проект с использованием CMake
cmake --build --preset conan-release

# Запускаем исполняемый файл
& ".\build\build\Release\main.exe"
