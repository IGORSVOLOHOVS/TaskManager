#!/usr/bin/env python3
import subprocess
import sys

def main():
    print("🧹 Formatting Python code using Ruff via uv...")
    try:
        # Run ruff format
        result = subprocess.run(["uv", "run", "ruff", "format", "."], check=True, text=True)
        print("✅ Python formatting complete.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Formatting failed: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ 'uv' command not found. Please install uv (https://github.com/astral-sh/uv).")
        sys.exit(1)

if __name__ == "__main__":
    main()
