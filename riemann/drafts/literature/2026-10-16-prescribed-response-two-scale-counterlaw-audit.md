# Source coverage for the prescribed-response two-scale counterlaw audit

TARGET: Critically audit L421's prescribed-response counterlaw against every selected moment tolerance, both amplitude branches, the bulk covariance correction and the vanishing capped limit.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 162 compared L421 in full with the step-160 lower-implication assessment, step-148/154/158 source coverage, step-155/159 audit records and the scoped lower-implication failure; read the exact L414/L415/L416/L417/L418 constraints and L419's matrix/weight implementation and audited branches. No matching completed L421 audit was found in these records; no fresh external retrieval or novelty inference.
SOURCE_EVIDENCE: Reuse Carlen--Lieb arXiv:0904.0734v2 Horn theorem after (1.1), proof through (1.2), pp. 1--2, as inspected in step 154; Bui--Hall arXiv:2304.05178v1 Introduction equation (1) and preceding odd display, Theorem 3/Proposition 3, as inspected in steps 44/146/148; Curran--Heycock arXiv:2403.00902v1 Theorem 1.1/(2) and Sections 3.1/4 as inspected in step 105 and reused in step 158; unchanged quartic/cubic inputs and qualifications are detailed below.
COMPARISON: The primary moment hypotheses are unchanged actual-input hypotheses, not assertions about conditional output states. Schur--Horn applies to any real symmetric matrix and imposes no O(1) covariance-correction hypothesis; L419's Borel implementation is a separate local input. L421 must still justify its larger correction, both amplitude components and every tolerance; the sources and prior audits do not validate those claims.
GAP: No essential unread source is identified for the exact proof audit. Check the full O(sqrt(log H)) subtraction, positive covariance and strict translated cone margin, fiber mass on both high branches, all six second entries, both first-mean tolerances, cubic, all 23 quartics, both absolute envelopes, uniform constants and the same-law fixed-lambda limit.
REASON: This separate source-scope comparison approves one later REPRODUCTION proof_audit of the unchanged TARGET, using ready literature coverage; it neither performs that audit nor establishes a new counterlaw, capped estimate or zeta theorem.
LITERATURE_REASON: Step 161 proposed this new critical audit as REVIEW_REQUIRED; the changed simultaneous amplitude components and full covariance subtraction require scope comparison with the ready L418/L419 and moment assessments, not renewed discovery for the already attempted lower implication.
SCOPE: Exactly L421's selected integrated-moment relaxation, actual height/response graph, exact curvature, uniform dt/H, ordinary critical jets through order two and fixed qualitative constants for every sufficiently large real H; no conditional critical moments, cross-H consistency, global critical function, actual capped equality, clipping or regulator margin.

## Retained startup proposal

The following proposed obligations are retained. The completed step-162
comparison below supersedes their pending-approval language only; their
mathematical checks remain for a separate research turn.

Essential inputs for the proposed audit are L405, L409, L414, L416,
L417, L418 and L419. The proof is canonical in
`lemmas/L421-prescribed-response-vanishing-capped-cubic-counterlaw.md`.
The bounded attempt's earlier sketch is not independent evidence.

Check that the selected relaxation imposes only integrated asymptotic
moments and fixed qualitative constants, not a single global critical
function or a common probability law across overlapping H intervals.
The response graph and curvature must remain actual at every height.
The high branch must preserve signed quartics even when rho0 exceeds
ell^3; its mass must leave room for the intermediate component.
The full covariance subtraction must preserve positive definiteness,
the uniform negative trace and measurable cone-supported realization.
No O(1) replacement may be used for an O(sqrt(ell)) correction without
checking the first-Delta tolerance. Both tiny odd tolerances need exact
cancellation. Finally distinguish F_lambda^nu from the actual F_lambda.

The counterlaw, if validated, stops inference from this selected list;
it does not refute actual capped nondegeneracy or supply actual/global
realization, clipping, a full-error regulator margin or mixed positivity.
At proposal time no audit was approved; step 162 below supplies only
source-scope approval for the separate audit. Full Mathlib matching
coverage remains unchecked.

## Completed source comparison — 2026-10-16, step 162

This is LITERATURE / NOVELTY_UNCHECKED / literature_comparison, outcome
EXPLORATION. It supplies new audit-scope comparison, not a mathematical
advance, a completed critical audit or evidence of originality. No fresh
external source retrieval was needed: the target uses the same fixed
actual moment inputs and finite matrix theorem already assessed. No
lemma, mathematical script, PROOF.md or DAG.md is changed.

