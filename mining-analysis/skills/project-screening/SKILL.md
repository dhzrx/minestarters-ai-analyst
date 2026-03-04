---
name: "Project Screening"
description: "Screen and qualify mining projects against investment criteria using a weighted scorecard covering resource quality, jurisdiction, ESG, management, and financial metrics."
---

# Project Screening

## Purpose

Evaluate one or more mining projects against defined investment criteria to identify the most attractive opportunities. This skill produces a ranked scorecard that enables rapid comparison and go/no-go decisions for further due diligence.

## Screening Criteria

Each criterion is scored 1-5 (1 = poor, 5 = excellent) and weighted by importance.

### 1. Resource Quality (Weight: 25%)

| Score | Grade Relative to Peers | Tonnage | Classification |
|-------|------------------------|---------|----------------|
| 5 | Top quartile | Large (>50Mt or equivalent) | Majority Measured + Indicated |
| 4 | Above average | Moderate-Large | Significant M+I |
| 3 | Average | Moderate | Mixed M+I and Inferred |
| 2 | Below average | Small | Majority Inferred |
| 1 | Bottom quartile | Very small | Entirely Inferred or exploration target |

Sub-criteria:
- **Grade**: Compared to global cost curves for the commodity
- **Tonnage**: Sufficient to support economic mine life
- **Classification level**: Higher confidence = lower risk
- **Mineralogy**: Simple (oxide) vs complex (refractory, polymetallic)
- **Metallurgical recovery**: Demonstrated through testwork

### 2. Jurisdiction (Weight: 20%)

| Score | Political Risk | Mining Code | Permitting | Precedent |
|-------|---------------|-------------|-----------|-----------|
| 5 | Very low (Tier 1) | Stable, transparent | Streamlined | Many successful mines |
| 4 | Low | Generally stable | Moderate timeline | Good precedent |
| 3 | Moderate | Some uncertainty | Complex process | Limited precedent |
| 2 | High | Recent adverse changes | Lengthy / uncertain | Few precedents |
| 1 | Very high | Unstable / hostile | Expropriation risk | No precedent |

Sub-criteria:
- **Political stability**: Governance indices, history of mining policy changes
- **Legal framework**: Mining code clarity, title security, arbitration access
- **Permitting timeline**: Typical time from application to approval
- **Fiscal regime**: Tax rates, royalties, windfall taxes
- **Repatriation of funds**: Currency controls, dividend restrictions

### 3. ESG Score (Weight: 15%)

| Score | Environmental | Social | Governance |
|-------|-------------|--------|-----------|
| 5 | Low impact, strong mitigation | Community support, no conflicts | Transparent, experienced board |
| 4 | Manageable impact | Generally positive relations | Good governance |
| 3 | Moderate issues, plans in place | Mixed community response | Adequate governance |
| 2 | Significant issues | Opposition or unresolved disputes | Governance concerns |
| 1 | Major environmental liabilities | Active conflict or litigation | Poor governance |

Sub-criteria:
- **Water management**: Availability, competing uses, treatment requirements
- **Biodiversity**: Protected areas, endangered species, offset requirements
- **Community relations**: Social licence, benefit sharing, employment
- **Climate / emissions**: Carbon footprint, decarbonisation pathway
- **Tailings management**: Storage method, facility stability, closure plan

### 4. Management Quality (Weight: 15%)

| Score | Track Record | Technical Team | Capital Markets |
|-------|-------------|----------------|-----------------|
| 5 | Multiple successful mine builds | Deep bench, CP/QP on team | Strong institutional backing |
| 4 | Proven operators | Experienced team | Good market access |
| 3 | Mixed record | Adequate expertise | Moderate market presence |
| 2 | Limited track record | Thin team | Limited market access |
| 1 | No mining experience | Inadequate expertise | No institutional support |

### 5. Financial Metrics (Weight: 15%)

| Score | NPV/CAPEX Ratio | IRR | Payback |
|-------|-----------------|-----|---------|
| 5 | > 2.0x | > 30% | < 3 years |
| 4 | 1.5-2.0x | 20-30% | 3-4 years |
| 3 | 1.0-1.5x | 15-20% | 4-5 years |
| 2 | 0.5-1.0x | 10-15% | 5-7 years |
| 1 | < 0.5x | < 10% | > 7 years |

### 6. Infrastructure (Weight: 5%)

- Proximity to power, water, roads, rail, port
- Availability of skilled labour
- Existing vs greenfield infrastructure requirements

### 7. Mine Life (Weight: 5%)

| Score | Mine Life |
|-------|-----------|
| 5 | > 20 years |
| 4 | 15-20 years |
| 3 | 10-15 years |
| 2 | 5-10 years |
| 1 | < 5 years |

## Workflow

### Step 1: Define Screening Parameters

- Set minimum thresholds (hard gates) for critical criteria
- Confirm weighting scheme (defaults above, adjustable per mandate)
- Identify target commodities and geographies

### Step 2: Gather Project Data

- Source resource estimates, technical reports, company presentations
- Collect jurisdiction data (mining code, political risk indices)
- Review ESG disclosures, community agreements, environmental assessments
- Assess management bios, track records, institutional shareholder registers

### Step 3: Score Each Criterion

- Apply scoring rubric (1-5) to each sub-criterion
- Calculate weighted sub-criterion scores
- Flag any hard-gate failures (automatic disqualification)

### Step 4: Aggregate and Rank

```
Total Score = SUM(Criterion Score x Weight) for all criteria
Maximum possible = 5.0
```

### Step 5: Generate Scorecard

Produce a ranked comparison table with colour coding:

| Rank | Project | Resource | Jurisdiction | ESG | Management | Financial | Infrastructure | Mine Life | **Total** |
|------|---------|----------|-------------|-----|-----------|-----------|---------------|-----------|-----------|
| 1 | Project A | 4.2 | 4.5 | 3.8 | 4.0 | 4.5 | 4.0 | 5.0 | **4.21** |
| 2 | Project B | 3.8 | 4.0 | 4.2 | 3.5 | 3.8 | 3.0 | 4.0 | **3.82** |

## Output Format

1. **Ranked scorecard table** as above
2. **Individual project profiles** with detailed scoring rationale
3. **Hard-gate pass/fail summary**
4. **Key risks and opportunities** for top-ranked projects
5. **Recommendation** for further due diligence or rejection

## Data Sources

- Resource estimation skill output
- Mineral valuation skill output
- SEC EDGAR, ASX announcements (company filings)
- S&P Global, Mining.com (industry data)
- Fraser Institute Survey of Mining Companies (jurisdiction ranking)
- Company websites, investor presentations, technical reports
