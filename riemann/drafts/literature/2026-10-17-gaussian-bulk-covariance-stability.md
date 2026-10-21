# Source review: covariance sensitivity of the exact bulk test

TARGET: Prove or refute an o(1) change in L424's bulk transport observable when only L423's full covariance correction A_H is removed.
CHECKED: 2026-10-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 178 searched Schur--Horn continuity and fixed selections, equal-diagonal Givens algorithms, positive-matrix square-root perturbation, semialgebraic branch regularity and exponential-polynomial sublevel bounds; inspected the primary statements and relevant two-dimensional proof cases listed below and checked the scoped local failures.
SOURCE_EVIDENCE: Chen--Li arXiv:2407.00701v2 (2026-01-04), Definition 1.2, Theorem 1.3, Corollary 1.4 and Lemma 2.1/Table 1; Carlsson arXiv:1810.01464v1, (1.2), Theorem 2.1/(2.2), pp. 1--3; reused Carlen--Lieb arXiv:0904.0734v2, Horn theorem/(1.1)--(1.2), pp. 1--2; Friedland--Yomdin, Studia Math. 218 (2013), Theorems 1.1/1.3 and Section 2 proof, as a scope comparison only.
COMPARISON: Known results control positive square roots and nearby admissible Schur--Horn representatives, not the basis prescribed by L419 or its nonlinear Q average. The two-dimensional rotation proof explicitly permits a non-small rotation at a degenerate tie; sublevel results require an identified function and nondegeneracy not yet checked here.
GAP: Prove stability of the selected Q sum across persistent ties, or control the actual-height measure of their neighborhoods together with the strict-branch perturbation error; no source inspected establishes |B_H-B_H^0|=o(1) for the actual correction.
REASON: The bounded source comparison supplies no direct import or actual-response obstruction. It justifies one branch-specific analytic test under the unchanged target, with an explicit stop condition; no novelty or mathematical result is claimed.
SCOPE: Exactly the covariance-removal target below, with L423's fixed mixture and actual response, w, g_H, J, curvature and dt/H marginal, and L419's complete first-index strict/equality selection. Local branch analysis and rigorously controlled auxiliary formulas are covered; replacing the basis, phase law or finite-H correction without proof is not.
COVERED_TARGET: Prove or refute an o(1) change in L424's bulk transport observable when only L423's full covariance correction A_H is removed.

## Exact proposed target and input scope

Use L424's audited Q, E, ell, B_H and V_i, L423's actual g_H,w,J,A_H,
and L419's exact deterministic coordinate-basis rule, including ties.
Define the comparison observable by replacing only Sigma with
Sigma_0=ell g_H K, taking its positive square root S_0, and applying
the same rule to S_0 J S_0 to obtain u_i^0. Put

    V_i^0=sqrt(3/ell) S_0 u_i^0,
    B_H^0=E[(w/3) sum_i Q(V_i^0)].

The requested threshold is |B_H-B_H^0|=o(1) as real H tends to
infinity. No assertion is made that the comparison states retain the
selected moment constraints; B_H^0 is only a proposed comparison
integral. Keep the complete response derivatives, curvature, moving
normalization, high/intermediate definitions and height marginal. Do
not replace g_H, w or J by a phase average or a limiting surrogate.

## Why this is an independently testable continuation

L424 already controls the high/intermediate contributions and the
translation. Removing A_H in the remaining observable, if justified,
could reduce one obstacle to later actual-height averaging. That later
averaging and a nonzero bulk defect remain separate unproved tasks;
neither is included in this proposed target.

The specific proposed mechanism is to separate heights near the finite
algebraic branch loci of L419's coordinate rule from heights where the
same strict branch is stable, with an error budget tending to zero.
No branch-locus measure estimate, continuity claim, rate or limiting
distribution has been proved or approved here. Check primary results
on measurable matrix selections and quantitative branch stability, and
whether actual response information suffices for the required exceptional
height control. A generic selection theorem need not cover this fixed
selection algorithm; smoothness of the positive matrix square root alone
does not do so.

