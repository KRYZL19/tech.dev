"""
Betting system simulator (Martingale, Fibonacci, D'Alembert, Flat).
Monte Carlo simulation with configurable number of sequences.
"""
import numpy as np
from typing import Literal


def simulate_betting_system(
    system: Literal["martingale", "fibonacci", "dalembert", "flat"],
    base_bet: float,
    target_wins: int,
    max_bets: int,
    bankroll: float,
    win_probability: float = 0.4768,
    payout: float = 2.0,
    n_simulations: int = 10_000,
) -> dict:
    """
    Simulate a betting system over many sequences.

    Args:
        system: Betting system name
        base_bet: Starting bet size
        target_wins: Number of wins needed to reach goal
        max_bets: Maximum bets per sequence
        bankroll: Starting bankroll
        win_probability: Probability of winning each bet
        payout: Decimal payout on win (2.0 = even money)
        n_simulations: Number of sequences to simulate

    Returns:
        dict with probabilities and statistics
    """
    rng = np.random.default_rng()

    # Target bankroll = initial bankroll + target_wins * base_bet * payout
    target_bankroll = bankroll + (target_wins * base_bet * payout)
    target_bankroll = float(target_bankroll)

    final_bankrolls = []
    reached_target = 0
    ruined = 0
    bets_placed_list = []
    worst_idx = 0
    worst_peak_dd = 0.0

    for sim in range(n_simulations):
        br = float(bankroll)
        current_bet = float(base_bet)
        bets_placed = 0
        wins_count = 0
        peak_bankroll = br
        peak_drawdown = 0.0

        # Track sequence for this simulation
        fib_seq = [1, 1]
        dalembert_step = 0

        for _ in range(max_bets):
            if br < current_bet:
                # Can't bet anymore
                break

            bets_placed += 1
            br -= current_bet

            # Win?
            if rng.random() < win_probability:
                br += current_bet * payout
                wins_count += 1

                if wins_count >= target_wins:
                    # Reached target!
                    break

                # Reset for next system
                if system == "martingale":
                    current_bet = float(base_bet)
                elif system == "fibonacci":
                    fib_seq = [1, 1]
                elif system == "dalembert":
                    dalembert_step = max(0, dalembert_step - 1)
                    current_bet = float(base_bet) + dalembert_step * float(base_bet) * 0.5
                # flat: current_bet stays same
            else:
                # Loss
                if system == "martingale":
                    current_bet = min(current_bet * 2, br)
                elif system == "fibonacci":
                    if len(fib_seq) == 2:
                        fib_seq.append(fib_seq[-1] + fib_seq[-2])
                    else:
                        fib_seq = fib_seq[1:] + [fib_seq[-1] + fib_seq[-2]]
                    current_bet = min(float(fib_seq[-1]) * float(base_bet), br)
                elif system == "dalembert":
                    dalembert_step += 1
                    current_bet = min(
                        float(base_bet) + dalembert_step * float(base_bet) * 0.5,
                        br
                    )
                # flat: current_bet stays same

            # Track peak and drawdown
            if br > peak_bankroll:
                peak_bankroll = br
            current_dd = (peak_bankroll - br) / peak_bankroll if peak_bankroll > 0 else 0
            if current_dd > peak_drawdown:
                peak_drawdown = current_dd

        final_bankrolls.append(br)
        bets_placed_list.append(bets_placed)

        if wins_count >= target_wins:
            reached_target += 1

        if br <= 0 or br < target_bankroll - bankroll:
            ruined += 1

        if peak_drawdown > worst_peak_dd:
            worst_peak_dd = peak_drawdown
            worst_idx = sim

    final_bankrolls = np.array(final_bankrolls)
    expected_value = float(np.mean(final_bankrolls)) - bankroll

    worst_case = {
        "final_bankroll": round(final_bankrolls[worst_idx], 2),
        "bets_placed": int(bets_placed_list[worst_idx]),
        "peak_drawdown_percent": round(worst_peak_dd * 100, 2),
    }

    return {
        "probability_of_reaching_target": round(reached_target / n_simulations, 4),
        "probability_of_ruin": round(ruined / n_simulations, 4),
        "expected_value": round(expected_value, 2),
        "median_ending_bankroll": round(float(np.median(final_bankrolls)), 2),
        "mean_ending_bankroll": round(float(np.mean(final_bankrolls)), 2),
        "worst_case_simulation": worst_case,
        "simulations_run": n_simulations,
    }
