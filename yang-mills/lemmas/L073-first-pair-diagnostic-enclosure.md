# L073 — Certified signs of both finite first-pair diagnostics

## Hypotheses

Use L072's exact finite tensor construction of L070(9), including its
Psi_13 probe sector after the L071 cancellation, at N=24, a=1/3 and
tau=1/16. Keep L008's exact cutoff and central differences, all relative
one-form modes, every axial level, upper row, normal end edge and pinned
prefix. The diagnostic has its defined physical lower-face distance sa.
It is not assumed to approximate L070(1)'s original circulation/path trace.

Use the explicit arithmetic model of L039: standard binary64 rounded
addition and multiplication or fused multiply-add, arbitrary summation
order, no overflow, and the stated allowance for local underflow. The
integer arithmetic is exact. This is an informal computer-assisted
proof under that model, not a formal verification of Python, NumPy,
BLAS or the processor. The finite-array comparison checks below do not
supply an arithmetic or statistical premise for the signs.

## Conclusion

Both N=24 diagnostics are strictly negative:

    -200.408 < D_(3,1/3) < -200.362,
     -20.752 < D_(6,1/3) < -20.210.                       (1)

The total absolute errors about the stored dyadic centers are respectively
below 0.022571 and 0.270823, hence below the required threshold 1.
These include coefficient, eigenbasis, heat, node/weight and tensor
arithmetic errors, the retained quadrature error, and both infinite
integration tails. No relative mode is truncated.

This is a sign result only for the finite diagnostic. It gives no mesh
limit, original-trace coefficient, direct first-pair O(N²) bound,
response logarithm, interacting reflected-error bound, or mass gap.

## Proof

### 1. Exact retained operator and a uniform quadrature bound

Import L072's finite identities

    D_i=Tr(M F Q_i^A F),
    F=Delta^(-1) exp(-t_0 Delta),       t_0=9/16.          (2)

Its one-dimensional maps define the component blocks exactly; its
spectral decomposition has one edge zero mode and N-1 positive vertex
modes in each coordinate. The full one-form eigenvalues obey

    lambda_* = 12 sin²(pi/48) <= lambda <= 16.

Concavity of sin on [0,pi/2] gives sin(pi/(2N))>=1/N, hence the
convenient lower bound g=12/N²=1/48 for every full eigenvalue.

Use the positive 20-point Gauss–Legendre rule in the shifted variable
v=t-t_0, on [0,1/32] and the fifteen panels [2^j,2^(j+1)],
j=-5,...,9. There are 320 nodes, ending at v=1024. Let B(lambda)
be its exact weighted sum of exp(-lambda v). The quadrature nodes and
weights here are the exact mathematical rule, before stored arithmetic.

Import the standard Gauss–Legendre remainder theorem in L039(4):
for a C^(2m) function on an interval of length h the error is at most
C_m h^(2m+1) sup |f^(2m)|, where

    C_m=(m!)^4 / [(2m+1)((2m)!)^3].

All functions used here are entire. On [b,2b], multiplying this error
for exp(-lambda v) by lambda gives
C_m (lambda b)^(2m+1) exp(-lambda b). The positive exponential series
implies x^k exp(-x)<=k! for x>=0, so each dyadic panel contributes at
most C_m(2m+1)! to the normalized error. On the initial panel,
lambda/32<=1/2, and the normalized error is at most C_m.
Consequently, with m=20,

    epsilon_q=C_20 [1+15(41!)],
    |lambda B(lambda) - (1-exp(-1024 lambda))|
        <=epsilon_q.                                    (3)

The certificate encloses lambda_* from its exact trigonometric formula;
let ell=3 times the lower endpoint of the enclosed one-dimensional
first positive eigenvalue. It verifies ell>=g. Define

    epsilon_t >= exp(-1024 ell)

as the upper endpoint of the exact interval exponential evaluation.
The missing scalar tail exp(-1024 lambda) is bounded by epsilon_t
for every full mode, including modes with one constant edge factor.
Thus epsilon=epsilon_q+epsilon_t satisfies

    |lambda B(lambda)-1|<=epsilon.                        (4)

Set F_R=exp(-t_0 Delta) B(Delta). The finite spectral theorem, (4),
and exp(-t_0 lambda)<=1 give

    ||F-F_R||<=epsilon/g,  ||F||<=1/g,
    ||F_R||<=(1+epsilon)/g.

