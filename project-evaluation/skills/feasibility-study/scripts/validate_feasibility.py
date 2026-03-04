"""
Validate feasibility study completeness and key metrics.
Checks that all required sections are present and economic metrics are reasonable.
"""
import json
import sys
from typing import Any


REQUIRED_SECTIONS = [
    "resource_estimate",
    "mining_method",
    "metallurgy",
    "infrastructure",
    "environmental",
    "capex",
    "opex",
    "revenue_model",
    "financial_model",
    "sensitivity_analysis",
    "risk_register",
    "implementation_schedule"
]

STUDY_ACCURACY = {
    "scoping": {"capex_range": 0.50, "contingency_min": 0.25},
    "pfs": {"capex_range": 0.30, "contingency_min": 0.15},
    "bfs": {"capex_range": 0.15, "contingency_min": 0.05},
    "dfs": {"capex_range": 0.15, "contingency_min": 0.05}
}


def check_completeness(study: dict) -> dict[str, Any]:
    """Check that all required sections are present."""
    present = []
    missing = []
    for section in REQUIRED_SECTIONS:
        if section in study and study[section]:
            present.append(section)
        else:
            missing.append(section)
    return {
        "score": f"{len(present)}/{len(REQUIRED_SECTIONS)}",
        "present": present,
        "missing": missing,
        "complete": len(missing) == 0
    }


def validate_economics(study: dict) -> dict[str, Any]:
    """Validate key economic metrics are within reasonable ranges."""
    issues = []
    financials = study.get("financial_model", {})

    irr = financials.get("irr")
    if irr is not None:
        if irr < 0:
            issues.append({"field": "irr", "severity": "critical", "message": "Negative IRR indicates project is uneconomic"})
        elif irr > 100:
            issues.append({"field": "irr", "severity": "warning", "message": f"IRR of {irr}% is unusually high — verify assumptions"})

    npv = financials.get("npv")
    capex = study.get("capex", {}).get("total")
    if npv is not None and capex is not None and capex > 0:
        npv_to_capex = npv / capex
        if npv_to_capex < 0:
            issues.append({"field": "npv", "severity": "critical", "message": "Negative NPV — project does not meet hurdle rate"})
        elif npv_to_capex > 5:
            issues.append({"field": "npv", "severity": "warning", "message": f"NPV/Capex ratio of {npv_to_capex:.1f}x is unusually high"})

    payback = financials.get("payback_years")
    if payback is not None and payback > 10:
        issues.append({"field": "payback", "severity": "warning", "message": f"Payback of {payback} years is long for mining projects"})

    mine_life = study.get("mining_method", {}).get("mine_life_years")
    if mine_life is not None and payback is not None:
        if payback > mine_life * 0.7:
            issues.append({"field": "payback", "severity": "critical", "message": "Payback exceeds 70% of mine life"})

    return {"issues": issues, "valid": len([i for i in issues if i["severity"] == "critical"]) == 0}


def validate_contingency(study: dict) -> dict[str, Any]:
    """Check contingency is appropriate for study stage."""
    stage = study.get("study_stage", "pfs").lower()
    accuracy = STUDY_ACCURACY.get(stage, STUDY_ACCURACY["pfs"])

    capex = study.get("capex", {})
    contingency = capex.get("contingency", 0)
    total = capex.get("total", 0)

    if total > 0:
        contingency_pct = contingency / (total - contingency) if total != contingency else 0
        min_required = accuracy["contingency_min"]
        adequate = contingency_pct >= min_required
        return {
            "stage": stage,
            "contingency_pct": round(contingency_pct * 100, 1),
            "minimum_required_pct": round(min_required * 100, 1),
            "adequate": adequate,
            "message": "Contingency adequate" if adequate else f"Contingency too low for {stage} stage"
        }
    return {"stage": stage, "adequate": False, "message": "No capex data provided"}


def main():
    """Read study JSON from stdin, validate, write results to stdout."""
    study = json.load(sys.stdin)
    results = {
        "completeness": check_completeness(study),
        "economics": validate_economics(study),
        "contingency": validate_contingency(study)
    }
    json.dump(results, sys.stdout, indent=2)


if __name__ == "__main__":
    main()
