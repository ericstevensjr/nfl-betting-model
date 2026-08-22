# Investigation 001 — nflverse Spread-Line Convention

## Question

What exactly does `spread_line` represent in the nflverse `games.csv`
dataset, and how should home-team ATS margin be calculated?

## Hypothesis

The nflverse `spread_line` field is expressed from the home-team
perspective and therefore uses the opposite sign convention from
conventional sportsbook team notation.

## Data

`data/raw/games.csv`

Representative games examined:

- `2025_01_DAL_PHI`
- `2025_01_KC_LAC`

## Method

1. Compared the project documentation and existing target implementation.
2. Identified conflicting spread conventions.
3. Examined representative rows from the raw nflverse dataset.
4. Compared `result`, `spread_line`, teams, scores, and market prices.
5. Verified the convention against the upstream data definition.

## Result

The raw nflverse convention is:

- positive `spread_line` = home team favored
- negative `spread_line` = away team favored

`result` is also expressed from the home-team perspective:

`result = home_score - away_score`

Therefore home-team ATS margin is:

`ats_margin = result - spread_line`

Example:

`2025_01_DAL_PHI`

- PHI home
- result = +4
- spread_line = +8.5
- ATS margin = 4 - 8.5 = -4.5

Philadelphia won the game but failed to cover by 4.5 points.

Example:

`2025_01_KC_LAC`

- LAC home
- result = +6
- spread_line = -3
- ATS margin = 6 - (-3) = +9

Kansas City was favored by 3 in conventional sportsbook notation.
Los Angeles therefore covered by 9 points from the home-team perspective.

## Interpretation

The raw nflverse spread representation must not be confused with
conventional sportsbook team notation.

The existing project implementation previously calculated:

`scoring_margin + spread`

using conventional sportsbook-style signs.

That implementation was internally consistent with its tests but did not
match the semantics of the raw nflverse `spread_line` column.

The target API was changed to explicitly accept the nflverse
home-perspective `spread_line`.

## Decision

Adopt the raw nflverse convention throughout the foundational dataset layer:

`home_ats_margin = home_scoring_margin - spread_line`

Code, tests, and documentation must explicitly distinguish this convention
from conventional sportsbook notation.

Status: VERIFIED
