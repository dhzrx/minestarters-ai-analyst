# ART (Asset-Referenced Token) Mechanics

## Overview

ART is a stablecoin backed by verified mineral reserves across the Minestarters platform. Unlike fiat-backed stablecoins, ART derives its value from the in-ground value of mineral resources held by SPVs in the Minestarters ecosystem.

## Backing Calculation

### Reserve Valuation
Each mining project contributing to ART backing is valued as:

```
Project Backing Value = Σ (Resource_category × Grade × Tonnes × Price × Recovery × Stage_Discount)
```

### Stage Discounts
| Project Stage | Discount Factor | Rationale |
|--------------|----------------|-----------|
| Producing | 0.80 | Proven economics, operational risk only |
| Construction | 0.60 | Capital risk, schedule risk |
| BFS/DFS complete | 0.50 | Feasibility proven, needs funding |
| PFS complete | 0.35 | Preliminary economics, needs more study |
| Exploration (Indicated) | 0.20 | Resource uncertainty, no economics |
| Exploration (Inferred) | 0.00 | Not included in backing |

### Resource Category Adjustments
| Category | Confidence Multiplier |
|----------|---------------------|
| Proved Reserve | 1.00 |
| Probable Reserve | 0.90 |
| Measured Resource | 0.85 |
| Indicated Resource | 0.70 |
| Inferred Resource | 0.00 (excluded) |

## Collateralization Rules

- **Target ratio**: 175% (backing value / ART outstanding)
- **Minimum ratio**: 150%
- **Warning trigger**: 160% (begin corrective action)
- **Liquidation trigger**: 120% (begin ART supply reduction)

## Rebalancing Actions

| Condition | Action |
|-----------|--------|
| Ratio > 200% | May issue new ART (if demand exists) |
| 175% < Ratio < 200% | Normal operation |
| 150% < Ratio < 175% | Monitor, prepare contingency |
| 140% < Ratio < 150% | Halt new ART issuance, increase reserve |
| 120% < Ratio < 140% | Begin ART buyback and burn |
| Ratio < 120% | Emergency: proportional redemption at discount |

## Redemption Mechanism

1. Token holder submits ART for redemption
2. System verifies KYC/AML status
3. ART burned
4. Equivalent value in USDC/USDT sent to holder
5. Backing ratio recalculated
