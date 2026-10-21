# Clipped linear coefficient: joint-sign source scope pending

TARGET: Assess source coverage for a positive liminf of the complete mean (H(log H)^4)^(-1) integral_[H,2H] Delta(t) max{-mathcal B(t),0}^2 dt, with Delta from L390 and mathcal B from L369.
CHECKED: 2026-10-13
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Step 99 performed bounded exact-clipping, Hardy joint-sign/distribution and derivative-moment searches; inspected the primary results named below and reused the ready L401 polynomial-family assessment; no exact clipped asymptotic or applicable joint-sign symmetry was found in the inspected sources, and no novelty is inferred.
SOURCE_EVIDENCE: Hughes–Young 0709.2345v2 Theorem 1.1/(16)–(17) and holomorphy remark; Bui–Hall 2304.05178v1 Theorems 1–3, Corollary 1, Proposition 3 and Sections 5–7; Curran–Heycock 2403.00902v1 Theorems 1.1–1.2 and Section 4; Gonek–Ivic 1604.00517v1 Theorem 1 and Section 3; Ivic 1601.06512v1 Section 4/Theorem 3 and proof, with its historical qualifications below.
COMPARISON: Fixed polynomial quartic moments and absolute derivative-moment bounds do not state a clipped mixed asymptotic; scalar Hardy sign density is unconditional but does not control the joint signs of Delta and mathcal B. Bui–Hall's odd-total-derivative-order cancellation is not sign symmetry of the clipped statistic.
GAP: Essential signed nonpolynomial mixed-moment or controlled approximation coverage is missing, including its actual phase dependence and uniform tail at H(log H)^4 scale; the positive liminf and any contrary sign remain undecided.
REASON: The bounded review is complete as a source-scope decision but does not make the clipped calculation ready; retain REVIEW_REQUIRED and park dependent research while a separate polynomial benchmark receives next-turn approval.
LITERATURE_REASON: The unchanged saved target was REVIEW_REQUIRED at invocation; its new one-sided clipping, rather than another concentration refinement, required this essential source comparison.

The proposed intermediate target keeps the exact physical pair and all
ordinary derivatives. Here

    mathcal B=(2F_0'G'-F_0 G''-F_0''G)/(A^2 T^2 L^2),
    Delta=D/(A^4 T^4 L^4), T=1+t, L=log(2+t).

The threshold sought is a strictly positive liminf for the displayed
complete sharp mean as real H tends to infinity. No coefficient or
sign is conjectured as established. Sign clipping is essential to this
proposed test; replacing it by the full square changes the target.

Plausible downstream use: a positive clipped weighted mean would locate
positive discriminant where L367's linear coefficient is negative,
linking the presently separate sign statements in a positive-regulator
pencil analysis. It would still leave the regulator scale, quantitative
total margin, comparison remainder and global actual-theta mixed
positivity unresolved. L368's response-quadratic positivity is relevant
to that later use, not an assumed solution of any margin. No common-zero
upper count or RH consequence is asserted.

Essential local inputs for the comparison are L367's exact signed
pencil and error, L369's normalized linear coefficient, L390's complete
physical identity and curvature, and L401's complete polynomial-weight
family and audited all-real-H limits. L404 is the concentration benchmark,
not a source of joint-sign independence. The comparison should first
check L401's family against this specific full square and determine what
the clipping changes in source hypotheses; do not infer independence of
the actual gamma carrier and zeta values. Any passage through a polynomial
approximation must have its required tail/uniform-integrability coverage
assessed before a mathematical implementation is approved.

Recorded contrasts: L394's fixed jet quadratic weights, L399's specified
short mollifier and L400's Wronskian-square weight failed their own
positive-leading-mean tests. L401 succeeds in a different direction but
does not select the sign of mathcal B. These stops are not removed by
naming a clipped weight. No duplicate joint-sign result was established
by the narrow local comparison, and no novelty claim follows.

Continuation/abandonment test: approve a bounded mathematical test only
if inspected unconditional theorems cover the needed mixed moment or
controlled approximation with the exact actual phase, full response,
curvature and sharp interval. If known symmetry or the complete signed
coefficient already rules out a positive liminf, import that obstruction
instead of computing an uncovered variant. If essential coverage remains
missing, record it without deriving a new clipping theorem in the same
literature turn. Full matching Mathlib coverage has not been checked.

## Completed source comparison — 2026-10-13, step 99

Outcome: NEGATIVE source-scope evidence changes the route; this is not a
negative clipped coefficient or a mathematical impossibility theorem.
No new lemma, mathematical script, asymptotic, phase symmetry or coefficient
was derived. The original target and all previous failure evidence remain.

### Discovery and local comparison

Queries included `Hardy Z derivatives mixed moments joint distribution
sign shifted fourth moment Hughes Young positive part`, `zeta derivative
joint distribution Hardy function signs clipped moments`, `"zeta"
"positive part" "moment" Hardy`, `"Hardy" "joint distribution"
"derivatives" zeta`, `"Hardy" "sign" "fourth moment" Z(t) sign
distribution`, `"zeta" "derivatives" "joint distribution" Selberg
theorem`, `"clipped" "Hardy" "zeta"`, and the exact title search for
Gonek–Ivic. Searches returned no inspected exact clipped theorem. This
does not establish absence from the literature.

Local reads used L369 (1), (7)–(11), L370 (1)–(5), L390's complete
physical replacement and ordinary response triple, and L401's statement,
replacement and changed-projection proof. The ready assessment
`drafts/literature/2026-10-12-response-linear-weight-family.md` supplies
unchanged polynomial source coverage. Targeted history/draft searches
found the proposed clipping but no completed duplicate joint-sign result.
L394's fixed-quadratic and L400's Wronskian-square ATTEMPTS records were
read; L399's specified mollifier stop is retained as an overview contrast,
not a mathematical input. These failures do not rule out clipping.

