# Conditional tilted-Xi audit2008 — completed record

Gate: assessment2007 SPECIALIZE, reused unchanged. This is a standard
conditional applicability proof, not an actual-family index estimate.

Checks completed in canonical C029m: exact real coefficients follow from
Kuznetsov (13), (4) and basis recurrence (2); actual degrees are used,
not degree=N. Imported compact limit is F(t)=exp(-pi*t/4)Xi(t).
Endpoint values give F(i/2)=exp(-i*pi/8)/2 and
F(-i/2)=exp(i*pi/8)/2, unequal. Hence compact convergence forces
all sufficiently late polynomials to be nonconstant. C029l applies
conditionally on eventual negative index<=1. The tilt has no zeros.
Real s excludes pure imaginary t; remaining off-real t has nonzero
real and imaginary parts, hence four distinct nonreal Xi orbit points.
This contradicts the bound of two. Multiplicities and nullity need no
extra assumptions. Full proof is in
[canonical C029m](../lemmas/C029m-tilted-xi-eventual-index-conditional-rh.md).

Unproved: the eventual index premise. Source convergence is imported
from Kuznetsov p568, not independently reproved; upstream[9] remains
unaudited. Runtime and summability stops2002/2003/2005 are preserved.

Validation: notebook-scoped documentation checker passed with 1521
nodes and 3772 edges, acyclic dependencies, complete file coverage,
valid links and compact overviews. Scoped git diff --check and exact
Next action / NEXT_REVIEW target matching passed. These are structural
checks only. Mathematical verification was the written applicability
audit, not a numerical computation. The only new local mathematical
input row is C029m: C029l; external inputs are cited in the proof.
