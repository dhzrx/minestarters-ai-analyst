---
name: "Skill Creator"
description: "Meta-skill for creating new mining analysis skills with proper structure, frontmatter, workflow steps, and command wrappers."
---

# Skill Creator

## Purpose

Generate new mining analysis skills following the established plugin conventions. This meta-skill ensures consistency across all skills in the mining-analysis plugin by enforcing naming conventions, file structure, frontmatter format, and workflow patterns.

## Workflow

### Step 1: Define Skill Name and Purpose

- Choose a clear, descriptive name (e.g., "Tailings Risk Assessment")
- Write a one-sentence description for the YAML frontmatter
- Identify the primary use case and target audience

### Step 2: Identify Required Data Sources

- List MCP data connectors from `.mcp.json` that the skill will use
- Identify any new data sources that need to be added
- Note which sources require subscriptions or authentication

### Step 3: Define Workflow Steps

- Break the skill into 3-7 sequential steps
- Each step should have a clear input, action, and output
- Include validation checkpoints where appropriate
- Reference existing skills or scripts where work can be reused

### Step 4: Create SKILL.md

Use the template below to generate the skill definition file.

### Step 5: Create Command Wrapper

Create a matching command file in `commands/` that invokes the skill.

### Step 6: Add Reference Docs (if needed)

Place supporting reference material in `skills/<skill-name>/references/`.

## SKILL.md Template

```markdown
---
name: "[Skill Name]"
description: "[One-sentence description of what the skill does and its primary output.]"
---

# [Skill Name]

## Purpose

[2-3 sentences explaining what this skill does, why it exists, and what decisions it supports.]

## Required Inputs

| Input | Description | Source |
|-------|-------------|--------|
| [Input 1] | [What it is] | [Where it comes from] |
| [Input 2] | [What it is] | [Where it comes from] |

## Workflow

### Step 1: [Action Name]

[Description of what happens in this step, including any data collection, analysis, or transformation.]

### Step 2: [Action Name]

[Continue for each step...]

## Output Format

[Describe the expected output: tables, scores, reports, recommendations. Include example table structures.]

## Data Sources

- **[Source Name]** (`mcp-key`): [What data is used from this source]

## References

- `references/[doc-name].md` — [Description]
```

## Command Wrapper Template

```markdown
---
description: [One-sentence description matching the skill purpose]
argument-hint: "[what the user should provide]"
---

Run the `[skill-name]` skill. [Brief instruction on what the skill does with the provided argument.]
```

## File Structure Rules

All new skills must follow this directory layout:

```
skills/
  <skill-name>/
    SKILL.md              # Required: Skill definition
    references/           # Optional: Supporting reference documents
      <ref-name>.md
    scripts/              # Optional: Validation or utility scripts
      <script-name>.py
```

## Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| **Skill directory** | kebab-case | `tailings-risk-assessment` |
| **SKILL.md** | Always uppercase | `SKILL.md` |
| **Command file** | kebab-case, matches skill | `tailings-risk.md` |
| **Reference docs** | kebab-case, descriptive | `dam-failure-modes.md` |
| **Python scripts** | snake_case | `calculate_stability.py` |
| **Frontmatter name** | Title Case | `"Tailings Risk Assessment"` |

## Checklist for New Skills

Before finalising a new skill, verify:

- [ ] SKILL.md has valid YAML frontmatter with `name` and `description`
- [ ] Purpose section clearly states what the skill does
- [ ] Workflow has 3-7 well-defined steps
- [ ] Output format is specified with example tables
- [ ] Data sources reference valid MCP connectors from `.mcp.json`
- [ ] Command wrapper created in `commands/`
- [ ] Command wrapper frontmatter has `description` and `argument-hint`
- [ ] `plugin.json` updated with new skill and command paths
- [ ] Reference docs added if the skill requires domain-specific standards
- [ ] Naming conventions followed throughout