The exact identity
F Q F-F_R Q F_R=(F-F_R)QF+F_R Q(F-F_R)
therefore yields

    |Tr(M F Q_i^A F)-Tr(M F_R Q_i^A F_R)|
       <= d B_M B_i (2epsilon+epsilon²)/g²,               (5)

where d=4N(N-1)^3 and the B's bound the relevant operator norms.
In particular (5) controls both infinite tails and their corner as
well as the two retained quadratures. It does not assume that the
signed integrand is positive or bound only sampled eigenvalues.

### 2. Explicit coefficient and norm bounds

From L008's definition, 0<=rho<=1 and f=x rho has |f|<=3. The
zero-extended central difference has infinity norm at most 1/a.
The product arrays of L072 thus give

    W_*<=8*3*(3/a)=72/a,
    W_3<=2*(3/a)^2=18/a²,
    S_6<=18/a².

For the last inequality each derivative of a displacement summand
is at most 9/a²: if it differentiates a cutoff factor, use
|C rho|<=1/a; if it differentiates an f or Cf factor, use
|Cf|<=3/a and |C²f|<=3/a². Each shear has at most two such summands.
These bounds cover transition vertices and zero-extended differences.

Use L072's norm inequalities, replacing sqrt(N-1) by the upper bound N:

    d=1168032,
    B_M=12 a N(1+4N)(72/a)=2011392,
    B_3=16*(18/a²)=2592,
    B_6=192*(18/a²)=31104.                               (6)

The rational evaluation of (5) is below 0.022569 for i=3 and
0.270822 for i=6. It uses the actual certified ell only for the
exponential tail; the denominator in (5) remains the coarser exact
g=1/48. Thus the norm and spectral constants are not inferred from
numerical eigenvalue samples.

### 3. Enclose every input to the exact rule

The implementation is
`scripts/combined-ward-response/enclose_first_pair_diagnostic.py`.
It expands precisely L072(5)–(7), using ordinary matrix transposes and
coefficient adjoint averages, not an average of a squared clover for
the triplet. In its zero-based coordinate convention there are 12
component terms in M, 24 in Q_3^A and 96 in Q_6^A. Algebraically
canceling coefficient summands are retained rather than deleted using
an approximate-zero threshold. Selecting opposing component blocks
in the trace leaves 28 triplet and 72 shear products. Every product
keeps all four coordinate factors.

For clarity the eigenbases used to evaluate the coordinate factors are

    V_(j,k)=sqrt(2/N) sin(pi j k/N),       1<=j,k<N,
    E_(l,0)=1/sqrt(N),                    0<=l<N,
    E_(l,k)=sqrt(2/N) cos(pi(l+1/2)k/N),  1<=k<N.

These are the orthonormal pinned vertex and edge bases of L072's
incidence matrices. They diagonalize the Laplacians with eigenvalues
4 sin²(pi k/(2N)); the edge k=0 eigenvalue is zero. Orthonormality is
the finite sine/cosine orthogonality identity, equivalently the
geometric-sum identity for the 2N-th roots of unity. No approximate
diagonalization or removal of a small eigenvalue is used.

Reuse the integer interval machinery of L037 and L039, at scale 10^180.
Machin's identity with alternating arctangent bounds encloses pi.
Integer square-root inequalities enclose the two normalizations.
The sine/cosine algorithm reduces nonnegative angles to at most 1/8,
encloses their alternating Taylor sums through degrees 60/62 (cosine)
and 61/63 (sine), and restores angles by double-angle identities.
Reducing an integer angle index modulo 4N is exact periodicity.

At the 23 rational interior coordinates the cutoff is exactly 1 on
|x|<=5/2 and 0 on |x|>=3. On the remaining coordinates its two
positive exponentials and their positive sum are enclosed directly
from L008's formula. All coefficient derivatives are the specified
finite differences, not continuum derivatives or interpolants.

