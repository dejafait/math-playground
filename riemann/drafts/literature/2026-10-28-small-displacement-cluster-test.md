# Small-displacement pair mass: proposed bounded cluster test

TARGET: Test whether zero-conditioned interpolation with finite Blaschke factorization proves B_epsilon(T)<=C epsilon^alpha T(log T)^3 for some fixed alpha>0, uniformly for T>=T_0 and 0<epsilon<=1, without zero separation or simplicity.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed discovery/stronger-result and local duplicate comparison in 2026-10-28-zero-conditioned-small-displacement-coverage.md and drafts/2026-10-28-zero-conditioned-source-notes.md; no new discovery claim for this continuation.
SOURCE_EVIDENCE: de Boor (2005) Section 9 (50)--(52), pp. 62--64, https://surveys-in-approximation-theory.com/papers/2/2.pdf; Broughan II (2017) Theorem 3.3 proof (1),(4), pp. 26--27, https://api.pageplace.de/preview/DT0400.9781108195430_A31720577/preview-9781108195430_A31720577.pdf; Bettin arXiv:1111.0925v1 Theorem 1 and its reused small-shift assessment; L471 definitions/(1)--(5) and L465 Sections 1--2/5.
COMPARISON: Classical complex-node interpolation and finite factorization accommodate coalescing nodes and multiplicities. Continuous small-shift second moments are covered. The checked discrete sources assume RH or give a reflected bilinear sum; no inspected theorem supplies the positive pair-divided aggregation. This is a new proposed application mechanism, not certified originality.
GAP: Establish or obstruct a cluster-aware local-to-global estimate for the exact restricted L471 sum, with no uncontrolled microscopic occupancy, no lower displacement bound and no extra logarithmic factor.
REASON: One bounded test of actual zero constraints addresses a restricted central mass gap left untouched by the ordinary-moment and finite-law failures. The newly written ready assessment is proposed for separate approval next invocation; no mathematical application is performed in its creation.
SCOPE: The exact B_epsilon defined in the completed review, counting each conjugate nonreal pair once with its multiplicity, removing only one pair in F_j, and retaining truncated J_j(T). Use finite local factors only; no infinite-product rearrangement, RH, simplicity, separation or fixed-half-plane premise.

The main gap is unbounded-height initial-sign control and eventually
all-degree mixed positivity. This target controls only the contribution
of pairs with 0<d_j log T<=epsilon. Even a uniform power bound would
leave the complementary sector and the full little-o target in L471
unproved; it would not exclude an individual off-line zero.

Import the named interpolation and finite Blaschke statements by
citation. Work on microscopic disks with an enclosing margin, retain
the zero conditions before taking absolute values, and test whether
the other nearby zero factors can absorb arbitrary multiplicity and
clustering before summation. Convert only the resulting continuous
norms using the already assessed Bettin input, justifying gamma factors,
combined pole cancellation, disks and dyadic/truncated endpoints.
Do not assume A has a holomorphic modulus extension. The source gives
no ready summed sampling inequality; that is the substance to test.

First test alpha=3 as a candidate suggested by the existing cubic
weight, with no assertion it is attainable. Continue only on a proved
bound at scale T(log T)^3 with some fixed alpha>0 and common C,T_0.
Explicitly compare any weaker scale with this threshold. Record a
precise cluster/normalization obstruction if the method fails, or
save partial reasoning and the missing inequality if inconclusive.
A generic holomorphic counterexample refutes only the proposed tool
implication; it is not a counterexample to the actual-Xi bound or RH.

Essential local input IDs: L471 and L465; L018 supplies actual Xi and
zero symmetries if needed. L473 and the two ATTEMPTS records are
contrasts, not estimates for this sum. Multiplicity, arbitrarily close
ordinates, all epsilon and clipped boundary windows remain mandatory.
No further positive discrete-moment input is assumed. Unread adjacent
real-gap papers are not dependencies. Mathlib full matching coverage
is not checked. Failure requires a refined mechanism or new input
before repeating this test.
