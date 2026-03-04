---
name: Comparable Projects
description: Identify and analyze comparable mining projects for valuation benchmarking and competitive positioning.
---

# Comparable Project Analysis

## Purpose

Find and analyze mining projects comparable to a target project for valuation benchmarking. Extract key financial and operational metrics for comparison.

## Selection Criteria

Select comparable projects based on:
1. **Commodity**: Same primary commodity
2. **Deposit type**: Similar geology and mining method
3. **Stage**: Same development stage (exploration, development, production)
4. **Scale**: Similar resource/reserve tonnage (within 0.5x–2x)
5. **Jurisdiction**: Similar country risk (Tier 1/2/3 jurisdictions)
6. **Grade**: Similar head grade range

## Key Metrics for Comparison

### Pre-Production Projects
| Metric | Description |
|--------|-------------|
| EV/Resource oz (or lb, t) | Enterprise value per unit of total resource |
| EV/Reserve oz | Enterprise value per unit of reserve |
| Initial Capex | Total initial capital cost |
| Capex/annual tonne | Capital intensity |
| NPV (8%) | Net present value at 8% discount |
| IRR | Internal rate of return |
| Payback | Payback period in years |
| AISC (projected) | Projected all-in sustaining cost |

### Producing Mines
| Metric | Description |
|--------|-------------|
| EV/EBITDA | Enterprise value to EBITDA |
| P/NAV | Price to net asset value |
| EV/Production | Enterprise value per unit of annual production |
| AISC | All-in sustaining cost |
| Cash cost | C1 cash cost per unit |
| Reserve life | Years of remaining reserves |
| FCF yield | Free cash flow yield |

## Workflow

### Step 1: Identify Peer Group
- Search for projects with matching criteria
- Target 5-10 comparable projects
- Sources: SEC EDGAR, ASX, TSX/SEDAR, company websites

### Step 2: Data Extraction
- Extract metrics from latest technical reports and financial statements
- Normalize to common units and currency (USD)
- Note date of data for each project

### Step 3: Analysis
- Calculate median, mean, and range for each metric
- Position target project relative to peers
- Identify premium/discount to peer averages
- Explain outliers

### Step 4: Implied Valuation
- Apply peer median multiples to target project metrics
- Calculate implied valuation range
- Cross-check with NPV-based valuation

## Output Format

```
## Comparable Projects — [Target Project]

### Peer Group
| Project | Company | Commodity | Stage | Resource | Grade |
|---------|---------|-----------|-------|----------|-------|
| ...     | ...     | ...       | ...   | ...      | ...   |

### Metric Comparison
| Metric | Target | Peer Median | Peer Range | Percentile |
|--------|--------|-------------|------------|------------|
| ...    | ...    | ...         | ...        | ...        |

### Implied Valuation
| Method | Low | Mid | High |
|--------|-----|-----|------|
| EV/Resource | $XM | $XM | $XM |
| EV/Reserve | $XM | $XM | $XM |

### Key Observations
[What explains the target's premium or discount to peers]
```
