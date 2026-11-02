# Weighted differential certificate: bounded-attempt source coverage

TARGET: Test whether weighted integration by parts gives a uniform positive common-observer lower bound exceeding L622's complete transfer error for the Xi signed integral with a_n=mu(n)/(sqrt(n) m_N), m_N^2=sum_(n<=N)mu(n)^2/n and N=floor(T^(1/100)), retaining every derivative of the amplifier and smooth weight.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact/standard-term searches for weighted Laguerre integration by parts, derivative-weighted mollified fourth moments and amplified Hardy differential inequalities; inspected the primary statements/cases below and reused the collective-spectrum and L399 source comparisons. No inspected result supplies the raw-Mobius common-observer coercive margin; no novelty or exhaustive absence claim.
SOURCE_EVIDENCE: Hughes–Young arXiv:0709.2345v2 Theorem 1.1/(11)–(17), printed pp. 3–5, https://arxiv.org/pdf/0709.2345v2#page=3; Bui–Hall arXiv:2304.05178v1 Propositions 1–2, mollifier definition preceding (3), Section 5/(21)–(22), https://arxiv.org/html/2304.05178v1; Bui–Hall–Subira Jorge arXiv:2511.14415v1 Sections 4.1–4.6, Theorem 4.1/(13)–(21), https://arxiv.org/html/2511.14415v1#S4; standard integration by parts, chain and product rules. Exact hypotheses, read cases and exclusions are recorded below.
COMPARISON: Standard calculus supplies identities, and the reused shifted-moment imports supply tools for later fixed-jet estimates. Bui–Hall's tapered mollifier and fourth-power formula do not match the raw square; the amplified Wirtinger result concerns endpoint-zero functions and gap tests. None supplies this signed lower bound. L399, stationary-law and periodic-storage stops have different observables/hypotheses and do not settle it.
GAP: A later attempt must derive the actual weighted identity, retain all weight/amplifier/observer derivatives and completion curvature, and prove a uniform positive margin above L622's full error. No such identity for the target, relative differential-cost bound, sign or onset is established by this review.
REASON: Essential standard/source coverage is sufficient for one bounded physical-certificate attempt without a new arithmetic theorem. Whether derivative costs admit coercivity is the test, not an assumed source input. Stop at the first uncontrolled cost; do not resume the stopped cutoff-boundary mechanism or replace the raw amplifier by a tapered one.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED changed the mechanism to a physical differential certificate. This turn supplies the missing derivative/mollifier/weighted-inequality comparison, reusing ready arithmetic coverage rather than repeating its discovery.
SCOPE: The actual Z,W,A, fixed nonnegative smooth w, T<=X<=2T and single normalized real observer c of L622; the original normalized Mobius amplifier is held fixed during height differentiation, with all of its height derivatives retained. No RH, spacing, zero-free, generic bandlimited-sign or independent-observer premise.

The original nomination below is preserved as history. Its pending-review
language is superseded by the completed comparison appended here. This
changed ready assessment is for separate next-turn gate approval; no
mathematical attempt on the differential certificate took place here.

This is a nomination, not a ready assessment. The next invocation is
literature-only. Preserve the displayed mathematical target rather than
silently replacing it by a review of the failed arithmetic boundary.
Search primary results for weighted Laguerre/quartic integration by
parts, derivative-weighted mollified moments, and relevant obstructions;
reuse the existing moment and L399 comparisons within their scopes.
The elementary identity alone would not supply the quantitative sign.

The intended bounded test, if coverage is approved, is to retain the
full physical weight w_XT |M|^2 and completion curvature, and compare
the resulting positive quartic terms with every differential cost.
The required normalized margin is strictly greater than
C_w[T^(-17/80)/log^4 T+T^(-199/100)/log^2 T], uniformly in X and
the common real unit observer. No new coefficient search, cutoff
extension, or generic positivity inference is part of this nomination.
Stop if the first derivative-weighted cost cannot be bounded relative
to the positive term; do not drop it using bandwidth alone. No such
identity or inequality was derived while preparing this assessment.

Essential local inputs for later applicability are L622, L624 Section 5,
L471's exact completion identity, and L619's audited H=T bounds, with
L018/L465 as qualified there. L622-L624 remain unaudited; Hughes–Young
and its holomorphy input remain named imports. The raw boundary
obstruction is a contrast, not an input implying a physical sign.
Mathlib matching is unknown; no cross-notebook result is needed.

Pointwise initial signs at exceptional heights and all-degree mixed
positivity remain independent gaps. A physical sign certificate would
decide only the fixed amplifier direction. No complete RH candidate is
proposed and no novelty is inferred from this incomplete comparison.

## Completed source comparison — 1 November 2026

### Gap, target and discriminating test

The main gap remains actual-Xi pointwise initial signs at unbounded
heights and all-degree mixed positivity. The unchanged TARGET asks only
about one raw Mobius amplifier and every common real unit observer.
A proved positive average with a controlled margin would exclude this
detector direction as a negative witness. It would leave other
amplifiers, exceptional heights, higher signs and RH unresolved.

