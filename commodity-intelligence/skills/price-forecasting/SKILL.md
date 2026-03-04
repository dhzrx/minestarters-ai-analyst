---
name: Price Forecasting
description: Analyze commodity price trends and generate multi-scenario price forecasts for mining commodities.
---

# Commodity Price Forecasting

## Purpose

Generate informed price forecasts for mining commodities to support project valuation, investment decisions, and basket construction. Combines fundamental analysis, technical indicators, and analyst consensus.

## Supported Commodities

### Precious Metals
- Gold (Au) — $/troy oz
- Silver (Ag) — $/troy oz
- Platinum (Pt) — $/troy oz
- Palladium (Pd) — $/troy oz

### Base Metals
- Copper (Cu) — $/lb or $/tonne
- Zinc (Zn) — $/lb or $/tonne
- Nickel (Ni) — $/lb or $/tonne
- Lead (Pb) — $/lb or $/tonne
- Tin (Sn) — $/lb or $/tonne
- Aluminum (Al) — $/lb or $/tonne

### Battery & Critical Metals
- Lithium (Li) — $/tonne LCE or $/tonne spodumene concentrate
- Cobalt (Co) — $/lb or $/tonne
- Manganese (Mn) — $/tonne
- Graphite — $/tonne
- Rare Earth Elements — $/kg by element

### Bulk Commodities
- Iron Ore (Fe) — $/tonne (62% Fe CFR China)
- Metallurgical Coal — $/tonne
- Uranium (U3O8) — $/lb

## Workflow

### Step 1: Historical Analysis
- Gather 10-year price history
- Calculate key statistics: mean, median, standard deviation, percentiles
- Identify long-term trends (secular bull/bear cycles)
- Analyze price volatility patterns
- Identify correlation with macro indicators (USD index, real rates, PMI)

### Step 2: Fundamental Analysis
- **Supply factors**: Mine production, inventory levels, supply disruptions, pipeline projects
- **Demand factors**: End-use consumption, growth rates by sector, substitution effects
- **Market balance**: Current surplus/deficit, projected balance
- **Cost support**: Marginal cost of production (price floor indicator)
- **Inventory dynamics**: Exchange warehouse stocks, strategic reserves

### Step 3: Forward Curve & Consensus
- Check LME/COMEX forward curves (contango vs. backwardation)
- Gather analyst consensus forecasts (bank reports, industry surveys)
- Note divergence between forward curve and fundamental outlook
- Check options-implied volatility for market uncertainty

### Step 4: Scenario Construction
| Scenario | Probability | Methodology |
|----------|------------|-------------|
| Bear | 20-25% | Demand disappointment + supply growth + strong USD |
| Base | 50-60% | Consensus view, trend continuation |
| Bull | 20-25% | Supply disruption + demand acceleration + weak USD |

### Step 5: Forecast Generation
- Short-term (0-12 months): Weight forward curve and near-term fundamentals
- Medium-term (1-3 years): Weight supply/demand model and cost curves
- Long-term (3-5+ years): Weight structural trends and marginal cost evolution

## Output Format

```
## Price Forecast — [Commodity Name]
### Current Price: $XX.XX/unit
### Date: [Date]

### Historical Context
| Metric | Value |
|--------|-------|
| 52-week high | $XX.XX |
| 52-week low | $XX.XX |
| 5-year average | $XX.XX |
| 10-year average | $XX.XX |

### Price Forecast
| Period | Bear | Base | Bull |
|--------|------|------|------|
| Q1 2026 | $XX | $XX | $XX |
| Q2 2026 | $XX | $XX | $XX |
| H2 2026 | $XX | $XX | $XX |
| 2027 | $XX | $XX | $XX |
| 2028 | $XX | $XX | $XX |
| 2030 | $XX | $XX | $XX |

### Key Drivers
| Driver | Direction | Impact |
|--------|-----------|--------|
| [Driver 1] | Bullish/Bearish | High/Medium/Low |
| [Driver 2] | ... | ... |

### Risks to Forecast
[Key upside and downside risks]

### Data Sources
[List sources used for this forecast]
```

## References

See `references/price-drivers.md` for commodity-specific price driver analysis.
