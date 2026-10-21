# Response-modulus-weighted second-moment diagnostic: source coverage

TARGET: Compare the actual leading coefficient of E[|zeta(5/2+it)|^4 x(t)^2] with L421's fixed-g0 law, retaining its allowed fixed k and theta, to test whether this added constraint separates that law.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 164 reused the October-8 fixed-twist assessment, searched mixed-vertical-line and Dirichlet-polynomial mean-square terminology, and inspected Young's Lemmas 4–5 and Bettin–Chandee–Radziwill's Theorem 1 in primary PDFs; scoped prescribed-response records contain no completed comparison for this extra observable.
SOURCE_EVIDENCE: Young, Arch. Math. 95 (2010), 539–548, (2.1)–(2.3), Lemmas 4–5 and both off-diagonal cases on pp. 542–543; Bettin–Chandee–Radziwill, arXiv:1411.7764v1, (1.1), Theorem 1 pp. 1–2 and collision calculation Section 3.1 pp. 8–9; reused audited L381 (7),(9),(12) and sharp-tail discussion, L389 (3), L419 (3)–(4), and L421 (4)–(10).
COMPARISON: Known twisted second moments cover every fixed finite head of the order-zero observable; the complete response series is absolutely convergent and L381 supplies the scalar norm and sharp-bracketing tools. The explicit full coefficient and its comparison with every admissible fixed-g0 choice are a specialization still to be written, not a new moment theorem or a sourced separator.
GAP: Establish the sharp full-response leading coefficient and compare it with L421's law for all fixed integers k with C_(k+1)/C_k>S and theta=(S-C_1)/(C_(k+1)/C_k-C_1); neither a discrepancy nor parameter matching has been established.
REASON: Essential source coverage is now available for one bounded mathematical attempt on the unchanged target. The extra correlation is outside the old selected list, while its moment input is known; no new lemma, coefficient calculation or mathematical script is produced in this literature turn.
SCOPE: E means dt/H on [H,2H], x=f=F_0/A, W=|zeta(5/2+it)|^2; fixed ordinary order zero, actual response, real H tending to infinity and the existing L419/L421 family. No conditional independence, growing response head, cross-H realization or universal separation of every alternative kernel is presumed.

## Relevance and bounded decision test

The main RH gap is global mixed positivity; actual clipping and the
quantitative full-error regulator margin remain unresolved. Step 163
validates L421's obstruction to deriving capped nondegeneracy from the
previously selected information. That result does not prohibit testing
an additional actual-function constraint. This single proposed target
tests the response dependence of the bulk covariance, rather than its
already audited amplitude or unweighted covariance calibration.

Essential local inputs for a later attempt are L416's exact old list,
L419's fixed-power weight, L421's actual-response law and the fixed-twist
second-moment tools of L381. The response weight W^2 is fixed and
bounded, but this observation alone does not determine its critical
second-moment coefficient. L419 chooses one fixed integer k with its
strict ratio condition and then fixes theta; a computation at an
arbitrarily convenient k cannot reject every choice allowed there.

The approved mathematical continuation has one test: establish the actual coefficient
and compare it with this family's coefficient under its allowed fixed
parameter choices. Continue the diagnostic only if it gives a proved
mismatch or a precise remaining parameter condition. Agreement, an
available parameter matching it, or lack of a justified coefficient
ends this diagnostic without claiming a universal moment obstruction
or a stronger actual positivity theorem. Failure to access an essential
source leaves the dependent calculation unapproved.

Step 164 completes literature coverage only. No coefficient is derived
and no separator is claimed. Even a successful separator for the displayed fixed-g0 family would leave
other covariance weights, other kernels, actual capped equality,
clipping, regulator margin and global mixed positivity unresolved.

## Primary theorem comparison completed in step 164

M. P. Young, *A short proof of Levinson's theorem*, Arch. Math. **95**
(2010), 539–548, DOI 10.1007/s00013-010-0199-9,
[primary published PDF, pp. 540, 542–543](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf).
Read (2.1)–(2.3), both terms of Lemma 4, Lemma 5/(4.5), and its
full proof. The weight satisfies 0<=w<=1, support in [T/4,2T], and
w^(j)=O_j((T/log T)^(-j)) for every j. Positive integer twists h,q
obey hq<=T^(2vartheta), fixed vartheta<1/2; complex shifts are
O(1/log T). Both functional-equation diagonals hm=qn are retained,
with an arbitrarily power-saving remainder. The proof handles both
off-diagonal orderings by logarithmic separation and integration by
parts. This is a finite-twist theorem, not permission to insert the
complete response in w. At zero total shift, reuse L381's combined-
diagonal holomorphic evaluation, not the separately singular auxiliary
terms. No real shift of size two or fast gamma carrier is needed here.

