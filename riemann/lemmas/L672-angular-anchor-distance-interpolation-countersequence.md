# Lemma 672: an undisplaced countersequence to angular anchor separation

## Hypotheses

Use L666's exact rational family and normalized angular measure. Let
q>=1, n=12q+3, M=4q+1, h=27/(10n), x=-d=-5/4, R=11/8,
U=R^2=121/64 and t_j=j/n for every 0<=j<n. Choose the admissible
displacements e_r=0 for all -2q<=r<2q, and put

    y_r=h*(r+1/2),  a_r=x+i*y_r,
    Z={x} union {a_r:-2q<=r<2q},
    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),               |u|=1,
    delta=inf_(lambda in C^(4q)) ||1-sum_r lambda_r W_(a_r)||_2.

All original residues in L666's G and D remain one. The lambda_r below
are auxiliary approximation coefficients only. No numerical condition
number, Gram inverse, separation beyond these stated nodes, source
kernel identification, or Xi realization is assumed.

## Conclusion

For every q>=1,

    0<delta <= 5*exp(15)*n*exp(-11*n/1000).              (1)

Consequently, along this admissible sequence,

    (-log delta-n/100)/log n
       >= n/(1000*log n)-1-(15+log 5)/log n -> +infinity. (2)

There are therefore no absolute C and onset giving the proposed
delta_e>=exp(-n/100)*n^(-C) for every L666 displacement vector.
This is a counterexample to that sufficient anchor-distance mechanism,
not an upper bound for the actual unit-residue c_0, G or H. The latter
full-angular inequality, support, Xi realization and mixed signs remain
open. A separate conceptual audit on 2 November 2026 verified this
countersequence and replayed the complete exact certificate; see
Section 6. This does not audit the other claims in L666.

## Proof

### 1. Scope, standard input and exact family

The invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-displaced-angular-anchor-distance.md`
covers precisely this distance or an admissible asymptotic witness.
Its primary rational-space and kernel comparisons do not evaluate the
distance. The preceding spatial and coefficient stops are contrasts,
not premises here. No claim of certified originality follows from that
bounded search. The calculation below is needed to evaluate the exact
family, rather than reprove any general rational-space or Riesz theorem.

The standard analytic input is Cauchy's residue theorem, in its finite
polynomial-interpolation remainder form; its application and all
residues are given below. The logarithm and arctangent series used in
the certificate have explicit elementary remainders. They are numerical
evaluation tools for the compact inequality, not new analytic inputs.

L666 (6), with the j=0 factor included, gives

    W_a(u)=(x/a) product_(1<=j<n)
             [(x-t_j*u)/(a-t_j*u)]
             *[(U*u-t_j*a)/(U*u-t_j*x)].               (3)

The poles a_r are distinct, nonreal and lie on Re(a)=x, with
|y_r|<9/20 and |a_r|^2<353/200<(273/200)^2. Thus the family
is admissible, M=n/3, and no original factor or residue changes.

For completeness the comparison span is nonsingular here. Each W_a
has a genuine simple exterior angular pole at a/t_j, 1<=j<n.
These points are distinct across all pairs (a,j): equality forces
t_j=t_k by comparing real parts, and then a=b. At such a point
no factor x-t_l*u vanishes because a is nonreal, and no factor
U*u-t_l*a vanishes because t_j*t_l<1<U. Common interior poles
t_l*x/U are real and cannot coincide. Thus any rational linear
relation between 1 and the nonanchor W_a has every nonanchor
coefficient zero, by taking these residues, and then its constant
coefficient zero. An L2 relation would be a rational identity by
continuity and the identity theorem. A finite-dimensional subspace
is closed, so 1 has strictly positive distance. The upper bound
below itself uses no inverse and would remain valid for a singular
comparison span.

### 2. Explicit interpolation coefficients and contour

Write z=a-x, c=4/3, w=9/100 and Y=1/2. Let Gamma be the
positively oriented boundary of |Re z|<=w, |Im z|<=Y, and set

    P(z)=product_(-2q<=r<2q)(z-i*y_r),
    F_n(z,u)=exp(-c*n*z)*W_(x+z)(u),
    lambda_r=exp(-i*c*n*y_r)*P(0)/[(-i*y_r)*P'(i*y_r)].  (4)

All nodes are strictly inside Gamma. Throughout its closed interior,
Re(x+z)<=-29/25<-1, so the parameter poles x+z=t_j*u, including
the j=0 pole at zero, are absent for every |u|=1. The factors
U*u-t_j*x are also nonzero. Hence F_n is holomorphic there. It has
value 1 at z=0, and Cauchy's theorem gives exactly

    1-sum_r lambda_r W_(a_r)(u)
      =(1/(2*pi*i)) integral_Gamma
                      F_n(z,u)*P(0)/[z*P(z)] dz.       (5)

Indeed the residue at zero is 1, while the residue at i*y_r is
minus the rth interpolant term in (5). All coefficients are fixed
across angles. Their exponential factors have modulus one; their
possibly large interpolation weights are fully retained in (5).

### 3. A compact continuum inequality

For z=s+i*y on Gamma define real functions

    F(z,u)=integral_0^1 log|[(x-t*u)/(x+z-t*u)]
                            *[(U*u-t*(x+z))/(U*u-t*x)]| dt,
    r_*=9/20,
    K(z)=(10/27) integral_(-r_*)^(r_*)
                              [log|t|-log|z-i*t|] dt,
    E(z,u)=F(z,u)-(4/3)*s+K(z).

The compact estimate used in this proof is

    E(z,u) <= -2594211229/225000000000 < -11/1000
                    for z on Gamma and |u|=1.          (6)

Here is a fully specified finite certificate, including its extension
between sample points. Run, from the notebook directory,

    python3 scripts/one-sided-hankel/angular-anchor-contour-certificate.py

The complete output is
`scripts/one-sided-hankel/angular-anchor-contour-certificate.json`.
It contains all 25,358 rational sample upper bounds, both meshes,
rounding and series bounds, the maximum and rational derivative checks.
No floating arithmetic enters an enclosure or pass/fail decision.

#### Exact evaluation at mesh points

Let a=x+z and S(v)=sum_(k>=1) Re(v^k)/[k*(k+1)]. Then

    F(z,u)=log(d/|a|)+S(u/a)-S(u/x)
                           +S(x/(U*u))-S(a/(U*u)).     (7)

This follows by integrating log|1-t*v| term by term; all four
arguments have modulus less than 9/10 uniformly on the rectangle.
Indeed |a|>=29/25, |a|<3/2 and (3/2)/U=96/121<4/5.
The series are absolutely uniformly convergent. Each tail after
degree N=100 is bounded by

    (9/10)^(N+1)/[(N+1)*(N+2)*(1-9/10)].

The circle is parametrized without trigonometric evaluations by

    u=epsilon*(1-v^2)/(1+v^2)+i*2v/(1+v^2),
    -1<=v<=1, epsilon in {-1,1}.                        (8)

All inputs to (7) at mesh points are rational complex numbers. The
code evaluates powers by integer fixed-point arithmetic at scale
S_0=10^40. Each real and imaginary input coordinate is rounded down
with error less than 1/S_0. The stored input has sum of coordinate
absolute values less than 3/2, since its true modulus is at most 9/10.
Each computed complex multiplication is rounded down in each coordinate.
If e_k is the coordinate error in the kth power, then

    e_0=0,  e_(k+1)<=(3/2)e_k+3/S_0,
    e_k<=6*((3/2)^k-1)/S_0.

The three units of rounding cover the two input-coordinate errors
against true powers of modulus at most one and the final integer
division. Flooring each summand contributes at most 1/S_0. Thus
one finite series has error at most

    [6*((3/2)^100-1)+100]/S_0 < 10^(-20).

Here the power errors are multiplied by 1/[k*(k+1)], whose sum
for 1<=k<=100 is 100/101<1; using their largest bound is therefore
valid. The true input's coordinate absolute sum is at most
(9/10)*sqrt(2), so coordinate flooring preserves the asserted 3/2
upper bound with ample room at S_0=10^40.

The four finite-series errors and four geometric tails are added,
not cancelled, and their sum is less than 10^(-6).

The remaining logarithms and K are enclosed by rational series. To
evaluate log b, scale b by powers of 2 into [1,2] and use the first
32 terms of 2*sum z^(2j+1)/(2j+1), z=(b-1)/(b+1) in [0,1/3].
The positive omitted tail is at most 2*z^65/[65*(1-z^2)]. The same
formula encloses log 2, with signed interval multiplication when the
scaling exponent is negative. Put

    J(s,v)=(v/2)log(s^2+v^2)-v+s*atan(v/s),  s>0,
    J(0,v)=(v/2)log(v^2)-v,                v!=0.

Then

    K(s+i*y)=(10/27)*[2r_*(log r_*-1)
                         -J(|s|,y+r_*)+J(|s|,y-r_*)]. (9)

For arctangents, reciprocal and pi/4 addition identities reduce the
argument to modulus at most 1/2. The first 60 alternating terms have
absolute error at most |v|^121/121. Pi is enclosed using
pi=16*atan(1/5)-4*atan(1/239) and the same series. This Machin identity
follows by the tangent addition formula: the tangent of
4*atan(1/5)-atan(1/239) is 1 and the angle is in (0,pi/2).
The series bounds follow by integrating the finite geometric identities
for 1/(1-z^2) and 1/(1+z^2), respectively. Thus every interval here
has a specified remainder and rational endpoints. Formula (9) has
no singular evaluation at the chosen boundary mesh points.

#### Derivatives and coverage between points

Conjugation sends (y,u) to (-y,conjugate u) without changing E.
It suffices to cover 0<=y<=1/2 on both vertical sides and the upper
horizontal side. Parametrization (8) covers the complete circle.

For variation in s or y, the logarithmic second derivatives of F
have absolute value bounded by

    integral_0^1 [1/(29/25-t)^2+t^2/(U-3/2)^2] dt
       <=625/116+4096/1875 < 8.                        (10)

On a vertical side, integrating the derivative of log|s+i(y-t)|
at the two endpoints yields |K_yy|<=(10/27)/|s|<5. Therefore
|E_yy|<13. On y=1/2,

    |K_ss| <=(10/27) integral_(-r_*)^(r_*)
                                      1/(1/2-t)^2 dt
             =(10/27)*(20-20/19)<8,

so |E_ss|<16.

For (8), |u'|<=2 and |u''|<=4. A term log|A+B*u| therefore has
second v derivative at most 4*b/dist+4*b^2/dist^2, with b=|B|.
Indeed |u'|=2/(1+v^2) and |u''|=4/(1+v^2)^(3/2) on either
chart; differentiate log|A+B*u| twice and take absolute values.
For the last two logarithms in F use
|U*u-t*a|=|U-t*a*conjugate(u)|, and similarly for x.
Integrating these four bounds gives

    |E_vv|=|F_vv|
      <4*[2+16/5 + 2+625/116 + 2+16/5 + 6/5+4/3]
      =35359/435 <100.                                (11)

For clarity, the first two pairs use
integral 1/(b-t)=log(b/(b-1))<2 for b=d or b=29/25,
and integral 1/(b-t)^2 equal to 16/5 or 625/116.
For the denominator terms put gamma=|a|/U<=4/5 or d/U<2/3.
Their first integrals are bounded by -log(1-gamma), and their
second by gamma^2/(1-gamma). Use log 5<2 and log 3<6/5.
Also log(29/4)<2, since exp(2)>109/15>29/4 by its first six
Taylor terms. These bounds justify every summand in (11).

The vertical mesh has y-step 1/50 and v-step 1/120. The upper
horizontal mesh has s-step 3/100 and v-step 1/10. A C2 real
function on an interval differs from its linear interpolant by at
most (sup|f''|)*length^2/8. Applying this successively in the two
coordinates gives errors

    vertical:   (13/8)*(1/50)^2+(100/8)*(1/120)^2
                    =1093/720000,
    horizontal: (16/8)*(3/100)^2+(100/8)*(1/10)^2.

No mixed-derivative estimate or sample-only maximum is used.
Every rational sample upper bound is rounded upward to a multiple
of 10^(-12), and the appropriate interpolation error is then added.
The largest resulting bound is exactly that in (6), at the recorded
vertical mesh row s=-9/100, y=0, u=1 before interpolation. Its strict
margin below -11/1000 is

    119211229/225000000000 > 0.

All sample rows and all auxiliary rational checks passed. This
establishes (6) via the stated finite arithmetic and analytic coverage;
the preliminary floating contour design is not evidence for (6).

### 4. Complete finite-grid and interpolation-product costs

For fixed z on Gamma and |u|=1, call the integrand defining F
f(t). All its denominators stay away from zero, and

    |f'(t)| <= 4+25/4+96/25+80/41 <17,   0<=t<=1.

Here |a|<3/2 and Re(a)<=-29/25. Comparing the full left Riemann
sum, including t_0=0, with its integral gives

    log|W_(x+z)(u)| = sum_(0<=j<n) f(j/n)
                       <= n*F(z,u)+9.                 (12)

The error is at most 17/2: each subinterval contributes at most
17/(2n) to the difference between its left value and its average.

Next, r_*=(2q+1/2)h exactly. For the positive half of the nodes,
monotonicity of log on [h*(k+1/2),h*(k+3/2)] gives

    log|P(0)|=2 sum_(k=0)^(2q-1) log(h*(k+1/2))
       <=(2/h) integral_(h/2)^(r_*) log t dt
       =(1/h) integral_(-r_*)^(r_*) log|t| dt
                                  +1-log(h/2).        (13)

For g(t)=log|z-i*t| on [-r_*,r_*], every boundary point z
has distance at least 1/20 from i[-r_*,r_*], so |g'|<=20.
The 4q nodes are midpoints of cells of length h filling
[-2q*h,2q*h]. The average distance to a cell midpoint is h/4.
Consequently

    log|P(z)| >= (1/h) integral_(-2q*h)^(2q*h) g(t) dt
                                  -(4q)*20*h/4.

The last cost is less than 9/2, since 4q*h<9/10. Moreover
|z-i*t|<=sqrt((9/100)^2+(19/20)^2)<1 everywhere on the full
integration interval, so g(t)<0. Extending the integral to
[-r_*,r_*] only lowers its value. Combining with (13), h=27/(10n)
and 1-log(h/2)=log n+1-log(27/20), proves

    log|P(0)/P(z)| <= n*K(z)+log n+6.                  (14)

This comparison includes the missing endpoint half-cells and the
logarithmic singularity at t=0; neither is a suppressed limiting step.

By (6), (12) and (14), the numerator of the absolute integrand in
(5), before division by z, is bounded by

    |exp(-c*n*z)*W_(x+z)(u)*P(0)/P(z)|
                    <= n*exp(15)*exp(-11*n/1000).

Gamma has length 59/25, and |z|>=9/100 there. Thus its remaining
factor in (5) is at most 118/(9*pi)<5. This proves the uniform
angular approximation error in (1). Normalized L2 is bounded by the
uniform norm, so the same upper bound holds for delta. Taking logarithms
and using its strict positivity gives (2).

### 5. Scope of the obstruction

If the lower-distance target had held, the actual unit-residue sum
would satisfy ||c_0||_2>=delta_e/R by taking auxiliary coefficients
lambda_a=-1. L666 (4)'s full spatial Jensen bound would then give
H>=log delta_e-log R. The present result instead supplies other,
explicit auxiliary coefficients making the residual small. It gives
no estimate from above for the coefficients -1, nor for H, and does
not alter any original residue. No criterion equivalent to RH has
been established or assumed. The separate source/application and
realization gaps recorded in the overview remain.

### 6. Separate conceptual audit — 2 November 2026, step 36

The unchanged invocation-start EXPLORE assessment covers this exact
countersequence audit. No additional source theorem, favorable Gram
spectrum or independent L666 quadrature claim is an input. The audit
checked the full proof above, including the following delicate points.

First, the genuine exterior poles prove strict positive distance for
each finite q; the proof does not infer a quantitative lower bound from
linear independence. Every parameter pole stays outside the closed
rectangle, and the residues in (5) retain their signs and complex phase
factors. The auxiliary coefficients are angle-independent and never
replace the original unit residues.

Second, the four series in (7) have the displayed signs. All signed
interval multiplications in log rescaling and the primitive (9) retain
both endpoints. The fixed-point recurrence bounds each coordinate,
including negative floors and propagation of the rounded input. The
weighted sum explanation above justifies its stated aggregate error.
The logarithm and arctangent tails, reciprocal reductions and Machin
identity were checked, rather than inferred from floating agreement.

Third, both rational circle charts and conjugation cover every angle
and the full contour. On the upper edge the formula for K has a smooth
extension through s=0 since |y-t|>=1/20; the absolute-value notation in
(9) creates no missing cell. Vertical and horizontal interpolation
use their own derivative bounds, including both endpoints of every
interval. Iterating linear interpolation bounds uses nonnegative
convex weights and adds the two errors; no mixed derivative is needed.

Fourth, the full finite left sum includes t_0=0 and contributes at
most 17/2<9. Exactly r_*=(2q+1/2)h: (13) pays the logarithmic central
interval explicitly. The midpoint cells in (14) fill precisely
[-2qh,2qh]. Since g<0 on the larger interval, adding its two missing
half-cells lowers the integral in the required direction. The total
cost is less than log n+6 for every q>=1, not only asymptotically.
The contour length and minimum |z| then give the factor less than 5.
Consequently the strict exponent difference 11/1000-1/100=1/1000
survives all finite-n costs and proves the divergence in (2).

For complete arithmetic replay, run

    python3 scripts/one-sided-hankel/angular-anchor-contour-audit.py

The full results are
`scripts/one-sided-hankel/angular-anchor-contour-audit.json` and
`scripts/one-sided-hankel/angular-anchor-contour-audit-replay.json`.
The original certificate is preserved. The audit reran every exact
series evaluation, compared the entire resulting data structure with
the original, and independently enumerated all 118 mesh rows and
25,358 sample coordinates, aggregated their maxima and checked every
row against -11/1000. All comparisons passed with zero failures.
Four additional direct Fraction power sums at the maximum witness
obeyed the fixed-point error bound; these are supplementary checks,
not replacements for the uniform recurrence or complete replay.
The actual maximum remains -2594211229/225000000000 and the strict
margin remains 119211229/225000000000. No floating screen is an input.

Verdict: (1)--(2) and the distance-mechanism stop are verified in this
informal audit. No inequality was strengthened and no new discovery
beyond the existing proof is claimed. The signed unit-residue response,
H, general support, Xi realization and RH remain unresolved. The
direct mathematical input remains L666's family/identity and its
conditional Jensen interpretation; no DAG edge changes are required.

## Mathlib

Full matching coverage for this rational-family countersequence and
its compact certificate has not been checked. No absence claim is made.
Cauchy/residue theory, finite-dimensional closedness and elementary
norm inequalities are supporting mathematics; they would not by
themselves supply (6), the finite-n costs, or this distance rate.
