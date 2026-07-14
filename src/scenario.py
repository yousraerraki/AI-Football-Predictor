"""
Representative Scenario Generator
Creates a readable scenario similar to Datalid Match Lab.
"""


def representative_scenario(prediction):
    """
    Generate a representative match scenario.
    """

    score = prediction.most_likely_score

    try:
        home_score, away_score = map(int, score.split("-"))
    except Exception:
        home_score = 0
        away_score = 0

    # ---------------------------------------------------
    # Regulation Time
    # ---------------------------------------------------

    regulation = (
        f"{prediction.home_team} "
        f"{home_score}-{away_score} "
        f"{prediction.away_team}"
    )

    # ---------------------------------------------------
    # Extra Time & Decision
    # ---------------------------------------------------

    if home_score == away_score:

        extra_time = (
            f"{home_score}-{away_score} "
            "after extra time"
        )

        if (
            prediction.home_qualification_probability
            >=
            prediction.away_qualification_probability
        ):

            decision = (
                f"{prediction.home_team} "
                "wins on penalties"
            )

            qualified_team = prediction.home_team

        else:

            decision = (
                f"{prediction.away_team} "
                "wins on penalties"
            )

            qualified_team = prediction.away_team

    elif home_score > away_score:

        extra_time = "Not required"

        decision = (
            f"{prediction.home_team} "
            "wins in regular time"
        )

        qualified_team = prediction.home_team

    else:

        extra_time = "Not required"

        decision = (
            f"{prediction.away_team} "
            "wins in regular time"
        )

        qualified_team = prediction.away_team

    # ---------------------------------------------------
    # Qualification Probability
    # ---------------------------------------------------

    probability = max(
        prediction.home_qualification_probability,
        prediction.away_qualification_probability
    )

    # ---------------------------------------------------
    # Return Dictionary
    # ---------------------------------------------------

    return {

        "regulation": regulation,

        "regular_time": regulation,

        "extra_time": extra_time,

        "decision": decision,

        "qualified_team": qualified_team,

        "probability": probability

    }


# ---------------------------------------------------
# Local Test
# ---------------------------------------------------

if __name__ == "__main__":

    class FakePrediction:

        home_team = "France"
        away_team = "Spain"

        most_likely_score = "0-0"

        home_qualification_probability = 0.506
        away_qualification_probability = 0.494

    prediction = FakePrediction()

    print(representative_scenario(prediction))