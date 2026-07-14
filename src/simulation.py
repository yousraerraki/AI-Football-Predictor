import numpy as np

from src.config import (
    DEFAULT_SIMULATIONS,
    DEFAULT_SEED
)


def simulate_matches(
    home_xg: float,
    away_xg: float,
    home_rating: float,
    away_rating: float,
    simulations: int = DEFAULT_SIMULATIONS,
    seed: int = DEFAULT_SEED
):
    """
    Monte Carlo simulation.

    Returns
    -------
    dict
        home_win_90
        draw_90
        away_win_90
        home_qualification
        away_qualification
        representative_scenario
        simulations
    """

    rng = np.random.default_rng(seed)

    # -------------------------
    # 90 minutes
    # -------------------------

    home_goals = rng.poisson(home_xg, simulations)
    away_goals = rng.poisson(away_xg, simulations)

    home_wins = np.sum(home_goals > away_goals)
    draws = np.sum(home_goals == away_goals)
    away_wins = np.sum(home_goals < away_goals)

    # -------------------------
    # Qualification simulation
    # -------------------------

    home_qualified = home_wins
    away_qualified = away_wins

    representative = {
        "regulation": "",
        "extra_time": "",
        "decision": ""
    }

    tied = np.where(home_goals == away_goals)[0]

    if len(tied) > 0:

        extra_home = rng.poisson(home_xg * 0.30, len(tied))
        extra_away = rng.poisson(away_xg * 0.30, len(tied))

        for i in range(len(tied)):

            if extra_home[i] > extra_away[i]:

                home_qualified += 1

            elif extra_home[i] < extra_away[i]:

                away_qualified += 1

            else:

                penalty_probability = (
                    1 /
                    (
                        1 +
                        10 ** (
                            -(home_rating - away_rating) / 800
                        )
                    )
                )

                if rng.random() < penalty_probability:

                    home_qualified += 1

                else:

                    away_qualified += 1

    # -------------------------
    # Representative Scenario
    # -------------------------

    modal_home = int(round(home_xg))
    modal_away = int(round(away_xg))

    representative["regulation"] = (
        f"{modal_home}-{modal_away}"
    )

    if modal_home == modal_away:

        representative["extra_time"] = (
            f"{modal_home}-{modal_away} after extra time"
        )

        if home_qualified >= away_qualified:

            representative["decision"] = (
                "Home team wins on penalties"
            )

        else:

            representative["decision"] = (
                "Away team wins on penalties"
            )

    else:

        representative["extra_time"] = (
            "Not required"
        )

        representative["decision"] = (
            "Winner after 90 minutes"
        )

    # -------------------------
    # Return
    # -------------------------

    return {

        "home_win_90":
            float(home_wins / simulations),

        "draw_90":
            float(draws / simulations),

        "away_win_90":
            float(away_wins / simulations),

        "home_qualification":
            float(home_qualified / simulations),

        "away_qualification":
            float(away_qualified / simulations),

        "representative_scenario":
            representative,

        "simulations":
            simulations

    }