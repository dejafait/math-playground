# Growing-jet localization — completed bounded source review

TARGET: Test whether L637's normalized bump has squared projection o(1), uniformly for T<=X<=2T, onto span_C{L^(-j) Z^(j):0<=j<=floor(L^(1/3))} in L2(w_XT dt).
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact projection/localization, growing-derivative second-moment and stronger-result searches completed; scoped duplicate/failure checks and queries are recorded below. No matching projection theorem identified; no novelty or literature-wide absence claim.
SOURCE_EVIDENCE: Bettin arXiv:1111.0925v1 Thm 1 p. 2 and small-shift proof pp. 9--10; Bui--Hall arXiv:2304.05178v1 Introduction (1), pp. 1--4; bramble_trace paper 36 displayed v4 Thm 9/Section 8.1, reusing the parent's Sections 8.1--8.4 proof-case assessment; DLMF Table 18.3.1, 18.5.8, 25.2.4; Tao 254A Supplement 3 (2014), (35)--(38). Precise scopes and links below; Hughes--Young is retained parent coverage, not needed to define this projection.
COMPARISON: Available analytic moment generators, classical polynomial formulas and pointwise convexity support a bounded test. Fixed-order joint moments, fourth-moment filtered positivity and the two-atom result do not import the actual growing-space projection conclusion.
GAP: Prove actual growing-order Gram control with the complete second-moment main term and quantitative order losses, then control correlations with the exact normalized bump uniformly in X; neither estimate is established here.
REASON: Essential source tools for this unchanged bounded test are accessible; approve exploration, not the o(1) claim. Reproof of the named arithmetic inputs is unnecessary. The optional inaccessible derivative paper is parked and is not used as a premise.
LITERATURE_REASON: The hypothesis j<=floor((log T)^(1/3)) and the actual bump-projection quantity are outside the completed fixed-dimensional remainder assessment. Reuse its named sources and the saved parent comparison; search only the missing growing-order localization scope.
SCOPE: Exact saved projection test only, using L637's fixed w,u0,psi,g_(T,X), exact analytic Hardy Z, L=log T and T<=X<=2T; complex coefficients and every order through floor(L^(1/3)). No amplifier, changed bump, exact bandlimitation or unrestricted atomic-density conclusion. Permission to attempt a bound is not a bound.

## Invocation-start nomination, preserved as historical scope

In the complex Hilbert space with norm ||.||_T from L637, let
V_(T,X) be the span of L^(-j)Z^(j), 0<=j<=floor(L^(1/3)),
and let P_(T,X) denote its orthogonal projection. The target concerns
||P_(T,X)g_(T,X)||_T^2, with the actual Gram matrix, not its leading
sine-kernel replacement. This specifies a growing family in which
realization can be tested independently of the unrestricted dictionary.
The exponent 1/3 specifies the proposed range; no optimality is claimed.

The source review must first compare the exact statement and any stronger
known localization or projection theorem. Reuse the inspected moment
theorem statements and proof-case comparison in
`2026-11-01-hardy-translate-gram-relative-error-review.md`, especially the
degree restrictions and different denominator in paper 36. The latter
is a recorded overlap lead, not an asserted source for this target.
L637's Fourier-filtered dual proof and its preserved absolute-TV stop
are relevant contrasts. A lower bound on TV does not settle a projection
onto V_(T,X); conversely a result for V_(T,X) would not settle arbitrary
finite translates. Do not differentiate the real Riemann--Siegel error
or apply fixed-order Cauchy constants uniformly in growing order.

Essential prospective local inputs are L637's definitions and exact
analytic domain, L638's audited first-order analysis, L473 Section 1
and L465/L622's phase bounds. These do not by themselves approve the
new growing-order calculation. Any further mathematical input needs
the primary hypotheses and relevant proof cases checked before use.
Mathlib matching coverage remains not checked.

Main gap: actual-Xi initial signs at unbounded heights and all-degree
mixed positivity. The plausible use is to decide whether improving
moment transfer in this explicit family can aid microscopic realization,
rather than merely enlarging a family that has no relevant localization.
Even successful realization would leave signed |W|-weighted approximation,
a useful main-term margin and growth beyond this range unresolved.

After coverage is ready, continue only with a uniform projection estimate
or a rigorous sequence refuting the proposed o(1) limit. A loose inverse
Gram bound is inconclusive. A vanishing projection would park realization
in this degree range while preserving possible larger or different
dictionaries; it would neither refute RH nor the unrestricted route.
No projection estimate, high-order derivative bound or new lemma was
derived during this nomination. It required the separate source review
completed below.

