# CODING 
- Plan first before you code. Use higher reasoning for planning than for coding.
- When delegating subagents, if subtasks do not require previous subtasks, run them in parallel. Subagents must have less usage than the original creator.
- Before asking about a consequential action, do all preparatory work before my approval so my approval is the final step
- Do not preserve backward compatibility, choose the simplest implementation that fully meets all the current requirements, prefer well established libraries over custom implementations
- Do not refactor unrelated systems. Do not introduce unnecessary complexity.
- Do not introduce new architecture unless required.
- Avoid unnecessary dependencies.
- Do not write unit tests unless something breaks.
- No tests for reversible, low impact changes, only critical infrastructure

# WRITING STYLE 
- Report files changed, commands run, build results, and manual verification steps.
- Respond with as little preamble as possible; keep explanations concise and not overly complex.
- Respond in paragraphs with one idea each. Use active voice and state main idea first.
- List all assumptions made in one line at the start of the response

 # INSTRUCTIONS
 - My instructions outrank any skill or ``AGENTS.md`` file. If anything makes you pause, ask permission or change direction, and name the file and quote the line that made you pause.
 - Say whether things you implement are critical parts of your plan

# RESPONSE FORMAT

At completion, provide:

- Status: complete / partial / blocked
- Changes: concise list of behavior and key files changed
- Database/config: migrations, environment variables, and setup steps
- Verification: commands run and actual outcomes, or what I should run and what I should expect
- Remaining issues: only known gaps or risks
- Run instructions: exact commands when relevant