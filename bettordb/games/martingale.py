import numpy as np


def simulate_betting_system(
    system: str,
    base_bet: float,
    target_wins: int,
    max_bets: int,
    bankroll: float,
    win_probability: float = 0.475,
    n_simulations: int = 10000,
    seed: int = 42
) -> dict:
    """
    Simulate a betting system (martingale/fibonacci/dalembert/flat).
    Returns ruin vs success rates, expected value, median ending bankroll, worst case.
    """
    rng = np.random.default_rng(seed)
    system = system.lower()

    results = []
    target_bankroll = bankroll + (base_bet * target_wins)

    for _ in range(n_simulations):
        bal = float(bankroll)
        current_bet = float(base_bet)
        wins_needed = target_wins
        sequence = []

        for step in range(max_bets):
            # Determine bet size based on system
            if system == "martingale":
                if sequence and sequence[-1] == 0:
                    current_bet = min(current_bet * 2, bal)
                else:
                    current_bet = float(base_bet)
            elif system == "fibonacci":
                if len(sequence) >= 2 and sequence[-1] == 0 and sequence[-2] == 0:
                    # Lost twice: move back two in fibonacci
                    # We'll keep it simple: after loss, increase by fib ratio
                    current_bet = min(current_bet + (current_bet - base_bet) if current_bet > base_bet else base_bet, bal)
                elif sequence and sequence[-1] == 1:
                    # Won: reset
                    current_bet = float(base_bet)
                else:
                    current_bet = min(current_bet, bal)
            elif system == "dalembert":
                if sequence and sequence[-1] == 0:
                    current_bet = min(current_bet + base_bet * 0.5, bal)
                else:
                    current_bet = max(current_bet - base_bet * 0.5, base_bet)
            elif system == "flat":
                current_bet = min(float(base_bet), bal)
            else:
                current_bet = min(float(base_bet), bal)

            current_bet = max(min(current_bet, bal), 0.01)

            # Flip
            win = rng.random() < win_probability

            if win:
                bal += current_bet
                wins_needed -= 1
                sequence.append(1)
                if wins_needed <= 0:
                    break
            else:
                bal -= current_bet
                sequence.append(0)
                if bal <= 0:
                    break

        results.append(bal)

    results = np.array(results)
    prob_ruin = np.mean(results <= 0)
    prob_success = np.mean(results >= target_bankroll)
    # prob_reaching_target counts anyone who reached target before ruin or max bets
    # Be more precise: reached target without going bust
    prob_reaching_target = np.mean((results >= target_bankroll))

    expected_value = float(np.mean(results) - bankroll)
    median_ending = float(np.median(results))
    worst_case = float(np.min(results))

    return {
        "system": system,
        "prob_reaching_target": round(prob_reaching_target, 6),
        "prob_ruin": round(prob_ruin, 6),
        "expected_value": round(expected_value, 4),
        "median_ending_bankroll": round(median_ending, 4),
        "worst_case": round(worst_case, 4),
        "n_simulations": n_simulations
    }
