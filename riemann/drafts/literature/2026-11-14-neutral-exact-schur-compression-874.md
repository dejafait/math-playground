# Exact finite energy-metric diagnostic: source review874

TARGET: Test whether the fixed U12 neutral compression at T=4log(3) satisfies the generalized Schur positivity criterion for V=U6, including positivity of the Z block and its kernel-range condition.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review874 searched generalized Schur/Moore-Penrose/range criteria and the fixed neutral Weil compression; read primary statements and essential proof cases below, searched exact U12 terminology in local lemmas/assessments/attempts, and reused assessment869's unchanged stronger-window and failed-method comparisons. No originality inference.
SOURCE_EVIDENCE: Read Sano2026 Theorem2.6/full proof, Theorem2.1/proof and Corollary2.2 at https://link.springer.com/article/10.1007/s44146-026-00231-y; Gallier24August2019 Proposition4.2/proof and Theorem4.3/pp9-13 at https://www.cis.upenn.edu/~jean/schur-comp.pdf; Dritschel--Rovnyak0903.3639v1 AppendixA LemmaA.1/full proof/printed pp28-29 at https://arxiv.org/pdf/0903.3639v1; Higham2023 Theorem1 at https://nhigham.com/2023/06/01/what-is-the-schur-complement-of-a-matrix/. Reuse assessed complete-entry/interval methods870/804/861; additional smaller-window lead inspected below.
COMPARISON: The exact finite Hermitian criterion is known, including singular blocks: nonnegative complementary energy, kernel-range compatibility and nonnegative pseudoinverse Schur remainder are jointly necessary and sufficient. C750c rejects a scalar replacement only. Known supported positivity reviewed869 and the additional even small-support theorem below do not settle these fixed U12 blocks.
GAP: Complete finite entries with rigorous errors, positivity or negative inertia of the Z block, exact singular compatibility if needed, and the Schur sign remain uncomputed. A passing finite test leaves the infinite complementary resolvent and all global/non-neutral/Xi gaps open.
REASON: Separate literature-only review874 completes the changed target's missing singular/complex source comparison; one bounded calculation/REPRODUCTION attempt is supported. Import the abstract criteria without reproof; justify only the exact finite coordinates, full entries and signed application. No local block sign is established by this review.
SCOPE: Same exact cutoff, T=4log3, U6 subset U12, original L2 metric, both complex moment constraints and complete31-delay form as C750c; no mode/window/shift sweep or infinite-complement conclusion.

## Preserved nomination from audit873

The following text recorded the REVIEW_REQUIRED nomination before review874.

This file nominates a future question only. It records no new lemma,
block inequality, positive eigenvalue or approval. The next source
review should keep the exact target above, inspect the required
positive-definite and singular cases in primary sources, compare any
stronger known supported positivity result, and search notebook-local
duplicates before choosing IMPORT, SPECIALIZE, EXPLORE or a stop.

Essential local inputs are C750c's exact V, U12 and Z, C750a's cutoff,
L744(6)-(8) and L750's validated full-form evaluation methods. C750c's
scalar comparison is contrast/stop evidence, not a positivity input.
No positive Z block, infinite floor, full covariance, H2-prime premise,
cross-notebook theorem, Xi realization or RH assumption is available.
Full matching Mathlib coverage is unchecked.

Plausible downstream use: a rigorously signed finite energy-metric
diagnostic can decide whether the exact-block route survives the
scalar-floor stop before investing in an infinite complementary
resolvent bound. A passing finite block would still leave that bound,
all other directions/windows, non-neutral terms and global assembly
open. A rigorously negative finite direction would need separate
critical review and would not itself be the local goal's certified
off-line zeta zero. Overlapping bounds are inconclusive; no sweep is
nominated. Generalized Schur testing is a standard method, not a new
central mechanism invented to satisfy creative-routing preferences.

## Completed literature comparison874 — 14 November 2026

LITERATURE_REASON: Assessment870 covered scalar-floor rejection, not the changed exact energy-block target or its singular kernel-range case. This essential missing coverage, nominated by audit873, requires this separate literature-only step despite the balance preference for mathematics.

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The intermediate question is the fixed finite neutral
compression. Its use is to screen the exact-block route before
investing in an infinite complementary inverse bound.

### Inspected primary criteria

