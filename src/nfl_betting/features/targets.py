"""Target-variable calculations for NFL betting models."""


def calculate_scoring_margin(points_for: float, points_against: float) -> float:
	"""Calculate scoring margin from a team's perspective."""
	return points_for - points_against


def calculate_ats_margin(
	points_for: float,
	points_against: float,
	spread: float,
) -> float:
	"""Calculate against-the-spread margin from a team's perspective."""
	scoring_margin = calculate_scoring_margin(points_for, points_against)
	return scoring_margin + spread
