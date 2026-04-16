#!/usr/bin/env python3
import sys
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: check_commit_msg.py <commit-msg-file>")
        sys.exit(1)

    commit_msg_file = sys.argv[1]
    
    try:
        with open(commit_msg_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading commit message: {e}")
        sys.exit(1)

    # Discard lines starting with '#'
    clean_lines = [line for line in lines if not line.strip().startswith('#')]
    if not clean_lines:
        print("Empty commit message. Aborting.")
        sys.exit(1)

    # The first line is the subject logic
    subject = clean_lines[0].strip()

    # Regex for type(scope): Message.
    # We enforce English-only ASCII characters in the scope and message, ending with a period.
    pattern = r'^(feat|feature|fix|bugfix|docs|refactor|test|chore)\([a-zA-Z0-9_\-]+\):\s[a-zA-Z0-9\s_\-\.,\'"\!\?]+[\.]$'
    
    if not re.match(pattern, subject):
        print("\n❌ COMMIT FAILED: Invalid message format.")
        print(f"Your message: '{subject}'\n")
        print("Commit messages must follow the exact structure: `action(scope): English description.`")
        print("Examples of valid messages:")
        print("  ✅ feat(api): Add user signin endpoint.")
        print("  ✅ bugfix(core): Fix parser crash on empty string.")
        print("\nRequirements:")
        print("1. Action must be one of: feat, fix, bugfix, docs, refactor, test, chore.")
        print("2. Scope must be inside parenthesis.")
        print("3. MUST be written in English.")
        print("4. MUST end with a mandatory period ('.')")
        sys.exit(1)

    # Success
    sys.exit(0)

if __name__ == "__main__":
    main()
