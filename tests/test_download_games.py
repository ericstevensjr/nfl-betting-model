from pathlib import Path

import pandas as pd
import pytest

from nfl_betting.data.download_games import REQUIRED_COLUMNS, validate_games_file


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
