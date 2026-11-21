# Central discrete pairing — completed source review

TARGET: Assess source coverage for a degree-dependent discrete-pairing family matching L791's exact central q_0,q_1,q_2 through the finite-free (R2) positive integer-difference mechanism, including both pairings and repeated-root qualifications.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step601 searched integer-difference hypergeometric root criteria and prescribed coefficient-ratio matching; reused steps474/594/597 and searched central/Jacobi assessments, attempts and history for discrete-family duplicates. No exact central feasibility theorem was located in this bounded search; no novelty claim.
SOURCE_EVIDENCE: Martinez-Finkelshtein–Morales–Perales https://arxiv.org/pdf/2309.10970v3 (2 May2024), printed pp.5–6 (8)–(14), p.9 (30), pp.11–12 Proposition2.7, pp.15–16 Theorem3.1/full coefficient proof, p.22 Remark4.1/(60)–(61), p.23 Table2, pp.33–34 (75), Proposition4.15(ii)/(R2) and iteration sentence; Holland https://arxiv.org/html/2608.08682v1 (9 August2026), Lemma6.2/full proof and (66)–(71). Earlier matching, mesh and fixed-tuple classification coverage reused.
COMPARISON: The primary rule covers either pairing with one or both continuous paired gaps replaced by integers 1,...,d-1, allowing multiplicities; it does not solve the central equations. L817 fixes a tuple and L818 assumes strict growing gaps; neither decides the discrete/mixed regime.
GAP: Exact central feasibility for unbounded degrees with freely degree-dependent tuples remains unproved; no inspected source supplies its answer, a degree cap, uniform separation or signed residual control.
REASON: Essential source coverage now supports one bounded algebraic compatibility attempt, importing matching and root results rather than reproving them. No feasibility result is derived in this literature-only step.
LITERATURE_REASON: Step600 changed the strict inequalities to discrete differences; prior strict-regime coverage did not settle their exact ranges, iteration or multiplicities.
SCOPE: Completed literature-only gate. The next mathematical test is specified separately in 2026-11-05-central-discrete-pairing-test.md; that newly written continuation awaits separate approval. No lemma or mathematical script is modified.

## Target and exact inputs

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
availability of degree-dependent positive-rooted comparison models in
the discrete source regime. Such models could support later model-specific
signed perturbation, but separation, signed payment and mixed assembly
remain independent gaps.

Retain L791's central normalization gamma(j)=8*4^j*j!*a_j,
R_j=gamma(j)/gamma(0), q_k=R_(k+1)^2/(R_k R_(k+2)), and its
L018/L021/L776/L778 completion, analytic-error, data, evaluator and
software contracts. The inherited full enclosures are

    1.07484394250019421126346157158 < q_0 < 1.07484394250019421126346157162,
    1.06274366627144916855311401273 < q_1 < 1.06274366627144916855311401285,
    1.05430333113463476927545484495 < q_2 < 1.05430333113463476927545484516.

No evaluator or binary was replayed or attested. Actual ratios stay
fixed and correlated; rounded centers are not exact inputs.
For k=0,1,2 retain the equations

    q_k=(A_d+k)(B_d+k+1)(C_d+k)(D_d+k+1)
        /[(A_d+k+1)(B_d+k)(C_d+k+1)(D_d+k)].

All four parameters are positive and may depend on integer degree d.
D is free; neither D=B_J/2 nor L791's one solution box is imposed.
The two pairings are (A_d,B_d),(C_d,D_d) and
(C_d,B_d),(A_d,D_d). Degree is the source's n, not the shift.

## Inspected primary statements and proof cases

