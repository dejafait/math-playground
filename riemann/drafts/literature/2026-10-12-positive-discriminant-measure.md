# Proposed quantitative positive-discriminant set estimate

TARGET: Prove that meas{t in [H,2H]:D(t)>0} is at least c H^(1/3)(log H)^4 for some fixed c>0 and every sufficiently large real H, using L401's positive direction and unconditional Hardy-jet bounds.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped search of October 10–12 local assessments, histories and failure records found L389 negative-set concentration, not this positive weighted target; web queries for discriminant/Hardy positive measure and zeta positive-part fourth moments found no inspected matching theorem. Jerby arXiv:2310.14415v1 Definition 1.5 and Theorems A–B concern a different Gram discriminant.
SOURCE_EVIDENCE: Reused inspected Bourgain arXiv:1408.5794v2 Theorem 5/(0.5), p. 2, with audited L391 fixed-strip/Cauchy specialization; Bui–Hall arXiv:2304.05178v1 Theorem 3, its defining asymptotic, and sign-set Cauchy–Schwarz (3)–(4), as documented in the step 40 assessment. Read L401 hypotheses/(1)–(3), L390 hypotheses/(1), complete response and norm proof, L391 pointwise consequence and (10)–(11), and L389 complete physical budget and sign-set argument.
COMPARISON: Known subconvexity, Hardy fourth moments and Cauchy–Schwarz cover the analytic tools; audited L401 supplies the positive mean for W=Re(RZ)f and L390 supplies the complete Delta second moment. No inspected source states the exact physical positive-set bound; the positive-part/weight specialization remains to be proved.
GAP: In the later proof retain the full weight, positive normalization and uniform all-real-H estimates, and verify that the supported powers reach c H^(1/3)(log H)^4. No new moment theorem, eighth-moment asymptotic, weight lower bound or phase assumption is needed within the reviewed method.
REASON: Essential coverage is adequate for one later REPRODUCTION application of existing inputs and standard inequalities; this literature turn approves source scope only and establishes no measure theorem.
SCOPE: Fixed actual F_0,G,A,D,Delta and exact weight [Re(RZ)f]^2, all sufficiently large real H, existential fixed constants, no growing response head, RH, simplicity, common-zero bound or total-pencil sign premise.

This is only a proposed target, not an approved estimate or a completed
literature review. No measure inequality is derived here. Reuse the existing
precise primary coverage where adequate; new retrieval is needed only for an
essential missing hypothesis or a materially stronger applicable result.

The main gap remains global actual-theta mixed positivity. After audited L401
excludes eventual D<=0, the intermediate target would quantify how much of
each high dyadic interval violates that premise. Its plausible downstream use
is to constrain proposals that tolerate exceptional positive-D sets; it still
would not sign the total L367 pencil or prove RH. It is not a positive-density
claim, a common-zero upper bound, or a positive Laguerre sign.

Essential continuation inputs are L401's audited positive weighted mean,
L390's exact physical normalization and norm bounds, and L391's fixed-strip
ordinary-jet estimates. L393's audited square mean may be used if needed;
L389's negative-set result is a comparison, not a positive-set premise.
The subsequent scope review must narrowly check relevant duplicate/stop
records, the precise uniformity in H and any additional standard inequality.
No independent phase or weight lower bound at individual heights is assumed.

Continue only if the stated lower bound follows with all weight, endpoint,
logarithmic and error factors retained. If the available bounds fall short,
record the exact supported threshold and the missing norm or concentration
estimate; do not infer that the actual set is smaller. This new review does
not reopen the stopped L394/L399/L400 positive-leading-mean witnesses or
require repeating their source approval. Full matching Mathlib coverage is
not checked. Any newly ready assessment requires its own later mathematical
invocation; this audit turn computes no part of the proposed measure bound.

## Completed scope comparison — step 87

The proposal above is preserved as the pre-review record. Its statements
that review is incomplete are superseded by this comparison. TARGET and
hypotheses are unchanged. This is source-coverage progress, not proof of
the proposed measure estimate or progress beyond the sources checked.