The recorded step-175 failure in
`ATTEMPTS/2026-10-17-gaussian-jet-trajectory-diagnostic.md` remains active:
more floating phase samples cannot establish stability or sign B_H.
Continue only with a justified o(1) comparison or a concrete obstruction
under the exact target hypotheses; failure of a generic matrix example
alone must not be reported as failure for the actual response. Park this
comparison if source review supplies no justified discriminating test.
No new lemma or mathematical calculation is contained in this review.
Full matching Mathlib coverage is not checked.

## Step 178: inspected sources and their limits

This is a LITERATURE / NOVELTY_UNCHECKED / literature_comparison step.
Its outcome is EXPLORATION: the exact target remains unanswered. The
assessment now permits a bounded mathematical attempt; completion of a
literature gate does not reset the mathematical exploration count.
LITERATURE_REASON: The covariance-removal target was outside the ready
step-176 audit scope and explicitly REVIEW_REQUIRED at invocation start.

The main gap is still actual-theta global mixed positivity. This
intermediate target concerns only the transport diagnostic of the
selected-moment counterlaw. Its plausible downstream use is simplifying
the exact bulk integral before a separate actual-height average. A
nonzero bulk defect, actual capped nondegeneracy, negative-Bcal clipping
and L413's full-error regulator margin remain independent gaps.

### Positive square root: covered smooth operation

