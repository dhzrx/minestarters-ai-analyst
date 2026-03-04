---
name: Token Economics
description: Model ART stablecoin backing mechanics and MINE utility token economics for the Minestarters mining RWA platform.
---

# Token Economics

## Purpose

Model and analyze the two-token system used by Minestarters:
1. **ART (Asset-Referenced Token)**: Stablecoin backed by mineral reserves
2. **$MINE**: Utility/governance token for platform operations

## ART Token Model

### Backing Mechanics
ART is an asset-referenced stablecoin where each token is backed by a defined value of verified mineral reserves.

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| Collateralization Ratio | Reserve value / ART supply | 150-200% |
| Reserve Composition | Mix of mineral reserves backing ART | Diversified across 5+ commodities |
| Valuation Method | How reserves are valued | Conservative (Indicated resources at discount) |
| Revaluation Frequency | How often backing is recalculated | Quarterly |
| Redemption Mechanism | How ART holders can redeem | Burn ART → receive equivalent in stablecoins |

### Reserve Valuation Formula
```
ART Backing Value = Σ (Reserve_i tonnes × Commodity_i Price × Recovery_i × Discount_i)

Where:
  Reserve_i = Measured + Indicated resources for commodity i
  Commodity_i Price = 90-day trailing average price
  Recovery_i = Expected metallurgical recovery (conservative estimate)
  Discount_i = Stage-based discount (Producing: 0.8, Development: 0.5, Exploration: 0.3)
```

### Stability Mechanisms
1. **Over-collateralization**: Maintain >150% backing ratio
2. **Reserve buffer**: Additional 10% unallocated reserves
3. **Rebalancing trigger**: If ratio drops below 140%, trigger reserve addition or ART buyback
4. **Oracle verification**: Independent verification of reserve values (see `oracle-verification` skill)
5. **Liquidation mechanism**: If ratio drops below 120%, gradual ART supply reduction

## $MINE Token Model

### Utility Functions
| Function | Description | Value Driver |
|----------|-------------|-------------|
| Governance | Vote on platform decisions, basket composition | Voting power proportional to staked MINE |
| Staking | Stake MINE to earn platform fee share | 40% of platform fees distributed to stakers |
| Fee discount | Reduced trading/management fees | Up to 50% discount based on MINE tier |
| Access | Premium features, early basket access | Tier-gated access to new offerings |
| Buyback/burn | Platform uses revenue to buy and burn MINE | Deflationary pressure on supply |

### Token Distribution
| Allocation | Percentage | Vesting |
|-----------|-----------|---------|
| Community & ecosystem | 35% | 4-year linear release |
| Team & advisors | 15% | 1-year cliff, 3-year vesting |
| Treasury | 20% | Governed by DAO votes |
| Liquidity mining | 15% | Programmatic release over 5 years |
| Strategic investors | 10% | 6-month cliff, 2-year vesting |
| Public sale | 5% | No lock-up |

### Revenue Flow Model
```
Platform Revenue Sources:
  ├─ Management fees (1-2% AUM annually)
  ├─ Performance fees (20% above hurdle)
  ├─ Trading fees (0.1-0.5% per trade)
  ├─ Tokenization fees (1-3% of raise)
  └─ RPA origination fees (0.5-1%)

Revenue Distribution:
  ├─ 40% → MINE stakers (pro-rata)
  ├─ 20% → Buyback & burn
  ├─ 25% → Operations & development
  └─ 15% → Treasury reserve
```

## Workflow

### Step 1: Define Token Parameters
- Total supply, initial circulating supply
- Distribution schedule and vesting
- Fee structure and revenue model
- Staking parameters (lock periods, reward rates)

### Step 2: Model Token Flows
- Circulating supply over time (emission schedule minus burns)
- Revenue projections by source
- Staking ratio assumptions (30-60% of supply)
- Fee revenue at various AUM levels

### Step 3: Valuation Scenarios
- Revenue multiple approach (P/E based on fee revenue to stakers)
- Comparable token analysis (other RWA platforms)
- Discounted cash flow of staking rewards
- Fully diluted vs. circulating valuation

### Step 4: Stress Testing
- Commodity price crash (reserves devalue → ART backing ratio drops)
- Mass redemption scenario
- Staking exodus (what if staking ratio drops to 10%)
- Regulatory change (securities classification)

## Output Format

```
## Token Economics Report — Minestarters

### ART Analysis
| Metric | Value |
|--------|-------|
| Total ART Supply | XXM tokens |
| Reserve Backing Value | $XXXM |
| Collateralization Ratio | XXX% |
| Reserve Composition | Au XX%, Cu XX%, Li XX%, ... |

### $MINE Analysis
| Metric | Value |
|--------|-------|
| Total Supply | XXXM tokens |
| Circulating Supply | XXM (XX%) |
| Staking Ratio | XX% |
| Annual Fee Revenue | $XXM |
| Staker Yield | XX% APY |
| Burn Rate | XXM tokens/year |

### Scenarios
| Scenario | AUM | Fee Revenue | MINE Value | ART Backing |
|----------|-----|-----------|------------|-------------|
| Bear | $XXM | $XXM | $X.XX | XXX% |
| Base | $XXM | $XXM | $X.XX | XXX% |
| Bull | $XXM | $XXM | $X.XX | XXX% |
```

## References

See `references/art-mechanics.md` and `references/mine-tokenomics.md`.
