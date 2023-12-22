param (
    [int]$runMode = 1
)

# Set the execution policy to allow script running
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

# Remove the 'build' directory if it exists
if (Test-Path -Path "build") {
    Remove-Item -Recurse -Force "build"
}

# Install dependencies through Conan
$ErrorActionPreference = 'Stop'
conan install . --deployer=full_deploy --build=missing --output-folder build -c tools.env.virtualenv:powershell=True

if ($runMode -eq 1) 
{
    # Run with 'conan-release' preset
    cmake --preset conan-release
    Write-Output "CMake has been successfully executed with preset conan-release!"
    & ".\build\build\Release\generators\conanbuild.ps1"
    & ".\build\build\Release\generators\conanrun.ps1"
    cmake --build . --preset conan-release
    .\build\build\Release\task.exe
} elseif ($runMode -eq 2) {
    # Run with 'conan-default' preset
    cmake --preset conan-default
    Write-Output "CMake has been successfully executed with preset conan-default!"
    & ".\build\build\generators\conanbuild.ps1"
    & ".\build\build\generators\conanrun.ps1"
    cmake --build . --preset conan-release
    .\build\build\Release\task.exe    
}