The later test must compare the normalized integral in L622 (1) with
the complete error

    E_w(T)=C_w[T^(-17/80)/log^4 T+T^(-199/100)/log^2 T].

Require a strict positive margin greater than E_w(T), uniformly in
T<=X<=2T and c0^2+c1^2=1, beyond a justified onset. The constants in
L622 are existential; a finite-height claim would need additional
effective bounds. An uncontrolled derivative cost or a bound larger
than the positive contribution ends this single mechanism test as
inconclusive or obstructed, according to the evidence. A formal positive
term, bandwidth bound, floating matrix, or nonnegative prefix is
insufficient. No new inequality or value of a differential cost was
derived in this literature turn.

### Primary tools and precise scope limits

1. C. P. Hughes and M. P. Young, *The twisted fourth moment of the
   Riemann zeta function*, J. reine angew. Math. 641 (2010), 203–236,
   [arXiv:0709.2345v2, Theorem 1.1/(11)–(17), printed pp. 3–5](https://arxiv.org/pdf/0709.2345v2#page=3).
   Reopened the versioned primary PDF: v2 is dated 27 September 2007,
   with a separate 26 November 2024 compilation date. Reinspected the
   theorem's hypotheses, all six terms and the p. 5 holomorphy remark.
   It assumes coprime h,k with hk<=T^(2/11-epsilon), four complex shifts
   O(1/log T), nonnegative smooth support in [T/2,4T], derivatives
   O_j(T0^(-j)), and T^(1/2+epsilon)<<T0<<T. Its absolute remainder is
   O(T^(3/4+epsilon)(hk)^(7/8)(T/T0)^(9/4)); 1/sqrt(hk) occurs in the
   main integral, not this error. Complete permutation-sum holomorphy
   is a named CFKRS Lemma 2.5.1 import, not positivity.

   Reuse [the completed collective comparison](2026-11-01-collective-arithmetic-signed-spectrum.md)
   and [its ready application assessment](2026-11-01-collective-arithmetic-spectral-test.md)
   for the prime-power factors, collision-safe differentiation, stronger
   BBLR comparison and coefficient conventions. L622 Sections 1–3 keep
   the exact phase inside the smooth source weight. Its Section 2
   explicitly verifies complex-weight decomposition and the twist range;
   its full application remains unaudited. The present raw coefficients
   are within L622's specified unit-norm family. These observations do
   not automatically extend its error to every differentiated amplifier
   or weight generated by a new identity. A later application must
   identify each finite coefficient sum, any rescaling, uniform smooth
   weight constants and absolute error before using it. In particular,
   do not treat the oscillatory factor |M|^2 as an undifferentiated
   source weight satisfying T-scale derivative hypotheses.

2. H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function
   Z(t)*, [arXiv:2304.05178v1](https://arxiv.org/html/2304.05178v1),
   11 April 2023. Read the mollifier definition preceding (3) and Propositions 1–2 in Sections
   3–4, and the Section 5 passage preceding (22). Proposition 1 allows
   fixed polynomial derivative filters, P(0)=0 and vartheta<4/7, for
   a mollified **second** zeta moment. Proposition 2 is a shifted
   **fourth** zeta moment with |M|^4, P(0)=P'(0)=0 and vartheta<1/8.
   The initial mollifier definition also fixes P(1)=1. Section 5 obtains
   fixed normalized derivatives by Cauchy's formula on small complex
   circles with a uniform error. This is relevant derivative-estimate
   methodology, already assessed locally; it is not a relative positive
   differential-cost theorem for the present |M|^2 statistic.

   The raw sharp cutoff corresponds to no vanishing taper, whereas
   these formulas require vanishing conditions at the cutoff. Scalar
   normalization by m_N and the short exponent 1/100 do not meet those
   polynomial conditions. We do not substitute P=1, take an unproved
   taper limit, or import the fourth-power main term for a square.
   The long Proposition 2 main expression is not an input requiring
   rederivation. Its exact source scope, rather than an evaluation of
   that expression, suffices for this exclusion.

3. H. M. Bui, R. R. Hall and M. Subira Jorge, *Amplified fourth moment
   of the Riemann zeta-function and applications*,
   [arXiv:2511.14415v1, Sections 4.1–4.6](https://arxiv.org/html/2511.14415v1#S4),
   18 November 2025. The older assessment covers Theorem 1.1's specified
   divisor-polynomial amplifier and its fourth power. The new relevant
   reading was (13)–(21), the full Theorem 4.1 proof and the Section 4.6
   derivative/Cauchy passage. Theorem 4.1 states, for endpoint-zero
   differentiable complex f and v>=0,

       3 lambda_0(v) integral_a^b |f|^4
        <= ((b-a)/pi)^4 integral_a^b |f'|^4
           +6v ((b-a)/pi)^2 integral_a^b |f f'|^2,
       lambda_0(v)=(1+4v+sqrt(1+8v))/8.

   The proof passes through |f|, using the real Hall inequality and
   the modulus derivative bound. Its stated claim of isolated zeros
   is not automatic for arbitrary differentiable functions; no general
   zero-regularity extension from that proof is imported here. Sections
   4.1 and 4.5 use consecutive zeros and a hypothetical upper gap bound
   to reach their gap contradiction. Our fixed height window and common
   observer have neither that gap hypothesis nor this observable.
   Section 4.6/(20)–(21) retains derivatives of both zeta and amplifier
   in the differentiation operator before applying uniform Cauchy
   estimates. This directly excludes dropping amplifier derivatives
   on the strength of their short length. Neither this inequality nor
   its moment application asserts the target's weighted Laguerre sign.
   It is a scope comparison, not an imported coercivity theorem.

4. Ordinary integration by parts for C1 functions on a compact interval,
   the chain/product rules and the fundamental theorem of calculus are
   the standard deterministic identity inputs. The reused
   [quartic-stationarity comparison](2026-10-31-quartic-stationarity-bulk-separator.md)
   records a primary finite-interval transport formulation (Lasserre et
   al., SIAM J. Control Optim. 47 (2008), (2.12), with both endpoints).
   No probabilistic stationarity or expectation interchange is needed
   for a compactly supported actual-function integral. A later short
   product-rule verification is necessary to specify the new weighted
   observable and every generated term; it is an application of known
   calculus, not a reproof of a moment theorem. It is not performed here.

### Local duplicates and failure comparison

Read L622's hypotheses, full transfer statement, exact extraction,
phase/weight application and final scope warning; L471 (7); L399's
hypotheses, conclusion and imported-component scope; the Mobius boundary
and zero-shift-freezing ATTEMPTS records and the preceding Mobius history.
Reused the collective source assessments rather than auditing all
arithmetic proofs again. The boundary evidence remains exactly L624
Section 5's qualified obstruction: it gives no signed tail sign.
Neither that route nor the failed row, freezing and prefix tests is
reopened by this approval.

Targeted integration-by-parts/derivative searches in the related
L471–L479/L575/L622/L624 files and in local literature/failure records
found elementary Fourier integration and different physical statistics.
L399 uses a tapered short mollifier, a different complete discriminant
and an ordered response limit; its negative mean does not decide the
present raw-amplifier form. L580's necessary quartic stationary identity
and its finite-law obstruction have translation-invariant path-law
hypotheses absent here. L589/L592/L593/L595 concern specified quadratic
or homogeneous coupled periodic-storage classes and clipped second
moments. Their statements were checked as potential obstructions;
they do not cover this actual arithmetic-weighted quartic integral.
Their failures remain valid within their scopes; no generic periodic
or one-height positivity inference is authorized. No matching proof
of the present full weighted certificate was identified in these
bounded local checks.

### Exact later scope and unresolved assumptions

Keep the original w,T,X,N,m_N,M and common real observer. During a
height derivative T,X,N,m_N,c and log T are fixed parameters. Retain
derivatives of M, its conjugate, w_XT and the observer, as well as
L471's completion-curvature term. Differentiating with respect to T
or changing the cutoff, taper or observer per frequency is outside
this assessment. Work with zero-safe products; neither M'/M nor a
logarithmic derivative at an amplifier or Xi zero is an allowed
shortcut. Smooth nonnegative w need not have a positive lower bound;
an estimate involving division by w or regularity of a fractional
power of w needs its own justification.

The retained full physical weight, exact identity and any lower/upper
comparison are still unproved for this target. The small logarithmic
bandwidth is not by itself a weighted relative norm estimate. The
attempt must obtain a bound for the actual correlated derivative
costs, not replace their weighted norms by unweighted ones. Moment
asymptotics and absolute bounds may be applied only with checked
uniformity and enough precision for E_w(T); a relative O(1/log T)
error cannot silently replace the smaller L622 error.

Essential continuation inputs are L622/L624, L471 and L619(H=T), with
L018/L465 as qualified there. L622–L624 and the named arithmetic
manuscript/holomorphy imports remain unaudited. This bounded attempt
can use those explicitly conditional inputs, but a successful margin
would still require their critical audit before promotion to a checked
Xi claim. Source coverage for a mathematical test is ready; its desired
answer is not assumed. Mathlib matching is not checked and unknown.
No cross-notebook input is used.

Queries included `Hardy Z function weighted Laguerre inequality
integration by parts mollifier fourth moment derivative`, `mollified
fourth moment zeta derivatives Mobius unweighted mollifier integration
by parts positivity`, `zeta Hardy Z amplifier integration by parts
fourth moment derivative gaps Bui Hall`, `weighted Laguerre inequality
integral`, and exact `weighted integration by parts zeta` and
`Mobius Laguerre fourth positivity` searches. Irrelevant Laguerre
orthogonal-polynomial material and snippets were not theorem evidence.
Searches also returned the already assessed filtered-positive/growing-
order papers; their untwisted or positive-order/log-height scopes remain
excluded by the reused collective comparison. Short-mollifier and
mollification-limit papers returned as leads were not read and are not
inputs or essential source blockers for this bounded physical test.

Decision: EXPLORE for the unchanged target, subject to separate approval
of this changed assessment on the next turn. This completed turn is
LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. It supplies source scope
and an actionable later test, not a new mathematical result or a
solution of the main gap. No lemma, mathematical script, DAG edge or
main argument was changed.