Marcus Carlsson, *Perturbation theory for the matrix square root and
matrix modulus*, [arXiv:1810.01464v1](https://arxiv.org/pdf/1810.01464v1),
2018-10-02, (1.2), Theorem 2.1/(2.2), pp. 1--3. Read the nonsingular
square-root formula, full theorem and the following remainder discussion.
For Hermitian A=U diag(alpha) U*, f C^2 near its spectrum, and sufficiently
small Hermitian E, the linear term is the divided-difference matrix
of f at alpha, entrywise multiplied by U*EU and conjugated by U; the
remainder is O(||E||^2), locally uniformly in A. For positive definite
A and f(s)=sqrt(s), the divided difference is
1/(sqrt(alpha_i)+sqrt(alpha_j)), including repeated eigenvalues.
The source explicitly distinguishes the singular case.

The applicability interface is the already established compact positive
spectral range of Sigma/ell and Sigma_0/ell in L423, not a claim that
A_H itself tends to zero. This covers the matrix square-root operation
after normalization. It says nothing about the subsequent fixed basis
selection. Import this standard input by citation in any later proof;
no reproof or singular-matrix extension is needed.

### Schur--Horn continuity: a different object from the prescribed basis

Hengzhun Chen and Yingzhou Li, *On the continuity of Schur-Horn mapping*,
[arXiv:2407.00701v2](https://arxiv.org/html/2407.00701v2), 2026-01-04.
The initial search retrieved v1 and the author's v1 PDF; checked the
latest version before deciding coverage. PDF numbering is Definition
1.2, Theorem 1.3, Corollary 1.4 and Lemma 2.1/Table 1; HTML numbers
these 2, 3, 4 and 7. Read the definitions, theorem, corollary proof,
all four two-dimensional cases and the real symmetric assembly in
Section 4; the updated scope discussion after Corollary 1.4 was inspected.

For a real symmetric A with fixed diagonal d, an O(epsilon) eigenvalue
perturbation satisfying the stated majorization admits a matrix with
that same diagonal within O(sqrt(epsilon)) in Frobenius norm. The
corollary concerns Hausdorff distance between the admissible classes.
Lemma 2.1 assumes its explicit nonnegative discriminant; with zero
off-diagonal, equal target diagonals and perturbation orders alpha<=beta,
the rotation can have order-one angle although the rotated matrix is
close. These are local, fixed-base asymptotics.

This does not select L419's first coordinate/pair, quadratic root or
complement order. Nor does a nearby equal-diagonal matrix control
the physical vectors S u_i in Q. Thus the result cannot be substituted
for stability of this particular observable. Its degenerate case is a
warning about an inference, not a counterexample to the actual target.
The general existence input remains Carlen--Lieb's
[arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2), Horn theorem
after (1.1), proof through (1.2), pp. 1--2, reused from step 169.

### Sublevel machinery: conditional tool, not actual-height coverage

Omer Friedland and Yosef Yomdin, *An observation on the Turan--Nazarov
inequality*, Studia Math. 218 (2013), 27--40,
[publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/89801),
DOI 10.4064/sm218-1-2. Read Theorem 1.1, Definition 1.2, Theorem 1.3,
and its Section 2 proof; the earlier arXiv text numbers the latter
theorem 1.2. The quoted classical theorem bounds the supremum of
p(t)=sum_(k=0)^m c_k exp(lambda_k t) on an interval B by its supremum
on a measurable positive-measure subset Omega, multiplied by
exp(|B| max |Re lambda_k|)(C|B|/|Omega|)^m. Their refinement replaces
measure by a diagram-dependent metric span and requires that span to
be positive. The proof uses the actual sublevel set and a bound on
its components; arbitrary floating samples do not furnish these data.

This is only a comparison source here. No branch comparison has yet
been reduced to such a fixed exponential polynomial with a uniform
nonzero norm. In particular the complete gamma/zeta response is not
asserted to be a finite exponential polynomial in height. No bound
from this source is imported into the argument. The original Nazarov
paper was located on the author's publication page, but its TeX fetch
was unsupported by the web tool and a shell fetch failed DNS; its proof
is unread. This optional lead is not essential to the test below.

Coste's semialgebraic notes were found, but the attempted author/mirror
PDFs were inaccessible; no theorem from them is asserted or used.
A generic stratification statement would still require checking its
restriction to the actual response. These optional access failures do
not block elementary analysis of the explicit three-dimensional rule.

## Duplicate/failure comparison and bounded continuation

The local check used L419's entire coordinate implementation (strict
pair, equality-first branch, complementary two-dimensional rotation,
and all index ties), L423 (5), (9)--(11) and its step-172 audit, and
L424 (1)--(7) with its step-177 audit. Scoped searches in October
15--17 assessments/attempts and October-17 histories found the proposal
but no completed covariance-stability proof. Existing moment and
selection assessments cover existence/calibration, not this replacement.
This is a scoped duplicate check, not evidence of novelty.

Preserve the step-175 failure in
`ATTEMPTS/2026-10-17-gaussian-jet-trajectory-diagnostic.md`:
phase samples, unverified quadrature and small covariance norm alone
provide no stability or sign certificate. The step-177 audit already
validated the unreplaced finite-H observable; do not repeat that audit.

The following is a proposed discriminating test, not a derivation or
approved intermediate result. Use L390 (4)--(5), L368's nonvanishing
right-line response and its separately controlled phase derivatives,
and L419's literal two-stage rule. Identify every branch equality
for the comparison matrix and test whether homogeneity reduces its
leading response dependence to finitely many algebraic conditions in
the angle of R(t)Z(t). At every identically vanishing condition, test
the selected *sum of Q values*, including permutation/sign symmetries,
rather than presuming that discontinuity of the basis implies a jump
of the sum. For nonidentical conditions, seek a uniform small-arc
bound and transfer it to actual height using the actual phase
derivatives. Such a transfer, all approximation errors near the ties,
and the complete complementary selection still need proof. Neither
independent phase averaging nor an unspecified limiting measure is
permitted. No branch polynomial or sublevel bound was derived this turn.

Continue if the complete strict-branch error and exceptional-height
contribution both tend to zero, with persistent ties handled directly,
or if an exact actual-response obstruction to the requested o(1)
comparison is obtained. A generic discontinuity example only refutes a
generic shortcut. If a persistent tie has an uncontrolled jump, or no
uniform actual-height estimate emerges in one bounded attempt, preserve
that obstruction and park this comparison; do not resume floating
sampling or re-browse the same continuity theorem. Signing B_H^0 and
showing a nonzero defect remain outside this target.
