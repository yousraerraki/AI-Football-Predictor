import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from math import exp, factorial


# ---------------------------------------------------
# 90-Minute Probability
# ---------------------------------------------------

def probability_chart(prediction):

    df = pd.DataFrame({

        "Outcome": [

            prediction.home_team,

            "Draw",

            prediction.away_team

        ],

        "Probability": [

            prediction.home_win_probability,

            prediction.draw_probability,

            prediction.away_win_probability

        ]

    })

    fig = px.pie(

        df,

        names="Outcome",

        values="Probability",

        hole=0.45,

        title="90-Minute Outcome Probabilities"

    )

    fig.update_traces(

        textinfo="label+percent"

    )

    return fig


# ---------------------------------------------------
# Qualification
# ---------------------------------------------------

def qualification_chart(prediction):

    df = pd.DataFrame({

        "Team": [

            prediction.home_team,

            prediction.away_team

        ],

        "Probability": [

            prediction.home_qualification_probability,

            prediction.away_qualification_probability

        ]

    })

    fig = px.bar(

        df,

        x="Team",

        y="Probability",

        text=df["Probability"].map(

            lambda x: f"{x:.1%}"

        ),

        title="Qualification Probability"

    )

    fig.update_yaxes(

        range=[0, 1]

    )

    return fig


# ---------------------------------------------------
# Expected Goals
# ---------------------------------------------------

def xg_chart(prediction):

    df = pd.DataFrame({

        "Team": [

            prediction.home_team,

            prediction.away_team

        ],

        "xG": [

            prediction.expected_goals_home,

            prediction.expected_goals_away

        ]

    })

    fig = px.bar(

        df,

        x="Team",

        y="xG",

        text_auto=".2f",

        title="Expected Goals (xG)"

    )

    return fig


# ---------------------------------------------------
# Exact Score Heatmap
# ---------------------------------------------------

def score_heatmap(

    home_xg,

    away_xg,

    max_goals=5

):

    max_goals = int(max_goals)

    matrix = []

    for home_goals in range(max_goals + 1):

        row = []

        for away_goals in range(max_goals + 1):

            p_home = (

                (home_xg ** home_goals)

                *

                exp(-home_xg)

                /

                factorial(home_goals)

            )

            p_away = (

                (away_xg ** away_goals)

                *

                exp(-away_xg)

                /

                factorial(away_goals)

            )

            row.append(

                p_home * p_away

            )

        matrix.append(row)

    fig = go.Figure(

        data=go.Heatmap(

            z=matrix,

            x=[

                str(i)

                for i in range(max_goals + 1)

            ],

            y=[

                str(i)

                for i in range(max_goals + 1)

            ],

            text=[

                [

                    f"{v:.1%}"

                    for v in row

                ]

                for row in matrix

            ],

            texttemplate="%{text}",

            hovertemplate=

            "Home %{y} - Away %{x}"

            "<br>Probability %{z:.2%}"

            "<extra></extra>"

        )

    )

    fig.update_layout(

        title="Exact Score Probability Map",

        xaxis_title="Away Goals",

        yaxis_title="Home Goals"

    )

    return fig


# ---------------------------------------------------
# Top Scores Table
# ---------------------------------------------------

def top_scores_table(prediction):

    if not hasattr(

        prediction,

        "top_scores"

    ):

        return pd.DataFrame(

            columns=[

                "Score",

                "Probability"

            ]

        )

    return pd.DataFrame({

        "Score": [

            item["score"]

            for item in prediction.top_scores

        ],

        "Probability": [

            f"{item['probability']:.2%}"

            for item in prediction.top_scores

        ]

    })