# Practical Guide to Resource Classification

## Overview

Resource classification determines the confidence level assigned to estimated mineral resources. While reporting codes (JORC, NI 43-101) provide principles-based guidance, classification in practice requires professional judgement applied to specific deposit characteristics. This guide provides practical benchmarks by commodity type.

## Drill Spacing Guidelines by Commodity

The following are industry-accepted starting points for classification. Actual classification must consider geological continuity, grade variability, structural complexity, and data quality.

### Precious Metals

#### Gold (Lode / Orogenic)

| Category | Typical Drill Spacing | Notes |
|----------|----------------------|-------|
| Measured | 12.5 - 25 m | Close spacing needed due to high grade variability (nugget effect) |
| Indicated | 25 - 50 m | Geological continuity must be demonstrated |
| Inferred | 50 - 100 m | Reasonable geological assumption of continuity |

- High nugget effect deposits (e.g., coarse gold) may require closer spacing
- Structurally controlled deposits require drilling perpendicular to controlling structures
- Screen fire assay or Leachwell recommended for coarse gold

#### Gold (Placer / Alluvial)

| Category | Typical Drill Spacing | Notes |
|----------|----------------------|-------|
| Measured | 25 - 50 m | Large-diameter drilling (e.g., Banka, bulk sampling) |
| Indicated | 50 - 100 m | Pay channel geometry must be defined |
| Inferred | 100 - 200 m | Based on geophysical or geochemical evidence |

#### Platinum Group Elements (PGE)

| Category | Typical Drill Spacing | Notes |
|----------|----------------------|-------|
| Measured | 25 - 50 m | Stratiform deposits (Bushveld-type) allow wider spacing |
| Indicated | 50 - 100 m | Reef continuity generally good in stratiform settings |
| Inferred | 100 - 200 m | Structural disruptions (potholes, faults) increase uncertainty |

### Base Metals

#### Copper (Porphyry)

| Category | Typical Drill Spacing | Notes |
|----------|----------------------|-------|
| Measured | 25 - 50 m | Large, relatively uniform deposits allow wider spacing |
| Indicated | 50 - 100 m | Grade shells well-defined by alteration zonation |
| Inferred | 100 - 200 m | Deposit geometry supports extrapolation |

#### Copper (VMS / Skarn)

| Category | Typical Drill Spacing | Notes |
|----------|----------------------|-------|
| Measured | 12.5 - 25 m | Higher grade variability in massive sulphide lenses |
| Indicated | 25 - 50 m | Lens geometry must be well-defined |
| Inferred | 50 - 100 m | Geophysical targets may support wider spacing |

#### Zinc-Lead

| Category | Typical Drill Spacing | Notes |
|----------|----------------------|-------|
| Measured | 25 - 50 m | Varies by deposit type (MVT vs VMS vs SEDEX) |
| Indicated | 50 - 75 m | Grade distribution often lognormal |
| Inferred | 75 - 150 m | Stratigraphic control may allow wider spacing |

#### Nickel (Laterite)

| Category | Typical Drill Spacing | Notes |
|----------|----------------------|-------|
| Measured | 25 - 50 m | Blanket-style deposits, relatively uniform |
| Indicated | 50 - 100 m | Topography and weathering profile control geometry |
| Inferred | 100 - 200 m | Geomorphological continuity supports extrapolation |

#### Nickel (Sulphide)

| Category | Typical Drill Spacing | Notes |
|----------|----------------------|-------|
| Measured | 12.5 - 25 m | Massive sulphide lenses require close spacing |
| Indicated | 25 - 50 m | Disseminated zones may allow wider spacing |
| Inferred | 50 - 100 m | EM geophysics can support targeting |

### Bulk Commodities

#### Iron Ore

| Category | Typical Drill Spacing | Notes |
|----------|----------------------|-------|
| Measured | 50 - 100 m | Large, geologically simple deposits |
| Indicated | 100 - 200 m | Channel iron deposits (CID) may require closer spacing |
| Inferred | 200 - 400 m | Banded iron formations (BIF) have good lateral continuity |

