# Coverage: lower-band relative Mellin comparison

TARGET: Attempt to extend L454's conditional relative Mellin comparison to 7/8≤m/r≤31/32, retaining the full sum, both residues, complete tails and non-Euler lower bound under the same pinned premise.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-sum Riesz/Perron searches and failure screen in L454's ready assessment; searched fixed-half-plane Littlewood/logarithmic-derivative terminology and logarithmic Riesz zeta products for the changed band. Read L454 in full, L452 through its interpolation/Cauchy proof, L303/L330 and the exact L323/L327/L335 contrasts; no matching full-band theorem was identified in the inspected sources.
SOURCE_EVIDENCE: Reused the pinned September 30 Theorem 1.1 and inspected DLMF inversion, meromorphy and Stirling coverage. Retrieved Titchmarsh–Heath-Brown (1986), Sections 14.1–14.3, and inspected Theorems 14.4–14.5 with their relevant proof cases, printed pp. 340–342; newly read Simonič (2023), Theorem 1, Theorem 4 proof and Corollary 4 Cauchy step, and Appendix Theorems 6–7. Exact applicability limits below.
COMPARISON: L452's stated strip does not cover the whole proposed domain. The printed RH/local-GRH derivative estimates cannot be imported from the weaker pinned premise. The inspected interpolation, Cauchy and contour mechanisms cover a bounded specialization attempt, including a negative threshold verdict; they do not establish the changed-band comparison or its endpoint.
GAP: First test whether a correctly normalized logarithm on the complete changed domain, with reserved complex neighborhoods, yields local derivative magnitude o(sqrt(r)) uniformly including m/r=7/8. If it does, prove a non-Euler square lower bound, both residues and every relative tail; if it does not, record the exact failed bound rather than assert freezing. No such specialization is proved here.
REASON: Essential source mechanisms are accessible and compared; the unresolved estimate is a mathematical obligation, not an inaccessible source. SPECIALIZE authorizes one bounded known-method attempt, with the lower endpoint as its first discriminating test and no promised success.
SCOPE: The exact TARGET for positive real r, positive even m, h=9/2+m/(2r), a=sqrt(4π²exp(4r)−h²)>0 and 7/8≤m/r≤31/32; arithmetic comparison and its threshold test only, without theta-sector extension, sign assembly or external-proof audit.
LITERATURE_REASON: The proposed band falls outside L454's audited analytic domain; review that changed hypothesis rather than repeat the completed C455b audit.

## Initial proposal record

The following paragraphs record the scope before this source review;
the completed decision and current authorization are below.

The main gap remains the initial low-index segment and global mixed
positivity. This arithmetic target could supply one input to a later
lower-index sign theorem. Matching theta-sector estimates and an
every-height transfer would remain independent tasks, as would the
initial segment and bounded exterior heights. No extension is claimed.

