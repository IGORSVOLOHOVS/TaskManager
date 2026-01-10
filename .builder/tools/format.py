import os, subprocess

def format_code():
    src_dir = "src"
    include_dir = "include"
    extensions = {".cpp", ".h", ".hpp"}

    if os.path.exists(src_dir):
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    path = os.path.join(root, file)
                    print(f"✨ Formatting {path}")
                    subprocess.run(["clang-format", "-i", path])

    if os.path.exists(include_dir):
        for root, dirs, files in os.walk(include_dir):
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    path = os.path.join(root, file)
                    print(f"✨ Formatting {path}")
                    subprocess.run(["clang-format", "-i", path])