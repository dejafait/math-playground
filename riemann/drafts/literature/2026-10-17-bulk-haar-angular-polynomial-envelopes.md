# Source assessment: angular envelopes before response averaging

TARGET: Certify polynomial upper and lower bounds for L426's conditional angular mean A(g), and test whether their exact prime-Haar expectations exclude zero.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 191 searched rigorous uniform polynomial approximation, Bernstein/Chebyshev error bounds, exponential Taylor remainders and random Euler-product integer moments; inspected DLMF 3.3(i), 4.2(iii), 27.4 and Trefethen's author Chapter 8 source; compared L419, L422, L423, L426 and the step-175 and step-188--190 failures. No inspected source evaluates this prescribed mean; no novelty inference is made.
SOURCE_EVIDENCE: NIST DLMF 3.3.4--3.3.6, 4.2.19 and 27.4.1--27.4.2, online versions accessed 2026-10-17; L. N. Trefethen, Approximation Theory and Approximation Practice (SIAM, 2013), author chap8.m, Theorems 8.1--8.2 and the contour proof of 8.1, accessed 2026-10-17; reuse step-187's inspected Rump 5.5 inclusion principle and Johansson Section 2 range integration, and L422's audited exact Euler factors/tails.
COMPARISON: Standard real interpolation remainder bounds cover a uniform polynomial envelope after a certified derivative bound, and classical Euler products cover each fixed integer moment after absolute convergence. The known methods do not certify this selector's angular coefficients, the derivative bound, their conditioning, or the sign of I. Analytic Chebyshev bounds require additional complex-domain verification and are not automatic consequences of an ordinary fit.
GAP: Produce certified angular data retaining both branch stages, a uniform response-scale remainder, signed coefficient-error propagation and full fixed-degree Euler-moment bounds. No such numerical certificate, useful width or sign is established here.
REASON: Essential approximation and enlarged fixed-moment coverage are now assessed; one bounded standard-method specialization is justified. The review approves an attempt, not its mathematical conclusions or efficiency.
LITERATURE_REASON: The target changed from joint prime/angle range subdivision to polynomial approximation of the conditional angle average followed by exact Euler-moment integration; its uniform remainder and enlarged moment scope were previously uncovered.
SCOPE: Only L426's unchanged A(g), full response at sigma=5/2, L423's fixed k=13,14 mixture and L419's exact ordered two-stage selector; fixed polynomial degrees at most 32, with all resulting response moments fixed independently of height. Real interpolation with a proved derivative remainder is covered; complex Chebyshev estimates are covered only after their analytic-domain and modulus hypotheses are proved in the mathematical attempt. No altered selector, free composite phases, fitted mixture or growing-height moment order.
COVERED_TARGET: Certify polynomial upper and lower bounds for L426's conditional angular mean A(g), and test whether their exact prime-Haar expectations exclude zero.

## Gap, intended use and exact input scope

The main RH gap is global mixed positivity or another exclusion of every
off-line zero. The immediate unresolved claim here is the sign of the
fixed integral I. The intermediate target is a rigorous pair of polynomial
bounds for the conditional angular mean, integrated over the *full*
prime-Haar response. Nonzero I would, through L424--L426, distinguish
L423's law from the corresponding trajectory occupation law. It would
not refute the selected-moment obstruction, evaluate actual clipping,
supply L413's full-error regulator margin, or resolve RH.

Retain exactly

    A(g)=(1/3) sum_i integral_0^(2pi)
          Q(sqrt(3g) P u_i(exp(i theta))) dtheta/(2pi).

The essential inputs are L426's definition and averaging theorem,
L423's fixed mixture, L419's ordered equality/strict and complementary
rotation rules, L425's exact gaps and branch controls, L422's Euler
construction, and L037's arithmetic contracts. L424 and audited
L368/L369/L390 enter only through the prospective trajectory comparison.
No cross-notebook input is used. This review establishes no new lemma.

The complete `/g_full_range` value from
`scripts/discriminant/bulk-haar-integral-enclosure-188.json` was inspected:

    [164144438496585479013809/1000000000000000000000000,
     2496151417412820236290361/62500000000000000000000].

It is approximately [0.1641444,39.9384227], including the source
coefficient intervals and full multiplicative-response tail. Use the
rational endpoints, not these decimal previews, in a certificate.

## Primary theorem comparison

