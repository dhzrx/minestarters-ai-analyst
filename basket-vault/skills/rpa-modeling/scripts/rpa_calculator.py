"""
Revenue Participation Agreement (RPA) cash flow calculator.
Models distributions from mining project revenue to RPA token holders.
"""
import json
import sys
from typing import Any


def calculate_rpa_distributions(
    annual_revenue: list[float],
    participation_rate: float,
    minimum_threshold: float = 0.0,
    cap_multiple: float | None = None,
    total_investment: float = 0.0
) -> dict[str, Any]:
    """
    Calculate RPA distributions over the life of a mining project.

    Args:
        annual_revenue: List of annual gross revenue figures ($M).
        participation_rate: Fraction of revenue paid to RPA holders (e.g., 0.02 = 2%).
        minimum_threshold: Minimum annual revenue before distributions start ($M).
        cap_multiple: Maximum total distributions as multiple of investment (e.g., 3.0 = 3x).
        total_investment: Total capital invested by RPA holders ($M).
    """
    cap_amount = (cap_multiple * total_investment) if cap_multiple and total_investment else None
    cumulative = 0.0
    distributions = []
    capped = False

    for year, revenue in enumerate(annual_revenue, 1):
        if capped:
            distributions.append({
                "year": year,
                "revenue": round(revenue, 2),
                "distribution": 0.0,
                "cumulative": round(cumulative, 2),
                "capped": True
            })
            continue

        eligible_revenue = max(0, revenue - minimum_threshold)
        distribution = eligible_revenue * participation_rate

        if cap_amount and (cumulative + distribution) > cap_amount:
            distribution = cap_amount - cumulative
            capped = True

        cumulative += distribution
        distributions.append({
            "year": year,
            "revenue": round(revenue, 2),
            "distribution": round(distribution, 2),
            "cumulative": round(cumulative, 2),
            "capped": capped
        })

    return {
        "distributions": distributions,
        "total_distributed": round(cumulative, 2),
        "years_active": sum(1 for d in distributions if d["distribution"] > 0),
        "average_annual": round(cumulative / len(annual_revenue), 2) if annual_revenue else 0,
        "cap_reached": capped
    }


def calculate_investor_returns(
    distributions: list[dict],
    total_investment: float,
    discount_rate: float = 0.10
) -> dict[str, Any]:
    """Calculate investor return metrics from RPA distributions."""
    cash_flows = [-total_investment] + [d["distribution"] for d in distributions]

    # NPV
    npv = sum(cf / (1 + discount_rate) ** t for t, cf in enumerate(cash_flows))

    # IRR (Newton-Raphson)
    rate = 0.10
    for _ in range(1000):
        f = sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows))
        df = sum(-t * cf / (1 + rate) ** (t + 1) for t, cf in enumerate(cash_flows))
        if abs(df) < 1e-12:
            break
        new_rate = rate - f / df
        if abs(new_rate - rate) < 0.0001:
            rate = new_rate
            break
        rate = new_rate

    # MOIC
    total_distributions = sum(d["distribution"] for d in distributions)
    moic = total_distributions / total_investment if total_investment > 0 else 0

    # Payback
    cumulative = 0
    payback = None
    for i, d in enumerate(distributions):
        cumulative += d["distribution"]
        if cumulative >= total_investment:
            payback = i + 1
            break

    return {
        "npv": round(npv, 2),
        "irr": round(rate * 100, 2),
        "moic": round(moic, 2),
        "payback_years": payback,
        "total_return": round(total_distributions, 2)
    }


def run_scenarios(
    base_revenue: list[float],
    participation_rate: float,
    total_investment: float,
    minimum_threshold: float = 0.0,
    cap_multiple: float | None = None
) -> dict[str, Any]:
    """Run Bear/Base/Bull scenarios."""
    scenarios = {
        "bear": [r * 0.8 for r in base_revenue],
        "base": base_revenue,
        "bull": [r * 1.2 for r in base_revenue]
    }

    results = {}
    for name, revenue in scenarios.items():
        dist = calculate_rpa_distributions(
            revenue, participation_rate, minimum_threshold, cap_multiple, total_investment
        )
        returns = calculate_investor_returns(dist["distributions"], total_investment)
        results[name] = {
            "distributions": dist,
            "returns": returns
        }

    return results


def main():
    """Read RPA parameters from stdin, calculate distributions, write results to stdout."""
    data = json.load(sys.stdin)

    results = run_scenarios(
        base_revenue=data["annual_revenue"],
        participation_rate=data["participation_rate"],
        total_investment=data.get("total_investment", 0),
        minimum_threshold=data.get("minimum_threshold", 0),
        cap_multiple=data.get("cap_multiple")
    )

    json.dump(results, sys.stdout, indent=2)


if __name__ == "__main__":
    main()
