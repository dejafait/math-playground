# Lemma 943: exact coordinates for the full allowed simplex field class

## Hypotheses

Use the twelve-coordinate simplex, actual weight W_E, score
h(x)=k'(x)/k(x), chart measure and operator T_E of L942, with
1/4<=E<=4. A field is a polynomial function on sum t_i=1 having an
ambient representative of component degree at most 13, equivariant
under all coordinate permutations, tangent to sum t_i=1 and normally
zero on every coordinate face. Coefficients are rational. Fields
whose restrictions coincide are identified. The zero-flux and radial
identities remain the inputs proved in L942, whose separate critical
audit is pending; they are not rederived here.

For a partition mu, let m_mu be the sum of distinct monomials whose
positive exponents are mu, with coefficient one for each monomial.
It is zero if there are fewer variables than parts, and m_empty=1.
Write n_r(mu) for the multiplicity of the positive part r. Removing
one occurrence is denoted mu minus r. For each partition mu of 13
with at most twelve parts, and each distinct positive part r, put

    V_(mu,r),i(t)=t_i^r m_(mu minus r)(t_1,...,omit t_i,...,t_12).

For each such mu choose s=max(mu), and, for every distinct r != s,
define

    B_(mu,r)=V_(mu,r)/n_r(mu)-V_(mu,s)/n_s(mu).                (1)

The V fields alone are generally not tangent. Only the differences
(1) are asserted to belong to the allowed field class.

## Conclusion

The 171 fields (1) are a rational basis for the entire allowed class,
not merely its gradient subspace. Every allowed field has a unique
homogeneous degree-13 representative and a unique linear combination
of (1). Thus checking every column of this basis is sufficient for
checking annihilation of all allowed field directions by a dual.
The assertion concerns the restricted field functions, not uniqueness
of their original, possibly inhomogeneous, ambient expressions.

There is also an exact evaluation formula. Set nu=mu minus r and

    C_(mu,r)(t)=sum_i t_i^(r-1) m_nu(t without t_i),
    R_(mu,r)(E,t)=[(r-1/2)C_(mu,r)(t)
                      +E sum_i t_i^r m_nu(t without t_i)h(E t_i)]/n_r(mu).

Then

    T_E B_(mu,r)=R_(mu,r)-R_(mu,s),                           (2)
    C_(mu,1)=(12-length(nu))m_nu,
    C_(mu,r)=(1+n_(r-1)(nu))m_(nu union {r-1}), r>1.           (3)

These identities extend continuously to the closed simplex. They
provide exact finite coordinates, not a positive residual or a
full-class obstruction. The associated numerical attempt below is
inconclusive. No integrated-density crossing or RH conclusion follows.
This lemma has not received a separate later critical audit.

The fixed rational candidate saved by the conditioned step67 calculation
also fails the proposed uniform residual: at the rational interior point
specified below and E=4 its residual is less than -173/125000000.
This is a counterexample to that candidate alone, not to the allowed
field class or the actual integrated-density crossing claim.

## Proof

### Homogenization preserves and captures the whole class

Let p1=sum_i t_i. If F_i=sum_alpha c_(i,alpha)t^alpha has degree at
most 13, define

    H_i(t)=sum_alpha c_(i,alpha)t^alpha p1^(13-|alpha|).

On p1=1 this is F_i. On p1!=0 it is p1^13 F_i(t/p1).
For positive t, the point t/p1 is in the simplex. Tangency and
equivariance there imply the corresponding polynomial identities
for H on the positive orthant, hence everywhere. This last implication
uses only the fact that a real polynomial vanishing on an open set
is zero, proved by applying the one-variable root bound successively
to each coordinate. In particular sum_i H_i=0 as an ambient identity.

On t_i=0 with all other coordinates positive, the same scaling
argument and the face condition give H_i=0. Its restriction to that
coordinate hyperplane is a polynomial vanishing on a relative open
set, so is identically zero. Thus H_i is divisible by t_i. This also
covers intersections of faces by polynomial continuity.

