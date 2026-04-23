---
name: Grossman-Stiglitz Noisy Rational Expectations Model
domain: economics
first_proposed: [[source/summary/grossman_1980_impossibility_informationally_efficient_summary]]
type: analytical
---

# Grossman-Stiglitz Noisy Rational Expectations Model

## Overview
Proves that informationally efficient markets cannot exist when information acquisition is costly - prices must partially reveal information to provide compensation for information gatherers.

## Basic Setup
- **Two assets**: Riskless (return R), Risky (return u = θ + ε)
- **Two trader types**: Informed (observe θ at cost c), Uninformed (observe only price)
- **Utility**: CARA V(W) = -e^(-aW) with coefficient a
- **Noise source**: Per capita supply x with variance σ_x² prevents perfect revelation
- **Equilibrium**: Price P_λ(θ,x) where demand equals supply

## Model Variations
| Paper | Variation | Key Insight Changed |
|-------|-----------|---------------------|
| [[source/summary/grossman_1980_impossibility_informationally_efficient_summary]] | Original: CARA + Normal distributions | Equilibrium exists only with partial revelation |
| [Future papers] | Different utility functions, multiple assets, strategic traders | [To be updated] |

## Key Comparative Statics
| Parameter Change | Effect on λ | Effect on ρ_θ² |
|-------------------|-------------|----------------|
| ↑ cost c | ↓ λ | ↓ ρ_θ² |
| ↑ quality n | ambiguous | ↑ ρ_θ² |
| ↑ noise σ_x² | ↑ λ | unchanged |
| ↓ risk aversion a | - | ↑ ρ_θ² |

## Papers Using This Model
- [[source/summary/grossman_1980_impossibility_informationally_efficient_summary]] - Original formulation, impossibility theorem