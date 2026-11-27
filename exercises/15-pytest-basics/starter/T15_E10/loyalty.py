"""Loyalty points for a coffee shop. This is the code under test: do not change it."""

REWARDS = {"coffee": 100, "sandwich": 250, "mug": 600}

TIER_MULTIPLIERS = {"bronze": 1, "silver": 2, "gold": 3}


def points_for_purchase(amount, tier="bronze"):
    """One point per whole currency unit spent, times the tier multiplier."""
    if amount < 0:
        raise ValueError("amount cannot be negative")
    if tier not in TIER_MULTIPLIERS:
        raise ValueError(f"unknown tier: {tier}")
    return int(amount) * TIER_MULTIPLIERS[tier]


def tier_for_points(total_points):
    """bronze below 500 points, silver below 2000, gold from 2000."""
    if total_points < 0:
        raise ValueError("points cannot be negative")
    if total_points >= 2000:
        return "gold"
    if total_points >= 500:
        return "silver"
    return "bronze"


def redeem(total_points, reward):
    """Spend points on a reward and return the points left."""
    if reward not in REWARDS:
        raise KeyError(f"no such reward: {reward}")
    cost = REWARDS[reward]
    if total_points < cost:
        raise ValueError(f"need {cost} points, have {total_points}")
    return total_points - cost


def summary(total_points):
    """A one-line description of the member's status."""
    tier = tier_for_points(total_points)
    affordable = [name for name, cost in REWARDS.items() if cost <= total_points]
    if not affordable:
        return f"{tier}: {total_points} points, no rewards available yet"
    best = max(affordable, key=lambda name: REWARDS[name])
    return f"{tier}: {total_points} points, best reward: {best}"
