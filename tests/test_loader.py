from src.loader import load_teams


def test_load_teams():

    teams = load_teams()

    assert len(teams) > 0

    assert "France" in teams

    assert "Spain" in teams