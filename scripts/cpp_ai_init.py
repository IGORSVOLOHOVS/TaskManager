#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys
import tempfile

SOURCE_REPO = "https://github.com/IGORSVOLOHOVS/TaskManager"

def run_cmd(cmd, cwd=None):
    try:
        subprocess.run(cmd, check=True, cwd=cwd, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{' '.join(cmd)}' failed.")
        print(e.stderr)
        sys.exit(1)

def main():
    print("🚀 Initializing C++ Agent Infrastructure...")
    
    # 1. Create a temporary directory for cloning
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = os.path.join(tmpdir, "TaskManager")
        
        print(f"📦 Cloning {SOURCE_REPO}...")
        run_cmd(["git", "clone", "--depth", "1", "--quiet", SOURCE_REPO, repo_path])

        # 2. Path to .agent in the cloned repo
        source_agent = os.path.join(repo_path, ".agent")
        target_agent = os.path.join(os.getcwd(), ".agent")

        if not os.path.exists(source_agent):
            print("❌ Error: .agent directory not found in source repository.")
            sys.exit(1)

        # 3. Copy .agent to current directory
        print("📁 Copying .agent to current path...")
        if os.path.exists(target_agent):
            print(f"⚠️ Warning: {target_agent} already exists. Overwriting...")
            shutil.rmtree(target_agent)
            
        shutil.copytree(source_agent, target_agent)

    print("✨ Successfully initialized .agent infrastructure!")
    print("💡 To install this command globally, run: python3 scripts/install.py")

if __name__ == "__main__":
    main()
