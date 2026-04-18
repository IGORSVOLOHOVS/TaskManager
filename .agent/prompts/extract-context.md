# Instruction: Extract Session Brain (High-Density Context)

**Task**: Synthesize a comprehensive, technical, and high-density summary of the current session's state for immediate context transfer to a new environment. 

**Requirements**:
1. **Core Context**: 
   - Define the primary project goal and the specific sub-task focused on in this session.
   - Mention any active agents or specialized roles that were operating.
2. **Technical State-of-the-Play**:
   - **Modified Files**: List all changed files with a 1-sentence summary of the *logic* change in each.
   - **Verification Status**: Precise result of the last build, test run, or lint (e.g., "Build passing, 3 lint errors in X.cpp remains").
3. **Established ADRs & Logic**:
   - List key architectural decisions and design patterns applied.
   - Document any discovered technical constraints or "dead ends" to avoid repeating mistakes.
4. **Contextual Memory Stack**:
   - Critical file paths, URIs, and environment variables.
   - Specific function names, data structures, or API endpoints that are "hot" (currently being worked on).
5. **Detailed Task Trace**:
   - What is 100% finished.
   - What is partially implemented (and where exactly it stops).
   - The immediate next 3 steps to resume execution.

**Output Format**:
1. **Suggested Name**: A clear, technical name (e.g., `feature-auth-refactor-part1-stable`).
2. **Transfer Block**: Provide the summary in a single Markdown block labeled `## SESSION CONTEXT TRANSFER: [Descriptive Name]`. Use concise, technical language (bullet points preferred).
