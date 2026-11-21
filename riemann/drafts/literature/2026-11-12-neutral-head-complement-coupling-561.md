# Source comparison: signed coupling to the infinite endpoint complement

TARGET: Assess a signed head-to-complement covariance bound for C999l's fixed reference comparison, extending its predictor by zero on free endpoint modes n>=512 and retaining full U and both T orientations; identify one quantitative mixed-block target without assuming complement positivity.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step562 searched signed Weil/Galerkin mixed covariance, infinite-dimensional Schur contraction and logarithmic Fourier complements; inspected the exact sources below and local assessments553/555/558/559, stop558 and C744z's scalar/derivative/response-prefix stops. No matching numerical bound was located; no novelty inference follows.
SOURCE_EVIDENCE: Inspected Friedrich-Gunther-Klotz1708.01545v1 Definitions4.1/4.4/4.5, Lemma4.2 pp5-6, Proposition5.4/Theorem6.1 and both proofs pp9-10; Li paper45 displayed v2 Sections4-5 (4.4)-(5.5); Dritschel-Rovnyak0903.3639v1 LemmaA.1 and both proofs pp28-29; Behrndt et al.1403.5704v1 Proposition2.1 p4/Corollary3.5 p12. Reuse553/555/559's representation and inverse-order proof coverage. Groskin2607.02828v3 Theorem3.2/Corollary3.3 and proofs Section3 were read for comparison only. Direct URLs and qualifications below.
COMPARISON: Standard form Schur criteria and complete weighted covariance cover a quantitative mixed-block test, not its unknown entries or bound. C999l's output tail does not cover infinite input support. Groskin's finite-band archimedean cutoff order does not bound this signed input complement. A fixed quarter-diagonal covariance budget is now specified as a test, without asserting it or the separate complementary sign.
GAP: Prove the infinite neutral-coordinate/domain specialization and enclose the complete signed mixed covariance against one quarter of the fixed free-tail diagonal budget; the complementary diagonal lower bound and all actual-Xi assembly gaps remain unpaid.
REASON: This completes the invocation-start literature-only task and supplies source scope for one independently testable continuation. It derives no new identity, norm estimate or numerical sign, changes no lemma/script and does not reopen automatic factorization as a sign mechanism.
LITERATURE_REASON: Essential infinite-input and mixed-block scope was explicitly REVIEW_REQUIRED at invocation start; ready553/555/558/559 cover only the finite endpoint head and unchanged inverse method.
SCOPE: Original ell=log(3)/2, full D/S/T/U, exact head predictor and C999k reference unchanged; free endpoint modes n>=512 with both low-mode moment corrections; no complementary positivity premise, tuning, RH or H2 assumption.

The original nomination below is preserved as historical scope; its
pending-review wording is superseded by the completed review below.

The main gap remains L030-L032/C032a actual-Xi positivity. A controlled
mixed block would be an intermediate interface for later complement work,
even while the complement's own coercive bound is missing. Do not infer
that C999l's positive finite margin signs that complement.

The proposed support decomposition uses the free exactly neutral cosine
coordinates of C999l(1): the current indices2,...,511 and free indices
n>=512, each with its two low-mode moment corrections. This is a proposed
new domain to assess, not a claim that raw P preserves neutrality. Retain
ell=log(3)/2, original D/S/T/U, reference R with d0=6.14, fraction1/2
and penalty256. On the free tail the proposed predictor is zero; on the
head it is precisely C999l's exact Galerkin predictor. No cutoff or
reference tuning is proposed.

The source review should determine whether retaining the signed U and
middle-residual cross terms gives an independently testable mixed-block
bound, preferably with an explicit finite collection of boundary
functionals and a paid remainder. It must check exact function/form
domains, the infinite neutral parametrization and every mixed product.
A generic boundedness observation or a restatement of block positivity
is insufficient. Name the norm, required complementary input and useful
threshold before approving a calculation. If no quantitative test can
be justified, abandon this nomination rather than iterate an automatic
factorization or scalar-norm argument.

Essential local inputs to assess are C744v/w's full operator and entry
contracts, C744z Sections1-3 and its scalar/response stops, C999j's strong
domain identity, C999k's unchanged reference and C999l including audit561.
Keep the whole-core, unreplayed c_* and analytic/IEEE754/Decimal
qualifications. The clamped-Green automatic-sign stop558 remains relevant
negative evidence, not a global ban. No cross-notebook input is proposed.

