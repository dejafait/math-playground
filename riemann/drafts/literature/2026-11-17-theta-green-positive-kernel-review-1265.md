# Theta Green-lift positive-kernel mechanism — completed review1266

TARGET: Review whether the actual theta Green-minimizer operator in Freedman2606.29555v1 Appendix C has a positive integral-kernel representation with row and column masses at most one in its stated profile measure, independently of the unpaid M<=P claim.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Reviewed versioned Appendix C and searched exact paper/Green-minimizer/positive-kernel terms, positive integral-operator Schur-test terminology, and scoped local assessments/failures. No inspected source supplies the requested profile kernel and unit mass estimates; this is bounded coverage, not an absence theorem.
SOURCE_EVIDENCE: Freedman arXiv:2606.29555v1 Section 3 (1)-(7), Section 11's Psi convention and Appendix C from its M/N feature definitions through CKE closure and parameter claim were inspected; Holighaus-Voigtlaender arXiv:2006.01083v2 Section 1.1, both Schur-test statements, and Heil Appendix C Theorem C.20 p308 with its complete proof were read. Precise citations and qualifications below.
COMPARISON: The uniform Schur test supplies the sufficient norm bound once a measurable kernel, correct measure, absolute row/column estimates and agreement with the given map are available. Appendix C supplies signed feature maps and CKE, not those additional premises; C032d already excludes filling them by generic stationarity/completion.
GAP: No actual-theta profile kernel, positivity, mass bound, extension/agreement or independent norm estimate is established. Full-theta versus corrected-core identification and all-parameter applicability remain unverified; no counterexample to theta contraction follows.
REASON: Complete the changed mechanism's source comparison once and park dependent mass calculations until a profile representation is supplied independently of M<=P. The source is accessible; the missing input is mathematical identification, not a network failure. No kernel construction or mathematical derivation was attempted.
SCOPE: Completed literature-only comparison for the exact TARGET. EXPLORE does not preapprove constructing a kernel or testing a different target; no COVERED_TARGET is added. Preserve the original nomination below as historical evidence.
LITERATURE_REASON: Invocation-start nomination1265 was REVIEW_REQUIRED and changed the sufficient mechanism from generic compression to a theta-specific nonnegative profile kernel; assessment1264 did not cover that representation or Schur-test specialization.

## Completed source comparison1266

The main gap is actual-Xi all-degree mixed positivity in L030-L032/C032a.
The intermediate target was an independent positive-kernel contraction
for the source's minimizing profiles. Its possible use was to pay its
trace sign before the separate Weyl/RH bridge. It would leave realization,
initialization and all-degree transfer unresolved.

### Primary source identification and limits

