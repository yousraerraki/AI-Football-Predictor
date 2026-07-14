from math import tanh


def expected_goals(home, away):
    """
    Expected Goals calculation using calibrated factors.
    """

    # -----------------------------
    # Base xG
    # -----------------------------

    home_xg = 1.55
    away_xg = 1.45


    # -----------------------------
    # Attack vs Defence
    # -----------------------------

    attack_diff = home.prior_attack - away.prior_attack

    defence_diff = away.prior_defence - home.prior_defence


    home_xg += attack_diff * 0.30

    home_xg += defence_diff * 0.20



    attack_diff = away.prior_attack - home.prior_attack

    defence_diff = home.prior_defence - away.prior_defence


    away_xg += attack_diff * 0.30

    away_xg += defence_diff * 0.20



    # -----------------------------
    # Rating
    # -----------------------------

    rating_diff = home.rating - away.rating


    rating_effect = tanh(rating_diff / 200.0) * 0.15


    home_xg += rating_effect

    away_xg -= rating_effect



    # -----------------------------
    # Rest Days
    # -----------------------------

    rest_diff = home.rest_days - away.rest_days


    rest_effect = rest_diff * 0.02


    home_xg += rest_effect

    away_xg -= rest_effect



    # -----------------------------
    # Home Advantage
    # -----------------------------

    home_xg += 0.12



    # -----------------------------
    # Limits
    # -----------------------------

    home_xg = max(0.40, min(home_xg, 3.50))

    away_xg = max(0.40, min(away_xg, 3.50))


    return home_xg, away_xg