#### Coal

| Category | Typical Drill Spacing | Notes |
|----------|----------------------|-------|
| Measured | 250 - 500 m | Seam continuity generally high for thick seams |
| Indicated | 500 - 1000 m | Quality variation may require closer spacing |
| Inferred | 1000 - 2000 m | Stratigraphic control allows wide spacing |

#### Bauxite

| Category | Typical Drill Spacing | Notes |
|----------|----------------------|-------|
| Measured | 50 - 100 m | Blanket-style deposits |
| Indicated | 100 - 200 m | Topography-controlled geometry |
| Inferred | 200 - 400 m | Geomorphological mapping supports extrapolation |

### Battery / Critical Minerals

#### Lithium (Hard Rock — Spodumene)

| Category | Typical Drill Spacing | Notes |
|----------|----------------------|-------|
| Measured | 25 - 50 m | Pegmatite geometry can be irregular |
| Indicated | 50 - 100 m | Structural controls must be well-understood |
| Inferred | 100 - 200 m | Pegmatite swarms allow moderate extrapolation |

#### Lithium (Brine)

| Category | Typical Drill Spacing | Notes |
|----------|----------------------|-------|
| Measured | 500 - 1000 m | Brine resources classified differently (porosity, concentration) |
| Indicated | 1000 - 2000 m | Aquifer testing and pump tests required |
| Inferred | 2000 - 5000 m | Regional hydrogeology supports extrapolation |

#### Rare Earth Elements (REE)

| Category | Typical Drill Spacing | Notes |
|----------|----------------------|-------|
| Measured | 25 - 50 m | Ionic clay deposits may allow wider spacing |
| Indicated | 50 - 100 m | Individual REE grades vary more than TREO |
| Inferred | 100 - 200 m | Weathering profile controls must be understood |

## Grade Continuity Analysis

### Variography

Before classification, grade continuity must be assessed through variographic analysis:

1. **Calculate experimental semi-variograms** for each domain and element
2. **Fit variogram models** (spherical, exponential, or Gaussian)
3. **Key parameters to extract**:
   - **Nugget**: Represents short-scale variability and sampling error. High nugget = lower confidence at a given drill spacing.
   - **Range**: Distance at which samples become uncorrelated. Classification boundary should be within the range.
   - **Sill**: Total variance. Relative nugget (nugget/sill) indicates data quality.

### Relative Nugget Effect

| Relative Nugget (C0/Sill) | Interpretation | Impact on Classification |
|---------------------------|---------------|------------------------|
| < 0.25 | Low — good grade continuity | Classification at wider spacing may be justified |
| 0.25 - 0.50 | Moderate — reasonable continuity | Standard drill spacing guidelines apply |
| 0.50 - 0.75 | High — poor grade continuity | Tighter spacing required for equivalent confidence |
| > 0.75 | Very high — near-random | Close spacing essential; Inferred only unless very dense data |

## Data Quality Requirements

Classification should be downgraded if data quality is inadequate:

| Factor | Acceptable | Flag for Review |
|--------|-----------|----------------|
| Core recovery | > 90% | < 80% |
| QAQC standards | < 5% failure | > 10% failure |
| Blanks | < 5x detection limit | Significant contamination |
| Field duplicates | < 15% HARD | > 20% HARD |
| Umpire checks | < 10% bias | > 15% bias |
| Sampling method | Diamond core, RC with cyclone | Grab, channel (may be acceptable for some deposit types) |

## Reconciliation with Production

For operating mines, classification should be informed by production reconciliation:

| Reconciliation Factor (Actual/Predicted) | Interpretation |
|------------------------------------------|---------------|
| 0.90 - 1.10 (tonnage) | Good — model is reliable |
| 0.85 - 1.15 (grade) | Acceptable — minor adjustment needed |
| < 0.85 or > 1.15 | Poor — review estimation methodology and classification |

Regular reconciliation supports upgrading Indicated to Measured or identifies where classification should be downgraded.