Marvin B. Freedman, *Finite-core Volterra reductions for a Weyl-positive
Riemann phase kernel*,
[arXiv:2606.29555v1, Appendix C](https://arxiv.org/html/2606.29555v1#A3),
displays M/N features, their signed plus/minus squares, and T=CKE.
The profile norm there is the sum over sigma of integrals in du;
the square-root branch weights are inside G, not an additional du weight.
This identifies the displayed ambient norm, not its minimizing range.
The integration in s defining M/N is not a kernel from observed plus
profiles to minus profiles. E is described as the minimizing right
inverse, without an independently justified profile integral formula.

The inspected closure passage uses the multiplier bound and fiber
stationarity; it supplies no separate row/column mass estimates or
positive extension agreeing with T. C032d already tests that generic
passage. Section 11 uses a corrected three-mode Psi, while Section 3
and later claims concern the full Phi; that specialization is not
verified here. Parameter-independent multiplication alone leaves the
omega-dependent lift unpaid. These observations concern the displayed
source argument, not impossibility of a different representation.

### The precise standard comparison

Nicki Holighaus and Felix Voigtlaender,
*Schur-type Banach modules of integral kernels acting on mixed-norm
Lebesgue spaces*,
[arXiv:2006.01083v2 (18 November 2020), Section 1.1](https://arxiv.org/html/2006.01083v2#S1.SS1),
state the specific and uniform Schur tests. The ambient spaces are
sigma-finite measure spaces, the kernel is measurable, and the uniform
version (1.1) assumes essential bounds C on both integrals of its
absolute value. It gives operator norm at most C on every Lp,
including p=2. Nonnegativity is sufficient to identify absolute
integrals with masses; it is not necessary for the Schur test.
The weighted specific version requires positive measurable functions
and two weighted absolute-integral bounds; it does not construct them.
No weighted variant repairs an unidentified kernel or measure.

Christopher Heil,
[*Functional Analysis and Operator Theory*, Appendix C,
Theorem C.20, printed p308](https://heil.math.gatech.edu/7338/fall09/appendixc_1.pdf),
states the Lebesgue-space version with separate essential row/column
bounds C1,C2 and norm at most sqrt(C1 C2). Read the whole proof:
measurability is handled by nonnegative components, Cauchy-Schwarz
uses absolute kernel values, and Tonelli pays the interchange. This
is a citation comparison, not a new proof. The general-measure statement
above covers a finite branch index times the half-line if that is the
identified domain and measure. No new specialization has been installed
as a lemma. Both unit bounds would suffice; neither is supplied for T.

In particular, a Schur operator on the ambient profile space must agree
with the prescribed T on the actual minimizing plus-profile image.
If only a proper subspace is specified, its norm estimate cannot be
inferred from an arbitrary extension. Kernel existence, agreement,
measurability, the two masses, and parameter coverage must each be paid.
The source's finite norms and its scripts' names do not pay these items;
no source script or numerical certificate was reconstructed or accepted.

### Duplicates, searches and decision

Reuse assessment1264 and the full C032d proof for the generic inference;
no second matrix audit was performed. Scoped searches in the November17
assessments/failures and local foundations found the same lead, not an
independent Schur representation. Search queries included `Schur test
integral operator row column masses L2 theorem lecture notes`,
`"2606.29555" "positive" "kernel" contraction`,
`"Green-minimizer" "kernel" "Schur"`, and
`"2606.29555" github`. Nonprimary search hits were discovery leads only.
The paper was searched for positive-kernel, profile-measure, row-sum,
Green-solver and Markov terminology; the actual feature and closure
passages, rather than missing search strings, determine the comparison.
A finite endpoint positive-kernel discussion elsewhere in the source
concerns a different map and does not provide this profile representation.

Continue this particular mass mechanism only with an explicit,
independently justified profile representation and its agreement proof;
then check its sign and both essential masses against 0 and 1. No such
representation emerged in this bounded review, so park it without
claiming a negative kernel value, excess mass or actual-theta failure.
Outcome EXPLORATION: new source comparison locates missing hypotheses;
it establishes no mathematical sign or progress beyond the cited tests.
This literature turn spends no mathematical-exploration attempt and
resets no supervisor counter. Full matching/supporting Mathlib coverage
is unchecked; no cross-notebook input is used.

A different, independently formulable compact-core branch-transport
screen is nominated in
`drafts/literature/2026-11-17-compact-core-branch-compatibility-review-1266.md`.
It has its own REVIEW_REQUIRED gate and does not assume a Green solver.
The October31 direct theta/de Branges construction comparison and stop
were read narrowly for this routing decision: its conditional-positive-
data failure remains in force. The new screen proposes no positive
construction or revival of that stopped argument. Source C.1's failed
coherent, endpoint-exponential, plus-inverse and scalar branch fits
remain source-reported numerical evidence, not local certificates.
A creative main-gap attempt is not justified by the missing positive
representation or bridge; the proposed consistency screen must first
receive its exact source comparison.

## Original nomination1265 — historical, completed above


The main gap remains L030-L032/C032a. The proposed downstream use is
to pay the original source's trace-image contraction by a norm mechanism
that does not assume its conclusion. Preserve C032d's finite stop and
the unrelated L870 forcing stop at their scopes. The precise model
and measure must be extracted from
[Freedman2606.29555v1, Appendix C](https://arxiv.org/html/2606.29555v1#A3);
source grids and the disputed inference are not premises for the bound.

The proposed finite/analytic discriminator is a representation of the
actual compressed operator on its specified plus-profile image by a
nonnegative integral kernel whose row and column masses, in the exact
profile measure, are each at most one. First compare the precise
Schur-test hypotheses with what the source actually defines. A source
that assumes M<=P to construct the representation does not pay the
gap. If the operator is defined only on a proper profile subspace,
an extension and agreement on that subspace require explicit evidence.

Continue only if a primary result or explicit source formula supplies
an independently justified representation and a bounded test for the
missing sign/mass estimates. A negative kernel value or excess mass
stops that particular representation; it does not rule out every other
representation or disprove theta contraction. If no representation is
available, record the missing identity and decide whether this target
is independently testable; do not label its absence a counterexample.
Do not expand to a general discovery survey or repeat the finite audit.

Essential local input is C032d's exact inference obstruction. The main
criterion L030/L032/C032a and theta definitions L019/L024/L025 retain
their existing qualifications; they are background, not assumed signs.
Actual model identification, parameter uniformity, graph realization,
initialization and the final Xi bridge remain unresolved. No cross-
notebook input or Mathlib coverage is claimed. An eventual creative
attempt needs a real theta-specific formula and a discriminating test;
the present nomination is only source comparison, not a creative proof.
