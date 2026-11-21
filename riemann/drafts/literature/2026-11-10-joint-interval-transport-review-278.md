# Joint observations: completed interval-transport source comparison

TARGET: Assess whether the exact moving-to-common-interval correction J_n(X_n-tilde_X_n) admits a subexponential norm bound.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step279 searched exact Laguerre/Mangoldt interval corrections, compensated weights, short-interval prime theorems and weighted explicit formulas; compared the named November10 transport, Vaughan, variance and spectral records. Inspected primary Guth-Maynard2405.20552v2 Corollaries1.3-1.4/section13.2 and Johnston2411.13791v2 Theorem2.1/section4; queries and scope below. No matching signed transport theorem located; no novelty inference.
SOURCE_EVIDENCE: Reuse audited L990/C990a/L993, L985 definitions, audited L989 and the canonical Gorodetsky2211.08973v6 Lemma5.2/AppendixA input. Primary additions: https://arxiv.org/html/2405.20552v2#S13.SS2 and https://arxiv.org/html/2411.13791v2#S2, with complete relevant pointwise/averaged and zero-splitting proof cases read. No inspected result supplies (T).
COMPARISON: Finite explicit formulas retain signed prefixes; newer pointwise prime theorems give relative errors outside the required weighted scale, and almost-all conclusions do not control the prescribed endpoints. Johnston's omega=o(log x) hypothesis excludes a direct constant-width-strip specialization. L993 pays inversion only; stop244 remains scoped to its sources.
GAP: The required subexponential bound (T), with every prime power and compensator, remains unproved. No applicable signed residual estimate or new cancellation mechanism was established by this bounded review.
REASON: New theorem-level comparisons park direct import/absolute-prefix payment of (T), not (T) itself. EXPLORE records completed bounded source coverage, not approval to repeat this stopped estimate chain. A distinct generating-representation nomination requires its own review.
LITERATURE_REASON: Moving arithmetic intervals and a subexponential signed-correction target are new hypotheses and conclusions outside reviews274-276; ready matrix and explicit-formula ingredients do not cover this estimate.
SCOPE: Actual von Mangoldt weights; exactly L985's K_m and full (exp(u),exp(v)] endpoints; exactly L993's J_n on its existential tail. No RH, off-line zero, simplicity, endpoint clearance, bound on other outputs or automatic L984(H) transfer.

## Original nomination, preserved as reviewed scope

The following nomination was uncovered at the start of step279.
Its missing-coverage language is superseded by the completed comparison
below; its target and definitions are preserved.

This is an uncovered continuation, not an approved research target.
Step278 completed only the earlier L993 audit. A separate literature
turn must assess the statement below; no new lemma is derived here.

For a real polynomial f and 0<=u<v define the finite compensated
functional, with all prime powers and the indicated exact endpoints,

    T(f;u,v)=sum_(exp(u)<m<=exp(v)) Lambda(m)*f(log m)/m
                                      -integral_u^v f(t)dt.

Keep K_m(t)=[L_(m-1)^(2)(t)-1]/(m-1), as in L985/L990, and set

    B_m=T(K_m;m,2*m),
    X_n=(B_n,B_(n+1),B_(n+2))^T,
    tilde_X_n=(T(K_n;n,2*n),T(K_(n+1);n,2*n),
                                      T(K_(n+2);n,2*n))^T.

Use the exact real J_n=[a_n/||a_n||_2;b_n/||b_n||_2;c_n] from
audited L993. The proposed estimate is

    For every epsilon>0 there is a finite C_epsilon such that
    ||J_n*(X_n-tilde_X_n)||_2<=C_epsilon*exp(epsilon*n)
    for every integer n beyond L993's one fixed definition onset. (T)

These definitions specify the target; no decomposition, upper bound,
counterexample or necessity of (T) for RH is asserted. In particular,
one must not treat a bounded interval length in log coordinates as
a bound on the exponentially scaled arithmetic functional.

