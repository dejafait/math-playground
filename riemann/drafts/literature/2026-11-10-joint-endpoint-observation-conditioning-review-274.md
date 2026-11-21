# Joint exact endpoint observations: completed source comparison

TARGET: Review polynomial conditioning of the joint exact observations with rows a_n/||a_n||_2, b_n/||b_n||_2 and c_n, including all cofinite indices.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step275 completed the bounded external exact-statement, deterministic-evaluation, simultaneous-small-value and near-collision searches recorded below, together with narrow November10 local overlap/failure checks. No inspected theorem states (T); this is not a novelty finding.
SOURCE_EVIDENCE: Reuse L990(5),(13), C990a(1),(12)-(16) and their audited GST1709.09656v1 section3.3 equations81-87/GST1609.00829v1 section2.1.3 equations20-25/DLMF10.17(iii) contracts. Newly read: Chretien-Darses, Proc.AMS143(2015),4383-4388, Theorem3.1 and proof pp4384-4385, https://www.i2m.univ-amu.fr/perso/sebastien.darses/PAMS.pdf; Fukshansky, Spring2015 Transcendental Number Theory notes, section4 equation13 and Theorem4.4/proof pp25-26, https://www1.cmc.edu/pages/faculty/lenny/classes/spring_2015/m195/m195_lectures.pdf; Bindel, CS6210 lecture25August2025, The SVD and the 2-norm, https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-08-25.html.
COMPARISON: Bulk asymptotics, exact noncollinearity and standard finite-dimensional conditioning tools cover ingredients, not the polynomial bound. Single-polynomial zero spacing and homogeneous algebraic approximation do not control the exact corrected endpoint-row angle. The remaining specialization is a quantitative robustness argument through collision neighborhoods.
GAP: Prove a uniform polynomial lower singular-value bound at every sufficiently large integer, or supply a rigorous obstruction; no exponent or lower bound is obtained here. The additional arithmetic outputs and all main-goal transfer gaps remain unproved.
REASON: Essential source comparison is now complete for one bounded exact-row specialization attempt; no source blocker requires another search. The proposed robustness extension of C990a must be proved separately, with no inference from qualitative invertibility, leading phases or a finite sample.
LITERATURE_REASON: The new joint-observation hypotheses and quantitative lower-bound target lie outside review272 and review267; reuse the existing GST contracts but compare the exact new statement before research.
SCOPE: Review only the exact integer rows from L990 and their joint matrix below. Retain all sufficiently large indices and the constant subtractions; no leading-phase replacement, generic random-matrix conclusion or arithmetic estimate is preapproved.

## Step274 nomination retained, with no result claimed

The following nomination describes coverage at step274. Its statements
that the source comparison is missing are superseded by the step275
completion below; its mathematical target and limitations are retained.

For the exact a_n,b_n,c_n of L990 put

    a_hat_n=a_n/||a_n||_2, b_hat_n=b_n/||b_n||_2,
    J_n=[a_hat_n; b_hat_n; c_n].

Rows are written in brackets, so J_n is a real 3-by-3 matrix acting
on a three-coordinate column vector. L990 and C990a ensure that
these rows are defined for every n beyond one fixed existential onset.
Do not assume a computed onset or a quantitative cross-product bound.

The proposed bounded mathematical target for a later turn is whether
there exist C>0, A>=0 and N<infinity such that

    ||J_n v||_2 >= C*n^(-A)*||v||_2
    for every integer n>=N and every v in R^3.                 (T)

Only source comparison for (T) is nominated now. Do not infer (T)
from pointwise invertibility, compactness of the leading phase torus,
or C990a's qualitative onset. Its collision set is nonempty.
The concrete lead is C990a's second-order phases and noninteger
limit 169/pi^2 in its exact-collinearity contradiction. Whether that
argument controls near collinearity uniformly is unproved; the present
step does not extend it. A polynomial bound is sufficient for the
intended recovery certificate, not asserted necessary for every
subexponential recovery method.

Main gap: actual-Xi positivity L030-L032/C032a and signed forcing
L966/L968. A bound (T) could supply a local recovery mechanism for
X_n=(B_n,B_(n+1),B_(n+2)) if all three outputs J_n X_n can separately
be bounded at the needed scale. The two additional outputs have no
such arithmetic bounds. Common-interval identification, shifted
intervals, every prime power, other zeros, both complements and the
link to L984(H) also remain open. No RH implication is claimed.

