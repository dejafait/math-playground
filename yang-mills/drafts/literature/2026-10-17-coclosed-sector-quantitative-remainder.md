# Co-closed rough sector — quantitative source comparison

TARGET: Assess whether L090's complete co-closed/co-closed rough-sector trace T_hh is O(N^(5/2) log(eN)^2) for both actual probes.
CHECKED: 2026-10-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Read L090 in full, L089 through its complete remainder estimate, L088's actual trace and heat bounds, history/116 and the original regularization continuation; checked the broad quantitative and original other/other assessments and ATTEMPTS/030. Exact-sector, finite-trace and sparse-matrix queries below found no inspected matching rate theorem.
SOURCE_EVIDENCE: Reuse the recorded Adams--Lee and flow/Ward comparisons; inspect Benzi--Simoncini arXiv:1501.07376v1, section 3 (3.1)--(3.2), Theorem 4.2 with both proof cases, Theorem 4.4 (4.1), and section 5, printed pp. 5--8 and 11--12. Benzi--Razouk and the original Demko PDF remain optional unread leads after retrieval failures.
COMPARISON: L089 already supplies O(N^2 sqrt(log(eN))) for T_hh-T_red. L090 supplies the reduced trace's zero cubic limit but no joint rate. The inspected matrix-decay results concern individual matrix functions, not this signed trace with variable coefficients and all heat modes; no complete rate can be imported.
GAP: Quantify the reduced trace's resolvent, projection, localization, coefficient-freezing and collar errors jointly at O(N^(5/2) log(eN)^2), or establish a specific obstruction to that transfer. In particular L090(16) and section 4 retain fixed-parameter constants.
REASON: Essential source comparison is complete for one bounded quantitative-transfer attempt; no adequate matching theorem was found in this search, with no novelty or global absence claim. No rate, parameter schedule or new lemma is established here.
LITERATURE_REASON: The requested quantitative bound changes the hypotheses beyond the completed cubic-limit coverage. This turn assesses that change and reuses the ready complete-coefficient and flow/Ward comparisons.
SCOPE: SU(2) relative all-face cube, straight lower-rooted direction-1 forest, admitted even N, a=8/N, tau=1/16, actual probes i=3,6, fixed-mesh-first bare expansion; no complete-response or interacting rate claim.

The main gap is interacting cutoff removal with reflected error
<=c_box/2, then continuum axioms and finite positive mass. A rate for
this one complete rough sector could support quantitative assembly after
L220's qualitative cancellation. Other component rates and interacting
control remain independent gaps. This review approves exploration of
the stated target, not its conclusion.

Essential IDs from L090's DAG row: L003 L009 L018 L026 L028 L085 L086
L088 L089. Keep T_hh distinct from its reduced T_red: L090(1) covers
both, while L089 supplies exterior-circulation and curvature-form errors.
The detailed comparison below records the inspected ranges. Existing
analytic inputs are imported, without recursively auditing their proofs.

Retain both generator orientations, actual signed trace order, every
axial level and end row, coincident plaquettes, upper jumps, constant
modes, both residual subtractions and the complete external heat sum.
No smooth upper extension, commuting variable multiplier, positive
residual or uniform mass-removal rate is assumed. Do not use a varying
mass in a fixed-mass limit without uniform error. Analytic input results
remain imported; Mathlib coverage for this rate is not checked.

## Local proof coverage and recorded failures

L088(1), (4)--(6) fixes the complete sector, the symmetric actual-probe
heat expansion and its summable polynomial envelope. L089(1)--(4)
defines the reduced generator trace and bounds its difference from the
complete sector; its proof sections 1--3 retain every exterior-circulation
placement and both curvature-form subtractions. That stated difference
is already below the requested threshold. This is reuse of its existing
conclusion, not a new improvement.

L090 was read in full. Its derivative/collar bounds (6)--(12) explicitly
retain staggered jumps and give low-spectrum and resolvent errors before
the mesh limsup. Equation (13) displays eta and epsilon but has discarded
the finite-N boundary term on taking that limsup. Equations (14)--(16)
regularize the transverse projection only after the covariance, with
a constant depending on epsilon. Equation (17) is an explicit geometric
polynomial approximation, not a uniform bound on the subsequent trace's
coefficient-freezing error as its degree grows. Section 4 controls the
collar and freezing only at fixed degrees; (18)--(21) cancels the frozen
trace exactly. Section 5 removes all parameters successively.

Consequently no particular varying-mass/degree schedule is justified by
the stated qualitative conclusion. A later attempt may return to these
finite inequalities and track their constants, but that tracking is the
unproved mathematical task. No parameter optimization is performed here.
L221--L224 concern different expressions; their rates are not inputs for
this trace merely because they concern the same probes.