### Relevance, downstream use and decision test

The main RH gap remains global mixed positivity or another exclusion of
every off-line zero. On this branch, actual negative-Bcal clipping and
L413's quantitative full-error regulator margin remain unproved. The
single intermediate target is reliability of L421's selected-information
counterlaw. Its plausible downstream use is to retain or correct the stop
on moment-only capped lower bounds and identify which genuinely additional
actual-function information would be necessary. It cannot evaluate
L418's actual F_lambda or provide a global critical realization.

Continue reliance on the counterlaw only if the separate audit verifies
every selected tolerance, both amplitude branches and the same-family
vanishing payoff with fixed constants on an eventual real-H ray. A false
bound, missing source hypothesis, loss of positive covariance or failed
exact cancellation requires a precise repair or narrowing within this
audit scope. If no such repair works, withdraw reliance on the affected
claim while preserving its proof and stop record. A scalar toy law,
numerical fit or verification of only the leading quartics is insufficient.

### Reused primary results and changed-hypothesis comparison

**Finite matrices.** E. A. Carlen and E. H. Lieb, *Short proofs of
theorems of Horn and Mirsky on diagonals and eigenvalues of matrices*,
[arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2), 13 May 2009,
pp. 1--2, Horn theorem following (1.1), proof through (1.2). The
[step-154 assessment](2026-10-16-prescribed-response-bulk-critical-audit.md)
records the inspected real orthogonal-conjugation statement, majorization
hypothesis and two-coordinate rotation/induction cases. Its constant
trace-average diagonal specialization is the same one used in L419.
This theorem concerns arbitrary finite real symmetric matrices; it does
not restrict how a covariance was obtained or its correction size.

L421's proposed matrix is again S J S with S the positive square root
of its proposed covariance. Positive definiteness, comparability to ell I
and a uniform negative trace must be established in the later audit;
they are not consequences of Schur--Horn. In particular the old O(1)
correction proof cannot simply be cited for the claimed O(sqrt(ell))
correction. The primary theorem asserts pointwise existence only. Borel
dependence and equality branches are supplied by L419's explicit local
algorithm, read in its construction and separate step-155 audit. That
algorithm is formulated for the resulting symmetric matrix, while the
translated cone estimate uses covariance bounds, negative trace and a
bounded mean. Check those interfaces anew without reproving Horn's
theorem or importing a measurable eigenbasis theorem. Unknown full
Mathlib coverage remains unknown.