## Recovery comparison and decision test

Three mechanisms were compared only to select a continuation:

1. Removing L992's cutoff would require new exact logarithmic-tail
   and individual-nonzero control; a zero determinant rate would still
   leave directional growth unanswered. No new such control is ready.
2. Continuing working271's fixed anchor would require infinite
   compatibility and uniform upper/lower growth. L991 stops the bounded
   fixed-pivot shortcut; enlarging the existing horizon is not new input.
3. Joint observations test pointwise quantitative information in three
   exact rows, without constructing a homogeneous infinite recurrence.
   Select this independent gap. Additional observations change the
   hypothesis; this is not a solution of the original scalar implication.

Preserve stops270/272 and working271. A later research test should seek
one uniform all-index bound (T), including collision neighborhoods, or
a rigorous obstruction to every polynomial bound. A finite sample, a
bound outside fixed neighborhoods, or failure to prove (T) decides
neither alternative. A negative result for polynomial conditioning
would not itself disprove a weaker subexponential recovery estimate.
First review the exact statement, stronger relevant known bounds and
known near-collision obstructions; import any matching theorem with
its full hypotheses instead of reproving it. Unread exact-source leads
remain unread, and this assessment does not approve mathematics.

Essential local inputs to assess are L990 and C990a. L991, L992 and
working271 are contrasts only; L984 is downstream context. No cross-
notebook input is proposed. Full matching Mathlib coverage is unchecked.
No independently justified signed arithmetic mechanism is ready for
central creative routing. Do not classify this source comparison or a
routine conditioning specialization as creative to meet a preference.

## Completed comparison — step275, 10 November 2026

This is one literature-only step for the saved TARGET. No new
mathematics, lemma, mathematical script or numerical test was produced.
The main gap remains actual-Xi positivity L030-L032/C032a and signed
forcing L966/L968. The intermediate target is exactly (T), with the
downstream use and independent arithmetic obligations stated above.

### Existing coverage, duplicates and failed shortcuts

Read L990 through its exact row definitions, bulk scaling and collision
description, and C990a's complete cofinite-definition proof. Reuse their
audited fixed-alpha compact-bulk GST and Bessel contracts; no refresh
of those unchanged hypotheses is needed. C990a supplies a uniform
additive O(n^-2) error for the middle-degree endpoint phases, but its
integer-limit contradiction assumes exact collinearity. It explicitly
does not claim a normalized cross-product lower bound.

The scoped November10 endpoint assessments and failure searches found
no completed quantitative joint-row estimate. Review258's inspected
Duran fixed-coefficient exterior asymptotics and Krattenthaler
Christoffel determinant identity do not provide this bound: the former
excludes the bulk and the latter is an identity without the required
lower bound. Reuse that comparison, not a new orthogonality assumption.
Source-notes268's Poincare-Perron/Bohl-Perron and analytic-cocycle
comparisons concern different evolution questions and cannot supply
all-index conditioning of this exact finite matrix. Stop274 preserves
the scalar fixed-anchor, pivot and cutoff failures; it does not ban
the independent simultaneous-observation test. No sibling proof or
cross-notebook result was read. Unfinished work271 is preserved.

### Newly inspected primary statements

