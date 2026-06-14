def calculate_costs(crop, land_size):
    total_cost = 0
    breakdown = {}

    for item, cost in crop["costs"].items():
        total = cost * land_size
        breakdown[item] = total
        total_cost += total

    return total_cost, breakdown


def calculate_profit(crop, land_size):
    yield_total = crop["yield_per_acre"] * land_size
    revenue = yield_total * crop["price_per_kg"]

    total_cost, breakdown = calculate_costs(crop, land_size)

    profit = revenue - total_cost

    return {
        "yield": yield_total,
        "revenue": revenue,
        "total_cost": total_cost,
        "profit": profit,
        "cost_breakdown": breakdown
    }