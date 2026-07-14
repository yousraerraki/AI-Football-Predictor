"""
Poisson model for football score prediction
"""

import math
import numpy as np

from src.config import MAX_GOALS


def poisson_probability(lmbda: float, goals: int) -> float:
    """
    Poisson probability:
    P(X = goals)
    """

    return (
        math.exp(-lmbda)
        * (lmbda ** goals)
        / math.factorial(goals)
    )


def score_matrix(
    home_xg: float,
    away_xg: float,
    max_goals: int = MAX_GOALS
):
    """
    Build exact-score probability matrix.
    """

    matrix = np.zeros(
        (max_goals + 1, max_goals + 1)
    )

    for home in range(max_goals + 1):

        p_home = poisson_probability(
            home_xg,
            home
        )

        for away in range(max_goals + 1):

            p_away = poisson_probability(
                away_xg,
                away
            )

            matrix[home, away] = (
                p_home * p_away
            )

    return matrix


def top_scores(
    home_xg: float,
    away_xg: float,
    max_goals: int = MAX_GOALS,
    top_n: int = 5
):
    """
    Return the N most likely exact scores.

    Example:
    [
        ("1-1",0.142),
        ("1-0",0.136)
    ]
    """

    matrix = score_matrix(
        home_xg,
        away_xg,
        max_goals
    )

    scores = []

    for home in range(max_goals + 1):

        for away in range(max_goals + 1):

            scores.append(

                (
                    f"{home}-{away}",
                    float(matrix[home, away])
                )

            )

    scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return scores[:top_n]


def score_probability(
    home_xg: float,
    away_xg: float,
    home_goals: int,
    away_goals: int
):
    """
    Probability of one exact score.

    Example:
        score_probability(
            1.3,
            0.9,
            2,
            1
        )
    """

    return float(

        poisson_probability(
            home_xg,
            home_goals
        )

        *

        poisson_probability(
            away_xg,
            away_goals
        )

    )


def outcome_probabilities(
    home_xg: float,
    away_xg: float,
    max_goals: int = MAX_GOALS
):
    """
    Compute 90-minute probabilities
    from the exact-score matrix.

    Returns:
        home_win
        draw
        away_win
    """

    matrix = score_matrix(
        home_xg,
        away_xg,
        max_goals
    )

    home = 0.0
    draw = 0.0
    away = 0.0

    for i in range(max_goals + 1):

        for j in range(max_goals + 1):

            p = matrix[i, j]

            if i > j:

                home += p

            elif i == j:

                draw += p

            else:

                away += p

    return (

        float(home),

        float(draw),

        float(away)

    )


def probability_heatmap_data(
    home_xg: float,
    away_xg: float,
    max_goals: int = MAX_GOALS
):
    """
    Returns data ready
    for Plotly Heatmap.
    """

    matrix = score_matrix(
        home_xg,
        away_xg,
        max_goals
    )

    x = list(
        range(max_goals + 1)
    )

    y = list(
        range(max_goals + 1)
    )

    z = matrix.tolist()

    return {

        "x": x,

        "y": y,

        "z": z

    }


if __name__ == "__main__":

    home_xg = 1.45
    away_xg = 1.10

    print("\nTop Scores\n")

    for score, probability in top_scores(
        home_xg,
        away_xg
    ):

        print(
            score,
            f"{probability:.2%}"
        )

    print("\nOutcome Probabilities\n")

    home, draw, away = outcome_probabilities(
        home_xg,
        away_xg
    )

    print("Home :", f"{home:.2%}")
    print("Draw :", f"{draw:.2%}")
    print("Away :", f"{away:.2%}")