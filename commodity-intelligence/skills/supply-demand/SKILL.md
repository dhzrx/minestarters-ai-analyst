---
name: Supply/Demand Modeling
description: Build comprehensive supply and demand models for mineral commodities with projected market balance over 5-10 years.
---

# Supply/Demand Modeling

## Purpose

Build bottom-up supply and demand models for mineral commodities to identify market imbalances, forecast price direction, and assess investment timing.

## Model Structure

### Supply Side

#### Primary Supply (Mine Production)
| Component | Data Required | Sources |
|-----------|--------------|---------|
| Current production | Annual output by mine | Company reports, USGS, ICSG, ILZSG |
| Production growth/decline | Mine plans, depletion rates | Feasibility studies, analyst reports |
| Pipeline projects | Stage, timeline, capacity | S&P Global, company announcements |
| Disruption risk | Political, weather, technical | Historical disruption rates by region |

#### Secondary Supply
| Component | Data Required |
|-----------|--------------|
| Recycling | Current and projected recycling rates |
| Stockpile releases | Government and strategic reserves |
| Scrap processing | Scrap collection and processing capacity |

### Demand Side

#### By End-Use Sector
Build demand model for each major end-use:
- Identify all demand sectors and current consumption share
- Project growth rate per sector
- Account for material intensity changes (e.g., EV battery chemistry evolution)
- Include substitution effects

#### Example: Copper Demand Breakdown
| Sector | Current Share | Growth Rate | Driver |
|--------|-------------|-------------|--------|
| Construction | 25% | 2-3% | Urbanization, infrastructure |
| Electrical grid | 20% | 4-6% | Grid expansion, renewables |
| EVs & charging | 10% | 15-25% | EV adoption curve |
| Electronics | 15% | 3-5% | AI data centers, consumer |
| Industrial | 20% | 2-3% | Industrial production |
| Other | 10% | 1-2% | Various |

### Market Balance

```
Annual Balance = (Mine Production + Secondary Supply) - Total Demand

Inventory Change = Previous Inventory + Annual Balance
Weeks of Consumption = Inventory / (Annual Demand / 52)
```

## Workflow

### Step 1: Gather Production Data
- Current global production by country and major mine
- Planned expansions and new projects with timelines
- Expected mine closures and depletion
- Project historical disruption rate (typically 3-5% of supply)

### Step 2: Model Supply Trajectory
- Base case: Only include projects with >70% probability of commissioning on time
- Apply ramp-up curves (typically 70% Year 1, 90% Year 2, 100% Year 3)
- Apply disruption allowance to gross supply
- Add secondary supply (recycling growth trajectory)

### Step 3: Model Demand Trajectory
- Bottom-up by end-use sector
- Apply sector-specific growth rates
- Account for technology shifts (e.g., thrifting, substitution)
- Cross-check with top-down GDP/industrial production correlation

### Step 4: Calculate Balance
- Annual surplus/deficit for each forecast year
- Cumulative balance and implied inventory
- Weeks of consumption (critical indicator)
- Identify inflection points (when deficit begins/ends)

### Step 5: Interpret Results
- Persistent deficit → price support/increase
- Growing surplus → price pressure
- Inventory < 3 weeks → supply crisis risk
- Inventory > 8 weeks → price ceiling

## Output Format

```
## Supply/Demand Model — [Commodity]
### Base Year: [Year]
### Forecast Period: [Year] to [Year]

### Supply Forecast (kt/year)
| Year | Mine Supply | Secondary | Total Supply | YoY Change |
|------|------------|-----------|-------------|------------|
| ...  | ...        | ...       | ...         | ...        |

### Demand Forecast (kt/year)
| Year | [Sector 1] | [Sector 2] | ... | Total Demand | YoY Change |
|------|-----------|-----------|-----|-------------|------------|
| ...  | ...       | ...       | ... | ...         | ...        |

### Market Balance
| Year | Supply | Demand | Balance | Inventory | Weeks of Consumption |
|------|--------|--------|---------|-----------|---------------------|
| ...  | ...    | ...    | ...     | ...       | ...                 |

### Key Findings
1. [When does deficit/surplus begin or end]
2. [Which demand sector drives the most growth]
3. [Which supply projects are critical to balance]
4. [Price implications of the balance outlook]
```
