---
name: "Check Model"
description: "Validate and debug mining financial models by checking for formula errors, circular references, unrealistic assumptions, and missing inputs."
---

# Check Model

## Purpose

Analyse a mining financial model (typically an Excel workbook or structured data) to identify errors, inconsistencies, and unrealistic assumptions. This skill acts as an automated model auditor, producing a prioritised list of issues with suggested fixes to improve model reliability before it is used for investment decisions.

## Validation Checks

### 1. Structural Checks

| Check | Description | Severity |
|-------|-------------|----------|
| **Formula errors** | #REF!, #VALUE!, #DIV/0!, #NAME? errors | Critical |
| **Circular references** | Cells that directly or indirectly reference themselves | Critical |
| **Hard-coded values in formulas** | Numbers embedded in formulas that should be input cells | Warning |
| **Inconsistent formulas** | Formulas that differ within a row/column that should be uniform | Warning |
| **Broken links** | References to external workbooks that are missing | Critical |
| **Hidden rows/columns** | Hidden content that may contain overrides or errors | Warning |
| **Unprotected input cells** | Input cells that lack validation or protection | Info |

### 2. Assumption Validation

Compare model assumptions against industry benchmarks and flag outliers:

| Assumption | Typical Range | Flag If |
|-----------|---------------|---------|
| **Gold grade (open pit)** | 0.5 - 5.0 g/t | < 0.3 or > 10 g/t |
| **Gold grade (underground)** | 2.0 - 15.0 g/t | < 1.0 or > 30 g/t |
| **Copper grade** | 0.3 - 2.0% | < 0.2 or > 5.0% |
| **Recovery rate** | 75 - 95% | < 60% or > 99% |
| **Strip ratio (open pit)** | 2:1 - 10:1 | < 1:1 or > 15:1 |
| **Mining cost (open pit)** | $1.50 - $4.00/t mined | < $1.00 or > $6.00 |
| **Processing cost** | $5 - $25/t processed | < $3 or > $50 |
| **CAPEX intensity** | Varies by commodity | Compare to analogues |
| **Discount rate** | 5 - 15% | < 3% or > 20% |
| **Mine life** | 5 - 30 years | < 3 or > 40 years |
| **Inflation rate** | 0 - 5% | < 0% or > 8% |
| **Tax rate** | Per jurisdiction | Compare to statutory rate |

### 3. Cash Flow Checks

| Check | Description | Severity |
|-------|-------------|----------|
| **Sign convention** | Revenue positive, costs negative (or consistent alternative) | Critical |
| **Cash flow balance** | Opening cash + net cash flow = closing cash (each period) | Critical |
| **NPV vs sum of DCF** | NPV formula result matches manual sum of discounted cash flows | Critical |
| **IRR reasonableness** | IRR consistent with NPV sign (positive NPV = IRR > discount rate) | Warning |
| **Terminal value** | No residual value unless justified (closure costs included) | Warning |
| **Working capital** | Working capital changes included in cash flow | Warning |
| **Depreciation** | Depreciation schedule matches CAPEX and asset lives | Warning |
| **Tax loss carry-forward** | Tax losses carried forward correctly, not lost | Warning |

### 4. Sensitivity and Scenario Checks

| Check | Description | Severity |
|-------|-------------|----------|
| **Sensitivity table integrity** | Sensitivity outputs change when inputs change | Critical |
| **Scenario consistency** | Bear < Base < Bull for price, costs reverse | Warning |
| **Tornado chart accuracy** | Variables ranked correctly by NPV impact | Warning |
| **Break-even calculations** | Break-even price/grade consistent with model | Warning |

### 5. Completeness Checks

| Check | Description | Severity |
|-------|-------------|----------|
| **Missing line items** | Common items absent (closure costs, working capital, sustaining CAPEX) | Warning |
| **Missing royalties** | Government or private royalties not included | Critical |
| **Missing taxes** | Income tax, withholding tax not modelled | Critical |
| **No contingency** | CAPEX without contingency allowance | Warning |
| **No escalation** | Multi-year model with no cost escalation | Info |
| **No ramp-up** | Production starts at full capacity with no ramp period | Warning |

## Workflow

### Step 1: Load Model

- Accept file path, URL, or structured data reference
- Parse model structure (worksheets, named ranges, input/output areas)
- Identify model type (scoping study, PFS, DFS, operating mine)

### Step 2: Run Structural Checks

- Scan all formulas for errors and inconsistencies
- Detect circular references
- Identify hard-coded values in formula cells
- Check for broken external links
- Flag hidden rows, columns, and sheets

### Step 3: Validate Assumptions Against Benchmarks

- Extract key assumptions from input sheets
- Compare each assumption to industry benchmarks (see table above)
- Flag assumptions outside expected ranges
- Cross-reference commodity-specific cost curves

### Step 4: Cross-Check Calculations

- Verify NPV calculation independently (use `scripts/validate_npv.py`)
- Confirm IRR is consistent with NPV
- Check cash flow balance (opening + net = closing)
- Validate tax and royalty calculations against statutory rates
- Confirm depreciation schedules

### Step 5: Report Findings

Generate a structured issue report sorted by severity.

## Output Format

### Issue Report

| # | Severity | Category | Location | Description | Suggestion |
|---|----------|----------|----------|-------------|------------|
| 1 | Critical | Formula | Sheet1!D15 | #REF! error in revenue calculation | Fix cell reference to price input |
| 2 | Critical | Cash Flow | CF!B30 | NPV formula differs from sum of DCF by $2.3M | Recalculate NPV or check discount periods |
| 3 | Warning | Assumption | Inputs!C8 | Recovery rate of 98% exceeds typical range | Verify with metallurgical testwork |
| 4 | Warning | Completeness | - | No mine closure costs included | Add closure cost estimate ($X-YM typical) |
| 5 | Info | Style | Various | 12 hard-coded values in formula cells | Move to input section for transparency |

### Summary Statistics

```
Total issues found: 15
  Critical: 3
  Warning:  8
  Info:     4

Model health score: 72/100
Recommendation: Address critical issues before use in investment decisions.
```

## References

- Mineral valuation skill `scripts/validate_npv.py` for independent NPV/IRR verification
- `references/cost-curves.md` for assumption benchmarking
- `references/discount-rates.md` for discount rate validation
