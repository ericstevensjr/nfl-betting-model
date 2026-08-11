"""Tests for betting-model target calculations."""

from nfl_betting.features.targets import (
	calculate_ats_margin,
	calculate_scoring_margin,
)


def test_calculate_scoring_margin_for_win() -> None:
	assert calculate_scoring_margin(27, 23) == 4

def test_calculate_scoring_margin_for_loss() -> None:
	assert calculate_scoring_margin(24, 27) == -3

def test_calculate_ats_margin_for_favorite_cover() -> None:
	assert calculate_ats_margin(27, 23, -3.5) == 0.5

def test_calculate_ats_margin_for_underdog_cover() -> None:
	assert calculate_ats_margin(24, 27, 6.5) == 3.5

def test_calculate_ats_margin_for_favorite_non_cover() -> None:
	assert calculate_ats_margin(24, 20, -7.5) == -3.5

def test_calculate_ats_margin_for_push() -> None:
	assert calculate_ats_margin(24, 21, -3.0) == 0.0