## Completed source comparison — 1 November 2026

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. The exact TARGET
is unchanged. No projection estimate or new mathematical result has
been derived. Approval supplies source coverage for one bounded attempt;
the supervisor retains next-turn approval and routing.

### Exact scope and relevance

Use the complex weighted Hilbert space, fixed bump and normalization
in L637's hypotheses, with a=X+u0*T, not a center chosen after observing
Z. The degree is floor((log T)^(1/3)); coefficients can depend on T,X.
The projection is onto actual ordinary derivatives of the analytic
Hardy function, normalized by L^(-j), with the actual weighted norm.
Leading sine kernels and a fixed-order covariance are prospective
comparison tools, not replacements for that norm.

Main gap: actual-Xi initial signs at unbounded heights and all-degree
mixed positivity. This intermediate target tests whether this explicit
growing family can realize a microscopic observer before further moment
transfer work. Vanishing projection would stop that family's realization
at this degree range. A failure of vanishing would still not establish
approximation, signed |W|-weighted control or useful main-term margins.
Those independent gaps remain, as does unrestricted translate realization.

### Primary inputs inspected and applicability limits

1. Sandro Bettin, *The second moment of the Riemann zeta function with
   unbounded shifts*, Int. J. Number Theory 6 (2010), 1933--1944,
   [arXiv:1111.0925v1, Theorem 1, p. 2](https://arxiv.org/pdf/1111.0925v1#page=2),
   DOI 10.1142/S1793042110003861. For complex a,b with real parts
   O(1/log Y), c=a-b, the primitive has complete bracket
   zeta(1+c)+zeta(1-c)chi(1/2+a+it)chi(1/2-b-it), and error
   O((sqrt(Y)+sqrt(|Im a|)+sqrt(|Im b|))log^2 Y).
   At c=0 take the bracket's joint limit. Rechecked the small-imaginary
   difference case and its W1/W2 split and integration by parts,
   pp. 9--10, and the other imaginary-endpoint sign in (9), p. 8.
   Reuse the parent assessment and L638 Section 1 for fixed physical
   shifts a=ir/L,b=is/L at every primitive endpoint and the exact
   Hardy phase/weight conversion on [T,3T]. Derivative order is not a
   source parameter: quantitative Cauchy extraction, all factorials,
   the full main term and conditioning remain local work. Do not import
   L638's fixed-order O(T) simplification as a growing-order estimate.

2. H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function
   Z(t)*, Bull. Lond. Math. Soc. 55 (2023), 2304--2323,
   [arXiv:2304.05178v1, Introduction (1), pp. 1--4](https://arxiv.org/pdf/2304.05178v1#page=1),
   DOI 10.1112/blms.12859. Read the even joint mean's full polynomial
   and power-saving error, the odd joint-mean bound and the explicit
   fixed-order qualification on p. 4. Constants in the odd bound
   depend on k,l; this does not supply simultaneous conditioning for
   growing k,l. Its reference [11, Theorem 3] is a lead, not an inspected
   replacement. Reuse the parent's assessment of its analytic Hardy
   conversion; no proof of its arithmetic moments is needed here.

3. bramble_trace, *Signs and uniform filtered positivity in fourth
   moments of Hardy's function*,
   [paper 36, displayed v4, 21 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/36),
   Theorem 9/(38), Section 8.1. For fixed integer p>=0,
   0<epsilon<1/2, 0<delta<1/13, fixed nonzero nonnegative smooth w,
   T<=X<=2T and T^(12/13+delta)<=H<=T, it treats all nonzero real
   polynomial filters of degree d<=L^(1/2-epsilon), with an onset
   independent of their coefficients. Reused the inspected proof cases
   in the parent assessment: Sections 8.1--8.4, (45a)--(49), and the
   denominator B_t^+(P). This is a manuscript import with its original
   qualifications. Its range includes the proposed degree with a
   suitable fixed epsilon, but its signed fourth-moment statement
   does not control our actual second Gram or bump correlations.
   Neither it nor the positive single-translation corollary imports
   the target. No source-manuscript audit is claimed.

4. Classical polynomial and analytic tools: inspected
   [DLMF Table 18.3.1](https://dlmf.nist.gov/18.3#T1), Legendre row
   (weight 1 on (-1,1), squared norm 2/(2n+1)), and the full finite
   Jacobi sum [18.5.8](https://dlmf.nist.gov/18.5#E8), whose
   alpha=beta=0 case is Legendre. These furnish exact normalization
   and coefficients, not an actual-Gram comparison. Rescaling to the
   spectral interval and all degree-dependent coefficient bounds must
   be justified in the attempt. The Laurent formula
   [DLMF 25.2.4](https://dlmf.nist.gov/25.2#E4) specifies the regular
   part of zeta at its simple pole; its use must retain the complete
   pole cancellation before differentiation. No resulting matrix
   estimate is proved here. Mathlib matching coverage is not checked.

5. For a possible correlation bound, the classical convexity bound is
   available in the author's primary exposition: T. Tao,
   [254A Supplement 3, 15 December 2014, (35)--(38)](https://terrytao.wordpress.com/2014/12/15/254a-supplement-3-the-gamma-function-and-the-functional-equation-optional/).
   It states |zeta(sigma+it)| <<_(sigma,epsilon)
   (1+|t|)^((1-sigma)/2+epsilon), 0<sigma<1, epsilon>0,
   and explains the functional-equation/three-lines inputs. The
   interpolation details are left as an exercise, so this is a citation
   of the standard named convexity theorem, not an independently
   audited proof. In particular the displayed constant depends on
   sigma. A use on complex Cauchy circles must obtain the required
   compact-substrip uniformity from the strip theorem, and bound the
   analytic Hardy phase with L465/L622; neither follows by differentiating
   a real-axis Riemann--Siegel remainder. No growing-order pointwise
   derivative estimate is asserted in this review.

### Search record, duplicates and access limits

Queries included: `Hardy Z function high derivatives mean square k
growing log T uniform derivatives`; `Riemann zeta derivatives growing
order second moment orthogonal polynomials localization`; `"Hardy"
"derivatives" "orthogonal projection"`; `"Z-function" "projection"
derivatives localization`; `"zeta" "growing" "derivatives" "second
moment"`; and exact-title queries for Minamide--Tanigawa's derivative
mean square. Generic Hardy-space/Szego projection results concern a
different space and were not imported. Queries found no matching exact
Hardy-jet bump projection theorem; this is not evidence of originality.

The Minamide--Tanigawa paper *Mean square of the derivatives of Hardy's
Z-function*, J. Math. Anal. Appl. 485 (2020), 123772,
DOI 10.1016/j.jmaa.2019.123772, is an unread overlap lead: the publisher
attempt returned HTTP 403 and only an abstract was available. No claim
about its exact order range, strongest conclusion or applicability is
made. The Lavrik uniform-derivative formula cited in secondary search
results was not read at its primary source and is also not used.
These are optional routes to sharper derivative inputs, not essential
premises: the approved attempt can use the accessible analytic generator
and named classical tools. If it requires an unread theorem instead,
stop dependent mathematics and nominate its precise source gate.

Additional access attempts: the Titchmarsh second-edition PDF title was
accessible, but targeted theorem searches timed out; no unseen theorem
number is supplied. DLMF TeX retrieval was unsupported; complete relevant
HTML formulas/table were read instead. Shell retrieval failed at DNS.
The PMC derivative-extrema paper encountered a recaptcha before its
relevant theorem was read and is not used. These access failures neither
approve nor refute any mathematics.

Scoped local checks used L637's exact definitions and preserved
absolute-budget stop, L638 Section 1 and order qualifications, L473
Section 1, the parent Gram-relative and localization-cost assessments,
and the preceding L638 audit history. No duplicate growing projection
claim was found there. L637 stops a sufficient TV error envelope;
it does not disprove projection or density. L473 supplies fixed-order
moments and an abstract-law contrast, not a growing actual-Xi theorem.
L638's two-dimensional coercivity is not a uniform family result.
No cross-notebook mathematical input was read or used.

### Approved attempt and discriminating test

EXPLORE permits exactly the saved TARGET. Keep the bump, degree, weight,
complex span and X-uniformity unchanged. Named arithmetic results are
imported by citation; only their new quantitative specialization is at
issue. A possible line to test is to retain Bettin's full second-moment
main expression, compare its polynomial form in a quantitatively
normalized basis, and estimate the bump correlations with analytic
Cauchy bounds. This is a proposed method, not a derivation or assurance
that its error survives conditioning. Track the full regular main part,
phase variation, all mixed derivatives and factorial/coefficient costs.
An O(T) fixed-order error or an inverse of the leading Gram alone is
not enough evidence for the actual projection.

Continue with a uniform o(1) bound for the actual squared projection or
a rigorous T,X sequence refuting it. If only an excessive upper envelope
is obtained, report the test as inconclusive and identify the precise
lost estimate; do not report a false lower bound or refutation. Park
this family only for a proved obstruction or the shared bounded-attempt
stop conditions. No conclusion about unrestricted dictionaries, signed
approximation or RH follows. No independent creative sign mechanism is
supplied by this source review; the absence of a realized observer with
a signed margin remains the concrete blocker to nominating one now.