### Primary results actually inspected

C. P. Hughes and M. P. Young, *The twisted fourth moment of the Riemann
zeta function*, J. reine angew. Math. 641 (2010), 203–236,
[0709.2345v2, Theorem 1.1/(16)–(17), pp. 4–5](https://arxiv.org/pdf/0709.2345v2#page=4):
four complex shifts O(1/log T), coprime h,k with
hk<=T^(2/11-epsilon), smooth nonnegative w supported in [T/2,4T],
w^(j)=O_j(T_0^(-j)), T^(1/2+epsilon)<<T_0<<T. The error is
O(T^(3/4+epsilon)(hk)^(7/8)(T/T_0)^(9/4)); the complete six-term
expression is holomorphic in the shifts. Fixed response heads and fixed
relative smoothing widths meet these premises. Its test weight is not an
arbitrary clipped function of zeta jets. Reuse the earlier inspected
residue cases (46)–(58) through the L401 assessment; no reproof is needed.

H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
[2304.05178v1, Theorems 1–3, Corollary 1, Proposition 3 and Sections 5–7](https://arxiv.org/html/2304.05178v1),
11 April 2023: fixed-order quartic Hardy jets have an explicit leading
coefficient and an error one logarithmic power smaller. The small-shift
fourth moment and Cauchy differentiation justify ordinary polynomial jets.
The sign-density argument uses a favorable mollified signed mean and its
square moment; it does not evaluate a clipped Delta-weighted coefficient.
Corollary 1 concerns odd total derivative order, rather than an arbitrary
odd function of the actual jet vector. No sign symmetry or phase
independence needed here is asserted. The physical ordinary-height
conversion and full-tail handling already audited in L401 remain usable
for a polynomial benchmark, without importing any clipped conclusion.

M. J. Curran and A. Heycock, *Sharp bounds for joint moments of the Riemann
zeta function*,
[2403.00902v1, Theorems 1.1–1.2 and Section 4, (2)](https://arxiv.org/html/2403.00902v1),
1 March 2024: for fixed n, 0<=k<=2, h_j>=0 and sum h_j<=k,
the absolute mixed moment of zeta and derivatives j<=n is bounded by
T(log T)^(k^2+2 sum j h_j). The corresponding k>2 upper bound assumes
RH. The first-derivative lower bound is also absolute. Section 4 uses
small-circle Cauchy transfer, convexity of the moment power and the
functional equation, not signs. Thus it supplies envelopes at total
critical power at most four, not a signed clipped asymptotic or arbitrary
higher-degree unconditional approximation coverage. A bounded fourth
moment alone is not the required uniform tail estimate for passage from
a compact polynomial approximation. No such passage is proved here.

S. M. Gonek and A. Ivic, *On the distribution of positive and negative
values of Hardy's Z-function*, J. Number Theory 174 (2017), 189–201,
[1604.00517v1, Theorem 1, p. 2, and Section 3, p. 7](https://arxiv.org/pdf/1604.00517v1#page=2),
2 April 2016: both scalar Hardy sign sets in [T,2T] have measure >>T
unconditionally. Section 3 combines signed mollified mean o(T), absolute
mollified mass >=T+o(T), and a bounded mollified second moment.
This controls the scalar sign and neither the response-linear coefficient
nor its Delta-weighted joint sign. Theorem 2 uses RH and pair correlation;
it is inapplicable to an unconditional input here. No result is imported
into the proof chain in this literature turn.

A. Ivic, *Hardy's function Z(t) — results and problems*,
[1601.06512v1, Section 4, pp. 10–13, Theorem 3 and proof](https://arxiv.org/pdf/1601.06512v1#page=10),
25 January 2016, distinguishes log-modulus distribution from signed Hardy
distribution and states historical sign questions. Its Theorem 3 assumes
RH, with interval length T^theta, 1/4<=theta<=1. This older survey is not
evidence that its questions remain open today: Gonek–Ivic supplies the
later unconditional scalar positive-proportion result. Neither source
provides the clipped mixed moment requested here.

Unread leads: the 2026 Simm random-matrix/joint-moment paper (publisher
full text failed to load), Voronin's off-line joint-value Omega theorem,
and Mawia's short-interval Hardy sign paper. No hypotheses or coverage
are imported from their search snippets. None is essential to the
polynomial benchmark. The failed 2403.00902v2 HTML and nonexistent
1604.00517v2 PDF were resolved by inspecting their v1 primary texts;
they are not persistent source blockers.

### Decision and remaining threshold

The inspected sources cover the existing polynomial apparatus but no
controlled clipping approximation, complete sign-restricted mean, or
applicable symmetry deciding the positive liminf. This narrows the
continuation: park the clipped calculation. A polynomial fourth-moment
limit alone does not justify treating its sign restrictions as half of
that limit, and a holomorphic contour argument for a polynomial cannot
simply be applied to max{-mathcal B,0}. No counterexample or theorem
excluding the positive liminf is claimed.

The independently testable continuation is the complete unclipped
Delta*mathcal B^2 benchmark, with exact physical-to-polynomial transfer
checked in a later mathematical turn. Its proposed assessment is
`drafts/literature/2026-10-13-linear-coefficient-full-square-benchmark.md`;
as a newly written ready continuation, it requires separate next-turn
approval. This benchmark does not decide the original clipped mean.
Reopening the latter requires a precise sign-sensitive mechanism with
adequate source scope and full tail control, not repeated scalar signs
or an independence heuristic. Full matching Mathlib coverage: not checked.
