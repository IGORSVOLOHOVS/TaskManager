#!/usr/bin/env python3
import os
import subprocess
import sys

def run_clang_tidy():
    print("========================================")
    print(" Running clang-tidy static analysis...")
    print("========================================")
    
    build_dir = "build"
    if not os.path.exists(f"{build_dir}/compile_commands.json"):
        print("Error: compile_commands.json not found in build/.")
        print("Please configure CMake with -DCMAKE_EXPORT_COMPILE_COMMANDS=ON")
        return False
        
    cmd = [
        "run-clang-tidy",
        "-p", build_dir,
        "-j", str(os.cpu_count() or 4),
        "-quiet"
    ]
    
    try:
        res = subprocess.run(cmd)
        if res.returncode != 0:
            print("\n[ERROR] clang-tidy found issues!")
            return False
        print("\n[SUCCESS] clang-tidy passed with no warnings.")
        return True
    except FileNotFoundError:
        print("Error: 'run-clang-tidy' utility not found in PATH.")
        print("Install it via your package manager (e.g., sudo apt install clang-tidy).")
        return False

def main():
    success = run_clang_tidy()
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
