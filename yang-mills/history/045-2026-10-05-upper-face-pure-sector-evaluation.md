# 2026-10-05 — Separable continuum pure-sector calculation

STEP_ID: YM-20261005-045-upper-face-pure-sector-evaluation

EXPLORATION / RESEARCH / POTENTIALLY_NEW; actual task calculation, using
the unchanged SPECIALIZE assessment for the combined response.
L008 and L030–L032 supply the mathematical inputs. The new
[working record](../drafts/2026-10-05-upper-face-pure-sector-evaluation.md)
and its referenced complete certificates retain both pure sectors,
both mixed sectors, all second-index components, transitions and weights.

At cutoff 12 the finite sums are approximately (290.672,1854.720),
versus (189.233,1162.697) at cutoff 10. Quadrature refinement is stable
at each cutoff; neither it nor finite positive partial sums certifies
the infinite sum. The zeroth residual/mixed-sector/axial-zero checks
pass the numerical tolerance. Three selected N2 entries approach the
new continuum calculation in the independent existing lattice residual
at N=24,32,48. These are implementation diagnostics, not new theorems.

The exact response target and its ready assessment remain unchanged.
Continue by exploiting separability for the inverse-Laplacian weights
and testing a quantified spectral tail; stop any sign claim lacking
full quadrature and tail control. L019 compensation and all remaining
jets are unresolved. No mathematical argument in PROOF or DAG changes,
no lemma is added, and the required reflected error <= c_box/2 is
unimproved. Exploration usage is 1 of 3 after L032; prior stops survive.
