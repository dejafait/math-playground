# Finite-phase bound — audit continuation using existing source coverage

TARGET: Independently audit L951's uniform bound h_r(s)>=s^2/512 and its twelve-coordinate constrained-simplex transfer on 8<=E<=48.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse assessment97's exact scalar target, its completed step98 approval, and assessment96's exact-object/finite-Laplace/duplicate/failure comparison. The audit concerns the same function, range and finite-sum transfer; no broader statement or fresh search is asserted.
SOURCE_EVIDENCE: Reuse NIST DLMF https://dlmf.nist.gov/1.4#E35 through E37, with C^(n+1) interval hypotheses inspected in step98; L939(10)-(14) fixes the phase and coordinate map. The primary source is not reopened in step99 because its scope is unchanged. L951 uses only the exponential's integral/Lagrange Taylor remainders and elementary finite algebra, not a general Laplace error theorem.
COMPARISON: Previously inspected Taylor formulas cover the proposed audit tools. L951's explicit 1/512 constant, exact seventh-degree lower bounds, endpoint substitution and twelve-coordinate domain transfer are concrete applicability claims to check, not conclusions supplied automatically by the source. L940 and L950 address different stopped mechanisms.
GAP: Separate independent verification of L951 remains pending. No new source theorem is required for this unchanged scalar mathematics; no signed-amplitude or mass estimate is covered by this audit.
REASON: Step100 completes the separate literature approval for the unchanged audit using assessment97 and step98 primary-source coverage. SPECIALIZE is ready for exactly TARGET. This approval supplies no mathematical audit verdict and authorizes no extension.
SCOPE: Exactly TARGET. Check the full analytic argument and exact arithmetic, including r=sqrt(2/3), r=1, r=2, s=-r, s=0, s=11r and simplex faces. No constant optimization, wider energy interval, signed-budget calculation, compact extension or new lemma is authorized by this scope. Full/supporting Mathlib coverage remains unchecked.

The relevant theorem is Taylor's formula with integral remainder for
v -> exp(2r tau v) on [0,1], and its seventh-degree Lagrange version
for exp(-b). Both functions are smooth on the stated finite intervals.
The independent audit must verify their exact use rather than infer
the scalar inequality from smoothness. Reuse the source hypotheses
already inspected in assessment97, step98; no repeated browsing is
needed absent a concrete missing hypothesis or changed scope.

Read the complete canonical L951 proof and its small rational check.
In particular verify the sign of the eighth-order remainder, both
rational gaps, monotonicity of delta(r), the r<=1/r>=1 split,
the positive-coordinate comparison, and the absence of division by
zero. Verify that the square-root endpoint is handled by substitution
and that each constrained coordinate is at most 11r. The script's
success is only evidence for finite arithmetic, not for these analytic
claims. Its complete certificate is
`scripts/heat/l951-balanced-phase-rational-check-99.json`.

The bound uses L939's phase and exact coordinate map. L938 supplies
the surrounding signed-integral interpretation through L939; no
L037 numerical contract or independent L019/L058 reproof enters the
scalar estimate. L947/L949 are budget context only, and L940/L950
are contrasts, not premises. No cross-notebook input is needed.

Accept only after checking the full closed-domain bound and transfer,
or record a specific error and its effect on the constant or domain.
A successful audit would clear one localization input for later use;
it would not pay m-B. Signed-amplitude/local errors, local-ball fit,
full-theta/boundary mass, effective infinite join, head/global variation,
other signs/degrees, contacts, initialization and realization remain
independent of this continuation. Main L030–L032/C032a all-degree
mixed positivity stays open. No central creative mechanism is inferred
from this elementary specialization.

## Separate source approval — step100, 9 November 2026

LITERATURE_REASON: The supervisor requires separate approval of the
new step99 continuation. This review compares the saved audit scope
with the completed source coverage; it does not repeat external searches
or execute the audit. Reuse is justified because the function, parameter
range, Taylor tools and finite-coordinate transfer are unchanged.

Read the complete canonical L951 to identify its actual imported tools,
assessment97 including step98's primary-source hypothesis inspection,
the source and search sections of assessment96, L939(10)-(14), and the
L940/L950 hypotheses and conclusions. No external source was reopened;
the previously inspected primary statements remain the evidence.
The exact-object and stronger-result search record in assessment96 is
reused, not represented as a new search or an originality finding.

The only general analytic import needed for this audit is NIST DLMF,
Section1.4, Taylor's theorem, equations1.4.35-37, as inspected on
9 November 2026 in step98: the function is C^(n+1) on the closed
interval, with the stated integral and Lagrange remainders. L951 cites
this source for its first-order integral identity and degree-seven
exponential remainder. Its first-order exponential lower bound also
uses this same tool. The proposed applications concern exponentials
of linear real maps on finite intervals. The future audit must check
the order, variable, sign and prefactors in every application, rather
than assume that this source proves L951's displayed identities.
No general convexity or Laplace theorem is required by this proof.

L951's square-root substitution, exact rational comparisons, two
parameter cases, scalar-to-simplex transfer and energy correspondence
are local applicability claims. Their verification is precisely the
approved research task, not an additional unassessed lemma. The
existing rational certificate is evidence to inspect during that task;
it was not executed or certified in this literature turn. No assertion
here independently validates the constant, coordinate inequalities,
closed endpoints, or uniqueness consequence.

The scope excludes L938's signed integral and L939's asymptotic proof.
Only L939(10)'s definitions and coordinate map are essential here;
L938 supplies interpretation through L939, with L019/L058 background.
L947/L949 are budget context. L940 refutes a signed-amplitude
Schur-concavity mechanism; L950 limits a fixed rowwise allowance.
Neither is a duplicate of, or a prohibition on auditing, this scalar
bound. Their stop evidence remains intact. No numerical kernel
contract is needed for the scalar claim; Mathlib coverage stays unchecked.

Decision: SPECIALIZE approved for the unchanged TARGET, classification
REPRODUCTION for the future mathematical audit. Accept only a full
closed-domain analytic and exact-arithmetic audit, or an identified
error with its effect. This is a completed source-gate approval with
outcome STALLED: it repeats adequate coverage and adds no mathematical
evidence. No central creative mechanism was established; the essential
pending audit takes precedence, and discovery remains a later priority.
