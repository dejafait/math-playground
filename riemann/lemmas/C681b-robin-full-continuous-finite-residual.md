# Corollary 681b: full continuous Robin residual at four finite sizes

## Hypotheses

Use L666's full rational W, L673's exact phase-aligned nodes and L681's
positive weights (1), without changing any original unit residues.
Put x=-5/4, R=11/8, U=121/64, n=12q+3, and define

    F_q(u)=W_(-R)(u)-1-sum_(a!=x) w_a W_a(u),  |u|=1,
    e_q=-log(||F_q||_2)/n.

The L2 norm uses normalized angular measure. This result concerns only
q in {1,2,4,8}. Its arithmetic certificate uses standard IEEE-754
binary64 operations with outward `nextafter` rounding and correctly
rounded square root; the recorded implementation uses NumPy float64.
No trigonometric library, fitted nodes, sampled-norm assumption or
unbounded-q numerical extrapolation is used.

## Conclusion

The following strict norm enclosures and enclosing exponent intervals
hold; every displayed decimal endpoint is an exact terminating decimal.

| q | n | ||F_q||_2 | e_q |
|---|---|---|---|
| 1 | 15 | (3.456, 3.458) | [-0.0827127, -0.0826741] |
| 2 | 27 | (3.037, 3.040) | [-0.0411800, -0.0411433] |
| 4 | 51 | (2.144, 2.148) | [-0.0149910, -0.0149543] |
| 8 | 99 | (1.985, 1.990) | [-0.0069509, -0.0069254] |

Thus both largest cases fail the predeclared finite diagnostic test
e_q>1/100. Park that diagnostic of these unmodified weights. This does
not exclude a faster asymptotic rate, an arbitrary polynomial prefactor
n^K, another onset Q, or other positive weights. It does not contradict
L681's upper bound with its large absolute constant. It supplies no
arbitrary-weight obstruction, original H estimate, support/realization
bridge, actual-Xi signs or RH candidate. This finite computational
result has not received a separate independent critical audit.

## Proof

### 1. Source scope and reason for this calculation

The unchanged ready EXPLORE assessment is
`drafts/literature/2026-11-02-discrete-parameter-positive-quadrature.md`.
It covers the exact prescribed-node residual with its fixed anchor and
complete continuous norm. L681 supplies the weights, not these evaluated
norms; its rate 3/500 is below 1/100. C681a's fixed-rectangle integrand
obstruction does not bound this residual. The earlier angular-mean and
polar screens did not enclose this norm. This is a finite calculation
on existing constructions, not a new general quadrature theorem or a
claim of originality beyond the inspected sources.

