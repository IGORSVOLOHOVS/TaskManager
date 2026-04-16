#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys
import tempfile
import platform
import stat
import argparse

SOURCE_REPO = "https://github.com/IGORSVOLOHOVS/antigravity-kit-cpp"

def run_cmd(cmd, cwd=None):
    try:
        subprocess.run(cmd, check=True, cwd=cwd, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{' '.join(cmd)}' failed.")
        print(e.stderr)
        sys.exit(1)

def make_executable(path):
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC)

def initialize_project():
    print("🚀 Initializing Polyglot Agent Infrastructure...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = os.path.join(tmpdir, "antigravity-kit-cpp")
        
        print(f"📦 Cloning {SOURCE_REPO}...")
        run_cmd(["git", "clone", "--depth", "1", "--quiet", SOURCE_REPO, repo_path])

        source_agent = os.path.join(repo_path, ".agent")
        target_agent = os.path.join(os.getcwd(), ".agent")

        if not os.path.exists(source_agent):
            print("❌ Error: .agent directory not found in source repository.")
            sys.exit(1)

        print("📁 Copying .agent to current path...")
        if os.path.exists(target_agent):
            print(f"⚠️ Warning: {target_agent} already exists. Overwriting...")
            shutil.rmtree(target_agent)
            
        shutil.copytree(source_agent, target_agent)
    
    print("✨ Successfully initialized .agent infrastructure!")

def install_unix():
    script_src = os.path.abspath(__file__)
    global_bin = "/usr/local/bin/ai-init"
    user_bin_dir = os.path.expanduser("~/.local/bin")
    user_bin = os.path.join(user_bin_dir, "ai-init")

    make_executable(script_src)

    try:
        if os.access("/usr/local/bin", os.W_OK):
            if os.path.exists(global_bin):
                os.remove(global_bin)
            os.symlink(script_src, global_bin)
            print(f"✅ Installed globally to {global_bin}")
            return
    except Exception:
        pass

    try:
        os.makedirs(user_bin_dir, exist_ok=True)
        if os.path.exists(user_bin):
            os.remove(user_bin)
        os.symlink(script_src, user_bin)
        print(f"✅ Installed to user path: {user_bin}")
        print(f"📢 Make sure {user_bin_dir} is in your PATH.")
    except Exception as e:
        print(f"❌ Failed to install: {e}")

def install_windows():
    script_src = os.path.abspath(__file__)
    bin_dir = os.path.join(os.environ.get("USERPROFILE", os.getcwd()), "bin")
    os.makedirs(bin_dir, exist_ok=True)
    
    cmd_file = os.path.join(bin_dir, "ai-init.cmd")
    
    with open(cmd_file, "w") as f:
        f.write(f'@echo off\npython "{script_src}" %*\n')
    
    print(f"✅ Created Windows wrapper at {cmd_file}")
    print(f"📢 Please ensure {bin_dir} is in your PATH environment variable.")

def main():
    parser = argparse.ArgumentParser(description="Bootstrap Polyglot Agent Infrastructure")
    parser.add_argument("--install", action="store_true", help="Install the utility globally")
    args = parser.parse_args()

    if args.install:
        system = platform.system()
        print(f"🛠️  Installing for OS: {system}")
        if system == "Windows":
            install_windows()
        elif system in ["Linux", "Darwin"]:
            install_unix()
        else:
            print(f"❌ Unsupported OS for global install: {system}")
            sys.exit(1)
    else:
        initialize_project()

if __name__ == "__main__":
    main()
