#!/usr/bin/env python3
import argparse
import subprocess
import os
import datetime 
import shutil

def install(args): # use ldd to check if all dependencies are installed
    build(args) 
    subprocess.run(["cmake", "--install", "."], check=True)
    print("Project installed successfully.")

def build(args):
    configure(args)
    subprocess.run(["cmake", "--build", "."], check=True)
    print("Project built successfully.")

def run(args):
    build(args)
    subprocess.run(["./task"], check=True)
    print("Project run successfully.")

def configure(args):
    subprocess.run(["cmake", ".."], check=True)
    print("Project configured successfully.")

def package(args):
    install(args)
    subprocess.run(["cpack"], check=True) 
    print("Project packaged successfully.")

def documentation(args):
    subprocess.run(["cmake", "..", "-DDOCUMENTATION=ON"], check=True)
    build(args)
    try:
        subprocess.run(["xdg-open", "docs/latex/refman.pdf"], check=True)
    except:
        print("Documentation generated successfully. Please open docs/latex/refman.pdf manually.")
    print("Documentation generated successfully.")

def csharp(args):
    subprocess.run(["cmake", "..", "-DSWIG_CSHARP=ON"], check=True)
    build(args)
    print("C# project built successfully.")

def python(args):
    subprocess.run(["cmake", "..", "-DSWIG_PYTHON=ON"], check=True)
    build(args)
    print("Python project built successfully.")

def web(args):
    subprocess.run(["emcmake","cmake", "..", "-DWEB=ON"], check=True)
    subprocess.run(["emmake", "cmake", "--build", "."], check=True)
    subprocess.run(["emrun", "--browser", "chrome", "../web/index.html"], check=True)
    print("WEB project built successfully.")

def tests(args):
    subprocess.run(["cmmake", "..", "-DTESTS=ON"], check=True)
    build(args)
    print("Tests built successfully.")

def clean():
    dir = os.getcwd()
    for f in os.listdir(dir):
        if f == "build":
            continue
        if os.path.isdir(f):
            os.rmdir(f)
        else:
            os.remove(f)

    print("Project cleaned successfully.")

