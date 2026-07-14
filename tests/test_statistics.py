from src.loader import load_teams
from src.statistics import team_statistics



def test_team_statistics():

    teams = load_teams()

    france = teams["France"]


    stats = team_statistics(france)


    assert stats["team"] == "France"

    assert stats["goals_per_match"] > 0