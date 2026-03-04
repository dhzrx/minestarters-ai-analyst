---
name: Oracle Verification
description: Design and validate trusted oracle verification workflows for on-chain mining data including reserves, production, and commodity prices.
---

# Oracle Verification

## Purpose

Design verification workflows using trusted oracles to bring real-world mining data on-chain. Ensures that reserve estimates, production data, commodity prices, and compliance attestations are accurately reflected in smart contracts.

## Oracle Data Types

### 1. Reserve Verification Oracle
| Data Point | Source | Update Frequency | Verification Method |
|-----------|--------|-----------------|-------------------|
| Resource estimate (M/I/I) | QP/CP technical report | Annually or on material change | Third-party QP attestation |
| Reserve estimate (P/P) | Feasibility study | Annually | Independent QP review |
| Resource changes | Company announcements | On event | Cross-reference with filings |

### 2. Production Oracle
| Data Point | Source | Update Frequency | Verification Method |
|-----------|--------|-----------------|-------------------|
| Monthly production | Mine site reports | Monthly | Auditor reconciliation |
| Head grade | Assay lab results | Monthly | Independent lab verification |
| Recovery rate | Plant records | Monthly | Mass balance reconciliation |
| Revenue | Sales records | Monthly/quarterly | Audited financial statements |

### 3. Price Oracle
| Data Point | Source | Update Frequency | Verification Method |
|-----------|--------|-----------------|-------------------|
| Gold price | LBMA, Kitco | Daily/real-time | Multi-source aggregation |
| Base metals | LME | Daily | Official LME settlement prices |
| Lithium | Fastmarkets, Asian Metal | Weekly | Multi-source median |
| Rare earths | Asian Metal, SMM | Weekly | Multi-source cross-check |

### 4. Compliance Oracle
| Data Point | Source | Update Frequency | Verification Method |
|-----------|--------|-----------------|-------------------|
| KYC status | KYC provider | On change | Provider API attestation |
| Accreditation | Verification service | Annually | Re-verification check |
| Sanctions | OFAC, EU, UN lists | Daily | Automated screening |

## Oracle Architecture

```
Data Source → Aggregator → Verification Layer → On-Chain Oracle Contract

Where:
  Data Source = Mining companies, exchanges, labs, regulators
  Aggregator = Multi-source data collection and normalization
  Verification Layer = Cross-checks, outlier detection, QP attestation
  Oracle Contract = On-chain data storage with access control
```

### Trust Model
| Model | Trust Assumption | Use Case |
|-------|-----------------|----------|
| Centralized oracle | Trust single operator | Simple price feeds |
| Multi-sig oracle | Trust M-of-N operators | Reserve attestations |
| Chainlink-style | Trust decentralized network | Commodity prices |
| ZK-proof oracle | Trustless (math guarantee) | Future: audited financials |

## Workflow

### Step 1: Define Data Requirements
- Identify all data points needed on-chain
- Determine update frequency and latency tolerance
- Define accuracy requirements and acceptable error margins
- Map data sources for each data point

### Step 2: Design Verification Pipeline
- Select oracle architecture per data type
- Define aggregation rules (median, TWAP, weighted average)
- Set outlier detection thresholds
- Design dispute resolution mechanism

### Step 3: Implement Attestation Process
- For reserve data: QP signs attestation, hash stored on-chain
- For production data: Auditor verifies, multi-sig publishes
- For price data: Aggregate from 3+ sources, reject >5% outliers
- For compliance data: Automated provider API with periodic manual review

### Step 4: Monitor and Alert
- Set up monitoring for oracle data staleness
- Alert on significant deviations from expected values
- Track oracle uptime and reliability metrics
- Periodic audit of oracle accuracy vs. actual values

## Output Format

```
## Oracle Verification Design — [Project/Platform]

### Data Feeds Required
| Data Point | Source(s) | Frequency | Oracle Type |
|-----------|----------|-----------|-------------|
| ...       | ...      | ...       | ...         |

### Verification Pipeline
[Description of verification steps for each data type]

### Trust Model
[Description of chosen trust model with rationale]

### Monitoring & Alerts
| Alert | Condition | Action |
|-------|-----------|--------|
| Data staleness | No update in >24h | Pause dependent operations |
| Price deviation | >5% from 24h TWAP | Flag for manual review |
| Reserve change | >10% change reported | Trigger QP re-attestation |

### Implementation Timeline
[Phased rollout plan]
```
