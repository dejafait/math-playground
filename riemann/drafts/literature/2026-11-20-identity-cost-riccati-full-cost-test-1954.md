# Identity-cost Riccati full-cost test1954

TARGET: Test whether C029b's actual companion in the prescribed identity-cost Riccati block metric has k_d^R=o(1) or a positive liminf, using degree-uniform metric bounds and a full-matrix Frobenius/trace obstruction test.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1954 searched exact Riccati/Jensen/companion, quantitative CARE bounds, bounded-conditioning similarity and imaginary-part Frobenius/trace terminology; compared C028h/i/o/p, C029a and stops1948/1949/1951 in their exact scopes. No inspected theorem evaluates this actual full-cost sequence; this is not a novelty claim. See drafts/literature/2026-11-20-identity-cost-riccati-source-notes-1954.md.
SOURCE_EVIDENCE: Wimmer1976 https://doi.org/10.1017/S0004972700025387 (1)-(3) pp457-458, definitions/Lemmas1-2 p459 and Theorems2-3/full proofs pp459-461, with (A,B,C)=(I,M_d,-I), cover positive stabilizing existence with full-rank identity input/output. Reuse Schmeisser2002 https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf Lemma1 pp211-212 and Watrous2018 https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf Section1.1 (1.165)-(1.181) pp32-34 under source-notes1523/1947 and C029b; newly reinspected Watrous (1.175),(1.179)-(1.181). Precise links and caveats are in source-notes1954.
COMPARISON: General Riccati existence supplies the finite positive metric without actual-root premises. It supplies no degree estimate for the full imaginary-part trace norm. Diagonal/shear, theta-moment, two-site and flat-horizon obstructions do not identify this metric with their own. Frobenius size and similarity-invariant traces offer a concrete independent test before any more difficult positive-metric development.
GAP: Calculate explicit degree-uniform spectral bounds from the fixed equation if possible, pass them to the upper-left block, and determine whether the complete imaginary-part cost admits a positive liminf or an o(1) estimate. Neither alternative, nor any conditioning estimate, is claimed here.
REASON: Essential source coverage suffices for this bounded specialization. Separate literature-only recovery1955 reinspected the cited existence/norm statements and added direct source URLs to this assessment; no calculation was performed. The exact saved target is ready for the next research turn.
LITERATURE_REASON: Supervisor recovery requires a direct source URL in the ready assessment itself; prior source notes contained URLs but this SOURCE_EVIDENCE field did not. Repair only that gate and reuse the existing comparison.
SCOPE: Only C029b's actual real matrices, all integer d>=3, the identity-cost stabilizing equation and its upper-left principal block; no spectral reality, separation, diagonalizability or bounded conditioning may be assumed. Scalar spectral bounds and finite trace/Frobenius algebra are the only proposed new calculations.

## Exact object

Retain C029b's actual b_j, c_(d,k), normalized centered C_d and
M_d=[0 -C_d; C_d 0]. Use exactly

    M_d^T X_d+X_d M_d-X_d^2+I_(2d)=0,
    X_d real symmetric positive definite,
    spectrum(M_d-X_d) in {z:Re(z)<0},
    G_d^R = upper-left d by d principal block of X_d,
    B_d^R = (G_d^R)^(1/2) C_d (G_d^R)^(-1/2),
    k_d^R = ||(B_d^R-(B_d^R)^*)/(2i)||_1.

The norm is Schatten trace norm, not entrywise norm. All square roots
are the positive symmetric ones. Wimmer's theorem covers X_d; any
use of G_d^R must justify its principal-block positivity and resulting
spectral bounds. No changed state cost, block deletion or parameter
schedule is allowed. Wimmer's general theorem should be cited, not
reproved. Include its exact hypotheses and the full-rank applicability
argument in any later canonical result.

## One bounded calculation and decision test

First test the extremal-eigenvector scalar consequences of this fixed
equation using C029b's already proved finite bound
||M_d||_op<=A=exp(b_1)F(1). Seek explicit constants independent of d
bounding the spectrum of X_d above and away from zero; do not assume
them. Then use only the actual full companion entries, the Schatten
ideal inequality at p=2, and trace cyclicity to compare its complete
Frobenius size with the trace of its square after the prescribed
similarity. Check explicitly whether this gives a lower bound for
the entire Hermitian-imaginary Frobenius norm, hence for k_d^R.
No derived inequality, coefficient trace evaluation or answer to that
comparison is asserted in this source assessment.

A rigorous liminf k_d^R>0 suffices to abandon this metric's o(1)
payment route; any stronger growth estimate must retain its exact
constants and onset. A proof of k_d^R=o(1) would instead pay the
Schmeisser height criterion after checking C029b's degree scale.
These are not exhaustive: an inconclusive attempt must save its
failed inequality and remain inconclusive. A compression floor stops
decay but cannot certify decay; computed samples certify neither
asymptotic alternative. Do not interpret a majorant floor as a lower
bound on actual H_d or a disproof of RH.

The use toward the main gap is precisely C028b's H_d=o(d). Inputs
for a later proof are C029b's exact C_d/coefficient and norm facts,
C028b's height criterion, and the named standard sources above.
C029c and stops1948/1949/1951 are contrasts only. Full-cost decay,
the proposed quantitative obstruction, actual signed positivity and
RH remain unresolved. Full Mathlib coverage is unchecked. No
cross-notebook input, mathematical script or new lemma is proposed
as an already established result.

## Separate source-link recovery1955

On 2026-11-20 reopened Wimmer's publisher PDF via the DOI above:
(1)-(3), pp457-458; definitions/Lemmas1-2 and Theorem2 with both
proof parts, pp459-460; Theorem3 and proof, p461. The real symmetric
coefficient, sign, controllability and observability hypotheses and the
identity-input/output applicability recorded in source-notes1954 are
unchanged. Reopened Watrous's author chapter at (1.175), p33, and
(1.179)-(1.181), pp33-34: compatible finite-dimensional operators,
p in [1,infinity], and the Frobenius and trace-norm definitions. This
is textbook norm coverage, not a claim that Watrous originated these
results. Reuse the inspected Schmeisser Lemma1 scope in source-notes1523;
its Gohberg--Krein proof reference remains not independently read.

This is a source-link/process repair, not a new overlap decision or
mathematical advance. No new search, derivation, quantitative metric
bound, cost floor or decay estimate is claimed. The duplicate/failure
comparison in source-notes1954 remains applicable; no target or
hypothesis changed. Full Mathlib coverage remains unchecked.
