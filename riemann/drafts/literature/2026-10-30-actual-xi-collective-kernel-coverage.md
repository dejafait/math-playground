# Actual-Xi collective kernel: completed source screen

TARGET: Source-assess an actual-Xi collective signed-kernel lower bound using horizontal-strip geometry and local zero counts, without conserved constant allocations.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the three-mechanism screen below; reused finite-allocation and count/masking assessments and searched exact Laguerre/local-count/logarithmic-derivative terms. No sufficient actual-Xi collective lower bound was identified; this is a bounded scope conclusion, not a novelty or nonexistence claim.
SOURCE_EVIDENCE: Inspected Csordas arXiv:1309.0055v2 Definition 1.1, Propositions 2.2–2.3 and their complete proofs; Bellotti–Wong arXiv:2412.15470v2 Corollary 1.6 and Section 6 increment/remainder and upper/lower cases; Maples–Rodgers arXiv:1404.3080v2 Theorem 2.4, Proposition 2.5 and Section 4 (18)–(23), reusing L485's restricted repair and prior assessment. No new theorem is imported into the argument.
COMPARISON: Interval positivity requires exclusion of nonreal centers; total local counts do not distinguish real and off-line budgets; averaged off-line counts give no pointwise signed compensation. L471 already supplies the convergent signed identity, and L486 already records the count-moment application's loss. None of these statements supplies a property excluding the recorded masking models.
GAP: No inspected displacement-sensitive actual-Xi compensation inequality yields D_1>=0 at every real height. Weighted negative mass and higher signs also remain unresolved; the source comparison does not disprove any actual-Xi positivity statement.
REASON: Park this geometry/count-only screen rather than repeat L486 or the finite audits. A newly located, theorem-unread rank-trace lead is nominated separately because it uses the actual arithmetic Hermitian form rather than the same count bounds; it is REVIEW_REQUIRED, not approved mathematics.
LITERATURE_REASON: The invocation's changed actual-Xi target had REVIEW_REQUIRED coverage; its missing geometry/count comparison required this source-only step. Existing adequate assessments were reused for their unchanged scopes.

## Original nomination, preserved as the scope of this step

The main gap is actual-Xi all-degree mixed positivity. The proposed
intermediate input is a lower bound for its collective first-Laguerre
signed zero-kernel expression using actual zero geometry/count information,
rather than assigning fixed fractions of real-zero budgets to individual
nonreal pairs. Even success at this first sign would leave higher signs,
zeros at evaluation points and full RH unresolved. No candidate solution
is claimed.

Bound the next source review to at most three quantitatively specified
geometry/count mechanisms. First search the notebook's relevant signed
allocation and finite masking assessments/failures, then inspect primary
theorem hypotheses for the best concrete lead. The initial exact inputs
are L511 (standalone audited finite obstruction) and its ready source
assessment; L510's one-pair deficit is only a contrast. Additional
canonical inputs must be identified narrowly before loading them.
No cross-notebook input is nominated.

Continue only if an inspected result yields a specific independently
testable quantitative inequality and identifies which actual-Xi property
excludes finite masking. Otherwise record an informative scope failure
or a bounded unanswered search without promoting it to ready mathematics.
Check required summation convergence, excluded centers, multiplicities,
and whether a proposed premise already assumes RH-equivalent positivity.
Do not infer a lower bound from counts alone without its exact theorem.
No new derivation or mathematical script is authorized by this nomination.

A creative proof attempt is not yet justified: L511 supplies no
geometry/unmatched-mass bridge. The source step should prepare one if
supported, rather than repeat the completed finite audit or manufacture
a creative label. Mathlib coverage is unchecked. Newly written coverage
requires the separate next-turn source review.

## Completed comparison, 30 October 2026

The main gap and downstream objective remain those in the nomination.
The intermediate threshold is the nonnegativity of L471 equation (6)
at every real nonzero Xi value, with the separate zero-safe extension
already recorded there. This is a target, not an assumption. No lower
bound has been established by this review. Only three mechanisms were
assessed; the rank-trace item below is an unread continuation lead.

### 1. Strip geometry and an interval without nonreal centers

George Csordas, *Fourier transforms of positive definite kernels and
the Riemann xi-Function*, [arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/html/1309.0055v2),
Definition 1.1 and Propositions 2.2–2.3, printed pp. 3–4.
The class has the displayed genus-one product, nonnegative Gaussian
parameter and reciprocal-square summability. Proposition 2.2 assumes
strip half-width one, f(0)!=0, and no nonreal zero centers in [A,B],
where B-A>2; it concludes L_1>=0 on [A+1,B-1]. Its proof uses
the signed reciprocal-square identity (2.3). Proposition 2.3 instead
fixes a nonvanishing remaining factor while varying a conjugate pair.
Read both complete proofs. They do not infer compensation from counts.

L471 already justifies the identity for actual Xi, its absolute/local
convergence away from zeros, equal pair multiplicities and the zero-safe
negative-part extension. Thus there is no reason to reprove that input.
The interval theorem's absent-center hypothesis has not been supplied
at the unknown heights. The existing identity does not establish it.

### 2. Pointwise local counts, including a lower bound

