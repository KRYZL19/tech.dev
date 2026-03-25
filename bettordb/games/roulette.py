def calculate_roulette_odds(variant: str = "european") -> dict:
    """
    Calculate roulette odds.
    European: 37 pockets (0-36), one green
    American: 38 pockets (0-36 + 00), two green
    """
    if variant.lower() == "european":
        pockets = 37
        house_edge = 1 / 37  # ~2.70%
        green_pockets = [0]
    elif variant.lower() == "american":
        pockets = 38
        house_edge = 2 / 38  # ~5.26%
        green_pockets = [0, 37]  # 0 and 00
    else:
        pockets = 37
        house_edge = 1 / 37
        green_pockets = [0]

    return {
        "variant": variant.lower(),
        "house_edge": round(house_edge, 6),
        "pockets": pockets,
        "green_pockets": green_pockets
    }
