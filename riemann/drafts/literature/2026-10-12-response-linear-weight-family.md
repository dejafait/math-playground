# Proposed full response-linear weight-family test

TARGET: Determine whether any fixed u,v in R^3 gives a strictly positive (log H)^4 coefficient in the complete sharp mean H^(-1) integral_[H,2H] Delta(t)[Re(RZ)(u dot (x,y,z))+Im(RZ)(v dot (x,y,z))]^2 dt.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact-family, weighted-discriminant, Wronskian and stronger moment searches listed below found supporting tools but no inspected matching sign theorem; narrow local comparison found L394/L400 and their recorded failures, not a full-family duplicate. No novelty is inferred from this search.
SOURCE_EVIDENCE: Directly read Hughes–Young arXiv:0709.2345v2 Theorem 1.1/(16)–(17) and holomorphy remark, pp. 4–5; Bui–Hall arXiv:2304.05178v1 Theorem 3/defining asymptotic, Proposition 3 and Section 5; reuse inspected Hughes–Young (46)–(58), Bui–Hall Section 7, modified-Gonek both branches and Bourgain v2 Theorem 5/Section 4 through the named ready assessments below. Jerby arXiv:2310.14415v1 Sections 3–4 definitions/Theorem 4.1 are a different-discriminant comparison only.
COMPARISON: Known tools cover fixed quartic ordinary jets through order two, fixed rational twists and the existing signed-carrier rectangle, not the new quadratic form or its inertia. L394's fixed-jet and L400's single response-dependent conclusions do not decide the full family; no source reproof is needed.
GAP: A later mathematical attempt must evaluate the complete six-parameter coefficient and its inertia, justify every changed projection, weighted physical error, absolute sharp endpoint and uniform full-tail limit. No matrix, carrier decomposition or family asymptotic is derived or verified in this review.
REASON: Separate target-specific source comparison now approves exactly TARGET for one REPRODUCTION specialization using known tools; fixed coefficients and the unchanged derivative/twist scope need no essential unread source. This local readiness advance is neither a new moment theorem nor progress beyond the sources checked.
SCOPE: Actual Delta,R,Z,x,y,z of L400, fixed real u,v independent of H, ordinary jet orders zero through two, four critical factors, fixed response heads and fixed smoothing widths before all-real-H height limits; no mollifier, growing head/twist/order or unproved zero/sign assumption.
LITERATURE_REASON: The target changes from auditing one established Wronskian coefficient to deciding existence of a positive direction throughout a six-parameter response-linear family; its new coefficient family required this separate comparison, while unchanged analytic source coverage is reused.

## Original proposal retained

The following proposal records its pre-review state. The separate step 83
comparison below supersedes its pending-source language, without deciding
any mathematical claim.

Use exactly the actual Delta, R, Z, x,y,z of L400; u,v are fixed real
vectors, independent of H. No arbitrary height-dependent coefficients or
growing response heads are permitted. The main gap is global actual-theta
mixed positivity; this intermediate question concerns the separate eventual
physical-discriminant-sign gap. A strictly positive complete leading mean
would force a positive physical discriminant value at arbitrarily large
heights. It would still leave total L367 margin, common-zero upper counts
and RH unresolved.

This proposes one family-wide sign decision, not another selected weight
or a reopening of L400's stopped direction. A later approved attempt should
retain every direction and determine the full leading quadratic form's
inertia. Continue the positive-mean route only on a rigorously positive
direction with complete o(log^4 H) error. A nonpositive form stops this
entire response-linear family; an uncontrolled essential projection or
error suspends the certificate without deciding its sign. No coefficient,
matrix, inertia, analytic reduction or new lemma is computed here.

Essential proposed inputs are L370's physical normalization, L390's full
response/critical-jet bounds, L391/L392's ordinary-jet carrier methods,
L393's general four-jet formula and arithmetic collisions, L394's absolute
signed-endpoint method, and audited L400's single-direction calculation.
The separate assessment must check exact target duplicates and known
obstructions and whether these tools cover every changed term. Reuse their
precise primary citations and inspected theorem cases; retrieve only
essential missing coverage or a specifically relevant stronger result.
L394/L399/L400 adverse coefficients and L390's absolute-contour failure
must be preserved. No phase independence, RH, simplicity, disjointness,
pointwise sign, common-zero upper bound or growing-N rate is assumed.
Full matching Mathlib coverage remains not checked.

## Separate source comparison — 2026-10-12, step 83