S. Bettin, V. Chandee and M. Radziwill, *The mean square of the product
of the Riemann zeta-function with Dirichlet polynomials*,
[arXiv:1411.7764v1, Theorem 1](https://arxiv.org/pdf/1411.7764v1#page=2),
November 28, 2014 (manuscript date December 1);
published J. reine angew. Math. **729** (2017), 51–79,
[DOI 10.1515/crelle-2014-0133](https://doi.org/10.1515/crelle-2014-0133).
Read (1.1), Theorem 1 and Section 3.1, pp. 1–2, 8–9. For fixed
smooth phi supported in [1,2], A(s)=sum_(n<=N) a_n n^(-s),
a_n=O_epsilon(n^epsilon), N=T^vartheta, 0<vartheta<17/33:

    integral_R |zeta(1/2+it) A(1/2+it)|^2 phi(t/T) dt
      =sum_(d,e<=N) a_d conjugate(a_e)/lcm(d,e)
         *integral_R [log(t gcd(d,e)^2/(2pi d e))+2gamma] phi(t/T) dt
       +O(T^(3/20+epsilon) N^(33/20)+T^(1/3+epsilon)).

Section 3.1 retains equal-product collisions; its intermediate diagonal
is later combined with an off-diagonal contribution. Zero padding
covers fixed heads using a small fixed vartheta. Neither shifted
differentiation nor the improved length range is needed. Support
[1,2] does not itself allow an upper bracket across both sharp
endpoints; use the audited Young/L381 method for that obligation.

## Applicability and remaining mathematical work

L389 (3) identifies x with a constant-sign Hardy function, including
at zeros; hence its square is the critical zeta modulus square.
L419's known absolutely convergent divisor series at j=2 supplies
zeta(5/2+it)^2. A fixed head has source coefficients
a_n=d_2(n)n^(-2) in A(1/2+it), meeting the polynomial coefficient
condition. This checks the theorem's observable and domain, not its
yet-unevaluated coefficient. Alternatively expand that fixed head
against L381 (7), which already gives the full gcd factor for every
fixed rational twist, with error O_(h,q,w)(H).

For sharp endpoints, L381 uses T=2H, fixed-shape weights supported
inside [H/2,3H], and brackets a complete nonnegative product after
summing its twists. These supports fit Young, with derivatives
O_(j,epsilon)(H^(-j)) at each fixed smoothing width epsilon. The
same type of nonnegative product occurs in this order-zero target.
The subsequent proof must retain the order H first, epsilon second,
and head length last; no growing-head estimate is approved.

For the complete response, the necessary existing inputs are L381's
scalar order-zero mean-square bound (9), its uniform right-line tail
(12), and the absolute j=2 series in L419. They permit uniform
approximation of the response factor in that scalar norm. A research
turn must write this transfer and absolute convergence of its limiting
arithmetic coefficient; finite-head convergence alone will not suffice.
This is a covered elementary specialization of known inputs, with no
essential unread source. Neither conditional independence nor a
pointwise bound substituted for the mean is justified.

For the comparison law, retain L421's high, intermediate and bulk
components, not just the displayed bulk covariance. Its (4), (6),
(8) give their integrated second-matrix sizes and the correction
O(sqrt(log H)); the response weight is bounded. The later calculation
must explicitly account for these terms at the leading-log scale.
Use L419's fixed k, theta and complete C_j moments as stated in GAP;
do not substitute a convenient k or let k grow with H. Compare every
admissible fixed choice, or record an exact remaining parameter
condition and stop. The family comparison is not settled by either
primary moment theorem.

## Duplicate and obstruction screen; scope of approval

Read the relevant parts of L416, L419 and L421, the step-163 audit
history, and the prescribed-response radial-lift failure. The old list
contains six unweighted critical second moments and response-dependent
quartics, not this separately specified weighted critical second
moment. The radial-lift cubic obstruction and the audited selected-law
stop remain intact. No existing record inspected evaluates this
coefficient against all allowed k. This is a scoped duplicate check,
not a claim of novelty or of absence from all literature.

Queries included `zeta mixed moments different vertical lines mean
square`, `zeta twisted second moment Dirichlet polynomials Bettin
Chandee Theorem 1`, `A short proof of Levinson Young Lemma 5`,
`zeta 5/2 fourth power moment`, and critical-line/absolutely-convergent
Dirichlet-series variants. The inspected general theorems above are
stronger finite-polynomial inputs than needed. Search hits concerning
shifted critical-line fourth moments, long-polynomial conjectural
divisor correlations, and Hardy derivative products were not used as
theorem evidence; no unread lead is essential to the order-zero test.

Approval is SPECIALIZE for the exact TARGET only. Reproduce the known
moment machinery and perform its explicit arithmetic/parameter
comparison; do not reprove either general source theorem. A mismatch
would reject only this fixed-g0 family under the added constraint.
Agreement or an admissible matching choice ends the diagnostic.
No assertion about every alternative covariance weight, actual
clipping, regulator margin, global realization or RH is approved.
Full matching Mathlib coverage is not checked; unknown coverage is
not an absence claim. No lemmas/ or scripts/ files changed in this step.
