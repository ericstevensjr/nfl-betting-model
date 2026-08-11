# System Architecture

## Overview

The NFL Betting Model is organized as a reproducible analytical pipeline.

```text
External NFL Data Sources
        |
        v
Raw Data Ingestion
        |
        v
Validation
        |
        v
Cleaning / Normalization
        |
        v
Feature Engineering
        |
        v
Point-in-Time Dataset
        |
        v
Model Training
        |
        v
Probability Calibration
        |
        v
Backtesting
        |
        v
Market Evaluation
```

## Architectural Principles

### Reproducibility

Every generated dataset and model artifact should be reproducible from version-controlled code and documented source data.

### Point-in-Time Correctness

Features must only contain information available at the prediction timestamp.

This requirement takes precedence over convenience.

### Separation of Concerns

Data acquisition, feature engineering, modeling, and evaluation remain separate modules.

### Testability

Business logic and statistical transformations should be implemented as testable functions rather than hidden inside notebooks.

### Research vs. Production

Notebooks may be used for exploration.

Reusable logic must eventually move into the src/nfl_betting package.

Production pipelines must not depend on notebook execution.

## Package Responsibilities
```nfl_betting.data```

Responsibilities:
	- source acquisition
	- schema validation
	- normalization
	- raw data persistence
	- dataset provenance
	- nfl_betting.features


```nfl_betting.features```
Responsibilities:
	- historical rolling statistics
	- opponent-adjusted metrics
	- rest and scheduling features
	- market features
	- injury features
	- team-strength metrics

- All features must preserve point-in-time integrity.

```nfl_betting.models```
Responsibilities:
	- model training
	- prediction
	- hyperparameter configuration
	- model serialization
	- probability estimation
	- nfl_betting.evaluation

```nfl_betting.evaluation```
Responsibilities:
	- out-of-sample evaluation
	- calibration
	- ATS performance
	- expected value analysis
	- closing-line value
	- ROI
	- drawdown
	- uncertainty analysis


## Initial Modeling Target
The first continuous target is:
	- ATS margin
Defined as:
	- ATS margin = scoring margin + spread
This allows the system to estimate how much a team is expected to outperform or underperform the market line.

Later models may directly estimate:
	- P(team covers spread)

## Data Leakage Policy
Any feature containing information generated after prediction timestamp is prohibited.

Test should eventually verify temporal ordering and prevent accidental future-data joins.

## Future Components
Potential additions include:
	- experiment tracking
	- model registry
	- configuration management
	- scheduled data ingestion
	- feature store
	- betting-line snapshots
	- database persistence
	- API serving
	- dashboards
	- automated retraining