S. Chretien and S. Darses, *On the spacings between the successive
zeros of the Laguerre polynomials*, Proc. AMS143(2015),4383-4388,
DOI10.1090/proc/12574, [author-hosted published PDF, Theorem3.1 and
proof, pp4384-4385](https://www.i2m.univ-amu.fr/perso/sebastien.darses/PAMS.pdf#page=2).
For alpha>-1 and all adjacent zeros of the single degree-n polynomial,
the spacing is at least sqrt(3)*(alpha+1)/sqrt(n*(n+alpha+1)).
Read the full theorem and both proof regimes, including its additional
alpha>=n/C hypothesis for the large-parameter bound. The proof uses
the Bethe-ansatz identity and a bound for its ODE coefficient on the
interval containing the zeros. It controls distances between zeros,
not distances of the prescribed nodes n,2n from zeros, nor angles of
two three-coordinate rows of shifted polynomials. Our fixed alpha=2
meets the basic hypothesis but does not remove that difference. No
specialized estimate from this theorem is derived or imported as (T).

L. Fukshansky, *Transcendental Number Theory*, Spring2015 lecture
notes, [section4, equation13 and Theorem4.4 with proof, printed
pp25-26](https://www1.cmc.edu/pages/faculty/lenny/classes/spring_2015/m195/m195_lectures.pdf#page=25).
For real algebraic alpha of degree d>=2, Liouville's theorem gives
|alpha-p/q|>=C(alpha)/q^d for all rationals p/q with q>0. Equation13
states the degree-two badly-approximable case. Read the proof's
nonzero-integer step and local polynomial comparison. These are
homogeneous approximation bounds with fixed algebraic target, not a
bound for the present phases with their specified offsets and 1/n
corrections. No algebraicity or Diophantine property of the full
frequencies is established. C990a already uses a more tailored integer
quadratic expression and a noninteger limiting constant. Robustness
under an approximate row relation remains the unproved specialization;
neither this theorem nor pi's irrationality alone supplies it. We use
the named theorem, not a printed effective derivative constant.

D. Bindel, *CS6210: Matrix Computations*, [lecture of25August2025,
section The SVD and the 2-norm](https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-08-25.html#the-svd-and-the-2-norm).
Read the SVD conventions and complete final section. For a square
invertible matrix the inverse spectral norm is the reciprocal of its
smallest singular value; that singular value also measures the
spectral-norm distance to singular matrices. These standard statements
may be cited for finite-dimensional conditioning. They give no
index-dependent distance bound for J_n. A later proof must establish
that missing bound before invoking an inverse estimate. No explicit
Gram eigenvalues or new J_n formula is calculated here.

### Search and access record

Queries actually used, in bounded batches:

```text
Laguerre polynomials consecutive degrees evaluations smallest singular value conditioning bulk asymptotic
Laguerre polynomials simultaneous small values rational arguments lower bounds near common zeros
Gil Segura Temme Laguerre 1609.00829 1709.09656 uniform asymptotic expansions zeros
"Laguerre" "evaluation matrix" condition number deterministic
"Laguerre" "simultaneous" "lower bound" polynomials
"orthogonal polynomials" "smallest singular value" deterministic evaluation
"Laguerre" "conditioning" "deterministic" polynomial matrix
"Laguerre" "near" "common zeros" quantitative
"quadratic irrational" "badly approximable" theorem lecture notes pdf
"matrix" "smallest singular value" "Gram matrix" Boyd Vandenberghe appendix
Chretien Darses "Laguerre" "spacings" arxiv
"Laguerre polynomials" "evaluation" "condition number"
"Laguerre" "small values" polynomials rational
"Laguerre" "endpoint-null" "conditioning"
"Laguerre" "near-collinearity"
"Laguerre" "joint" "polynomial conditioning"
```

No matching deterministic theorem was found among the inspected
results. Search-result leads on random Wishart conditioning,
pseudospectral differentiation, irreducibility and interlacing were
not assessed at theorem level and supply no evidence for or against
(T). They are unread leads, not required inputs for the selected direct
robustness test. Search snippets and secondary reposts were not used as
theorems. The selected primary statements and relevant proof cases were
accessible in parsed text; one Fukshansky p26 screenshot request timed
out, then the complete selected proof text was retrieved. No persistent
source blocker is asserted. Full matching Mathlib coverage is unchecked.

### Decision and bounded continuation

SPECIALIZE for one later attempt on (T). Sources cover the uniform
asymptotic and linear-algebra ingredients; the exact quantitative
near-collision difference is still unproved. A reproof of GST, the
generic SVD facts or qualitative C990a nonvanishing would add no needed
input. What would be useful is an error-controlled extension of C990a's
exact recurrence/phase contradiction to nearly parallel rows, followed
by a cited finite-dimensional singular-value argument. This is a
proposed test, not a derivation or an approved conclusion.

Require C>0, finite A>=0 and one N valid for every integer n>=N and
every v in R^3. All constant subtractions, endpoint row scales and
collision neighborhoods must be retained. Continue only with a proved
bound or a specific informative obstruction. Failure to obtain a
polynomial bound is inconclusive; refutation requires rigorous evidence
against every such C,A,N and would still not refute all subexponential
recovery. Fixed neighborhoods and finite samples do not meet the test.

The exact mathematical continuation is nominated in review275 for
separate next-turn approval. No genuinely new signed arithmetic
mechanism is justified here; that is the blocker to central creative
routing, not a reason to relabel this specialization creative. No
progress beyond checked sources or toward RH itself is claimed.
