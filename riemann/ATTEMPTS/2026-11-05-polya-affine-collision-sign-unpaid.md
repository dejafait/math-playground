# Corrected Pólya affine collision sign: bounded test inconclusive

Step 575, 5 November 2026. One analytic attempt on the approved
`0<x<=40`, `0<tau<1` target was completed. The calculations and exact
qualifications are canonical in
[L814](../lemmas/L814-normalized-polya-pencil-elimination-and-heat-order-limit.md).
No numerical scan, actual collision certificate or global zero assertion
was used. Outcome: EXPLORATION; no collision sign advance is claimed.

WHY IT FAILS: The positive raw-kernel comparison survives normalization
as a zero-mass difference with a negative tail, not a Fourier sign. It
rules out an exact normalized forward-heat identity and a nondecreasing
kernel ratio for this path. At a nondegenerate event the desired product
still contains L814's oscillatory remainder E times the curvature integral
V. The available absolute integral bound does not meet the required
relative threshold `|E|<=b|V|`; the derivative collision constraint has
not paid that remainder either. Nondegeneracy provides no numerical lower
bound for |V|. This does not show an adverse actual collision, refute the
affine path, or disprove RH. Park repetition of this unsigned comparison;
an adjacent-cosine-lobe cancellation proposal needs its own source review
and an independently checkable bound before another attempt.

Step577 audit addendum: L814's diagnostic survives the conceptual check.
Its canonical relative-bound qualification now explicitly shows that
merely choosing some positive coefficient b is equivalent to the unknown
event sign. This closes free-coefficient selection as a proposed payment,
without excluding an independently proved remainder estimate. The fold
orientation is local on the real axis; an event at x=40 does not assert
two zeros inside the test box. No actual event or adverse sign was found.
