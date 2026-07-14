import streamlit as st
from copy import deepcopy
from pathlib import Path
from src.loader import load_teams
from src.predictor import predict_match
from pathlib import Path
from src.charts import (
    probability_chart,
    qualification_chart,
    xg_chart,
    score_heatmap,
)

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
teams = load_teams()


team_names = list(teams.keys())

ASSETS = Path("assets/logos")
st.set_page_config(
    page_title="AI Football Predictor",
    page_icon="⚽",
    layout="wide",
)

# ---------------------------------------------------
# Main Title
# ---------------------------------------------------

st.markdown(
    """
    <h1 style="
        text-align:center;
        font-size:55px;
        font-weight:800;
    ">
    ⚽ AI Football Predictor
    </h1>
    """,
    unsafe_allow_html=True
)





# ---------------------------------------------------
# Load Teams
# ---------------------------------------------------

teams = load_teams()

# ---------------------------------------------------
# Assets Paths
# ---------------------------------------------------

ASSETS = Path("assets/logos")

FIFA_IMAGE = Path("assets/fifa/worldcup.png")
team_names = list(teams.keys())

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.title("⚙️ Model Controls")

home_name = st.sidebar.selectbox(
    "Home Team",
    team_names,
    index=0,
)

away_name = st.sidebar.selectbox(
    "Away Team",
    team_names,
    index=1 if len(team_names) > 1 else 0,
)


# ---------------------------------------------------
# FIFA World Cup Header
# ---------------------------------------------------

if FIFA_IMAGE.exists():

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.image(
            str(FIFA_IMAGE),
            width=600
        )


st.markdown(
    """
    <h2 style="text-align:center;">
     FIFA WORLD CUP 2026
    </h2>
    """,
    unsafe_allow_html=True
)


st.markdown("---")

