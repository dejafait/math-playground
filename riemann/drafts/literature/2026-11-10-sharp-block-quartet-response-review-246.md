# Sharp moving-block response to one synthetic zero quartet

TARGET: Test whether the exact moving-block response W_n of the fixed synthetic quartet rho=3/4+i*10^13 has positive exponential upper excursions, retaining all four terms, degree averaging and both endpoints.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step247 separately reviewed step246's nomination; reused its Laguerre/weighted-prime and full-Li comparisons, searched exact truncated-Laplace/finite-interval variants and discrete trigonometric sign tools. No inspected matching W_n theorem was located; this is no novelty claim. Exact queries and unread leads are recorded below.
SOURCE_EVIDENCE: Live DLMF18.15.17-20,10.17.1-3/iii,2.4.10-13 and2.3.4-6 inspected; reuse DLMF18.18.18 through L985. Added Tao Higher Order Fourier Analysis, 5June2012 author manuscript, Proposition1.1.2, Exercise1.1.5 and Proposition1.1.5, pp5-7; Fukshansky Geometric Number Theory, live undated author notes, Theorem6.2.1, p138. Contracts and limits below; parent Voros comparison reused, not reopened.
COMPARISON: Known tools cover the exact finite connection, uniform bulk expansion, finite endpoint integration and resonant linear-sequence structure. They do not give this signed moving-integral conclusion. Approve only the missing specialization, including its remainder and discrete-sign obligations; no general theorem needs reproof.
GAP: Compute the signed endpoint specialization and prove or refute positive exponential upper excursions at integer n, with all four terms and smaller remainder. Source availability is sufficient for an attempt, not evidence that these mathematical obligations hold. Actual-zero realization and actual B_n remain outside scope.
REASON: Separate source approval completed in step247 without deriving a new result. The exact saved target is ready for one REPRODUCTION specialization attempt; no arithmetic gain, certified originality or creative-mechanism claim.
LITERATURE_REASON: The startup REVIEW_REQUIRED gate required separate coverage of the new sharp moving-quartet target; its endpoint and discrete-sign contracts were missing from the ready arithmetic and full-Li assessments.
SCOPE: Integers n>=2; exact K_n from the L981/L982 degree-average context and L985; synthetic simple quartet only; finite integrals on [n,2*n]. No RH, actual off-line zero, isolation in zeta, simple zeta zeros, arbitrary-frequency independence or full-zero-sum exchange.

## Exact proposed calculation

Use the existing kernel

    K_n(u)=(n-1)^(-1)*sum_(k=2)^n L_(k-1)^(1)(u).

Fix rho=3/4+i*10^13 and prescribe the four-element model set
Q={rho,conjugate(rho),1-rho,1-conjugate(rho)}, all with weight1.
Define, without claiming it equals any part of actual B_n,

    W_n=-Re sum_(q in Q) integral_n^(2*n) exp((q-1)*u)*K_n(u)du.

Determine whether

    limsup_(n->infinity) log(1+max(W_n,0))/n > 0.

The height is fixed, never allowed to grow with n. It is synthetic,
not a claimed off-line zero in a known finite verified-zero range.
No existence claim, changed compensator or prime substitute is made.

Require a controlled signed asymptotic including both endpoints and
all quartet terms, and a rigorous integer-index positive subsequence
or its failure. An amplitude envelope does not establish excursions.
Check rescaled phase, analytic domain, endpoint dominance and remainder
bounds; retain the -1 in L985's exact identity. Do not differentiate
an O remainder or interchange a degree sum with moving endpoints.
If the endpoint theorem misses an n-dependent amplitude, justify
finite integration by parts with explicit errors instead. Import
general theorems precisely; only the missing specialization is sought.

## Relevance and stopping rule

The main bottleneck is actual-Xi positivity and L966/L968 signed forcing.
The actual block target remains B_n<=C_epsilon*exp(epsilon*n) for
every epsilon>0. A positive model rate would expose a single-mode
obstruction to automatic spectral payment of this kernel; it would
give no actual B_n lower bound, RH equivalence or arithmetic estimate.

