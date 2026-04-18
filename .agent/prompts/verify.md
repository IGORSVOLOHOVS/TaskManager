# Instruction: Verify Previous Step

**Task**: Critically evaluate the most recent action or implementation step performed in this conversation.

**Requirements**:
1. **Consistency Check**: Does the implemented code or action exactly match the approved plan?
2. **Quality Check**: 
   - Does it adhere to the relevant Rules (e.g., `CPP_FUNCTIONAL_CORE.md`, `PYTHON_CLEAN_CODE.md`)?
   - Are there any obvious bugs, missing edge cases, or logic errors?
3. **Execution Check**: 
   - If code was written, has it been verified with the appropriate verification script (e.g., `verify_all.py` or `/lint-python`)?
   - Are there any manual verification steps remaining?

**Output**:
- If everything is correct: State "Verification successful. The step was performed correctly."
- If issues are found: Provide a clear, bulleted list of discrepancies or required fixes.
