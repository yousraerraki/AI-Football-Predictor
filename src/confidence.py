"""
Confidence Level Calculator
"""

from src.config import (
    HIGH_CONFIDENCE,
    MEDIUM_CONFIDENCE
)


def confidence_level(
    home_probability: float,
    away_probability: float
):
    """
    Determine confidence level
    from qualification probabilities.
    """

    strongest = max(
        home_probability,
        away_probability
    )

    if strongest >= HIGH_CONFIDENCE:
        return "HIGH"

    if strongest >= MEDIUM_CONFIDENCE:
        return "MEDIUM"

    return "LOW"


def confidence_color(level: str):

    level = level.upper()

    colors = {

        "HIGH": "#2ecc71",

        "MEDIUM": "#f39c12",

        "LOW": "#e74c3c"

    }

    return colors.get(level, "#95a5a6")


if __name__ == "__main__":

    print(confidence_level(0.82, 0.18))

    print(confidence_level(0.59, 0.41))

    print(confidence_level(0.51, 0.49))