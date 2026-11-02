# Primitive diagonal family: bounded boundary-tail specialization

TARGET: Justify the primitive-pair regrouping of L233's first associated kernel and determine the eventual Fourier sign of its full diagonal (1,1) family.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-object, stronger-result and local failure comparison in 2026-10-31-primitive-theta-block-source-scope.md; the same reflected half-axis modes and first-spectrum hypotheses apply. No inspected source decides the full diagonal family; no novelty claim.
SOURCE_EVIDENCE: Durrett, Probability: Theory and Examples, author version 5 (11 January 2019), https://math.duke.edu/~rtd/PTE/PTE5_011119.pdf, Theorem 1.7.2/proof pp.38-40 and counting-measure corollary p.41; Csordas, https://arxiv.org/pdf/1309.0055v2, Definition 1.2 p.2 and Theorems 4.5-4.6/Open Problem 4.7 pp.11-12. Direct sources reopened 2026-10-31. Reuse L019/L233/L234 and L356, especially (1) and (6)-(8), as assessed in the parent review.
COMPARISON: The standard Fubini tools and existing infinite parity-block boundary method cover the technique. The identified difference is restriction to primitive positive index pairs and, first, all self-pairs n=m rather than a product of two summed parity kernels. No new representation or sign has been derived in nominating this continuation.
GAP: Prove legitimate regrouping and summable diagonal Fourier remainders, retaining every mode and the full reflected boundaries; then determine the eventual diagonal-family sign. No full-spectrum, off-diagonal or higher-degree sign follows.
REASON: A concrete mathematical discriminator is available without more source browsing. This newly written continuation receives separate approval next turn; no calculation or proof was performed in its source-review turn.
SCOPE: Actual L019 half-axis modes reflected individually as k_n(u)=K_n(|u|); unordered a<=b with gcd(a,b)=1, common multiplier d>=1, both orientations (da,db)/(db,da) for a<b and only (d,d) for a=b=1. Use L233's first associated kernel and Fourier convention. No regulator, auxiliary Jacobi derivative, whole-line unreflected summation or cross-notebook input.

## Purpose and bounded test

Actual-Xi all-degree signs at unbounded heights remain the main gap.
The intermediate sufficient mechanism is separate spectral positivity
of complete primitive families. First certify that the proposed
partition is legitimate and test the full diagonal family. If its
spectrum has a rigorously negative value or eventual tail, stop that
separate-positivity mechanism. This would not determine the sign of
the total, where cross-family cancellations can matter.

Use the spatial double-series expansion already present in L356 and
retain its integrable moment majorants. Invoke the nonnegative or
absolutely integrable cases of Fubini with their actual hypotheses.
Every n=m=d term belongs once to the diagonal; unordered off-diagonal
pairs retain two ordered orientations. These are object definitions
to implement and justify, not an identity proved by this assessment.

The Fourier-tail test must establish bounds uniform enough in the
mode index to sum all relevant derivative/boundary remainders. L234's
fixed-N error term cannot simply be summed. L356's envelope is a
ready tool, not a precomputed diagonal coefficient. Derivatives of
Fourier transforms must come from dominated differentiation of the
original integrals, rather than differentiation of a big-O term.

A nonnegative eventual tail leaves every finite frequency and all
off-diagonal families unresolved, so it justifies only a further
independently specified test. Failure of the required summability
must be reported as inconclusive. No numerical preview can decide
the infinite-family claim. Save any incomplete bounds and do not
repeat an unsuccessful test without refined input.

## Reuse, classification and limits

Full citations, queries, source versions and failure comparison are
in the completed parent assessment. The nearest local results are
L234's finite cusp stop, L235's modular-average mass stop and L356's
complete parity cancellation. They are contrasts and technique
inputs with the stated hypotheses; none is an actual-Xi sign premise.
The normalized quotient jet and L600/L601 profile obstructions
provide no global primitive-family factorization.

The intended work is REPRODUCTION: a bounded specialization of an
existing analytic method, not a protected creative attempt. An
affirmative inter-family compensation mechanism remains uncovered.
Mathlib coverage for the full diagonal result is not checked; no
absence is claimed. No lemma or mathematical script accompanies
this assessment. Any later established result belongs in its own
canonical lemma with hypotheses, proof, qualifications and Mathlib.


## Direct-source recovery — 31 October 2026

LITERATURE_REASON: Supervisor required a direct source URL in this ready assessment; repair source traceability without repeating discovery or changing the mathematical target.

Reopened both primary PDFs linked in SOURCE_EVIDENCE. Durrett's version
and date match the parent review. Rechecked Theorem 1.7.2, its proof
cases 1–4 (indicators, simple functions, nonnegative monotone limits,
and integrable signed functions), and the counting-measure corollary.
The product spaces are sigma-finite; measurable nonnegative functions
permit Tonelli, whereas signed integrands require absolute integrability.
Counting measure on a countable index set and Lebesgue measure meet the
space hypotheses. Complex Fourier factors require the signed theorem
on their real and imaginary parts. This imports the known theorem;
it does not verify the proposed family's required majorants.

Rechecked Csordas v2 Definition 1.2 and Theorems 4.5–4.6 through Open
Problem 4.7. Admissibility requires smoothness, evenness, positivity,
strict decrease on the positive half-line and the specified derivative
decay. Theorem 4.5 asserts admissibility of the full associated kernels,
not their positive definiteness. Theorem 4.6 identifies all associated
positive-definiteness conditions with the real-zero criterion. Open
Problem 4.7 asks for the first Laguerre sign in that 2014 source; no
current-status conclusion follows. No individual reflected mode or
primitive family is certified admissible or spectrally positive by
these statements. L233 retains the local Fourier normalization.

The parent assessment's exact-object searches, duplicate comparison
and failure record remain applicable and were reused. Revisited L233's
moment/Fubini proof and L356's envelope (1) and Fourier argument (6)–(8)
for scope only; no new specialization or independent audit is claimed.
The saved SPECIALIZE decision and exact TARGET are retained. This is
a metadata/source-traceability repair, not mathematical progress or a
new search outcome. No lemmas, mathematical scripts, DAG or argument
were changed. Full-result Mathlib coverage remains not checked.
