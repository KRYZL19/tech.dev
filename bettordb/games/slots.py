"""
Slot machine simulator using weighted reel simulation.
"""
import numpy as np
from typing import List, Optional


def simulate_slots(
    spins: int,
    paylines: int,
    symbol_weights: List[float],
    reels: int,
    symbol_values: Optional[List[float]] = None,
    bet_per_line: float = 1.0,
) -> dict:
    """
    Simulate slot machine spins with weighted symbols.

    Args:
        spins: Number of spins to simulate
        paylines: Number of active paylines
        symbol_weights: Relative weights for each symbol (e.g. [10, 5, 2, 1])
        reels: Number of reels
        symbol_values: Payout multiplier for each symbol (same length as symbol_weights)
        bet_per_line: Bet amount per payline

    Returns:
        dict with house_edge, rtp, expected_loss, confidence_interval
    """
    n_symbols = len(symbol_weights)
    weights = np.array(symbol_weights, dtype=float)
    weights = weights / weights.sum()

    if symbol_values is None:
        symbol_values = [float(i + 1) for i in range(n_symbols)]
    else:
        symbol_values = list(symbol_values)

    # Payout table: matching all reels pays symbol_values[i]^reels ratio
    # For simplicity: if all reels match symbol i, win = symbol_values[i] * bet
    payouts = []
    for i, val in enumerate(symbol_values):
        payout_multiplier = val * (0.5 if reels > 3 else 1.0)
        payouts.append(payout_multiplier)

    max_payout = max(payouts)

    # Simulate
    total_wins = 0.0
    total_bets = spins * paylines * bet_per_line

    # Precompute symbol indices
    symbol_indices = np.arange(n_symbols)

    # Batch simulation for speed
    batch_size = min(spins, 50_000)
    n_batches = (spins + batch_size - 1) // batch_size

    win_samples = []

    for batch in range(n_batches):
        current_batch_size = min(batch_size, spins - batch * batch_size)

        # Generate random reel results
        rng = np.random.default_rng()
        results = rng.choice(symbol_indices, size=(current_batch_size, reels), p=weights)

        # Check for all-matching symbols (jackpot)
        for reel_result in results:
            if np.all(reel_result == reel_result[0]):
                sym_idx = reel_result[0]
                total_wins += payouts[sym_idx] * paylines * bet_per_line
                win_samples.append(payouts[sym_idx] * paylines * bet_per_line)
            else:
                win_samples.append(0.0)

    win_samples = np.array(win_samples[:spins])
    rtp = (total_wins / total_bets) * 100 if total_bets > 0 else 0
    house_edge = 100 - rtp

    # Confidence interval using binomial proportion
    p_hat = total_wins / total_bets if total_bets > 0 else 0
    se = np.sqrt(p_hat * (1 - p_hat) / spins)
    ci_lower = max(0, (p_hat - 1.96 * se)) * 100
    ci_upper = min(1, (p_hat + 1.96 * se)) * 100

    expected_loss_per_100 = house_edge  # per $100 wagered

    return {
        "house_edge_percent": round(house_edge, 4),
        "rtp_percent": round(rtp, 4),
        "expected_loss_per_100_dollars": round(expected_loss_per_100, 4),
        "confidence_interval": {
            "lower": round(ci_lower, 4),
            "upper": round(ci_upper, 4),
            "level": "95%",
        },
        "total_spins": spins,
        "actual_simulations": spins,
    }
