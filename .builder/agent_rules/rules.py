import shutil
import os
import glob

def copy_rules():
    os.makedirs('.agent/rules', exist_ok=True)
    for file in glob.glob('.builder/agent_rules/*.md'):
        shutil.copy(file, '.agent/rules/')
        print(f"Copied {file} to .agent/rules/")
copy_rules()