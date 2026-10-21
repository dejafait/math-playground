# Proposed response-dependent Wronskian-square witness

TARGET: Determine whether H^(-1) integral_[H,2H] Delta(t) Wcal(t)^2 dt = gamma_W (log H)^4+o((log H)^4) with gamma_W>0, where Wcal=(F_0'G-F_0G')/(A^2(1+t)^2 log(2+t)).
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded target-specific web searches for zeta/Hardy Wronskian weighted moments and discriminants found no inspected exact-product theorem; notebook-scoped searches found the proposal and adjacent moments but no completed duplicate. Reused the ready fourth-moment and signed-carrier assessments; directly inspected Hughes–Young Theorem 1.1 and its holomorphy remark. Queries and unread leads are qualified below; no novelty is inferred.
SOURCE_EVIDENCE: Hughes–Young arXiv:0709.2345v2 Theorem 1.1/(11)–(17), pp. 3–5, holomorphy remark, and previously inspected (46)–(58); Bui–Hall arXiv:2304.05178v1 Theorem 3, Proposition 3/(7), Sections 5 and 7; Sourmelidis–Steuding–Suriajaya arXiv:2007.14008v2 Section 3 between (35) and (36), both gamma branches; Bourgain arXiv:1408.5794v2 Theorem 5/(0.5) and Section 4 (4.1)–(4.3), through unchanged ready assessments. Exact applicability and limits below.
COMPARISON: The known tools cover fixed quartic ordinary jets, fixed rational response twists and signed carrier primitives, not this coefficient or its sign. L394's fixed-vector obstruction does not decide the response-dependent weight; L381 and L393's individual moments are supporting inputs, not an evaluation of their signed product.
GAP: A later REPRODUCTION attempt must prove weighted physical replacement, the complete changed carrier decomposition and every projection estimate, the balanced signed coefficient with all collisions, absolute sharp-endpoint control and uniform full response-tail transfer. Existence and sign of gamma_W remain unknown.
REASON: Changed-target source scope is adequate for one bounded known-tool specialization of exactly TARGET. Import the existing analytic theorems and derive only the identified family-specific application; this literature turn computes no polynomial, coefficient, limit or sign.
SCOPE: Fixed actual F_0,G,A and physical Delta of L370, ordinary height derivatives, all real H tending to infinity, sharp [H,2H], no mollifier, fixed response heads before height limits; no RH, phase independence, zero simplicity, disjointness, growing-head rate or pointwise sign.
LITERATURE_REASON: Step 78 proposed a new response-dependent weight outside the assessed fixed-vector/mollifier targets; its exact product and carrier scope required separate comparison. Unchanged primary coverage is reused, not refreshed to meet a quota.

## Original proposal retained

The following proposal records the pre-review state. The separate source
comparison below supersedes its pending-approval language only.

The main gap remains global actual-theta mixed positivity. This
intermediate target concerns the independent eventual-discriminant-sign
gap: a strictly positive leading mean with the nonnegative Wcal^2 weight
would force positive physical D somewhere in every sufficiently high
dyadic interval. No such mean or positive value is asserted here.

The essential proposed inputs are L370's zero-safe normalization, L381's
exact Wcal definition and response-carrier representation, L390's complete
physical reduction and fourth-jet norms, and the L391–L393 projection,
fixed-twist and full-tail methods. L394 and L399 are contrasts recording
failed weights, not premises for the new coefficient. The proposed weight
has coefficients depending on the actual response and its phase; the
fixed-vector obstruction cannot simply be applied pointwise and then
averaged. Equally, varying coefficients do not imply a positive direction.

Reuse the adjacent assessments
`drafts/literature/2026-10-11-positive-weighted-discriminant-mean.md` and
`drafts/literature/2026-10-11-complete-discriminant-second-moment-audit.md`
for inspected primary statements. First compare the exact new statistic
against their scope and recorded failure mechanisms. Perform bounded
target-specific discovery and retrieve only essential missing theorem
hypotheses or proof cases. In particular, a previous theorem for a
particular carrier polynomial is not approval for this changed product.
No proof, carrier expansion, coefficient calculation or mathematical
script for the proposed target was undertaken during the L399 audit.

