#!/usr/bin/env python3
import argparse
import subprocess
import os
import datetime 
import shutil

import tkinter as tk
from tkinter import messagebox


# --run <generator> <type>
# --run_tests
# --run_web
# --docs
# --docker
# --lib <name>
# --web
# --swig
# --git <branch_name>
# --pack
# --empty

def run(generator, type):
    command = ["cmake"]

    if generator == 'N':
        generator = "Ninja"
    elif generator == 'M':
        generator = "MinGW Makefiles"
    elif generator == 'V':
        generator = None
    elif generator == 'X':
        generator = "Xcode"
    else:
        generator = None

    if type == 'D':
        type = "Debug"
    elif type == 'R':
        type = "Release"
    else:
        type = None

    if generator is not None:
        command.append(f"-G{generator}")
    if type is not None:
        command.append(f"-DCMAKE_BUILD_TYPE={type}")

    command.append("-Bbuild")
    command.append("-S.")
    
    # configure
    subprocess.run(command)

    # build
    command = ["cmake", "--build", "build"]
    subprocess.run(command)

def run_tests():
    command = ["ctest", "--test-dir", "build"]
    subprocess.run(command)

def run_web():
    # Linux
    if os.name == "posix":
        # configure 
        command = ["cmake", "-Bbuild", "-S."]
        subprocess.run(command, check=True)

        # build
        command = ["make", "-C", "build", "install"]
        subprocess.run(command, check=True)

        # run
        command = ["xdg-open", "web/index.html"]
        subprocess.run(command, check=True)
    else:
        # configure 
        command = ["emcmake.bat", "cmake", "-Bbuild", "-S."]
        subprocess.run(command, check=True)

        # build
        command = ["emmake.bat", "make", "-C", "build", "install"]
        subprocess.run(command, check=True)

        # run
        command = ["emrun.bat", "--browser", "chrome", "web"]
        subprocess.run(command, check=True)

def docs():
    command = ["cmake", "--build", "build", "--config", "Release", "--target", "documentation"]
    subprocess.run(command)

def docker():
    print("Unfortunatelly, the docker is not available yet.")

