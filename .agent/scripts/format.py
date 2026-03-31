import os
import subprocess
import sys
import glob

def run_command(command, fail_message):
    print(f"[Exec] Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"[Error] {fail_message}")
        sys.exit(1)

def main():
    print("🧹 Starting clang-format Check...")
    
    # Check if clang-format is installed
    if subprocess.call("clang-format --version", shell=True, stdout=subprocess.DEVNULL) != 0:
        print("[Error] clang-format is not installed.")
        sys.exit(1)

    cpp_files = []
    for ext in ("*.cpp", "*.hpp", "*.c", "*.h"):
        cpp_files.extend(glob.glob(f"src/**/{ext}", recursive=True))
        cpp_files.extend(glob.glob(f"tests/**/{ext}", recursive=True))
        cpp_files.extend(glob.glob(f"core/**/{ext}", recursive=True)) # added core
        cpp_files.extend(glob.glob(f"shell/**/{ext}", recursive=True)) # added shell
        
    # Main file
    if os.path.exists("main.cpp"):
        cpp_files.append("main.cpp")

    if not cpp_files:
        print("[Info] No C++ files found to format.")
        return

    files_str = " ".join(set(cpp_files))
    run_command(f"clang-format -i {files_str}", "clang-format failed to run.")
    
    print("✅ Formatting completed successfully.")

if __name__ == "__main__":
    main()