1. [NIST DLMF, Section 3.3(i), (3.3.4)--(3.3.6)](https://dlmf.nist.gov/3.3.i).
   The real Lagrange error is the nodal polynomial times an
   (n+1)-st derivative value divided by (n+1)!, provided that derivative
   is continuous on the closed interval containing the nodes and the
   evaluation point. The alternative contour remainder requires
   analyticity in a simply connected domain and a suitable enclosing
   contour. Read the hypotheses and both cases. A supremum derivative
   bound therefore supplies a uniform real error; sampled residuals do
   not. Rational nodes near Chebyshev points may use the real formula
   with their actual nodal polynomial; an ideal-node error constant
   cannot silently be retained after rounding nodes.

2. [Trefethen, author Chapter 8](https://raw.githubusercontent.com/chebfun/ATAP/master/chap8.m),
   Theorems 8.1--8.2, equations (8.1)--(8.3). Analytic continuation to
   the open Bernstein ellipse E_rho, with modulus at most M there,
   gives projection error 2M rho^(-n)/(rho-1) and interpolation error
   4M rho^(-n)/(rho-1). Read the annulus/contour proof of 8.1,
   including the inner-ellipse limit when analyticity is only open,
   and the reduction of 8.2 to coefficient tails/aliasing. This is
   an optional sharper alternative, conditional on verifying its
   complex-domain hypotheses for this angular mean. No analyticity
   across selector ties as a function of the *angle* is supplied.
   The real DLMF alternative avoids that requirement. Floating-point
   Chebfun resolution is not a validated remainder certificate.

3. [DLMF 4.2.19 and Section 4.2(iii)](https://dlmf.nist.gov/4.2.iii)
   supplies the entire exponential and its power series. For applying
   interpolation here, the future attempt must first rewrite the
   scaled Q at each fixed selector state, avoiding a fictitious complex
   square-root cut in g, and prove a common bound for the required
   g derivatives before integrating them. The selector is prescribed
   by theta alone in L426. Derivatives of branch locations in g must
   not be invented; nor may differentiation under the angle integral
   be assumed without the uniform bound. These are elementary
   specialization obligations, not results proved during this review.

4. [DLMF 27.4.1--27.4.2](https://dlmf.nist.gov/27.4)
   requires absolute convergence to identify a multiplicative
   Dirichlet series with its Euler product. This is consistent with
   L419's fixed-j absolute Fourier multiplication and L422's local
   factors. It supplies no high-order asymptotic or numerical precision
   guarantee. Here every required order remains finite and fixed.

The primary searches were `rigorous uniform polynomial approximation
continuous nonsmooth functions interval arithmetic Bernstein polynomial
envelopes`, `site.chebfun.org ATAP chapter 7 polynomial approximation
theorem Lipschitz Bernstein`, `site.chebfun.org ATAP chap8 Theorem 8.2`,
`site.dlmf.nist.gov exponential Taylor remainder factorial exp`, and
`random Euler product moments absolute convergence divisor function
prime local factors integer moments`. Wikipedia, secondary tutorials,
and search snippets were not used as theorem evidence. The lead
arXiv:2212.11429 on automatic Taylor-remainder bounds remains unread
and is unnecessary for this bounded real-interpolation attempt.

## High-degree moments, uncertainty and branch obligations

Reuse L419's fixed-integer C_j definition and L422 (9)--(10), including
its audited proof, rather than import a critical-line high-moment
conjecture. For a polynomial of degree d in g, substitution of L423's
fixed degree-14 polynomial calls for response powers only through
j=14d. The prospective cap d=32 thus requires at most j=448. This
is a finite algebraic bookkeeping requirement, not a uniform-in-j
asymptotic assertion. The Haar identification must be explicitly
justified by absolute multiplication and prime-character orthogonality
in the subsequent proof.

L422's *saved certificate* covers only j in {1,2,13,14,15,16}; it does
not certify the larger list. Its proof of the local ratio bound is for
any fixed positive integer j. Its prime-tail argument likewise applies
only when its displayed denominator is positive; the conversion of a
log tail r to [1,1/(1-r)] additionally needs r<1. Recheck these conditions
for every requested j. Increase the local exponent cutoff until the
next ratio is strictly below one even at p=2; do not reuse e=40
blindly. For a proposed p cutoff at most 200 and local exponent cutoff
at most 1024, certify all ratios and prime-tail inequalities explicitly;
if the prescribed caps fail, record the failure rather than omit tails.
The proof is already in L422, so the reason for additional computation
is the new finite list of orders and conditioning, not reproof of the
Euler-product theorem.

The angular node values or polynomial coefficients need interval
integration with both literal selector stages. Certified strict cells
may use existing range callbacks; cells crossing either selection
boundary need a bound for every allowed state, with their full angular
mass charged. A finite tie set has zero measure but gives no bound on
a finite unresolved neighborhood. Use the Rump inclusion and Johansson
whole-segment range method already assessed in step 187. Complex
quadrature across uncertified branches remains disallowed.

Propagate the source intervals for alpha, theta_j and C_13,C_14 through
the same exact mixture. Use certified angular value errors through
the actual Lagrange basis, or outward coefficient intervals through
all signed operations. Full prime-Haar expectations of finite
polynomials are exact mathematical expressions; their computed
Euler products have certified intervals, not exact decimal values.
Use interval arithmetic in the signed sum and retain each coefficient
and moment error after cancellation. High precision cannot remove
inherited coefficient uncertainty; any resulting floor must be reported.

## One bounded mathematical attempt and discriminating test

Permit degrees 8,16,32 within one attempt, stopping early on a sign
certificate or a diagnosed obstruction. Cap total angular callback
boxes across nodes/remainder checks at 65536, retained primes at 200,
local exponents at 1024 and outward working precision at 512 decimal
digits. These are work limits, not claims that the bounds are adequate.
A derivative-based uniform remainder must be certified on the full
rational g interval; if a complex-ellipse alternative is chosen, its
entire-domain and modulus proof must precede use of Theorem 8.2.
No unassessed approximation mechanism is authorized by this scope.

Success is a strict lower bound I>0 or upper bound I<0, retaining
all branch, interpolation, coefficient, Euler-tail and rounding errors.
If zero remains, compare the final width with the *exact* saved step-190
width. Continue this implementation only if width is at most 75 percent
of that width and a specific residual source is demonstrably reducible;
otherwise stop at the caps and preserve the certificate. A narrower
interval alone is not a sign result. If the first rigorous remainder or
conditioning budget already precludes a useful bound at the caps,
that obstruction is a legitimate negative outcome without performing
all angular evaluations. Do not resume the stopped joint-subdivision
implementation under a different name.

## Remaining qualifications

No polynomial envelope, derivative majorant, enlarged moment certificate
or value of I was derived here. Those are next-turn mathematics under
this SPECIALIZE assessment, with REPRODUCTION classification. Unknown
full Mathlib coverage remains unknown; no search of Mathlib was needed
to settle this source comparison. All actual clipping, nondegeneracy,
realization, regulator-margin and global mixed-positivity gaps remain.
