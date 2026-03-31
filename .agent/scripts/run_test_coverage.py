import os
import subprocess
import sys
import platform
import shutil
import glob

# Config
BUILD_DIR = "build"
OUTPUT_DIR = "docs/coverage-report"
INFO_FILE = "coverage.info"
FILTERED_FILE = "coverage_filtered.info"

def run_command(command, fail_message):
    print(f"[Exec] Executing: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"[Error] {fail_message}")
        sys.exit(1)

def run_windows_coverage():
    print("[Windows] Verify OpenCppCoverage...")
    executable = "OpenCppCoverage"
    
    if shutil.which("OpenCppCoverage") is None:
        default_path = r"C:\Program Files\OpenCppCoverage\OpenCppCoverage.exe"
        if os.path.exists(default_path):
            executable = f'"{default_path}"'
        else:
            print("[Error] OpenCppCoverage not found.")
            sys.exit(1)

    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)

    test_exes = glob.glob(os.path.join(BUILD_DIR, "**", "test_*.exe"), recursive=True)
    if not test_exes:
        test_exes = glob.glob(os.path.join(BUILD_DIR, "**", "*_test.exe"), recursive=True)
        
    if not test_exes:
        print(f"[Error] No test executables found in {BUILD_DIR}.")
        sys.exit(1)

    cov_files = []
    for i, test_exe in enumerate(test_exes):
        cov_file = f"coverage_{i}.cov"
        cov_files.append(cov_file)
        cmd = f"{executable} --export_type binary:{cov_file} --sources {os.getcwd()} --modules * -- {test_exe}"
        run_command(cmd, f"Coverage failed for {test_exe}")

    merge_args = " ".join([f"--input_coverage {cov}" for cov in cov_files])
    cmd = f"{executable} {merge_args} --export_type html:{OUTPUT_DIR} --sources {os.getcwd()} --modules *"
    run_command(cmd, "Failed to merge coverage reports")
    
    for cov in cov_files:
        if os.path.exists(cov):
            os.remove(cov)
    print(f"[Success] Open {OUTPUT_DIR}/index.html to view results.")

def run_linux_coverage():
    print("[Linux] Detected Linux/Unix. Using lcov/genhtml...")
    if subprocess.call("which lcov", shell=True, stdout=subprocess.DEVNULL) != 0:
        print("[Error] lcov not found.")
        sys.exit(1)

    run_command(f"lcov --directory {BUILD_DIR} --zerocounters", "Failed to reset counters")
    run_command(f"cd {BUILD_DIR} && ctest --output-on-failure", "Tests failed! Coverage aborted.")
    run_command(f"lcov --directory {BUILD_DIR} --capture --output-file {INFO_FILE} --ignore-errors mismatch,source", "Failed to capture")
    
    run_command(
        f"lcov --remove {INFO_FILE} '/usr/*' '*/_deps/*' '*/tests/*' '*/external/*' --output-file {FILTERED_FILE} --ignore-errors unused",
        "Failed to filter coverage data"
    )

    run_command(f"genhtml {FILTERED_FILE} --output-directory {OUTPUT_DIR} --legend --demangle-cpp", "Failed to generate HTML")
    print(f"[Success] Open {OUTPUT_DIR}/index.html to view results.")

def main():
    if not os.path.exists(BUILD_DIR):
        print(f"[Error] Build directory '{BUILD_DIR}' does not exist. Run build.py first.")
        sys.exit(1)
        
    if platform.system() == "Windows":
        run_windows_coverage()
    else:
        run_linux_coverage()

if __name__ == "__main__":
    main()
