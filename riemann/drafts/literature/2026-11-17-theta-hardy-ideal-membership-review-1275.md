# Theta coefficient ideal membership — reviewed1276

TARGET: Review whether Hardy-space ideal-membership results decide C032f(20) for its fixed theta coefficients and R with both Y_sigma in H2(Re z>0), checking coefficient growth, one-sided L2 correspondence and every hypothesis of a proposed analytic inverse.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact half-plane Laplace/H2, unbounded Hardy ideal membership, corona/Leech and RKHS membership/range searches; compared C032f(12)-(25), review1270/completed1271 and stops1272/1273. Primary statements and essential proof cases inspected as detailed below; no theta membership answer located or novelty inferred.
SOURCE_EVIDENCE: Seifert--Trostorff--Waurick2022 Chapter8 Theorem8.1.2/Corollary8.1.3 and full proof pp119-124; Hartz--Wick1709.07939v2 Section2 Theorems2.1-2.2/Lemma2.3 and its full proof pp3-5; Sarason2008 Sections3-4 pp585-586; Hamilton2012 Proposition2.1.7/Remark2.1.8 and full proof pp15-16; Manton--Amblard1408.0952v2 Sections2.5,5.1,6.1-6.2/Theorem6.2.1 and proof; Gale et al2401.16091v1 Section1(1.1) and following Hardy-kernel display.
COMPARISON: Paley--Wiener pays the exact one-sided L2/H2 identification with its normalization. Bounded corona/Leech does not directly apply to the raw theta coefficients or decide a single RHS; Smirnov operator domains add unpaid hypotheses. General RKHS range/membership criteria instead require bounded individual evaluations, not bounded coefficient multipliers, and offer a full-complex finite-evaluation test after a separate theta specialization.
GAP: No inverse, incompatible finite system or divergent preimage-norm sequence has been established for this witness. The coefficient-weighted RKHS construction, conjugations, common-zero cases and singular matrices must be justified in a later mathematical attempt. Membership alone still leaves universal range inclusion, delta, source metric and actual-Xi signs unresolved.
REASON: Known results cover the transform class and an alternative exact range criterion, but not its theta decision. Park automatic bounded-corona/Smirnov inversion; nominate a separately approved simultaneous-complex-evaluation attempt using the inspected criteria. This is source progress, not a new lemma or a reopened positive-axis calculation.
LITERATURE_REASON: The exact analytic ideal and one-sided L2 realization hypotheses were not covered by the earlier finite necessary norm bound or conditional Hankel factorization. This is a specific missing source comparison, not another search for the unchanged pointwise obstruction.
SCOPE: Fixed C032f(19)-(20), omega=1/4,z=i,c as stated; complex profiles, both components and no preimage-norm cap. Covers source comparison and later specialization of the inspected RKHS criteria, not a bounded normalization, an applicable corona estimate, a delta decision or source-metric transfer. No theta calculation was performed in review1276.

## Completed source comparison1276

The main gap remains actual-Xi mixed positivity in every degree,
L030-L032/C032a. The intermediate target is precisely the fixed
two-component equation below, with actual half-line L2 transforms.
Its possible use is to exclude one vector from ran B*, and only then
to use C032f(5), subject to its unaudited reduction. A membership
answer for this vector has no converse implication for the whole range.

### Sources actually inspected