A. Martínez-Finkelshtein, R. Morales and D. Perales,
*Real roots of hypergeometric polynomials via finite free convolution*,
[arXiv:2309.10970v3](https://arxiv.org/pdf/2309.10970v3),
2 May2024 (printed manuscript date 3 May2024),
IMRN2024(16),11642–11687. Page numbers below are printed PDF pages;
the previously noted inconsistent HTML date is not used.

Proposition4.15(ii), p.33: b_1,b_2>0 and a_i>b_i+d-2 for
i=1,2 imply positive roots. (R2), p.34, permits replacing either
paired condition by a_i-b_i in {1,...,d-1}. The following sentence
expressly permits iteration on the other parameter set when its
conditions hold. The discussion preceding the proposition permits
parameter permutations. Thus the exact reviewed discrete extension
has at least one paired gap in that integer set, and the other gap
either in the same set or strictly greater than d-2, with positive
denominators throughout. This is sufficient coverage, not a complete
classification of positive-rooted models.

At d=1 the discrete set is empty. Equality at d-2 is not silently
included in the continuous branch; a positive integer in the stated
set belongs instead to the discrete branch. Zero gaps, rounded
noninteger gaps, negative denominators and rules (R1)/(R3)/(R4) are
outside this proposed test.

The relevant proof cases were inspected: (75), p.33, factors into two
2F1 blocks; Table2 covers the discrete block; (30), p.9, supplies its
(1-x)^(d-m) factor for integer gap m. The source's (61), p.22, states
multiplicity d-m at x=1 and the location of the remaining roots.
Remark4.1/(60) expressly gives m=1. Theorem3.1 with its complete
coefficient proof, pp.15–16, concatenates parameters, and
Proposition2.7(iii), pp.11–12, supplies preservation. These are
imports, not reproofs. Older classification proofs referenced by
Table2 were not independently audited; the explicit factorization
cases and the source's own sufficient rule suffice for this scope.

The modified terminating polynomial (8)–(9), pp.5–6, is the ordinary
3F2 multiplied by (B_d)_d(D_d)_d, positive and nonzero here.
Positive A_d,C_d meet the source's exact-degree restriction (13);
(12) gives nonzero constant term. Holland (69) uses the positive
dilation x=D_d*y/(A_d*C_d). These normalization differences do not
alter roots or their multiplicities. They do not establish matching
or parameter existence.

No simple-root conclusion follows from (R2). Its blocks can have
repeated roots; preservation does not assert that the convolution
retains or removes their specific multiplicities. Reuse the inspected
Proposition2.17, p.15: logarithmic mesh is preserved, but a strict
bound needs a strictly separated factor. No such margin is imported.

Jonathan Holland, *A new hyperbolicity wedge and a joint semicircle
limit for Jensen polynomials of Riemann's xi-function*,
[arXiv:2608.08682v1](https://arxiv.org/html/2608.08682v1),
9 August2026: reaccessed (66)–(71) and Lemma6.2's full proof.
It uses positive ratios, initial values and the three quotient
equations to match through index4, without needing D=B_J/2 in that
induction. Reuse step597's comparison: its large-shift existence
construction is not central feasibility, and its stronger localization
hypotheses are not consequences of the discrete root rule. No full
manuscript audit or automatic signed transfer is claimed.

## Search, duplicates and failures

Queries included `"hypergeometric" "integer differences" "prescribed"
coefficients zeros`, `"3F2" "positive" "integer" "4.15" roots`,
`"Jensen" "central" "degree-dependent" "matching" Jacobi`,
`"hypergeometric" "coefficient ratios" "integer" real roots prescribed`,
and `"3F2" "prescribed coefficients" roots`.
No exact central feasibility statement was found in this bounded
search. Summation identities and irrelevant hits were not theorem
evidence. No originality is inferred. Step597's inaccessible optional
broader-matching leads remain unread and unimported; they are not
essential to this narrow local compatibility test.

Read L791's exact model/data/matching proof, L817's classification and
both-pairing exclusions, L818's hypotheses/stop, and the relevant
step474/594/597 assessments and strict-cap attempt/history. Searches
were confined to central/Jacobi assessments, attempts and 5 November
histories. No earlier discrete-family feasibility result was located
there. L817 fixes one tuple; L818 assumes strict growing gaps.
Neither stops this whole discrete/mixed extension. C792a/b and L793
retain their previously assessed residual/tolerance scope, supplying
neither existence nor signed payment here. No cross-notebook input.

## Continuation and limits

SPECIALIZE supports the single bounded algebraic test in
[the next assessment](2026-11-05-central-discrete-pairing-test.md).
Seek exact unbounded-degree feasibility or an obligatory obstruction
covering every tuple and both pairings in the stated regime.
An obstruction may use fewer than three equations if it is necessary
for all solutions. A finite scan, failed solver or one-degree
success does not decide unbounded feasibility.

Continue only with exact feasibility or a surviving explicit necessary
test supporting refinement; a uniform obstruction stops this regime
alone. An inconclusive attempt must name its unpaid condition, not
restart a sweep under another label. No such calculation or conclusion
is derived here. Full matching Mathlib coverage is unchecked.
This is conventional specialization. No justified new creative
mechanism at the central signed-positivity gap follows from these
root-preservation sources alone.
