# Three-degree endpoint-null filter — source assessment

TARGET: Assess the normalized three-degree endpoint-null filter for eventual definition and retained positive exponential quartet response, comparing known results and the recorded smoothing stops before any calculation.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step259 searched exact endpoint-null and prescribed-zero/consecutive-Laguerre variants, inspected Duran2507.22425v1 Lemma5.2 and Theorem1.5 and Krattenthaler2023 Theorem1/Section2.2, and checked the nominated local stops. No inspected theorem covers this exact shifted, n-dependent, normalized bulk family; no novelty inference.
SOURCE_EVIDENCE: New primary comparison: Duran, arXiv2507.22425v1 (30July2025), Section5/(5.1)-(5.6), Lemma5.2 and Theorem1.5; Krattenthaler, Ramanujan J.61 (2023),597-627, Theorem1/(1.1), Section2.2/(2.2)-(2.3). Live DLMF18.15.17-20 rechecked; reuse review246's finite integration and integer-orbit contracts and L985's exact connection. Precise links, hypotheses and exclusions below.
COMPARISON: Fixed-coefficient exterior asymptotics and Christoffel determinant identities do not establish the shifted filter's nondegeneracy, conditioning or signed quartet response. Uniform scaled Laguerre asymptotics and the ready finite-integration/orbit tools support one specialization attempt, without assuming its outcome or paying the original arithmetic criterion.
GAP: Eventual d_n!=0, normalization error control, three neighboring degrees on the common interval, exact constant corrections, the full signed quartet expansion and integer positive subsequence remain mathematical obligations. Actual B_n/L984(H) transfer, other-zero control and both complements remain independent gaps.
REASON: The previously uncovered family's theorem-level comparison is complete enough for a bounded specialization, not an IMPORT or a claimed result. The separately nominated test in review259 requires next-turn approval; this literature-only turn derives no result and changes no lemma or mathematical script.
LITERATURE_REASON: Startup REVIEW_REQUIRED covers a changed kernel whose n-dependent normalization and common-interval signed response lie outside ready review246; additional source comparison was essential rather than a repeat of its unfiltered assessment.
SCOPE: Real coefficients, integer n>=2, exact K_j(u)=[L_(j-1)^(2)(u)-1]/(j-1), common interval [n,2n], L987's fixed synthetic quartet, full prime-power endpoints in any later arithmetic interpretation. No RH, actual off-line zero, simplicity, automatic sign or criterion transfer.

## Original nomination: main gap and three compared directions

Actual-Xi positivity and signed arithmetic forcing remain the main
gap. L989 leaves two signed prefixes, and L988 leaves a low-zero
remainder. Their technical bounds do not pay actual B_n or L984(H).

Compare three directions at nomination level only:

1. Direct payment of the original signed A(x) endpoint pair: no new
   signed input is available; repeating the ready derivative or
   centered-Vaughan contracts repeats L985 and step244's losses.
2. Automatic degree averaging or lobe signs: L982's step235 inverse
   and the step233 lobe stop block those mechanisms on their scopes.
3. Constrain a three-adjacent-degree test to have zero endpoint values,
   then test whether a signed spectral signal survives. Select only
   this finite viability question for source review, without assuming
   that a changed weight pays the original arithmetic criterion.

These are reused scoped comparisons, not new impossibility results.
The selected family below is specified without proving any claim.

## Exact family and proposed bounded test

For every integer n>=2 propose the real rows

    a_n=(K_n(n),K_(n+1)(n),K_(n+2)(n)),
    b_n=(K_n(2n),K_(n+1)(2n),K_(n+2)(2n)).

Let d_n be their ordinary cross product. Only if d_n!=0 define
c_n=d_n/(|d_(n,0)|+|d_(n,1)|+|d_(n,2)|), with fixed orientation,
and propose

    F_n(u)=sum_(j=0)^2 c_(n,j)*K_(n+j)(u), n<=u<=2n.

Eventual nonvanishing of d_n and useful size of F_n are obligations,
not hidden assumptions. Do not replace the family by a fitted
polynomial or change its orientation after observing signs.

Keep rho=3/4+i*10^13 and Q={rho,conjugate(rho),1-rho,
1-conjugate(rho)}, each with weight1, as synthetic parameters only.
If the family is eventually defined, the proposed diagnostic is

    Z_n=-Re sum_(q in Q) integral_n^(2n) exp((q-1)*u)*F_n(u)du,
    limsup_(n->infinity) log(1+max(Z_n,0))/n > 0.

