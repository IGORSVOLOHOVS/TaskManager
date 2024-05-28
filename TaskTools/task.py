#!/usr/bin/env python3
import argparse
import subprocess
import os
import datetime


def install(args):
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
    # set also webassembly target
    subprocess.run(["emcmake","cmake", "..", "-DWEB=ON"], check=True)
    subprocess.run(["emmake", "cmake", "--build", "."], check=True)
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
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
