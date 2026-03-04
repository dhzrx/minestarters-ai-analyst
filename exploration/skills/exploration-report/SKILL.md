---
name: Exploration Report
description: Generate structured exploration stage reports for mining projects compiling drilling, geology, and resource potential.
---

# Exploration Report Generator

## Purpose

Compile exploration results into a structured, investor-ready report covering project overview, exploration history, geological setting, drilling results, resource potential, and forward program.

## Inputs

- **Project name and location**
- **Exploration data**: Drill results, geochemical surveys, geophysical surveys
- **Tenement details**: License numbers, area, expiry dates
- **Budget information** (if available)

## Workflow

### Step 1: Project Overview
- Location, access, infrastructure
- Tenement status and ownership
- Exploration history timeline
- Previous resource estimates (if any)

### Step 2: Geological Summary
- Regional and local geology
- Mineralization style and controls
- Target deposit model

### Step 3: Exploration Results
- Summary of all exploration activities
- Key drill intercepts (invoke `drill-results` skill if raw data available)
- Geochemical anomalies
- Geophysical survey interpretations
- Maps and cross-sections (describe or reference)

### Step 4: Resource Potential Assessment
- Estimated exploration target range (tonnes and grade)
- Comparison to analogous deposits
- Confidence level assessment
- Factors that could upgrade or downgrade potential

### Step 5: Forward Program & Budget
- Recommended next phase of exploration
- Drill targets and proposed hole locations
- Estimated costs by activity
- Timeline and milestones
- Key decision points (go/no-go criteria)

## Output Format

```
# Exploration Report — [Project Name]
## Date: [Date]

### 1. Executive Summary
[One paragraph summary of key findings and recommendations]

### 2. Project Overview
[Location, tenure, history]

### 3. Geological Setting
[Regional and local geology, mineralization model]

### 4. Exploration Results
[Detailed results with tables and descriptions]

### 5. Resource Potential
[Exploration target estimate with supporting rationale]

### 6. Forward Program
| Activity | Description | Cost Estimate | Timeline |
|----------|-------------|--------------|----------|
| ...      | ...         | ...          | ...      |

### 7. Risks and Mitigations
[Key risks and how they will be addressed]

### 8. Conclusions and Recommendations
[Key conclusions and clear recommendations]
```

## Compliance Note

This report template aligns with JORC Table 1 reporting requirements. Ensure all material exploration results are reported with appropriate context and qualifications.
