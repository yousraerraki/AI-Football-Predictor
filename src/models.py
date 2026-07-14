"""
Data Models
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any


# =====================================================
# TEAM
# =====================================================

@dataclass
class Team:

    name: str

    matches: int

    goals_for: int

    goals_against: int

    prior_attack: float

    prior_defence: float

    rating: float

    rest_days: int


    def to_dict(self):

        data = asdict(self)

        for key, value in data.items():

            if hasattr(value, "item"):

                data[key] = value.item()

        return data



# =====================================================
# PREDICTION
# =====================================================

@dataclass
class Prediction:


    # --------------------------
    # Teams
    # --------------------------

    home_team: str

    away_team: str



    # --------------------------
    # Expected Goals
    # --------------------------

    expected_goals_home: float

    expected_goals_away: float



    # --------------------------
    # 90 Minutes
    # --------------------------

    home_win_probability: float

    draw_probability: float

    away_win_probability: float



    # --------------------------
    # Qualification
    # --------------------------

    home_qualification_probability: float

    away_qualification_probability: float



    # --------------------------
    # Exact Score
    # --------------------------

    most_likely_score: str

    score_probability: float



    # --------------------------
    # Simulation
    # --------------------------

    simulations: int



    # --------------------------
    # Dashboard
    # --------------------------

    confidence: str = "MEDIUM"

    engine: str = "Poisson + Monte Carlo"


    top_scores: List[Dict[str, Any]] = field(
        default_factory=list
    )


    representative_scenario: Dict[str, Any] = field(
        default_factory=dict
    )


    home_goals: int = 0

    away_goals: int = 0

    notes: str = ""



    # --------------------------
    # Export
    # --------------------------

    def to_dict(self):

        data = asdict(self)

        for key, value in data.items():

            if hasattr(value, "item"):

                data[key] = value.item()

        return data



    # --------------------------
    # Pretty Print
    # --------------------------

    def summary(self):

        return f"""
Match:
{self.home_team} vs {self.away_team}


Expected Goals:

{self.expected_goals_home:.2f} - {self.expected_goals_away:.2f}


90 Minutes:


Home Win : {self.home_win_probability:.2%}


Draw     : {self.draw_probability:.2%}


Away Win : {self.away_win_probability:.2%}



Qualification:


{self.home_team}: {self.home_qualification_probability:.2%}


{self.away_team}: {self.away_qualification_probability:.2%}



Most Likely Score:


{self.most_likely_score}



Probability:


{self.score_probability:.2%}



Confidence:


{self.confidence}



Engine:


{self.engine}



Simulations:


{self.simulations:,}

"""



# =====================================================
# TEST
# =====================================================

if __name__ == "__main__":


    team = Team(

        name="France",

        matches=6,

        goals_for=16,

        goals_against=2,

        prior_attack=1.75,

        prior_defence=0.78,

        rating=1870,

        rest_days=5

    )


    print(team)

    print()

    print(team.to_dict())