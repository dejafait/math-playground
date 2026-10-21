# Proposed nonnegative quadratic-weight discriminant test

TARGET: Determine whether a fixed real vector v gives H^(-1) integral_[H,2H] Delta(t)(v_0 x(t)+v_1 y(t)+v_2 z(t))^2 dt = gamma_v (log H)^4+o((log H)^4) with gamma_v>0.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Target-specific bounded searches for weighted Hardy derivative fourth moments, zeta Laguerre/discriminant moments and mixed-jet polynomials found supporting moment results but no inspected exact weighted-discriminant theorem; narrow local assessment/history/failure searches found no completed duplicate. Primary Bui–Hall fixed-order and sign cases and Hughes–Pearce-Crump's conjectural discrete scope were inspected; unchanged Hughes–Young, modified-Gonek and Bourgain coverage was reused.
SOURCE_EVIDENCE: Hughes–Young arXiv:0709.2345v2 Theorem 1.1/(11)–(17), holomorphy remark and (46)–(58), via the saved complete-square assessment; Bui–Hall arXiv:2304.05178v1 Theorems 1–3, Proposition 3, (7), Sections 5 and 7; Sourmelidis–Steuding–Suriajaya arXiv:2007.14008v2 Section 3 between (35) and (36) and Bourgain arXiv:1408.5794v2 Theorem 5/(0.5), via the saved signed-k1 assessment and audited L391. Precise hypotheses, links and application limits below.
COMPARISON: Known inputs cover fixed-twist balanced quartic jets, a signed right-line carrier primitive and fixed-order norm control; they do not assert this weighted discriminant coefficient or its sign. L391/L393 provide reusable conversion methods, while their specific polynomial conclusions cannot be imported for the changed polynomial. Signed endpoints require absolute boundary-error control rather than direct nonnegative bracketing.
GAP: In a later attempt verify the weighted physical replacement, complete changed carrier polynomial, all balanced quartic coefficients and gcd collisions, signed endpoint error and full-tail limits; then decide whether the full real quadratic form has a positive direction. None has been evaluated or certified here.
REASON: Essential source coverage is adequate for one bounded REPRODUCTION specialization of exactly TARGET. Import the known moment and signed-primitive theorems; derive only this family-specific application. Approval does not assert an asymptotic or positive direction, and the historical coarse-contour failure remains preserved.
SCOPE: Fixed actual Delta,x=f,y=f'/log(2+t),z=f''/log(2+t)^2 as in L390; fixed v in R^3, all sufficiently large real H, fixed heads before height limits; no RH, simplicity, noncoincidence, growing twists or eventual discriminant sign.
LITERATURE_REASON: The target changes from the complete square to a signed mean with a nonnegative quadratic jet weight; its coefficient, carrier polynomial and sharp signed endpoints were not approved by the complete-square audit assessment.

## Original proposal retained

The following pre-review proposal preserves the target and its motivation.
Its pending-source language is superseded by the separate review below.

The main gap remains actual-theta global mixed positivity. This proposed
intermediate target addresses the separate unresolved eventual physical
discriminant sign. A strictly positive weighted mean would force positive
Delta, hence positive physical D, somewhere in each sufficiently high dyadic
interval, without requiring a common-zero upper bound. That implication is
the proposed downstream use; no such positive mean or D value is proved.
The aim is an independently testable sign witness, not more precision in a
moment whose sign implications have already been exhausted.

The essential proposed inputs are audited L390's complete physical reduction
and Hardy fourth-jet norm, L391's fixed-head signed carrier implementation,
and L393's small-complex-shift ordinary-jet conversion. L392's complete-square
harmonic conclusion alone is not a theorem for a changed polynomial. The
literature approval must decide whether the precise source hypotheses and
existing proofs cover this weighted application, including a signed sharp
interval and the uniform response-tail transfer. Retrieve only any essential
missing theorem or proof case; do not refresh unchanged sources by default.
The relevant approved general primary theorems may be imported unchanged,
but a positive coefficient for this family cannot be presumed.

After separate approval, the continuation/abandonment test would be the sign
of the complete leading quadratic form in the fixed vector v, retaining all
its carrier contributions and gcd collisions. Continue only if a positive
direction survives with error o(log^4 H); if no positive direction exists,
record that obstruction and stop this fixed-quadratic-weight implementation.
Failure would not show that actual positive discriminant values do not occur.
No test, matrix entry or lemma for this proposed statistic was computed here.

The earlier coarse absolute-rectangle failure remains valid and is not
reopened. This proposal seeks a sign-sensitive witness, not a better
unweighted Cauchy–Schwarz sign-set estimate from the now-known full moment
scale. Main positivity, total L367 margin, actual common-zero upper counts,
low indices, heights above forty and endpoint arithmetic margins remain
unresolved. Full matching Mathlib coverage has not been checked. This file
is an uncovered proposal, not source approval or a mathematical result.

## Separate source comparison — 2026-10-11, step 54

