# Conditional audit of the prime-activation comparison

TARGET: Audit bramble_trace v1 Theorem 2.4's one-prime activation comparison conditional on its trace and collar-resolvent inputs, checking the complete complementary elimination at scale delta/log(1/delta).
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The completed support-enlargement comparison searched compact-window criteria, endpoint traces, renewal and vanishing eigenvalues; its exact primary match is bramble_trace paper 67 v1 Theorem 2.4 and Section 8. Narrow local endpoint-trace/support-variation/renewal searches found no duplicate audit; earlier theta-boundary and heat-energy failures concern different operators. This target is reproduction of a source calculation, not a novelty claim.
SOURCE_EVIDENCE: bramble_trace, Boundary traces and support variation for localized Weil operators, paper 67 v1 (27 October 2026), Theorem 2.4, Sections 3.3–5 and 8, equations (3.19), (4.5), (4.7), (5.1)–(5.4), (8.1)–(8.8), inspected in the primary manuscript at https://rstation.ai/problems/riemann_hypothesis/papers/67/v1; Section 9 explicitly leaves arithmetic positivity propagation open.
COMPARISON: The source already states and proves the signed activation asymptotic for a fixed simple eigenvalue of the full operator. The audit reproduces its smaller-scale complementary elimination and branch comparison, conditional on the named analytic inputs; it does not invent the law, improve its remainder or assume enlarged-window positivity.
GAP: Independently verify uniform little-o(delta/log(1/delta)) for every eliminated complementary mode and the derivative/root comparison. Do not replace strong collar convergence by norm convergence or little-o by a scalar-gap big-O bound. Existence/normalization of traces and the underlying renewal/regularity theorems remain independent source audits.
REASON: A reproof is justified as a critical check of the load-bearing full-complement argument before this recently found source law is used locally. Its fixed-cluster little-o is the precise fragile point; the original source and all conditional hypotheses are now available. This ready continuation is newly written and requires the supervisor's separate approval next turn.
SCOPE: Conditional conceptual audit of Section 8 for fixed prime power n, fixed a=log(n)/2 and a fixed isolated simple eigenvalue; accept the stated domain, boundary traces and collar inverse/response limits as explicit external hypotheses. No numerical certificate, generic all-support theorem, multiple-branch extension or effective onset is covered.

Primary source: [bramble_trace, paper 67 v1](https://rstation.ai/problems/riemann_hypothesis/papers/67/v1).
The source comparison and obstruction evidence are in
[the completed assessment](2026-10-30-weil-support-enlargement-coverage.md).

The mathematical audit starts from the full zero-extension geometric
Weil operator A_a in source (2.1)/(3.5), with its common finite real
even signed measure on a fixed compact radius range. Retain all prime
powers and the signed pole. Take a prime power n, a=log(n)/2,
w=Lambda(n)/sqrt(n), and an L2-normalized simple eigenfunction u of
parity p in {+1,-1}. Neither positivity of its eigenvalue nor positivity
of the larger interval is assumed. The nearby full/deleted branches
live on radius a+delta/2 and delete only the atoms at +-log(n).
The proposed imported conclusion is exactly source (2.9), including
its coefficient -2wp|tau_+(u)|^2 and its little-o remainder. A zero
trace is allowed; the claim then asserts a smaller-order difference.

Treat source (3.19), (4.5), (4.7) and the fixed old complementary
spectral gap as retained hypotheses, not as independently proved
local facts. The strong inverse limit is only asserted on fixed
vectors, uniformly on compact z sets. Check its use on the converging
response vectors and the passage from (5.3) to the exact full
Feshbach expression (5.4). Section 8.1's compact reduced resolvent
must improve the complementary contribution to little-o at the
activation scale uniformly in z. Section 8.2 then compares the two
exact scalar functions and their roots, retaining all source terms.
No unproved infinite sum of squared endpoint traces is permitted.

Main gap: actual-Xi all-degree positivity. The intermediate result is
a reliable conditional one-atom response law. Its downstream use is
to identify which parity and low-mode inverse response need an
arithmetic bound in a later support-extension attempt. Uniformity
near a first zero, effective finite collar widths, multiple ground
clusters, all-support positivity and the full analytic input audits
remain unresolved. The known scalar-shifted pure-log comparison in
source Section 9 rules out inferring them from regularity alone.

Continuation test: accept the conditional law only if all omitted
modes cost little-o at the stated scale and the two scalar roots are
compared on their common fixed gap. An O bound at that scale,
unjustified derivative of a remainder, missing atom or hidden
finite-dimensional substitution requires a qualified import or a
recorded failure, not an unconditional theorem. One audit attempt;
no certificate replay or original arithmetic estimate in its scope.

No local lemma input is essential to this conditional audit. L471 and
L511 remain historical contrasts only and need not be reread. No
cross-notebook result is used. Matching Mathlib coverage is unchecked;
supporting spectral/compactness theorems do not certify the entire law.
