---
name: Vault Report
description: Generate comprehensive vault performance reports covering NAV history, returns, distributions, and forward outlook.
---

# Vault Performance Report

## Purpose

Generate periodic performance reports for Minestarters vaults, covering investment returns, underlying project updates, distribution history, and forward-looking outlook.

## Report Sections

### 1. Executive Summary
- Vault name, inception date, current AUM
- Period return (MTD, QTD, YTD, since inception)
- Key events and highlights
- NAV per token current vs. inception

### 2. Performance Analysis
- NAV chart (inception to date)
- Period returns table (monthly)
- Comparison to benchmarks (commodity indices, mining ETFs)
- Risk-adjusted metrics: Sharpe ratio, Sortino ratio, max drawdown
- Volatility (annualized)

### 3. Holdings Review
- Current portfolio composition with weights
- Individual project performance attribution
- Material project updates (resource upgrades, feasibility milestones, production starts)
- Watch list items (projects with elevated risk)

### 4. Distribution History
- Distributions paid (dates, amounts, type: income vs. return of capital)
- Distribution yield (trailing 12 months)
- Next expected distribution date and estimated amount

### 5. Market Commentary
- Relevant commodity price movements
- Mining sector developments
- Regulatory or policy changes affecting holdings
- Macro factors (interest rates, currency, inflation)

### 6. Forward Outlook
- Expected catalysts for each holding
- Upcoming milestones (drill results, studies, construction, production)
- Risk factors to monitor
- Rebalancing considerations

## Workflow

### Step 1: Gather Data
- NAV history from tracking system
- Project-level updates from announcements
- Commodity price data
- Distribution records

### Step 2: Calculate Performance
- Time-weighted returns (TWR) for each period
- Risk metrics calculation
- Benchmark comparison
- Attribution analysis

### Step 3: Compile Report
- Structure per sections above
- Include relevant charts and tables
- Write commentary connecting data to narrative
- Highlight actionable insights

## Output Format

```
# Vault Performance Report — [Vault Name]
## Period: [Start Date] to [End Date]

### Executive Summary
[2-3 paragraph overview]

### Performance
| Period | Return | Benchmark | Alpha |
|--------|--------|-----------|-------|
| MTD    | X.XX%  | X.XX%     | +X.XX% |
| QTD    | X.XX%  | X.XX%     | +X.XX% |
| YTD    | X.XX%  | X.XX%     | +X.XX% |
| Since Inception | X.XX% | X.XX% | +X.XX% |

### Risk Metrics
| Metric | Value |
|--------|-------|
| Annualized Volatility | XX% |
| Sharpe Ratio | X.XX |
| Max Drawdown | -XX% |
| Current Drawdown | -XX% |

### Holdings
[Table with project details and attribution]

### Distributions
[History table and yield metrics]

### Outlook
[Forward-looking commentary]
```
