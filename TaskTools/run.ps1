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

# Install dependencies through Conan --deployer=full_deploy
$ErrorActionPreference = 'Stop'
conan install . --build=missing --output-folder build -c tools.env.virtualenv:powershell=True

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

# Переход в директорию build для выполнения CPack
Push-Location -Path .\build\build

# собираем пакет NSIS с помощью cpack
try {
    cpack -G "NSIS"
    Write-Output "CPack has successfully created the NSIS package!"
} catch {
    Write-Output "An error occurred during CPack execution: $_"
    exit 1
} finally {
    # Возвращаемся обратно в исходную директорию
    Pop-Location
}

