from pathlib import Path
from urllib.request import urlretrieve

import pandas as pd

GAMES_URL = (
	"https://raw.githubusercontent.com/"
	"nflverse/nfldata/master/data/games.csv"
)

DEFAULT_OUTPUT_PATH = Path("data/raw/games.csv")

REQUIRED_COLUMNS = {
	"game_id",
	"season",
	"game_type",
	"week",
	"gameday",
	"away_team",
	"away_score",
	"home_team",
	"home_score",
	"result",
	"spread_line",
}

def download_games(
	output_path: Path = DEFAULT_OUTPUT_PATH,
) -> Path:
	output_path.parent.mkdir(parents=True, exist_ok=True)
	urlretrieve(GAMES_URL, output_path)
	return output_path

def validate_games_file(path: Path) -> None:
	dataframe = pd.read_csv(path, nrows=5)

	missing_columns = REQUIRED_COLUMNS - set(dataframe.columns)

	if missing_columns:
		missing = ", ".join(sorted(missing_columns))
		raise ValueError(f"Games data is missing required columns: {missing}")
