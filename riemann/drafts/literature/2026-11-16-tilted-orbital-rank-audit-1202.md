# Separately tilted orbital rank comparison — audit coverage1202

TARGET: Audit Sra author v3 Lemma C.7 and Theorem C.8: for every finite real diagonal D, real x and adjacent ranks k,k+1, verify min(D)<=Gamma_(k+1)(x)-Gamma_k(x)<=max(D) under their separately normalized Haar exponential tilts, including repeated rates and ranks0,n, and retain the finite-reference qualification in (C.17).
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Discovery1202 searched exact tilted-corner/rank-increment terminology and scoped duplicate records; review884 covered C.9's statement/closure but no local C.7/C.8 audit was found. No novelty claim. Reuse the completed discovery for source/stop comparison.
SOURCE_EVIDENCE: Sra author riem-xi-v3, released2November2026, LemmaC.7/TheoremC.8 complete proofs pp25-27, (C.14)-(C.17); LemmaC.6 statement/(C.10),(C.13) pp23-25 and C.9 complete downstream proof pp27-29. Olshanski JLT23(2013), Corollary3.2 p1017 and Proposition3.1/(10) pp1015-16 inspected in publisher PDF; exact links below.
COMPARISON: The desired inequality is explicitly known in this source. Only a bounded independent proof audit and precise applicability qualification are proposed; no new theorem, arbitrary-order actual-Xi sign or reproof of the cited orbital-measure theorem is needed. Separate normalizers and repeated top boundaries are load-bearing issues that an untilted coupling cannot settle.
GAP: Verify the source's mesh/stationary and degenerate-boundary arguments and both field-ordering cases before relying on its signed reference comparison. Actual-Xi transfer, factor supply for all orders and common-graph realization remain independent unresolved gaps.
REASON: A conceptual audit of a newly scoped signed multi-particle input is useful before constructing any central mechanism from it. SPECIALIZE permits source reproduction/audit only; this assessment is newly written and requires separate approval next turn.
SCOPE: Arbitrary finite n>=1; real q_j and x; 0<=k<n; normalized Haar measure. This is not an audit of C.9's full PF theorem, the verified-height certificate, Gaussian transfer, or an actual-Xi all-order application.

## Exact source claim and audit test

Use [Sra author v3](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf)
and the [author version page](https://suvrit.github.io/papers/riem-xi/).
Let D=diag(q_1,...,q_n) with q_j real; P_k is any rank-k orthogonal
projection. For normalized Haar V in U(n), set

    Z_k(x)=E exp(-x tr(D V P_k V*)), Gamma_k(x)=-(log Z_k(x))'.

Audit only the source's claimed inequality

    min_j q_j <= Gamma_(k+1)(x)-Gamma_k(x) <= max_j q_j

for every real x and k=0,...,n-1. Keep the endpoint definitions
Gamma_0=0 and Gamma_n=tr(D). The source covers repeated q_j and
does not require positive rates for this comparison. Positivity of
rates enters its later finite-exponential application, not this claim.

The load-bearing premise is LemmaC.7 for fixed identical real fields
c_r and coordinatewise ordered top rows of Haar orbital corner arrays.
It compares expectations of continuous coordinatewise increasing
functions after each law is separately weighted by exp(sum c_r S_r)
and normalized. Audit the finite-mesh one-site conditional comparison,
irreducibility and stationary coupling, continuum limit, and extension
to arbitrary real/repeated top rows. For zero/one top rows the generic
polytope's Lebesgue-density formula alone is insufficient.

The standard orbital input is imported by precise citation:
G. Olshanski, *Projections of Orbital Measures, Gelfand-Tsetlin
Polytopes, and Splines*, J. Lie Theory23(2013),1011-1022,
[publisher PDF](https://www.heldermann-verlag.de/jlt/jlt23/olshla2e.pdf),
Corollary3.2 p1017, Proposition3.1/(10) pp1015-16. Its strictly
increasing boundary hypothesis must be retained until the separate
continuity argument is checked. Do not reprove general orbital theory.

Then audit TheoremC.8's exact field matching, rate-permutation invariance,
and increasing/decreasing rate-ordering cases. An untilted nested
projection coupling, one common normalizer, or a numerical sample is
not a substitute. If a step fails, record its exact hypotheses and
scope and park that proof chain. If all pass, record a known-source
reproduction, not a new mathematical discovery.

Plausible use: the source's (C.17) controls the diagonal in the moving
basis for a finite convolution of positive exponentials. It could inform
a future comparison with a paid actual-Xi remainder. Cite this downstream
identity and its finite-reference qualification; do not derive a new
transfer or approve a new creative target during the audit. The finite
factor budget and weighted variation in C.9 remain essential. C030k's
scalar law and L030's actual logarithmic forms are different objects.

Essential local context: L030/C030b/C030k, completed discovery1202,
review884 and stops1117/1181/1193/1200/1107. These are scope comparisons,
not premises of the standalone orbital theorem. No local mathematical
lemma inputs are required for its proof. No cross-notebook import.
Full matching Mathlib coverage is unchecked. The suitable task route
is proof_audit/conceptual_audit, not creative: normalization, stochastic
comparison and singular-boundary passage require analytic scrutiny.
