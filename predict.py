"""
Console entry point
"""

from src.loader import load_teams
from src.predictor import predict_match
from src.charts import (
    probability_chart,
    qualification_chart,
    xg_chart
)


def main():

    print("\n==============================")
    print(" AI FOOTBALL PREDICTOR ")
    print("==============================\n")

    # Load teams
    teams = load_teams()

    home_name = "France"
    away_name = "Spain"

    home_team = teams[home_name]
    away_team = teams[away_name]

    print(f"Prediction: {home_name} vs {away_name}\n")

    prediction = predict_match(
        home_team,
        away_team,
        simulations=100000
    )

    print("------ Expected Goals ------")
    print(f"{prediction.home_team}: {prediction.expected_goals_home:.2f} xG")
    print(f"{prediction.away_team}: {prediction.expected_goals_away:.2f} xG")

    print("\n------ 90 Minutes ------")
    print(f"{prediction.home_team} Win : {prediction.home_win_probability:.2%}")
    print(f"Draw               : {prediction.draw_probability:.2%}")
    print(f"{prediction.away_team} Win : {prediction.away_win_probability:.2%}")

    print("\n------ Qualification ------")
    print(f"{prediction.home_team}: {prediction.home_qualification_probability:.2%}")
    print(f"{prediction.away_team}: {prediction.away_qualification_probability:.2%}")

    print("\n------ Most Likely Score ------")
    print(
        f"{prediction.most_likely_score} "
        f"({prediction.score_probability:.2%})"
    )

    print("\n------ Simulation ------")
    print(f"Engine       : {prediction.engine}")
    print(f"Confidence   : {prediction.confidence}")
    print(f"Simulations  : {prediction.simulations:,}")

    if prediction.top_scores:

        print("\n------ Top 5 Scores ------")

        for score in prediction.top_scores:

            print(
                f"{score['score']:>5}   "
                f"{score['probability']:.2%}"
            )

    if prediction.representative_scenario:

        print("\n------ Representative Scenario ------")

        scenario = prediction.representative_scenario

        print(
            f"90 Minutes : {scenario.get('regular_time','')}"
        )

        print(
            f"Extra Time : {scenario.get('extra_time','')}"
        )

        print(
            f"Decision   : {scenario.get('decision','')}"
        )

    print("\n------ JSON ------")
    print(prediction.to_dict())

    try:

        probability_chart(prediction).show()

        qualification_chart(prediction).show()

        xg_chart(prediction).show()

    except Exception as e:

        print("\nCharts error:", e)


if __name__ == "__main__":
    main()