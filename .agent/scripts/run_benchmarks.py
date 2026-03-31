#!/usr/bin/env python3
import os
import subprocess
import glob

def main():
    print("========================================")
    print(" Running nanobench benchmarks...")
    print("========================================")
    
    build_dir = "build"
    if not os.path.exists(build_dir):
        print("Build directory not found. Please run CMake build (e.g., via /build workflow) first.")
        return

    # Find executables prefix 'bench_'
    bench_execs = glob.glob(f"{build_dir}/**/bench_*", recursive=True)
    bench_execs = [x for x in bench_execs if os.path.isfile(x) and os.access(x, os.X_OK)]

    if not bench_execs:
        print("No executable benchmark binaries found matching 'bench_*'.")
        print("Ensure your CMakeLists.txt produces output starting with 'bench_'.")
        return

    for exe in bench_execs:
        print(f"\n---> Executing {exe}")
        subprocess.run([exe], check=False)
    
    html_files = glob.glob("*.html")
    if html_files:
        print("\n[SUCCESS] Benchmark reports generated:")
        for html in html_files:
            print(f"  - {os.path.abspath(html)}")
            # Optional: 
            # os.system(f"xdg-open {html}")

if __name__ == "__main__":
    main()
