# Rational separator stability specialization1756

TARGET: Specialize positive-argument Laplace regularity and C032q's signed integration bound to give an explicit perturbation budget preserving at least half of any prescribed C033l separator gap under rational arguments and coefficients.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Comparison1756 completed nomination1755's exact source review; queries, bounded local duplicate checks and stops1571/1576 are recorded in drafts/literature/2026-11-19-residual-rational-stability-source-notes-1756.md. The exact rational conclusion was not located; no novelty is inferred.
SOURCE_EVIDENCE: Mimica, Laplace transform, Dresden course 27April-1May2015, Remark1.2(i), Proposition1.4(i)-(ii) and relevant proof, printed pp5-7, https://web.math.pmf.unizg.hr/~amimica/lt.pdf ; C032q's established signed bounded integration; C033l's audited real separator. Mean value theorem and density of Q are standard named tools. Reuse coverage1748/1750 and C033m/audit1755 without repeating their audits.
COMPARISON: The general source supplies positive-argument derivatives without an undamped moment. It does not state simultaneous rational argument/coefficient perturbation of this full signed-width separator. The finite-data uniform error budget is the local specialization still required; no reproof of differentiation is justified.
GAP: Produce explicit positive argument neighborhoods and coefficient-error tolerances, control both sides uniformly over the full signed mass-one TV<=2 class, and prove preservation of at least half the given gap with nonzero rational coefficients. No numerical input gap, construction algorithm or search termination is assumed.
REASON: This connects C033l's qualitative real existence to rational test data compatible with C033m; it is independent of the parked maximum citation and coarse-box/cost stops. Coverage is newly written and must receive separate approval before research.
SCOPE: C033l's exact finite separator and C033i's residual probability mu; C032j/q probability family on X=[0,infinity), W=[1,2]; arbitrary finite real signed Borel eta of mass1 and TV<=2, including atoms and singular parts. Retain divisor/conjugation/multiplicity, excluded ordinate zero, strip/counting, first-zero, through100, retained real zero, heat, both fixed-v1, half-variance and C033j/C032s error qualifications.

The comparison is literature only. The application obligations in
source-notes1756 are the authorized scope after separate approval.
Treat any C033l finite data and positive gap as given mathematical
parameters, not computed quantities. Do not impose a moment at zero,
drop a zero atom, restrict eta to probabilities or a grid, or exchange
suprema without proving the required uniform bound.

Continue only with a fully stated perturbation budget retaining at
least half the prescribed gap. Stop and preserve the exact missing
hypothesis if a stronger unreviewed input is required. No new numerical
search, signed support formula, continuum extremum computation,
evaluator implementation, useful-runtime claim, uncapped variation,
J_eta=0, moment control or actual-Xi realization is included. Matching
Mathlib coverage is unknown. This is routine specialization of known
tools, not a creative mechanism for the central RH gap.
