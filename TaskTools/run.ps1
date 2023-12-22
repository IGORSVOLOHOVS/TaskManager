param (
    [int]$runMode = 1
)

# Set the execution policy to allow script running
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

# Remove the 'build' directory if it exists
if (Test-Path -Path "build") {
    Remove-Item -Recurse -Force "build"
}

if (Test-Path -Path "cmake") {
    Remove-Item -Recurse -Force "cmake"
}

# Install dependencies through Conan
$ErrorActionPreference = 'Stop'
conan install . --deployer=full_deploy --build=missing --output-folder build -c tools.env.virtualenv:powershell=True

if ($runMode -eq 1) 
{
    # Run with 'conan-release' preset
    cmake --preset conan-release
    Write-Output "CMake has been successfully executed with preset conan-release!"
    & ".\build\cmake\conanbuild.ps1"
    & ".\build\cmake\conanrun.ps1"
    cmake --build . --preset conan-release
} elseif ($runMode -eq 2) {
    # Run with 'conan-default' preset
    cmake --preset conan-default
    Write-Output "CMake has been successfully executed with preset conan-default!"
    & ".\build\cmake\conanbuild.ps1"
    & ".\build\cmake\conanrun.ps1"
    cmake --build . --preset conan-release   
}

# поиск task.exe в директории build
$taskExe = Get-ChildItem -Path .\build -Filter task.exe -Recurse -ErrorAction SilentlyContinue

# запуск task.exe
if ($taskExe) {
    Write-Output "task.exe has been found!"
    & $taskExe.FullName
} else {
    Write-Output "task.exe has not been found!"
    exit 1
}

# Экспорт пакета с помощью Conan
conan export-pkg . --name=task --version=1.0 --user=user --channel=testing

# Запуск ISCC.exe с полным путем к файлу .\pkg-setup\task-1.0.iss + перемести task-1.0-setup.exe в директорию pkg-setup
& "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" .\pkg-setup\task-1.0.iss
& Move-Item -Path .\task-1.0-setup.exe -Destination .\pkg-setup -Force


