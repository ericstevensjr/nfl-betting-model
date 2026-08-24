# Investigation 003 — NFL Home-Team Scoring-Margin Distribution

## Question

How are NFL home-team scoring margins distributed in the current historical
dataset, and what does their variability imply for predicting individual game
outcomes?

## Hypothesis

Home teams will have a modest positive average scoring margin historically,
but individual game margins will vary substantially around that average.

If the variability is large relative to the average home advantage, then an
expected scoring-margin prediction should not be interpreted as a precise
forecast of the final game margin.

## Data

`data/raw/games.csv`

The analysis uses completed games only.

Scoring margin is represented by:

`result = home_score - away_score`

Current artifact:

- total rows = 7,548
- completed games = 7,276
- unplayed games = 272

All rows with missing `result` were excluded from the scoring-margin
distribution analysis.

## Method

1. Loaded the current raw nflverse games artifact.
2. Selected nonmissing `result` values representing completed games.
3. Calculated the mean and median home-team scoring margin.
4. Calculated variance and standard deviation.
5. Examined the minimum, maximum, and quartiles of the distribution.
6. Interpreted the statistics in the context of NFL scoring-margin prediction.

Variance and standard deviation were calculated using pandas' default sample
statistics (`ddof=1`).

## Result

Completed games:

`7,276`

Mean home-team scoring margin:

`+2.344`

Median home-team scoring margin:

`+3`

Variance:

`212.905`

Standard deviation:

`14.591 points`

Observed range:

`-49 to +59`

Quartiles:

- 25th percentile = `-7`
- 50th percentile = `+3`
- 75th percentile = `+11`

The middle 50% of observed home-team scoring margins therefore falls between:

`-7 and +11`

## Interpretation

Across the current historical sample, home teams have outscored away teams by
approximately 2.34 points per game on average.

This should not be interpreted as saying that a home team usually wins by
2.34 points or more.

The mean describes the average result across thousands of games.

The standard deviation of approximately 14.6 points is much larger than the
average home-team scoring advantage.

This indicates substantial game-to-game variability.

Even the middle 50% of outcomes spans from an away-team advantage of 7 points
to a home-team advantage of 11 points.

Therefore, an expected scoring margin and an actual realized scoring margin
are fundamentally different quantities.

For example, a future model predicting:

`Expected home margin = +3`

would not be claiming that the game will finish with the home team winning by
exactly 3 points.

The prediction would represent the center of an uncertain outcome
distribution.

This variability is one reason that sports-prediction systems must eventually
be evaluated across many observations rather than judged by individual wins,
losses, or exact-score misses.

It also motivates later use of prediction-error measurements such as mean
absolute error.

## Decision

Treat predicted scoring margin as an expected value rather than a precise
individual-game outcome.

Future scoring-margin models should be evaluated over sufficiently large
samples using appropriate error metrics and uncertainty-aware interpretation.

The observed historical variability should remain part of the project's
mental model when interpreting both model predictions and betting results.

Status: VERIFIED
