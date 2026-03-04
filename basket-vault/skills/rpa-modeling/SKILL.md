---
name: RPA Modeling
description: Model Revenue Participation Agreement cash flows including revenue triggers, participation rates, waterfall distributions, and investor return scenarios.
---

# RPA (Revenue Participation Agreement) Modeling

## Purpose

Model the cash flow mechanics of Revenue Participation Agreements used by Minestarters to structure mining project investments. RPAs give token holders the right to a percentage of project revenue.

## RPA Structure

### Key Terms
| Term | Description | Typical Range |
|------|-------------|---------------|
| **Revenue Participation Rate** | % of gross revenue paid to RPA holders | 1-5% |
| **Effective Date** | When revenue sharing begins | Production start or first commercial shipment |
| **Duration** | Length of RPA | Mine life or fixed term (10-25 years) |
| **Minimum Revenue Threshold** | Revenue below which no distribution occurs | Breakeven or $0 |
| **Cap** | Maximum total distributions (multiple of investment) | 2-5x investment |
| **Waterfall Priority** | Payment priority vs. other obligations | Senior to equity, junior to debt |

### Cash Flow Waterfall
```
Gross Revenue
  └─ Operating Costs → Net Operating Income
      └─ Debt Service (senior)
          └─ RPA Distribution (participation rate x gross revenue)
              └─ Sustaining Capex
                  └─ Taxes & Royalties
                      └─ Equity Returns (residual)
```

## Workflow

### Step 1: Define RPA Terms
- Participation rate
- Duration / expiry conditions
- Cap (if any)
- Minimum thresholds
- Payment frequency (monthly/quarterly)

### Step 2: Build Production & Revenue Model
- Annual production schedule (from mine plan or feasibility study)
- Commodity price assumptions (Bear/Base/Bull)
- Revenue calculation: production x price x recovery rate
- Apply any contractual price adjustments

### Step 3: Calculate RPA Distributions
- For each period: RPA distribution = max(0, Revenue - Threshold) x Participation Rate
- Apply cap if cumulative distributions reach limit
- Calculate distribution per token (total distribution / tokens outstanding)

### Step 4: Investor Return Analysis
- Calculate investor IRR at different price scenarios
- Calculate payback period
- Calculate total multiple on invested capital (MOIC)
- Compare to alternative investments (bond yields, mining equity returns)

### Step 5: Sensitivity Analysis
- Sensitivity to commodity price (plus/minus 20%, plus/minus 40%)
- Sensitivity to production volume (plus/minus 10%, plus/minus 20%)
- Sensitivity to participation rate
- Sensitivity to mine life
- Break-even commodity price for target return

## Output Format

```
## RPA Model — [Project Name]

### RPA Terms
| Term | Value |
|------|-------|
| Participation Rate | X.X% |
| Duration | XX years |
| Cap | X.Xx investment |
| Minimum Threshold | $XX/unit |

### Projected Distributions (Base Case)
| Year | Revenue ($M) | RPA Distribution ($M) | Per Token ($) | Cumulative ($M) |
|------|-------------|----------------------|---------------|-----------------|
| 1    | ...         | ...                  | ...           | ...             |
| ...  | ...         | ...                  | ...           | ...             |

### Investor Returns by Scenario
| Scenario | Commodity Price | IRR | MOIC | Payback (yrs) |
|----------|----------------|-----|------|---------------|
| Bear     | $XX/unit       | XX% | X.Xx | XX            |
| Base     | $XX/unit       | XX% | X.Xx | XX            |
| Bull     | $XX/unit       | XX% | X.Xx | XX            |

### Sensitivity Matrix (IRR)
| Price \ Volume | -20% | Base | +20% |
|---------------|------|------|------|
| -20%          | XX%  | XX%  | XX%  |
| Base          | XX%  | XX%  | XX%  |
| +20%          | XX%  | XX%  | XX%  |
```

## References

See `scripts/rpa_calculator.py` for automated RPA cash flow calculations.