Takashi Sano, *Moore-Penrose inverse, generalized Schur complement and
inertia*, Acta Scientiarum Mathematicarum, published27February2026,
[Theorem2.6](https://link.springer.com/article/10.1007/s44146-026-00231-y#Sec2),
states for any finite complex Hermitian block matrix

    M = [ A  B ; B*  G ]:
    M >= 0 iff G >= 0, ker(G) subset ker(B),
                      A-B G^dagger B* >= 0.

Dagger is the Moore-Penrose inverse. Read the full proof: positivity
forces kernel inclusion using the square root of M; an invertible
triangular congruence gives both directions. Read Theorem2.1's
multiplication/range-projection proof and Corollary2.2's congruence
and inertia identity. They also give ran(B*) subset ran(G).
Albert1969 Theorem1 is Sano's original attribution; the original paper
was not read. The bounded-operator extension additionally assumes
closed range; it is not an import for an unbounded Weil operator.

Jean Gallier, *The Schur Complement and Symmetric Positive Semidefinite
(and Definite) Matrices*,24August2019,
[Theorem4.3, printed p12](https://www.cis.upenn.edu/~jean/schur-comp.pdf),
gives the real symmetric criterion with (I-G G^dagger)B^t=0.
Read Proposition4.2's entire singular minimization proof, pp9-12:
kernel coordinates must have zero linear coefficient; minimization
then reduces to the invertible part. Read the criterion and ensuing
factorizations, pp12-13. Reuse assessment870's Propositions2.1-2.2,
pp3-4, for the positive-definite case. Invertibility alone is not
positivity. No abstract criterion needs reproof.

Higham's [Theorem1, Generalized Schur Complement,1June2023](https://nhigham.com/2023/06/01/what-is-the-schur-complement-of-a-matrix/)
explicitly states the complex Hermitian range criterion. Read that
statement and its positive-definite specialization; Sano supplies
the inspected proof. Dritschel--Rovnyak, *The Operator Fejer-Riesz
Theorem*, [0903.3639v1,21March2009, AppendixA LemmaA.1](https://arxiv.org/pdf/0903.3639v1),
printed pp28-29, gives positive diagonal blocks plus a contraction
factorization for bounded complex Hilbert-space blocks. Read both
directions, including the partial-isometry construction. This is
supporting theory, not a source of either concrete block's sign.
LemmaA.2 assumes whole-block positivity and cannot supply it.

### Applicability and the remaining specialization

Use C750c(1)-(2), C750a's chi, L744(6)-(8) and L750 Proof3-4.
C750c Proof1 already defines the exact two moment kernels and the
original L2 orthogonal split, with complex dimensions4,6,10 for V,Z,U12.
Every vector is smooth and supported. Hence the finite restriction
has finite entries on a complex finite space: the finite Hermitian
criterion has the right scope without any assertion of positivity
or an inverse on the infinite complement. This is applicability
comparison, not a signed theorem application.

The prospective blocks A,B,G have sizes4-by4,4-by6,6-by6 in orthonormal
V,Z coordinates. With first-linear Q, define matrix entries as
M_ij=Q(e_j,e_i), so E(sum c_i e_i)=c* M c. An exact real basis with
its L2 Gram and rigorously paid coordinate changes is also suitable.
The future attempt must verify the conjugations and coordinate
identities; a coefficient-space projection is not P_V. Approximate
nullspaces do not define the exact two complex moment constraints.

G must be the complementary ENERGY matrix, not the L2 Gram or
C750c's finite covariance. The criterion uses A-B G^dagger B*,
not A-B B*/d. C750c's scalar rejection therefore leaves this test
open; its E(z) interval still straddles zero. No concrete block
entry or sign is computed here.

Reuse the previously assessed complete Fourier/linear-interpolant
method of L750 and C750c's real Simpson moment method, checking new
functions' error constants. Retain all31 prime powers, the full
archimedean head, infinite frequency tail, period images, interpolation
and rounding. Both exact moments cancel the pole cross term.
The existing selected directions do not supply missing symmetric or
mixed entries. Reuse assessment861's integration/DLMF coverage and
assessment804's inspected Rump2010
[Section10.8, Lemma10.12 and(10.53)-(10.55)](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf)
as optional residual verification only: all entry and factor errors
must enter the residual. No new numerical constant is approved here.

A certified positive-definite G has a vacuous kernel condition and
its ordinary inverse suffices. In the singular case certify the
exact kernel/range and compatibility before using the pseudoinverse.
A small numerical eigenvalue is not an exact zero; an interval
containing zero proves neither singularity nor positivity.
Unresolved rank, compatibility or sign means inconclusive.
Discarding modes or replacing the question by a regularized matrix
is outside scope. Numerical regularization, if used as machinery,
must still certify the original unshifted matrix.

### Overlap, duplicates, failures and search limits

Reused completed assessment869 and approval870 for unchanged supported
positivity: paper45/v2 Theorem1.1 reaches a<=(log11)/2; paper60/v1
Theorem1.1 reaches a<=2; the requested half-width is2log3>2. Neither
their bases nor their complement/covariance certificates transfer.
Suzuki's realization supplies no sign. Zhu v2's corrected upper-comb
condition supplies no six-mode complement. Those already inspected
statements and proof cases are not browsed again. Assessment552's
inverse-order inputs and C744j's ell=log3/2 Legendre neutral graph
concern different spaces and windows; their values are not inputs.

Scoped searches for U_12, U12, first-twelve-mode and kernel-range in
lemmas/, drafts/literature/ and ATTEMPTS/ found C750c, this nomination,
scalar assessment870 and its stop. Read C750c's definitions,
dimensions, representability, numerical contracts and audit scope;
Proof4 explicitly leaves this exact-inverse question open. Reused869's
comparisons of C750a's coarse screen, C750b's exterior functional
stop and C998x's different Gram geometry. None signs this compression.
The historical scalar-floor stop stays in force for that family.

Queries issued: `positive semidefinite Hermitian block matrix generalized
Schur complement Moore Penrose range condition theorem Albert 1969`;
`"Weil" "neutral" "Schur" "4" "log" "3"`; `"Weil" "U12" positivity Schur`;
`"generalized Schur complement" "range" "Hermitian" Albert 1969`;
`"Restricted Weil Forms" "Constraints" "Negative Index"`; and
`"Weil" "neutral" "4log" positivity`. The U12 query produced irrelevant
sports hits. No exact compression theorem was located; this is no
evidence of novelty.

One additional author-hosted lead was inspected for scope:
Pavel V. Kramarenko-Byrd, *Restricted Weil Forms: Constraints, Negative
Index, and Certified Sign*,21September2026, displayed
doi:10.5281/zenodo.22885925,
[author manuscript, Sections1.1/2 and Theorem12.1, pp26-27](https://www.academia.edu/175970157/Restricted_Weil_Forms_Constraints_Negative_Index_and_Certified_Sign).
Its class is even complex supported tests with a cosh moment constraint;
its displayed certificate interval is a in[(log3)/2,11/20]. Read the
statement and proof, including the paid tail and support-comparison
steps. It does not cover the present half-width or both reflection
sectors. No certificate was replayed or constant imported. Enlarged
support/global index equivalences supply no fixed-window sign.
Other search hits remain unused, uninspected leads, not essential
source blockers for this finite criterion.

### Decision and bounded continuation

SPECIALIZE approves only the exact TARGET/SCOPE for one bounded
calculation/REPRODUCTION attempt. The criterion is known; the missing
work is its full signed finite application and rigorous errors.
Nonnegative G, exact singular compatibility if needed and nonnegative
Schur remainder keep the finite route alive, but leave the infinite
complementary inverse bound unproved. A rigorously negative finite
direction or certified failure of an exact kernel condition stops
this fixed positivity test, subject to later critical review.
Neither is the goal's certified off-line zeta zero. Overlapping
bounds are inconclusive: preserve them without a mode/window/shift
sweep or scalar-floor retry.

Essential inputs are C750c for V,U12,Z, C750a for chi, L744 for the
complete form and L750 for evaluation methods. The later calculation
still owes its coordinate, entry, error and arithmetic-model checks.
No RH, positive infinite complement, H2-prime, source numerical
certificate, cross-notebook input or Xi realization is assumed.
Full matching Mathlib coverage was not checked; supporting matrix
or Fourier results are not a verified match for the whole target.

Completed outcome EXPLORATION, LITERATURE/REPRODUCTION: essential
singular complex-block coverage is ready, but no local block sign,
lemma or mathematical script was produced. The next task is
calculation, standard/high. This known-method specialization is not
creative. No separately sourced new central creative mechanism is
ready; that preference does not change the fixed gate target or
justify relabeling this diagnostic.
