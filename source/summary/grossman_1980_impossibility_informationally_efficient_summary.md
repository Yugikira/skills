---
title: On the Impossibility of Informationally Efficient Markets
doi: 10.7916/D8765R99
citekey: grossman_1980_impossibility_informationally_efficient
authors: [Sanford J. Grossman, Joseph E. Stiglitz]
year: 1980
journal: The American Economic Review
keywords: [informationally efficient markets, rational expectations, information acquisition, price system, competitive equilibrium]
processed: 2026-04-23
source: [[raw/papers/grossman_1980_impossibility_informationally_efficient/grossman_1980_impossibility_informationally_efficient.pdf]]
---

# On the Impossibility of Informationally Efficient Markets

## One-Line Summary
Proves that informationally efficient markets cannot exist when information acquisition is costly, because prices cannot perfectly reflect costly information without eliminating the incentive to acquire it.

## Abstract Summary
The paper develops a noisy rational expectations model showing that equilibrium requires prices to partially—but not perfectly—reveal informed traders' information. If prices fully revealed information, informed traders would have no advantage; if no one acquires information, prices convey nothing, creating an incentive to become informed. This paradox proves competitive equilibrium cannot exist with perfect information revelation.

## Claimed Findings
> **5 KEY INTERPRETATIONS** - Authors' main claims.

- Claim 1: Informationally efficient markets (where prices fully reflect available information) cannot exist when information acquisition is costly.
- Claim 2: Equilibrium requires an "equilibrium degree of disequilibrium" where prices partially reveal information.
- Claim 3: The informativeness of the price system depends on the proportion of informed traders λ, which is endogenously determined.
- Claim 4: Markets become thin when the price system is very informative (λ near 0) or very uninformative (λ near 1).
- Claim 5: There is a fundamental conflict between the efficiency with which markets spread information and the incentives to acquire it.

## Ground Truth Findings
> **ANALYTICAL MODEL - No empirical findings. Results are Theorems/Propositions.**

- Finding 1: **Theorem 5** - If σ_x² = 0 (no noise), equilibrium does not exist if e^ac < √(1+n). If σ_ε² = 0 (perfect information), equilibrium never exists.
- Finding 2: **Equation (19b)** - Equilibrium informativeness ρ_θ² = 1 - (e^2ac - 1)/n, determined by cost c, quality n, and risk aversion a.
- Finding 3: **Theorem 2** - Ratio of expected utilities γ(λ) = e^ac × √(Var(u|θ)/Var(u|w_λ)), strictly increasing in λ.
- Finding 4: **Theorem 4A** - Equilibrium informativeness rises if n rises, c falls, or a falls.
- Finding 5: **Theorem 4B** - Equilibrium informativeness unchanged if σ_x² or σ_u² changes (with n fixed); λ adjusts to offset.

## Other Interpretations
- [Awaiting future papers]

## Concepts Defined
| Concept | Definition | Constructs | Wiki Page |
|---------|------------|------------|-----------|
| Informationally Efficient Market | Market where prices fully reflect all available information | Price function P_λ(θ,x) | [[concepts/Informationally_Efficient_Market]] |
| Price Informativeness | Degree to which price system reveals θ to uninformed traders, measured by ρ_θ² = 1/(1+m) | w_λ signal, variance Var(w_λ|θ) | [[concepts/Price_Informativeness]] |
| Equilibrium Degree of Disequilibrium | Equilibrium fraction λ of informed traders that balances information value against cost | γ(λ) function | [[concepts/Equilibrium_Degree_of_Disequilibrium]] |

## Measures/Variables
> **ANALYTICAL MODEL - No observable variables. Skip wiki/variables/ creation.**

| Paper Variable | Wiki Name | Constructs | Concept | Computational Definition | Wiki Page |
|----------------|-----------|------------|---------|--------------------------|-----------|
| N/A | - | - | - | This paper has no empirical variables | [Skip - analytical model] |

## Model Parameters & Constructs (Analytical Models Only)
> **For analytical/model papers**: These are theoretical constructs.
> Create wiki/constructs/ pages for these. NO wiki/variables/ pages.