def save():
    original_directory = os.getcwd()
    try:
        os.chdir("..")

        # Check if the remote is already set
        result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
        if "origin" not in result.stdout:
            git_remote = ["git", "remote", "add", "origin", "https://github.com/IGORSVOLOHOVS/Tasks"]
            subprocess.run(git_remote, check=True)

        # Get the current branch name
        result = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True)
        current_branch = result.stdout.strip()

        if current_branch == "master" or current_branch == "main":
            # name of current directory
            branch_name = os.path.basename(os.getcwd())
            git_branch = ["git", "checkout", "-b", branch_name]
            subprocess.run(git_branch, check=True)
        else:
            branch_name = current_branch  # Use the existing branch

        git_add = ["git", "add", "."]
        git_commit = ["git", "commit", "-m", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        git_push = ["git", "push", "--set-upstream", "origin", branch_name]
        subprocess.run(git_add, check=True)
        subprocess.run(git_commit, check=True)
        subprocess.run(git_push, check=True)

        print("Project saved successfully.")
    finally:
        os.chdir(original_directory) 

def docker(args):
    os.chdir("..")
    subprocess.run(["docker", "build", "-t", "task", "."], check=True)
    subprocess.run(["docker", "run", "-t", "-p", "8086:8085", "task"], check=True)
    os.chdir("build")
    print("Project run in docker successfully.")

def add(args):
    os.chdir("..")
    name = input("Enter the name of the task: ")

    repo = "https://github.com/IGORSVOLOHOVS/TaskManager.git"
    current_directory = os.path.basename(os.getcwd())
    cloneDir = os.path.join(os.path.expanduser("~"), "temp", name)
    targetDir = os.path.join(os.path.expanduser("~"), "Projects", current_directory, name)

    if os.path.exists(cloneDir):
        os.rename(cloneDir, f"{cloneDir}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}")

    cloneCmd = f"git clone -n --depth=1 --filter=tree:0 {repo} {cloneDir}"
    subprocess.run(cloneCmd, check=True)
    os.chdir(cloneDir)
    subprocess.run("git sparse-checkout set --no-cone TaskTools", check=True)
    subprocess.run("git checkout", check=True)
    os.makedirs(targetDir, exist_ok=True)

    for f in os.listdir("TaskTools"):
        shutil.move(os.path.join("TaskTools", f), targetDir)

    print("Task added successfully.")

def build_all(args):
    os.chdir("..")
    dir = os.getcwd()
    for f in os.listdir(dir):
        if os.path.isdir(f):
            if f == "build" or f == "include" or f == "src" or f == "subsrc" or f == "images" or f == "test" or f == ".vscode":
                continue
            else:
                print(f"Building {f} project")
                if not os.path.exists(os.path.join(f, "build")):
                    os.makedirs(os.path.join(f, "build"))

                os.chdir(os.path.join(f, "build"))
                build(args)
                os.chdir("../..")
    os.chdir("build")
    build(args)
    print("All projects built successfully.")


def install_all(args):
    os.chdir("..")
    dir = os.getcwd()

    if not os.path.exists("install"):
        os.makedirs("install")

    for f in os.listdir(dir):
        if os.path.isdir(f):
            if f == "build" or f == "include" or f == "src" or f == "subsrc" or f == "images" or f == "test" or f == ".vscode" or f == "install":
                continue
            else:
                print(f"Installing {f} project")
                if not os.path.exists(os.path.join(f, "build")):
                    os.makedirs(os.path.join(f, "build"))

                os.chdir(os.path.join(f, "build"))
                install(args)
                os.chdir("../..")

    os.chdir("build")
    install(args)
    os.chdir("..")

    for f in os.listdir(dir):
        if os.path.isdir(f):
            if f == "build" or f == "include" or f == "src" or f == "subsrc" or f == "images" or f == "test" or f == ".vscode" or f == "install":
                continue
            else:
                shutil.copytree(os.path.join(f, "install"), "install", dirs_exist_ok=True)

    print("All projects installed successfully.")


def only():
    os.chdir("..")
    dir = os.getcwd()
    for f in os.listdir(dir):
        if f == "include" or f == "src" or f == "task.py" or f == ".vscode":
            continue
        if os.path.isdir(f):
            shutil.rmtree(f)
        else:
            os.remove(f)

    cmake_content = """cmake_minimum_required(VERSION 3.20)
get_filename_component(ProjectId ${CMAKE_CURRENT_SOURCE_DIR} NAME)
string(REPLACE " " "_" ProjectId ${ProjectId})
project(${ProjectId} LANGUAGES C CXX VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_INSTALL_PREFIX ${CMAKE_SOURCE_DIR}/install)

if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    set(CMAKE_CXX_FLAGS_DEBUG   "${CMAKE_CXX_FLAGS_DEBUG} -O0 -g -ggdb -D_DEBUG")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Ofast -march=native -g -ggdb -DNDEBUG")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -pg")
elseif(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    set(CMAKE_CXX_FLAGS_DEBUG   "${CMAKE_CXX_FLAGS_DEBUG} -O0 -g -ggdb -D_DEBUG")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Ofast -march=native -g -ggdb -DNDEBUG")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -pg")
elseif(CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    set(CMAKE_CXX_FLAGS_DEBUG   "${CMAKE_CXX_FLAGS_DEBUG} /Od /Zi /D_DEBUG")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /O2 /Ob2 /DNDEBUG")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /DEBUG /PROFILE")
endif()


set(SOURCE_FILES src/main.cpp)

#---[ Add subdirectories ]--- (do not delete this comment)

add_library(${PROJECT_NAME}d SHARED ${SOURCE_FILES})
target_include_directories(${PROJECT_NAME}d PUBLIC include)

add_executable(${PROJECT_NAME} src/main.cpp)
target_link_libraries(${PROJECT_NAME} ${PROJECT_NAME}d)

include(InstallRequiredSystemLibraries)
include(CMakePackageConfigHelpers)
include(CPack)

install(DIRECTORY include/ DESTINATION include)
install(TARGETS ${PROJECT_NAME} ${PROJECT_NAME}d
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
)
install(FILES 
    "${PROJECT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    "${PROJECT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
    DESTINATION lib/cmake/${PROJECT_NAME}
)

file(WRITE ${PROJECT_NAME}Config.cmake.in "@PACKAGE_INIT@
include(CMakeFindDependencyMacro)
# Поиск зависимостей
#find_dependency(имя_зависимости)
set(${PROJECT_NAME}_FOUND TRUE)
set(${PROJECT_NAME}_INCLUDE_DIRS include)
set(${PROJECT_NAME}_LIBRARIES ${PROJECT_NAME}d) # Используйте имя вашего проекта для библиотеки
")
configure_package_config_file(
    "${PROJECT_SOURCE_DIR}/${PROJECT_NAME}Config.cmake.in" # Шаблон конфигурационного файла
    "${PROJECT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    INSTALL_DESTINATION lib/cmake/${PROJECT_NAME}
)
write_basic_package_version_file(
    "${PROJECT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY SameMajorVersion
)
"""

    with open("CMakeLists.txt", "w") as file:
        file.write(cmake_content)

    print("Project cleaned successfully.")

def lib():
    os.chdir("..")
    library_name = input("Enter the name of the library (use underscores for spaces): ")
    if os.path.exists(library_name):
        print("Library already exists.")
        return
    else:
        os.makedirs(library_name, exist_ok=True)

    library_namespace = library_name.lower()
    class_name = library_name.title().replace("_", "")
    struct_name = class_name + "Data"

    # open tools/other/my/CmakeLists.txt and replace my on library_name
    with open("tools/other/my/CMakeLists.txt", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if "my" in line:
                lines[i] = line.replace("my", library_name)
    # save the file
    with open(library_name + "/CMakeLists.txt", "w") as file:
        file.writelines(lines)

    # open tools/other/my/my.cpp and replace my on library_name, My on ClassName, MY on NAMESPACE
    with open("tools/other/my/my.cpp", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if "my" in line:
                lines[i] = line.replace("my", library_name)
            if "My" in line:
                lines[i] = line.replace("My", class_name)
            if "MY" in line:
                lines[i] = line.replace("MY", library_namespace)

        # replace my on library_name, My on ClassName, MY on NAMESPACE
        new_lines = lines
        for i, line in enumerate(new_lines):
            lines[i] = line.replace("my", library_name).replace("My", class_name).replace("MY", library_namespace).replace("my_d_", library_name + "_d_")
            

    # save the file
    with open(library_name + "/" + library_name + ".cpp", "w") as file:
        file.writelines(lines)

    # open tools/other/my/my.hpp and replace my on library_name, My on ClassName, MY on NAMESPACE
    with open("tools/other/my/my.hpp", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if "my" in line:
                lines[i] = line.replace("my", library_name)
            if "My" in line:
                lines[i] = line.replace("My", class_name)
            if "MY" in line:
                lines[i] = line.replace("MY", library_namespace)

                    # replace my on library_name, My on ClassName, MY on NAMESPACE
        new_lines = lines
        for i, line in enumerate(new_lines):
            lines[i] = line.replace("my", library_name).replace("My", class_name).replace("MY", library_namespace).replace("my_d_", library_name + "_d_")
    # save the file
    with open(library_name + "/" + library_name + ".hpp", "w") as file:
        file.writelines(lines)


    # add add_subdirectory({library_name}) to the main CMakeLists.txt after #---[ Add subdirectories ]--- (do not delete this comment)
    # add target_link_libraries(${PROJECT_NAME} + remove ( + ${library_name}) to the main CMakeLists.txt after target_link_libraries(${PROJECT_NAME} (do not delete this comment)
    with open("./CMakeLists.txt", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if "#---[ Add subdirectories ]---" in line:
                lines.insert(i + 1, f"add_subdirectory({library_name})\n")
            if "target_link_libraries(${PROJECT_NAME}" in line:
                lines[i] = line.replace("${PROJECT_NAME}", "${PROJECT_NAME} " + library_name)      
    with open("./CMakeLists.txt", "w") as file:
        file.writelines(lines)

    os.makedirs(library_name, exist_ok=True)
    os.chdir(library_name)

    print("Library created successfully in the", library_name, "directory.")

    






def main():
    parser = argparse.ArgumentParser(description="Task.py - CMake project helper")

    # Aliases
    install_parser = parser.add_argument("--install", "-i", action="store_true", help="Install the project")
    build_parser = parser.add_argument("--build", "-b", action="store_true", help="Build the project")
    run_parser = parser.add_argument("--run", "-r", action="store_true", help="Run the project")
    package_parser = parser.add_argument("--package", "-p", action="store_true", help="Package the project")
    documentation_parser = parser.add_argument("--documentation", "-d", action="store_true", help="Generate documentation")
    csharp_parser = parser.add_argument("--csharp", "-c", action="store_true", help="Build the C# project")
    python_parser = parser.add_argument("--python", "-py", action="store_true", help="Build the Python project")
    web_parser = parser.add_argument("--web", "-w", action="store_true", help="Build the WEB project")
    tests_parser = parser.add_argument("--tests", "-t", action="store_true", help="Build the tests")
    clean_parser = parser.add_argument("--clean", "-cl", action="store_true", help="Clean the project")
    save_parser = parser.add_argument("--save", "-s", action="store_true", help="Save the project")
    docker_parser = parser.add_argument("--docker", "-dock", action="store_true", help="Run the project in docker")
    add_parser = parser.add_argument("--add", "-a", action="store_true", help="Add a new task")
    only_parser = parser.add_argument("--only", "-o", action="store_true", help="Delete all without /include /src/ task.py .vscode")
    build_all_parser = parser.add_argument("--build_all", "-ba", action="store_true", help="Build all projects")
    install_all_parser = parser.add_argument("--install_all", "-ia", action="store_true", help="Install all projects")
    library_parser = parser.add_argument("--lib", "-l", action="store_true", help="Create a new library")

    args = parser.parse_args()

    # Create build directory if it doesn't exist
    build_directory = "build"
    os.makedirs(build_directory, exist_ok=True)  

    # change to build directory if we are not already in it
    if not os.getcwd().endswith(build_directory):
        os.chdir(build_directory)


    if args.install:
        install(args)
    elif args.build:
        build(args)
    elif args.run:
        run(args)
    elif args.package:
        package(args)
    elif args.documentation:
        documentation(args)
    elif args.csharp:
        csharp(args)
    elif args.python:
        python(args)
    elif args.web:
        web(args)
    elif args.tests:
        tests(args)
    elif args.clean:
        clean()
    elif args.save:
        save()
    elif args.docker:
        docker(args)
    elif args.add:
        add(args)
    elif args.only:
        only()
    elif args.build_all:
        build_all(args)
    elif args.install_all:
        install_all(args)
    elif args.lib:
        lib()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

# ------------------------------------------------------server------------------------------------------------------
# #include <iostream>
# #include "connector.hpp"

# int main(int argc, char** argv) {
#     std::cout << "Server started" << std::endl;
#     ServerTCP server({"0.0.0.0", 8085});

#     server.listen();

#     return 0;
# }

# ------------------------------------------------------client------------------------------------------------------
# #include <iostream>

# #include "connector.hpp"

# int main(int argc, char** argv) {
#     ClientTCP client({"0.0.0.0", 8086});

#     client.speak();

#     return 0;
# }
