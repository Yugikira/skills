---
name: Outside Opportunities
domain: accounting
first_defined: [[source/summary/gao_2026_aggregated_compensation_peer_summary]]
---

# Outside Opportunities

## Definition
The number and quality of alternative employment options available to executives in the managerial labor market. A key construct in contracting theory that determines the reservation wage and shapes compensation contract design.

> **Key Paper**: [[source/summary/gao_2026_aggregated_compensation_peer_summary]] - Gao & Lu (2026, JAR) operationalize outside opportunities via network measures (InDegree, Louvain Size).

## Alternative Definitions
| Definition | Source | Note |
|------------|--------|------|
| "Alternative employment options with similar compensation" | Oyer [2004] | Theoretical definition; requires identification of similar firms |
| "Job offers received by executive" | Fee & Hadlock [2003] | Direct but unobservable; inferred from actual moves |
| "Firms in same product industry" | Rajgopal et al. [2006] | Narrow approximation; misses cross-industry opportunities |

## Constructs & Variables
Two primary operationalizations at different scope levels:

| Construct | Variable | Computational Definition | Key Paper |
|----------|----------|--------------------------|-----------|
| Local Opportunities | Peer_Selection_Count (InDegree) | Count of firms selecting focal firm as compensation peer | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |
| Broad Opportunities | Louvain_Group_Size | Count of firms in focal firm's Louvain group | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |

## Related Theories
- [[theories/Outside_Options_Theory]] - Oyer [2004]: outside options explain pay-for-luck and RPE puzzle
- [[theories/Reservation_Wage]] - Holmstrom & Kaplan [2003]: benchmarking sets reservation wage

## Determinants of Outside Opportunities
| Determinant | Mechanism | Key Paper | Finding |
|-------------|-----------|-----------|---------|
| Firm visibility | More visible firms attract more talent interest | Faulkender & Yang [2010] | S&P500 membership increases peer selection |
| Executive reputation | High-reputation executives have more options | Fee & Hadlock [2003] | Past performance predicts mobility |
| Industry growth | Growing industries create more opportunities | Murphy & Zabojnik [2004] | Industry pay trends affect mobility |

## Economic Consequences of Outside Opportunities
| Consequence | Mechanism | Key Paper | Finding |
|-------------|-----------|-----------|---------|
| Total compensation | Higher reservation wage increases pay | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | InDegree beta=0.105*** (t=7.363) on Ln(Total Pay); PCOMP1 beta=0.069*** |
| Equity pay share | Retention motive increases equity weight | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | PCOMP1 increases Ln(Equity Pay) by 15.1% (p<0.01) |
| Pay for luck | Firms pay for luck to retain executives | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Luck x PCOMP1 beta=0.088*** (t=2.624) |
| RPE usage | Less RPE when outside options matter | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Competition reduces RPE sensitivity by 45.6% |

## Identification Strategy
| Strategy | Assumption | Key Paper | Note |
|----------|------------|-----------|------|
| InDegree measure | Selection as peer indicates talent demand | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Captures revealed demand, not latent options |
| Louvain Size | Group size reflects market breadth | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Broader scope; may include irrelevant firms |

## Future Works
- **Quality vs quantity**: How to weight opportunities by compensation level?
- **Dynamic measurement**: How quickly do outside opportunities change?
- **Individual heterogeneity**: Do outside options vary by executive skill type?