# Explicit gamma-log linearization: quantitative component

TARGET: Test the explicit gamma-log linearization error <=1/100 on |z-X|<=1 for 1/25<=t<=11/50 and X>=4*pi*exp(10000)+2, using the source logarithm.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact gamma/phase/linearization and stronger explicit real-simple-tail search and local duplicate/failure comparison recorded in drafts/heat/2026-10-30-explicit-gamma-phase-source-review.md; no matching numerical linearization certificate was found in the checked material, with no novelty inference.
SOURCE_EVIDENCE: D. H. J. Polymath, arXiv:1904.12438v2 (4 August 2019), https://arxiv.org/html/1904.12438v2 , (6)–(10),(26),(42)–(43),(75)–(76),(100), Lemma 9.2 and its proof inspected; these give the explicit logarithm/derivatives and the corresponding qualitative phase/variation model.
COMPARISON: Lemma 9.2 has the needed qualitative model but an unspecified O(log X/X) constant and onset. The exact formulas permit a numerical specialization without a new saddle theorem; they do not state the proposed 1/100 inequality.
GAP: Prove or refute the specified uniform numerical error from explicit formulas, keeping the source branch at the center and throughout the closed complex disk. No phase error bound is established here.
REASON: This local phase/modulus component could feed a strict contour comparison with L490 and later a numerical collision rectangle; zero counts, complete exhaustion, collision exclusion and zero-time control remain independent.
SCOPE: One analytic calculation of the explicit model only, with elementary complex logarithm estimates and integration of the exact derivative. No source saddle reproof, residual reflection theorem, contour count, global tail, new zero-free region, or creative collision mechanism is covered. This newly written continuation receives separate approval next turn.

## Exact proposed test

Use the source's functions alpha and M_t, and define the explicit
logarithm ell_t(s) to be source equation (7) plus t*alpha(s)^2/4.
Use that branch, rather than a principal logarithm of the value M_t(s).
For the purpose of the proposed test define

    G_t(z)=ell_t((1+iz)/2)-ell_t((1-iz)/2),
    L_X=log(X/(4*pi)),
    g(X,t)=X/(4*pi)*L_X-X/(4*pi)+11/8+(t/16)*L_X.

The precise UNPROVED test inequality is

    |G_t(X+w)-i*(2*pi*g(X,t)-pi)-(i/2)*L_X*w| <= 1/100

for every real 1/25<=t<=11/50, real X>=4*pi*exp(10000)+2,
and complex w with |w|<=1. The tolerance and the extra 2 in the edge
are proposed parameters, not achieved bounds or a certified cutoff.
No center phase estimate, disk estimate or corollary is derived here.

## Available inputs and application obligations

The source's exact branch (7), alpha formula (9), deformation (10),
derivative (42) and logarithmic derivative (100) are the inputs.
Its explicit (43) requires Im(s)>3. In the Proposition 6.6 proof,
(75)–(76) are used at s=sigma+ix/2 with 0<=sigma<=1, x>=200:

    |alpha'(s)| <= 1/(x-6),
    |alpha(s)-(1/2)*log(x/(4*pi))-i*pi/4|
        <= (2+sigma)/(x-6).

Any use at the lower half-plane arguments must be justified from the
explicit formulas/conjugation; a negative imaginary part cannot be
inserted into (43). Any real-center argument computation must retain
the fixed branch in (7), not merely an argument modulo 2*pi.
The closed time and disk endpoints and varying X must all be covered.
The added edge padding is to keep a future radius-one comparison
within L490's x-range; no height transfer is thereby proved.

L490 is a downstream input, not needed to calculate this explicit
model. L488's qualitative proof provides motivation for the linear
comparison but supplies no numerical constants. Neither result is
being reproved. The need for this specialization is exactly the
missing effective constant in Lemma 9.2; it is reproduction of known
asymptotic structure, with no originality claim.

Continue only on a uniform analytic certificate for the complete
stated domain. If the tolerance fails, record the responsible term
and domain before changing it or the height. A finite sample or a
bare asymptotic does not pass. Even success requires later separate
strict contour and exhaustion work before a numerical real/simple
tail can be claimed. Full matching Mathlib coverage is unchecked.
