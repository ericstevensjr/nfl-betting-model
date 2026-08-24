from pathlib import Path

import pandas as pd
import pytest

from nfl_betting.data.download_games import (
    REQUIRED_COLUMNS,
    validate_game_ids,
    validate_game_outcomes,
    validate_games_file,
    validate_team_assignments,
)


def test_validate_games_file_accepts_required_schema(tmp_path: Path) -> None:
    path = tmp_path / "games.csv"

    dataframe = pd.DataFrame(
        {column: [None] for column in REQUIRED_COLUMNS}
    )
    dataframe.to_csv(path, index=False)

    validate_games_file(path)


def test_validate_games_file_rejects_missing_column(tmp_path: Path) -> None:
    path = tmp_path / "games.csv"

    columns = REQUIRED_COLUMNS - {"game_id"}
    dataframe = pd.DataFrame({column: [None] for column in columns})
    dataframe.to_csv(path, index=False)

    with pytest.raises(
        ValueError,
        match="Games data is missing required columns: game_id",
    ):
        validate_games_file(path)


def test_validate_game_outcomes_accepts_completed_game(
    tmp_path: Path,
) -> None:
    path = tmp_path / "games.csv"

    dataframe = pd.DataFrame(
        {
            "home_score": [24],
            "away_score": [17],
            "result": [7],
        }
    )
    dataframe.to_csv(path, index=False)

    validate_game_outcomes(path)


def test_validate_game_outcomes_accepts_unplayed_game(
    tmp_path: Path,
) -> None:
    path = tmp_path / "games.csv"

    dataframe = pd.DataFrame(
        {
            "home_score": [None],
            "away_score": [None],
            "result": [None],
        }
    )
    dataframe.to_csv(path, index=False)

    validate_game_outcomes(path)


def test_validate_game_outcomes_rejects_partial_outcome(
    tmp_path: Path,
) -> None:
    path = tmp_path / "games.csv"

    dataframe = pd.DataFrame(
        {
            "home_score": [24],
            "away_score": [None],
            "result": [None],
        }
    )
    dataframe.to_csv(path, index=False)

    with pytest.raises(
        ValueError,
        match="Games data contains partially missing outcomes",
    ):
        validate_game_outcomes(path)


def test_validate_game_outcomes_rejects_inconsistent_result(
    tmp_path: Path,
) -> None:
    path = tmp_path / "games.csv"

    dataframe = pd.DataFrame(
        {
            "home_score": [24],
            "away_score": [17],
            "result": [6],
        }
    )
    dataframe.to_csv(path, index=False)

    with pytest.raises(
        ValueError,
        match="Games data contains inconsistent game results",
    ):
        validate_game_outcomes(path)


def test_validate_game_ids_accepts_valid_ids(tmp_path: Path) -> None:
    path = tmp_path / "games.csv"

    dataframe = pd.DataFrame(
        {
            "game_id": ["2025_01_DAL_PHI"],
            "season": [2025],
            "week": [1],
            "away_team": ["DAL"],
            "home_team": ["PHI"],
        }
    )
    dataframe.to_csv(path, index=False)

    validate_game_ids(path)


def test_validate_game_ids_rejects_missing_id(tmp_path: Path) -> None:
    path = tmp_path / "games.csv"

    dataframe = pd.DataFrame(
        {
            "game_id": [None],
            "season": [2025],
            "week": [1],
            "away_team": ["DAL"],
            "home_team": ["PHI"],
        }
    )
    dataframe.to_csv(path, index=False)

    with pytest.raises(
        ValueError,
        match="Games data contains missing game_id values",
    ):
        validate_game_ids(path)


def test_validate_game_ids_rejects_duplicate_ids(tmp_path: Path) -> None:
    path = tmp_path / "games.csv"

    dataframe = pd.DataFrame(
        {
            "game_id": [
                "2025_01_DAL_PHI",
                "2025_01_DAL_PHI",
            ],
            "season": [2025, 2025],
            "week": [1, 1],
            "away_team": ["DAL", "DAL"],
            "home_team": ["PHI", "PHI"],
        }
    )
    dataframe.to_csv(path, index=False)

    with pytest.raises(
        ValueError,
        match="Games data contains duplicate game_id values",
    ):
        validate_game_ids(path)


def test_validate_game_ids_rejects_inconsistent_id(tmp_path: Path) -> None:
    path = tmp_path / "games.csv"

    dataframe = pd.DataFrame(
        {
            "game_id": ["2025_01_PHI_DAL"],
            "season": [2025],
            "week": [1],
            "away_team": ["DAL"],
            "home_team": ["PHI"],
        }
    )
    dataframe.to_csv(path, index=False)

    with pytest.raises(
        ValueError,
        match="Games data contains inconsistent game_id values",
    ):
        validate_game_ids(path)


def test_validate_team_assignments_accepts_distinct_teams(
    tmp_path: Path,
) -> None:
    path = tmp_path / "games.csv"

    dataframe = pd.DataFrame(
        {
            "home_team": ["PHI"],
            "away_team": ["DAL"],
        }
    )
    dataframe.to_csv(path, index=False)

    validate_team_assignments(path)


def test_validate_team_assignments_rejects_missing_home_team(
    tmp_path: Path,
) -> None:
    path = tmp_path / "games.csv"

    dataframe = pd.DataFrame(
        {
            "home_team": [None],
            "away_team": ["DAL"],
        }
    )
    dataframe.to_csv(path, index=False)

    with pytest.raises(
        ValueError,
        match="Games data contains missing home_team values",
    ):
        validate_team_assignments(path)


def test_validate_team_assignments_rejects_missing_away_team(
    tmp_path: Path,
) -> None:
    path = tmp_path / "games.csv"

    dataframe = pd.DataFrame(
        {
            "home_team": ["PHI"],
            "away_team": [None],
        }
    )
    dataframe.to_csv(path, index=False)

    with pytest.raises(
        ValueError,
        match="Games data contains missing away_team values",
    ):
        validate_team_assignments(path)


def test_validate_team_assignments_rejects_identical_teams(
    tmp_path: Path,
) -> None:
    path = tmp_path / "games.csv"

    dataframe = pd.DataFrame(
        {
            "home_team": ["PHI"],
            "away_team": ["PHI"],
        }
    )
    dataframe.to_csv(path, index=False)

    with pytest.raises(
        ValueError,
        match="Games data contains identical home and away teams",
    ):
        validate_team_assignments(path)

def test_validate_game_outcomes_rejects_negative_home_score(
    tmp_path: Path,
) -> None:
    path = tmp_path / "games.csv"

    dataframe = pd.DataFrame(
        {
            "home_score": [-1],
            "away_score": [17],
            "result": [-18],
        }
    )
    dataframe.to_csv(path, index=False)

    with pytest.raises(
        ValueError,
        match="Games data contains negative home scores",
    ):
        validate_game_outcomes(path)


def test_validate_game_outcomes_rejects_negative_away_score(
    tmp_path: Path,
) -> None:
    path = tmp_path / "games.csv"

    dataframe = pd.DataFrame(
        {
            "home_score": [24],
            "away_score": [-1],
            "result": [25],
        }
    )
    dataframe.to_csv(path, index=False)

    with pytest.raises(
        ValueError,
        match="Games data contains negative away scores",
    ):
        validate_game_outcomes(path)
