# Proposed growing arithmetic weight for a positive discriminant mean

TARGET: Assess a growing arithmetic Dirichlet-polynomial weight for a positive complete physical discriminant mean, determining an admissible length and the signed ordinary-jet moment and error thresholds.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded exact discriminant/Laguerre-weight queries and stronger twisted-second-moment comparison; reused the October 8 and October 10 mollifier assessments and searched the specific fixed-weight/contour failures. No inspected theorem states the complete proposed mean; unrelated search hits and conjectures are not evidence of coverage or novelty.
SOURCE_EVIDENCE: Bui–Hall arXiv:2304.05178v1 mollifier definition, Proposition 1 and Section 3 (6)–(8), printed pp. 6–8; Young, Arch. Math. 95 (2010), 539–548, (2.1)–(2.3), Lemmas 3–7, full Lemma 5 proof and Section 6 contour/residue cases, pp. 540–546; Bettin–Chandee–Radziwill arXiv:1411.7764v1 Theorem 1, pp. 1–2, with previously inspected Section 3.1 reused; local L390 complete physical-error and tail arguments and L381 Section 4 complete projection/endpoint argument.
COMPARISON: Known mollified second moments supply constant-scale normalized critical-jet control for a specified short Mobius family, and Young permits growing twists below his stated barrier. They do not supply the complete weighted discriminant coefficient. The old O(1) averaged carrier estimate is insufficient at this new constant scale, even before insertion of the growing weight.
GAP: Complete balanced response-twisted diagonal evaluation, the same-height carrier at constant scale, its growing-weight connectors and signed sharp endpoints, and a strictly positive total coefficient remain unproved. Only the explicitly covered weighted physical replacement and full-tail subtarget is approved for specialization.
REASON: Essential primary coverage is adequate for one narrower weighted-transfer attempt, not for discarding or signing the complete carrier. Select that independently testable obligation first; no coefficient, new lemma or mathematical script is derived in this literature-only step.
LITERATURE_REASON: The target changes from a fixed critical-jet vector to an arithmetic Dirichlet polynomial with growing length; fixed-twist constants and unweighted fourth-jet norms do not by themselves give the required uniform signed physical asymptotic.

## Proposed target and decision test

The main unresolved gap is global actual-theta mixed positivity. A positive
complete discriminant mean under an everywhere nonnegative weight would
provide an actual positive physical discriminant value and test eventual
D<=0 on this separate route. It would supply neither global mixed positivity
nor an RH conclusion. This is a proposed relevance argument, not a claim
that such a mean exists.

Consider a height-dependent arithmetic Dirichlet polynomial P_H(t), with
length at most H^theta for an explicitly selected fixed theta>0, and the
nonnegative weight |P_H(t)|^2. The prospective statistic is
H^(-1) integral_[H,2H] Delta(t)|P_H(t)|^2 dt. Its natural normalization,
coefficient restrictions and error threshold must be settled by the source
comparison; the log^4 H normalization of the previous jet-weight statistic
is not automatically appropriate. No polynomial coefficients, positive
leading direction, length range or moment formula have been derived here.

Approve a concrete mathematical specialization only if complete primary
hypotheses cover a specified family and expose an independently checkable
positive-coefficient test whose physical and analytic errors can be smaller
than its sought margin. If coverage applies only to unrelated mollifiers,
omits the carrier or does not control the weighted physical error, record
that exact mismatch and choose a genuinely covered subtarget or abandon
this mechanism. Do not repeat blocked source-access searches as the test.

## Essential inputs and prior boundaries

Essential local inputs are L370's exact physical discriminant identity,
L388's complete unweighted mean, L390's zero-safe reduction, L391's signed
carrier tools, L393's fixed-twist ordinary-jet conversion and audited L394's
fixed-weight obstruction. These identify available tools, not premises of
a new asymptotic. In particular L390's unweighted norm error alone need
not be negligible at the prospective weighted mean scale; this is an
explicit unresolved obligation rather than an assumed transfer.

The narrow local search found prior Bui–Hall mollifier comparisons in
`2026-10-08-wronskian-second-moment.md` and
`2026-10-08-actual-wronskian-noncommon-zeros.md`, and their limitations in
the October 10 residual and derivative-square assessments. These are
potential source leads; they were not reapproved for the proposed statistic.
The old sharp-Hardy access failure in
`ATTEMPTS/2026-10-10-parked-sharp-hardy-source-and-recovery.md` remains
parked. Preserve L394's fixed-weight and L390's absolute-contour stops.
The future review should reuse relevant inspected statements before seeking
a genuinely missing uniform theorem, and must distinguish bounded twists
from growing support throughout.

No RH, simplicity, noncoincidence, independent phases, eventual D sign or
actual common-zero estimate is available. Total L367 margin, global mixed
positivity, common-zero upper counts, low-index signs, heights above forty
and endpoint arithmetic margins remain independent unresolved gaps.
Matching Mathlib coverage for the proposed application is not checked.

## Completed source comparison — 2026-10-11, step 58

The proposal above is retained as historical motivation. This review is
LITERATURE / KNOWN_IMPORTED / EXPLORATION: it imports source scope and
selects a covered application, without proving a weighted estimate or
claiming progress beyond the sources checked. SPECIALIZE covers only the
subtarget below; it does not approve the original positive-mean calculation.

### Primary statements and essential cases

