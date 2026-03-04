# Mining Discount Rate Reference

## Overview

The discount rate used in mining project valuations reflects the time value of money and the risk profile of the project. Mining projects carry unique risks including geological uncertainty, commodity price volatility, jurisdictional risk, and long development timelines. The discount rate is typically expressed as a Weighted Average Cost of Capital (WACC) or, for equity valuations, a cost of equity.

## Typical WACC Ranges by Project Stage

| Stage | Typical Real WACC Range | Rationale |
|-------|------------------------|-----------|
| **Grassroots Exploration** | Not applicable | Too early for DCF; use comparable transactions or option-value methods |
| **Advanced Exploration** | 12 - 15% | High geological uncertainty, no defined resource, binary outcome risk |
| **Pre-Feasibility Study (PFS)** | 10 - 12% | Resource defined but modifying factors uncertain; significant execution risk |
| **Definitive Feasibility Study (DFS)** | 8 - 10% | Reserves defined, engineering advanced, permitting underway |
| **Construction** | 7 - 10% | Capital committed, execution risk remains, schedule and cost overrun potential |
| **Production (established)** | 5 - 8% | Proven operational track record, steady-state cash flows |
| **Production (mature / declining)** | 6 - 9% | Declining reserve life, potential closure cost uncertainty |

## WACC Calculation

```
WACC = (E/V) x Re + (D/V) x Rd x (1 - Tc)
```

### Cost of Equity (Re) using CAPM

```
Re = Rf + Beta x ERP + CRP + SRP + CSRP
```

| Component | Description | Typical Range |
|-----------|-------------|---------------|
| **Rf** | Risk-free rate (10-year government bond) | 2 - 5% (nominal) |
| **Beta** | Systematic risk relative to market | 0.8 - 1.5 for mining (commodity-dependent) |
| **ERP** | Equity risk premium (market return - Rf) | 5 - 7% |
| **CRP** | Country risk premium | 0 - 15% (see table below) |
| **SRP** | Size / stage risk premium | 0 - 5% |
| **CSRP** | Company-specific risk premium | 0 - 5% |

### Mining Betas by Commodity

| Commodity | Typical Equity Beta | Notes |
|-----------|-------------------|-------|
| Gold | 0.8 - 1.2 | Counter-cyclical; lower beta than base metals |
| Silver | 1.0 - 1.4 | Higher volatility than gold |
| Copper | 1.0 - 1.5 | Correlated with economic cycles |
| Iron Ore | 1.0 - 1.4 | High China exposure |
| Nickel | 1.2 - 1.6 | Volatile, stainless/battery demand shifts |
| Lithium | 1.2 - 1.8 | High growth but volatile pricing |
| Zinc / Lead | 1.0 - 1.3 | Moderate cyclicality |
| Coal (thermal) | 0.8 - 1.2 | Declining sector; ESG discount applies |
| Coal (metallurgical) | 1.0 - 1.4 | Steel industry linked |
| Uranium | 1.0 - 1.5 | Policy-driven, long contract cycles |
| Rare Earths | 1.3 - 2.0 | High uncertainty, limited market data |

## Country Risk Premiums

| Tier | Jurisdictions (examples) | CRP Range | Notes |
|------|-------------------------|-----------|-------|
| **Tier 1** | Canada, Australia, USA, Chile, Scandinavia | 0 - 2% | Stable mining codes, transparent permitting |
| **Tier 2** | Peru, Brazil, Mexico, Botswana, Namibia | 2 - 5% | Generally mining-friendly but some regulatory uncertainty |
| **Tier 3** | Argentina, Colombia, Philippines, Indonesia | 4 - 8% | Elevated political or regulatory risk |
| **Tier 4** | DRC, Tanzania, Russia, Myanmar | 6 - 12% | High political risk, resource nationalism |
| **Tier 5** | Venezuela, Sudan, North Korea | 10 - 15%+ | Extreme risk; most investors avoid |

Sources for country risk data:
- **Fraser Institute** Annual Survey of Mining Companies
- **Aswath Damodaran** country risk premium data (updated annually)
- **World Bank** Worldwide Governance Indicators

## Size and Stage Premiums

| Company Size / Stage | Premium | Rationale |
|---------------------|---------|-----------|
| Large-cap producer (>$5B market cap) | 0% | Well-diversified, liquid stock, institutional ownership |
| Mid-cap producer ($1-5B) | 1 - 2% | Less diversified, moderate liquidity |
| Small-cap producer (<$1B) | 2 - 3% | Single or few assets, limited financial flexibility |
| Developer (post-DFS) | 3 - 4% | Construction and execution risk |
| Explorer (post-PFS) | 4 - 5% | Resource uncertainty, funding risk |
| Junior explorer | 5%+ or N/A | Use comparable transactions, not DCF |

## Real vs Nominal Discount Rates

Mining valuations are typically performed in **real (constant dollar) terms** to avoid forecasting inflation for each cost and revenue line:

```
Real Rate = (1 + Nominal Rate) / (1 + Inflation Rate) - 1

Example:
  Nominal WACC = 10%
  Expected inflation = 2.5%
  Real WACC = (1.10 / 1.025) - 1 = 7.3%
```

If the model uses nominal cash flows, use the nominal discount rate. Consistency between cash flows and discount rate is critical.

## Examples

### Example 1: Gold Producer in Canada

```
Rf = 3.5% (Canadian 10-year bond)
Beta = 1.0
ERP = 6.0%
CRP = 0% (Tier 1)
SRP = 1.5% (mid-cap)

Re = 3.5% + 1.0 x 6.0% + 0% + 1.5% = 11.0%

D/V = 20%, Rd = 6%, Tc = 26.5%
WACC = 0.80 x 11.0% + 0.20 x 6.0% x (1 - 0.265)
WACC = 8.8% + 0.88% = 9.7% (nominal)
Real WACC = ~7.0% (assuming 2.5% inflation)
```

### Example 2: Copper Developer in Peru

```
Rf = 4.0% (US 10-year bond, USD model)
Beta = 1.2
ERP = 6.0%
CRP = 3.0% (Tier 2)
SRP = 3.5% (developer)

Re = 4.0% + 1.2 x 6.0% + 3.0% + 3.5% = 17.7%

Assume 100% equity (pre-construction)
WACC = Re = 17.7% (nominal)
Real WACC = ~14.8% (assuming 2.5% inflation)
```

### Example 3: Lithium Explorer in DRC

```
Rf = 4.0%
Beta = 1.5
ERP = 6.0%
CRP = 10.0% (Tier 4)
SRP = 5.0% (explorer)

Re = 4.0% + 1.5 x 6.0% + 10.0% + 5.0% = 28.0%

At this discount rate, DCF is often impractical.
Consider using comparable transactions ($/t LCE in-situ) instead.
```

## Common Pitfalls

1. **Mixing real and nominal**: Using a real discount rate on nominal cash flows (or vice versa) produces materially wrong NPV
2. **Ignoring country risk**: Using a Tier 1 discount rate for a Tier 3 jurisdiction overstates NPV
3. **Understating size premium**: Applying large-cap rates to junior companies
4. **Using a single rate for all scenarios**: Bear case should arguably use a higher rate (higher risk), but common practice is to hold the rate constant and vary cash flows
5. **Ignoring debt capacity changes**: Pre-construction projects are typically 100% equity; production-stage projects may carry 30-50% debt
