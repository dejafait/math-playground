# Strict rank-two Selmer rationality — three mechanisms compared

TARGET: Compare up to three geometric rationality mechanisms for placing a nonzero strict rank-two Selmer class in E(Q) tensor Q_p, against ATTEMPTS/003/004/007/019/030.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Read the five named failures, L005/L006 and relevant L009/L026 statements; reused cycle and auxiliary-field assessments; searched geometric Kato rationality, visibility, and algebraic-coefficient elliptic logarithms; primary read ranges and queries below.
SOURCE_EVIDENCE: Agashe--Stein, JNT 97 (2002), Section 1.1 equation (1.1) and its finiteness paragraph pp.172--173, Proposition 1.3 and proof pp.173--174, Theorem 3.1 and proof cases pp.176--181; Fuchs--Pham, Glasnik Mat.51 (2016), Theorems 1.1/2.2 pp.337--338 and Section 3.2 pp.340--341, with arXiv:1412.1248v2 for algebraic closures; reused foundations/08 and the 2026-10-14 auxiliary-field assessment.
COMPARISON: No inspected theorem produces the required class unconditionally. Fixed-embedding visibility is finite, whereas pointwise visibility exists for every torsor. This supplies a geometric finiteness input for a conditional tower test; logarithm independence separately constrains an algebraic-coefficient shortcut.
GAP: Establish a uniform fixed embedding for the compatible Sha obstruction of an actual class, rather than a different ambient variety at every level; nonzero strict-class production and analytic-order-to-Selmer comparison remain independent.
REASON: Select only the fixed-embedding visibility applicability audit. Its input is a named published result, not a new geometric construction or a proof of rationality for generalized Kato classes.
SCOPE: Completed literature-only comparison of three mechanisms; no new lemma, proof specialization, mathematical script or BSD case. The proposed tower implication is reserved for the separate continuation assessment.
LITERATURE_REASON: The invocation target was REVIEW_REQUIRED; the prior cycle/auxiliary assessments did not cover visibility or the proposed algebraic-coefficient discriminator.

## Main gap, intermediate target and decision threshold

The main gap is rational rank versus complex central order for arbitrary
E/Q with m(E)>=2. In L006's full setting, including its nonzero class,
the particular missing assertion is q(kappa)=0. L005 then supplies the
strict Kummer rank lower bound; L006 supplies the Selmer dimension upper
bound. Neither those premises nor L026's coefficient certificate follow
here from m(E)=2. This review supplies no class or new rank comparison.

The intermediate discovery target was an additional geometric/arithmetic
membership discriminator. Continue only with a precise theorem or an
independently testable condition beyond Selmer membership. Abandon direct
imports that assume points or finite Sha, or conditions automatic for all
torsors. A sufficient condition may leave existence of a suitable geometry,
class nonvanishing and the complex-order comparison unresolved.

## 1. Cycle specialization to divisors: reuse, no reopening

Reused [the cycle-map assessment](../../foundations/08-diagonal-cycle-specialization.md)
for Darmon--Rotger, *Diagonal cycles and Euler systems II*, JAMS 30
(2017), equations (52)--(54), (60)--(63), Definition 1.15, Proposition 2.5
and Section 2.2.2. Its retained ordinarity, character, regularity,
prime-to-level and non-Eisenstein hypotheses still apply. The inspected
maps give higher-codimension Abel--Jacobi classes and cohomological
weight-one specialization; a map to Pic^0(E) remains missing.

ATTEMPTS/003 and /004 prevent treating conjectural point membership or
a finite-Sha point formula as a theorem. ATTEMPTS/005 additionally records
the crossed-stabilization obstruction to the tame-dual contraction.
ATTEMPTS/007 and /019 exclude automatic ordinary lifting and a formal
height-radical argument. Reused the exact Castella theorem/proof scope in
[the auxiliary-field review](2026-10-14-varying-auxiliary-field-kummer-direction.md)
against ATTEMPTS/030; auxiliary variation still supplies no membership
comparison. These are specific stopped inferences, not bans on geometry.

