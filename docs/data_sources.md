# Data Sources 

## NFL Game/Schedule Data

### Upstream Source

The initial historical NFL game-level dataset is sourced from the [nflverse/nfldata](https://github./com/nflverse/nfldata) project.

Raw source artifact:

`data/games.csv`

Local raw destination:

`data/raw/games.csv`

Acquistion code:

`src/nfl_betting/data/download_games.py`

The raw file is downloaded programmatically and should be treated as an immutable source artifact.

Generated raw data is excluded from Git. The repository versions the code required to reproduce the acquisition instead of comitting the downloaded dataset itself.

## Unit of observation

One row represents one NFL game.

The downloaded artifact currently contains:

- 7,548 game rows
- 46 columns
- seasons from 1999 through 2026

Observed game types include:

- `REG` - regular season
- `WC` - Wild Card
- `DIV` - Divisional Round
- `CON` - Conference Championship
- `SB` - Super Bowl

These properties describe the artifact observed during development and should not be assumed to remain permanently unchanged upstream.

## Game identifier

`game_id` behaves as a unique, non-null game identifier in the current artifact.

Example:

`1999_01_MIN_ATL`

Structure:

`SEASON_WEEK_AWAY_HOME`

for this example:

- season: 1999
- week: 1
- away team: MIN
- home team: ATL

The current artifact contains no missing or duplicate `game id` values.

## Outcome convention

The `result` field is expressed from the home team's perspective:

`result = home_score - away score`

Examples:

- positive `result` -> home team won
- negative `result` -> home team lost
- zero `result` -> tie

Completed games should satisfy this relationship exactly.

Future or unplayed games may legitimately have missing outcome fields.

Partially populated outcome fields are treated as invalid/incomplete data.

## Spread convention

The upstream `spread_line` field is also expressed using the home-team perspective.

A positive value means the home team is favored.

A negative value means the away team is favored.

Example:

`spread_line = +3.5`

means the home team is favored by 3.5 points.

Example:

`spread_line = -3.0`

means the away team is favored by 3 points.

For the home team, an ATS-margin target can therefore be constructed as:

`ats_margin = result - spread_line`

Example:

- home result: +6
- spread line: -3
- ATS margin: +9

The home team outperformed the market expectation by 9 points.

## Betting-market fields

Relevant market fields include:

- `spread_line`
- `home_spread_odds`
- `away_spread_odds`
- `total_line`

These represent different quantities.

`spread_line` describes the market's expected scoring-margin relationship.

Spread odds describe the wager price.

`total_line` describes the over/under scoring market.

These fields must not be treated as interchangeable.

## Point-in-time integrity

Feature eligibility depends on the predictive timestamp.

A value is not safe merely because its column name sounds like pregame information.

For every candidate feature, the project must determine whether the value was actually available at the historical prediction timestamp.

Outcome fields such as:

- `home_score`
- `away_score`
- `result`
- `total`

must never be used as predictive features for the same game.

They may be used after the game to construct historical targets and evaluate predictions.

The current `spread_line` is treated as a closing line. It is only a valid feature for models whose prediction timestamp occurs after that closing line would constitute future information.

## Historical feature construction

Rolling or historical team features must exclude the game being predicted.

For example, a Week 10 pregame feature may use information through Week 9 but must not use Week 10 results or later games.

This rule applies to statistics such as:

- scoring averages
- EPA
- success rate
- turnovers
- team ratings
- opponent strength
- rolling performance measures

## Provenance caution

Some fields require additional provenance investigation before they are approved as model features.

For example, quarterback-name fields may appear to be pregame information, but the project must verify whether the upstream value represents a pregame-known starter or a designation assigned using postgame information.

Feature inclusion requires evidence of point-in-time validity, not merely a plausible column name. 
