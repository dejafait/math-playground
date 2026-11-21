# Structured joint enclosure: completed source notes599

Literature-only step on assessment598's exact TARGET. Main gap:
L030-L032/C032a actual-Xi positivity. A fixed joint2044 comparison could
pay finite head/band cross terms; all higher-input/global obligations stay
open. No new mathematical result or numerical bound is claimed here.

Inspected attempt598 and C999q Sections1-6; reuse assessment596/597's
form/reference and analytic all-output coverage. Narrow searches of
12November literature/history/attempt records found the existing scalar
enclosure and its stop, not a ready joint entrywise verification. This
is not an originality claim. Preserve all598 artifacts and parameters.

## Primary hypotheses and relevant proof cases

[S. M. Rump, *Verification methods: Rigorous results using floating-point
arithmetic*, Acta Numerica19(2010),287-449](https://www.tuhh.de/ti3/paper/rump/Ru10.pdf),
corrected author version accessed12November2026; alternate author-hosted
[INTLAB copy](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf).
The header lists corrections including author pp53/54/56. Page references
here use author pagination, not journal pagination.

Inspected Section9.3, Algorithm9.1/(9.10)-(9.14), pp42-44, including
conversion/product rounding; Theorem10.2/proof p53; Lemma10.5 p56;
Theorem10.6/proof and residual(10.14) p57; Algorithm10.7,
Theorem10.8/full proof and matrix-right-hand-side remark pp58-59.
For real interval A,b, a verified strict residual inclusion

    W(b-A yhat)+(I-W A)X subset int(X)

encloses the solution in yhat plus that image and verifies regularity.
W is a fixed approximate inverse, not the reference R. Lemma10.5 uses
positive interval radii and Perron-Frobenius; Theorem10.6 uses invariant
iteration and spectral radius<1. Theorem10.8 applies10.6 to each fixed
admissible input; its explicit remark covers matrix right-hand sides.
The product enclosure is entrywise, with outward conversion and arithmetic.
These are sufficient tests, without an accuracy guarantee.

The first extraction of p56 had corrupted fonts. The complete primary
indexed passage at the INTLAB URL supplied its hypothesis and short proof;
the intact10.6/10.8 passages were read in full, including the latter's
matrix-RHS remark. Requested web screenshots returned no visible page;
shell download failed DNS. No missing theorem is inferred from either
failure, and neither is essential after the primary passages were read.

Reopened Rump, BIT46(2006),433-452, author PDF
[PDF](https://www.tuhh.de/ti3/paper/rump/Ru06c.pdf), Theorem2.3/full proof,
Corollary2.4, (2.12), Lemma2.6, Corollary2.7, author pp4-6.
Theorem2.3 assumes symmetric/Hermitian floating data, alpha_jj<1 and
completion of the specified Cholesky algorithm. Its reconstruction proof
includes underflow. For symmetric nonnegative entry-radius P, Corollary2.7
requires verified bounds c on the reconstruction error and r on ||P||,
and completion after a downward diagonal shift by c+r. It covers all
Hermitian members of the interval. Lemma2.6 bounds the Perron root with
a strictly positive vector; neither this vector nor the shift is free of
rounding obligations. No correlated parameter model is supplied.

## Applicability to the saved target (method comparison only)

The original cosine-data coefficient matrices, moment-ratio coordinates
and predictor equation in C999q/attempt598 are real. A real interval solve
therefore applies to their real matrix coefficients. The final test is
Hermitian order on the full complex endpoint space; no restriction to
real endpoint directions or reflection symmetry is proposed. The middle
has1022 free coordinates; the combined forcing has2044 columns. The
matrix-RHS remark removes a possible scope gap here. It does not remove
the need to verify every column's inclusion.

The analytic entry intervals in C999q Sections2/8, as assessed596/597,
can supply input boxes for this standard solver, rather than the two
scalar eta bounds being the only representation. Exact neutrality still
comes from the exact ratios, with directed boxes enclosing their values;
it does not come from treating independently chosen boxed entries as
neutral. For the true ratios neutrality is already established. The
interval computation may enclose an enlarged, nonneutral parameter box
as a conservative arithmetic device, but the true expression and its
neutral penalty cancellation must remain those in C999q/attempt598.

Both losses must be replaced. A componentwise enclosure of Y belongs
inside the existing full trial-energy and residual expressions, before
their products and reference action are bounded. The head inverse action
uses the exact rational H of C999k; its solve also needs verification.
All finite row products and both endpoint copies must be enclosed. Adding
only an entrywise solve to598's scalar covariance ledger does not test the
proposed mechanism. There is no theorem promising that the resulting
boxes are narrow enough. In particular final use of a radius norm may
still destroy any gain.

Interval inclusion tolerates repeated uncertain occurrences by enlarging
the set. It does not justify identifying independent interval choices,
dropping cross products, or claiming full shared-data correlations were
preserved. This conservative entrywise alternative is implementable using
the inspected algorithms; a sharper affine/correlated-block method would
be a changed target requiring its own assessment. Generic Schur positivity
cannot be assumed as an alternative premise.

The infinitely many output rows remain essential. Reuse C999q Sections5/8
and the unchanged analytic boundary-functional mechanism, evaluating its
predictor-dependent functionals/bounds on the newly enclosed exact map.
No598 tail total for a dyadic trial automatically bounds that exact map.
The old scalar whole-LZ correction must not simply disappear. This review
supplies neither a new tail inequality nor any improved constant.

The final interval Hermitian comparison must cover energy, finite head
action, finite diagonal-reference Gram and full output tail, with all
arithmetic/assembly errors and the .000999 identity threshold paid. It
may use the already assessed full-factor reconstruction instead of the
specific Cholesky implementation, if all its debts are verified. A center
eigenvalue, a factor success flag, a failed sufficient enclosure, or598's
negative lower-matrix witness says nothing decisive about actual F.

Reuse the form/reference theorem assessments596/597 unchanged; no new
application to an unbounded block operator is proposed. Retain the analytic
response, IEEE754/Decimal, whole-neutral-core and unreplayed c_* contracts.
Full matching Mathlib coverage is unchecked, not asserted absent.

## Search record and decision

Queries used: `Rump verified positive definiteness interval matrix
preconditioning Cholesky residual multiple right hand sides structured
error`; `verified solution linear matrix equation interval multiple right
hand sides Rump residual Krawczyk`; `site.tuhh.de/ti3/paper/rump
"Enclosing solutions of linear equations"`; `site.tuhh.de/ti3/paper/rump
Krawczyk "Theorem" "multiple right"`; and precise Lemma10.5/inclusion
property queries to resolve extraction. The author publication list led
to the inspected Acta source. Preliminary Ru10a.pdf was identified as
the distinct BIT51(2011) spectral-norm paper; no theorem from it is used.

Unread theorem leads: Frommer-Hashemi's2012 Sylvester paper, Rohn-Rex's
enclosure paper, Rump-Ogita's2024 factorization paper and Rump's2026 sparse
systems papers. Their abstracts/listings were seen, not their applicable
proofs; they are unnecessary for the chosen direct method and supply no
claimed coverage. This bounded review establishes no novelty.

Decision SPECIALIZE: nominate one unchanged-parameter interval test, with
separate approval next turn. Use at most the inspected Algorithm10.7's15
inclusion iterations per right-hand side, fixed dyadic proposals from598,
and complete unchanged output ranges; stop on noninclusion/unpaid errors
or failure of the final rigorous threshold. No tuning or inference of an
actual negative direction from that failure. Continue on a fully paid
uniform comparison subject to later audit, or an actual rigorously enclosed
violating direction. The latter would refute only the specified comparison.

Local progress is essential method-source coverage, not a mathematical
advance beyond these known methods. No inverse, Gram specialization,
new bound, lemma or mathematical script was derived/written599. The main
RH gap and all independent assumptions remain. A justified unbounded-input
remote-plus-induced creative mechanism is still unavailable; this finite
routine refinement is not relabeled creative.
