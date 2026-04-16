#!/usr/bin/env python3
import subprocess
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def run_script(script_name):
    script_path = os.path.join(SCRIPT_DIR, script_name)
    try:
        subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError:
        print(f"\n❌ Pipeline halted at {script_name}")
        sys.exit(1)

def main():
    print("🚀 Starting Complete Python Verification Pipeline...")
    
    print("\n--- [1/3] FORMATTING ---")
    run_script("format_python.py")
    
    print("\n--- [2/3] LINTING ---")
    run_script("lint_python.py")
    
    print("\n--- [3/3] TESTING ---")
    run_script("run_pytest_coverage.py")
    
    print("\n✅ Python Verification Complete! Code is ready to ship.")

if __name__ == "__main__":
    main()
