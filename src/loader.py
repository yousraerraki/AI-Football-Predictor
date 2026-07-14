"""
Data Loader

Loads:
- team_inputs.csv
- matches.csv
"""

from pathlib import Path

import pandas as pd

from src.models import Team


# ----------------------------------------------------
# Data folder
# ----------------------------------------------------

DATA_PATH = Path(__file__).resolve().parent.parent / "data"


# ----------------------------------------------------
# Load teams
# ----------------------------------------------------

def load_teams():

    """
    Load teams from team_inputs.csv
    """

    file = DATA_PATH / "team_inputs.csv"

    if not file.exists():
        raise FileNotFoundError(
            f"Missing file: {file}"
        )

    df = pd.read_csv(file)

    teams = {}

    for _, row in df.iterrows():

        team = Team(

            name=str(row["team"]),

            matches=int(row["matches"]),

            goals_for=int(row["goals_for"]),

            goals_against=int(row["goals_against"]),

            prior_attack=float(row["prior_attack"]),

            prior_defence=float(row["prior_defence"]),

            rating=float(row["rating"]),

            rest_days=int(row["rest_days"])

        )

        teams[team.name] = team

    return teams


# ----------------------------------------------------
# Load matches
# ----------------------------------------------------

def load_matches():

    """
    Load matches.csv
    """

    file = DATA_PATH / "matches.csv"

    if not file.exists():
        raise FileNotFoundError(
            f"Missing file: {file}"
        )

    df = pd.read_csv(file)

    df["date"] = pd.to_datetime(df["date"])

    return df


# ----------------------------------------------------
# Team History
# ----------------------------------------------------

def team_history(team_name: str):

    """
    Returns all matches
    for one team.
    """

    matches = load_matches()

    history = matches[
        matches["team"] == team_name
    ]

    return history.sort_values(
        "date"
    )


# ----------------------------------------------------
# Last Matches
# ----------------------------------------------------

def last_matches(
    team_name: str,
    n: int = 5
):

    """
    Returns last N matches.
    """

    history = team_history(team_name)

    return history.tail(n)


# ----------------------------------------------------
# Tournament Goals
# ----------------------------------------------------

def tournament_goals(team_name: str):

    """
    Returns:

    goals_for,
    goals_against
    """

    history = team_history(team_name)

    goals_for = int(
        history["goals_for"].sum()
    )

    goals_against = int(
        history["goals_against"].sum()
    )

    return goals_for, goals_against


# ----------------------------------------------------
# Team Exists
# ----------------------------------------------------

def team_exists(team_name: str):

    """
    Check if team exists.
    """

    teams = load_teams()

    return team_name in teams


# ----------------------------------------------------
# List Teams
# ----------------------------------------------------

def list_teams():

    """
    Returns all team names.
    """

    teams = load_teams()

    return sorted(
        list(teams.keys())
    )


# ----------------------------------------------------
# Debug
# ----------------------------------------------------

if __name__ == "__main__":

    print("\nAvailable Teams\n")

    print(list_teams())

    print("\n")

    teams = load_teams()

    print(teams["France"])

    print("\nLast Matches\n")

    print(last_matches("France"))

    gf, ga = tournament_goals("France")

    print("\nGoals")

    print(gf, ga)