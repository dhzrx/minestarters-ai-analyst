---
name: "Competitive Analysis"
description: "Benchmark mining companies and projects against peer groups on production costs, reserves, market capitalisation, EV/resource ratios, and operational efficiency."
---

# Competitive Analysis

## Purpose

Compare a target mining company or project against its peer group to identify relative strengths, weaknesses, and valuation anomalies. This skill produces a structured peer comparison matrix with standardised metrics that enable apples-to-apples benchmarking across the sector.

## Key Metrics

### Valuation Multiples

| Metric | Formula | What It Measures |
|--------|---------|------------------|
| **EV/Resource** | Enterprise Value / Total Resource (M+I+I) oz or lb | Market's implied value per unit of in-ground resource |
| **EV/Reserve** | Enterprise Value / Total Reserve (P+P) oz or lb | Market's implied value per unit of economically extractable resource |
| **P/NAV** | Share Price / Net Asset Value per share | Premium or discount to intrinsic value |
| **P/E** | Share Price / Earnings per share | Earnings multiple |
| **EV/EBITDA** | Enterprise Value / EBITDA | Cash earnings multiple |

### Cost Metrics

| Metric | Formula | What It Measures |
|--------|---------|------------------|
| **AISC** | All-In Sustaining Cost per unit produced | Full cost of maintaining current production |
| **C1 Cash Cost** | Direct cash cost per unit produced | Variable production cost |
| **AIC** | All-In Cost (AISC + growth CAPEX) | Total cost including expansion |
| **Cost Curve Position** | Percentile rank on global cost curve | Competitiveness vs global peers |

### Operational Metrics

| Metric | Description |
|--------|-------------|
| **Annual Production** | Metal produced per year (oz, lb, kt) |
| **Reserve Life** | Reserves / Annual Production (years) |
| **Resource-to-Reserve Conversion** | Reserves / Total Resources (%) |
| **Grade** | Head grade or reserve grade vs peers |
| **Recovery Rate** | Metallurgical recovery (%) |
| **Throughput** | Tonnes processed per day/year |

### Financial Metrics

| Metric | Description |
|--------|-------------|
| **Market Capitalisation** | Share price x shares outstanding |
| **Enterprise Value** | Market cap + net debt + minority interests |
| **Revenue** | Annual revenue |
| **EBITDA Margin** | EBITDA / Revenue (%) |
| **Net Debt / EBITDA** | Leverage ratio |
| **Free Cash Flow Yield** | FCF / Market Cap (%) |
| **Dividend Yield** | Annual dividend / Share price (%) |

## Workflow

### Step 1: Identify Peer Group

Select comparable companies or projects based on:

- **Commodity**: Same primary commodity (e.g., gold producers, copper developers)
- **Stage**: Same development stage (explorer, developer, producer)
- **Size**: Similar market cap or production scale
- **Geography**: Same or similar jurisdiction (optional, for jurisdiction-specific analysis)
- **Mining method**: Open pit vs underground (optional)

Typical peer group size: 5-15 companies.

### Step 2: Gather Financial and Operational Data

Sources:
- **SEC EDGAR** (`sec-edgar`): 10-K, 10-Q filings for US-listed companies
- **ASX Announcements** (`asx-announcements`): Annual reports, quarterly activity reports
- **Company websites**: Investor presentations, technical reports, mine plans
- **S&P Global** (`sp-global-mining`): Standardised financial and operational data
- **Broker research**: Consensus estimates, NAV models (where available)

### Step 3: Normalise Metrics

- Convert all currencies to a common base (typically USD)
- Standardise units (oz, lb, kt as appropriate for commodity)
- Adjust for reporting period differences
- Apply consistent AISC definitions (World Gold Council standard for gold)
- Handle multi-commodity operations (allocate or use primary commodity equivalent)

### Step 4: Create Comparison Matrix

Build a structured table with all metrics for all peers:

| Metric | Target | Peer 1 | Peer 2 | Peer 3 | Peer Avg | Rank |
|--------|--------|--------|--------|--------|----------|------|
| Market Cap ($M) | 500 | 800 | 350 | 1,200 | 783 | 3/4 |
| EV/Resource ($/oz) | 45 | 62 | 38 | 85 | 62 | 2/4 |
| AISC ($/oz) | 1,050 | 1,150 | 980 | 1,200 | 1,110 | 2/4 |
| Reserve Life (yrs) | 12 | 8 | 15 | 10 | 11 | 2/4 |
| ... | ... | ... | ... | ... | ... | ... |

### Step 5: Identify Strengths and Weaknesses

For each metric, determine the target's position relative to peers:

- **Top quartile**: Competitive advantage (highlight green)
- **Second quartile**: Above average
- **Third quartile**: Below average (flag for attention)
- **Bottom quartile**: Competitive weakness (highlight red)

Identify:
- **Valuation gaps**: Where the target trades at a discount/premium to peers
- **Operational advantages**: Cost, grade, or recovery advantages
- **Risk factors**: Higher leverage, shorter mine life, jurisdiction risk
- **Catalyst potential**: Upcoming events that could close valuation gaps

## Output Format

1. **Peer group summary table** with all metrics and rankings
2. **Valuation comparison chart data** (EV/Resource, P/NAV scatter)
3. **Cost curve positioning** (target vs peers on AISC/C1 cost curve)
4. **Strengths and weaknesses summary** with supporting data
5. **Valuation gap analysis** — quantified discount/premium to peer average
6. **Key differentiators** — what sets the target apart (positive and negative)

## Data Sources

- **SEC EDGAR** (`sec-edgar`): Financial filings
- **ASX Announcements** (`asx-announcements`): Operational reports
- **S&P Global** (`sp-global-mining`): Standardised peer data
- **Mining.com** (`mining-com`): Industry news and rankings
- **Company investor presentations**: Slide decks, fact sheets
