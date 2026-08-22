"""Target-variable calculations for NFL betting models."""


def calculate_scoring_margin(
    home_score: float,
    away_score: float,
) -> float:
    """Calculate scoring margin from the home team's perspective."""
    return home_score - away_score


def calculate_ats_margin(
    home_score: float,
    away_score: float,
    spread_line: float,
) -> float:
    """Calculate ATS margin using nflverse's home-perspective spread line.

    nflverse convention:
    - positive spread_line: home team favored
    - negative spread_line: away team favored

    Positive ATS margin means the home team covered.
    Negative ATS margin means the home team failed to cover.
    Zero means a push.
    """
    scoring_margin = calculate_scoring_margin(home_score, away_score)
    return scoring_margin - spread_line