#!/usr/bin/env python3
import os
import platform
import shutil
import sys
import stat

def make_executable(path):
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC)

def install_unix():
    script_src = os.path.abspath(os.path.join(os.path.dirname(__file__), "cpp_ai_init.py"))
    
    # Try global path first, then user path
    global_bin = "/usr/local/bin/cpp-ai-init"
    user_bin_dir = os.path.expanduser("~/.local/bin")
    user_bin = os.path.join(user_bin_dir, "cpp-ai-init")

    # Ensure source is executable
    make_executable(script_src)

    try:
        # Try to link to global bin (might need sudo)
        if os.access("/usr/local/bin", os.W_OK):
            if os.path.exists(global_bin):
                os.remove(global_bin)
            os.symlink(script_src, global_bin)
            print(f"✅ Installed globally to {global_bin}")
            return
    except Exception:
        pass

    # Fallback to user bin
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
    script_src = os.path.abspath(os.path.join(os.path.dirname(__file__), "cpp_ai_init.py"))
    bin_dir = os.path.join(os.environ["USERPROFILE"], "bin")
    os.makedirs(bin_dir, exist_ok=True)
    
    cmd_file = os.path.join(bin_dir, "cpp-ai-init.cmd")
    
    # Create a CMD wrapper
    with open(cmd_file, "w") as f:
        f.write(f'@echo off\npython "{script_src}" %*\n')
    
    print(f"✅ Created Windows wrapper at {cmd_file}")
    print(f"📢 Please ensure {bin_dir} is in your PATH environment variable.")

def main():
    system = platform.system()
    print(f"🛠️  Detected OS: {system}")
    
    if system == "Windows":
        install_windows()
    elif system in ["Linux", "Darwin"]:
        install_unix()
    else:
        print(f"❌ Unsupported OS: {system}")
        sys.exit(1)

if __name__ == "__main__":
    main()
