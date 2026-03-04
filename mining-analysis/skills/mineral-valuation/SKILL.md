---
name: "Mineral Valuation"
description: "Value mining projects using NPV/IRR/DCF methodology with Bear/Base/Bull commodity price scenarios, mining-specific cost inputs, and sensitivity analysis."
---

# Mineral Valuation

## Purpose

Perform discounted cash flow (DCF) valuation of mining projects and mineral deposits. This skill builds a full financial model from resource estimates through to NPV, IRR, and payback period, incorporating mining-specific parameters such as strip ratio, metallurgical recovery, and staged capital deployment.

## Required Inputs

| Input | Description | Typical Source |
|-------|-------------|---------------|
| **Resource/Reserve estimate** | Tonnes and grade by category | Resource estimation skill output |
| **Commodity prices** | Current spot, forward curve, long-term consensus | LME, Kitco, broker consensus |
| **Mining method** | Open pit, underground, or combined | Technical study |
| **Strip ratio** | Waste-to-ore ratio (open pit) | Mine plan |
| **Recovery rate** | Metallurgical recovery (%) | Testwork / feasibility study |
| **Mine life** | Years of production | Reserve / production schedule |
| **CAPEX** | Initial and sustaining capital | Feasibility study or analogues |
| **OPEX** | Mining, processing, G&A costs per tonne | Feasibility study or cost curves |
| **Royalties** | Government and private royalties (%) | Jurisdiction / agreements |
| **Tax rate** | Corporate tax rate | Jurisdiction |
| **Discount rate (WACC)** | Weighted average cost of capital | See `references/discount-rates.md` |

## Workflow

### Step 1: Define Commodity Price Scenarios

Establish three price scenarios for each commodity:

| Scenario | Basis | Typical Approach |
|----------|-------|------------------|
| **Bear** | Downside case | 10th-25th percentile of analyst forecasts or cost-curve support |
| **Base** | Most likely case | Median analyst consensus or forward curve |
| **Bull** | Upside case | 75th-90th percentile of analyst forecasts |

### Step 2: Build Production Schedule

- Convert resources/reserves to annual production (tonnes mined, tonnes processed, metal produced)
- Apply mining dilution and ore loss factors
- Apply metallurgical recovery rates
- Account for ramp-up and ramp-down periods
- Include stockpile management if relevant

### Step 3: Calculate Revenue

```
Annual Revenue = Metal Produced x Commodity Price
               - Treatment/Refining Charges (TC/RC)
               - Transport and Insurance
```

### Step 4: Calculate Operating Costs

- Mining cost per tonne (ore + waste)
- Processing cost per tonne of ore
- General and administrative (G&A) costs
- Apply escalation factors where appropriate
- Reference cost curves for reasonableness (see `references/cost-curves.md`)

### Step 5: Calculate Capital Costs

- Initial CAPEX (pre-production)
- Sustaining CAPEX (annual maintenance and replacement)
- Expansion CAPEX (if staged development)
- Closure and rehabilitation costs
- Working capital requirements

### Step 6: Apply Taxes and Royalties

- Government royalties (ad valorem or profit-based)
- Private royalties (NSR, NPI, or other)
- Corporate income tax with depreciation and loss carry-forward
- Withholding taxes on dividends (if relevant)

### Step 7: Calculate NPV and IRR

- Construct annual free cash flow (FCF) schedule
- Apply discount rate to calculate NPV (use `scripts/validate_npv.py` for verification)
- Solve for IRR (rate at which NPV = 0)
- Calculate simple and discounted payback periods

### Step 8: Run Sensitivity Analysis

Vary key inputs independently to assess impact on NPV:

| Variable | Range | Typical Steps |
|----------|-------|---------------|
| Commodity price | +/- 30% | 5 steps |
| Grade | +/- 20% | 5 steps |
| CAPEX | +/- 25% | 5 steps |
| OPEX | +/- 25% | 5 steps |
| Recovery rate | +/- 10% | 5 steps |
| Discount rate | +/- 3% | 5 steps |

Generate tornado chart and spider diagram data.

## WACC Calculation

```
WACC = (E/V x Re) + (D/V x Rd x (1 - Tc))

Where:
  E = Market value of equity
  V = Total value (E + D)
  Re = Cost of equity (CAPM: Rf + Beta x ERP + CRP + SRP)
  D = Market value of debt
  Rd = Cost of debt
  Tc = Corporate tax rate

Mining-specific adjustments:
  CRP = Country risk premium (0-15% depending on jurisdiction)
  SRP = Size/stage risk premium (2-5% for juniors, 0-2% for majors)
```

See `references/discount-rates.md` for typical ranges by project stage.

## Output Format

The valuation output should include:

1. **Valuation summary table**

| Metric | Bear | Base | Bull |
|--------|------|------|------|
| NPV (pre-tax) | $X M | $X M | $X M |
| NPV (post-tax) | $X M | $X M | $X M |
| IRR (pre-tax) | X.X% | X.X% | X.X% |
| IRR (post-tax) | X.X% | X.X% | X.X% |
| Payback (years) | X.X | X.X | X.X |
| Peak funding | $X M | $X M | $X M |

2. **Annual cash flow schedule** (year-by-year detail)
3. **Sensitivity tables** for each variable
4. **Tornado chart data** showing NPV sensitivity ranking
5. **Key assumptions summary**
6. **Comparison to market valuation** (if public company)

## Validation

Use `scripts/validate_npv.py` to cross-check NPV, IRR, and payback calculations against model outputs. The script accepts cash flows as JSON input and returns independent calculations for comparison.

## References

- `references/discount-rates.md` — Mining discount rate guide by stage and jurisdiction
- `references/cost-curves.md` — Commodity cost curve benchmarks for reasonableness checks