**All six second moments and first tolerances.** H. M. Bui and R. R.
Hall, *On the derivatives of Hardy's function Z(t)*, Bull. Lond. Math.
Soc. 55 (2023), 2304--2323,
[DOI 10.1112/blms.12859](https://doi.org/10.1112/blms.12859),
[arXiv:2304.05178v1](https://arxiv.org/pdf/2304.05178v1#page=1),
Introduction p. 1 equation (1) and preceding odd-order display. Reuse
the inspected even/odd hypotheses and proof discussion recorded in
[step 146](2026-10-15-compatible-jet-second-moment-scope.md) and
[step 148](2026-10-15-compatible-jet-second-moment-critical-audit.md).
For fixed nonnegative j,k the even cumulative integral has the monic
polynomial main term and error O(T^(3/4)(log T)^(j+k+1/2)); the odd
primitive bound is O(T^(1/3)). L416's audited sharp weighted specialization
uses only the six pairs through order two and applies logarithmic divisors
after ordinary differentiation. No new source specialization is needed.

The exact selected tolerances are four even entries ell K_ij+O(1),
E xy=O(H^(-2/3)ell^(-1)) and E yz=O(H^(-2/3)ell^(-3)). L415's
first mean is E Bcal=-b0+O(ell^(-1)+H^(-1/2)ell^2); the first Delta
mean in L414 is only -a_* ell+o(ell). These are integrated raw moments,
not conditional moments or prescribed lower polynomial coefficients.
L421 claims exact ell K and exact -b0; those algebraic claims must be
audited. An O(sqrt(ell)) error is not acceptable for a second entry or
the first Bcal tolerance, and may be assessed only against the stated
first-Delta tolerance. No stronger tolerance may be silently imposed.

**Quartics, cubic and absolute envelopes.** Reuse the precise moment
coverage in steps 148/158 and the
[step-160 comparison](2026-10-16-signed-quartic-capped-cubic-lower-bound.md).
The underlying quartic source is Hughes--Young,
[arXiv:0709.2345v2](https://arxiv.org/pdf/0709.2345v2#page=4),
Theorem 1.1/(12)--(17), pp. 4--5: small complex shifts O(1/log H),
coprime twists hk<=H^(2/11-epsilon) and the stated smooth weight scales.
Its existing audited local applications already provide the actual
coefficients. L421 proposes no growing twist, new shift domain or new
twisted moment. Bui--Hall's same v1 Theorem 3, Proposition 3 in Section
4.2 and Sections 5/7 supply the fixed-order quartic envelopes already
imported through L390/L418. The selected 23 coordinates are Delta^2,
Delta Bcal^2 and all 21 Delta omega_i omega_j, including signed
off-diagonal entries; U^2 is an additional envelope, not a 24th fixed
coefficient. Preserve each actual coefficient, including L405's positive
kappa_*, without fitting it or inferring a limiting joint distribution.

M. J. Curran and A. Heycock, *Sharp bounds for joint moments of the
Riemann zeta function*,
[arXiv:2403.00902v1](https://arxiv.org/html/2403.00902v1), 1 March 2024,
Theorem 1.1/(2), Sections 3.1 and 4, was inspected in step 105 and
reused in step 158. The unconditional range is fixed derivative order,
0<=k<=2 and nonnegative derivative exponents summing to at most k.
The retained power-three input uses k=3/2 and ordinary orders at most
two through L406. These actual upper bounds neither evaluate a radial
restriction nor prove a moment bound for the output states. L421 must
verify both output absolute third-power envelopes and the fourth envelope
directly. Do not reprove the source theorem or apply it to model states.

The signed cubic coefficient beta_* is exactly L409's audited full-response
constant with its H-first, fixed-head-then-tail quantifiers; the signed
quartic constant is L405's audited complete-square coefficient. Their
unchanged applications were compared in step 160; their canonical
hypotheses and conclusions were read here. Neither theorem signs a
clipped mean. L419's fixed positive weight g0 and actual right-line/gamma
inputs are covered by step 154 and its step-155 audit. L421's new
normalization against its own remaining mass still needs direct checking;
no new Euler or gamma theorem is called for.

### Framework, duplicates and exact audit boundary

The [step-150 assessment](2026-10-15-compatible-jet-actual-response-marginal.md)
already distinguishes selection/purification from constructing prescribed
moments. L421 uses explicit finite Borel fibers, so no such existence
theorem or atomic replacement is essential. The Bertsimas--Popescu weak
and strong duality comparison in step 160 remains background: the latter
requires interiority, and neither an optimizer nor strong duality is used.
No additional source access blocker is essential to the present audit.
Unread underlying Hall, Horn or broader selection references are not
new premises. No fresh theorem discovery is warranted merely to repeat
this adequate coverage; no novelty is inferred from the scoped search.

L414/L416 use an adjustable response and height law; they are not matching
duplicates. L418's separate step-159 audit validates a partial rare
component with an unevaluated cubic. L419's step-155 audit validates its
original bounded correction, not L421's simultaneous components. The
step-161 counterlaw is the object awaiting audit, not independent evidence
that the audit passes. Preserve the earlier capped-radial and L420
magnitude-certificate failures and
`ATTEMPTS/2026-10-16-signed-quartic-capped-lower-implication.md`.
None is a global prohibition on additional actual-function constraints.

The later audit must check the exact Borel direction and its uniform
positive cubic bound; r=max(ell^3,2^(1/4)rho0), both high branches and
rho0=0; reservation of fiber probability for the intermediate component;
and every unnormalized rather than conditional moment estimate. It must
check the full integrated second-matrix subtraction and translated
six-state support, not only the two odd entries. Check both first means,
the beta_* cubic tolerance, all quartics including zero coefficients,
both absolute third moments and U^2, exact actual response/curvature and
uniform qualitative bounds for every sufficiently large real H.

Finally audit the quantifiers: one family independent of lambda must
give the asserted o(ell^2) payoff for each fixed lambda>0; its cap onset
may depend on lambda, while its selected-law constants do not vary with H.
F_lambda^nu is not L418's actual F_lambda. Cross-H consistency and a
single global critical function are unassumed. The actual capped equality,
clipping, L413's regulator margin and global mixed positivity remain
independent gaps. SPECIALIZE authorizes this exact separate audit only.
