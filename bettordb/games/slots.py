import numpy as np


def simulate_slots(
    spins: int,
    paylines: int,
    symbol_weights: dict,
    reels: int,
    bet_per_line: float = 1.0
) -> dict:
    """
    Simulate slot machine spins using weighted symbols.
    Returns house edge, RTP, and expected loss.
    """
    symbols = list(symbol_weights.keys())
    weights = np.array(list(symbol_weights.values()))
    probs = weights / weights.sum()

    total_wagered = spins * paylines * bet_per_line
    total_return = 0.0

    rng = np.random.default_rng()

    for _ in range(spins):
        # Spin each reel
        for _ in range(paylines):
            result = rng.choice(symbols, size=reels, p=probs)
            # Simple win: all symbols match (jackpot)
            if len(set(result)) == 1:
                # 10x for jackpot
                total_return += bet_per_line * 10

    rtp = total_return / total_wagered if total_wagered > 0 else 0
    house_edge = 1 - rtp
    expected_loss = total_wagered * house_edge

    return {
        "house_edge": round(house_edge, 6),
        "rtp": round(rtp, 6),
        "expected_loss": round(expected_loss, 4)
    }