This is LITERATURE / KNOWN_IMPORTED / literature_comparison. It approves
the unchanged TARGET as SPECIALIZE for a later REPRODUCTION attempt.
No lemma or mathematical script is written or run. No family coefficient,
matrix, inertia, carrier identity or asymptotic has been computed here.

### Gap, use and stopping test

The main gap is global actual-theta mixed positivity. This intermediate
target tests the separate eventual physical-discriminant-sign question:
a positive complete leading mean with the stated nonnegative squared
weight would force positive physical discriminant values at arbitrarily
large heights. It would leave the total L367 margin, actual common-zero
upper counts, low-index positivity and RH unresolved.

Continue this positive-mean route only if a rigorously positive direction
survives the complete sharp asymptotic with o(log^4 H) error. A nonpositive
leading form stops this entire fixed response-linear family as a witness
at this scale; it does not exclude positive discriminant values, or a
lower-order witness along a null direction. Failure to control an essential
projection or error suspends the certificate and does not decide its sign.

### Discovery, duplicates and failures actually checked

Web searches on 2026-10-12 used the queries:

- `"zeta" "discriminant" "weighted" "Hardy"`;
- `"Hardy" "response" "Wronskian" zeta`;
- `Hughes Young twisted fourth moment derivatives quadratic form sign Hardy function`;
- `"A new discriminant for the Hardy" Jerby arxiv`;
- `"zeta" "response-linear" weights`;
- `"Hardy" "Wronskian" "moment"`;
- `"zeta" "weighted" "Laguerre" "moment"`;
- `"zeta" "5/2" "fourth moment"`;
- `"Hughes" "Young" "quadratic divisor problem" "Theorem 1.1"`.

Search results supplied no inspected exact-family sign decision. Search
snippets and unrelated discriminants are not theorem evidence. The stronger
twist-range lead *A quadratic divisor problem and moments of the Riemann
zeta-function* (Bettin–Bui–Li–Radziwill, author manuscript returned by search)
and Bui's *Mean values of Hardy's Z-function and weak Gram's laws* seminar
slides are unread leads, not imported coverage. A larger twist range is
not essential for the fixed heads in this target. No assertion about a
theorem's precise hypotheses is imported from either snippet.

