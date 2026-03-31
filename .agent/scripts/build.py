import os
import subprocess
import sys

def run_command(command, fail_message):
    print(f"[Exec] Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"[Error] {fail_message}")
        sys.exit(1)

def main():
    print("🚀 Starting CMake Build Pipeline...")
    # Generate build files
    run_command("cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug -DCMAKE_EXPORT_COMPILE_COMMANDS=ON", "CMake configure failed")
    
    # Try to copy compile commands for LSP
    if os.path.exists("build/compile_commands.json"):
        import shutil
        shutil.copy("build/compile_commands.json", ".")
        print("[Info] Copied compile_commands.json to root.")
        
    # Build
    # Get physical cores
    cores = os.cpu_count() or 2
    run_command(f"cmake --build build -j {cores}", "CMake build failed")
    print("✅ Build completed successfully.")

if __name__ == "__main__":
    main()
