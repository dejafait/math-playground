# Arbitrary even contact fibers — working checkpoint

6 November 2026. Invocation-start EXPLORE assessment:
`drafts/literature/2026-11-06-all-even-rank-one-contact-fibers.md`.
The sole target is its unchanged TARGET. Existing notebook changes are
preserved. L847 supplies the exact coefficient and L864 supplies the
rank-one tangents and positive scalar. L865 is the audited double-order
comparison, not an input needed for the proposed extension. The inspected
count-only, two-moment and singular real-flux stops remain in force.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Intermediate use: excluding isolated rank-one contacts of arbitrary
fixed even orders would remove this singular-preimage exception from a
finite ENTIRE contact census, without supplying global signs or extension.
Test: prove both exact fibers and the entire union under the full C2
hypotheses, or exhibit an exact admissible counterexample; if inconclusive,
save the first missing phase estimate and reassess.

## Partial argument saved before full write-up

Write f=(Phi1-zeta)/alpha and g=(Phi2-eta)/beta, with
alpha=zeta(a+i), beta=eta(d+i), b=c=0 from L864. Then
Df(0)(x,y)=x, Dg(0)(x,y)=y and q=B f^m g^n, where
B=K alpha^m beta^n is continuous and B(0)>0. K retains L847's
minus sign, units, squared difference, denominators and J.

For each signed t!=0 on |x|<=|t|, y=t, differentiability at the
origin gives g(x,t)/t -> 1 uniformly as |t| -> 0. Thus
A_t(x)=B(x,t)(g(x,t)/t)^n has positive real part on every such
small segment. Put theta=pi/m. The real continuous function
Im(exp(-i theta) f(x,t)) has opposite endpoint signs, since
f(+/-|t|,t)/|t| -> +/-1 for both signs of t. At its zero,
f=r exp(i theta) for real r, so f^m=-r^m. Since m,n are even,
Re q=-t^n r^m Re A_t forces r=0. Angular rigidity then forces
x=0; hence Phi1(0,t)=zeta. Interchange the roles and use pi/n
to force Phi2(t,0)=eta.

This is a proposed complete mechanism, not yet an independently audited
result. Still to write/check: the explicit uniform first-order remainder
bound, common signed-t neighborhood, endpoint margins for every fixed
even order, nonvanishing full coefficient and complete local zero union.
No Hatcher lift or root branch is required: the inspected real IVT
suffices. No higher-order Taylor theorem for the C1 density is used.

Actual multiple-zero labels, rank-two and J=0 cases, nonisolated-germ
existence, global extension and Xi signs remain unresolved. No central
creative mechanism is nominated by this local specialization. Full
matching Mathlib coverage is not checked. No mathematical script used.

## Completion checkpoint

The uniform signed-segment estimates, tilted-line test and entire union
are now written in canonical
`lemmas/L866-even-rank-one-contacts-force-crossing-fibers.md`.
The above partial reasoning is preserved as the pre-write-up checkpoint.
The proof uses only the already assessed factorization, differentiation
and real IVT tools; the Hatcher lift is unnecessary. This completed
mathematical attempt records a local ADVANCE / POTENTIALLY_NEW in the
bounded-search sense, pending an independent conceptual audit. It is
not a candidate solution of RH or an assertion that the germs exist.