The [published 2016 Darmon--Rotger article](https://link.springer.com/article/10.1186/s40687-016-0074-9)
was reopened at Section 3.1 and Conjecture 3.12: its representation
identifications have a p-adic scalar ambiguity, and the point formula is
still explicitly conjectural there. No refresh of unchanged cycle proofs
or import of an unproved conjecture was needed.

## 2. Visibility: distinguish fixed geometry from pointwise geometry

Primary source: Agashe--Stein, *Visibility of Shafarevich--Tate Groups of
Abelian Varieties*, J. Number Theory 97 (2002), 171--185,
[published offprint](https://wstein.org/papers/visibility_of_sha/jnt_version.pdf).
For a number field K and a **fixed closed embedding** i:A->J of abelian
varieties over K, Section 1.1, equation (1.1) and the following paragraph
(p.173) identify Vis_J H^1(K,A) as a quotient of (J/A)(K) and prove it
finite: that quotient is finitely generated and torsion. No finite-Sha
hypothesis is used. Proposition 1.3 (pp.173--174) makes every individual
H^1(K,A) class visible somewhere, using a splitting extension and Weil
restriction; J and i depend on the class.

Theorem 3.1 and its Sections 3.3--3.4 proof were inspected only
for output scope: its additional torsion, reduction, ramification and
Tamagawa hypotheses construct **visible Sha classes** from point
quotients. No application of that theorem is proposed. Its real-place,
prime-to-n and residue-characteristic-dividing-n cases prove local
triviality, not global torsor triviality.

The usable input is fixed-embedding finiteness. The proposed arithmetic
condition is that every component of one compatible integral Sha tower
be visible under the **same E->J over Q**. This condition is not verified
for any generalized Kato class. Testing its consequence requires the
transition maps, finite exponent and integral Kummer exactness; that
specialization is deferred. Pointwise visualization, with unrestricted
J_n and embeddings i_n, must not be substituted. No uniform bound or
compatible geometry is supplied by Proposition 1.3.

## 3. Algebraic-coefficient divisor descent: an arithmetic constraint

Primary source: Fuchs--Pham, *Some applications of the p-adic analytic
subgroup theorem*, Glasnik Mat.51(71) (2016), 335--343,
[published PDF](https://web.math.pmf.unizg.hr/glasnik/51.2/51%282%29-04.pdf),
Theorem 2.2, p.338. For simple A/Qbar, logarithms u_i in an exponential
domain with exp_A(u_i) algebraic, independence over End(A) implies
independence over End(Lie A), the latter defined over Qbar. Section 3.2,
pp.340--341, applies Theorem 1.1 to A^m and an algebraic linear relation;
the proper subgroup forces an endomorphism relation. This published
theorem is imported by citation, not reproved.

The [arXiv:1412.1248v2 HTML](https://arxiv.org/html/1412.1248), dated
2016-01-11, was used to disambiguate Qbar lost in PDF text extraction;
Theorem 2.2 and Section 3.2 have the same relevant statement and argument.
For any proposed non-CM application, geometric End(E), the exponential
domain and the rational-point logarithm normalization must be checked.
This concerns algebraic coefficients; a finite extension of Q_p is not
thereby a field of numbers algebraic over Q. It does not decide arbitrary
Q_p-linear point membership, and L005's logarithm-weighted vector cannot
be rejected merely because its coefficients are p-adic.

No coefficient-descent calculation is selected or performed. Its role is
to prevent mistaking an algebraic geometric origin for an automatically
suitable strict vector; it is not a positive membership theorem.

## Queries, coverage and selected continuation

Scoped local searches covered the named failures, relevant foundations
and assessment terms `visibility`, `analytic subgroup`, `coefficient
descent`, and `logarithm.*independ`. No matching visibility assessment
was found in that checked scope; this is not a novelty claim.
External queries included:

- `generalised Kato classes rationality Chow group rational points diagonal cycles weight one elliptic rank two theorem`
- `visibility Tate Shafarevich divisible subgroup Tate module abelian varieties theorem`
- `p-adic logarithms elliptic curves algebraic linearly independent analytic subgroup theorem`
- `Fuchs Pham Some applications p-adic analytic subgroup theorem Theorem 2.1 elliptic logarithms linear independence`
- `"elliptic" "p-adic logarithms" "algebraic coefficients" independent`
- `"strict Selmer" "algebraic" "logarithms"`
- `"Kummer" "Fuchs" "Pham" elliptic logarithm`

Search-only leads include higher-level visibility refinements, the 2026
visibility-category paper, and effective two-logarithm lower bounds.
They are not inputs; none is needed to apply the fixed-embedding
finiteness paragraph. No persistent source blocker is declared.
Direct command-line PDF retrieval failed DNS resolution; the web PDF
reads supplied the visibility evidence. PDF screenshot requests returned
references without visible images and were not evidence; the cited
arXiv HTML supplied the algebraic-closure notation instead.

The [Clay primary statement](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf),
p.2, was rechecked: rank equality is the displayed conjecture, while
Remark 1 states the refined coefficient formula separately. The existing
target foundation needs no mathematical change.

The single selected continuation is specified in
[the fixed-embedding assessment](2026-10-26-fixed-embedding-visibility-kummer-audit.md).
It is a known-source applicability audit, not a creative construction.
Continue if the exact fixed-embedding hypotheses and all integral
transitions justify the conditional membership test; stop that inference
if a varying ambient variety, unbounded exponent, or unproved global
lifting assumption is needed. Producing the fixed geometry is a separate
uncovered target and would require REVIEW_REQUIRED coverage. No justified
creative class-production test was found in this bounded review.

## Mathlib

Full visibility, analytic-subgroup and conditional tower coverage: **not
checked**. Named published inputs are mathematical references, not claims
that Mathlib contains the full results. No new result was derived here.