Use the standard named Cauchy integral formula for Laurent coefficients.
The required source contour theorem is the finite Cauchy residue theorem
already imported in L681 from NIST DLMF, Section 1.10(iv),
[equation (1.10.8)](https://dlmf.nist.gov/1.10#E8).
The Laurent coefficient formula is its specialization to the two
concentric circles and the corresponding monomial. No general contour
theorem is reproved. The following family-specific bounds pay the actual
integration error, which no cited source supplies automatically.

### 2. A complete angular integration error bound

For every parameter used here, 5/4<=|a|<=11/8: L673 gives
|x+-iy_k|^2<353/200<R^2, and a=-R is included separately.
The angular poles of W_a are among t_j*x/U and a/t_j for 1<=j<n.
Their moduli are respectively less than 80/121 and at least 5/4.
The j=0 factor x/a is retained and is constant in u. Consequently F_q
is holomorphic on a neighborhood of the closed annulus

    9/10<=|u|<=10/9.

For u in this annulus and 0<=t<1,

    |x-tu| < 5/2,               |a-tu| > 1/8,
    |Uu-ta| < 7/2,              |Uu-tx| > 2/5.

Indeed the sharper lower differences are 5/4-10/9=5/36 and
(121/64)*(9/10)-5/4=289/640; the upper sums are
5/4+10/9<5/2 and (121/64)*(10/9)+11/8<7/2.
Thus each j>=1 paired product factor has modulus less than 175,
and |x/a|<=1. The number of nonanchor nodes is 4q=(n-3)/3 and
L681 gives 0<w_a<13/3. In particular throughout the annulus

    |F_q(u)| <=1+(1+13*(n-3)/9)*175^(n-1)
               <=2*n*175^n.

Let F_q^sharp(u)=conjugate(F_q(1/conjugate(u))) be the rational
reflection, and g_q=F_q*F_q^sharp. Inversion interchanges the two
annulus radii, so g_q is holomorphic on the same closed annulus
and neighborhood, and

    |g_q(u)|<=M_n=4*n^2*175^(2*n).

On the unit circle g_q(u)=|F_q(u)|^2. Write its Laurent coefficients
as c_m. The two Cauchy coefficient bounds give

    |c_m|<=M_n*(9/10)^|m|,  m in Z.

These estimates imply absolute uniform convergence on the circle.
Its normalized integral is c_0. At all N-th roots of unity, finite
averaging of each monomial is zero unless its index is divisible by
N. Exchanging that finite average with the absolutely convergent series
is justified. Therefore with N=16384 and u_l=exp(2*pi*i*l/N),

    | ||F_q||_2^2 - N^(-1)*sum_(0<=l<N)|F_q(u_l)|^2 |
       <=2*M_n*(9/10)^N/(1-(9/10)^N) <10^(-250).       (1)

The final comparison is checked as an exact rational inequality for
each n=15,27,51,99. This is an estimate for the complete rational
function; there is no Fourier cutoff or omission of cross terms.

### 3. Exact-node and angular-node enclosures

The generator is
`scripts/one-sided-hankel/robin-continuous-residual-certificate.py`.
Machin's named identity pi=16*atan(1/5)-4*atan(1/239), with 60-term
alternating arctangent series and the next-term remainder, encloses pi
as rational endpoints. For each k=0,...,15, 48 dyadic bisections in
(k+1/2,k+5/8) use 30-term alternating arctangent bounds to enclose
the unique L673 root. Each bisection chooses a side only when its
entire rational function-value interval has one strict sign. Final
endpoint signs are checked again exactly. L673 proves uniqueness;
no rounded root is substituted for the exact one.

The primitive angle theta=2*pi/N lies in (0,1). Sixteen terms of
the sine and cosine Taylor series enclose its primitive circle point;
the absolute first omitted term bounds each remainder. All inputs and
operations in these series are intervals. Binary powers and the
fourteen binary digits of l give boxes containing each exact u_l,
including l=0 and every point through l=N-1. This construction uses
no floating trigonometric value. The maximum box coordinate width
is checked to be below 10^(-8). That width is propagated rather than
discarded; it is not itself a claim about the final residual error.

### 4. Arithmetic propagation and the complete norm

Real interval endpoints are rounded outward after each addition,
subtraction, multiplication, division and square root. Multiplication
takes all four endpoint products; division excludes zero; squaring
includes zero exactly when its input interval crosses zero. Rational
inputs are bracketed by the neighbors of their binary64 conversion.
Thus each primitive encloses its exact value, including subnormal
rounding if encountered. No unchecked exponential or logarithmic
floating evaluation enters the norm certificate.

Products use Euclidean complex balls to avoid rectangular wrapping.
For a box, its computed midpoint c is enclosed with a radius bounding
both coordinate distances by outward arithmetic and the square root
of their squared sum. For balls A=(a,r_a), B=(b,r_b), the center
operation is first evaluated as rectangular point intervals and
replaced by a ball with center-rounding radius r_0. Multiplication adds

    |a|*r_b+|b|*r_a+r_a*r_b

to r_0, with upper bounds for both center moduli. Addition adds
r_a+r_b. For division, put q=a/b and require a certified lower
bound m<=|b|-r_b with m>0. The exact identity

    (a+delta_a)/(b+delta_b)-q
           =(delta_a-q*delta_b)/(b+delta_b)

shows that adding (r_a+|q|*r_b)/m to r_0 suffices. A bound for
|q| includes the center-rounding radius. These are elementary
perturbation identities needed to certify this implementation, not
assumed accuracy of a complex-library division. All scalar and vector
denominator margins are checked by the interval operations.

Every W product includes x/a and all 1<=j<n factors, using interval
nodes and weights. The generator forms W_(-R) minus the unit anchor
and all weighted complex terms as in F_q before taking a squared modulus.
Ball moduli are enclosed by the center-modulus interval plus/minus
the radius, clipping the lower endpoint at zero, then squaring.
Every one of the N lower/upper squared-modulus bounds is retained.

For the sum of N nonnegative binary64 endpoints use the conservative
relative rounding allowance gamma=N/(2^52-N). Each summand's accumulated
rounding multiplier is a product of at most N-1 factors (1+delta_j),
|delta_j|<=2^(-53). Its deviation from one is at most
(N-1)*2^(-53)/(1-(N-1)*2^(-53)), smaller than gamma.
The still looser chosen gamma covers any addition ordering, including
NumPy's pairwise order. All sums are finite, nonnegative and ordered.
Dividing the rounded lower sum by 1+gamma and the upper sum by
1-gamma, using exact rational arithmetic, encloses the true discrete
mean. Finally subtract/add 10^(-250) from (1).

The generator checks that the resulting full squared-mean interval
lies strictly between the squares of the claimed rational norm
endpoints in the table. It also verifies positive weight bounds and
finiteness of every sample enclosure. The four squared-mean widths
are less than 2.5e-7, 6.5e-7, 9.9e-7 and 2.0e-6 respectively.
These rounded width summaries are ancillary; all exact endpoints
are saved in the certificate. All 63 checks pass, with no failures.

Reproduce with

    OPENBLAS_NUM_THREADS=1 python3 scripts/one-sided-hankel/robin-continuous-residual-certificate.py

The full evidence is
`scripts/one-sided-hankel/robin-continuous-residual-certificate.json`,
including source hash, NumPy version, exact pi/root endpoints, every
sample interval, all squared-mean endpoints and all checks. An initial
rectangular-product implementation failed the requested tight norm
enclosures at q=4,8 through accumulated interval width. Its source
and evidence are preserved in
`scripts/one-sided-hankel/robin-continuous-residual-rectangular-failed.py`
and the matching `.json`. Those failed enclosures are not premises
of the table; the failure was numerical enclosure, not a counterexample.

### 5. Effective exponents and interpretation

For a rational v>1 put t=(v-1)/(v+1), so 0<t<1. The positive
atanh series gives

    2*sum_(j=0)^79 t^(2j+1)/(2j+1) <=log v
      <=2*sum_(j=0)^79 t^(2j+1)/(2j+1)
           +2*t^161/[161*(1-t^2)].

Apply the upper logarithm bound to the upper norm endpoint and
the lower logarithm bound to the lower endpoint; negate and divide
by n. Exact outward rounding to multiples of 10^(-7) gives the
exponent table. Reproduce the four checks with

    python3 scripts/one-sided-hankel/robin-continuous-residual-exponent-bounds.py

The matching `.json` stores the complete rational logarithm bounds
and binds them by SHA256 to the norm certificate. All four checks pass.
In particular ||F_q||_2>1 and e_q<0<1/100 in all four cases.

The test was a criterion for whether to pursue asymptotic cancellation
of the unmodified L681 weights immediately. Its failure changes that
research decision only. Any finite collection is compatible with an
eventual bound n^K*exp(-(1/100+epsilon)*n) after a larger onset;
even that bound need not give e_q>1/100 at these four sizes.
No asymptotic impossibility is inferred. Independent unresolved
bridges to the original H and actual Xi remain open.

## Mathlib

Full matching coverage for this four-size Robin residual certificate,
its exact-node specialization and interval implementation was not
checked; unknown availability is not evidence of absence. Cauchy's
integral formula, Laurent series, finite roots-of-unity orthogonality,
elementary ball perturbation identities and norm comparisons are
supporting mathematics. No formal Mathlib verification or originality
claim is made.