The title-matching primary lead was inspected narrowly: Y. Jerby,
*A New Discriminant for the Hardy Z-Function and the Corrected Gram's law*,
[arXiv:2310.14415v1, Sections 3–4](https://arxiv.org/html/2310.14415v1),
22 October 2023. Its parameter-space/global and Gram-discriminant definitions
and Theorem 4.1 concern critical values along non-degenerate curves of
finite cosine sums. That is a different discriminant and a proposed RH
equivalence, not the sharp weighted mean here. No theorem from this paper,
and no correctness claim about its equivalence, is imported.

Local reads compared the exact hypotheses and relevant proof passages of
L390, L393 (5), L394's separate audit and audited L400, and the step 82
history. The specific ATTEMPTS records for the L390 absolute rectangle,
L394 fixed-vector weight and L400 Wronskian weight retain different stops.
L399's specified mollifier stop remains a contrast supplied by the overview;
it is not an input or evidence for the new form's sign. The recorded
repeated-carrier-source approval failure also remains parked. The later
attempt must decide the whole new family, not rerun the stopped direction
or infer a sign from the fixed-vector result.

### Precise primary inputs and reuse

C. P. Hughes and M. P. Young, *The twisted fourth moment of the Riemann
zeta function*, J. reine angew. Math. 641 (2010), 203–236,
[arXiv:0709.2345v2, Theorem 1.1, (16)–(17), pp. 4–5](https://arxiv.org/pdf/0709.2345v2#page=4),
is unconditional. It requires two factors at each height orientation,
coprime positive h,k with hk <= T^(2/11-epsilon), four complex shifts
O(1/log T), a smooth nonnegative weight supported in [T/2,4T], and
w^(j)=O_j(T_0^(-j)), with T^(1/2+epsilon) << T_0 << T. Its error is
O(T^(3/4+epsilon)(hk)^(7/8)(T/T_0)^(9/4)). The following remark makes
the complete six-term main expression holomorphic at coincident shifts;
individual singular terms may not be differentiated there.

Fixed heads and fixed relative endpoint widths meet this theorem's scope
eventually. Reuse the previously inspected residue cases (46)–(58) in
`drafts/literature/2026-10-11-complete-discriminant-second-moment-audit.md`.
L393 (5) supplies the general ordinary-height four-jet specialization for
all orders in {0,1,2} and fixed reduced twists, not just its nine evaluated
monomials. Its complex-shift differentiation, half-log carrier, finite
Euler factors and O(H log^3 H) conversion error are the reusable inputs.
Its particular positive square coefficient is not the new coefficient.

H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1, Theorem 3 and defining asymptotic](https://arxiv.org/html/2304.05178v1),
11 April 2023, gives the leading rational coefficient of fixed-order
quartic Hardy-derivative moments, with error O(T log^(k+l+m+n+3) T).
Proposition 3 has a sharp dyadic fourth-moment formula uniform for four
complex shifts O(1/log T), with O(T log^3 T) error. Section 5 explicitly
uses holomorphy and Cauchy differentiation on scaled circles. These passages
were directly read; reuse the ordinary-phase conversion in Section 7
through the ready L400 assessment. Theorem 3 gives norm coverage, not this
response-weighted sign decision; Theorems 1–2 concern other jet products.

For carriers reuse
`drafts/literature/2026-10-10-discriminant-unequal-orientation-projection.md`
and `drafts/literature/2026-10-12-wronskian-square-weighted-discriminant.md`.
A. Sourmelidis, J. Steuding and A. I. Suriajaya,
[arXiv:2007.14008v2, Section 3 between (35) and (36)](https://arxiv.org/html/2007.14008v2#S3),
states the modified-Gonek lemma for a fixed positive integer q, fixed
delta>0, a=1+delta and a Dirichlet series convergent on Re s>1 with
coefficients O_eta(n^eta) for every eta>0. Its negative-exponential gamma
branch equals the additive-phase coefficient sum through Vq/(2pi), with
O_delta(V^(1/2+delta)) error; the opposite branch is O_delta(1). Constants
may depend on the fixed series and q. Both inspected branches are retained;
periodicity is not a premise of this lemma. The unread originating proof
does not block reuse of this readable precise statement.

J. Bourgain, *Decoupling, exponential sums and the Riemann zeta function*,
J. Amer. Math. Soc. 30 (2017), 205–224,
[arXiv:1408.5794v2, Theorem 5/(0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2),
supplies the unconditional bound |zeta(1/2+it)| <<_epsilon
|t|^(13/84+epsilon). Reuse inspected Section 4 (4.1)–(4.3), p. 19,
and L391's audited interpolation/Cauchy specialization on the fixed
height rectangle -11/20 <= Im tau <= 0 with ordinary jets through order
two. It permits the existing four-factor connector bounds, not an arbitrary
larger strip or an independent theorem for the new physical projection.

No reproof of any cited moment, signed mean-value or subconvex theorem is
justified. The changed coefficient and applicability checks are necessary
because no inspected source states this exact response-linear statistic.

### Approved application boundaries and remaining obligations

The proposed family uses the same three critical jets and the same actual
right-line value and phase as L400. Its weight adds no critical-line zeta
factor, new derivative order or growing twist. This is a source-scope
comparison, not an analytic reduction of the new product. The general
quartic functional, bounded response series and signed-carrier techniques
therefore supply adequate coverage for a bounded specialization attempt.

That attempt must retain all six parameters and every mixed entry, using
the exact actual normalization of L370/L400. Establish the weighted
physical error against L390's full quartic jet envelope, including the
common-envelope correction and complete response derivatives. Prove the
changed balanced and projected identities, rather than substituting L400's
particular polynomials. For every nonzero projection check the exact net
carrier, ordinary-jet conversion, fixed rational-frequency encoding,
slow coefficient variation, pole-free holomorphic rectangle and both sharp
connectors before using the signed primitive or carrier-free method.
If a term falls outside this scope, preserve it and suspend that estimate;
do not infer its negligibility from an independent-phase heuristic.

Evaluate every signed quartic entry from the complete six-term moment,
retaining all equal-product and reduced-ratio collisions and ordinary i
factors. Certify the full real quadratic form's inertia, including any
nullspace; checking selected diagonal directions is insufficient. Use
L394's absolute endpoint-majorant method for a signed polynomial. Verify
a response-head-independent absolute bound before removing the full tail,
then take height limits at fixed head/width before width/head removal.
No growing-N rate or height-dependent optimizing vector is approved.

Essential continuation inputs are L370, audited L390/L391/L392/L393,
L394's audited absolute endpoints, and audited L400. Its ready source
assessment and the two earlier carrier/four-moment assessments above are
reused, with no newly essential source blocker. No RH, simplicity,
disjointness, independent phases, eventual pointwise sign, common-zero
upper count or favorable total L367 margin is assumed. Full matching
Mathlib coverage remains not checked; unknown coverage is not absence.