Review L454's full sum and contour identity, L452's actual logarithm
and derivative domains, and the L303/L330 inversion and relative-variation
mechanisms already cited there. Retain OpenAI's September 30, 2026
[Theorem 1.1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, with its strict
half-plane, allowed pole and unaudited manuscript/import closure.

Reuse [L454's assessment](2026-10-23-subendpoint-relative-mellin-coverage.md)
and [audit coverage](2026-10-23-subendpoint-relative-mellin-critical-audit-coverage.md)
where their inspected primary hypotheses and proof cases still apply.
First compare the needed logarithmic-variation scale on the proposed
band with the actual source bounds, including reserved complex
neighborhoods. Do not apply L452's old conclusion outside its domain.
Then check whether the residue and complete-tail mechanisms require
additional essential coverage. No such derivation or approval was
performed in this C455b audit turn.

The eventual test would be uniform S/B=1+o(1), with
B=|ζ((1+m/r)/2+ia)|² nonzero and a justified lower bound, at the
exact coupled height beyond one real-r onset. A vanishing complete
relative error would justify pursuing the independent sector estimate.
If the assessed tools fail this threshold, record the precise obstruction
and park that implementation without claiming a negative sum. The next
turn is the coverage review, not this mathematical test.

L323's strip-modulus failure, L327's phase-uniform PSD obstruction and
fixed-r negative-phase examples remain in force on their stated domains.
The scoped screen located no approved lower-band continuation in the
checked records; it establishes neither originality nor an exhaustive
absence of other results. Full matching Mathlib coverage is unchecked.

## Completed source review — 2026-10-23

This invocation is literature-only. It establishes coverage for a
bounded attempt, not the target comparison or a new analytic bound.
The exact TARGET is retained, including its closed lower endpoint;
no smaller band is silently substituted. Classify the next known-method
attempt as REPRODUCTION. The newly ready assessment receives separate
supervisor approval next turn before mathematical work.

The main gap is the unproved initial low-index segment and global
mixed positivity. The intermediate target is uniform S/B=1+o(1),
where S is L454's full finite sum at exponent m and
B=|ζ((1+m/r)/2+ia)|², on the proposed band. A successful input could
support a separately assessed theta-sector reduction and then a lower
Laguerre sign band. Those sector estimates, every-height passage,
smaller indices and bounded exterior heights remain independent gaps.

### Primary-source comparison

Reuse the [Littlewood assessment](2026-10-21-fixed-half-plane-endpoint-derivative-review.md)
and [L454 attempt assessment](2026-10-23-subendpoint-relative-mellin-coverage.md)
for their unchanged inspected inputs. Fresh retrieval of
[Titchmarsh–Heath-Brown, second edition (1986)](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=173)
confirms the RH hypothesis in Section 14.1. Theorem 14.2 and Section
14.3 use logarithm interpolation and Cauchy transfer. Theorems
14.4–14.5, printed pp. 340–342, improve the fixed-strip estimates:
under RH, ζ′/ζ=O((log t)^(2−2σ)) and
log ζ=O((log t)^(2−2σ)/log log t), uniformly on each fixed compact
subinterval of (1/2,1). Their proof uses a smoothed von Mangoldt sum
and the zero contribution on the critical line. That zero-location
case is unavailable under the pinned premise. Neither this stronger
bound nor its logarithmic saving is imported on a changed half-plane.

New primary comparison:
[Aleksander Simonič, *Estimates for L-functions in the Critical Strip
Under GRH with Effective Applications*, Mediterr. J. Math. 20, 87
(2023), DOI 10.1007/s00009-023-02289-2](https://doi.org/10.1007/s00009-023-02289-2).
Theorem 1 assumes a Selberg-class function with polynomial Euler
product and local nonvanishing throughout Re z>1/2 in a window of
width C₃ log log(c(|t|+1))+3. It bounds log L and L′/L by the power
(log(c|t|))^(2(1−σ)), with respective log-log factors of powers one
and two, on its stated moving strip. This local-GRH premise is still
stronger than the pinned half-plane. Theorem 4's proof and Corollary
4's Cauchy step were read; Appendix Theorems 6–7 state the standard
Borel–Caratheodory and three-circles inequalities. Only those general
mechanisms are reusable here. No rescaled function is asserted to
satisfy the theorem's Selberg-class hypotheses.

The modern theorem's conclusion is thus a comparison, not an input
on the proposed band. Its proof inspection also shows why a
neighborhood and the Cauchy radius must be budgeted explicitly;
the target derivative cannot be replaced by a bound for log|ζ|.
The book's sharper RH cases are inspected alternatives, not essential
unread sources or authorization to assume RH. No inaccessible primary
source blocks the bounded test below.

### Domain and complete-error obligations

The proposed real parts are σ∈[15/16,63/64] and
c=m/(2r)∈[7/16,31/64]. L452 (1) only asserts its derivative bound
for σ≥63/64; even its larger analytic-log disk in proof (8) does
not cover this whole interval. These are source/domain comparisons,
not a newly proved logarithmic estimate. Its elementary growth formula
(4), analytic-branch normalization and interpolation organization may
be reused as mechanisms, with every changed constant rechecked.

First construct or test new disks using the strict boundary 7/8 and
an inner disk entirely in Re s>1. Reserve an actual Cauchy
neighborhood around every required point and both shifted positive
heights, with height-uniform constants. Compute the interpolation
exponent and any radius/logarithmic losses before trying the rest of
the proof. A bound with a fixed exponent strictly below 1/2 would
meet L330's sufficient scale on log a=2r+O(1); another bound must
be compared to that scale explicitly. No such exponent, endpoint
little-o estimate or optimized-radius obstruction is derived here.
The closed endpoint must be checked, even if an interior interval
works. This is the first bounded mathematical test of the saved target.

If that test passes, the [DLMF inputs already inspected for
L454](2026-10-23-subendpoint-relative-mellin-coverage.md#exact-primary-inputs-and-reuse-limits)
remain relevant: 1.14.20 for scalar inversion, 25.2(i)/25.2.4 for
meromorphy and the unit pole residue, and 5.11.3/5.11(ii) for
positive-real Stirling with error. Read L454's complete contour and
tail proof against those hypotheses. The changed c interval is compact
in (0,1/2), and σ stays a fixed distance from the pole at height zero;
these observations identify what must be verified, not a uniform
tail theorem on the new band.

Retain the full sum, m!/(2r)^m, both poles z=1/2±ia and
the exact signed kernel integral. Establish horizontal-edge limits
at fixed parameters before uniform bounds. Seek the new non-Euler
upper and lower modulus estimates from the normalized analytic
logarithm. Compare the central relative variation, the whole fixed-window
complement through |v|≤a/2, the unbounded |v|>a/2 region
(including v=±a), and both residues to the same B. No Euler or
reciprocal Dirichlet series is licensed at σ<1, and the factors are
conjugate only at v=0. No residue or tail is omitted by this approval.

Continue toward the independent sector target only after a uniform
complete relative error tending to zero and one real-r onset are
proved. Stop the tested implementation if its complete-domain
variation bound cannot meet that threshold, or any relative tail or
residue remains uncontrolled. Record achieved versus required bounds;
neither a failed certificate nor L330's sharpness model proves an
actual negative sum. An interior-only estimate is a weakening and
must not be reported as the full closed-band target.

### Duplicate and failure checks; limits

The supplied overview/DAG and local L454/audit records contain the
old band, not this extension. Read L303, L330 and the relevant L452
proof in full through the specialization. L304's recorded
coefficientwise failure and L330's nonvanishing conjugate-paired model
show why localization and an O(sqrt(r)) bound alone do not justify
relative freezing. L335's negative values keep r fixed or change prime
phases; those quantifiers are not the coupled-height target. L323's
strip-modulus failure and L327's non-PSD/AFE obstruction concern
m/r=3/4 and different implementations; their hypotheses were read
and are preserved, rather than extended to a new band. None supplies
the desired actual-zeta bound or globally bans further arithmetic work.

Additional bounded queries were: `zeta zero free half plane alpha
logarithmic derivative Littlewood bound log t power 1 sigma 1 alpha`;
`Littlewood Riemann hypothesis logarithmic derivative zeta sigma three
quarters sqrt log t bound`; `"logarithmic derivative" "Riemann
hypothesis" "three" "Littlewood" bound`; `"logarithmic derivative"
"zero-free half-plane" zeta`; and `"logarithmic Riesz" "zeta"
product Mellin`. They identified the inspected Simonič paper but no
inspected theorem matching S/B on this coupled band. Search snippets,
unread adjacent Riesz-mean papers and unrelated search results are not
theorem evidence. This search and the reused exact-sum screen do not
establish originality or exhaustive absence.

Essential continuation inputs are L454, L452, L303 and L330, with
the same pinned September 30 Theorem 1.1 and the register's strict
half-plane, allowed pole and unaudited manuscript/import closure.
Do not silently substitute Liu's stronger boundary or a local-GRH
premise. Matching Mathlib coverage for the full target and the new
interpolation specialization is unchecked; no absence is asserted.
No lemma, mathematical script, DAG edge or assembled argument changes
in this source review. Outcome EXPLORATION: new source comparison and
a concrete test, with no established lower-band mathematical result.
