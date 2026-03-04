---
name: Portfolio Rebalance
description: Generate rebalancing signals, trade lists, and execution plans for mining baskets with cost-aware optimization.
---

# Portfolio Rebalance

## Purpose

Monitor mining basket allocations against target weights, identify drift, and generate optimized rebalancing trade lists considering transaction costs, liquidity, and tax implications.

## Rebalancing Triggers

| Trigger | Description |
|---------|-------------|
| **Calendar** | Quarterly scheduled rebalance |
| **Drift** | Any single holding drifts >5% from target weight |
| **Event** | Material project event (production start, resource update, delisting) |
| **Risk** | Portfolio risk metrics breach thresholds |
| **Redemption** | Investor redemption requiring cash raise |

## Workflow

### Step 1: Calculate Current vs. Target Allocations
- Retrieve current holdings and market values (invoke `nav-tracking`)
- Compare current weights to target weights
- Calculate absolute drift for each holding

### Step 2: Determine Rebalancing Need
- Check if any trigger conditions are met
- Calculate total portfolio turnover required
- Estimate transaction costs (token trading spread + gas fees)
- Determine if rebalancing benefit exceeds costs

### Step 3: Generate Trade List
- Calculate required buy/sell amounts per holding
- Prioritize trades by: drift magnitude, liquidity, cost efficiency
- Apply minimum trade size filter (avoid dust trades)
- Consider tax-loss harvesting opportunities

### Step 4: Liquidity Check
- Assess available liquidity for each token
- Estimate market impact for large trades
- Spread large orders over time if needed
- Identify tokens requiring OTC execution

### Step 5: Execution Plan
- Order trades by dependency (sells before buys if cash-constrained)
- Set limit prices or TWAP parameters
- Define execution timeline
- Set fail-safe conditions (max slippage, price limits)

## Output Format

```
## Rebalancing Report — [Basket Name]
### Date: [Date]
### Trigger: [Calendar/Drift/Event/Risk]

### Drift Analysis
| Project | Target % | Current % | Drift | Action |
|---------|----------|-----------|-------|--------|
| ...     | XX%      | XX%       | +X.X% | Sell   |
| ...     | XX%      | XX%       | -X.X% | Buy    |

### Trade List
| # | Action | Project | Amount ($) | Est. Cost | Priority |
|---|--------|---------|-----------|-----------|----------|
| 1 | Sell   | ...     | $XXX      | $X.XX     | High     |
| 2 | Buy    | ...     | $XXX      | $X.XX     | High     |

### Cost Summary
- Total turnover: $XXX (XX% of NAV)
- Estimated transaction costs: $XX (X.XX% of NAV)
- Net benefit of rebalancing: $XX

### Execution Plan
[Timeline and order of execution]
```