Conversely, a homogeneous degree-13 equivariant field with component
H_i divisible by t_i and sum_i H_i=0 restricts to an allowed field.
If a homogeneous degree-13 polynomial vanishes on the simplex, scaling
shows that it vanishes throughout the positive orthant, hence it is
the zero polynomial. The restriction map is therefore injective.
This proves existence and uniqueness of the homogeneous representative,
including when the original field has degree strictly smaller than 13.

### The pointed monomial orbits and their tangent kernel

Equivariance implies that component H_i is symmetric in the other
eleven variables. Expand it uniquely in the ordinary monomial basis,
collect the exponent r>=1 of t_i, and group the remaining monomials
by their exponent partition nu. Their degree is 13-r. The polynomials
t_i^r m_nu(t without t_i) are linearly independent in that component.
Equivariance determines all other components from it. Consequently
the V_(mu,r) form a basis of homogeneous equivariant fields divisible
componentwise by t_i, before imposing tangency.

For a fixed monomial with exponent partition mu, its occurrence in
sum_i V_(mu,r),i is counted once for each coordinate whose exponent
is r. There are exactly n_r(mu) such coordinates. Therefore

    sum_i V_(mu,r),i=n_r(mu)m_mu(t).                           (4)

Distinct m_mu are linearly independent. For each mu, tangency imposes
the single relation sum_r n_r(mu)c_(mu,r)=0 on its coefficients.
Its kernel has the basis (1): given the coefficients c, take the
coefficient of B_(mu,r) to be n_r(mu)c_(mu,r) for r!=s. The relation
determines the coefficient of V_(mu,s), and this representation is
unique. Different partitions have disjoint monomial supports, so
these bases combine without further relations.

For an explicit count, the partition numbers p(0),...,p(13) are

    1,1,2,3,5,7,11,15,22,30,42,56,77,101.

They can be obtained by starting with the polynomial 1 and multiplying
successively by (1+z^j+z^(2j)+...), truncating after degree 13, for
1<=j<=13. Each coefficient counts a partition by its part
multiplicities, so this finite recurrence also verifies the count.
Exactly one partition of 13 has more than twelve parts, namely
(1,...,1) with thirteen entries. Hence there are 100 target orbits.
The number of pointed orbits is

    sum_(r=1)^13 #{partitions of 13-r with at most eleven parts}
      =sum_(n=0)^12 p(n)-1=271.

The one exclusion is the partition of 12 into twelve ones. Formula
(4) makes the sum map onto the 100-dimensional symmetric degree-13
space, so its kernel has dimension 271-100=171, as claimed. The
script below enumerates these finite partitions exactly as a check;
the spanning and independence arguments do not depend on numerics.

### Intrinsic divergence and the actual score

For a tangent homogeneous representative X, differentiate the ambient
identity sum_i X_i=0 with respect to t_12. It follows that

    sum_(j=1)^11 (partial_j-partial_12)X_j
      =sum_(i=1)^12 partial_i X_i.

Substitution into L942(7) yields

    T_E X=sum_i [partial_i X_i-X_i/(2t_i)+E X_i h(E t_i)].       (5)

The ambient expression on the right can be evaluated linearly on
the two V terms in (1); it is not an intrinsic divergence assertion
for a nontangent V. In V_(mu,r),i, the factor m_nu omits t_i, so
partial_i V_(mu,r),i=r t_i^(r-1)m_nu. Equation (5) proves (2).
If r=1, each monomial of m_nu occurs for exactly 12-length(nu)
omitted coordinates. If r>1, lowering the distinguished exponent
gives exponent partition nu union {r-1}; each resulting monomial
is counted 1+n_(r-1)(nu) times. This proves (3).

All quotients X_i/t_i are polynomials. The function h is continuous
on the compact range by the analytic positive-kernel input in L942.
Thus (2)--(5) have continuous boundary limits, including every zero
coordinate. No numerical differentiation at a singular face is used.

### Scope and the associated unsuccessful screen

The representation was needed to avoid calling a restricted field
test a full-class test. It is elementary polynomial algebra within
the already approved ansatz; no new general divergence theorem or
positivity-completeness theorem is asserted. L942 supplies the precise
known-source specialization behind (5). Originality of these finite
coordinates is not claimed.