The continuation test, after separate coverage approval, is an evaluation
of the complete signed coefficient with error o((log H)^4), retaining
every physical projection and response collision. Continue the witness
only if a strictly positive coefficient is proved. A zero or negative
coefficient abandons this leading-mean diagnostic without ruling out
positive D values. Missing essential analytic coverage must first be
recorded and assessed; it is not evidence about the coefficient's sign.

Eventual physical sign, total L367 margin, actual common-zero upper
counts and global mixed positivity remain unproved. Full matching Mathlib
coverage has not been checked. At proposal time this was a REVIEW_REQUIRED
continuation; it established no mathematics. The separate approval below
does not validate a coefficient or an asymptotic.

## Separate source comparison — 2026-10-12, step 79

This is LITERATURE / KNOWN_IMPORTED / literature_comparison. It approves
exactly TARGET as SPECIALIZE for a later REPRODUCTION attempt. The advance
is local source readiness, not a new mathematical result or an RH advance.
No lemma, mathematical script, carrier expansion or coefficient is written
or computed in this turn. In particular gamma_W is neither evaluated nor
asserted to exist or be positive.

### Main gap, intermediate target and discriminating test

Global actual-theta mixed positivity is still the main gap. This target
tests the independent eventual physical-discriminant-sign question. A
positive complete leading mean with this nonnegative weight would supply
positive physical D values on every sufficiently high dyadic interval.
It would not imply mixed positivity, a total L367 pencil margin, an actual
common-zero upper bound or RH. Continue this witness only if the later
complete coefficient is strictly positive and the physical error is
o(log^4 H). A nonpositive coefficient stops this leading-mean diagnostic;
an uncontrolled essential error suspends the certificate without deciding
the statistic's sign. Preserve these as separate possible outcomes.

### Known results and precise scope

Reuse `drafts/literature/2026-10-11-positive-weighted-discriminant-mean.md`
and `drafts/literature/2026-10-11-complete-discriminant-second-moment-audit.md`.
The latter retains the inspected diagonal/off-diagonal residue cases,
(46)–(58), from the leading-square source assessment. There is no newly
missing source proof case for the unchanged fixed-twist balanced theorem.

