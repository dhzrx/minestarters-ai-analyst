---
name: NAV Tracking
description: Calculate and track on-chain Net Asset Value for mining baskets and vaults with attribution analysis.
---

# NAV Tracking

## Purpose

Calculate the Net Asset Value (NAV) of mining baskets and vaults on the Minestarters platform. Track NAV changes over time and provide attribution analysis explaining value drivers.

## NAV Calculation Method

### Per-Token NAV
```
NAV = (Sum of [Project_i Token Price x Quantity_i] + Cash Holdings - Liabilities) / Total Basket Tokens Outstanding
```

### Project Valuation Inputs
For each project in the basket:
1. **Market price**: Latest token trading price (if liquid market exists)
2. **Fair value estimate**: NPV-based valuation (invoke `mineral-valuation` skill)
3. **Reserve/resource updates**: Adjust for material changes in resource estimates
4. **Commodity price impact**: Mark-to-market based on underlying commodity prices

### NAV Adjustment Events
| Event | Impact | Frequency |
|-------|--------|-----------|
| Commodity price change | Direct, proportional | Daily |
| Resource estimate update | Revaluation | Quarterly or on announcement |
| Feasibility study release | Step-change revaluation | On release |
| Production start/stop | Major revaluation | On event |
| Token distribution/dividend | NAV reduction | Per schedule |
| Rebalancing trade | Neutral (plus/minus transaction costs) | Per policy |

## Workflow

### Step 1: Gather Current Data
- Current token prices for all basket holdings
- Latest commodity prices for relevant minerals
- Any recent material announcements (resource updates, feasibility studies)
- Cash/stablecoin balance in vault

### Step 2: Calculate Component Values
- Value each holding: tokens x price
- Apply fair value adjustments where market price is stale or illiquid
- Sum component values plus cash minus liabilities

### Step 3: Attribution Analysis
- Decompose NAV change into: commodity price effect, project-specific events, rebalancing costs, fees
- Identify largest positive and negative contributors

### Step 4: Track and Report
- Record NAV with timestamp (on-chain if applicable)
- Compare to previous NAV calculation
- Calculate period return (daily, weekly, monthly)
- Generate trend chart data

## Output Format

```
## NAV Report — [Basket/Vault Name]
### As of: [Date/Time]

### Current NAV: $X.XXXX per token
### Previous NAV: $X.XXXX ([date])
### Period Return: +X.XX%

### Holdings Breakdown
| Project | Tokens | Price | Value ($) | % of NAV | Change |
|---------|--------|-------|-----------|----------|--------|
| ...     | ...    | ...   | ...       | ...      | ...    |
| Cash    | —      | —     | $XXX      | X%       | —      |
| **Total** | — | — | **$XXX** | **100%** | — |

### Attribution
| Driver | Impact ($) | Impact (%) |
|--------|-----------|------------|
| Gold price +2.1% | +$XXX | +X.XX% |
| Project A resource update | +$XXX | +X.XX% |
| Management fee | -$XX | -X.XX% |
| **Net Change** | **+$XXX** | **+X.XX%** |
```
