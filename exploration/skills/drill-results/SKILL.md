---
name: Drill Results Analysis
description: Analyze drill hole data and assay results to identify significant mineralization intercepts and inform resource estimation.
---

# Drill Results Analysis

## Purpose

Interpret drill hole data including collar coordinates, downhole surveys, lithology logs, and assay results to identify significant mineralization intercepts and assess geological continuity.

## Inputs

- **Drill hole collar data**: Hole ID, easting, northing, elevation, azimuth, dip, depth
- **Assay results**: From/to intervals, element grades (e.g., Au g/t, Cu %, Li2O %)
- **Lithology logs**: Rock types, alteration, mineralization descriptions
- **Previous drill results** (if available): For comparison and trend analysis

## Workflow

### Step 1: Data Validation
- Check for missing or duplicate hole IDs
- Validate collar coordinates are within project boundary
- Check for assay interval overlaps or gaps
- Flag anomalous values (negative grades, extreme outliers)

### Step 2: Significant Intercepts
- Calculate composite intercepts using appropriate cut-off grades by commodity:
  - **Gold**: 0.3-0.5 g/t cut-off (open pit), 2-3 g/t (underground)
  - **Copper**: 0.2-0.3% cut-off (open pit), 0.5-1.0% (underground)
  - **Lithium**: 0.5-1.0% Li2O cut-off
  - **Nickel**: 0.3-0.5% Ni cut-off
- Allow maximum 2m internal dilution for compositing
- Report as: "X.Xm @ Y.Y g/t Au from Zm depth (Hole ID)"

### Step 3: Grade Distribution Analysis
- Generate grade histograms and statistics (mean, median, CV, top cuts)
- Identify high-grade zones vs. bulk-tonnage mineralization
- Assess grade continuity between holes

### Step 4: Geological Interpretation
- Correlate mineralization with lithology and alteration
- Identify structural controls on mineralization
- Assess deposit geometry (thickness, dip, strike extent)
- Determine mineralization style (vein, disseminated, massive sulphide, etc.)

### Step 5: Recommendations
- Identify areas requiring infill drilling
- Suggest optimal drill spacing for resource classification upgrade
- Recommend step-out targets for resource extension
- Estimate confidence level of current data

## Output Format

```
## Drill Results Summary — [Project Name]

### Key Intercepts
| Hole ID | From (m) | To (m) | Width (m) | Grade | Commodity |
|---------|----------|--------|-----------|-------|-----------|
| ...     | ...      | ...    | ...       | ...   | ...       |

### Statistics
- Total holes analyzed: X
- Average intercept grade: X.X
- Maximum intercept: X.Xm @ Y.Y from Zm
- Coefficient of variation: X.X

### Geological Model
[Description of mineralization controls and geometry]

### Recommendations
1. [Infill drilling targets]
2. [Step-out targets]
3. [Additional data needs]
```

## Data Sources

- Company drill result announcements (ASX, SEDAR, SEC EDGAR)
- Technical reports (NI 43-101, JORC)
- Use web search for latest drilling announcements

## References

See `references/assay-interpretation.md` and `references/drill-spacing.md` for detailed guidance.
