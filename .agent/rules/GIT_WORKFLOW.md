# Git Workflow & Commit Guidelines

## 1. Branching Strategy
The project strictly follows a structured branching model:
- `main`: The production-ready code.
- `test`: The staging environment for testing release candidates.
- `dev`: The active development channel. All features are merged here first.
- `feat/feature-name` (or `feature/...`): Used to implement new functionality. Branches off from `dev`, merges back to `dev`.
- `bugfix/issue-name` (or `fix/...`): Used to patch non-critical bugs. Branches off from `dev`, merges back to `dev`.

## 2. Semantic Commit Pattern
We utilize Semantic Conventional Commits. Every commit must adhere to this exact blueprint:

`type(scope): Description.`

### Commit Types
You MUST use one of the following words as the commit type:
- `feat` (or `feature`): A new feature.
- `fix` (or `bugfix`): A bug fix.
- `docs`: Documentation changes only.
- `refactor`: A code change that neither fixes a bug nor adds a feature.
- `test`: Adding missing tests or correcting existing tests.
- `chore`: Changes to the build process, scripting, or auxiliary tools.

### English Only
Commit messages **MUST be written in English**. 

### The Mandatory Period (`.`)
Every single commit description **MUST end in a period (`.`)**.

### Examples
✅ `feat(parser): Add regex matching support.`
✅ `bugfix(laser): Resolve null pointer exception.`
❌ `fix(Laser) resolve null pointer` -> Missing period, bad casing.
❌ `добавил фичу` -> Non-English, no scope, no period.
