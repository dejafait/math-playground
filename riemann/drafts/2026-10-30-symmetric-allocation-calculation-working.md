# Symmetric signed allocation: working calculation

The gate-approved target is the exact all-real-x feasibility region for
G(x)=2(x^2-1)/(x^2+1)^2+w/(x+r)^2+w/(x-r)^2,
r>0, 0<=w<=1, x!=+/-r. Reuse the supplied EXPLORE assessment
`literature/2026-10-30-signed-real-zero-allocation-coverage.md`.

Main gap: actual-Xi all-degree positivity and initial signs at unbounded
height. A finite compensation rule might retain real-zero mass dropped
in L471 (6), but actual-Xi geometry, conserved allocations, residual
mass and higher signs remain unresolved. L251/L257 are co-centered
masking contrasts; the count/gap and ordinary-moment failures remain.

Put a=r^2>0, y=x^2>=0. Away from y=a,
G/2=(y-1)/(y+1)^2+w(y+a)/(y-a)^2.
For 0<=y<1 the exact requirement is w>=f_a(y), where
f_a(y)=(1-y)(y-a)^2/((y+a)(y+1)^2).
Thus w>=a is necessary at y=0; with w<=1, a>1 is impossible.
For y>=1 all terms are nonnegative. For 0<a<=1, the remaining
question is whether the maximum on a<y<1 exceeds f_a(0)=a.
These reductions are provisional until the full endpoint and pole
cases and the polynomial identities are checked.

Continuation/abandonment test: obtain the exact threshold and equality
cases with explicit negative witnesses outside. A nonempty strict
range supports only this local certificate. No uniform positive
lower bound at infinity or actual-Xi transfer is presumed.

## Completion

The exact region, equality list, exclusions and negative witnesses
are now canonical in `lemmas/L509-symmetric-real-zero-allocation-region.md`
(notebook-relative). The comparison identity reduces the branch
transition to a^2-14a+1=0, with a0=7-4 sqrt(3). The first branch
has a unique interior maximizer; the other is governed by x=0.
The strict parameter margin does not give a global constant margin.
Three exact polynomial identities passed in the saved certificate.
The separate critical audit has not been performed. No actual-Xi
allocation or higher-sign result follows. The next audit nomination
is REVIEW_REQUIRED; no broader mechanism is approved here.