**Reused primary coverage.** Bourgain, *Decoupling, exponential sums and
the Riemann zeta function*, J. Amer. Math. Soc. 30 (2017), 205–224,
[arXiv:1408.5794v2, Theorem 5/(0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2),
gives the unconditional critical-line exponent 13/84+epsilon for each
fixed epsilon>0. L391 already records a fixed epsilon and the weaker
O(t^(1/6)) consequence, and proves the fixed-strip interpolation and
Cauchy estimates through ordinary order two. For the selected weight,
only the order-zero bound is essential: L389 identifies f with a fixed
sign times Hardy's function without division by a zeta value. This holds
at zeros as well. L401 has |R|=1 and the complete Z=zeta(5/2+it);
absolute convergence on that right line supplies its uniform upper bound.
No derivative estimate for a growing order or growing head is licensed.

Bui–Hall, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1, Theorem 3 and its defining asymptotic](https://arxiv.org/html/2304.05178v1),
provides unconditional fourth product moments at fixed nonnegative orders.
The step 40 primary assessment inspected (3)–(4), Proposition 3/(7), and
the Sections 5 and 7 derivative/endpoint cases. Reuse those cases unchanged:
orders zero through two, sharp dyadic intervals, all sufficiently large
real H. L390 has already specialized the complete physical second-moment
upper bound for Delta; L393's sharper asymptotic is optional, not essential.
The known sign-set Cauchy–Schwarz argument is the relevant inequality;
it is not necessary to reprove a source moment theorem. The proposed
positive weighted statistic differs from the source Hardy-product signs
and from L389's negative unweighted statistic, so its application must
be written separately rather than imported as an existing conclusion.

**Bounded duplicate and obstruction screen.** Read L389's full relevant
physical budget and measure proof, L390's exact definitions and complete
norm bounds, and L401's exact positive direction and audited conclusion.
The scoped textual search found no second copy of this positive-set
threshold. Read the L394 fixed quadratic-weight, L399 specified mollifier,
L400 Wronskian-weight failure records and the repeated-carrier-approval
stop. They prohibit neither this already positive L401 direction nor its
measure application. No stopped weight is reopened. The step 86 history
confirms that this quantitative bound was proposed, not established.

External queries were `"discriminant" "Hardy" "positive" zeta measure
weighted` and `"Riemann zeta" "positive part" "Cauchy" measure fourth
moment`, followed by the exact Jerby title. Retrieved the primary
[Jerby arXiv:2310.14415v1 HTML](https://arxiv.org/html/2310.14415v1),
Definition 1.5 and Theorems A–B: its discriminant is a varied finite
section evaluated at a moved Gram extremum, not the F_0,G physical pencil.
Those statements supply no matching positive-set measure estimate. Its
proofs are not imported or audited here. A nearby newsletter search hit
initially led to arXiv:2310.13542, whose primary abstract is about Bessel
interlacing; that identifier is unrelated. No novelty is inferred from
these searches. Other search hits remain unread, nonessential leads.

**Approved specialization and discriminating test.** The subsequent
attempt may apply the standard positive-part restriction and
Cauchy–Schwarz to the exact weighted L401 mean, with the uniform upper
bound for the square weight and L390's full second-moment budget. It
must state the weight bound explicitly, retain every log power, and
compare the resulting measure threshold to the exact TARGET. It must
check measurability, positive normalization D/Delta, signed-integral
restriction, all-real-H quantifiers and absorption of L401's little-o.
This is a proof obligation, not a calculation performed in this review.
If the powers or uniformity fail, record the exact supported threshold
and missing input; that failure would not bound the actual set from above.
A stronger subconvex consequence is unnecessary for this focused target.

The downstream use remains control of how small exceptional positive-D
sets can be in weakened discriminant strategies. Global mixed positivity,
total L367 signed margin and common-zero upper counts remain independent
open gaps. No RH, simplicity, noncoincidence, positive-density conclusion,
weight lower bound, eighth-moment theorem or phase independence is assumed.

**Mathlib.** The full physical target and analytic source theorems are not
checked for matching coverage. The inspected
[Holder module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/Holder.html)
contains supporting bilinear/Lp infrastructure; no exact integral
Cauchy–Schwarz declaration was identified in that page. The mathematical
inequality is cited through the primary Bui–Hall sign-set proof instead.
No Mathlib absence claim is made.