st.markdown(
    """
    <p style="
        text-align:center;
        font-size:18px;
        color:#94A3B8;
    ">
    Datalid Match Lab · World Cup semifinal · Dallas · 14 July 2026
    </p>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# Match Header With Logos
# ---------------------------------------------------

home_logo = ASSETS / f"{home_name.lower()}.png"

away_logo = ASSETS / f"{away_name.lower()}.png"



col1, col2, col3 = st.columns([1, 2, 1])


# ---------------- HOME TEAM ----------------

with col1:

    if home_logo.exists():

        st.image(
            str(home_logo),
            width=120
        )

    st.markdown(
        f"""
        <h3 style="text-align:center;">
        🇫🇷 {home_name}
        </h3>
        """,
        unsafe_allow_html=True
    )



# ---------------- VS ----------------

with col2:

    st.markdown(
        """
        <h1 style="text-align:center;">
        VS
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="text-align:center;">
       
        </p>
        """,
        unsafe_allow_html=True
    )



# ---------------- AWAY TEAM ----------------

with col3:

    if away_logo.exists():

        st.image(
            str(away_logo),
            width=120
        )

    st.markdown(
        f"""
        <h3 style="text-align:center;">
        🇪🇸 {away_name}
        </h3>
        """,
        unsafe_allow_html=True
    )


st.markdown("---")
# ---------------------------------------------------
# Rating Controls
# ---------------------------------------------------

home_rating = st.sidebar.slider(
    f"{home_name} strength rating",
    min_value=1700,
    max_value=2000,
    value=int(teams[home_name].rating),
)

away_rating = st.sidebar.slider(
    f"{away_name} strength rating",
    min_value=1700,
    max_value=2000,
    value=int(teams[away_name].rating),
)

# ---------------------------------------------------
# Rest Days
# ---------------------------------------------------

home_rest = st.sidebar.slider(
    f"{home_name} rest days",
    min_value=2,
    max_value=7,
    value=int(teams[home_name].rest_days),
)

away_rest = st.sidebar.slider(
    f"{away_name} rest days",
    min_value=2,
    max_value=7,
    value=int(teams[away_name].rest_days),
)

# ---------------------------------------------------
# Simulations
# ---------------------------------------------------

simulations = st.sidebar.slider(
    "Simulations",
    min_value=10000,
    max_value=250000,
    value=100000,
    step=10000,
)

# ---------------------------------------------------
# Tactical Edge
# ---------------------------------------------------

tactical_edge = st.sidebar.slider(
    "Tactical Edge",
    min_value=-10,
    max_value=10,
    value=0,
)

# ---------------------------------------------------
# What-if Scenarios
# ---------------------------------------------------

st.sidebar.markdown("---")

# ---------------------------------------------------
# Player Scenarios With Images
# ---------------------------------------------------

st.sidebar.subheader(" Scénarios hypothétiques")


PLAYERS = Path("assets/players")


# Mbappé

mbappe_img = PLAYERS / "mbappe.png"

if mbappe_img.exists():

    st.sidebar.image(
        str(mbappe_img),
        width=100
    )


mbappe_out = st.sidebar.checkbox(
    "🇫🇷 Mbappé indisponible",
    value=False,
)



# Yamal

yamal_img = PLAYERS / "yamal.png"

if yamal_img.exists():

    st.sidebar.image(
        str(yamal_img),
        width=100
    )


yamal_out = st.sidebar.checkbox(
    "🇪🇸 Yamal indisponible",
    value=False,
)

st.sidebar.markdown("---")

predict = st.sidebar.button(
    " Predict Match",
    use_container_width=True,
)
# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

if predict:

    home = deepcopy(teams[home_name])
    away = deepcopy(teams[away_name])

    home.rating = home_rating
    away.rating = away_rating

    home.rest_days = home_rest
    away.rest_days = away_rest

    # Tactical Edge
    edge = tactical_edge / 500

    home.prior_attack *= (1 + edge)
    away.prior_attack *= (1 - edge)

    # -----------------------------------
    # Hypothetical scenarios
    # -----------------------------------

    if mbappe_out:
        home.prior_attack *= 0.90
        home.rating -= 20

    if yamal_out:
        away.prior_attack *= 0.92
        away.rating -= 15

    # -----------------------------------
    # Prediction
    # -----------------------------------

    prediction = predict_match(
        home,
        away,
        simulations=simulations
    )

    # ---------------------------------------------------
    # Success
    # ---------------------------------------------------

    st.success(
        f"✓ {prediction.simulations:,} simulated matches complete"
    )

    # ---------------------------------------------------
    # Match Card
    # ---------------------------------------------------

    st.markdown("---")

  

    # ---------------------------------------------------
    # Active Scenarios
    # ---------------------------------------------------

    active = []

    if mbappe_out:
        active.append("🇫🇷 Mbappé indisponible")

    if yamal_out:
        active.append("🇪🇸 Yamal indisponible")

    if active:

        st.info(

            "### 🧪 Scénarios appliqués\n\n"

            +

            "\n".join(

                f"• {item}"

                for item in active

            )

        )

    # ---------------------------------------------------
    # Representative Scenario
    # ---------------------------------------------------

    st.markdown("---")

    st.subheader("Representative Scenario")

    scenario = prediction.representative_scenario

    if not isinstance(scenario, dict):
        scenario = {}

    regulation = scenario.get(
        "regulation",
        scenario.get("regular_time", "Unknown")
    )

    extra_time = scenario.get(
        "extra_time",
        "Not required"
    )

    decision = scenario.get(
        "decision",
        "No decision available"
    )

    st.info(
        f"""
**90 minutes**

{regulation}

**Extra time**

{extra_time}

**Decision**

{decision}
"""
    )

    # ---------------------------------------------------
    # Qualification
    # ---------------------------------------------------

    st.markdown("---")

    st.subheader("🏆 Qualification Probability")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            f"{prediction.home_team} reaches final",
            f"{prediction.home_qualification_probability*100:.1f}%"
        )

    with col2:

        st.metric(
            f"{prediction.away_team} reaches final",
            f"{prediction.away_qualification_probability*100:.1f}%"
        )

    # ---------------------------------------------------
    # 90 Minutes
    # ---------------------------------------------------

    st.markdown("---")

    st.subheader("90-minute outcome")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Home Win",
            f"{prediction.home_win_probability*100:.1f}%"
        )

    with c2:

        st.metric(
            "Draw",
            f"{prediction.draw_probability*100:.1f}%"
        )

    with c3:

        st.metric(
            "Away Win",
            f"{prediction.away_win_probability*100:.1f}%"
        )

    # ---------------------------------------------------
    # Expected Goals
    # ---------------------------------------------------

    st.markdown("---")

    st.subheader("Expected Goals")

    g1, g2 = st.columns(2)

    with g1:

        st.metric(
            prediction.home_team,
            f"{prediction.expected_goals_home:.2f}"
        )

    with g2:

        st.metric(
            prediction.away_team,
            f"{prediction.expected_goals_away:.2f}"
        )
            # ---------------------------------------------------
    # Most Likely Score
    # ---------------------------------------------------

    st.markdown("---")

    st.subheader("⭐ Most Likely Score")

    st.success(
        f"{prediction.most_likely_score} "
        f"({prediction.score_probability*100:.2f}%)"
    )

    # ---------------------------------------------------
    # Top Exact Scores
    # ---------------------------------------------------

    st.markdown("---")

    st.subheader("📋 Five Most Likely Scores")

    col1, col2 = st.columns([2, 1])

    col1.markdown("**Score**")
    col2.markdown("**Probability**")

    st.divider()

    for item in prediction.top_scores:

        c1, c2 = st.columns([2, 1])

        c1.write(item["score"])

        c2.write(
            f"{item['probability']*100:.2f}%"
        )

    # ---------------------------------------------------
    # Visual Analysis
    # ---------------------------------------------------

    st.markdown("---")

    st.subheader("📊 Visual Analysis")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "90 Minutes",
            "Qualification",
            "Expected Goals",
            "Score Heatmap",
        ]
    )

    # -----------------------------
    # 90 Minutes
    # -----------------------------

    with tab1:

        st.plotly_chart(
            probability_chart(
                prediction
            ),
            use_container_width=True
        )

    # -----------------------------
    # Qualification
    # -----------------------------

    with tab2:

        st.plotly_chart(
            qualification_chart(
                prediction
            ),
            use_container_width=True
        )

    # -----------------------------
    # Expected Goals
    # -----------------------------

    with tab3:

        st.plotly_chart(
            xg_chart(
                prediction
            ),
            use_container_width=True
        )

    # -----------------------------
    # Heatmap
    # -----------------------------

    with tab4:

        st.plotly_chart(

            score_heatmap(

                prediction.expected_goals_home,

                prediction.expected_goals_away

            ),

            use_container_width=True

        )

            # ---------------------------------------------------
    # Why the model leans this way
    # ---------------------------------------------------

    st.markdown("---")

    st.subheader("🧠 Why the model leans this way")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            f"{prediction.home_team} tournament goals",
            prediction.home_goals
        )

    with col2:

        st.metric(
            f"{prediction.away_team} tournament goals",
            prediction.away_goals
        )

    st.metric(
        "Expected Goals (xG)",
        f"{prediction.expected_goals_home:.2f} - {prediction.expected_goals_away:.2f}"
    )

    st.metric(
        "Prediction Engine",
        prediction.engine
    )

    # ---------------------------------------------------
    # Methodology
    # ---------------------------------------------------

    st.markdown("---")

    st.subheader(" Methodology")

    st.info(
        """
This prediction combines four complementary models:

• Bayesian-adjusted Attack & Defence Strength

• Expected Goals (xG)

• Poisson Goal Distribution

• Monte Carlo Simulation

The hypothetical scenarios (Mbappé unavailable, Yamal unavailable)
are user-selected assumptions for exploration only.
They are NOT real injury information.
"""
    )

    # ---------------------------------------------------
    # Prediction Summary
    # ---------------------------------------------------

    st.markdown("---")

    st.subheader("📄 Prediction Summary")

    st.write(
        f"""
**Match**

{prediction.home_team} vs {prediction.away_team}

**Expected Goals**

{prediction.expected_goals_home:.2f} - {prediction.expected_goals_away:.2f}

**Most Likely Score**

{prediction.most_likely_score}

**Qualification Probability**

{prediction.home_team}: {prediction.home_qualification_probability:.1%}

{prediction.away_team}: {prediction.away_qualification_probability:.1%}

**Confidence**

{prediction.confidence}
"""
    )

    # ---------------------------------------------------
    # Download Prediction
    # ---------------------------------------------------

    st.markdown("---")

    st.subheader("⬇️ Download Prediction")

    import json

    prediction_json = json.dumps(
        prediction.to_dict(),
        indent=4
    )

    st.download_button(
        label="📥 Download JSON",
        data=prediction_json,
        file_name=f"{prediction.home_team}_vs_{prediction.away_team}.json",
        mime="application/json",
    )

    # ---------------------------------------------------
    # Footer
    # ---------------------------------------------------

    st.markdown("---")

    st.caption(
        "AI Football Predictor • Bayesian Rating • Expected Goals • "
        "Poisson Distribution • Monte Carlo Simulation"
    )

