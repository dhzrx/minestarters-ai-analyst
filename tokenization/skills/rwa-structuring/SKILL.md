---
name: RWA Structuring
description: Structure mining real-world assets for tokenization including SPV design, legal wrappers, and token-to-asset mapping.
---

# RWA Structuring

## Purpose

Design the legal and technical structure for tokenizing mining assets on the Minestarters platform. Covers SPV formation, token-to-asset mapping, custody arrangements, and regulatory wrappers.

## Structuring Components

### 1. Special Purpose Vehicle (SPV)
- **Jurisdiction**: Typically Cayman Islands, BVI, Singapore, or Delaware
- **Purpose**: Hold the mining asset or rights; issue tokens against it
- **Structure**: LLC or Ltd company with token holders as beneficial owners
- **Governance**: Board or manager with fiduciary duties to token holders

### 2. Asset Wrapper
| Asset Type | Wrapper | Token Represents |
|-----------|---------|-----------------|
| Operating mine | Revenue share (RPA) | Right to % of gross revenue |
| Development project | Equity + revenue share | Proportional ownership + RPA |
| Mineral rights | Royalty stream | Right to royalty payments |
| Exploration property | Equity interest | Proportional ownership of SPV |

### 3. Token-to-Asset Mapping
- Each token represents a defined fractional interest in the SPV
- Token metadata includes: asset ID, SPV reference, interest type, rights
- Transfer restrictions encoded in smart contract (compliance checks)
- Dividend/distribution mechanics automated via smart contract

### 4. Custody & Verification
- Mining asset held by SPV (title registered with mining registry)
- Independent verification of reserves/resources (QP/CP sign-off)
- Regular audits (financial + technical)
- Oracle-based verification for on-chain data (see `oracle-verification` skill)

## Workflow

### Step 1: Asset Assessment
- Identify the mining asset to be tokenized
- Determine asset type and appropriate wrapper structure
- Assess legal title and encumbrances
- Review existing obligations (royalties, JV agreements, offtake contracts)

### Step 2: SPV Design
- Select jurisdiction based on tax efficiency, regulatory clarity, investor base
- Design SPV structure (single asset or multi-asset)
- Define governance framework
- Engage legal counsel for formation

### Step 3: Token Design
- Define token standard (ERC-20, ERC-1400 for securities, ERC-3643 for regulated tokens)
- Encode transfer restrictions (whitelist, holding period, max holders)
- Define distribution mechanics
- Set up compliance oracle integration

### Step 4: Documentation
- Private Placement Memorandum (PPM) or offering circular
- Subscription agreement
- SPV operating agreement
- Token holder rights agreement
- Technical report summary (for mining asset)

### Step 5: Launch Preparation
- KYC/AML onboarding setup
- Investor accreditation verification
- Smart contract audit
- Listing on Minestarters platform

## Output Format

```
## RWA Structure — [Project Name]

### Asset Summary
| Field | Value |
|-------|-------|
| Asset Type | [Operating Mine/Development/Exploration] |
| Commodity | [Primary commodity] |
| Location | [Country, region] |
| Valuation | $XXM |

### Structure
| Component | Detail |
|-----------|--------|
| SPV Jurisdiction | [Country] |
| SPV Type | [LLC/Ltd] |
| Token Standard | [ERC-20/ERC-1400/ERC-3643] |
| Token Represents | [Revenue share/Equity/Royalty] |
| Total Tokens | XXX,XXX |
| Token Price | $XX.XX |
| Raise Target | $XXM |

### Investor Rights
[List of rights encoded in token holder agreement]

### Compliance Requirements
[KYC/AML, accreditation, jurisdiction restrictions]

### Timeline
| Milestone | Target Date |
|-----------|------------|
| SPV formation | ... |
| Legal documentation | ... |
| Smart contract audit | ... |
| Token launch | ... |
```
