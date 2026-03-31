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
    print("🔍 Starting clang-tidy check...")
    
    # Ensure compile_commands.json exists
    if not os.path.exists("build/compile_commands.json") and not os.path.exists("compile_commands.json"):
        print("[Error] compile_commands.json not found. Please run build.py first to configure CMake.")
        sys.exit(1)
        
    # Use run-clang-tidy if available to run concurrently
    run_tool = "run-clang-tidy"
    if subprocess.call("which run-clang-tidy", shell=True, stdout=subprocess.DEVNULL) != 0:
        run_tool = "clang-tidy"
        print("[Warning] 'run-clang-tidy' not found, running 'clang-tidy' strictly on src/")
        run_command("find src/ core/ shell/ -name '*.cpp' | xargs clang-tidy -p build/", "Linting failed.")
    else:
        run_command(f"{run_tool} -p build/", "Linting failed.")

    print("✅ Linting passed successfully.")

if __name__ == "__main__":
    main()
