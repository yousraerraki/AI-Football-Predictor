"""
AI Football Predictor Configuration
"""

# =====================================================
# LEAGUE AVERAGES
# =====================================================

# Average goals scored per team per match
LEAGUE_AVERAGE_GOALS = 1.35


# =====================================================
# BAYESIAN MODEL
# =====================================================

# Bayesian prior weight
PRIOR_WEIGHT = 4


# =====================================================
# EXPECTED GOALS (xG)
# =====================================================

# Minimum expected goals
MIN_XG = 0.20

# Maximum expected goals
MAX_XG = 4.50


# =====================================================
# TEAM RATING MODEL
# =====================================================

# Elo-like rating base
RATING_BASE = 1.35

# Rating difference scaling
RATING_SCALE = 400


# =====================================================
# REST DAYS
# =====================================================

# Extra recovery factor
REST_FACTOR = 1.015


# =====================================================
# MONTE CARLO
# =====================================================

# Default number of simulations
DEFAULT_SIMULATIONS = 100000

# Random seed for reproducibility
DEFAULT_SEED = 42


# =====================================================
# POISSON
# =====================================================

# Maximum goals considered in score matrix
MAX_GOALS = 8


# =====================================================
# EXTRA TIME
# =====================================================

# Extra time uses ~30% of regular xG
EXTRA_TIME_FACTOR = 0.30


# =====================================================
# PENALTIES
# =====================================================

# Logistic divisor for penalty shootout probability
PENALTY_RATING_DIVISOR = 800


# =====================================================
# CONFIDENCE THRESHOLDS
# =====================================================

HIGH_CONFIDENCE = 0.70

MEDIUM_CONFIDENCE = 0.55

LOW_CONFIDENCE = 0.00


# =====================================================
# DASHBOARD
# =====================================================

ENGINE_NAME = "Poisson + Monte Carlo"

MODEL_NAME = "AI Football Predictor"

VERSION = "2.0"


# =====================================================
# PLOTLY
# =====================================================

PLOT_THEME = "plotly_white"


# =====================================================
# STREAMLIT
# =====================================================

APP_TITLE = "⚽ AI Football Predictor"

APP_ICON = "⚽"

LAYOUT = "wide"


# =====================================================
# FILES
# =====================================================

TEAM_INPUT_FILE = "team_inputs.csv"

MATCHES_FILE = "matches.csv"


# =====================================================
# DEFAULT MATCH
# =====================================================

DEFAULT_HOME_TEAM = "France"

DEFAULT_AWAY_TEAM = "Spain"