Reproduction command for the bounded diagnostic, not a proof certificate:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/heat/l938-full-field-screen-66.py

The full record is `scripts/heat/l938-full-field-screen-66.json`, with
arrays in the adjacent `.npz`. It contains all 171 basis labels,
598 rational simplex samples, all 34 original factorial-normalized
Pbar rows, rationalized candidate coefficients, and numerical failures.
At E=1/4 the affine scalar has one effective column, giving 172 columns
including the fields. The floating SVD retained only 168 at its stated
relative cutoff 10^(-13). The barrier stopped at its coefficient
magnitude limit, without an optimality or boundedness conclusion.

The saved sample minimum is about 3.2145*10^12 in units where Pbar
is multiplied by 10^24, but four numerical directions were discarded,
the theta calculations have no rounding/tail certificate, and the
domain was only sampled. The nominal dual has scaled-column defect
about 0.02158, so it annihilates neither the numerical columns nor
the exact class. A negative nominal dual objective is inconclusive.
Extending the same candidate with constant a to E=4 yields 298 negative
sampled residuals, with minimum about -1.6019*10^25 in those units.
This diagnostic does not exclude all affine extensions or other fields.
No uniform margin or rigorous full-class dual was obtained.

### Conditioned continuation and rejection of its fixed candidate

The next bounded calculation keeps exactly (1), with no degree or
energy enlargement. Its full record is
`scripts/heat/l938-conditioned-endpoints-67.json`; `/candidate` specifies
all 171 rational coefficients c_b in the order of step66's `/basis`.
This is an exact finite specification of the field X=sum_b c_b B_b,
not an existence claim. Its scalar coefficients are

    a_0=-78031764810144,
    a_1=6581096224983139/2199023255552.

To condition the same basis, form exact polynomial coefficient columns
for T_0 B_b and sum_i (B_b)_i t_i^j, j=1,...,4. T_0 here denotes only
the first two terms of (5), not zero energy. For the latter map,
sum_i V_(mu,r),i t_i^j equals n_(r+j)(nu union {r+j}) times
m_(nu union {r+j}). The coefficient formula is the same distinguished
coordinate count as (4). Exact rational column elimination orders these
maps first by j (j=0 for T_0), then by partition. Subtract earlier pivot
columns and divide by each nonzero new pivot. The saved transformation
is triangular with nonzero diagonal, so retains precisely the entire
171-dimensional field space. There are 76, 85 and 10 pivots at levels
0, 1 and 2 respectively. These finite counts describe conditioning,
not approximation of the theta score or a positivity theorem.

The simultaneous E=1/4,4 diagnostic used 214 rational simplex points,
80-digit Decimal evaluation and an untruncated numerical SVD; its
smallest/largest singular-value ratio is about 6.68*10^(-10). The
barrier again hit its coefficient magnitude stop. Positive sampled
residuals therefore give no optimum, boundedness or uniform margin.
The fit producer later acquired an optional energy-list argument for
held-out replay; its default calculation is unchanged. The input hash
in the fit record identifies the version at execution time.

The separate `scripts/heat/l938-conditioned-replay-67.json` verifies
positive necessary values at both exact L942 algebraic roots for both
energy endpoints, and at every vertex limit. The root intervals are
refined by 100 further exact sign-preserving bisections, rather than
replaced by midpoints. At the four root/energy pairs the actual residual
is enclosed respectively in [28,29], [31,32], [41,42] and [41,42], each
multiplied by 10^(-12). At a vertex the exact residual is
79757487081620403/2944000000000000000000000000>0, independently of E.
These are necessary tests only. In particular they show why the old
three-point, two-field dual does not reject this candidate.

Held-out Decimal evaluation of the same fixed candidate, with no refit,
is saved in `scripts/heat/l938-conditioned-heldout-67.json`. Of 384 new
simplex points, 57, 98 and 117 have negative diagnostic residuals at
E=1/4,17/8,4 respectively. This prompted the following rigorous check,
which alone suffices to reject the candidate.