The nominated literature turn was to determine whether this exact target is
covered, overlaps a recorded failure, or has adequate tools for one
later attempt. It may reject the nomination on source/relevance
grounds; it may not derive or silently approve a different family.

A later attempt must check both endpoint constraints, normalization,
conditioning, all three neighboring degrees on the common interval,
retained -1 corrections, all quartet terms, a smaller remainder and
integer-index signs without unproved frequency independence. Infinite
vanishing of d_n, failed normalization control or an amplitude-only
conclusion is a specific stop. No degree or quartet parameter sweep.

Plausible use: test whether eliminating the leading endpoint functional
preserves spectral sensitivity before proposing a full zero estimate.
Even success supplies no actual off-line zero, other-zero dominance
or signed prime estimate. A later arithmetic functional must retain
the compensator with F_n and all prime powers; its transfer to the
original K_n block and L984(H) needs a separate test. Missing transfer
limits relevance and can justify abandoning an unhelpful filter.

## Reuse and routing

Essential context: L985 exact connection only, audited L988 finite
decomposition and L989 technical cost, L987 synthetic diagnostic only.
Compare L982 step235, step233 lobe and step244 centered-source stops,
and reviews245/246's sharp/smooth/full-Li distinctions. Search exact
endpoint-null/adjacent-degree statements and stronger orthogonal-
polynomial or Christoffel-type modifications in primary sources.
Those terms are unread leads, not imported theorems. Endpoint
vanishing alone is not a new cancellation theorem.

At nomination, new-family coverage and original arithmetic transfer
were missing. The completed source comparison below addresses only
the former. Routine finite algebra must not be labeled creative for
scheduling. Full matching Mathlib coverage remains unchecked and
unknown. No cross-notebook input is used.

## Completed source comparison — step259, 10 November 2026

This is a literature-only completion of the exact saved TARGET.
The supplied overview and DAG were used first. Narrow local searches
of the nominated November10 assessments/attempts found only the
nomination and earlier Christoffel leads, not a matching completed
filter test. L985's connection/bulk setup, L987's complete signed
argument, and the relevant L988/L989 definitions and endpoint scope
were read. No other notebook was read; existing work was preserved.

### Primary comparisons