This nomination prepares a possible complement mechanism; it is not
classified creative or preapproved. An independent signed-complement
sign mechanism is not yet justified. Missing source scope comes first;
a later creative nomination must name its own bounded discriminating test.

## Completed source comparison — 12 November 2026, step562

The main gap is L030-L032/C032a actual-Xi positivity. The intermediate
target is a quantitative signed coupling between the audited finite
endpoint family and its infinite free-coordinate complement. Its use
would be to state an explicit complementary energy budget for a later
assembly, without supplying that energy or signing the full three-cell
form. This is a source review, with no calculation or mathematical proof
attempt in this turn.

### Inspected primary statements and essential proof cases

[Friedrich, Gunther and Klotz, *A generalized Schur complement for
non-negative operators on linear spaces*, pinned arXiv1708.01545v1](https://arxiv.org/pdf/1708.01545v1),
Definitions4.1/4.4/4.5, Lemma4.2, Proposition5.4 and Theorem6.1,
printed pp5-6/9-10: complex linear spaces map to their antilinear
duals, with first-slot-linear Hilbert products. Positive type requires
the off-diagonal range in the adjoint square-root range of the
nonnegative first diagonal. Lemma4.2 gives the kernel and finite
Rayleigh-supremum conditions. Theorem6.1 requires positive type AND
nonnegative generalized Schur remainder. Its forward proof obtains a
contraction from Proposition5.4; its reverse proof bounds the square-root
inverse action by the second diagonal and constructs that contraction.
Both directions and Proposition5.4's factorization proof were inspected.
These statements concern forms, including spaces without a Hilbert
operator domain, and do not require assuming the entire block positive
before testing its remainder. They supply no local quantitative bound.
The served PDF header says v1,4August2017, with internal date30July2018;
the theorem numbering above refers to that retrieved PDF.

[Dritschel and Rovnyak, *The Operator Fejer-Riesz Theorem*,
0903.3639v1,21March2009](https://arxiv.org/pdf/0903.3639v1),
LemmaA.1 pp28-29: a bounded Hermitian block on a Hilbert space split
by a closed subspace is nonnegative exactly when both diagonals are
nonnegative and its off-diagonal factors through their square roots
with a contraction. The forward construction uses the positive square
root and partial isometries; the reverse direction is an explicit
positive factorization. Both were read. LemmaA.2 starts with positivity;
it supplies no missing sign. Apply a bounded theorem only after checking
the weighted coordinate maps, rather than to the raw unbounded D.

[Behrndt, Hassi, de Snoo and Wietsma, *Antitonicity of the inverse
for selfadjoint matrices, operators, and relations*,1403.5704v1](https://arxiv.org/pdf/1403.5704v1),
Proposition2.1 p4 and Corollary3.5 p12 were reopened. The former gives
shifted square-root domain inclusion and norm comparison for order of
lower-semibounded selfadjoint relations; the latter gives inverse
antitonicity for nonnegative selfadjoint relations on a separable Hilbert
space. Reuse553/555/559's inspected nonnegative proof case of Theorem3.4
and Teschl GSM99,12February2009, Theorems2.13/2.18 pp71-72/77
[author PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
The existing restriction on H0, its multivalued encoding on L2 and
R<=L remain the required applicability inputs. No new general inverse
theorem, projected-unrestricted inverse identity or c_* floor is needed.
Changing endpoint support does require checking forcing and form-domain
membership; those are the proposed specialization, not checked facts here.

[Hongmin Li, *Cutoff-free positivity of localized Weil forms through
the (log11)/2 threshold*,paper45, displayed v2,9November2026](https://rstation.ai/problems/riemann_hypothesis/papers/45),
Sections4-5, (4.4)-(5.5), was read including its complete-form bridge.
Its complementary diagonal is positive and increasing, and its finite
head mixed map is bounded. Parseval gives a complete positive covariance;
the expansion keeps atom/base cross products. Monotone inverse weights
pay the remaining covariance beyond the finite range. The proof extends
a core comparison using shifted closed-form norms before square
completion. This is an explicit quantitative precedent, not just an
abstract factorization. Its radius, operators, positive complementary
diagonal and numerical certificate differ from this notebook's
remote-plus-induced block. Import its method, not its sign or constants.

[Akiva Groskin, *A finite Guinand-Weil dictionary and archimedean
tail order for the truncated Weil quadratic form*,2607.02828v3,
14August2026](https://arxiv.org/html/2607.02828v3), Section3,
Theorem3.2/Corollary3.3 and proofs: for a fixed finite band I_N and
T2>T1>max(rho N,7), the change in the archimedean integration cutoff
has a positive rank-two-density Gram representation. The diagonal-limit
case, rational-function proof of definiteness, minor argument and the
improper-tail/trace estimate were read. This supplies order and a finite
tail budget in that finite matrix. It does not treat input indices
n>=512, neutral Galerkin forcing, full U or the signed residual cross
term here. It is inspected nonmatching coverage, not an imported
complement estimate. Its computational certificates were not replayed
and none of its numerical signs is used.

### Discovery and local overlap

Queries actually issued included `Schur complement infinite dimensional
block operator positive contraction off diagonal square root Dritschel
Rovnyak lemma A.1`, `logarithmic Weil head covariance`, `Fourier Galerkin
a posteriori off diagonal operator tail rigorous Schur complement mixed
block`, `localized Weil forms mixed Schur`, `Weil neutral Galerkin
covariance complement`, and `logarithmic Fourier Schur complement
positivity`. They led to the above primary statements. General numerical
preconditioning and secondary Schur summaries were not theorem inputs.
This bounded search establishes neither originality nor nonexistence of
a matching bound elsewhere.

Read the relevant proofs/contracts in C744v Sections1-5/response formula,
C744w Sections1-3, C744z Sections1-3, C999j's strong-domain paragraph,
C999k Sections1-2 and C999l Sections1-7. Reuse ready553/555/558/559.
C744z's Sections4/6/7/8 stops and assessment557/ATTEMPTS stop558 already
explain failures of scalar norms, absolute first-derivative payment,
middle-response removal,32-response truncation and automatic clamped
factorization. None tests the new mixed covariance of the unchanged
successful finite-family comparison. C999l's trace-based first pass
was inconclusive, not a negative actual direction. Keep all that evidence.

### Quantitative continuation, still unproved

The separate nomination562 defines the form and mixed map by
polarization, with the exact head predictor extended by zero on the
free input tail. Its fixed test is

    B D_tail^-1 B* <= M_cert/4,

where M_cert is C999l's certified head comparison matrix and
D_tail has the imported positive lower weights d_n for each free
endpoint coordinate n>=512. This is a concrete finite-dimensional
matrix covariance, with infinitely many input columns, not a claimed
inequality. It must retain full U and both T orientations and their
signed residual cross products before forming column outer products.
All output tails in the inverse action also remain payable.

The standard Schur criterion above explains the budget: even a pass
would still need the independent complementary comparison >=D_tail/4.
That claim is NOT assumed, approved or established. The stronger actual
head might improve a later comparison, but is not substituted for the
fixed M_cert in this test. The .000999 scalar floor is available only
for certified solve-error control, not as a replacement for matrix
covariance or as evidence that the quarter budget holds.

A signed finite-input covariance plus a paid analytic remainder can
decide this test. A finite subcollection already exceeding M_cert/4
in a certified direction rejects this fixed budget; an unpaid tail or
an enclosure overlapping the threshold is inconclusive. A generic finite
bound or a Schur equivalence alone is not a pass. No budget, predictor,
reference or cutoff retuning is nominated. See562 for exact domains,
norm, procedure and remaining assumptions. This is ready method coverage
for a REPRODUCTION specialization, subject to the separate approval of
that newly written continuation; no mathematical derivation is performed
or approved as a result of this literature turn.

Full matching Mathlib coverage is unchecked. Standard sources are cited
without reproof; neither their hypotheses nor the signed-complement
estimate are hidden as an automatic consequence. No new creative central
mechanism has emerged: the next test develops an established quantitative
route. Complement positivity, whole-core/unreplayed c_*, execution
contracts, C744q, H2, non-neutral coverage and actual-Xi assembly stay open.
