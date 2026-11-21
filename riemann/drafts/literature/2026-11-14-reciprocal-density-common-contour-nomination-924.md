# Reciprocal-density common-contour mechanism: completed review925

TARGET: Assess whether a common right-half-plane contour through z=1 can make both the scalar inverse-Laplace weight and the full two-variable determinant integrand pointwise nonnegative for C466a's p at x=B'(1), retaining the contour Jacobians and determinant sign.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review925 searched inverse-Laplace/Hankel/Vandermonde, positive and perfect contour, actual reciprocal-Xi and characteristic-function symmetry terminology; reused assessment914 and the November6 phase/Jacobian comparison, and inspected the primary passages below. No exact simultaneous-phase theorem was located; no novelty inference.
SOURCE_EVIDENCE: Forrester arXiv1806.10411v1 (1.7) p2, full Section2.2 proof p4 and N=2 (2.4) p5; Ruzza notes updated4May2022 Lemma3.1.1 pp27-28 full proof; Iksanov Xi’an2019 notes Theorem113/Remark114 p63 and Lemma141 p76 full proofs of113/141; Lawrence–Yamauchi PRD110(2024)014508 (4)-(8) p3 and phase qualifications pp4-5. C466a audited density/inversion is reused with its external-input qualifications.
COMPARISON: The bilinear determinant identity supplies a representation subject to integrability, not pointwise signs; scalar perfect-contour theory supplies no common-contour theorem for the determinant observable. A standard real-characteristic-function symmetry test is available, but its applicability to these simultaneous phases is unproved. C466g boundary signs and C466j chamber stop are contrasts, not premises.
GAP: A separate mathematical step must compute the exact signed two-variable pullback, check its geometric phase implications, and test scalar-phase compatibility with the actual tilted law. No contour existence/nonexistence or phase implication is established here. Arbitrary noncompact deformation/end estimates remain unproved and may not be assumed.
REASON: Essential representation and probability sources now support a bounded necessary-condition screen before contour construction; derive only this identified applicability difference in a separate turn. Successful signs would still need admissible deformation and all-order/global transfer. No known identity is to be reproved.
SCOPE: Completed literature-only comparison of the exact TARGET; C466a actual h and normalized p=theta_1, x=B'(1), regular injective C2 common product curves in Re(z)>0 with gamma(0)=1 and gamma'(0)=i. No lemma, phase consequence, mathematical script, contour construction or sign theorem is derived. The original nomination below is retained as provenance.


## Completed source comparison925 — 14 November 2026

Outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. This review
fills source scope and specifies a test; it establishes neither a new
mathematical input nor an obstruction. Its differences from the sources
are unproved applicability steps. No mathematical exploration counter
is spent or reset. The unfinished working note925 is preserved.

### Inspected primary inputs

