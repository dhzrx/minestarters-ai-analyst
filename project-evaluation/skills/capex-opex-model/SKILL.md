---
name: CAPEX/OPEX Model
description: Build and validate capital and operating cost models for mining projects with benchmarking against industry standards.
---

# Capital & Operating Cost Model

## Purpose

Develop, review, or benchmark capital expenditure (CAPEX) and operating expenditure (OPEX) estimates for mining projects.

## CAPEX Components

### Initial Capital
| Category | Typical % of Total | Description |
|----------|--------------------|-------------|
| Mining equipment | 15-25% | Trucks, loaders, drills, ancillary |
| Processing plant | 30-45% | Crushing, grinding, flotation/leaching/smelting |
| Infrastructure | 15-25% | Roads, power, water, camp, airstrip |
| Tailings facility | 5-10% | Dam construction, liner, pipelines |
| Indirect costs | 10-15% | EPCM, owner's costs, commissioning |
| Contingency | 5-15% | Risk-based contingency by study stage |

### Sustaining Capital
- Equipment replacement and rebuilds
- Tailings dam raises
- Underground development (for UG mines)
- Typically 5-15% of initial capex annually

## OPEX Components

### Open Pit Mining
| Item | Typical Range | Units |
|------|--------------|-------|
| Drill & blast | $0.50–1.50 | /t mined |
| Load & haul | $1.00–3.00 | /t mined |
| Grade control | $0.10–0.30 | /t mined |
| Mine management | $0.20–0.50 | /t mined |

### Underground Mining
| Item | Typical Range | Units |
|------|--------------|-------|
| Development | $15–40 | /m advance |
| Stoping | $20–60 | /t ore |
| Backfill | $5–15 | /t ore |
| Ventilation | $3–8 | /t ore |

### Processing
| Item | Typical Range | Units |
|------|--------------|-------|
| Crushing & grinding | $3–10 | /t ore |
| Reagents | $1–5 | /t ore |
| Power | $2–8 | /t ore |
| Maintenance | $1–3 | /t ore |
| Labor | $2–6 | /t ore |

### G&A
- Typically $1–5/t ore processed
- Includes: corporate, site admin, community, environment, exploration

## Workflow

### Step 1: Estimate or Review CAPEX
- Break down by category (use table above)
- Cross-check against benchmarks ($/tonne annual capacity)
- Assess contingency adequacy for study stage
- Identify capex per unit of annual production

### Step 2: Estimate or Review OPEX
- Build bottom-up cost model by activity
- Express as $/t mined, $/t processed, and $/unit of product
- Calculate all-in sustaining cost (AISC)
- Include royalties, sustaining capex, corporate G&A

### Step 3: Benchmark
- Compare CAPEX intensity to comparable projects
- Position on cost curve (AISC or C1)
- Identify cost advantages/disadvantages (grade, scale, energy, labor)

### Step 4: Sensitivity
- Test OPEX sensitivity to: energy price (±30%), labor (±15%), currency (±10%)
- Test CAPEX sensitivity to: scope changes, construction market conditions
- Identify fixed vs. variable cost split

## Output Format

```
## Cost Model — [Project Name]

### CAPEX Summary
| Category | Estimate ($M) | % of Total | Benchmark |
|----------|--------------|------------|-----------|
| ...      | ...          | ...        | ...       |
| **Total** | **$XXM** | **100%** | ... |

### OPEX Summary
| Item | $/t Mined | $/t Processed | $/unit Product |
|------|-----------|---------------|----------------|
| ...  | ...       | ...           | ...            |
| **AISC** | ... | ... | **$XX/unit** |

### Cost Curve Position
[Description of position relative to industry peers]

### Cost Optimization Opportunities
1. [Opportunity 1]
2. [Opportunity 2]
```
