# Three-factor central matching — completed source review

TARGET: Test unbounded-degree feasibility of the three-factor central quotient system with A1-B1=A2-B2=1 and A3-B3>d-2, using L791's exact q0,q1,q2.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step605 reused step601/603's inspected two-factor coverage, searched the dated central/Jacobi assessments, stops and histories for three-factor/third-factor/two-unit-gap/4F3 duplicates, and searched primary-source leads for coefficient-ratio matching, integral parameter differences and convolution multiplicities; no exact feasibility theorem found in this bounded search, with no novelty inference.
SOURCE_EVIDENCE: Martinez-Finkelshtein–Morales–Perales https://arxiv.org/pdf/2309.10970v3 (2 May2024), printed pp.5–6 (8)–(14), pp.11–12 Proposition2.7(iii), p.15 Proposition2.17/proof, pp.15–16 Theorem3.1/full coefficient proof, pp.22–23 Remark4.1/(60)–(61)/Table2, p.26 Theorem4.7/proof, pp.33–34 Proposition4.15(ii)/(R2); Holland https://arxiv.org/html/2608.08682v1 (9 August2026), (66)–(71), Lemma6.2/full proof; prior factorization cases reused and changed-scope passages reaccessed.
COMPARISON: General parameter concatenation and sufficient per-degree root preservation are known; Proposition4.15 alone is two-factor, while Theorem3.1 permits further factors. Neither source solves these fixed shift-zero three-factor equations or provides unbounded-degree feasibility, a degree cap or uniform separation.
GAP: Establish exact positive feasibility for unbounded degrees or a uniform obstruction covering all positive tuples, including escaping parameters; generalized model initialization/matching, simplicity, separation and actual signed transfer remain separate obligations.
REASON: A third factor changes the matching family outside the audited two-factor caps. Ready known methods now support one bounded algebraic compatibility attempt without reproving root theorems or claiming a creative signed-positivity mechanism.
LITERATURE_REASON: The target changed from two factors to three with two prescribed unit gaps; general concatenation, normalization and multiplicity implications were outside the prior ready assessment. This essential scope review is now complete.
SCOPE: One subsequent feasibility attempt for the exact TARGET, subject to separate supervisor approval of this changed assessment. No degree sweep, new evaluator, additional coefficient matching or signed-stability theorem is covered. Step605 itself is literature-only and derives no feasibility result.

## Exact question, relevance and inherited inputs

For integer d>=2, seek positive A_i,B_i, i=1,2,3, allowed to depend
on d, satisfying

    q_k=product_(i=1)^3 [(A_i+k)(B_i+k+1)/((A_i+k+1)(B_i+k))], k=0,1,2,
    A_1-B_1=A_2-B_2=1, A_3-B_3>d-2.

The question is existence for arbitrarily large integer d. The q_k are
L791's fixed actual central ratios, not adjustable interval centers.
Retain L791's normalization gamma(j)=8*4^j*j!*a_j,
R_j=gamma(j)/gamma(0), q_k=R_(k+1)^2/(R_k R_(k+2)), and inherited
L018/L021/L776/L778 completion, analytic-error, data, evaluator and
software contracts. Its full proof and step478 audit were read, including
the distinction between the polynomial evaluator and actual coefficients.
No evaluator, binary or numerical certificate was revalidated here.

The inherited enclosures are

    1.07484394250019421126346157158 < q_0 < 1.07484394250019421126346157162,
    1.06274366627144916855311401273 < q_1 < 1.06274366627144916855311401285,
    1.05430333113463476927545484495 < q_2 < 1.05430333113463476927545484516.

A universal obstruction on their Cartesian product includes the actual
correlated triple. Finding a solution for just some triple in that box
does not establish actual feasibility. A uniform validated existence
argument on the box would suffice; a midpoint solution would not.
L791's degree-five solution box and fixed D must not be imposed.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
this exact algebraic prerequisite. Plausible downstream use: decide
whether a third factor can supply comparison models in degrees beyond
the two-factor caps. Success leaves full model matching, simplicity,
separation, signed residual payment and mixed assembly unpaid.

## Primary comparison and applicability

