#!/usr/bin/env python3
import subprocess
import sys

def main():
    print("🧪 Running Pytest Coverage...")
    try:
        # Run pytest with coverage reporting
        subprocess.run(["uv", "run", "pytest", "--cov=src", "--cov-report=term-missing", "--cov-report=html"], check=True, text=True)
        print("✅ Pytest Execution complete. Coverage report generated in htmlcov/index.html")
    except subprocess.CalledProcessError as e:
        print(f"❌ Testing failed. Please check the logs above.")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ 'uv' command not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