Continue only with a complete signed asymptotic, smaller controlled
remainder and justified integer positive subsequence. Zero rate or
exact leading cancellation is an informative stop; an unpaid sign or
remainder comparison is unfinished, not positive evidence. No quartet
parameter sweep. Later actual-zero transfer or other-zero domination
requires a new concrete target and source gate. L981/L982 normalization,
L986's proper-power payment and the original compensator stay fixed.
Both complements, L984(H) and arithmetic realization remain open.
Full matching Mathlib coverage is unchecked.

## Separate source approval — step247, 10 November 2026

The nomination above was REVIEW_REQUIRED at invocation start. This
section completes that source-only gate; it proves no specialization.
The whole supplied PROOF and DAG were used before reading L981/L982's
normalization and L985's connection/bulk proof. L985's Vaughan argument
is not audited or imported. Its scoped stop and step244's centered
source limit were read; lobe, average, variance, Selberg and whole-Li
comparisons are reused through the completed parent assessment.
No global ban on spectral or Selberg methods is inferred.

### Inspected primary contracts

1. [DLMF18.15.17-20](https://dlmf.nist.gov/18.15#iv), live on the
   checked date, gives the scaled Bessel expansion for fixed alpha
   and fixed M, uniformly for 0<=x<=1-delta, with nu=4d+2alpha+2
   and xi=(sqrt(x-x^2)+arcsin(sqrt(x)))/2. Its error is the Bessel
   envelope times O(nu^(-2M+1)), inside the stated exponential
   prefactor; A_0=1 and B_0 is explicit. The source's compact,
   fixed-unscaled-argument expansion18.15.14 is a different contract.
   Reuse L985's d=n-1, alpha=2, x in[1/5,1/2] check and its
   finite connection from [18.18.18](https://dlmf.nist.gov/18.18.E18).
   The next proof must substantiate the source-to-kernel application;
   a source review does not audit the entire unaudited L985.
2. [DLMF10.17.1-3](https://dlmf.nist.gov/10.17#i) gives fixed-order
   large-argument Bessel expansions in |arg z|<=pi-delta, with
   omega=z-order*pi/2-pi/4. Both orders2 and3, the correction and
   additive error must survive specialization. Positive real arguments
   qualify. The sharper real remainder rules in
   [10.17(iii)](https://dlmf.nist.gov/10.17#iii) were also inspected:
   z>0, order>=0; truncation ell must be at least
   max(order/2-1/4,1) for the even series and
   max(order/2-3/4,1) for the odd series. Do not import a
   first-neglected-term assertion at a different truncation.
3. [DLMF2.4.10-13](https://dlmf.nist.gov/2.4#iii) requires phase and
   amplitude analytic on an open domain containing the contour,
   apart from the allowed endpoints. At the selected endpoint its
   convergent expansions require Re(lambda)>0, mu>0 and p_0!=0,
   continuous branches, and |theta+mu*omega+arg p_0|<=pi/2.
   The parameter sector has width<pi; convergence at the other
   endpoint is absolute and uniform. The real phase difference is
   strictly positive away from the selected endpoint and uniformly
   bounded away from zero near the other endpoint. This is not a
   uniform theorem for an unchecked parameter-dependent amplitude.
4. [DLMF2.3.4-6](https://dlmf.nist.gov/2.3#i) provides the alternative
   finite Fourier integration-by-parts expansion: finite a,b,
   smooth q on[a,b], both endpoint series, with the error after
   truncation controlled by x^(-r) times the total variation of
   q^(r-1). Its printed asymptotic has fixed q as x tends to infinity.
   For a family q_n, use the finite identity and bound its remaining
   integral explicitly. Neither this result nor2.4 permits
   differentiation of an unknown O remainder. The general theorems
   are imported; only their finite-family application is to be proved.
5. T. Tao, *Higher Order Fourier Analysis*,
   [author manuscript dated5June2012](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-142-tao7-higher-book-05june2012.pdf#page=13),
   Proposition1.1.2/Exercise1.1.5/Proposition1.1.5, printed pp5-7,
   was inspected, including the irrational and rational-relation
   cases of the linear decomposition proof. Weyl's criterion tests
   every nonzero integer character. Full-torus equidistribution of
   n*alpha+beta requires k*alpha!=0 in the circle for every such k.
   Without that premise, Proposition1.1.5 gives a totally
   equidistributed subtorus component plus a periodic component.
   Thus resonances must be retained, not assumed absent. These
   results do not assert positivity of the target's trigonometric
   expression on the actual orbit. That sign/nonvanishing check is
   precisely part of the specialization, or can be handled by finite
   geometric sums for the characters actually needed.
6. L. Fukshansky, *Geometric Number Theory*,
   [live undated author notes](https://www1.claremontmckenna.edu/pages/faculty/lenny/papers/GNT_lecture_notes.pdf#page=142),
   Theorem6.2.1, printed p138, states Lindemann-Weierstrass:
   exponentials of finitely many distinct algebraic numbers are
   linearly independent over the algebraic numbers. Its complete
   statement was inspected. This optional named input can resolve
   exact phase resonance only after the research proof shows that
   the numbers in question meet its algebraicity/distinctness
   hypotheses. No such application or frequency independence is
   established here. Only this theorem is approved, not every
   surrounding corollary in the notes; no transcendence reproof.

### Comparison, search and allowed mathematical difference

The strongest applicable inspected results are uniform polynomial
asymptotics and the linear-sequence structure theorem above. None
directly evaluates the moving signed transform or supplies its positive
integer subsequence. The parent assessment's inspected Voros full-Li
cases remain contrast only; its existing Tao explicit-formula comparison
already records the smooth-weight, fixed-height and absolute-tail
limitations. No larger external passages or repeat searches on those
ready scopes were needed.

Additional queries were `"Laguerre" "truncated Laplace" asymptotic
moving interval`, `"Laguerre" "truncated Laplace" "asymptotic"`,
`"Laguerre" "Li" "finite interval" zeta`,
`"trigonometric polynomial" "positive" "mean" almost periodic sign
changes`, `site.terrytao.wordpress.com equidistribution linear sequences
torus Weyl criterion`, and `Lindemann Weierstrass theorem nonzero
algebraic exponential lecture notes theorem site:edu`. The truncated
Laplace operator thesis and survey hits remain unread leads, not
matching-theorem evidence. A guessed Tao blog URL was inaccessible;
the inspected author book supplies the needed discrete source instead.
DLMF TeX endpoints were unsupported by the browser; the complete
relevant HTML equations and hypotheses were inspected. Neither issue
blocks the stated attempt. No novelty follows from a search miss.

Approve SPECIALIZE for the exact TARGET only, with expected classification
REPRODUCTION. Keep fixed tau=10^13 while n tends to infinity: constants
and onset may depend on tau. A uniform-in-growing-height theorem is
neither needed nor approved. Use the exact finite average and retain
the -1. The remaining work is to control the finite integral's signed
endpoint terms, the integrated additive error, all four prescribed
terms and their cancellation, and the integer-index sign test. If a
rescaling creates n-dependent phases or amplitudes, their uniform
bounds must be justified within the specialization; the source gate
does not supply them. No formal generating-function exchange,
infinite zero sum or contour transfer is approved.

Success requires the positive limsup stated above, a smaller rigorous
remainder and an integer subsequence. Exact leading cancellation or
zero rate stops this diagnostic; an unproved remainder or sign leaves
unfinished reasoning and supplies no positive evidence. This attempt
may reveal a necessary spectral obligation but cannot pay actual B_n,
its complements or L984(H). No general theorem needs reproof, and no
new result was derived during approval. Full matching Mathlib coverage
is unchecked. Expected routing is proof_attempt/development; the lack
of a new actual signed arithmetic input still blocks justified creative
escalation. Do not invent a different creative target to fill a quota.
