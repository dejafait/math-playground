# Dyadic amplitude flattening — 2026-09-13

Attempt: replace W(t) by its dyadic average in E_T[χ''(Q/M)W(t)]
using the small pointwise derivatives of the Gaussian amplitudes.

WHY IT FAILS: [Lemma 166](../lemmas/L166-gaussian-resonant-mass-does-not-flatten.md)
proves that the absolute L1 variation about that average is comparable
to (log T)^4, even after relative normalization it stays bounded away
from zero. The derivative's 1/T scale is canceled by the dyadic interval
length. Thus no estimate uniform over bounded test functions supplies
o(1) error. This does not disprove replacement for the actual fixed
χ''(Q/M): that special signed covariance still requires a separate
cancellation argument.
