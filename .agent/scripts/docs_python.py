#!/usr/bin/env python3
import subprocess
import sys
import os

def main():
    print("📚 Generating Python documentation via pdoc...")
    
    # Try looking for a src/ directory
    target_dir = "src" if os.path.exists("src") else "."
    
    try:
        # Run pdoc and output html to a /docs directory by default
        subprocess.run(
            ["uv", "run", "--with", "pdoc", "pdoc", target_dir, "-o", "docs"], 
            check=True, 
            text=True
        )
        print("✅ Documentation generated successfully in the 'docs/' directory.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Generating documentation failed: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ 'uv' command not found. Please install uv (https://github.com/astral-sh/uv).")
        sys.exit(1)

if __name__ == "__main__":
    main()
