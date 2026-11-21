# Gaussian remainder derivative-sign hypothesis — reviewed specialization

TARGET: Classify the whole-support derivative-sign applicability of the n-node Gaussian remainder for L795's theta/Laguerre integrand for all integers n>=1,d>=0 and real x>0, separating exactness, nonzero constant-sign and sign-changing cases without numerical sweeps.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step543's completed Gaussian/Hermite-remainder and Laguerre-derivative comparison in 2026-11-05-theta-signed-gauss-remainder-discovery.md, including exact queries and targeted duplicate/stop checks; no new search or mathematical derivation in this nomination.
SOURCE_EVIDENCE: Gautschi OUP2004 Theorem1.48/corollary pp23–24,(1.4.10)–(1.4.16), complete proofs reused from step543, https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf ; directly rechecked https://dlmf.nist.gov/18.9.E23 , https://dlmf.nist.gov/18.3.T1 , https://dlmf.nist.gov/18.2#vi and https://dlmf.nist.gov/3.5.E19 through E20_1; L795 normalization https://dlmf.nist.gov/18.5.E12 reused.
COMPARISON: Known derivative and zero theorems supply the tools; the exact normalized theta-integrand degree/node classification is the unpaid conventional specialization. This is different from testing the two reference cubics for common interlacing and proves no new hyperbolicity result.
GAP: Check the full degree/node classification, all chain-rule factors and degenerate cases on unbounded positive support, and decide what it permits for a derivative-sign-only barrier mechanism. Actual signed cancellation and reference margins remain independent gaps.
REASON: One finite symbolic argument can establish an exact applicability threshold or expose a precise sufficient-premise obstruction; no additional numerical pair, precision increase, degree sweep or general tolerance theorem is justified.
SCOPE: Proposed in step543; separate literature approval completed in step544, repairing missing direct source URLs. Covers only a polynomial derivative and quadrature-exactness hypothesis test, not construction of a theta Peano kernel, its cancellation, a new contour limit or a root-sign barrier.

Use L019/L021 and L795's actual law nu, the pushforward of K(u)du/m_0
under v=u^2. For each fixed d and real x>0 set

    f_(d,x)(v) = [d!/(1/2)_d] L_d^(-1/2)(vx/4).

The n-node Gaussian rule is for raw v moments, not orthogonality of
the Jensen family. Examine the sign of the ordinary derivative
partial_v^(2n) f_(d,x)(v) for every v>0. Determine its exact regimes,
including derivatives above the polynomial degree, degree zero and
the x=0 endpoint separately. Do not assume the sign of P_d, its
roots, or any common interlacer. No L791/L778 numerical input is
needed. Integrability of any polynomial used must be tied to L021;
do not invoke a smooth-function theorem on an infinite interval
without that check. For the derivative formula cite DLMF18.9.23;
for zero location cite the Laguerre theorem with its actual shifted
parameter >-1. Do not reprove these standard theorems.

Main gap: actual-Xi all-degree mixed positivity. Downstream use:
decide whether the most direct derivative-sign-only Gaussian
remainder mechanism has any nontrivial growing-degree scope before
investing in a signed barrier construction. The discriminating test
is an exact symbolic classification valid for all n,d, not a sample
of degrees. Check whether any nonzero sign case can furnish the
alternating directions a root barrier would need. Continue only if
it leaves such a regime; otherwise record the precise limitation and
park this sufficient mechanism. Sign changes of a derivative do not
determine its actual weighted integral. Reference hyperbolicity,
signed cancellation, quantitative margins and transfer to mixed
positivity remain unresolved whatever this test yields.

This is a REPRODUCTION/theorem-specialization target, not a protected
creative attempt or a claimed new standard theorem. A proof may be
short and needs no mathematical script or numerical certificate.
Keep a canonical proof if a relevant classification is established;
do not manufacture auxiliary lemmas. Mathematical exploration usage
is not reset by this nomination. Full matching Mathlib coverage is
unchecked; no cross-notebook input is proposed.

## Separate source approval — step544, 5 November 2026

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this otherwise ready assessment; this bounded repair verifies the cited source scope, without reopening discovery or performing the saved calculation.

The target text and SPECIALIZE decision are unchanged. Directly inspected
[DLMF18.9.23](https://dlmf.nist.gov/18.9.E23), including its attribution
to Szego (1975), (5.1.14): a first derivative lowers the Laguerre degree
by one, raises alpha by one and introduces a minus sign. Apply it only
at positive degree; polynomial exhaustion and the x=0 endpoint must be
handled separately in the research turn. No iterated theta derivative
or sign classification is derived in this approval.

Directly inspected the Laguerre row of
[Table18.3.1](https://dlmf.nist.gov/18.3.T1): the orthogonality interval
is (0,infinity), the weight is z^alpha exp(-z), and alpha>-1 is required.
[Section18.2(vi)](https://dlmf.nist.gov/18.2#vi), citing Andrews et al.
(1999), Theorems5.4.2–5.4.3, supplies simplicity and location of all
positive-degree orthogonal-polynomial zeros in their open interval.
The research turn must verify the shifted parameter and degree before
using this theorem; these are not statements about zeros of the average.

Rechecked [DLMF3.5(v)](https://dlmf.nist.gov/3.5#v), specifically
[3.5.19](https://dlmf.nist.gov/3.5.E19),
[3.5.20](https://dlmf.nist.gov/3.5.E20) and
[3.5.20_1](https://dlmf.nist.gov/3.5.E20_1): the setup allows finite or
infinite orthogonality intervals; it states the derivative remainder
with squared monic-polynomial norm and exactness through degree 2n-1.
Reuse the complete Hermite-interpolation proof inspected in step543,
Gautschi (2004), Theorem1.48 and corollary, pp23–24, at the direct book
URL in SOURCE_EVIDENCE. That proof was not reread in this repair.
No general unbounded-interval smooth-function extension is approved.
The saved target uses polynomials only: use L021's finite moments and
L019/L795's actual measure, checking every integral needed. The
Laguerre weight describes the source zero theorem, not the theta
quadrature measure. No replacement of that measure is authorized.

Reuse step543's exact-statement searches and duplicate/failure
comparison (including L795/L796/L805 and the root-disk transfer stop);
no new broader search was needed for this unchanged target. Full
matching Mathlib coverage remains unchecked. This source repair adds
no mathematical result, no new obstruction and no claim of novelty.
The exact all-n,d classification remains unpaid. The sufficient-mechanism
continuation test and independent sign/margin gaps above remain intact.
The next turn may carry out the saved REPRODUCTION calculation under
SPECIALIZE; no new target has been nominated.
