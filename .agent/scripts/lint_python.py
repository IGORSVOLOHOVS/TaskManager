#!/usr/bin/env python3
import subprocess
import sys
import os

def main():
    print("🔍 Linting Python code...")
    failed = False
    
    try:
        print("➡️ Running Ruff (check)...")
        subprocess.run(["uv", "run", "ruff", "check", "."], check=True, text=True)
        print("✅ Ruff linting passed.")
    except subprocess.CalledProcessError:
        print("❌ Ruff found issues.")
        failed = True
    except FileNotFoundError:
        print("❌ 'uv' command not found.")
        sys.exit(1)

    try:
        print("➡️ Running Mypy (strict type check)...")
        subprocess.run(["uv", "run", "mypy", "--strict", "."], check=True, text=True)
        print("✅ Mypy typing passed.")
    except subprocess.CalledProcessError:
        print("❌ Mypy found type errors.")
        failed = True

    try:
        print("➡️ Running Vulture (dead code check)...")
        # Run vulture to find dead/unused code.
        subprocess.run(["uv", "run", "--with", "vulture", "vulture", "."], check=True, text=True)
        print("✅ Vulture found no dead code.")
    except subprocess.CalledProcessError:
        print("❌ Vulture found potentially dead/unused code. (Warning or Error based on strictness)")
        failed = True

    try:
        print("➡️ Running Bandit (security vulnerabilities)...")
        # Run bandit recursively (-r) and only report high severity issues or standard (-ll/-lll is quieter, we use default for now)
        subprocess.run(["uv", "run", "--with", "bandit", "bandit", "-r", "."], check=True, text=True, stdout=subprocess.DEVNULL)
        print("✅ Bandit found no high severity security issues.")
    except subprocess.CalledProcessError:
        print("❌ Bandit found potential security vulnerabilities.")
        failed = True

    try:
        print("➡️ Running Radon (complexity check)...")
        # Run radon to find complex blocks (C rank or worse). 
        # This acts as a warning and does not fail the build.
        result = subprocess.run(
            ["uv", "run", "--with", "radon", "radon", "cc", ".", "-nc"], 
            capture_output=True, 
            text=True
        )
        if result.stdout.strip():
            print("⚠️ [WARNING] Radon found complex code blocks (Class C or worse):")
            print(result.stdout)
        else:
            print("✅ Radon complexity looks good.")
    except Exception as e:
        print(f"⚠️ Radon check warnings/errors: {e}")

    if failed:
        print("❌ Python Linting Failed.")
        sys.exit(1)
    else:
        print("✅ All Python static analysis & security passed!")

if __name__ == "__main__":
    main()
