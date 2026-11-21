# Fixed-quadratic differential range screen — nomination2029

TARGET: Test whether C029n's full U_6 admits U_6=(t^2+1/4)h'+2alpha*t*h for any alpha>=0 and real quintic h, certifying all parameter cases without changing the quadratic or degree.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Discovery2029 compares differential range and basis-diagonal preservation, checks relevant local stops and searches actual-family operator statements; no matching inverse-range result was located. drafts/literature/2026-11-20-post-residue-independent-discovery-2028.md
SOURCE_EVIDENCE: Bunton et al., arXiv:1312.2283v2, 22 December2013, Theorems7-8 and complete proofs, manuscript pp3-4, https://arxiv.org/pdf/1312.2283v2 ; Kuznetsov, CMB51(2008), (2)/(4)/(6)/(9)/(13), pp563-564/566, https://doi.org/10.4153/CMB-2008-055-0 ; reuse C029n's audited finite coefficients/enclosures.
COMPARISON: The forward zero-count theorem is known; its inverse polynomial range condition for this U_6 is not supplied by inspected sources. The quadratic is fixed from the source normalization, independently of numerator roots; no residue signs or inter-degree PSD increment enters.
GAP: Existence of a compatible nonnegative parameter and quintic is unknown. Even existence would leave preimage hyperbolicity and eventual family control unproved.
REASON: One finite coefficient-compatibility test can reject a specific representation mechanism without another isolated root count or precision campaign. This is known-method specialization, not certified originality.
SCOPE: Newly written ready nomination requiring separate next-turn approval. N=6, q=t^2+1/4, alpha>=0 only; no coefficient elimination or mathematical derivation performed in this literature turn.

## Exact proposed test

Use U_6=T_6/S, S=sin(pi/8)/sqrt(2)>0, with every odd/even coefficient
as in C029n. Fix q(t)=t^2+1/4. Seek alpha>=0 and a real polynomial h
of degree exactly five such that

    U_6(t)=q(t)h'(t)+alpha q'(t)h(t).

Do not fit q to roots, discard odd terms, reweight the family or use
the auxiliary u_n expansion instead. Alpha=0 is included. No root
simplicity or hyperbolicity of h is assumed in this range screen.

The cited source theorem is relevant to a prospective one-pair route
only after verifying its hypotheses and controlling preimage zeros.
Its finite application and any Hermite interpretation must be justified
later; this review establishes neither. Do not reprove the general
theorem. The occurrence of the quadratic in a multiplication identity
is motivation only, with no assumed differential identity.

## One bounded attempt

Make one analytic coefficient-elimination attempt for this operator
and degree. Derive compatibility rather than assuming a triangular
solve is onto. Cover zero denominators and every alpha>=0, including
zero and the unbounded tail. Sampling parameters is insufficient.
An analytic necessary-condition proof is allowed if it tests this
same identity and covers the full parameter domain.

Reuse C029n's exact formulas and unchanged proved 60-decimal rational
pi/sqrt(2) bounds. No precision increase, new degree or shifted
quadratic. Interval inclusion must respect repeated coefficient
parameters; zero-containing enclosures remain unresolved. An integer-
coefficient Sturm implementation is not automatically applicable
to pi-dependent coefficients.

A pass requires an exact compatible parameter and polynomial identity,
not a numerical residual. A negative result must exclude every
alpha>=0. Otherwise preserve the compatibility equations and unpaid
sign conditions as an inconclusive attempt, without enlarging scope.
If a script is useful after approval, save full certificates under
scripts/pollaczek/, print actual/required bounds and failures, and
inspect complete load-bearing values. No script is required.

## Downstream use and limits

A pass may motivate a separately assessed preimage hyperbolicity test;
it proves no hyperbolicity, uniform law or RH conclusion. A failure
parks this fixed-quadratic baseline, not every differential mechanism
or an eventual-only conjecture. Reopening needs new family-specific
structure rather than another isolated degree.

Essential inputs: C029m's exact family/conditional context; C029n's
finite normalization, coefficients and rational enclosures; cited
Theorem8. C029p/q/r are contrasts only. Actual-degree/singular cases,
preimage hyperbolicity, eventual uniformity, initialization and
qualified weighted convergence/upstream[9] remain open. No cross-
notebook input. Matching Mathlib coverage unchecked. Proposed work:
REPRODUCTION/calculation; separate approval must precede mathematics.