The original assessment, history/116 and
`drafts/2026-10-10-other-other-co-closed-regularization.md` already cover
the qualitative cancellation. No duplicate quantitative result was found
in these targeted records or the pending assessment search. Repeating
that cancellation would not be a quantitative advance. ATTEMPTS/030
records a different transverse-H trace's failed use of fixed-mass limits
at varying mass. Its lesson applies to limit order here, without importing
its trace estimate or globally banning regularization. L090's two local
co-closed rough lines and quantitative derivative bounds distinguish the
proposed test from that exhausted shortcut.

## Primary source scope

M. Benzi and V. Simoncini, *Decay bounds for functions of matrices with
banded or Kronecker structure*,
[arXiv:1501.07376v1](https://arxiv.org/pdf/1501.07376v1),
29 January 2015, printed pp. 5--8 and 11--12. Theorem 4.2 assumes banded
Hermitian positive semidefinite M, spectrum in [0,4rho], and gives
regime-dependent Gaussian/superexponential heat decay. Both proof cases
use polynomial propagation and Krylov error bounds. Theorem 4.4 integrates
these bounds for positive definite M and Laplace--Stieltjes functions,
retaining its smallest eigenvalue. Section 5 uses graph distance; uniform
finite-section estimates require bounded spectrum and analyticity near
it. Section 3 (3.1) records conditioning-dependent inverse decay, citing
Demko--Moss--Smith; that original theorem was not read.

Applicability comparison: L090's component Laplacians are finite real
symmetric sparse matrices with the indicated relative end rows. Massive
inverses are appropriate candidates for these tools. Their unregularized
versions have N-dependent small eigenvalues; zero-mass uniform constants
are not supplied. The projection has incidence factors on both sides of
a vertex inverse, and the complete expression has intervening variable
multipliers. Thus a single-function entry bound does not settle the
signed trace or its heat-summed error. Applying such a bound locally,
including graph components and the correct pinned stencil, would require
an explicit applicability argument in the research attempt. No reproof
of the general decay theorem is warranted; the unresolved work is the
specific trace estimate.

Reuse the primary Adams--Lee Appendix A comparison in
`2026-10-17-complete-coefficient-quantitative-remainder.md` and the
flow/Ward comparison in
`2026-10-10-other-other-cubic-leading-scale.md`. Their unchanged scope
does not cover the actual pinned, spatially varying bare sector rate.
They are not reread or promoted to new inputs in this review.

Optional retrieval leads: Benzi--Razouk, ETNA 28 (2007--2008), pp. 16--39,
and Demko--Moss--Smith, Math. Comp. 43 (1984), pp. 491--499. Publisher
PDF fetches failed; searches and abstracts do not count as theorem reads.
The accessible primary Benzi--Simoncini paper supplies the inspected
localization comparison, so neither unread original is an essential
premise and no dependent theorem is left SOURCE_BLOCKED.

Queries on 2026-10-18 included:

- `"co-closed" "trace" "lattice" "remainder"`
- `"finite volume" "lattice" "trace" "frozen" "cancellation" rate`
- `"sparse matrices" "trace" "variable coefficients" "decay" resolvent`
- `Benzi Razouk decay bounds functions sparse matrices theorem 3.4 2007 pdf`
- `Demko Moss Smith decay rates inverses band matrices 1984 theorem 2.4 pdf`
- `lattice perturbation theory finite volume position dependent coefficients power counting Reisz theorem boundary`

Other search hits are unread leads, not evidence of theorem coverage.
Failure to find a matching theorem is not evidence of novelty.

## Bounded continuation and decision

EXPLORE covers exactly the TARGET above in the existing SCOPE. The next
attempt should expose the N, epsilon, delta and localization-range
dependence in L090's original two-orientation trace, then test whether
their combined absolute errors reach the requested threshold. Retain
L089's complete-sector remainder and the full polynomial heat envelope.
An alternative signed regrouping within this same reduced trace needs
its own proof; changing the trace or hypotheses needs a source review.

Continue for a justified uniform rate or a new quantitative estimate
that reduces the remaining rate gap. Stop this transfer if an explicit
parameter-dependent estimate cannot meet the threshold, and record the
precise loss before selecting a materially different mechanism. A coarse
upper bound is neither signed growth nor a disproof of the target.
This test does not assume that a feasible schedule exists. Boundary,
projection and localization estimates remain unresolved obligations.

Essential continuation IDs are L003 L009 L018 L026 L028 L085 L086
L088 L089 L090. Keep both actual probes, generator orientations, residual
subtractions, all axial levels, coincident plaquettes, normal end rows,
upper jumps, constant modes and heat sums. No coefficient commutation,
positive residual, smooth upper extension or varying-mass limit theorem
is assumed. Independent complete-response rates, interacting control,
continuum axioms and finite positive mass remain open. Mathlib coverage
for the full rate and supporting decay theorems is **not checked**.

Completed step: LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. The new
evidence is a primary localization comparison and an exact list of
unquantified trace estimates, not a new bound. No lemma, mathematical
script, proof assembly or DAG change is made. This newly completed
assessment receives separate next-turn approval before research; it
does not authorize deriving and approving uncovered mathematics here.
