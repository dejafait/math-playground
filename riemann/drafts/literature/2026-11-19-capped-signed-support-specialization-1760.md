# Full signed support specialization1760

TARGET: Calculate the exact support value and an attaining measure for the full signed Borel mass-one TV<=2 class on [1,2] for a given continuous real finite Laplace payoff, including constant payoffs.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Six targeted searches and local duplicate/failure checks are recorded in drafts/literature/2026-11-19-capped-signed-support-source-notes-1760.md; no inspected exact joint-constraint formula was located. No novelty claim is made.
SOURCE_EVIDENCE: Bass2011 Theorem12.8/proof/(12.1), p97, https://webspace.science.uu.nl/~kraai101/SignedMEasures ; Buhler-Salamon2016 Example1.3.7, p28, https://math.jhu.edu/~js/Math637/eth.functionalanalysis.pdf ; Chizat2022 AppendixA PropositionA.1/proof, https://doi.org/10.1007/s10107-021-01636-z . Source-notes1760 records exact scope; bounded integration is reused from C032q.
COMPARISON: Jordan decomposition and total variation cover the full measurable class; compact continuity supplies ordinary extremum existence. The separate probability-distance and penalized problems do not state this support identity. Only the elementary simultaneous mass/cap application needs calculation and proof of attainment.
GAP: Establish the exact support value with a full-class upper bound and feasible attaining input; handle constant payoffs, cap nonsaturation and coincident extremizers without silently assuming singular nonzero parts. No formula is established in this assessment.
REASON: Essential general-source coverage is complete; a separate approved mathematical turn can perform the bounded specialization without a new source theorem, fresh general reproof or stopped evaluator implementation.
SCOPE: W=[1,2], eta finite real signed Borel, eta(W)=1, |eta|(W)<=2; f(sigma)=sum_j b_j exp(-B_sigma(q_j)), finite real b_j and q_j>0, continuous and real by C033l under unchanged C032q/C033l/n qualifications. Atoms, singular continuous parts, endpoints and infinite support are allowed; no moments, cancellation or density constraints are added.

The continuation calculates the scalar mass constraints from the imported
Jordan theorem, bounds the payoff for every input, and checks equality
by an admissible measure. Use the standard named extreme value theorem
only for existence of extrema, without claiming their computability.
Treat constant payoffs explicitly. Do not assume positivity of eta,
TV=2, or reduction to a width grid. A finite atomic attainer, if proved,
must result from the calculation, not be an input restriction.

Keep all actual-divisor, conjugation/multiplicity, zero-ordinate,
strip/counting/first-zero/through100/retained-real-zero, heat, fixed-v1,
half-variance and C033i/j/C032s qualifications. The abstract support
calculation itself uses only the signed class and real continuity;
its use for the actual Laplace family retains those conditional inputs.
No full signed positivity, moment payment, J_eta=0, uncapped variation
or actual-Xi realization is supplied. Full matching Mathlib coverage
is unchecked/unknown.

Success requires a matching upper bound and admissible attainment,
including the degenerate constant case. If either needs an unreviewed
hypothesis, record it and stop that application. The downstream use is
to identify which extrema a finite separator certificate must bound.
Actual separator data, certified extrema, coefficient-amplified margin
and useful runtime remain separate. Preserve stops1571/1576; no
implementation, general computable maximum, or numerical search is
authorized by this target. This newly written ready continuation is
submitted for separate supervisor approval, not executed this turn.
