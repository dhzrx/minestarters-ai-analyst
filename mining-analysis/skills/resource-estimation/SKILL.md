---
name: "Resource Estimation"
description: "Classify mineral resources (Measured/Indicated/Inferred) and reserves (Proved/Probable) per JORC Code 2012 and NI 43-101 standards using drill data, assay results, and geological modelling."
---

# Resource Estimation

## Purpose

Estimate and classify mineral resources and reserves for mining projects in compliance with internationally recognized reporting codes. This skill takes raw geological data (drill hole intercepts, assay results, geological mapping) and produces a resource statement suitable for public disclosure and investment decision-making.

## Resource and Reserve Categories

### Resources (increasing geological confidence)

| Category | Confidence | Typical Evidence |
|----------|-----------|------------------|
| **Inferred** | Low — sufficient to imply but not verify continuity | Wide-spaced drilling, limited data |
| **Indicated** | Reasonable — adequate for mine planning at PFS level | Moderate drill spacing, demonstrated continuity |
| **Measured** | High — sufficient for detailed mine planning and final feasibility | Close-spaced drilling, well-understood geology |

### Reserves (resources modified by mining, metallurgical, economic, and other factors)

| Category | Derived From | Requirements |
|----------|-------------|--------------|
| **Probable** | Indicated Resources | Positive feasibility study, modifying factors applied |
| **Proved** | Measured Resources | Positive feasibility study, modifying factors applied |

## Workflow

### Step 1: Collect Drill Data and Assay Results

- Gather drill hole collar coordinates, downhole surveys, and lithological logs
- Collect assay results for target elements (e.g., Au g/t, Cu %, Li2O %)
- Validate data quality: QAQC results (standards, blanks, duplicates)
- Flag any data gaps or suspect assays

### Step 2: Analyse Geological Continuity

- Interpret geological domains (lithology, alteration, structural controls)
- Create wireframe models of mineralised zones
- Assess grade continuity using variography (semi-variograms by domain)
- Determine appropriate search ellipse parameters and estimation block sizes

### Step 3: Apply Estimation Methods

Select the appropriate method based on data density and deposit style:

- **Ordinary Kriging (OK)**: Preferred for deposits with well-understood variography and sufficient data density. Provides local estimates with minimised estimation variance.
- **Inverse Distance Weighting (IDW)**: Suitable when variography is unreliable or data is sparse. Uses distance-weighted averaging with a power of 2 or 3.
- **Polygonal / Nearest Neighbour**: Used for early-stage projects with very wide drill spacing. Assigns block grades from the nearest sample.
- **Multiple Indicator Kriging (MIK)**: Useful for highly skewed grade distributions (e.g., gold). Estimates grade probability distributions.

### Step 4: Classify Resources per JORC / NI 43-101

Apply classification criteria based on:

- **Drill spacing**: Compare actual spacing to commodity-specific guidelines (see `references/classification-guide.md`)
- **Data quality**: QAQC pass rates, sample representativeness
- **Geological confidence**: Continuity of mineralisation between drill holes
- **Estimation quality**: Slope of regression, kriging efficiency, conditional bias checks

### Step 5: Generate Resource Statement

Produce a resource table in standard format:

| Category | Tonnes (Mt) | Grade | Contained Metal |
|----------|-------------|-------|-----------------|
| Measured | X.X | X.X g/t Au | X,XXX oz |
| Indicated | X.X | X.X g/t Au | X,XXX oz |
| M+I Subtotal | X.X | X.X g/t Au | X,XXX oz |
| Inferred | X.X | X.X g/t Au | X,XXX oz |

Include:
- Effective date of the estimate
- Cut-off grade and basis for selection
- Bulk density assumptions
- Competent Person / Qualified Person statement
- Any material assumptions or caveats

## Output Format

The final resource statement should include:

1. **Summary table** as shown above
2. **Cut-off grade justification** with supporting economic parameters
3. **Classification rationale** explaining the basis for each category
4. **Data quality summary** covering QAQC and data validation
5. **Comparison with previous estimates** (if applicable) highlighting material changes
6. **Competent Person / Qualified Person declaration**

## References

- `references/jorc-code.md` — JORC Code 2012 key provisions
- `references/ni-43-101.md` — NI 43-101 Canadian disclosure standard
- `references/classification-guide.md` — Practical classification guidelines by commodity

## Data Sources

- **USGS Mineral Resources Data System** (`usgs-mineral-data`): Geological data, deposit databases
- **SEC EDGAR** (`sec-edgar`): US mining company technical reports and filings
- **ASX Announcements** (`asx-announcements`): Australian mining company resource disclosures
- **S&P Global** (`sp-global-mining`): Project-level resource data (subscription required)