C. P. Hughes and M. P. Young, *The twisted fourth moment of the Riemann
zeta function*, J. reine angew. Math. **641** (2010), 203–236,
[arXiv:0709.2345v2, Theorem 1.1, (11)–(17), pp. 3–5](https://arxiv.org/pdf/0709.2345v2#page=4),
is unconditional. It assumes two factors at each height orientation,
coprime positive h,k with hk <= T_Y^(2/11-epsilon), complex shifts
O(1/log T_Y), and a smooth nonnegative weight supported in [T_Y/2,4T_Y],
with derivatives O_j(T_0^(-j)) and T_Y^(1/2+epsilon) << T_0 << T_Y.
Its error is O(T_Y^(3/4+epsilon)(hk)^(7/8)(T_Y/T_0)^(9/4)). The complete
six-term sum is holomorphic through coincident shifts. This turn directly
read that statement and the following holomorphy remark, not only the
abstract. Fixed response heads and fixed relative endpoint widths fit
this scope. The complex shifts permit fixed-order Cauchy differentiation
of the complete total; singular summands cannot be differentiated alone.
Import this theorem without reproof. It supplies no sign for the changed
weighted polynomial.

The local general ordinary-jet conversion is L393 (5), with each of four
height orders in {0,1,2}. Its proof, read here, treats arbitrary such order
tuples and fixed rational twists, retaining the half-log gamma phase,
i factors, finite Euler factors, nested Cauchy circles and O(H log^3 H)
conversion error. Its particular nine square coefficients are not inputs
for the new coefficient. The later calculation must use the entire
six-term conversion, including all equal-product/gcd collisions of the
new response weight. Statistical phase independence is never licensed.

H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1, Theorem 3](https://arxiv.org/html/2304.05178v1),
11 April 2023, supplies fixed-order quartic Hardy moments. Reuse its
inspected Proposition 3/(7) and Sections 5 and 7 through the adjacent
assessments, together with L390's audited conversion to the physical
fourth-jet norm. This is norm coverage, not a theorem for Delta Wcal^2.
No sixth critical-line moment or growing derivative order is approved.

For nonzero carrier projections reuse the primary coverage in
`drafts/literature/2026-10-10-discriminant-unequal-orientation-projection.md`.
A. Sourmelidis, J. Steuding and A. I. Suriajaya, *Dirichlet Series
with Periodic Coefficients and their Value-Distribution Near the
Critical Line*, [arXiv:2007.14008v2, Section 3 between (35) and (36)](https://arxiv.org/html/2007.14008v2#S3),
states the modified-Gonek lemma for fixed positive integer q, fixed
delta>0, a=1+delta, and a Dirichlet series F(s)=sum c(n)n^(-s)
convergent on Re s>1 with c(n)=O_eta(n^eta) for every eta>0. The integral
of (q/(2 pi))^s Gamma(s) exp(-pi i s/2) F(s) ds/(2 pi i), from a+i
to a+iV, equals sum_(n<=Vq/(2 pi)) c(n) exp(-2 pi i n/q), with error
O_delta(V^(1/2+delta)); the positive-exponential branch is O_delta(1).
Constants may depend on fixed q and the series. Periodicity is not a
premise of this lemma. The adjacent assessment inspected both branches
and their following application. No growing q or shifted-primitive
theorem is assumed, and the garbled original Gonek displays remain
unnecessary. Laaksonen–Petridis's accepted 2017-02-26 manuscript, Lemma
1.2, p. 3, is the previously inspected matching restatement; the
fixed-right-line version above is the version to use.

J. Bourgain, *Decoupling, exponential sums and the Riemann zeta function*,
[arXiv:1408.5794v2, Theorem 5/(0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2),
gives the unconditional critical-line exponent 13/84+epsilon. Reuse the
previously inspected Section 4 cases (4.1)–(4.3) and L391's audited
fixed-strip interpolation and Cauchy jet bounds. The permitted rectangle
is the existing -11/20 <= Im tau <= 0 at comparable positive heights,
and the jet orders remain at most two. There is no reproof of the
subconvex theorem and no new strip or source exponent.

### Changed application and remaining proof obligations

Read L370's zero-safe normalization, L381 (2)–(5)'s exact Wcal projection,
L390 (4)–(5) and its audited norms/tails, L391's ordinary-jet, signed
primitive and connector ranges, L392's carrier-free contour range, and
L393's general four-jet formula. These statements put the proposed
application in the same critical-jet and bounded-response scope as the
reviewed quartic methods. The weight introduces response-dependent
coefficients; it does not add an independent critical-line zeta factor.
This is a scope comparison, not a derived carrier decomposition.

The later attempt must first prove the weighted physical replacement,
using the complete response derivatives and L370's envelope correction.
It must bound Wcal^2 by the existing nonnegative quadratic jet envelope
with actual response constants, and control replacement errors against
the quartic envelope of L390. L381's second-moment L2 transfer alone does
not suffice for a product with Delta. Its exact projection formula is
the usable starting point; no mean may be multiplied by another mean.

Then explicitly decompose the changed product into its balanced and
nonzero carrier projections. The adjacent square and fixed-weight
proofs cover the source techniques, not these new polynomials. For
every changed quartic projection, verify the exact ordinary jets,
gamma carrier, fixed rational-twist encoding, coefficient variation
and Dirichlet coefficient hypotheses before using the signed primitive
or carrier-free contour. L391's coefficient argument is for finite
products of four zeta derivatives through order two and slow scalar
coefficients; L392 uses the same jet/rectangle bounds after exact carrier
cancellation. These are the approved method scopes. If the new algebra
does not fit them, retain the term and record the specific obstruction;
do not declare it lower order from a phase heuristic or import L392's
particular cancellation. The full coefficient includes any surviving
leading projection.

The balanced integrand is signed. Direct bracketing by its sign is
invalid. L394's signed-endpoint proof supplies a reusable method:
majorize the absolute boundary error by a nonnegative quartic jet
envelope, evaluate fixed-width smooth endpoint majorants by the
untwisted four-jet theorem, take the height limit, then let their
relative widths tend to zero. The later proof must verify that the
new response weight admits this envelope with constants independent
of the response head. A whole-interval O(H log^4 H) bound alone is
insufficient for that endpoint limit.

Finally prove full-minus-fixed-head transfer for this product at the
fourth-log scale. The actual response line stays Re s=5/2; its complete
absolute value and derivative tails are already retained in L381/L390.
The new product requires its own telescoping/norm estimate with a
constant independent of N. Height limits must be taken at fixed N
and fixed endpoint width before removing width and response tails.
No growing-head rate, exchange of uncontrolled limits, source-uniform
twist constant or omission of derivative tails is approved. These
are application obligations for the next turn, not new results here.

### Discovery, duplicates and recorded failures

Queries used were `"Wronskian" "zeta" "fourth moment"`, `"Hughes"
"Young" "twisted fourth moment" 0709.2345`, `"Hardy" "discriminant"
"weighted" zeta moment`, `"zeta" "Wronskian" "weighted" moment`,
`"Hardy" "Wronskian" discriminant moment`, and `"zeta" "discriminant"
"Wronskian" square`; additional arxiv.org-restricted queries were
`"Hardy" "mixed moments" "derivatives" "fourth" Wronskian` and
`"zeta" "Wronskian" moment discriminant`. No exact matching physical
signed-product theorem was inspected. Much of the Wronskian terminology
returned unrelated differential-equation or arithmetic-zeta results;
these are not theorem inputs. Failure to find a match proves no novelty.

Search results also exposed *Amplified Fourth Moment of the Riemann
Zeta-Function and Applications*, arXiv:2511.14415. Its theorem statement
was not inspected; it is an unread lead, not stronger coverage claimed
here. No amplifier length is needed for this fixed-head application.
The previously screened conjectural discrete derivative moments and
RH-conditional higher moment bounds are not inputs.

Narrow notebook searches for the exact product, gamma_W and
response-dependent weights found the step-78 proposal and adjacent
statistics, with no completed duplicate. Read the fixed-weight failure
`ATTEMPTS/2026-10-11-fixed-quadratic-discriminant-weight.md`, the
repeated-approval failure
`ATTEMPTS/2026-10-11-repeated-carrier-source-approval.md`, and
`ATTEMPTS/2026-10-10-discriminant-four-factor-absolute-contour.md`.
L394 excludes a fixed vector; L399 excludes its specified mollifier;
neither signs this response-dependent statistic. The old O(H^2)
absolute rectangle is still above o(H log^4 H) and is not reopened.
The new test requires the signed primitive and audited stronger
connector bounds, with its own carrier verification. Do not repeat
this source approval once ready; the next turn defaults to mathematics.

Essential continuation inputs are L370, L381, audited L390/L391,
L392's contour method, L393's general four-jet conversion and L394's
signed-endpoint method. L394/L399's adverse coefficients are failure
contrasts, not premises for the new coefficient. All changed physical,
carrier, endpoint and tail estimates and the existence/sign of gamma_W
remain unverified. Main mixed positivity, total L367 margin, eventual
physical sign and actual common-zero upper counts remain independent
gaps. Full matching Mathlib coverage has not been checked; the named
external moment theorems are supporting citations, not a claimed
formal implementation. PROOF.md and DAG.md require no change because
only source readiness has changed.