The plausible downstream use is to connect common-interval estimates
to the three actual moving-block observations before applying L993.
Even (T) leaves bounds for J_n*tilde_X_n, signed arithmetic forcing,
other zeros, both complements and L984(H) unresolved. The Euclidean
bound asks for two-sided information; L984's one-sided premise does
not supply it. No RH implication follows from (T) alone.

The bounded review should compare the exact signed boundary functional
with available compensated explicit-formula and prime-sum theorems,
reusing the already inspected finite weighted formula in review254.
Retrieve any genuinely relevant primary theorem's full hypotheses and
essential proof cases. Do not repeat the scalar pivot/volume routes
or approve another absolute-value/centered-Vaughan calculation without
a new signed input. Stop244 remains evidence on its precise scope.

Continue only if a matching theorem can be imported, or one distinct
and bounded signed-cancellation test is justified with its missing
source coverage paid. If the exact correction merely reproduces the
unpaid signed prefixes and no distinct mechanism is found, record that
comparison and select a different target. A failed majorant or a
synthetic quartet would not refute the actual arithmetic bound (T).

Essential local context is L985's definitions, L990/C990a/L993's
matrix, and L984's downstream premise. L988/L989 and review254 are
representation leads only until their exact relevant statements are
read for this target; no unaudited signed conclusion is imported.
No cross-notebook input. Matching Mathlib coverage is unchecked.

Next routing is literature_comparison, standard/high. A new central
creative attempt is desirable, but no independent signed input for
this correction is yet justified. Do not label a finite interval
identity, a repeated envelope estimate or the completed conditioning
specialization creative. This nomination neither spends an additional
mathematical attempt nor approves its own coverage.

## Completed source comparison — step279, 10 November 2026

This literature-only turn establishes no estimate or identity for (T).
The main gap is still L030-L032/C032a actual-Xi positivity and
L966/L968 signed forcing. The exact intermediate target is (T),
with its proposed transport use and independent unpaid outputs as
specified above. The continuation test was a matching source or a
distinct bounded signed mechanism, rather than another absolute bound.

### Ready coverage and local overlap

Read L985 for definitions only, L993 through its matrix/conditioning
contract, L984 through its one-sided premise, and L989 through its
finite formula, error proof and relevant audit. Reuse the complete
Gorodetsky contract and AppendixA inspection in
[the canonical source input](../../foundations/2026-11-10-finite-weighted-landau-input.md)
and review254. The primary Lemma5.2 s=1 statement was checked again
only for the changed transport application. It controls a weighted
prefix with a finite zero sum, not the sign of that prefix.
L989 already pays its particular cutoff/jump errors while explicitly
retaining both signed arithmetic prefixes. It is not silently extended
to all the shifted endpoints or integrated polynomial weights here.

Stop244 and review243 already exclude automatic centered-Vaughan
payment; review231 already records the averaging/covariance gap in
the older interval-variance theorem. Stop267 concerns the earlier
synthetic-to-arithmetic gap. Its former lack of joint conditioning
has since been addressed by L993, but its missing arithmetic bounds
have not. None of these historical stops is a global ban.
Reviews245/246 already cover full-Li versus moving-block spectral
scope and warn against a formal moving-endpoint generating exchange.
The fixed synthetic quartet and scalar recovery tests are complete;
they are not repeated. No cross-notebook mathematical input is used.

### New pointwise and almost-all interval comparison