**Transform convention.** C. Seifert, S. Trostorff and M. Waurick,
*Evolutionary Equations*, OTAA287 (2022), Chapter8,
[Theorem8.1.2 and Corollary8.1.3, pp121-124](https://link.springer.com/content/pdf/10.1007/978-3-030-89397-2_8.pdf).
For a Hilbert value space and real nu, the normalized Laplace
transform (2pi)^(-1/2) integral_0^infinity exp(-zt)f(t)dt is an
isometric isomorphism from weighted half-line L2_nu onto the
holomorphic Hardy space with norm squared
sup_(r>nu) integral_R ||g(r+it)||^2dt. Read its definition, the
forward norm identity, the entire converse proof and Lemma8.1.1:
vertical inverse Fourier transforms are related by exponential
weights, the uniform bound gives one-sided support and L2, and
the contour-side terms vanish along a subsequence. Use nu=0 and
value space C^2. Thus C032f's unnormalized Y has Hardy norm
sqrt(2pi)||y||, or exactly ||y|| if the Hardy squared norm includes
1/(2pi). No reproof or additional support assumption is needed.
This is the only unconditional transform-class input imported here;
its theta consequences are reserved for the mathematical turn.

**Bounded ideal comparison.** M. Hartz and B. D. Wick,
*Ideal membership in H-infinity: Toeplitz corona approach*,
[arXiv1709.07939v2, 19 September2018, Section2 pp3-5](https://arxiv.org/pdf/1709.07939).
Theorem2.2 assumes bounded analytic operator functions F1,F2 on
the disk; it equates a contractive analytic factor F1H=F2 with
M_F1 M_F1* >= M_F2 M_F2*. Lemma2.3 assumes bounded f and a
bounded analytic row F. It equates f=FH, ||H||_infinity<=C, with
solvability FG=fg for EVERY g in H2 with ||G||_2<=C||g||_2.
Read both implications: multiplication proves one direction;
the universal norm bound yields operator majorization and Leech
proves the other. Theorem2.1 additionally requires ||F||<=1,
nonincreasing psi:[0,infinity)->[0,1], integral psi<=1 and the
global size bound |f|<=||F||^2 psi(log ||F||^(-2)). None of those
global theta bounds is paid. The raw coefficients in C032f are
not established bounded multipliers; its existing F-growth/m
discussion prevents treating them as such without normalization.
A single witness solution is weaker than Lemma2.3's quantifiers.
Failure of this sufficient theorem cannot exclude that solution.
Theorem2.1's later Carleson proof is unread and not imported.

**Unbounded-domain comparison.** D. Sarason,
*Unbounded operators commuting with restricted backward shifts*,
Operators and Matrices2 (2008), 583-601,
[Sections3-4, pp585-586](https://files.ele-math.com/articles/oam-02-36.pdf).
Read the Smirnov quotient definition, canonical numerator/outer
denominator construction and the stated multiplier domain.
For phi=b/a in that class, multiplication has domain
{f in H2:phi f in H2}=aH2. This does not assert arbitrary
holomorphic coefficients are Smirnov, or supply a two-component
inverse. Applying such a domain componentwise would also demand
individual products in H2, absent from C032f's equation, which
permits cancellation. The 2008 paper summarizes these facts from
its reference[5]; that earlier proof was not independently read,
and no domain theorem is imported to settle the witness. A
zero-free analytic common multiplier, with certified coefficient
and RHS bounds, would be needed for a bounded normalization;
none is constructed or assumed here.

**General membership criterion.** R. Hamilton,
*Pick Interpolation and the Distance Formula*, Waterloo PhD thesis
(2012), [Proposition2.1.7 and Remark2.1.8, pp15-16](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/5cb1b66f-d860-4f95-963e-898cda124537/content).
For a Hilbert-valued RKHS on a set X and any function f on X,
membership is equivalent to one C>0 making every finite matrix
[C^2 E_xi E_xj* - f(x_i)f(x_j)*] positive semidefinite.
The least C is the norm. Read both proof directions, including
finite Douglas factorization and weak compactness. The finite-set
family in the converse must be directed by inclusion and a
convergent subnet used; mere unrelated finite fits do not suffice.
Use C as a norm bound, as specified by the statement and Remark;
do not infer a different normalization from the PDF's extracted
norm typography in the first proof line. The source requires nonzero
evaluation maps; common-zero points must be dealt with explicitly
or removed before applying it. This condition is recorded for
the future specialization, not assumed checked. No strict Gram
invertibility hypothesis is present.

**Range construction.** J. H. Manton and P.-O. Amblard,
*A Primer on Reproducing Kernel Hilbert Spaces*,
[arXiv1408.0952v2, 5 November2015, Sections2.5,5.1,6.1-6.2; Theorem6.2.1](https://arxiv.org/html/1408.0952v2).
For arbitrary vectors a_t in a Hilbert space, the closed span U
is isometric to the RKHS with Gram kernel <a_t,a_s>. The equations
<x,a_t>=b_t have a solution exactly when b belongs to this RKHS;
the U-solution minimizes norm. Read the embedding construction,
the theorem/proof and the finite interpolation discussion including
singular matrices. Its displayed theorem uses real spaces;
Section2.5 explains the complex convention and Hermitian transpose.
The complex specialization and conjugations must be explicit in
the later proof. It requires each a_t to belong to the input
Hilbert space, not a globally bounded map into an original
Hardy output space. This is the relevant alternative to bounded
coefficient inversion. No theta Gram matrix is derived here.

For normalization cross-check only, J. E. Gale, V. Matache,
P. J. Miana and L. Sanchez-Lajusticia,
[*Hilbertian Hardy-Sobolev spaces on a half-plane*, arXiv2401.16091v1,
29 January2024, Section1(1.1) and following display](https://arxiv.org/html/2401.16091v1)
give the Hardy norm with factor1/(2pi) and kernel
1/(z+conjugate(w)). Only this classical n=0 convention was read;
no higher-Sobolev or composition theorem is used.

### Search limits and route decision

Queries included `Paley Wiener theorem Laplace transform H2 right
half plane theorem L2 pdf`, `Hardy H2 ideal membership unbounded
analytic coefficients Leech theorem corona Smirnov`, `ideal
membership unbounded Hardy`, `reproducing kernel f belongs positive
rank one theorem Aronszajn`, and exact Paulsen/RKHS-note queries.
The original Aronszajn AMS endpoint returned403; its Wisconsin
scan had no extractable text through this interface. Paulsen's old
Houston notes returned404 and candidate Waterloo note endpoints
were inaccessible. These are unread originals, not evidence for
any theorem. The fully readable Hamilton and Manton--Amblard
statements/proofs remove the essential access blocker for a range
criterion. An attempted shell download had DNS failure; the web
primary sources above were accessible. No large scan was treated
as inspected by preview alone.

Reused Douglas/Hankel coverage in review1270/completed1271; no
reproof or repeated search for that unchanged operator theorem.
The local branch records contain no full-complex simultaneous
evaluation criterion; stops1272/1273 leave it untested. This is a
bounded comparison, not a claim of novelty or comprehensive absence.

There is no automatic analytic inverse in the inspected results.
Park direct bounded-corona/Smirnov inversion until its extra
normalization/domain hypotheses are paid. The general RKHS criterion
is a concrete different test: simultaneous complex evaluations
can constrain a common preimage, whereas1273 only used independent
positive-real point norms. Its theta specialization and any actual
obstruction remain entirely future mathematical work.

The continuation is nominated separately in review1276. Continue
only with an incompatible finite system or a rigorously unbounded
sequence of required preimage norms (or a controlled global pair).
Finite large norms alone do not exclude membership: no norm cap
exists. Do not claim that passing finite tests proves membership,
that a criterion decides its own positivity, or that this single
witness determines delta in the membership case. No mathematical
exploration budget is reset. Full Mathlib coverage is unchecked;
no cross-notebook input is used. No justified creative central-sign
target emerges: an independent signed bridge to Xi remains absent.

## Original nomination1275 — preserved below

## Exact object and bounded source test

Use the notation already established in C032f: alpha=1-c, beta=1+c,
a=1/8, F(z)=2Xi(2iz),

    d_sigma(z)=alpha F(z+sigma*a)-beta F'(z+sigma*a),
    R(z)=[F(z+a)+F'(z+a)]/(z+1).

The question is whether the fixed equation

    d_-(z)Y_-(z)+d_+(z)Y_+(z)=R(z),   Re z>0,

has a pair whose members are Laplace transforms of L2(0,infinity)
profiles. The proposed H2 convention is
sup_(r>0) integral_R |Y(r+it)|^2 dt < infinity. Its exact equivalence
with the one-sided L2 class, including Fourier normalization and
converse direction, is an essential theorem to inspect, not a new
assertion established in audit1275. The coefficients are not assumed
bounded analytic functions; arbitrary division by a common factor
must preserve the equation and the requested solution class.

The source review has one discriminator: find a primary analytic
ideal-membership theorem whose checked hypotheses apply to this exact
coefficient/R pair, or identify the precise unpaid hypothesis that
prevents its use. An applicable normalization must be specified,
including zero-freeness and boundedness conditions; an assertion that
some outer factor exists is insufficient. A common-zero or lower-bound
condition cannot be assumed from its positive-real counterpart.
Do not calculate complex zeros, construct profiles, or derive a new
normalization during this literature-only review. If a theorem leaves
a concrete uncovered mathematical condition, nominate that exact
condition with separate coverage and an independently testable bound.
If no such criterion emerges, park this proposed inverse route; do not
repeat the finite positive-axis test or call that repetition discovery.

Reuse the already inspected Douglas and Hankel results rather than
reproving them. Search exact/stronger half-plane Hardy ideal membership,
the appropriate nonbounded-coefficient formulation and known failure
conditions. Inspect primary statements and the proof cases essential
to the claimed implication before importing any result. An ordinary
bounded corona theorem is not automatically applicable here.

## Relevance and preserved stops

The main gap remains L030--L032/C032a actual-Xi all-degree mixed
positivity. A controlled inverse or analytic nonmembership obstruction
would test one missing branch-realization requirement before further
transport work. A positive membership answer for this single witness
would only discharge this witness, not the universal range condition;
an exclusion could be used with C032f's existing Douglas reduction,
after its hypotheses are verified. No sign gain is asserted either way.

Preserve the stops in
`ATTEMPTS/2026-11-17-normalized-branch-pointwise-stop-1272.md` and
`ATTEMPTS/2026-11-17-normalized-adjoint-positive-axis-stop-1273.md`.
Their two exploratory attempts remain recorded. This review seeks
the materially new analytic inverse/obstruction required to reopen
the witness; it does not claim that such an input has been found.
The new L559 negative-block audit provides no input to this equation
and does not revive termwise block positivity or the31Oct global-sign
route. The central theta identity discovery1274 found no independently
signed bridge, so no justified creative positivity target is available.

Essential local material is C032f(12)-(25), C032e's actual theta
conventions and L016/L018/L019/L020 where their hypotheses are used;
reuse `2026-11-17-normalized-approximate-branch-compatibility-review-1270.md`.
Joint transform realizability, coefficient growth, source-metric
transfer, actual-Xi signing, initialization, singular blocks and all
degrees remain unresolved. No cross-notebook input is proposed.
Mathlib coverage is unchecked; no absence or novelty claim is made.
Route the next turn as literature_comparison, standard/high. A later
proof task needs its own precise covered target; no creative or
candidate-audit label is warranted by this nomination.
