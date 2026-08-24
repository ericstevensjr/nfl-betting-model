# Investigation 002 — Historical Team-Identifier Chronology

## Question

How do relocation-related team identifiers behave in the current nflverse
`games.csv` dataset, and should historical source identifiers be normalized
in the raw data?

## Hypothesis

The identifiers `SD` / `LAC`, `OAK` / `LV`, and `STL` / `LA` represent
coherent historical franchise transitions rather than inconsistent team
coding.

If the transitions are clean, the raw source identifiers should remain
unchanged, and any franchise normalization should occur explicitly in a
processed or modeling layer only when required by a research question.

## Data

`data/raw/games.csv`

Relocation-related identifiers examined:

* `SD`
* `LAC`
* `OAK`
* `LV`
* `STL`
* `LA`

Current dataset contains 7,548 rows.

## Method

1. Identified all games in which each relocation-related identifier appeared
   as either `home_team` or `away_team`.
2. Calculated the first season and last season in which each identifier
   appeared.
3. Counted the number of games associated with each identifier.
4. Compared the transition boundaries for each historical franchise pair.
5. Checked whether old and new identifiers overlapped unexpectedly by season.
6. Evaluated whether raw identifiers should be preserved or normalized.

## Result

The current artifact contains the following identifier chronology:

`SD`

* first season = 1999
* last season = 2016
* games = 298

`LAC`

* first season = 2017
* last season = 2026
* games = 171

Transition:

`SD: 1999–2016 → LAC: 2017–2026`

---

`OAK`

* first season = 1999
* last season = 2019
* games = 344

`LV`

* first season = 2020
* last season = 2026
* games = 119

Transition:

`OAK: 1999–2019 → LV: 2020–2026`

---

`STL`

* first season = 1999
* last season = 2015
* games = 282

`LA`

* first season = 2016
* last season = 2026
* games = 198

Transition:

`STL: 1999–2015 → LA: 2016–2026`

No unexpected season overlap was observed within any of the three historical
identifier pairs.

The transitions therefore behave coherently in the current dataset.

## Interpretation

The presence of more than 32 unique raw team identifiers does not indicate
that the dataset contains invalid team assignments.

Instead, the dataset preserves historical identifiers associated with
franchise relocation.

The current artifact distinguishes between historical identities such as:

`SD`

and:

`LAC`

even though those identifiers correspond to the same underlying franchise
across different periods.

The same applies to:

`OAK → LV`

and:

`STL → LA`

This distinction may be useful when representing the source data faithfully.

However, some future research questions may require franchise continuity
across relocations.

For example, a model or historical feature calculation may need Chargers
history before and after the move from San Diego treated as one continuous
franchise.

That requirement should not be satisfied by silently changing the raw data.

A future processed or modeling layer may instead define an explicit
normalization such as:

```python
FRANCHISE_NORMALIZATION = {
    "SD": "LAC",
    "OAK": "LV",
    "STL": "LA",
}
```

when franchise continuity is required.

This preserves the distinction between:

`raw_team_id`

and:

`franchise_id`

rather than forcing one representation to serve both purposes.

## Decision

Preserve historical nflverse team identifiers unchanged in:

`data/raw/games.csv`

Do not normalize:

`SD → LAC`

`OAK → LV`

`STL → LA`

inside the raw-data layer.

If franchise continuity is required by a future research question, perform
that transformation explicitly in a processed, feature, or modeling layer
and document the mapping.

Do not enforce a hard-coded modern 32-team identifier list against the raw
historical dataset.

Status: VERIFIED
