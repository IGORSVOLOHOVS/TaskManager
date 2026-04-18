# Instruction: Split Plan by Context (Parallelization)

**Task**: Decompose the current implementation plan into independent, self-contained sub-prompts that can be executed in parallel or in separate context windows.

**Action**:
1. **Identify Independent Blocks**: Group tasks from the `implementation_plan.md` into logically separated modules (e.g., "Database Layer", "API Endpoints", "Frontend UI").
2. **Handle Dependencies**: If a block depends on another, explicitly state: "PREREQUISITE: Wait for Part [N] to be completed and verified before starting."
3. **Storage**: 
   - Create a directory in the current working directory named after the plan (e.g., `plan-auth-system/`).
   - Create numbered Markdown files (e.g., `part1.md`, `part2.md`) inside this directory.

**Content for each `part[N].md`**:
```markdown
# [Plan Name] - Part [N]: [Topic]

- [ ] Status: In Progress (Mark this checkbox when an AI window starts working on this)

## 📋 Context
Briefly summarize the overall project goal and how this specific part fits in.

## 🎯 Specific Task
Provide the detailed implementation instructions, file paths, and logic extracted from the original plan for THIS part only.

## ✅ Verification
Define how to verify that this specific part is completed (e.g., specific test commands or directory checks).
```

**Output**:
Confirm the directory has been created and list the generated part files with a 1-sentence description of each.