This is LITERATURE / KNOWN_IMPORTED: new local coverage for the changed
target, not a mathematical result beyond the checked sources. No matrix
entry, direction, coefficient, weighted asymptotic, lemma or mathematical
script has been computed or written. Approve exactly TARGET as SPECIALIZE
for one later REPRODUCTION attempt; keep v fixed independently of H.

### Known inputs and exact applicability

Reuse the ready primary extraction in
`drafts/literature/2026-10-10-discriminant-second-moment-leading-scale.md`
and its audit-scope comparison in
`drafts/literature/2026-10-11-complete-discriminant-second-moment-audit.md`.
C. P. Hughes and M. P. Young, *The twisted fourth moment of the Riemann
zeta function*, J. reine angew. Math. **641** (2010), 203–236,
[arXiv:0709.2345v2, Theorem 1.1, pp. 4–5](https://arxiv.org/pdf/0709.2345v2#page=4),
is unconditional. It requires two zeta factors at each height orientation,
coprime positive integers h,k with hk <= T_Y^(2/11-epsilon), four complex
shifts O(1/log T_Y), and a smooth nonnegative weight supported in
[T_Y/2,4T_Y]. Its derivatives are O_j(T_0^(-j)), with
T_Y^(1/2+epsilon) << T_0 << T_Y. The error is
O(T_Y^(3/4+epsilon)(hk)^(7/8)(T_Y/T_0)^(9/4)).

The saved review inspected (11)–(17), the whole-sum holomorphy remark,
Proposition 2.1, the residue cases (46)–(57), (58), and their combination.
Those cases remain within scope: fixed response heads give finitely many
fixed rational twists, and derivative orders stay at most two in each
of four critical factors. Fixed relative smoothing widths meet the
support/derivative conditions; fixed twists eventually meet the size
condition. L393's ordinary-jet formula (5) is stated for every such
four-order tuple, not just its nine evaluated monomials. Reuse its
complete scaled-shift conversion, including the i factors, half-log
gamma phase, nested Cauchy contours and finite Euler factors; the
changed polynomial still needs its own exact coefficient evaluation.
Differentiate the complete holomorphic six-term total, never its
singular coincident-shift summands. No reproof of Hughes–Young is needed.

H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1, Theorem 3](https://arxiv.org/html/2304.05178v1),
11 April 2023, supplies unconditional fixed-order quartic Hardy moments.
For this changed endpoint question, inspected its defining asymptotic,
Proposition 3's uniform complex shifts, and Sections 5 and 7's Cauchy
differentiation and ordinary-phase conversion. Its unweighted moments
support norm and boundary-envelope estimates; they do not evaluate
twisted or physical discriminant moments. Its Theorems 1–2 sign
derivative products, not D. Reuse the fuller earlier norm assessment
`drafts/literature/2026-10-10-negative-discriminant-set-measure.md`.

For the changed carrier use the unchanged primary coverage in
`drafts/literature/2026-10-10-discriminant-unequal-orientation-projection.md`.
A. Sourmelidis, J. Steuding and A. I. Suriajaya, *Dirichlet Series
with Periodic Coefficients and their Value-Distribution Near the
Critical Line*, [arXiv:2007.14008v2, Section 3 between (35) and (36)](https://arxiv.org/html/2007.14008v2#S3),
states the fixed-right-line modified-Gonek lemma. For fixed positive
integer q, fixed delta>0, a=1+delta and a Dirichlet series F(s) convergent
on Re s>1 whose coefficients are O_eta(n^eta) for every eta>0,

    (2 pi i)^(-1) integral_[a+i,a+iV]
      (q/(2 pi))^s Gamma(s) exp(-pi i s/2) F(s) ds
      = sum_(n<=Vq/(2 pi)) c(n) exp(-2 pi i n/q)
        +O_delta(V^(1/2+delta)).

The positive-exponential branch is O_delta(1); constants can depend on
the fixed series and q. Periodicity is not a coefficient premise of
this lemma, although it is used later in that paper. The saved review
read both branches and the following two-exponential application.
Laaksonen–Petridis, *On the Value Distribution of Two Dirichlet
L-functions*, [accepted manuscript, 26 February 2017, Lemma 1.2, p. 3](https://discovery.ucl.ac.uk/1544001/1/lvalues_accepted.pdf#page=3),
is an independently inspected matching lead; its moving-right-line
formulation is not needed. No growing q or uniform shifted-primitive
theorem is assumed. The unreadable originating Gonek displays remain
unnecessary; this review does not claim to have repaired their access.

J. Bourgain, *Decoupling, exponential sums and the Riemann zeta function*,
[arXiv:1408.5794v2, Theorem 5 (0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2),
gives |zeta(1/2+it)| <<_epsilon t^(13/84+epsilon) unconditionally.
The saved assessment inspected Section 4 (4.1)–(4.3), including the
remaining short-sum cases. Import that value bound; use audited L391's
fixed-strip interpolation and Cauchy jet bounds only on its existing
rectangle and fixed derivative orders. Reprove neither decoupling nor
the signed primitive. L391's proof treats finite quartic combinations
of ordinary jets through order two with slow scalar coefficients,
fixed rational-twist encoding and both sharp connectors. Its specific
MK conclusion is not a theorem for a different polynomial: the later
attempt must check the changed carrier, coefficient variation and
Dirichlet majorants against these same source hypotheses.

### Changed endpoints and complete physical scope

Audited L390 supplies the complete physical replacement and the
fourth-jet norm on comparable dyadic intervals. Multiplication by the
proposed quadratic weight needs an explicit norm argument in the
later proof; it cannot be inferred from the square asymptotic alone.
The source scope remains four critical factors, fixed jets and the
same absolutely convergent right-line response. No sixth-moment
theorem, growing derivative order or growing response head is licensed.

For the balanced signed polynomial, L393's direct nonnegative
bracketing of its square integrand is unavailable. The later proof
must bound the absolute boundary error with a nonnegative quartic
jet envelope and smooth endpoint-strip majorants meeting Hughes–Young's
weight conditions. It must obtain a bound that vanishes after division
by H log^4 H and then the fixed relative strip width tending to zero.
An O(H log^4 H) estimate on the whole interval alone is inadequate.
The known smooth quartic moments cover evaluating such fixed-width
majorants; this is adequate source scope, not a proved boundary bound
for the changed statistic. Preserve signed monomials in the main mean.

For the projected term, verify the changed algebra before invoking the
signed primitive and sharp connector method. Do not import L392's k=2
square cancellation or assume L391's exact polynomial vanishes here.
If a surviving leading carrier contribution appears, retain it in the
full quadratic form rather than forcing it to be negligible.

The later proof must also retain response derivative errors already
present in L390, and check a uniform full-minus-fixed-head error at
the required log^4 scale using its jet norm. Take height limits at
each fixed head and width, then remove smoothing and the head in a
justified order. Fixed-head constants may depend on the head; no
uniform-in-growing-twist theorem or independent phase model is allowed.
This review approves that application test, not any of these estimates.

### Discovery, duplicate check and stopping test

Queries actually used included `"Hardy" "weighted" "derivatives"
"fourth moment" discriminant`, `"zeta" "Laguerre" "discriminant"
moments`, `Hughes Young twisted fourth moment derivatives Hardy function
mixed moments`, `"Hardy" "Z" "fourth" "mixed" "derivatives" polynomial
moment`, `"zeta" "discriminant" "weighted mean"`, and `"Hardy" "joint
moments" "Hughes" "Young" polynomial derivatives`. Bounded searches
found no inspected exact physical weighted theorem. This does not
establish novelty or absence of further literature.

A relevant-looking newer lead was inspected directly: C. Hughes and
A. Pearce-Crump, *Integer moments of the derivatives of the Riemann
zeta function*, [arXiv:2509.07792v1, Abstract and Section 1, Conjectures 1–4](https://arxiv.org/html/2509.07792v1),
9 September 2025. These are conjectural mixed moments sampled at
nontrivial zeros and assume RH, so they are no input for this
unconditional continuous mean. Random-matrix joint moments and the
search lead *Amplified moments of the Riemann zeta function* were not
inspected as theorem inputs; no claim is made from those leads.

Narrow searches in the active notebook's literature assessments,
history and ATTEMPTS found the saved proposal and existing square,
signed-residual and negative-set work, with no completed duplicate.
Read the relevant L390/L391/L393 proof ranges and step-53 history.
Preserve `ATTEMPTS/2026-10-10-discriminant-four-factor-absolute-contour.md`:
the failed coarse O(H^2) rectangle remains above the required
o(H log^4 H). The changed signed-primitive implementation and endpoint
envelope test are distinct from that failed certificate, not a claim
that its obstruction disappeared. Parked sharp-source and discrete-grid
routes are not reopened.

Continuation test: compute the complete leading real quadratic form
in fixed v, retaining every signed carrier contribution and gcd
collision, and verify the physical, endpoint and tail errors at
o(log^4 H). Continue this fixed-weight implementation only if a
strictly positive direction survives. If the full form is nonpositive,
record that obstruction and stop this implementation. An uncontrolled
error stops its certificate without deciding the actual sign of D.

Essential local inputs are audited L390's physical/norm reduction,
L391's ordinary jets, signed-primitive implementation and connectors,
and L393's general fixed-twist four-jet formula (5) and complete
scaled-shift kernel, not its particular square coefficient. Remaining
application assumptions are proof obligations, not hypotheses silently
granted by approval. Global mixed positivity, total L367 margin,
actual common-zero upper counts, low-index signs, heights above forty
and endpoint arithmetic margins remain open. No RH, simplicity,
noncoincidence, phase independence or eventual D sign is assumed.
Full matching Mathlib coverage has not been checked; the supporting
analytic theorems above are precise external citations, not purported
Mathlib implementations. PROOF.md and DAG.md need no change because
this turn changes source readiness only.
