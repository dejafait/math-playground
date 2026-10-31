# Shared-budget finite separation test: reviewed nomination

TARGET: Seek a certified aggregate-positive but allocation-infeasible block on the grid h,r in {j/16: 1<=j<=32} with unit displacements and unit real-zero budgets.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed joint-budget searches and local duplicate/failure comparisons in 2026-10-30-shared-budget-allocation-comparison.md; this finite grid is a subtarget of that reviewed h,r>0 family, with no changed analytic hypotheses.
SOURCE_EVIDENCE: Csordas https://arxiv.org/html/1309.0055v2 Definition 1.1/Proposition 2.2 (2.3)/Proposition 2.3; Tyaglov https://arxiv.org/html/0902.0413v3 Theorem 4.1; Katkova–Tyaglov–Vishnyakova https://arxiv.org/html/2406.00686v1 Theorem 2.2/Section 6. Direct pages and theorem statements rechecked 2026-10-30; prior proof-case comparisons retained in the completed source assessment.
COMPARISON: The signed identity identifies the aggregate expression, while the count results and single-pair L509 benchmark do not decide conserved fractional allocations. No directly matching separation example was established by the bounded search; originality is unverified.
GAP: Seek one exact rational parameter pair with H(x)>=0 for every real x!=+/-r and a rigorous contradiction to the simultaneous constant-allocation inequalities, or report an honestly bounded search failure.
REASON: This independently testable finite comparison measures possible loss of pairwise decomposition before any actual-Xi application. This literature-only recovery supplies direct source URLs and confirms the existing comparison; no mathematical invocation occurred. The finite scope remains ready as EXPLORE, subject to supervisor gate validation.
SCOPE: Exactly the grid in TARGET, h,r>0; K_c, H and all four nonnegative allocation constants with both unit-budget inequalities as defined below. No Xi realization or infinite extension.

Use the unchanged definitions in the
[completed comparison](2026-10-30-shared-budget-allocation-comparison.md):

    K_c(x)=2((x-c)^2-1)/((x-c)^2+1)^2,  c in {h,-h},
    H(x)=K_h(x)+K_{-h}(x)+1/(x+r)^2+1/(x-r)^2.

Allocation feasibility means constants alpha_c,beta_c>=0 with
alpha_h+alpha_{-h}<=1 and beta_h+beta_{-h}<=1, and both inequalities

    K_c(x)+alpha_c/(x+r)^2+beta_c/(x-r)^2 >= 0

for every real x!=+/-r. No symmetry reduction of the constants is
assumed as an already proved input. L509 is an audited isolated-pair
benchmark, not a criterion for these shifted competing pairs; L251/L257
are existing masking contrasts. L354, L471 and L508 stops remain intact.

Perform one bounded search over the stated grid, stopping at the first
fully certified separation. Numerical values can nominate parameters
but cannot certify the all-real inequality. Its certificate must cover
the complete real domain and behavior near the excluded poles and at
infinity, using exact polynomial/rational inequalities with checked
denominator signs. Infeasibility must exclude all allowed allocation
constants; a finite set of rational x tests with an exact nonnegative
linear-combination contradiction is a permitted certificate. Such a
certificate is sufficient; its existence is not assumed. Any failed
identity, missing range or incomplete infeasibility argument remains
an unresolved case rather than a proof. No new general decomposition
theorem is preapproved.

Save full certificates, tested parameter bounds and unresolved cases
under `scripts/signed-allocation/`; print only the decisive bounds,
failures and artifact paths. A search with no exact certificate is
EXPLORATION unless it yields independently justified new negative
evidence. Do not infer equivalence from absence of a grid witness or
resume an exhausted mesh search without a new mechanism.

The downstream purpose is to assess whether preserving collective
signed cancellation can outperform pairwise compensation. Actual-Xi
geometry, convergence, residual mass and all higher signs remain
unproved, so this routine finite test is not a creative central-gap
attempt or an RH candidate. Mathlib coverage is unchecked. No
mathematical script or new lemma was written during this review.

## Direct-source recovery, 30 October 2026

LITERATURE_REASON: The supervisor reported missing direct source URLs in this ready assessment; repair that essential source record without repeating the completed discovery search or changing the target.

Opened all three versioned primary URLs in SOURCE_EVIDENCE and retrieved
the named theorem statements. Csordas Proposition 2.2 requires strip
half-width one, nonzero value at zero and an interval excluding nonreal
centers for its interval sign claim; its proof equation (2.3) supplies
the signed identity. Retain the polynomial applicability argument in
the completed comparison; no global sign follows from that interval claim.
Tyaglov Theorem 4.1 bounds real zeros of the logarithmic derivative's
derivative using nonreal-zero counts of the function and its derivative.
It supplies no allocation constants. Katkova–Tyaglov–Vishnyakova Theorem
2.2 requires simple real zeros and exclusively real simple derivative
zeros; those derivative hypotheses remain unverified for the nominated
family. It likewise supplies no budget decomposition.

The earlier retrieved proof cases, duplicate checks, recorded L354/L471
failures and Cardon/Tyaglov–Atia comparison are reused from
[the completed comparison](2026-10-30-shared-budget-allocation-comparison.md).
No source change or new overlap was established. This is a process repair,
not an informative mathematical negative or a novelty claim. No lemma,
script, grid test, symmetry reduction or new specialization was produced.
Mathlib coverage remains unchecked.
