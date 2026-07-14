"""
Main Prediction Pipeline
"""

from src.expected_goals import expected_goals
from src.poisson import top_scores
from src.simulation import simulate_matches
from src.models import Prediction
from src.confidence import confidence_level
from src.scenario import representative_scenario


def predict_match(
    home_team,
    away_team,
    simulations=100000
):
    """
    Complete prediction pipeline.
    """

    # --------------------------------------------------
    # Expected Goals
    # --------------------------------------------------

    home_xg, away_xg = expected_goals(
        home_team,
        away_team
    )

    # --------------------------------------------------
    # Top Exact Scores
    # --------------------------------------------------

    scores = top_scores(
        home_xg,
        away_xg,
        top_n=5
    )

    best_score = scores[0][0]
    best_probability = scores[0][1]

    # --------------------------------------------------
    # Monte Carlo Simulation
    # --------------------------------------------------

    simulation = simulate_matches(
        home_xg=home_xg,
        away_xg=away_xg,
        home_rating=home_team.rating,
        away_rating=away_team.rating,
        simulations=simulations
    )

    # --------------------------------------------------
    # Prediction Object
    # --------------------------------------------------

    prediction = Prediction(

        home_team=home_team.name,
        away_team=away_team.name,

        expected_goals_home=home_xg,
        expected_goals_away=away_xg,

        home_win_probability=float(
            simulation["home_win_90"]
        ),

        draw_probability=float(
            simulation["draw_90"]
        ),

        away_win_probability=float(
            simulation["away_win_90"]
        ),

        home_qualification_probability=float(
            simulation["home_qualification"]
        ),

        away_qualification_probability=float(
            simulation["away_qualification"]
        ),

        most_likely_score=best_score,

        score_probability=float(
            best_probability
        ),

        simulations=simulations

    )

    # --------------------------------------------------
    # Confidence
    # --------------------------------------------------

    prediction.confidence = confidence_level(
        prediction.home_qualification_probability,
        prediction.away_qualification_probability
    )

    # --------------------------------------------------
    # Representative Scenario
    # --------------------------------------------------

    prediction.representative_scenario = (
        representative_scenario(
            prediction
        )
    )

    # --------------------------------------------------
    # Top Scores
    # --------------------------------------------------

    prediction.top_scores = [

        {
            "score": score,
            "probability": float(probability)
        }

        for score, probability in scores

    ]

    # --------------------------------------------------
    # Tournament Goals
    # --------------------------------------------------

    prediction.home_goals = (
        f"{home_team.goals_for}-{home_team.goals_against}"
    )

    prediction.away_goals = (
        f"{away_team.goals_for}-{away_team.goals_against}"
    )

    # --------------------------------------------------
    # Engine
    # --------------------------------------------------

    prediction.engine = "Poisson + Monte Carlo"

    prediction.notes = (
        "Prediction generated using Bayesian Team Strengths, "
        "Expected Goals (xG), Poisson Distribution "
        "and Monte Carlo Simulation."
    )

    return prediction