Peter J. Forrester, *Meet Andréief, Bordeaux1886, and Andreev,
Kharkov1882–83*, [arXiv1806.10411v1](https://arxiv.org/pdf/1806.10411v1),
27 June2018, (1.7) p2, Section2.2 p4, and the full N=2 display
(2.4) p5: determinant integration is bilinear; no conjugation or
positivity conclusion is supplied. Read the complete permutation,
transpose and row-integration proof. Reuse assessment914's identity
comparison; no reproof or actual-density specialization was performed.

Giulio Ruzza, [*Introduction to Random Matrix Theory, Riemann–Hilbert
problems, and Universality*, notes updated4May2022](https://webpages.ciencias.ulisboa.pt/~gruzza/introRMT.pdf),
Lemma3.1.1 pp27–28 (PDF pages27–28): measurable complex-valued f_i,g_j
on a measure space, with every f_i g_j in L1, give

    integral det[f_i(u_j)] det[g_i(u_j)] product dmu(u_j)
        = n! det[integral f_i(u)g_j(u) dmu(u)].

Read (3.1.2)–(3.1.9) completely. This is sufficient under absolute
integrability and does not require a positive complex contour weight.
For a parametrized contour, a future application can absorb its
complex weight and Jacobian into one function family over Lebesgue
measure; the required product L1 checks must then be supplied. Neither
this observation about the theorem's scope nor its bilinear convention
is an actual determinant sign certificate.

Alexander Iksanov, [*Characteristic functions and their relatives in
probability theory*, Xi’an2019 lecture notes](https://do.csc.knu.ua/wp-content/uploads/2023/01/Char_funct_XIan2019.pdf),
Theorem113 and Remark114 p63, and Definition139/Lemma141 pp75–76
(PDF pages63,75–76). Read both full theorem/lemma proofs. A probability
law is symmetric about zero exactly when its characteristic function
is real and even on the entire real axis. Uniqueness uses agreement
on a dense subset of the positive axis; agreement on a finite interval
is explicitly insufficient in general. This gives a possible scalar
phase discriminator, not a conclusion about the nominated curve.
Any argument starting with only local reality must separately justify
an analytic extension in the tilted-law setting. No moment,
independence or density hypothesis is imposed by Lemma141 itself.

Scott Lawrence and Yukari Yamauchi, [*Convex optimization of contour
deformations*, Phys.Rev.D110(2024),014508](https://journals.aps.org/prd/pdf/10.1103/PhysRevD.110.014508),
(4)–(8) p3: permitted deformations are boundaries in a region where
the holomorphic top form is closed; the pulled-back action includes
the logarithm of the Jacobian determinant. Rechecked the primary
passages; reuse November6's full phase comparison. Their pp4–5
distinguish locally constant effective phase from a globally perfect
contour, and footnote7 explicitly qualifies the proposed parameter
family as conjectural. No existence result for a common scalar and
determinant contour is available from these passages. For a noncompact
Bromwich deformation, truncation and vanishing connecting-end integrals
would still have to be verified; this paper supplies no such estimates
for h. No strong-duality theorem or model-specific no-go is imported.

### Applicability and remaining obligations

C466a's audited hypotheses and proof were read completely. Reuse its
one-sided smooth strictly positive density assertion, transform,
polynomially weighted inversion and sector estimates; retain the
counting and verified-zero external qualifications. The probability
normalization for the proposed test is p=theta_1, not Theta=theta_1/c_0.
The positive constant relating them must be retained when identifying
an exact determinant. The source's Gaussian-mixture claims are unused.
No logarithm across a zero, extra zero verification, new zero-free
estimate, residual PF assumption or cross-notebook input is introduced.

The future specialization must check the derivative moments at s=1,
not silently substitute a large-s asymptotic. It must retain the sign
in C466a's definition of the differential determinant and both factors
gamma'/i. The two determinant factors in the source are algebraic,
so replacing either by a conjugate changes the question. Compute the
full N=2 pullback before drawing any secant or tangent conclusion.
No formula for that specialized pullback is proved in this review.

A bounded screen can examine necessary scalar/pair conditions on a
nontrivial arc through1 before trying to construct an admissible
infinite contour. Such a negative test needs no successful deformation:
any purported admissible contour must satisfy its local conditions.
If only an arc is used, extending a phase identity requires a justified
holomorphic domain and the identity theorem, or an equally rigorous
alternative. The density transform is an available interface, not a
license to apply the probability uniqueness theorem on an interval.
If there is no contradiction, stop with that limited result; endpoint
control, actual construction and all-order signs remain unpaid.

### Duplicate/search comparison and decision

Narrowly screened November14 actual-density/contact/semigroup records
and November6 angular-contour records for Andreief, inverse-Laplace,
common-contour, secant and characteristic-symmetry overlap. Assessment914
already supplies the general determinant identity; its contact-cone
question does not test these phase conditions. The angular-contour
stop retains its different actual-G integral and does not ban this
mechanism. C466g and the audited C466j stop remain intact.

Queries included `"inverse Laplace" "Hankel determinant" "Vandermonde"`,
`"positive" "contour" "Vandermonde" phase sign problem`,
`"perfect contour" Vandermonde sign problem`,
`"Hankel" "contour" "real-valued" "Vandermonde"`,
`"Sra" "Xi" "contour" positivity reciprocal`, and
`characteristic function real valued if and only if symmetric distribution
lecture notes theorem pdf`. Search snippets were discovery only.
The kissing-polynomial/multi-cut Hankel and newer author Xi PDFs were
unread leads, not imported results. KTH and Melbourne probability PDFs
failed direct web retrieval; Iksanov's inspected theorem and proof supply
the required symmetry coverage instead. This is not an essential blocker.

SPECIALIZE permits a separate bounded application of these standard
inputs, without asserting originality. The mathematical target is saved
in `2026-11-14-reciprocal-common-contour-phase-test-925.md`; the newly
written ready continuation requires separate approval next turn. No
mathematical attempt was invoked in this literature-only review. A
creative mechanism is due, but a routine representation/phase prerequisite
must not be mislabeled creative. Full matching Mathlib coverage is
unchecked; the probability and determinant support is not the full
common-contour result. All-order/global signs and L030-L032/C032a
transfer remain independent open gaps.

## Original prospective nomination retained (unexecuted)

## Prospective screen and decision threshold

Use h(z)=xi(1/2+sqrt(z))/xi(1/2) and B=log h with C466a's
normalization. The inverse-transform factor to source-check is
exp(x*z)/h(z), at x=B'(1). Work in Re(z)>0; no logarithm is
continued across zeros. The regularity and convergence hypotheses
required for inversion and deformation must be obtained from sources.

The proposed contour class is regular injective C^2 curves
gamma:R -> {Re(z)>0}, oriented from the lower to the upper end,
with gamma(0)=1 and gamma'(0)=i. The contour is common to both
variables, with Cartesian product as integration surface. Required
endpoint and homotopy conditions remain source obligations; they
do not follow from these local requirements. Coupled nonproduct
surfaces are outside this first test.

Define the proposed scalar pullback condition using

    w_gamma(u)=exp(x*gamma(u))/h(gamma(u))*gamma'(u)/i.

Ask whether w_gamma is strictly positive real for all finite u,
and the full two-variable signed determinant pullback is real
nonnegative for every distinct u,v. The latter must include the
Vandermonde, determinant convention and both Jacobians from an
inspected identity. No formula for that identity or consequence of
these phase conditions is derived here. Exponent phase alone is
insufficient; the Jacobian is part of the question. The fixed
tangent removes an arbitrary orientation phase.

Retrieve primary determinant-integration hypotheses and sign/proof
cases before larger passages. Classical Andreief/continuous
Cauchy--Binet and contour phase-rigidity are leads, not imported
theorems here. Check stronger results and exact local duplicates.
Import a known obstruction rather than reprove it. If a specialization
is needed, assess its precise scope for a separate mathematical turn.

Continue only if the comparison supplies a valid contour/sign import
or a fully specified, independently testable phase compatibility
question under actual h hypotheses. Abandon this common product-contour
mechanism if its necessary conditions are inconsistent or deformation
already requires the missing zero geometry/PF property. Source access
failure parks dependent work; a failed search is not nonexistence.

## Recovery comparison and downstream limits

Three mechanisms were compared at nomination level, without a second
mathematical attempt. A smaller actual-law chamber cone needs explicit
new constraints and a new preservation test; none is presently justified.
It must not rename the unrestricted cone or increase particle count.
Another growing-order boundary estimate duplicates C466g's audited
relative-error result through floor((log s)^(1/4)) (steps908/909);
changing a trial order range does not pay spatial/global signs.
The selected direct common-contour screen instead tests pointwise
phase at one fixed x. It differs from the actual-G angular coefficient
integral and fixed-collar collective saddle, while retaining their
phase/Jacobian warnings. No automatic contour sign import is reopened.

Plausible downstream use is a positive determinant integral at arbitrary
finite orders if representation and geometry can eventually be proved.
The two-variable screen alone establishes neither this extension nor
all-x coverage. Known finite PF signs for actual p are not the objective;
the target tests a proposed mechanism for reaching unbounded orders.
All orders, global spatial coverage and L030-L032/C032a transfer remain
open independently.

Essential future local input is C466a with inherited L018/external
qualifications. C466g and C466j are overlap/route comparisons, not
positivity premises. No C466b contact, C466i, residual PF assumption,
new zero-free estimate or cross-notebook input is used. Full matching
Mathlib coverage is unchecked. A creative proof attempt is not ready:
exact representation and phase-obstruction source scope must be assessed
first. This uncovered nomination requires its separate literature turn;
no new mathematics is approved in this file.