Twenty disjoint root brackets in (-1,1), of width at most 10^-90,
have opposite certified signs of P_20 at their endpoints. Degree 20
and the intermediate value theorem identify all simple roots.
Legendre recurrence and
P'_20(z)=20(P_19(z)-z P_20(z))/(1-z²)
enclose the positive weights 2/[(1-z²)(P'_20(z))²]. Exact affine
maps give all 320 time/weight intervals. Machine proposals locate
brackets but are not trusted for inclusion.

All 7680 coordinate heat entries exp(-t lambda_k), including k=0,
are enclosed by the interval exponential routine of L039: divide the
argument until it is at most 1/8, use alternating lower/upper Taylor
bounds through orders 61/60, then square outward. Integer endpoint
operations preserve inclusion even if a final lower endpoint is zero.
No machine exponential, sine, cosine or square root is a numerical
accuracy premise.

### 4. Retained tensor and arithmetic propagation

For a component pair alpha,beta, transform each one-dimensional M
factor with the corresponding alpha/beta bases and each Q factor
with the beta/alpha bases. If their transformed entries are m_ab
and q_ba, the coordinate trace at quadrature times s,t is

    sum_(a,b) exp(-s lambda_(alpha,a))
                    m_ab q_ba exp(-t lambda_(beta,b)).    (7)

The order agrees with L072(2); swapping the dummy integration labels
does not transpose an unpaired physical operator. Multiply the four
coordinate traces and the exact component coefficient, then contract
both positive time weights. Sum all 100 component products.

Integer intervals are converted to binary64 midpoint-radius pairs
only after exact rational containment checks. Every subsequent matrix
product, entrywise product and sum carries an outward radius by L039's
proved rules. The dot error bound is Higham, *Accuracy and Stability
of Numerical Algorithms*, 2nd ed., SIAM (2002), Lemma 3.1, applied as
in L039 to at most 2n+2 elementary operations. All coordinate dot
inner dimensions are at most 24. Final 320-node contractions are split
into blocks of size at most 160, so every dot obeys L039's n<=276
hypothesis. Its conservative G>10^-12, denominator check and 10^-290
underflow allowance remain valid. Scalar additions and products use
its 10^-15 relative allowance. No overflow occurred in any saved factor
or contraction. This establishes enclosure by induction through the
actual arithmetic operations under the stated model.

The resulting retained centers and radii, with exact dyadic values
in the certificate, are approximately

    center_3 = -200.384962701,  radius_3 < 0.000001594,
    center_6 =  -20.4808377793, radius_6 < 0.000000241.

These radii include all retained coefficient, basis, node/weight,
heat and tensor arithmetic errors. Add (5), using exact rational
arithmetic, to obtain total errors below 0.022571 and 0.270823.
The final endpoint comparisons with (1) are strict rational checks.

### 5. Full evidence and qualifications

Reproduce with

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/enclose_first_pair_diagnostic.py
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/audit_first_pair_diagnostic.py

The complete certificate, factor archive and audit are respectively

    scripts/combined-ward-response/first-pair-retained-enclosure-certificate.json
    scripts/combined-ward-response/first-pair-retained-enclosure-factors.npz
    scripts/combined-ward-response/first-pair-retained-enclosure-audit.json

The audit reads every saved record. It recomputes all primitive
trigonometric, coefficient, root/weight and heat intervals; checks the
complete component-pair coverage and coefficients; verifies the factor
archive's dimensions, finite entries, nonnegative radii and hashes;
checks all stored heat/weight conversions; and aggregates all 100 term
intervals using exact rationals. It independently recomputes the
quadrature/tail budget and both strict final signs. It does not
independently repeat every tensor matrix multiplication; those rely on
the generator's inclusion induction, not merely archive previews.

As separate implementation checks, both Q matrices and M are evaluated
on deterministic seeded rank-one component fields using the original
full-array incidence, clover, upper-row and prefix routines. These
floating comparisons test the tensor assembly at N=24; they are not
used to certify the intervals and do not replace the analytic row
identification in L072. The audit records their actual and required
errors. The initial audit run encountered a NumPy boolean serialization
error after computation; conversion to a Python boolean repaired the
reporting failure. The final saved audit passes all checks.

### 6. Meaning for the response problem

Both signs concern exactly the diagnostic's chosen row averages and
sa factor. An original-trace claim still requires control of their
replacement of actual staggered paths, axial embedding normalization,
variable coefficients, and the pinned-boundary trace remainder.
A finite N=24 sign is neither a continuum coefficient nor an asymptotic
lower bound. L066's norm obstruction, the other endpoint monomials and
all nine mixed placements remain in force. Other response/forest jets,
the full logarithm and interacting error <=c_box/2 remain uncomputed.
The shared quartic is not added again. No Yang–Mills candidate follows.

This is a local standard-method reproduction under the unchanged
SPECIALIZE assessment: no novelty beyond the checked sources, general
flow renormalizability or bulk matching theorem is claimed.

## Mathlib

Coverage of this full finite diagnostic enclosure: **not checked**.
Coverage of supporting spectral calculus, sine/cosine orthogonality,
Gaussian quadrature, interval arithmetic and rounding-error bounds:
**not checked**. No full matching theorem or absence claim is asserted.
The numerical certificate is not a proof-assistant formalization.