**Bui–Hall**, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1, Proposition 1 and Section 3](https://arxiv.org/html/2304.05178v1#S3),
uses the specified Mobius mollifier of length T^vartheta, with fixed
polynomials P,Q_1,Q_2, P(0)=0, and vartheta<4/7. The mollifier definition
also normalizes P(1)=1. Proposition 1 gives the sharp [T,2T] normalized
two-jet moment, an explicit constant functional and O(1/log T) error.
Read (6)–(8): ordinary Hardy derivatives include the i^k factors and
R_k(X)=(1/2+X)^k; Cauchy–Schwarz controls the lower-order derivative
errors. This directly covers scalar weighted jet norms, but adding the
right-line response factors is not an application of that proposition.
The sign-set theorems concern different statistics.

**Young**, *A short proof of Levinson's theorem*,
[Arch. Math. 95 (2010), 539–548](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf),
Lemma 5, p. 543, allows positive h,k with hk<=T^(2 theta), theta<1/2,
complex shifts O(1/log T), and weights satisfying (2.1)–(2.3):
0<=w<=1, support [T/4,2T], derivatives O_j((T/log T)^(-j)). It retains
both functional-equation diagonals with O_(A,theta)(T^(-A)) error.
Read both off-diagonal orderings, large-product decay and integration
by parts. Lemma 3 and the Cauchy argument after (3.4) provide uniform
shift differentiation. Section 6 handles the canceled s pole, the
arithmetic Euler factor and residue errors. Those formulas evaluate
the specified mollifier; additional fixed response twists require a
new local applicability and arithmetic calculation. No fast carrier
is allowed in w, and no fixed-twist asymptotic from L381 is promoted
to a uniform growing-twist formula.

**Bettin–Chandee–Radziwill**, *The mean square of the product of zeta(s)
with Dirichlet polynomials*,
[arXiv:1411.7764v1, Theorem 1, pp. 1–2](https://arxiv.org/pdf/1411.7764v1),
allows general coefficients a_n<<n^epsilon and length N=T^theta,
theta<17/33, with a fixed smooth weight supported in [1,2]. Its
unshifted modulus-square formula retains gcd/lcm collisions and error
O(T^(3/20+epsilon)N^(33/20)+T^(1/3+epsilon)). The previously read
Section 3.1 diagonal cases are reused. This stronger length range
does not authorize differentiated complex-shift errors or the carrier.
No longer-polynomial theorem is needed for the selected subtarget.

### Covered family and uncovered complete-mean obligations

Select y=H^(1/100), fixed P(u)=u^2 and

    P_H(t)=sum_(n<=y) mu(n)n^(-1/2-it) P(log(y/n)/log y).

The polynomial meets both endpoint normalizations in the inspected
mollifier definition. Its exponent lies strictly inside both inspected
second-moment ranges. This is a deliberately conservative source-covered
family, not a proved maximal admissible length for the physical statistic.
No growing coefficient optimization or response-grid window is approved.

The source moment suggests constant scale for the normalized critical
jets under this weight. The discriminant mean is signed: constant scale
and a positive coefficient for the complete mean remain targets, not
conclusions. In particular L381 (20) proves only O(1) for a different,
unweighted same-height projection. Such a bound does not establish o(1),
and its proof does not allow insertion of P_H unchanged. L391's fixed
gamma scales also do not give uniform constants for this new support.
Any later full-mean calculation must retain the entire carrier or prove
its actual constant-scale contribution, rather than discard it using
the earlier logarithmic normalization. Boundary contributions must be
bounded absolutely, not bracketed as though the integrand were positive.

For future balanced-head use, Young's two diagonals are an available
starting theorem, not an evaluated coefficient after summing the growing
mollifier. Finite response twists change the collision arithmetic.
Uniform summed errors, holomorphic jet conversion, those arithmetic
factors and the head limit all require proof. The corresponding complete
mean target remains uncovered and requires another assessment when chosen.

### Selected intermediate test and relevance

The one ready proposed continuation is recorded in
`drafts/literature/2026-10-11-mollified-physical-transfer.md`. Test weighted
critical-jet mass O(1), absolute physical replacement O(1/log H), and an
absolute response-head error bounded by C eta_N, with C independent of N
and H and eta_N=sum_(n>N)n^(-5/2). These are sought thresholds, not results
derived in this turn. The existing pointwise bounds in L390 identify the
application; Bui–Hall supplies the essential sharp scalar input. Reproving
the source moment theorem is unnecessary.

Success would remove the previously uncovered weighted replacement/tail
obligation at the putative constant scale, while leaving the carrier and
coefficient independent. Continue only if the full physical error and
uniform tail satisfy these thresholds. If an omitted derivative or
endpoint prevents this transfer, preserve that failure and reassess the
specified family; do not claim a positive witness from a truncated model.
A later complete positive mean could exclude eventual D<=0 but would
not prove global mixed positivity or RH. All original independent gaps
and the L394/L390 stop evidence remain in force. Mathlib coverage of the
matching weighted application is not checked.

Queries actually used: `zeta Hardy derivatives Laguerre discriminant
resonator mollifier twisted second moment`; `Young short proof Levinson
theorem Lemma 5 hk T 2 theta error twisted second moment`; `Bettin Chandee
Radziwill mean square zeta Dirichlet polynomials 1/2 1/66 theorem`;
`"shifted second moment" "Dirichlet polynomial" complex shifts theorem`;
`"zeta" "discriminant" "mollifier"`; `"Hardy" "Laguerre" "mollifier"`;
`"zeta" "Laguerre" "twisted moment"`; `"zeta" "discriminant"
"Dirichlet polynomial"`; `"mollified" "second moment" "twist" shifts fixed`.
Search hits alone are unused. No matching theorem or duplicate was
established in the narrowly checked local records. Conditional long
mollifiers, CUE conjectures, and unrelated discriminant articles are not
inputs. The parked sharp-Hardy source was not retried.
