# Git Deploy Prompt

Use this prompt to automate the staging, committing, and pushing of changes to the repository according to the established `GIT_WORKFLOW.md`.

## Instruction

1. **Check Status**: Run `git status` to see all changed files.
2. **Stage Changes**: Stage all relevant files.
3. **Commit**: Create a commit message following the pattern `action(scope): Description.`.
   - Ensure the description starts with a capital letter and ends with a period.
   - Example: `feat(prompts): Add implementation plan template and git-deploy prompt.`
4. **Push**: Push the changes to the current branch.

## Rules
- Never push directly to `main` if a feature branch is active.
- Always verify that the code passes linting/formatting (if applicable) before pushing.
