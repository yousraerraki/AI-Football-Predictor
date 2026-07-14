"""
Team Statistics Module

Calculates:
- Attack Strength
- Defence Strength
- Goals per Match
- Bayesian Adjustment
"""

from src.models import Team
from src.config import (
    LEAGUE_AVERAGE_GOALS,
    PRIOR_WEIGHT
)


def goals_scored_per_match(team: Team) -> float:
    """
    Average goals scored per match.
    """

    if team.matches == 0:
        return LEAGUE_AVERAGE_GOALS

    return team.goals_for / team.matches


def goals_conceded_per_match(team: Team) -> float:
    """
    Average goals conceded per match.
    """

    if team.matches == 0:
        return LEAGUE_AVERAGE_GOALS

    return team.goals_against / team.matches


def attack_strength(team: Team) -> float:
    """
    Bayesian attack strength.

    Formula:

    ((Goals + Prior*Weight) /
    (Matches + Weight))
    /
    LeagueAverage
    """

    attack = (

        (

            team.goals_for

            +

            team.prior_attack
            *
            PRIOR_WEIGHT

        )

        /

        (

            team.matches

            +

            PRIOR_WEIGHT

        )

    )

    return attack / LEAGUE_AVERAGE_GOALS


def defence_strength(team: Team) -> float:
    """
    Bayesian defensive strength.

    Lower goals conceded
    -> stronger defence
    """

    defence = (

        (

            team.goals_against

            +

            team.prior_defence
            *
            PRIOR_WEIGHT

        )

        /

        (

            team.matches

            +

            PRIOR_WEIGHT

        )

    )

    defence = defence / LEAGUE_AVERAGE_GOALS

    if defence <= 0:
        defence = 0.05

    return 1 / defence


def team_summary(team: Team):
    """
    Returns every statistic for dashboard.
    """

    return {

        "Team":
            team.name,

        "Matches":
            team.matches,

        "Goals For":
            team.goals_for,

        "Goals Against":
            team.goals_against,

        "Goals/Match":
            round(
                goals_scored_per_match(team),
                3
            ),

        "Conceded/Match":
            round(
                goals_conceded_per_match(team),
                3
            ),

        "Attack Strength":
            round(
                attack_strength(team),
                3
            ),

        "Defence Strength":
            round(
                defence_strength(team),
                3
            ),

        "Rating":
            team.rating,

        "Rest Days":
            team.rest_days

    }


def compare_teams(
    home_team: Team,
    away_team: Team
):
    """
    Compare two teams.
    """

    return {

        "home": team_summary(home_team),

        "away": team_summary(away_team)

    }


if __name__ == "__main__":

    from src.loader import load_teams

    teams = load_teams()

    france = teams["France"]
    spain = teams["Spain"]

    print("\nFrance\n")
    print(team_summary(france))

    print("\nSpain\n")
    print(team_summary(spain))

    print("\nComparison\n")
    print(compare_teams(france, spain))