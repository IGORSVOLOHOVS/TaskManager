import os
import subprocess
import sys

def colored_print(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def run_step(name, script_path):
    colored_print(f"=====================================", "34")
    colored_print(f"== STEP: {name}", "34")
    colored_print(f"=====================================", "34")
    
    result = subprocess.run([sys.executable, script_path])
    if result.returncode != 0:
        colored_print(f"[FAIL] {name} failed!", "31")
        sys.exit(1)
    else:
        colored_print(f"[PASS] {name} compiled successfully.\n", "32")

def main():
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    
    colored_print("🚀 Running Final Checklist (verify_all)", "35")
    
    run_step("FORMAT", os.path.join(scripts_dir, "format.py"))
    run_step("BUILD", os.path.join(scripts_dir, "build.py"))
    # Note: run tests via coverage script which implicitly tests
    run_step("LINT", os.path.join(scripts_dir, "lint.py"))
    run_step("TEST & COVERAGE", os.path.join(scripts_dir, "run_test_coverage.py"))
    
    colored_print("🎉 All verification steps passed successfully! The C++ project is green.", "32")

if __name__ == "__main__":
    main()
