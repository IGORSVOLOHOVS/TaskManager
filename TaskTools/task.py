import argparse
import os
import subprocess
import sys
import shutil

def install_dependencies():
    try:
        subprocess.check_call(["conan", "install", ".", "--build=missing", "--output-folder", "build", "-c", "tools.env.virtualenv:powershell=True"])
    except subprocess.CalledProcessError:
        sys.exit(1)

def cmake_build(preset):
    try:
        subprocess.check_call(["cmake", "--preset", preset])
        print(f"CMake has been successfully executed with preset {preset}!")

        # Запуск PowerShell скриптов от имени администратора
        subprocess.call(["powershell.exe", "-File", "./build/cmake/conanbuild.ps1"])
        subprocess.call(["powershell.exe", "-File", "./build/cmake/conanrun.ps1"])

        subprocess.check_call(["cmake", "--build", ".", "--preset", preset])
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

def run_task_exe():
    shutil.copyfile("./build/build/bin/task.exe", "./build/build/bin/task.exe")
    subprocess.call("./build/build/bin/task.exe")

def pack():
    os.chdir("./build/build")
    try:
        subprocess.check_call(["cpack", "-G", "NSIS"])
        print("CPack has successfully created the NSIS package!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during CPack execution: {e}")
        sys.exit(1)
    finally:
        os.chdir("../../")

def main():
    parser = argparse.ArgumentParser(description='Task automation script.')
    parser.add_argument('command', choices=['all', 'install', 'debug', 'build', 'run', 'pack'])
    args = parser.parse_args()

    if args.command == 'all':
        install_dependencies()
        cmake_build('conan-release')
        run_task_exe()
        pack()
    elif args.command == 'install':
        install_dependencies()
    elif args.command == 'release':
        cmake_build('conan-release')
    elif args.command == 'default':
        cmake_build('conan-default')
    elif args.command == 'run':
        run_task_exe()
    elif args.command == 'pack':
        pack()

if __name__ == "__main__":
    main()