Put E=4 and let t be the vector of positive integers

    (176249,1,100000000,305682,28,43251,873,84,
                         6296,8325533,134144,1017164)/110009305.

The numerator sum is exactly the denominator. The full rational
certificate `scripts/heat/l938-conditioned-candidate-rejection-67.json`
proves for this fixed candidate that

    -277/200000000 <= D_4(t)+T_4 X(t)-a(4)Pbar(t)
                                      <= -173/125000000 < 0.       (6)

Here residuals use the unscaled normalization D_E of L942(3), not
step66/67's diagnostic units 10^24 Pbar. Any epsilon>0 uniform on the
simplex is contradicted by (6).

Here are the full evaluation and error rules underlying (6). For a
finite list x and partition lambda define m_empty(x)=1 and other
m_lambda=0 initially. On appending coordinate x_i update in decreasing
degree by

    m_lambda(x_1,...,x_i) = m_lambda(x_1,...,x_(i-1))
                + sum_(r distinct in lambda) x_i^r
                            m_(lambda minus r)(x_1,...,x_(i-1)).

This partitions monomials by the exponent assigned to x_i, counting
each once. It evaluates all m_lambda of degree <=12, and each
leave-one-coordinate-out value, using rational arithmetic only.
Equation (1) gives each X_i exactly; (3) and the polynomial part of
(5) give a rational value

    g=sum_i [partial_i X_i-X_i/(2t_i)].

The script checks sum_i X_i=0 exactly. Pbar is the exact rational sum
of all 34 rows with L940's orbit/factorial normalization. With enclosed
h_i=h(4t_i), the three quantities evaluated outward are

    D=(17+4 sum_i t_i h_i)Pbar,
    T=g+4 sum_i X_i h_i,
    R=D+T-(a_0+4a_1)Pbar.

For each h_i use L942's rational pi, exp and square-root algorithms,
now with outward grid 2^(-400), and retain theta terms n=1,...,12.
Every argument has 0<u=sqrt(4t_i)<2. Using pi in (3,4), exp(4)<55,
exp(1)<3 and exp(3)>20 gives 3n^2<=z_n<=220n^2 and exp(u/2)<3.
The absolute K and K' summands are therefore bounded by

    1169520 n^4 20^(-n^2),
    519835800 n^6 20^(-n^2),

respectively. For n>=13, successive majorants have ratio at most
rho=2/20^27, since (14/13)^6<2. The full omitted tails are bounded by

    T_K=1169520*13^4/[20^169(1-rho)],
    T_K'=519835800*13^6/[20^169(1-rho)].

Add [0,T_K] to K (positive tail by L019), and [-T_K',T_K'] to K'.
Every enclosed K is positive. Division by 2uK encloses the full score,
not a truncated-kernel score. The stated exponential bounds are also
checked by the same rational Taylor algorithm. Exact rational
operations plus these outward bounds prove (6). No Decimal contract
or fitted epsilon enters this rejection. The script and complete
certificate give the selected rational values, all twelve full-kernel
enclosures and exact output endpoints; all three checks pass.

Reproduction commands, with diagnostics distinguished from proof:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/heat/l938-conditioned-endpoints-67.py
    python3 scripts/heat/l938-conditioned-replay-67.py
    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/heat/l938-conditioned-heldout-67.py
    python3 scripts/heat/l938-conditioned-candidate-rejection-67.py

The first and third are floating/Decimal diagnostics. The second and
fourth perform rational necessary checks of the fixed rational
candidate. Neither searches all fields or certifies a continuum.
This records one failed candidate rather than introducing another
lemma or claiming progress beyond the sources checked. The exact
conditioning remains reusable with a materially different new test;
repeating endpoint fitting alone is not justified by these results.

## Mathlib

Full coverage of this exact field-coordinate statement and the
actual-theta evaluation formula has not been checked. Supporting
symmetric-polynomial, homogenization and partition-count results
have also not been checked. Availability is unknown; the Python
enumeration and numerical screen are not a Lean formalization.