A. Martinez-Finkelshtein, R. Morales and D. Perales, *Real roots of
hypergeometric polynomials via finite free convolution*,
[arXiv:2309.10970v3](https://arxiv.org/pdf/2309.10970v3),
IMRN2024(16),11642–11687, uses a terminating normalization multiplied
by the denominator Pochhammer product, (8)–(9). Positive parameters
avoid its exclusions and zero constant/leading terms, (12)–(14).
Thus normalization does not change roots. Its degree n is our d.

Theorem3.1 concatenates arbitrary parameter tuples; its full coefficient
proof (48)/(33) was inspected. Proposition2.7(iii) preserves nonnegative
roots. Table2, row2, covers both positive integer gaps and gaps >d-2.
These are the relevant building-block inputs. Proposition4.15/(R2)
is a two-block presentation; its iteration sentence alone is not a
three-block theorem. Theorem4.7 has stronger gaps >=d-1 and cannot
be applied directly to both unit gaps in arbitrary degree.

Remark4.1/(61) assigns multiplicity d-1 at 1 to each unit-gap block.
It does not assign those multiplicities to the final convolution.
Proposition2.17 preserves logarithmic mesh when positive-rooted factors
are given; a strictly separated factor is needed for a strict imported
bound. No uniform separation or final multiplicity is asserted here.
The scalar in the displayed (60) is not used in coefficient matching.

Jonathan Holland, *A new hyperbolicity wedge and a joint semicircle
limit for Jensen polynomials of Riemann's xi-function*,
[arXiv:2608.08682v1](https://arxiv.org/html/2608.08682v1),
9 August2026, (66)–(71), Lemma6.2 and its full proof, gives conditional
two-factor matching through index4 from positive initial values and
three quotient identities. Its large-shift existence construction is
not a central three-factor existence theorem. A later three-factor
model must explicitly verify its normalization, first ratio and quotient
identities before invoking that induction; the two-factor formula for
S must not be copied unchanged. This review approves the quotient-system
feasibility question, not an unwritten generalized model theorem.

These inputs are imported by citation, not reproved. The needed local
difference is compatibility with the particular exact central data.
No full manuscript audit or full matching Mathlib coverage is claimed.
The older Table2 classification references were covered to the limited
extent recorded in step601; no stronger classification is imported.

## Search record, duplicates and limitations

Reuse [step601's completed comparison](2026-11-05-central-discrete-pairing-feasibility.md)
and [step603's audit coverage](2026-11-05-central-discrete-mixed-cap-audit-coverage.md)
within their stated scopes. Reaccessed only the primary passages listed
above; the earlier (30) factorization review is reused. The pinned PDF
has arXiv date 2 May2024 and printed date 3 May2024; the HTML rendering's
different displayed date is not treated as a revised theorem version.

New web queries included `"finite free" "hypergeometric" "three"
Jacobi multiplicity Martinez Finkelshtein Morales Perales`,
`"hypergeometric" "coefficient ratios" "4F3" roots`,
`"finite free multiplicative convolution" "multiple roots"`,
`"hypergeometric" "prescribed coefficients" "positive" roots`,
`"4F3" "positive roots" "integer"`, and
`"hypergeometric" "two" "unit" "parameter differences" roots`.
No exact feasibility result was located. Search failure is not novelty
or mathematical evidence against feasibility.

Two additional primary leads were screened at abstract/contents level
only: [arXiv:2404.11479v2](https://arxiv.org/html/2404.11479v2),
3 June2024 (multiple orthogonality/asymptotic zero distributions), and
Karp–Prilepkina [arXiv:2202.04388v2](https://arxiv.org/abs/2202.04388v2),
18 April2022 (unit-argument summations with integral differences).
Their detailed theorems remain unread and are not imported. Neither
abstract supplies the prescribed-ratio existence result. They are
optional leads, not essential blockers for an algebraic compatibility
attempt already supported by the inspected sources. No claim that the
broader literature contains no answer is made.

Local searches were confined to the dated central/Jacobi assessments,
central attempts, relevant 5 November histories and step602's working
note. L791's full proof/audit, L819's hypotheses/conclusion/source scope,
and the discrete/mixed and universal-preserver stops were read.
L817 fixes a tuple; L818 assumes two strict growing gaps; L819 concerns
two factors, with at least one integer gap. None states a cap for this
six-parameter product. No duplicate exact three-factor answer was found.
C792a's universal-preserver stop supplies no positive transfer input;
it also does not prohibit a changed model-specific argument. No earlier
stop is erased or treated as a global ban. No cross-notebook input.

## One bounded continuation and decision test

SPECIALIZE authorizes one algebraic compatibility argument after the
separate approval required for this updated assessment. Seek either
positive exact solutions for an unbounded sequence of integer degrees,
or a finite upper bound on the third gap valid for every positive
solution, which would cap d through the stipulated strict inequality.
A full inconsistency proof also resolves the target. No particular
upper bound, limiting tuple or candidate solution has been calculated
or asserted in this source review.

Choose one elimination/inequality argument or one rigorously controlled
limiting construction. Any compactification or limiting construction
must justify its treatment of parameters tending to zero or infinity;
a limiting residual equal to zero is insufficient. A construction must
verify exact equations, positivity and the strict degree-gap condition,
using an appropriate existence theorem with all hypotheses checked.
L791's already assessed Banach-validation method can be reused if an
appropriate box and uniform bounds are actually established. A failed
solver, finite degree scan or parameter count does not decide this test.

Continue on a proved unbounded family or a concrete necessary condition
with a specified unresolved case. Abandon this regime on an all-tuples
obstruction; an inconclusive bounded attempt must preserve the escaping
case or failed estimate and reassess before repeating. It cannot be
relabelled as a new mechanism to renew exploration. This target is a
conventional finite-free specialization, not a creative signed-positivity
mechanism. The blocker to such a creative target remains the absence of
an independently justified model-specific signed payment principle.

Step605 completes source coverage only: EXPLORATION, not a mathematical
advance or negative feasibility result. No new lemma, proof, mathematical
script or script execution occurred. The main argument and DAG are
unchanged; RH remains IN_PROGRESS.
