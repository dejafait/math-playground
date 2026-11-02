# Rotation-averaged Hankel attempt — working checkpoint

Invocation-start EXPLORE assessment: drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md; exact target matches PROGRESS.md's Next action verbatim. The supplied recovery mismatch is not reproduced by the supplied snapshots. No assessment change is needed for this bounded attempt.

Main gap: actual-Xi all-degree mixed positivity. Target: the exact saved angular mean bound at exponent 1/32, or an admissible common-pole countersequence. Use C645g's normalization and C645l's same odd-m, n=3m, unit-residue Chebyshev poles on x+i[-1/2,1/2]. Independent Xi realization/census/other-pole/upper-bound/sign gaps remain.

Scoped input reads: C645g hypotheses and proof through its residue estimate; C645l hypotheses and complete proof through its full-norm limit; associated anchor-line and fixed-third ATTEMPTS, and relevant audit/source-review passages. The fixed-angle result is not an angular result.

Initial uncertified numerical endpoint screen (2000 midpoint t samples, 17 rotation directions) gives asymptotic endpoint product gains about 0.037 or larger, above 1/32. This is only exploratory evidence, not a bound or certificate. Potential countersequence mechanism: extend the SAME Chebyshev family to all rotations by controlling the continuous arc and finite-node error uniformly. The arc's individual-factor worst rotation and the ellipse's grid-inverse cost must both be bounded. The old imaginary-axis ellipse estimate is not rotation-uniform. No conclusion yet.

Continue only if the full angular norm can be rigorously bounded with an exponent strictly above 1/32. Otherwise preserve the failed constants and unresolved inequality; do not treat the screen as verification.

## Completed bounded attempt

The attempted all-angle extension by a global ellipse supremum is stopped:
the complete proof and qualifications are canonical in
[C645m](../lemmas/C645m-rotation-uniform-chebyshev-ellipse-envelope-stop.md).
At theta=pi/2 its error majorant is > (8/11)exp(s*n/12), uniformly for
0<s<=1/10 and n=3m>=39, m odd. This lower bound concerns the majorant
only; the actual error and angular norm remain undetermined. The initial
endpoint gains did not justify discarding this error cost. Full numerical
screen data and exact constant checks are saved in
`scripts/one-sided-hankel/rotation-ellipse-envelope-check.json`.

Refined continuation within the unchanged ready target: use exact angular
Laurent coefficients/residues of a scalar negative Hardy coefficient of
q_theta, rather than a uniform ellipse supremum. For w=exp(i*theta),
the exact factor in B_theta(x)/B_theta(a) is

    [(x-i*w*t)/(a-i*w*t)]*[(R^2*w+i*t*a)/(R^2*w+i*t*x)].

This is an algebraic rewriting of the saved product, not a new bound.
For t>0, the common angular poles -i*t*x/R^2 lie inside |w|=1;
the possible poles a/(i*t) lie outside. For t=0 the factor is x/a.
Some indicated poles can cancel. A future coefficient calculation must
account for these interior poles; holomorphy of the quotient in the
whole angular disk must not be assumed. The identity does not imply
noncancellation after summing over a. Parseval can be used on scalar
coefficients, not directly as an identity for an operator norm.

The unchanged invocation-start EXPLORE assessment covers this refinement;
the exact target is retained. Neither a full-mean countersequence nor a
uniform lower constant/onset has been established. The failed envelope
must not be repeated as an all-angle proof without a new contour or
cancellation mechanism. Actual-Xi realization and signs remain separate.
