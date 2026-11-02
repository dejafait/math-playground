# Bounded sextic first-sign attempt

Approved input: `drafts/literature/2026-11-01-sextic-finite-first-sign-test.md`
(EXPLORE, saved before invocation). Main gap: actual-Xi signs at all
heights/degrees. Target: BOTH global spatial Stein nonincrease and a
strict negative first Fourier sign in the approved rectangle. A witness
would stop the generic transfer implication, not imply any Xi sign.

Existing contrast L606 has all real zeros and cannot work; L605's hazard
specialization is a methodological comparison only. Reuse the named
Bagnoli--Bergstrom and Saumard source coverage; do not infer a first-sign
failure or collision from Newman necessity. No external browsing needed.

Plan: at most 256 exploratory triples (F,F',F'') at positive b and
0<x<=64, followed by one rigorous candidate certificate if available.
Use unnormalized Fourier integrals; normalization multiplies the
determinant by a positive constant. Preserve all sample values and
distinguish floating cancellation from proof. No automatic budget growth.

Spatial reasoning to complete: q(s)=exp(-s^3-bs), s>0, has
(log q)''=-6s. The weighted-tail substitution should give
tau(u)=1/(2 r(u^2)); check all normalization and endpoint hypotheses.
The auxiliary density is positive, normalized by finite J, C1 on
(0,infinity), and log-concave. The imported hazard theorem gives
tau nonincrease on [0,infinity), with tau(0)=J/2, evenness and smoothness.

The 256 exploratory triples identified b=4,x=10 as the strongest
negative candidate (unnormalized D about -1.2845884e-6). One exact
integer-interval Simpson certificate, N=8192 on [0,2], encloses
G in [2041,2043]*1e-6, G' in [-552,-550]*1e-6, and
G'' in [777,779]*1e-6, hence D<=-1281153/10^12.
The certificate includes derivative-based Simpson errors, Taylor
rounding enclosures and full infinite-tail errors; no collision premise.
Files: scripts/sextic/first_sign_search.py and certify_first_sign.py,
with their corresponding JSON records. Canonical statement/proof to
be saved as L607. This refutes precisely the generic implication
from the stated smooth even spatial hypotheses to the first sign;
it does not transfer a sign to Xi. Independent audit remains necessary.
