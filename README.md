# NFL Betting Model

A professional sports data analytics and predictive modeling project focused on NFL point-spread markets.

The long-term objective is to build, validate, and backtest models that estimate NFL game outcomes and identify potential market mispricing while maintaining strict point-in-time integrity.

## Project Goals

- Ingest reliable historical NFL data
- Build reproducible data pipelines
- Engineer pregame predictive features
- Model scoring margin and ATS margin
- Estimate cover probailities
- Compare model probabilities against sportsbook prices
- Backtest strategies without data leakage
- Evaluate calibration, closing-line value, ROI, and risk
- Maintain production-quality softwar engineering standards

## Modeling Philosophy

The objective is not simply to predict winners.

The system aims to estimate the probability distribution of NFL outcomes and compare those estimates with market prices.

A useful beeting model must answer questions such as:
- What is the expected scoring margin?
- What ist he expected ATS margin?
- What is the probability that a team covers?
- How does the model probability compare with the market-implied probability?
- Is the estimated edge large enough to justify a wager after uncertainity and transaction costs?

## Repository Structure

```
nfl-betting-model/
	- .github/
		- workflows/
	- data/
		- raw/
		- interim/
		- processed/
	- docs/
	- notebooks/
	- src/
		- nfl_betting/
			- data/
			- features/
			- models/
			- evaluations/
	- tests/
	- .gitignore
	- README.md
	- pyproject.toml
	- LICENSE
```

## Data Layers
- data/raw
	- Immutable source data exactly as acquired from upstream providers.
	- Raw data should never be manually modified.
- data/interim
	- Intermediate datasets created during cleaning, normalization, joins, or transformation.
- data/processed
	- Model-ready datasets containing validated features and targets.
	- Generated datasets are excluded from Git. Code and metadat required to reproduce them are version controlled.

## Python Environment
Create the enviornment:
	```
	python3 -m venv .venv
	source .venv/bin/activate
	```
Install the project and development dependencies:
	```
	python -m pip install --upgrade pip
	python -m pip install -e ".[dev]"
	```

## Development Quality Gates
Before merging changes:
	```
	ruff check .
	mypy src
	pytest
	```
Additional automated checks will be added through GitHub Actions

## Core Definitions
For a selected team:
	scoring_margin = points_scored - points_allowed
	ats_margin = scoring_margin + spread
Interpretation:
	ats_margin > 0: covered
	ats_margin < 0: failed to cover
	ats_margin = 0: push

## Point-in-Time Integrity
All model features must represent information that was available at the exact prediction timestamp.

Future game information must never enter training features.

Examples of prohibited leakage include:
- final score
- in-game statistics
- postgame metrics
- injury information reported after the prediction timestamp
- future closing lines when modeling an earlier betting decision

## Status
Initial project bootstrap.

Current Phase:
	1. Repository initialization
	2. Development environment
	3. Architecture definition
	4. Historical NFL data ingestion

## Disclaimer
This project is intended for research, analytics, and software development. Predictive models do not guarantee profitable betting outcomes.
