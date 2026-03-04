---
name: Basket Builder
description: Construct diversified mining investment baskets with defined allocation strategies, risk profiles, and mineral/geography exposure targets.
---

# Basket Builder

## Purpose

Construct diversified baskets of tokenized mining assets for the Minestarters platform. Each basket represents a curated portfolio of mining project tokens with defined allocation percentages, risk parameters, and exposure targets.

## Basket Types

| Type | Risk Profile | Min Projects | Target IRR | Typical Investor |
|------|-------------|-------------|------------|-----------------|
| Conservative | Low | 8-12 | 8-12% | Institutional, pension |
| Balanced | Medium | 6-10 | 12-18% | Family offices, HNWI |
| Aggressive | High | 4-8 | 18-30%+ | Venture, speculative |
| Thematic | Varies | 4-8 | Varies | ESG-focused, sector bets |

## Allocation Constraints

### Diversification Rules
- **Single project max**: 20% (conservative), 30% (balanced), 40% (aggressive)
- **Single commodity max**: 40% (conservative), 50% (balanced), 70% (aggressive)
- **Single country max**: 35% (conservative), 50% (balanced), 70% (aggressive)
- **Single stage max**: 50% (must mix producing + development + exploration)
- **Minimum projects**: As per basket type table above

### Stage Allocation Guidelines
| Stage | Conservative | Balanced | Aggressive |
|-------|-------------|----------|------------|
| Producing | 60-80% | 40-60% | 10-30% |
| Development | 15-30% | 25-40% | 20-40% |
| Exploration | 0-10% | 10-20% | 30-60% |

## Workflow

### Step 1: Define Investment Thesis
- Target commodity exposure (e.g., "battery metals", "precious metals", "critical minerals")
- Risk profile (conservative/balanced/aggressive)
- Minimum investment size (determines eligible projects)
- Geographic preferences or restrictions
- ESG minimum score threshold

### Step 2: Screen Eligible Projects
- Filter projects meeting minimum criteria (invoke `project-screening` skill if needed)
- Assess liquidity (token trading volume, lock-up periods)
- Check project stage and timeline compatibility
- Verify data availability for valuation

### Step 3: Optimize Allocation
- Score each project on: risk-adjusted return, diversification contribution, liquidity, ESG
- Apply allocation constraints
- Optimize for maximum Sharpe ratio (or target return at minimum risk)
- Run Monte Carlo simulation for return distribution

### Step 4: Generate Basket Specification
- Project list with allocation percentages
- Risk metrics: expected return, volatility, max drawdown, Sharpe ratio
- Exposure breakdown: by commodity, country, stage, ESG score
- Minimum capital requirement
- Rebalancing frequency and triggers

## Output Format

```
## Basket Specification — [Basket Name]
### Type: [Conservative/Balanced/Aggressive/Thematic]
### Theme: [Investment thesis]

### Holdings
| Project | Commodity | Country | Stage | Allocation | Expected Return |
|---------|-----------|---------|-------|------------|----------------|
| ...     | ...       | ...     | ...   | XX%        | XX%            |

### Exposure Analysis
| Dimension | Breakdown |
|-----------|-----------|
| Commodity | Au 30%, Cu 25%, Li 20%, ... |
| Geography | Australia 35%, Canada 25%, ... |
| Stage | Producing 50%, Development 30%, Exploration 20% |

### Risk Metrics
| Metric | Value |
|--------|-------|
| Expected Annual Return | XX% |
| Expected Volatility | XX% |
| Sharpe Ratio | X.XX |
| Max Drawdown (est.) | XX% |

### Parameters
- Minimum Investment: $XXX,XXX
- Rebalancing: Quarterly / on 5% drift threshold
- Management Fee: X.XX%
- Performance Fee: XX% above hurdle
```

## References

See `references/allocation-strategies.md` and `references/risk-profiles.md`.
