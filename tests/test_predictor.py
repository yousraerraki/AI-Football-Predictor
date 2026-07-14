from src.loader import load_teams
from src.predictor import predict_match



def test_predictor():


    teams = load_teams()


    result = predict_match(

        teams["France"],

        teams["Spain"],

        simulations=10000

    )


    assert result.home_team == "France"

    assert result.away_team == "Spain"

    assert result.simulations == 10000