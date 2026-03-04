# AI Mining Analyst Plugins

Plugins that turn Claude into a specialist for mining investment analysis — resource estimation, project valuation, basket construction, RWA tokenization, and commodity intelligence. Built for [Claude Cowork](https://claude.com/product/cowork), also compatible with [Claude Code](https://claude.com/product/claude-code).

## Why Plugins

Cowork lets you set the goal and Claude delivers finished, professional work. Plugins let you go further: tell Claude how your firm does analysis, which data sources to pull from, how to handle critical workflows, and what slash commands to expose — so your team gets better and more consistent outcomes.

Each plugin bundles the skills, connectors, slash commands, and reference materials for a specific mining analysis workflow. Out of the box, they give Claude a strong starting point for helping anyone in the mining investment space. The real power comes when you customize them for your firm — your models, your templates, your processes — so Claude works like it was built for your team.

## What is the AI Mining Analyst?

The AI Mining Analyst is a comprehensive plugin suite built for [Minestarters](https://minestarters.com), a blockchain-based platform for tokenized real-world mining assets (RWAs). It connects Claude to mining data sources and tools — eliminating the need to juggle multiple browser tabs and improving source verification to reduce errors from manual data gathering.

## End-to-End Workflows

These plugins aren't just a collection of point tools — they enable complete workflows that span exploration through tokenization:

- **Exploration to Resource**: Analyze drill results, interpret geological data, classify resources per JORC/NI 43-101, and generate resource statements — all in a single session
- **Project Valuation**: Build DCF models with mining-specific inputs (strip ratios, recovery rates, mine life), run Bear/Base/Bull scenarios, and benchmark against comparable projects
- **Due Diligence**: Run comprehensive DD checklists, assess technical/ESG/political/market risks, evaluate feasibility studies, and model CAPEX/OPEX
- **Basket Construction**: Build diversified mining baskets with allocation constraints, track NAV, generate rebalancing signals, and report vault performance
- **Tokenization**: Structure mining RWAs for tokenization, model ART stablecoin backing and $MINE utility token economics, screen for regulatory compliance
- **Market Intelligence**: Forecast commodity prices, model supply/demand balances, track critical minerals, and compile market briefs

Each workflow connects upstream data sources (via MCP) to downstream outputs, so you move from raw drill data to investment-ready analysis without context-switching.

## Plugin Marketplace

Start with **mining-analysis** — the core plugin that provides shared modeling tools and all MCP data connectors. Then add any function-specific plugins to enhance Claude's capabilities for your workflow.

| Plugin | Type | How it helps | Key Skills |
|--------|------|-------------|------------|
| **[mining-analysis](./mining-analysis)** | Core (install first) | Estimate resources (JORC/NI 43-101), value projects (NPV/IRR/DCF), screen projects, run competitive analysis, validate financial models. Provides the shared foundation and all data connectors. | 6 skills, 5 commands |
| **[exploration](./exploration)** | Add-on | Analyze drill results and assay data, assess regional geology, deep-dive on target minerals, generate exploration reports. | 4 skills, 4 commands |
| **[project-evaluation](./project-evaluation)** | Add-on | Evaluate feasibility studies (PFS/BFS/DFS), run DD checklists, assess risks, find comparable projects, model CAPEX/OPEX. | 5 skills, 5 commands |
| **[basket-vault](./basket-vault)** | Add-on | Build diversified mining baskets, track NAV, rebalance portfolios, report vault performance, model RPA cash flows. | 5 skills, 5 commands |
| **[tokenization](./tokenization)** | Add-on | Model ART stablecoin and $MINE token economics, structure RWAs for tokenization, screen compliance, design oracle verification. | 4 skills, 4 commands |
| **[commodity-intelligence](./commodity-intelligence)** | Add-on | Forecast commodity prices, model supply/demand, track critical minerals, compile market briefs. | 4 skills, 4 commands |

**28 skills, 27 commands, 8 MCP integrations, 3 Python utilities**

Install these directly from Cowork, browse the full collection here on GitHub, or build your own.

## Getting Started

### Cowork

Install plugins from [claude.com/plugins](https://claude.com/plugins/).

### Claude Code

```bash
# Add the marketplace
claude plugin marketplace add dhzrx/minestarters-ai-analyst

# Install the core plugin first (required)
claude plugin install mining-analysis@minestarters-ai-analyst

# Then add function-specific plugins as needed
claude plugin install exploration@minestarters-ai-analyst
claude plugin install project-evaluation@minestarters-ai-analyst
claude plugin install basket-vault@minestarters-ai-analyst
claude plugin install tokenization@minestarters-ai-analyst
claude plugin install commodity-intelligence@minestarters-ai-analyst
```

Once installed, plugins activate automatically. Skills fire when relevant, and slash commands are available in your session:

```bash
# Core analysis
/resource-estimate [project]       # JORC/NI 43-101 resource estimation
/mineral-valuation [project]       # NPV/IRR/DCF valuation
/project-screen [criteria]         # Screen projects against criteria
/competitive-analysis [company]    # Benchmark against peers
/debug-model [file]                # Validate financial models

# Exploration
/drill-analysis [project]          # Analyze drill hole data
/geo-assessment [region]           # Geological prospectivity assessment
/target-minerals [mineral]         # Deep mineral analysis (Li, Cu, Au, REE...)
/exploration-report [project]      # Generate exploration report

# Project evaluation
/feasibility [project]             # Analyze feasibility studies
/dd-checklist [project]            # Due diligence checklist
/risk-assessment [project]         # Comprehensive risk scoring
/comps [project]                   # Comparable project analysis
/capex-opex [project]              # Cost modeling and benchmarking

# Basket & vault
/create-basket [name]              # Build diversified mining basket
/nav-tracker [basket]              # Calculate NAV
/rebalance [basket]                # Generate rebalancing trades
/vault-report [vault]              # Vault performance report
/rpa-model [project]               # Model RPA cash flows

# Tokenization
/token-model [project]             # Token economics modeling
/art-analysis                      # ART stablecoin analysis
/mine-analysis                     # $MINE utility token analysis
/compliance-check [project]        # Regulatory compliance screening

# Commodity intelligence
/price-forecast [commodity]        # Price forecasting (Bear/Base/Bull)
/supply-demand [mineral]           # Supply/demand modeling
/critical-minerals                 # Critical minerals tracker
/market-brief                      # Mining market intelligence
```

## How Plugins Work

Every plugin follows the same structure:

```
plugin-name/
├── .claude-plugin/plugin.json   # Manifest
├── hooks/hooks.json             # Hook configurations
├── commands/                    # Slash commands you invoke explicitly
└── skills/                      # Domain knowledge Claude draws on automatically
    └── skill-name/
        ├── SKILL.md             # Workflow definition
        ├── references/          # Reference material
        └── scripts/             # Python validation utilities
```

- **Skills** encode mining domain expertise, industry standards (JORC, NI 43-101), and step-by-step workflows Claude needs to deliver professional-quality analysis. Claude draws on them automatically when relevant.
- **Commands** are explicit actions you trigger (e.g., `/resource-estimate`, `/feasibility`, `/create-basket`).
- **Connectors** wire Claude to external mining data sources — geological databases, commodity exchanges, regulatory filings, and more — via [MCP servers](https://modelcontextprotocol.io/).
- **Reference docs** provide detailed standards, benchmarks, and guidelines that skills reference during analysis.
- **Python scripts** validate outputs independently (NPV/IRR calculations, feasibility study completeness, RPA cash flows).

Every component is file-based — markdown and JSON, no code, no infrastructure, no build steps.

## MCP Integrations

All connectors are centralized in the **mining-analysis** core plugin and shared across all add-on plugins.

| Provider | URL | Data Coverage |
|----------|-----|---------------|
| [USGS](https://www.usgs.gov/) | `https://mrdata.usgs.gov/` | Mineral resources, geological data, commodity statistics |
| [London Metal Exchange](https://www.lme.com/) | `https://www.lme.com/api/` | Base metals pricing (Cu, Al, Zn, Ni, Pb, Sn) |
| [Kitco](https://www.kitco.com/) | `https://www.kitco.com/` | Precious metals (Au, Ag, Pt, Pd) |
| [S&P Global](https://www.spglobal.com/) | `https://www.spglobal.com/marketintelligence/` | Mining company data, project databases |
| [Mining.com](https://www.mining.com/) | `https://www.mining.com/` | Mining news, project data |
| [SEC EDGAR](https://www.sec.gov/edgar) | `https://efts.sec.gov/LATEST/` | US mining company filings |
| [ASX](https://www.asx.com.au/) | `https://www.asx.com.au/` | Australian mining announcements |
| [Mining Intelligence](https://www.mining-technology.com/) | `https://www.mining-technology.com/` | Cost data, benchmarks |

> Some MCP integrations are placeholders for future MCP server availability. Skills include fallback instructions using web search and direct API calls where MCP endpoints are not yet active. Providers marked with subscription requirements need separate access.

## Python Utilities

Three validation scripts are included for independent verification of calculations:

| Script | Location | Purpose |
|--------|----------|---------|
| `validate_npv.py` | `mining-analysis/skills/mineral-valuation/scripts/` | Validates NPV, IRR (Newton-Raphson), and payback period calculations |
| `validate_feasibility.py` | `project-evaluation/skills/feasibility-study/scripts/` | Checks feasibility study completeness, economics, and contingency adequacy |
| `rpa_calculator.py` | `basket-vault/skills/rpa-modeling/scripts/` | Calculates RPA distributions with Bear/Base/Bull scenarios |

All scripts read JSON from stdin and write results to stdout:

```bash
echo '{"cash_flows": [10, 15, 20, 25, 30], "discount_rate": 0.08, "initial_investment": 50}' | python mining-analysis/skills/mineral-valuation/scripts/validate_npv.py
```

## Mining Standards Covered

| Standard | Coverage | Plugin |
|----------|----------|--------|
| **JORC Code (2012)** | Resource/reserve classification, Competent Person requirements, Table 1 reporting | mining-analysis |
| **NI 43-101** | Canadian mineral project disclosure, Qualified Person, technical reports | mining-analysis |
| **CIM Standards** | Resource/reserve definitions aligned with NI 43-101 | mining-analysis |
| **CRIRSCO** | International reporting template alignment | mining-analysis |

## Making Them Yours

These plugins are starting points. They become much more useful when you customize them for how your firm actually works:

- **Swap connectors** — Edit `.mcp.json` to point at your specific data providers and internal tools.
- **Add firm context** — Drop your terminology, deal processes, and formatting standards into skill files so Claude understands your world.
- **Adjust workflows** — Modify skill instructions to match how your team actually does analysis.
- **Add commodities** — Extend the `target-mineral-analysis` skill with minerals specific to your portfolio.
- **Customize screening** — Update project screening criteria and weightings in `project-screening/SKILL.md` to match your investment mandate.
- **Build new plugins** — Follow the structure above to create plugins for workflows we haven't covered yet (e.g., mine operations, ESG reporting, investor relations).

## Contributing

Plugins are just markdown files. Fork the repo, make your changes, and submit a PR. For new skills or plugins, include:

- A `SKILL.md` with clear trigger conditions and workflow steps
- A corresponding command in `commands/` if user-invocable
- Updated plugin manifest if adding new capabilities

## License

[MIT License](./LICENSE)

## Disclaimer

These plugins assist with mining analysis workflows but do not provide financial, investment, or geological advice. All resource estimates, valuations, and forecasts should be reviewed by qualified professionals (Competent Persons, Qualified Persons, financial advisors) before being relied upon for investment decisions. AI-generated analysis is a starting point, not a substitute for professional judgment.