| Construct | Symbol | Type | Definition | Wiki Page |
|-----------|--------|------|------------|-----------|
| Proportion Informed | λ | model_parameter | Fraction of traders who pay cost c to observe θ | [[constructs/Proportion_Informed]] |
| Information Noise | σ_ε² | model_parameter | Variance of unobservable component ε in u=θ+ε | [[constructs/Information_Noise]] |
| Signal Variance | σ_θ² | model_parameter | Variance of observable signal θ | [[constructs/Signal_Variance]] |
| Supply Noise | σ_x² | model_parameter | Variance of per capita supply x (noise source) | [[constructs/Supply_Noise]] |
| Risk Aversion | a | model_parameter | Coefficient of absolute risk aversion in V(W)=-e^(-aW) | [[constructs/Risk_Aversion]] |
| Information Cost | c | model_parameter | Cost to observe realization of θ | [[constructs/Information_Cost]] |
| Information Quality | n | model_parameter | Ratio σ_θ²/σ_ε² (higher = more precise information) | [[constructs/Information_Quality]] |
| Price Noise Ratio | m | model_parameter | (aσ_ε²/λ)² × σ_x²/σ_θ² (inversely related to informativeness) | [[constructs/Price_Noise_Ratio]] |
| Price Informativeness | ρ_θ² | model_parameter | Squared correlation between P_λ and θ, = 1/(1+m) | [[constructs/Price_Informativeness]] |
| Informed Traders | - | definitional_construct | Traders who pay cost c to observe θ, demand X_I(P,θ) | [[constructs/Informed_Traders]] |
| Uninformed Traders | - | definitional_construct | Traders who only observe price, demand X_U(P;P*) | [[constructs/Uninformed_Traders]] |
| Price Signal | w_λ | definitional_construct | w_λ = θ - (aσ_ε²/λ)(x-Ex), signal revealed by price | [[constructs/Price_Signal]] |

## Hypothesis
### Hypothesis Statement
No formal hypothesis. The paper proves an impossibility theorem: competitive equilibrium cannot exist when prices perfectly reflect costly information.

### Argument Structure
| Premise | Source | Type |
|---------|--------|------|
| Information acquisition is costly (c > 0) | Assumption | Assumption |
| Prices convey information from informed to uninformed traders | Rational expectations theory (Lucas, Green) | Theory |
| Competitive equilibrium means all arbitrage profits eliminated | Definition | Definition |
| Traders maximize CARA expected utility | Economic theory | Assumption |

### Reasoning Approach
- **Type**: Deductive - Mathematical proofs derive conclusions from assumptions with logical certainty.
- **Relation**: Valid - Conclusions necessarily follow from premises through formal proofs.

### Evaluation
- **Status**: Sound
- **Reason**: Mathematical proofs are correct and assumptions (costly information, rational expectations) are empirically plausible.

## Methods
> **ANALYTICAL MODEL - Use method_analytical.md template.**

**Model**: Grossman-Stiglitz Noisy Rational Expectations Model
- **Type**: analytical, rational-expectations
- **Assets**: Riskless (return R), Risky (return u = θ + ε)
- **Traders**: Informed (observe θ at cost c), Uninformed (observe price)
- **Utility**: CARA V(W) = -e^(-aW)
- **Equilibrium**: Price function P_λ(θ,x) where demand = supply

→ Create wiki/methods/Grossman_Stiglitz_Noisy_RE_Model.md using templates/method_analytical.md

## Limitations
- CARA utility assumption may not match real preferences
- Single risky asset with normal distribution - simplified market
- Assumes traders learn true distribution over time - ignores learning dynamics
- No strategic behavior by informed traders (competitive price-taking)
- Perfect competition assumption may not hold in real markets

## Related Papers
| Authors | Year | Title | Relevance | Wiki Link |
|---------|------|-------|-----------|-----------|
| Lucas, R.E. | 1972 | Expectations and the Neutrality of Money | Rational expectations model foundation | [not in wiki] |
| Green, J.R. | 1973 | Information, Efficiency and Equilibrium | Information flows between traders | [not in wiki] |
| Fama, E. | 1970 | Efficient Capital Markets: A Review of Theory and Empirical Work | Efficient markets hypothesis target | [not in wiki] |
| Hayek, F. | 1945 | The Use of Knowledge in Society | Price system as information conveyor | [not in wiki] |