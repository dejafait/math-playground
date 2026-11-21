# Fixed complete complex-zero tail budget for low-time H2

TARGET: Derive an explicit uniform operator-norm bound for the complete complex-zero contribution to D H2(lambda) D from |z|>100 on 0<=lambda<=1/20, with D=diag(1,200,40000), and state the conditional finite-head margin required for strict positivity.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step200's completed comparison in 2026-11-09-low-time-h2-finite-zero-domination-review.md searched the finite-zero/Hankel heat and complete-tail mechanism; adequate product/counting methods, not a matching explicit matrix budget, were inspected. Reuse its recorded queries and inspected/unread distinctions.
SOURCE_EVIDENCE: Polymath arXiv:1904.12438v2 Section3 Proposition3.1 proof, paired Hadamard product after (33): https://arxiv.org/html/1904.12438v2#S3 ; Tao 246B Notes1 (23 December2020), Theorem2/(3)-(6), Proposition8: https://terrytao.wordpress.com/2020/12/23/246b-notes-1-zeroes-poles-and-factorisation-of-meromorphic-functions/ ; supporting Mathlib AnalyticOnNhd.circleAverage_log_norm: https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/JensenFormula.html#AnalyticOnNhd.circleAverage_log_norm . Direct sources and load-bearing passages rechecked in step201; details below.
COMPARISON: The known paired product permits complex zeros; Jensen bounds all-zero counts from growth and a nonzero centre. These cover the method, not effective compact-time constants, reciprocal-power summation or the scaled matrix budget. Real-head tracking is unnecessary for this tail-only target.
GAP: Specialize the product to L058's normalization, justify extraction of L874's S2 through S6, obtain an effective uniform growth/count bound, sum the entire |z|>100 remainder with multiplicities/opposite-pair bookkeeping and bound its scaled matrix norm. No such calculation is already performed.
REASON: Explicit constants and complete remainder accounting could make a later real-zero head usable without RH. Cite the general product/Jensen theorems; prove only the quantitative application and matrix estimates. This is established-method specialization, not certified originality.
SCOPE: Exact TARGET only. Step201 separately rechecked the primary sources and repaired the missing direct URLs; SPECIALIZE is retained for a subsequent research invocation. No derivation, lemma or mathematical script is included here; no tracking or positivity claim is approved as proved.

Use L019/L058/L874 for the actual kernel, entire family and H2; use
L914's audited normalizer lower bound only under its stated L037
contracts if needed. L488 records source normalization; its real/simple
tail is a contrast, not a premise. Cite the parent assessment's precise
product and Jensen sources. No cross-notebook input is authorized.

Keep every zero with multiplicity. Pair opposite zeros consistently;
retain conjugate symmetry so the remainder is real symmetric. Do not
replace algebraic powers by modulus squares or assume remote zeros
real. Justify the power-sum identification and all limits: a pointwise
product is not a uniform effective remainder. F(lambda,0)>0 is known;
no global logarithm or zero-free radius100 boundary may be assumed.
Assign boundary zeros, and all interior zeros, to an uncertified finite
part without claiming reality, isolation or a constant head census.

Seek one explicit finite budget on the whole closed band, with every
constant and the entire infinite remainder paid. Fix radius100 and D;
no optimization or parameter sweep. Bound any infinite auxiliary series
analytically through its full remainder. Scripts, if necessary after
approval, save full certificates and print only actual/required bounds,
failures and paths. A certificate preview never verifies the result.

State the finite-head threshold using the standard named Rayleigh
variational characterization for a real symmetric matrix. A positive
finite-part margin remains an independent hypothesis for later work.
This step does not locate zeros or establish H2 positivity.

Continue only on an explicit complete uniform budget with recorded
magnitude and qualifications. If that fails, retain the exact unpaid
estimate and stop this envelope without refinement. A finite but
uncompetitive bound is an inconclusive partial input, not domination
or proof of feasibility. Head tracking, a paid margin, higher degrees
and the global RH argument remain open. Full specialized Mathlib
coverage is unchecked; only the parent's supporting Jensen matches
were inspected.

## Step201 separate source approval and URL repair

On 2026-11-09, reopened the direct primary URLs above, reusing step200's
search/duplicate/failure comparison rather than repeating discovery.
Polymath v2, Section3, proof of Proposition3.1, after (33), explicitly
uses evenness, order one and a nonzero origin to give the opposite-paired
product with locally uniform convergence. Complex and repeated zeros
are permitted in its enumeration. This product input, rather than its
simple-zero motion equation, is the relevant citation. Section1 (4)
fixes the source integral normalization. The previously recorded local
normalization remains to justify in the quantitative application; no
new specialization was derived here. Fixed-time convergence supplies
no numerical constant uniform over the requested closed time band.

Tao's Theorem2 requires meromorphicity near the closed disk and a
centre which is neither zero nor pole; multiplicities are retained,
including boundary zeros with zero logarithmic weight. Read (3)-(6)
and the proof's radius perturbation and Blaschke removal. Proposition8
requires an entire nonzero function bounded by C exp(C |z|^alpha),
C,alpha>0; its proof uses the doubled radius when the origin is nonzero.
Its existential count constant is insufficient for this target. The
future application needs explicit compact-time growth and centre
bounds, then complete reciprocal-power summation. This is a reason
for specialization, not reproof of Jensen or Hadamard.

The current official Mathlib page confirms
AnalyticOnNhd.circleAverage_log_norm: nonzero radius, analyticity on a
neighborhood of the closed ball and nonzero centre. The earlier
parent's sum_divisor_le name was not found on this page during this
check; do not rely on that name without locating its declaration.
The confirmed Jensen theorem suffices as supporting coverage. Full
heat-family and scaled-tail formalization remains unchecked.

Decision: source access is not blocked; retain exactly the saved target
and its continuation/abandonment test. L917's exhausted moment boxes,
L918's unpaid sign and step193 remain preserved through the parent
comparison. No finite-head census, realness or strict margin follows
from these sources. This is a valid process repair, labeled STALLED
because it adds no mathematical evidence beyond step200.