def lib():
    name = input("Enter the name of the library (use underscores for spaces): ")


    if os.path.exists(name):
        print("Library already exists.")
        return
    else:
        os.makedirs(name, exist_ok=True) 

    namespace = name.lower()
    class_name = name.title().replace("_", "")
    struct_name = class_name + "Data"

    # open tools/other/my/CmakeLists.txt and replace my on name
    with open("tools/other/my/CMakeLists.txt", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if "my" in line:
                lines[i] = line.replace("my", name)
    # save the file
    with open(name + "/CMakeLists.txt", "w") as file:
        file.writelines(lines)

    # open tools/other/my/my.cpp and replace my on name, My on ClassName, MY on NAMESPACE
    with open("tools/other/my/my.cpp", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if "my" in line:
                lines[i] = line.replace("task", name)
            if "My" in line:
                lines[i] = line.replace("My", class_name)
            if "MY" in line:
                lines[i] = line.replace("MY", namespace)

        # replace my on name, My on ClassName, MY on NAMESPACE
        new_lines = lines
        for i, line in enumerate(new_lines):
            lines[i] = line.replace("my", name).replace("My", class_name).replace("MY", namespace).replace("my_d_", name + "_d_")
            

    # save the file
    with open(name + "/" + name + ".cpp", "w") as file:
        file.writelines(lines)

    # open tools/other/my/my.hpp and replace my on name, My on ClassName, MY on NAMESPACE
    with open("tools/other/my/my.hpp", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if "my" in line:
                lines[i] = line.replace("task", name)
            if "My" in line:
                lines[i] = line.replace("My", class_name)
            if "MY" in line:
                lines[i] = line.replace("MY", namespace)

                    # replace my on name, My on ClassName, MY on NAMESPACE
        new_lines = lines
        for i, line in enumerate(new_lines):
            lines[i] = line.replace("my", name).replace("My", class_name).replace("MY", namespace).replace("my_d_", name + "_d_")
    # save the file
    with open(name + "/" + name + ".hpp", "w") as file:
        file.writelines(lines)

def web():
    shutil.copytree("tools/other/web/backend", "backend", dirs_exist_ok=True)
    shutil.copytree("tools/other/web/frontend", "frontend", dirs_exist_ok=True)
    shutil.copyfile("tools/other/web/CMakeLists.txt", "CMakeLists.txt")

    dir = os.getcwd()
    for f in os.listdir(dir):
        if os.path.isdir(f):
            if f == "backend" or f == "frontend" or f == ".vscode" or f == "tools":
                continue
            else:
                shutil.rmtree(f)

def swig():
    shutil.copytree("tools/other/swig", "swig", dirs_exist_ok=True)

def git():
    branch_name = input("Enter the name of the branch: ")

    # Initialize git repository
    subprocess.run(["git", "init"])

    # Check if remote origin already exists
    result = subprocess.run(["git", "remote"], capture_output=True, text=True)
    if "origin" not in result.stdout:
        subprocess.run(["git", "remote", "add", "origin", "https://github.com/IGORSVOLOHOVS/Tasks"])

    # Check if branch already exists
    result = subprocess.run(["git", "branch", "--list", branch_name], capture_output=True, text=True)
    if branch_name not in result.stdout:
        subprocess.run(["git", "checkout", "-b", branch_name])
    else:
        subprocess.run(["git", "checkout", branch_name])

    # Add, commit, and push changes
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    subprocess.run(["git", "push", "--set-upstream", "origin", branch_name], check=True)
    

def pack():
    os.chdir("build")
    command = ["cpack", "-C", "Release", "-G", "ZIP"]
    subprocess.run(command, check=True)
    os.chdir("..")

def empty():
    # remove all folders and file except task.py task.cpp and CMakeLists.txt
    dir = os.getcwd()
    for f in os.listdir(dir):
        if os.path.isdir(f):
            if f == "tools":
                continue
            else:
                shutil.rmtree(f)
        else:
            if f == "task.py" or f == "task.cpp" or f == "CMakeLists.txt":
                continue
            else:
                os.remove(f)
    with open("CMakeLists.txt", "w") as file:
        file.write("cmake_minimum_required(VERSION 3.19)\n\n")
        file.write("project(Task)\n\n")
        file.write("add_executable(Task task.cpp)\n")

    with open("task.cpp", "w") as file:
        file.write("#include <iostream>\n\n")
        file.write("int main() {\n")
        file.write("    std::cout << \"Hello, World!\" << std::endl;\n")
        file.write("    return 0;\n")
        file.write("}\n")

class TaskManager(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Task Manager")
        self.geometry("200x300")

        self.create_widgets()
        self.bind("<Configure>", self.on_resize)

    def create_widgets(self):
        self.run_button = self.create_button("Run", self.run)
        self.run_tests_button = self.create_button("Run tests", self.run_tests)
        self.run_web_button = self.create_button("Run web", self.run_web)
        self.docs_button = self.create_button("Generate documentation", self.docs)
        self.docker_button = self.create_button("Run in docker", self.docker)
        self.lib_button = self.create_button("Create library", self.lib)
        self.web_button = self.create_button("Create web project", self.web)
        self.swig_button = self.create_button("Create SWIG project", self.swig)
        self.git_button = self.create_button("Push to git", self.git)
        self.pack_button = self.create_button("Pack the project", self.pack)
        self.empty_button = self.create_button("Empty the project", self.empty)

    def create_button(self, text, command):
        button = tk.Button(self, text=text, command=command)
        button.pack(expand=True, fill='both')
        button.bind("<Enter>", self.on_enter)
        button.bind("<Leave>", self.on_leave)
        return button

    def on_enter(self, event):
        event.widget.config(borderwidth=2, relief="solid")

    def on_leave(self, event):
        event.widget.config(borderwidth=1, relief="flat")

    def on_resize(self, event):
        new_size = max(10, min(event.width // 10, event.height // 10))
        self.set_button_font_size(new_size)

    def set_button_font_size(self, size):
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(font=("Helvetica", size))

    def run(self):
        run("V", "D")

    def run_tests(self):
        run_tests()

    def run_web(self):
        run_web()

    def docs(self):
        docs()

    def docker(self):
        docker()

    def lib(self):
        lib()

    def web(self):
        web()

    def swig(self):
        swig()

    def git(self):
        git()

    def pack(self):
        pack()

    def empty(self):
        empty()

def main():
    console = False
    if console:
        parser = argparse.ArgumentParser(description="Task manager")
        parser.add_argument("--run", nargs=2, help="Run the project", metavar=("generator", "type"))
        parser.add_argument("--run_tests", action="store_true", help="Run the tests")
        parser.add_argument("--run_web", action="store_true", help="Run the web project")
        parser.add_argument("--docs", action="store_true", help="Generate documentation")
        parser.add_argument("--docker", action="store_true", help="Run the project in docker")
        parser.add_argument("--lib", help="Create a library")
        parser.add_argument("--web", action="store_true", help="Create a web project")
        parser.add_argument("--swig", action="store_true", help="Create a SWIG project")
        parser.add_argument("--git", action="store_true", help="Push the project to the git")
        parser.add_argument("--pack", action="store_true", help="Pack the project")
        parser.add_argument("--empty", action="store_true", help="Empty the project")
        args = parser.parse_args()

        if args.run:
            run(args.run[0], args.run[1]) # python.exe .\task.py --run V D - run the project with Visual Studio and Debug configuration
        elif args.run_tests:
            run_tests()
        elif args.run_web:
            run_web()
        elif args.docs:
            docs()
        elif args.docker:
            docker()
        elif args.lib:
            lib()
        elif args.web:
            web()
        elif args.swig:
            swig()
        elif args.git:
            git()
        elif args.pack:
            pack()
        elif args.empty:
            empty()
    else:
        # create ui with tkinter
        app = TaskManager()
        app.mainloop()


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
