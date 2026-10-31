# Approved polynomial collision-energy calculation

Target and gate: the unchanged EXPLORE target in
`drafts/literature/2026-10-30-polynomial-heat-energy-obstruction.md`.
Main gap: actual-Xi all-degree positivity. Intermediate test: generic
locally bounded backward comparison for clipped first-Laguerre energy.
Downstream use: determine whether that comparison can be used without
an additional collision hypothesis; no actual-Xi realization is claimed.

Candidate, not yet certified: P(x)=(x^2-1)^2 and t=-lambda in [0,1/100],
H_{-t}(x)=x^4+(-2+12t)x^2+1-4t+12t^2. At t=0 there are double zeros at
both 1 and -1. For t>0 the quadratic discriminant in x^2 is negative.
The imaginary-axis positivity, full strip bound, fixed positive-defect
collars, complete sign intervals and clipped-energy calculation remain
to be checked. Expected local scaling x=1+sqrt(t)u gives
q/t -> 32u^2-64 and suggests E(-t) has order t^(3/2).

Decisive test: rigorously certify E(0)=0 and E(-t)>0 with zero external
flux for every small positive t, then apply integral Gronwall with the
correct time orientation. If a candidate condition fails, preserve the
failure and do not infer a general energy theorem. L058's quadratic
collision, L469's pointwise weighted barrier obstruction and the old
L126/L128 moving-supremum stop are comparisons, not this certificate.

No source refresh or theorem reproof is needed: the approved assessment
covers elementary smooth finite-polynomial differentiation and the
known Gronwall/truncation tools. The explicit energy evaluation is the
uncovered difference. Full matching Mathlib coverage is unchecked.

## Calculation checkpoint

The quartic meets the certificate conditions with h=1/100. With
beta=-2+12t and gamma=1-4t+12t^2, its defect is
q=4x^6+2beta x^4+(2beta^2-12gamma)x^2-2beta gamma.
Writing q=4Q_t(x^2), Q_t has exactly one negative and two positive roots
for 0<t<=h: the positive ones lie in (1/2,1) and (1,3/2).
The two negative-defect intervals therefore lie strictly inside the
required collars. Their endpoint contributions to differentiation of
the energy vanish because q=0 there; their contributions to integrating
q_xx do not vanish. Both must be distinguished.

The scaled roots x=1+sqrt(t)u tend to u=+-sqrt(2), and
q_t(1+sqrt(t)u)/t -> 32u^2-64 (here q_t denotes the slice, not a time
derivative). Consequently the expected exact energy asymptotic is
E(-t)=(512sqrt(2)/3)t^(3/2)+O(t^2). The separate derivative ratio
requires analytic dependence of the scaled endpoints; it cannot follow
by differentiating an unspecified O(t^2) remainder.

Tool note: the initial optional symbolic check could not import SymPy
in the system Python. No package was installed, no numerical output was
used, and no mathematical script or certificate depends on it. The
calculation is being completed as an exact hand proof.

Completed: the exact hand certificate, including the differentiated
analytic scaled-energy identity, is now canonical in
`lemmas/L487-quartic-heat-collision-negative-energy-obstruction.md`.
Its independent critical audit remains pending. Earlier candidate
wording above is retained as the working checkpoint, not current status.
