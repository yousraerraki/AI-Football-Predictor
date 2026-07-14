from copy import deepcopy

from src.models import Team


def apply_model_controls(
    home_team: Team,
    away_team: Team,
    home_rating: int,
    away_rating: int,
    home_rest_days: int,
    away_rest_days: int,
    tactical_edge: int = 0
):
    """
    Apply all sidebar controls before prediction.
    """

    home = deepcopy(home_team)
    away = deepcopy(away_team)

    home.rating = home_rating
    away.rating = away_rating

    home.rest_days = home_rest_days
    away.rest_days = away_rest_days

    # Tactical Edge
    # +10 => +50 rating
    # -10 => -50 rating

    bonus = tactical_edge * 5

    home.rating += bonus
    away.rating -= bonus

    return home, away