L. Guth and J. Maynard, *New large value estimates for Dirichlet
polynomials*, [arXiv2405.20552v2](https://arxiv.org/html/2405.20552v2#S1),
7 April2026, Corollary1.3: for fixed epsilon>0, sufficiently large x and
x^(17/30+epsilon)<=y<=x^.99,

    pi(x+y)-pi(x)=y/log x+O_epsilon(y*exp(-(log x)^(1/4))).

Corollary1.4 has y in [X^(2/15+epsilon),X^.99] and an exceptional
set of integer starting points, rather than every starting point.
[Section13.2](https://arxiv.org/html/2405.20552v2#S13.SS2)
was read completely: the pointwise case uses truncated explicit
formula and zero-density bounds; the almost-all case integrates the
squared zero sum, including cross terms. The latter cannot remove
exceptions at prescribed endpoints. Fixed-log-length transport bands
are not the stated sublinear-y intervals; subdivision and growing-degree
weight control would need justification. More fundamentally, the
pointwise conclusion supplies relative error, not the near-square-root
saving demanded by the exponential kernel scale recorded in L985.
This is a contract comparison, not a newly derived weighted bound or
a claim that the paper's every possible consequence has been excluded.

### Generic zero-free-to-PNT comparison and its scope restriction

D. R. Johnston, *Zero-density estimates and the optimality of the
error term in the prime number theorem*,
[arXiv2411.13791v2, Theorem2.1](https://arxiv.org/html/2411.13791v2#S2),
header21 October2025 (rendered title date24 August2026), assumes C^1
decreasing 0<eta(t)<=1/2 on t>=0, no zeros beta>1-eta(|t|), and
N(sigma,t)<<t^(A*(1-sigma)^B)*(log t)^C uniformly on
[sigma_0,1], with A>0,B>=1,C>=0,1/2<sigma_0<1. Here N counts
zeros with sigma<beta<1 and 0<Im(rho)<t, with multiplicity.
For sufficiently large x it also requires a unique minimizer of
eta(t)*log x+log t (over t>=1 as in (1.5)), whose minimum omega obeys
2log log x<=omega=o(log x). For Delta_3=|psi(x)-x|/x it gives

    Delta_3 << exp(-omega)*exp(2*A*omega*(omega/log x)^B)*omega^C.

The constant depends on the two input estimates. The full relevant
[section4 proof](https://arxiv.org/html/2411.13791v2#S4), all three
real-part ranges, was read; it takes absolute zero terms before
splitting. This supplies no signed correlation theorem. Its stated
omega=o(log x) hypothesis does not authorize substituting a constant
eta from the notebook's fixed-strip input. No such specialization is
made. This rules out that particular direct import, not consequences
of other zero-free-to-PNT theorems.

The supplied October baseline and external-input register were read
before comparing prime estimates. Their stronger fixed half-plane
statements are reused within their recorded verification limits.
They do not assert RH or a signed growing-degree transport bound.
The classical estimates above are therefore scope comparators, not
claims to be the notebook's strongest available zero localization.
No fixed-strip PNT estimate, contour shift or RH-conditional bound
is derived in this turn.

### Search evidence, decision and remaining work

Queries included `Laguerre polynomials von Mangoldt sums short
intervals weighted explicit formula`, `prime number theorem short
intervals fixed ratio exponential polynomial weight zero density
subexponential Laguerre`, `"Laguerre" "von Mangoldt" "interval"`,
`"Laguerre" "prime" "compensated"`, and `Guth Maynard large value
estimates Dirichlet polynomials primes short intervals theorem`.
Exact local searches were confined to the named November10 records,
foundations and the necessary lemma definitions/proof ranges.
No failed search is evidence of novelty. Johnston-Yang2204.01980,
higher-uniformity almost-all results and 2610.18923 are unread leads,
not imported theorems or scheduled source retries. No essential source
blocker was encountered. Full matching Mathlib coverage is unchecked.

The new comparisons give an informative negative source result:
neither the inspected modern interval theorem nor the generic PNT
theorem directly pays (T); Gorodetsky still leaves the signed prefixes.
No distinct signed estimate was justified. Park direct arithmetic
payment by this chain, preserve (T) as open, and record
[the scoped stop](../../ATTEMPTS/2026-11-10-joint-interval-transport-direct-import-stop-279.md).
Do not interpret this as a counterexample, an RH implication, or
proof that every conceivable source or mechanism fails.

The different continuation is a source review of an exact actual
moving-band degree-generating representation, defined in
[review279](2026-11-10-moving-band-degree-germ-review-279.md).
It tests the representation/exchange obstacle before any all-zero
singularity or cancellation argument; it is not another norm-majorant
or finite-quartet test. Its coverage is REVIEW_REQUIRED, with no new
formula, convergence domain or singularity claim established here.
A creative attempt remains blocked until that precise analytic
interface and a discriminating signed test are justified. No lemma,
mathematical script, PROOF.md argument or DAG edge was changed.
