# Task Manager

## Introduction
Task Manager is an advanced application designed for efficient task and project management. It facilitates the organization and tracking of various project-related tasks, offering a streamlined approach to managing workflows and project timelines.

## Requirements
- C++20: The application is built using C++20 standards.
- CMake: Required for building the project.
- Conan: Used for dependency management.

## How to Use
After installation and setup, execute `manager.bat` to launch the application. The application provides the following functionalities:
- Create, edit, and delete tasks.
- Organize tasks into projects.
- Track the progress of tasks and overall project timelines.

## How to Build
1. Clone the project repository to your local machine.
2. Install necessary dependencies using Conan:
   ```bash
   conan install . --build=missing --output-folder build -c tools.env.virtualenv:powershell=True
   ```
3. Use CMake to build the project:
   ```bash
   cmake --preset conan-default
   cmake --build --preset conan-release
   ```
4. Link libraies and run exe file:
   ```bash
   .\build\build\generators\conanbuild.ps1
   .\build\build\generators\conanrun.ps1
   .\build\build\Release\main.exe
   ```

## Directory Structure
- `TaskTools`: Contains the main source code, tests, and configuration files.
- `icon`: Stores the application icons and related graphical assets.
- `README.md`: Provides information about the project, installation, and usage instructions.
- `manager.bat`: A batch file to launch the application.

## Additional Information
- The `conanfile.txt` and `CMakeLists.txt` files are used for managing dependencies and build configuration, respectively.