Antonio J. Duran, *Zeros of linear combinations of Laguerre
polynomials*, [arXiv2507.22425v1, 30July2025, Section5](https://arxiv.org/html/2507.22425v1#S5),
defines q_m=sum_(j=0)^K gamma_j L_(m-j)^alpha, with fixed real
coefficients, gamma_0=1 and gamma_K!=0. Lemma5.2/(5.6) supplies
scaled asymptotics uniformly on compact subsets of C\[0,4]. This
excludes the bulk arguments of the nominated test. Theorem1.5 also
requires its coefficient polynomial to have no nonreal root in the
closed unit disk, and alpha>=K-N_nr-1; its conclusions concern zero
counts, simplicity and interlacing, not our integral's sign. Both
real-rooted and nonreal-root cases of the statement were read.
Neither statement covers the added constant correction or establishes
uniform estimates for the endpoint-determined coefficients as n
changes. No hypotheses on that coefficient polynomial have been
verified here. These are inspected comparisons, not imported filter
theorems or an assertion that the filter violates their conclusions.

C. Krattenthaler, *Hankel determinants of linear combinations of
moments of orthogonal polynomials, II*, [Ramanujan J.61 (2023),597-627,
Theorem1/(1.1) and Section2.2/(2.2)-(2.3)](https://link.springer.com/article/10.1007/s11139-021-00514-8),
published online22November2021, was inspected in the publisher HTML
and [publisher-version PDF, PDF pp2,7-8](https://d-nb.info/1250655633/34#page=2).
Theorem1 assumes monic degree-m polynomials orthogonal for a
characteristic-zero linear functional with every squared norm
nonzero. It identifies a modified-moment Hankel determinant with a
consecutive-polynomial evaluation determinant divided by the
Vandermonde factor. It is an identity, not a lower bound for the
modified determinant. Section2.2 explains the Christoffel quotient.
The shifted kernels in this test have not been shown to form such
an orthogonal family. This source therefore supplies no automatic
nonzero cross product or conditioning estimate here. No new
orthogonality or determinant specialization is derived or imported.

### Applicable tools and the precise unproved difference

[DLMF18.15.17-20](https://dlmf.nist.gov/18.15#iv), live checked on
10November2026, was read through its complete scaled formula and
uniformity statement. It fixes alpha and truncation M, sets
nu=4m+2alpha+2 and xi=(sqrt(x-x^2)+arcsin(sqrt(x)))/2, and expands
L_m^alpha(nu*x) uniformly for 0<=x<=1-delta, delta>0 fixed.
Its remainder is additive and includes the Bessel envelope. It does
not assert a relative error at oscillatory zeros or a lower bound
for any determinant. The fixed-unscaled-argument formula18.15.14
has a different domain and cannot replace it.

Reuse [review246](2026-11-10-sharp-block-quartet-response-review-246.md)
for DLMF10.17's fixed-order positive-real Bessel expansions, the
finite integration identity rather than an unchecked n-dependent
Watson application, and Tao's *Higher Order Fourier Analysis*,
5June2012 manuscript, Proposition1.1.2, Exercise1.1.5 and
Proposition1.1.5 (printed pp5-7). Its linear-sequence decomposition
retains rational relations; no full-torus independence is available
by default. Reuse its precisely cited Lindemann-Weierstrass input
only if a later application verifies the needed hypotheses.

These tools cover the ingredients, not the desired mathematical
conclusion. The later proof must check their scaled domain for each
of the three degrees on [n,2n]; substituting n+j into L987 alone
changes its integration interval. It must control coefficient errors
through normalization, and may not divide an additive asymptotic by
an unboundedly small unexamined cross product. Eventual definition
is required on all sufficiently large integer n; proving definition
only on a favorable subsequence would change the family. A global
uniform conditioning constant is not assumed: the actual error
comparison must be sufficient for whatever conclusion is claimed.

No differentiation of an O remainder is licensed. Preserve every
-1/(n+j-1) term, both endpoints and all four synthetic terms. A
signed leading expression must be nonzero and positive on a justified
integer subsequence with smaller remainder; a norm, continuous-n
positive point or phase-independence assumption cannot replace that
test. Finite exact algebra and calculus may be supplied as the local
specialization; none of the general imported results needs reproof.

### Recorded failures, access and search limits

Read the precise step233 lobe-pair counterexample, step235 moving
average inversion stop and step244 centered-Vaughan source limit.
Their scopes remain unchanged. The selected endpoint-row constraint
is a different finite viability question, not evidence of signed
prime cancellation or a repair of those failures. Review245/246's
full-Li versus sharp moving-block comparison is reused. The reviewed
L989 restoration cost is already below its benchmark; refining it
again is not the selected mechanism.

Queries used included `Laguerre polynomials linear combination three
consecutive prescribed two zeros Christoffel transformation asymptotics`,
`Laguerre polynomials bulk Plancherel Rotach asymptotics uniform adjacent
degree n x oscillatory`, `"Laguerre" "endpoint" "annihilation" polynomials
filter`, `"Laguerre" "three consecutive" "prescribed" zeros`,
`"Laguerre" "endpoint-null"`, and `Christoffel formula orthogonal
polynomials determinant nonnegative polynomial Szego 2.5 pdf`.
No exact matching result was identified in the inspected sources;
this bounded search does not certify novelty or exhaust the literature.

Szego's1975 book PDF timed out. *Asymptotic expansions for Laguerre-like
orthogonal polynomials*, JCAM159(2),325-339 (2003), was403-blocked;
its search preview is not evidence of its theorem hypotheses. Neither
is essential to this attempt: the accessible primary determinant
comparison above and the ready uniform bulk tools suffice. DLMF18.2(xii)
was checked but is not a substitute Christoffel determinant theorem.
These access failures do not justify a retrieval-only continuation.

### Decision and bounded continuation

SPECIALIZE: source coverage permits one attempt at the exact fixed
family, with expected REPRODUCTION classification. It neither
establishes eventual definition nor predicts a positive answer.
The ready continuation is recorded separately in
[review259](2026-11-10-endpoint-null-degree-filter-test-review-259.md)
for next-turn approval. A zero-rate conclusion, infinite exact
degeneracy, or a rigorous obstruction to the required normalization
would be informative; unpaid signs or uncontrolled errors must be
saved as unfinished work. No degree or quartet sweep is authorized.

Downstream use remains a conditional design diagnostic: decide
whether exact endpoint removal can retain spectral sensitivity
before asking for actual-zero and arithmetic transfer. It does not
pay B_n, L984(H), either complement or the full positivity gap.
There is no new mathematical result or RH candidate in this turn.
The unavailable arithmetic transfer and the purely synthetic scope
still block justified central-gap creative escalation. No extra
browsing of unchanged coverage is called for after separate approval.