Chiara Bellotti and Peng-Jie Wong, *Improved estimates for the argument
and zero-counting function of the Riemann zeta-function*,
[arXiv:2412.15470v2, 7 July 2025](https://arxiv.org/html/2412.15470v2),
Corollary 1.6 and Section 6, (6.1)–(6.4) and the subsequent
large/compact-height and lower-bound cases, were inspected.
For T+1>30610046000, its stated two-sided-window lower bound is

    N(T+1)-N(T-1) >= (1/pi-0.201521) log T
      - min{0.4892 log log T+13.7861,
            3.3769 log log T+2.3884} - 1/(25(T-1)).

It also supplies upper bounds and separate computed-range estimates.
N counts all nontrivial zeros with multiplicity, not just line zeros.
Section 6 uses argument increments, the gamma remainder and the cited
argument bounds; no displacement-resolved lower bound is stated.
This is a theorem-scope inspection, not an audit of those computations
or the manuscript's constants. No new use of its constants is approved.

L467 already supplies a qualified closed-unit-shell upper bound from
the same source's Theorem 1.1. Counting zeros on both sides of a center
does not identify real-zero mass available for its signed kernel.
In particular the new-to-this-screen lower-count statement does not
assert a lower bound for a positive part of that kernel.

### 3. Actual-zeta off-line local count moments

Kenneth Maples and Brad Rodgers, *Bootstrapped zero density estimates
and a central limit theorem for the zeros of the zeta function*,
IJNT 11 (2015), 2087–2107,
[arXiv:1404.3080v2, 4 June 2016](https://arxiv.org/html/1404.3080v2),
Theorem 2.4 and Proposition 2.5, printed p. 5, give cumulative
off-line density and local count moments. For integer k>=1,
1<=H<=T^(1/4) and fixed 0<c<1/2, the latter states

    (1/T) integral_0^T |N(sigma,t+H/log T)-N(sigma,t)|^k dt
      <<_(c,k) H^k T^(-c(sigma-1/2)).

N uses beta>sigma and 0<gamma<U; retain 1/2<=sigma<=1.
Read Section 4 (18)–(23) and reused the prior restricted repair:
L485 covers only k=2,c=1/4, with full multiplicities and count-only
weights. It does not import the general-weight (19)/Lemma 4.3.
The source's proof and endpoint/normalization issues are recorded
there; no new specialization or manuscript audit is performed here.

The ready local-density assessment already covers its aggregate
application. L486 gives the normalized upper bound
C delta^(-1) exp(-delta log T/8) for its restricted nonnegative
majorant. Its recorded test at delta=log log T/log T fails to vanish;
this is an upper-bound certificate limitation, not actual negative
mass or a sharp threshold. Neither the source statement nor that
application gives pointwise collective signed positivity. The ready
weighted-count assessment additionally records that an analytic
complex-zero statistic cannot simply be read as a positive selected
count; that stopped premise is not supplied again here.

### Duplicates, failures and decision

Reused `2026-10-30-l511-critical-audit-coverage.md`, the signed-real-zero
and shared-budget assessments, `2026-09-27-count-and-positive-kernel-model.md`,
`2026-10-25-explicit-unit-shell-count-coverage.md`,
`2026-10-30-local-density-aggregate-kernel-coverage.md` and
`2026-10-30-zeta-squared-weighted-local-density.md` in this directory.
Read the relevant statements/ranges in L354, L355, L467, L471,
L485, L486 and L511 after identifying them by the local paths.
The coarse-count and positive-kernel masking stops under ATTEMPTS
are preserved, including L355's arithmetic qualification. The L486
universal-threshold stop supplies the exact repeated-calculation limit.
L511 is a finite separation result, not an actual-Xi countermodel.

Searches included `Riemann xi Laguerre inequality zeros strip local zero
counts Csordas 2014`, `Riemann zeta local zero density Laguerre inequality
sum reciprocal squared zeros unconditional`, `"Laguerre" "xi" "zero"
"density" inequality collective`, and `"xi" "logarithmic derivative"
"concavity" "zeros" unconditional`. Primary statements, not snippets,
support the three comparisons above. No cross-notebook input was used.

Outcome: NEGATIVE source-scope evidence. This completes the nominated
bounded comparison without finding its continuation criterion. There
is no new mathematical theorem, no proof that every count-based method
fails, and no RH candidate. PROOF and DAG are unchanged. Mathematical
exploration usage is zero; full matching Mathlib coverage is unchecked.

### Independently testable continuation lead, not assessed here

The search returned Alpöge–Furman,
[*More than two thirds of the zeta zeros are simple and on the critical
line*, arXiv:2608.13637v2](https://arxiv.org/abs/2608.13637v2).
Only its abstract/version record was read: it describes finite Weil-form
compression, rank-trace and inertia. Its theorem hypotheses, analytic
inputs and proof cases remain unread. No asserted proportion or
formalization is imported. The later arXiv:2610.08965 abstract was also
read solely as a related lead, not theorem evidence. Narrow local
searches for these IDs and rank-trace/finite-compression terms found no
assessment in the checked literature/failure paths; that is not novelty.

The separate rank-trace nomination asks whether the exact source
inequality can detect a single off-line pair in a height-localized
compression without assuming Weil positivity. This changes the input
from counts to an arithmetic Hermitian form. Continue only after
inspecting a sufficient quantitative statement and all positivity,
support, localization and error hypotheses; otherwise park this lead.
No creative proof attempt is ready until that missing source comparison.
