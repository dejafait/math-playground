# One-coordinate theta marginal — completed source comparison

TARGET: Test whether the one-coordinate marginal J_2(u,v)=integral_0^infinity A(w) Psi_tilde_2(u,v,w)dw of L969 is nonnegative for all u,v>0, retaining the actual normalization and every signed term.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step179 searched the exact Li/theta marginal, conditional-expectation and signed-kernel terminology; searched November10 Li/theta/profile assessments, histories and stops for J_2, Psi_tilde_2, marginal and one-coordinate. Only the nomination and prior full-kernel failures matched locally; no inspected external theorem determines this marginal sign. Reused step167/175/177 coverage without repeating its searches. No novelty inference.
SOURCE_EVIDENCE: Oudghiri, arXiv:2012.08808v2 (16December2021), Section3/Theorem3 pp5-7 including the continuous proof in Section3.2; official Mathlib Integral.Prod statements MeasureTheory.integral_prod and integral_integral_swap, and ConditionalExpectation.Basic statement MeasureTheory.condExp_nonneg, retrieved10November2026. Read L019, L966 hypotheses/(1)-(4), L967(1)-(8), L969(1)-(8) and its absolute-integration proof, plus step168/176/158 stop records. Prior probability/normalization and calculus assessments reused as scoped below.
COMPARISON: Absolute Fubini covers the averaging operation once integrability is checked; conditional-expectation positivity requires an already nonnegative input. Oudghiri requires independent log-concave densities and specified weighted coordinate monotonicity, and concludes monotonicity given a sum, not positivity of this fixed-coordinate average. Those additional hypotheses and a sign anchor are not established. Full-kernel negatives do not decide its marginal; no known sign is imported.
GAP: Compute and check the complete exact marginal in a later research turn, then prove a global sign or a rigorously negative value/region with the actual moments and normalization. A finite positive grid is insufficient. The final integrated sign and all-index L966(16) remain unresolved even if this pointwise marginal test fails.
REASON: Approve one bounded attempt at the unchanged TARGET. Exact one-coordinate averaging is a distinct payment test after the audited full-kernel stop; no essential source is inaccessible and no inspected theorem makes the test redundant. This review supplies scope and tools only, not a marginal formula or sign result.
LITERATURE_REASON: The nominated marginal observable was REVIEW_REQUIRED at invocation and lies outside the ready full-kernel audit/profile assessments. This separate literature-only step completes its changed-observable comparison; further literature on the unchanged target requires a new essential lead or hypothesis.
SCOPE: Only n=2,b=1/4,h=5184,q=72, actual A,H_r,c_0,c_1 and gamma=1/[2(c_0+c_1)], and complete L969(5); integrate exactly one coordinate against A(w)dw, retaining normalized symmetrization, every sign and the h-origin/derivative. No profile tuning, general-n extension, numerical normalization premise, RH or simplicity assumption.

## Completed comparison — step179

This completed review supersedes the nomination's readiness status
and prospective literature instructions preserved below.
The main gap remains L030-L032/C032a actual-Xi mixed positivity;
this route needs all-index L966(16), R_n<=N_n. The intermediate
target is exactly TARGET above. A nonnegative marginal would support
the n=2 integrated inequality and motivate a separately assessed
higher-order mechanism. It would leave all other indices unpaid.
A rigorously negative marginal point or asymptotic region abandons
this two-variable pointwise payment test, without signing the final
double integral. This turn derives no new mathematical result.

### Inspected primary hypotheses and limits

