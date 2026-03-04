---
name: Feasibility Study Analysis
description: Evaluate PFS/BFS/DFS mining feasibility studies for completeness, economic viability, and alignment with industry benchmarks.
---

# Feasibility Study Analysis

## Purpose

Critically evaluate mining project feasibility studies at all stages — Scoping Study, Pre-Feasibility Study (PFS), Bankable/Definitive Feasibility Study (BFS/DFS) — to assess economic viability, identify risks, and validate key assumptions.

## Study Stage Definitions

| Stage | Accuracy | Purpose | Typical Cost |
|-------|----------|---------|-------------|
| Scoping Study | ±35-50% | Conceptual viability | $0.2–1M |
| Pre-Feasibility (PFS) | ±25-30% | Investment decision gate | $2–10M |
| Bankable/Definitive (BFS/DFS) | ±10-15% | Bank financing, construction decision | $10–50M+ |

## Workflow

### Step 1: Study Completeness Check
Verify all required sections are present:
- [ ] Mineral resource/reserve estimate (by a Competent Person / QP)
- [ ] Mining method selection and mine plan
- [ ] Metallurgical testwork and process design
- [ ] Infrastructure (power, water, roads, tailings)
- [ ] Environmental baseline and impact assessment
- [ ] Capital cost estimate (initial + sustaining)
- [ ] Operating cost estimate (per tonne or per unit of product)
- [ ] Revenue model (commodity prices, production schedule)
- [ ] Financial model (NPV, IRR, payback)
- [ ] Sensitivity analysis
- [ ] Risk register
- [ ] Implementation schedule

### Step 2: Assumption Validation
For each key assumption, check against benchmarks:
- **Commodity prices**: Compare to consensus forecasts and forward curves
- **Recovery rates**: Compare to testwork results and analogous operations
- **Mining costs**: Benchmark vs. cost curves (see `references/benchmarks.md`)
- **Processing costs**: Compare to similar plant designs
- **Capex**: Benchmark on $/tonne annual capacity basis
- **Discount rate**: Validate WACC assumptions

### Step 3: Economic Analysis
- Recalculate NPV at multiple discount rates (6%, 8%, 10%, 12%)
- Verify IRR calculation
- Check sensitivity to: commodity price (±20%), capex (+20%), opex (+15%), grade (-10%), recovery (-5%)
- Identify break-even commodity price
- Assess margin of safety

### Step 4: Technical Risk Assessment
- Mining: Geotechnical stability, water management, dilution assumptions
- Metallurgy: Testwork stage, variability, scale-up risk
- Infrastructure: Power reliability, water availability, logistics
- Schedule: Construction timeline vs. comparable projects

### Step 5: Comparative Benchmarking
- Compare key metrics to comparable projects (invoke `comparable-projects` skill)
- Position on industry cost curves
- Assess relative attractiveness

## Output Format

```
## Feasibility Study Review — [Project Name]
### Study Stage: [Scoping/PFS/BFS/DFS]

### Completeness Score: X/12 sections

### Key Metrics
| Metric | Study Value | Benchmark Range | Assessment |
|--------|------------|-----------------|------------|
| NPV (8%) | $XXM | ... | ... |
| IRR | XX% | ... | ... |
| Payback | X.X yrs | ... | ... |
| Capex | $XXM | ... | ... |
| AISC | $XX/unit | ... | ... |
| Break-even price | $XX/unit | ... | ... |

### Sensitivity Analysis
[Table showing NPV sensitivity to key variables]

### Key Risks
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| ...  | ...       | ...    | ...        |

### Recommendations
1. [Items requiring further work]
2. [Key de-risking steps before next stage]
```

## References

See `references/study-stages.md` for detailed stage requirements and `references/benchmarks.md` for cost benchmarks.
