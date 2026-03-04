---
name: Compliance Screening
description: Screen mining project tokenizations for KYC/AML, securities law, and jurisdiction-specific regulatory compliance.
---

# Compliance Screening

## Purpose

Evaluate regulatory compliance requirements for tokenizing mining assets. Covers securities law classification, KYC/AML obligations, jurisdiction analysis, and accreditation requirements.

## Compliance Dimensions

### 1. Securities Law Classification
Determine if the token constitutes a security under relevant jurisdictions:

| Test | Jurisdiction | Key Criteria |
|------|-------------|-------------|
| Howey Test | USA | Investment of money, common enterprise, expectation of profits, from efforts of others |
| FCA Assessment | UK | Transferable security or collective investment scheme |
| MiCA Classification | EU | Asset-referenced token, e-money token, or utility token |
| ASIC Guidance | Australia | Financial product test |

### Token Classification Outcomes
| Classification | Implications |
|---------------|-------------|
| Security token | Full securities regulation, restricted investors, prospectus/PPM required |
| Asset-referenced token (MiCA) | MiCA authorization, reserve requirements, redemption rights |
| Utility token | Lighter regulation, broader distribution, but limited financial rights |
| Hybrid | May need to comply with multiple frameworks |

### 2. KYC/AML Requirements
| Level | Requirements | Applicable To |
|-------|-------------|---------------|
| Basic KYC | ID verification, sanctions screening | All token purchases |
| Enhanced KYC | Source of funds, PEP screening | Purchases > $10,000 |
| Institutional KYC | Corporate docs, UBO identification | Entity investors |
| Ongoing monitoring | Transaction monitoring, SAR filing | All accounts |

### 3. Jurisdiction Analysis
For each target jurisdiction, assess:
- Securities regulator requirements (SEC, FCA, ASIC, BaFin, MAS)
- Token offering exemptions available (Reg D, Reg S, Reg A+ in US)
- Cross-border offering restrictions
- Tax treatment of token distributions
- Reporting obligations

### 4. Investor Accreditation
| Jurisdiction | Accredited Investor Threshold |
|-------------|------------------------------|
| USA | $1M net worth (ex. primary residence) or $200K income |
| EU (MiFID) | Professional investor classification |
| UK | High net worth (£250K+) or sophisticated investor |
| Singapore | Accredited investor (S$2M net assets) |
| Australia | Sophisticated investor (A$2.5M net assets) |

## Workflow

### Step 1: Token Classification
- Analyze token rights and structure
- Apply Howey Test and equivalent tests for target jurisdictions
- Determine primary classification (security, ART, utility)
- Document reasoning

### Step 2: Jurisdiction Mapping
- Identify target investor jurisdictions
- Map applicable regulations per jurisdiction
- Identify available exemptions
- List restricted jurisdictions (OFAC sanctions, high-risk)

### Step 3: Compliance Gap Analysis
- Current compliance measures vs. requirements
- KYC/AML provider capabilities
- Smart contract compliance features (transfer restrictions, holding periods)
- Reporting and filing requirements

### Step 4: Recommendations
- Required registrations or filings
- Exemption strategy (e.g., Reg D 506(c) for US accredited investors)
- KYC/AML provider selection criteria
- Ongoing compliance obligations
- Estimated compliance costs

## Output Format

```
## Compliance Assessment — [Project Name]

### Token Classification
| Jurisdiction | Classification | Confidence |
|-------------|---------------|------------|
| USA | Security (Reg D exempt) | High |
| EU | Asset-Referenced Token (MiCA) | High |
| UK | Security Token | Medium |

### Eligible Investor Base
| Jurisdiction | Eligible | Requirements |
|-------------|----------|-------------|
| USA | Accredited only | Reg D 506(c), verification required |
| EU | Qualified investors | MiCA-compliant offering |
| Singapore | Accredited investors | MAS exemption |

### Restricted Jurisdictions
[List with reasons]

### Required Actions
| Action | Priority | Est. Cost | Timeline |
|--------|----------|-----------|----------|
| SEC Form D filing | High | $5-15K | 2-4 weeks |
| MiCA authorization | High | $50-200K | 3-6 months |
| KYC provider integration | High | $20-50K | 4-8 weeks |

### Ongoing Obligations
[List of recurring compliance requirements]
```

## References

See `references/regulatory-frameworks.md` for detailed jurisdiction-by-jurisdiction analysis.