**Integration.** Official [Mathlib Integral.Prod](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Prod.html#MeasureTheory.integral_prod),
retrieved 10 November 2026: `MeasureTheory.integral_prod` identifies
the product integral with the iterated integral for an integrable
function on two measurable spaces with S-finite measures; the target
is real-valued. `MeasureTheory.integral_integral_swap` has the same
integrability and S-finiteness requirements. These are supporting
Fubini results, not inequalities. L969 already proves absolute
integrability term by term using L019's decay and bounds on its
finitely many factors. Reuse that proof and its exact single-factor
integrals; do not redo the boundary transfer. For a sign at every
u,v, check every fixed-coordinate slice, since a general Fubini
statement alone gives slice integrability only almost everywhere.
No marginal expansion is performed in this review.

**Positive conditional expectation.** Official [Mathlib
ConditionalExpectation.Basic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/ConditionalExpectation/Basic.html#MeasureTheory.condExp_nonneg),
same retrieval date: `MeasureTheory.condExp_nonneg` requires
almost-everywhere nonnegativity of its real input and concludes
almost-everywhere nonnegativity of the conditional expectation.
For its probabilistic meaning use an integrable input, a sub-sigma-
algebra and a measure sigma-finite on that sub-sigma-algebra; Mathlib
uses zero by convention when these conditions fail. L969's negative
open set prevents using this as an automatic positivity argument for
the full kernel. It does not preclude positivity of a particular
average. No identification of a conditional expectation, normalized
law or all-point sign is asserted here.

**Conditional monotonicity.** Oudghiri, [*Generalizations of Efron's
theorem*](https://arxiv.org/pdf/2012.08808v2), v2, Section3/Theorem3 p5,
Section3.2 proof pp6-7.
For independent real X,Y with log-concave densities, a>=0 and
measurable phi, require x->exp(-ax)phi(x,y) and
y->exp(-ay)phi(x,y) nondecreasing for every fixed other argument.
When Phi(s)=E[phi(X,Y)|X+Y=s] is well defined, the conclusion is
monotonicity of exp(-as)Phi(s). The proof applies Efron's theorem
to exp(-a(X+Y))phi and pulls out exp(-as). The TARGET fixes u,v
and integrates w; neither these shape hypotheses nor a sign anchor
is established. No theorem is imported. Efron1965 remains a
bibliographic lead, not an inspected primary theorem or input.

### Reuse, duplicate checks and failures

Reuse the source comparisons in
`2026-11-10-li-theta-ibp-remainder-review-166.md`,
`2026-11-10-h-derivative-boundary-profile-review-174.md`, and
`2026-11-10-h-derivative-profile-audit-review-176.md`.
They already cover DLMF transfer/endpoints, the specific
Biane-Pitman-Yor theta laws/cumulants and Patil-Rao nonnegative
weight normalization. The strongest relevant checked conclusions
there concern known transfer methods, normalization, particular
size-bias identities and the first two ordinary Li signs. None
signs the new h-dependent marginal. Their optional damaged/unread
mean-comparison and Coffey leads are not essential sources for
exact finite-factor integration; do not reopen them merely to wait.

The exact local searches found no completed J_2 calculation or
matching marginal sign test in the named Li/theta records. L967's
old-profile ray and L969's derivative-profile diagonal, with their
step168/176 ATTEMPTS records, remain valid full-kernel obstructions.
The latter's instruction to retire the profile records the failed
pointwise rule; it is not evidence about averaging a coordinate.
The step158 finite-Li-index/mixed-degree import stop remains separate.
This target retains the prescribed observable and does not relabel
ordinary Li signs as its sign. No cross-notebook theorem is used.

External queries were `"Riemann" "Li" "theta" "marginal" positivity`,
`"theta kernel" "conditional expectation" positivity`,
`"signed kernel" marginal positivity integration`,
`"Li coefficients" "marginal" theta kernel`,
`"Riemann" "theta" "one-coordinate" positivity`, and Efron1965
Polya-frequency/conditional-expectation theorem/PDF searches.
Unrelated search hits, abstracts and snippets were not theorem evidence.
This bounded comparison found no inspected sufficient sign result;
it establishes neither nonexistence of such a theorem nor originality.

### Bounded continuation and qualifications

The unchanged TARGET is ready for one research attempt. Start from
complete L969(5); use its exact factor integrals and normalizations
to integrate one coordinate, checking repeated-factor permutation
multiplicities and the entire h subtraction. Justify each slice
and any subsequent limiting operation before drawing a sign.
Seek global nonnegativity or a proved negative point/region; a grid
is diagnostic only. If an actual moment bound is load-bearing,
prove or rigorously certify it rather than substituting a floating-
point gamma. Save incomplete reasoning and its exact unpaid inequality
if neither threshold is met; do not tune a profile or generalize n.

Essential inputs are L019, L966, L967 and audited L969, with the
L018/L024/L026 framework inherited. L968 supplies only downstream
all-index sufficiency. The marginal sign, any needed actual moment
inequality and all-n positivity remain open. Supporting Mathlib
Fubini/conditional-positivity statements above were checked; full
matching Mathlib coverage for this marginal sign is unknown.
No mathematical lemma, script, DAG edge or PROOF argument changes.

Outcome EXPLORATION, kind LITERATURE, classification NOVELTY_UNCHECKED.
Next routing is proof_attempt/creative: test exact averaging as a
new payment mechanism at the sign gap; the bounded discriminator is
the unchanged all-u,v marginal sign, or a rigorously negative value.
This is permission to attempt the missing inequality, not approval
of an unseen mathematical conclusion. A new ready continuation does
not invalidate step178's completed audit or this source review.

## Original nomination — step178, preserved

## Precise scope for the separate review

Keep n=2, b=1/4, h=5184, q=72, and gamma=1/[2(c_0+c_1)]
with the actual theta integrals. Psi_tilde_2 means the complete L969(5),
including the even-block subtraction, the h-origin and the full C_1.
The new operation integrates exactly one coordinate against A(w)dw;
it neither changes the profile nor drops a negative region. No formula
for J_2 and no claim about its sign is derived or approved here.

The main gap remains L030-L032/C032a and the all-index L966(16)
comparison. The proposed intermediate target asks whether one actual
integration can pay the cancellation that a full-kernel pointwise
certificate cannot. A global nonnegative marginal would support the
n=2 integrated comparison and motivate a separately assessed higher-
order mechanism. This finite-order result alone would not approach
all-n closure without additional input. A rigorously negative marginal
point or asymptotic region would retire this two-variable pointwise
test without assigning a sign to the final double integral.

The review should first compare the exact operation with the ready
calculus/weighted-normalization assessments and inspect relevant known
conditional-integral sign hypotheses. Search narrowly for this marginal
and equivalent terminology in local Li/theta records and primary sources.
Record any known overlap instead of reproducing it as a discovery.
The old blocked optional probability sources are not presumed essential;
identify an exact needed theorem before reopening a source blocker.

Continue to one bounded mathematical test only after IMPORT, SPECIALIZE
or EXPLORE coverage is saved in a separate turn. Do not reopen the
failed full-kernel pointwise rule or derive and approve this target in
the same turn. Global nonnegativity is the positive threshold; a proved
negative point is the abandonment threshold. A sample grid alone cannot
meet either threshold. No new kernel family or all-n generalization is
included in this target.

Essential inputs: L019 for A and decay, L966 for the observable and
integrated comparison, L967 for the complete transfer, L969 for the
audited replaced kernel. L018/L024/L026 are inherited; L968 is downstream
sufficiency only. No RH, simplicity, positive Stieltjes representation,
effective gamma bound, uniform onset or cross-notebook theorem is assumed.
The sign of J_2, actual moment inequalities and all-index positivity are
unresolved. Full matching Mathlib coverage is unknown.

The next invocation is literature_comparison, standard/high. The reason
for source work is the changed marginal observable outside the prior
fixed-profile audit scope, not a repeated review of an already ready
target. Step178's completed audit remains accepted independently of
this new nomination.
