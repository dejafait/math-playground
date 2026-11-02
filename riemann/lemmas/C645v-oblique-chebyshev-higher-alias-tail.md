# Corollary 645v: a uniform bound for the complete oblique higher-alias tail

## Hypotheses

Let m>=5 be odd, n=3m, d=5/4, x=-d, R=11/8, U=R^2,
r=27/50 and eta=1/100. Use the common poles

    a_k=x+i*r*cos((2*k-1)*pi/(2*m)), 1<=k<=m,

with original simple-pole residues all one. For |u|=1 define

    B_u(v)=product_(j=0)^(n-1) R*(v-(j/n)*u)/(U-(j/n)*conjugate(u)*v),
    W_n(v,u)=B_u(x)/B_u(v),
    q_u(zeta)=sum_k [W_n(a_k,u)/R]/(zeta-a_k/R).

The angle is u=exp(i*phi)=i*exp(i*theta); this retains the conjugated
angle in the factor denominator. Restrict phi to the fixed sector

    |phi-13*pi/16|<=epsilon, epsilon=10^(-6).                (1)

Use C645g's normalized Hardy spaces and H_q f=P_-(q*f). Put

    F_n(t,u)=W_n(x+i*r*cos(t),u),
    b_l(u)=(2*pi)^(-1) integral_0^(2*pi) F_n(t,u)*exp(-i*l*t) dt,
    S_m(u)=(1/m)*sum_k W_n(a_k,u).

No separation, actual-Xi realization, sign condition or angular lower
bound is assumed. The poles and residues are independent of u.

## Conclusion

Uniformly for every stated n and u, the complete alias identity is

    S_m=b_0-2*b_(2m)+E_m,
    E_m=2*sum_(h>=2) (-1)^h*b_(2*m*h),                       (2)
    2*sum_(h>=2)|b_(2*m*h)| <=4*exp(-21*n/250).               (3)

In particular

    ||H_q_u|| >= ||q_u||_2
      >= (m/R)*max{0, |b_0-2*b_(2m)|-4*exp(-21*n/250)}.       (4)

The remainder rate 21/250=0.084 exceeds 1/32 by 211/4000.
This controls all higher aliases, with no unbounded series omitted.
It does NOT establish a lower bound for the leading signed term
b_0-2*b_(2m), or for the full angular norm at rate 1/32. That lower
bound and the general common-pole target remain open. This is a local
quantitative input within the previously assessed Fourier/residue
route; originality beyond the inspected sources is not certified.
A separate conceptual audit on 2 November 2026 verified the full
argument and rational certificate without a mathematical correction;
see below. This is not an RH candidate.

## Proof

### Sources, local scope and purpose

Reuse the invocation-start EXPLORE assessment
[angular source comparison](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md).
It covers the unchanged common-pole family and angular Fourier/residue
test. C645g supplies the operator normalization, C645t the r=27/50
admissibility, and C645l its exact Chebyshev logarithmic-derivative
identity (23). Its old fixed-grid norm bound is not an input.

The imported standard theorems are the residue theorem and simple-pole
rule in R. W. Howell and J. H. Mathews, *Complex Analysis*, online
edition, front matter updated 22 August 2025,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
and the contour inequality in
[Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html).
Scalar Fourier Parseval uses A. Levitt, *Analyse de Fourier et
applications*, version retrieved 2 November 2026,
[author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
Theorem 1.3/Exercise 1.2 and Theorem 1.11/Corollary 1.12, printed
pp.6,8 (PDF pp.12,14), with measure divided by 2*pi here.
The operator convention is L. Baratchart, S. Chevillard and T. Qian,
*Minimax principle and lower bounds in H2-rational approximation*,
J. Approx. Theory 206 (2016), 17--47,
[preprint v2, Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
These inspected inputs are reused rather than reproved. No Nehari/AAK
claim, saddle theorem or Parseval identity for operator norms is used.
The calculation needed here is the evaluated uniform product bound
on a contour for this varying complex integrand. The sources do not
give that numerical bound.

### 1. Geometry and a contour without grid poles

C645t's admissibility argument gives distinct poles, includes x because
m is odd, and gives

    |a_k|^2<=d^2+r^2=18541/10000<(273/200)^2=(R-eta)^2.

Their moduli are at least d>1, whereas every rotated grid point has
modulus <1. Also |U-t*conjugate(u)*v|>=U-t*R>0 for |v|<=R
and 0<=t<1. Thus all original weights and boundary symbols exist.

Set

    sigma=3/10, rho=sqrt(1+sigma^2)+sigma=(sqrt(109)+3)/10,
    s=r*sigma=81/500, h_*=d-s=136/125.

The Joukowski parametrization

    v(lambda)=x+(i*r/2)*(lambda+lambda^(-1)), |lambda|=rho   (5)

has horizontal semiaxis s and vertical semiaxis r*sqrt(1+sigma^2).
For rho^(-1)<=|lambda|<=rho, Re(v(lambda))<=-h_*.

Write c=cos(phi), e=sin(phi). The following rational intervals hold
throughout (1):

    -831471/10^6 <= c <= -831468/10^6,
     555569/10^6 <= e <=  555572/10^6.                      (6)

For completeness, enclose sqrt(2) between 1414213562373/10^12 and
1414213562374/10^12; then w=sqrt(2-sqrt(2)) lies between
765366864729/10^12 and 765366864732/10^12. Squaring rational endpoints
encloses sqrt(2+w)/2 in [831469612301,831469612304]/10^12
and sqrt(2-w)/2 in [555570233018,555570233022]/10^12.
The central cosine is minus the former and the central sine is the
latter. The Lipschitz bounds |cos(a)-cos(b)|,|sin(a)-sin(b)|<=|a-b|
give (6). All endpoint square comparisons are in the exact certificate.

Every grid point t*u has real part t*c>=-831471/10^6>-h_*.
The rational expression

    W_n(v,u)=product_j [(x-t_j*u)*(U*u-t_j*v)]
                              /[(v-t_j*u)*(U*u-t_j*x)]

has possible finite poles only there. It also specifies W_n at any
removable zero of the original quotient of disk products. Its anchor
denominators are nonzero. Consequently W_n is holomorphic on a
neighborhood of the filled ellipse, and W_n(v(lambda),u) on a
neighborhood of the closed annulus in (5). This argument does not
require that the entire ellipse lie inside |v|<R.

### 2. Exact half-plane product envelope

For 0<=t<=1 and v=-H+i*y, H>=h_*, define

    D1=d^2+2*d*c*t+t^2=|x-t*u|^2,
    D2=U^2+2*U*d*c*t+d^2*t^2=|U*u-t*x|^2.

They are positive. The squared factor ratio is exactly

    |b_t(x;u)/b_t(v;u)|^2
      = (D1/D2)*[(U*c+t*H)^2+(U*e-t*y)^2]
                   /[(H+t*c)^2+(y-t*e)^2],                (7)

where b_t(v;u)=R*(v-t*u)/(U-t*conjugate(u)*v).
The denominator in (7) is positive, since H+t*c>=h_*-831471/10^6>0.

Here is a finite rational certificate for its upper envelope. Split
[0,1] into N=512 equal closed cells I_j. For each cell the saved K_j
is rational, K_j>=1, and the K_j are nondecreasing. Define

    A=K_j*D2-t^2*D1, D=K_j*D2-U*D1,
    B=2*t*e*D,
    C=K_j*D2*(h_*^2+2*h_*c*t+t^2)
                    -D1*(U^2+2*U*h_*c*t+h_*^2*t^2).        (8)

Exact rational interval arithmetic verifies, on every I_j and (6),

    D1>0, D2>0, A>0, 4*A*C-B^2>0, h_*A+t*c*D>0.           (9)

These inequalities imply (7)<=K_j for all real y and H>=h_*.
Indeed the desired inequality after multiplication by its positive
denominators is Q(H,y)>=0, where

    Q(H,y)=A*y^2-B*y+A*H^2+2*t*c*D*H+K_j*D2*t^2-U^2*D1.

At H=h_* the quadratic in y is positive by A>0 and 4AC-B^2>0.
For H>=h_*, its H derivative is 2*A*H+2*t*c*D>0 by (9).
This covers the entire unbounded half-plane directly, without a
sampling argument or a maximum-modulus assertion at infinity.

The complete reproducible certificate is
`scripts/one-sided-hankel/oblique-alias-tail-certificate.json`, generated
by `python3 scripts/one-sided-hankel/oblique-alias-tail-certificate.py`.
Its 512 rows contain every t cell, K_j and all five lower margins.
The rational algorithm starts with a valid upper K=4 and bisects
between 1 and 4 for fourteen steps, retaining a checked valid upper
endpoint, then replaces it by the running maximum and checks (9)
again. Thus validity needs no monotonicity of the interval predicate
used in bisection. Every final cell was checked, including endpoints.

The minimum certified margins for D1,D2,A,4AC-B^2 and h_*A+t*c*D are,
respectively,

    393150517/819200000,
    15739986733/13107200000,
    62111357097079/21474836480000,
    5757188643879569828205889351160079/
        2882303761517117440000000000000000000000,
    295910441511758373/214748364800000000.

All are strictly positive. The largest K_j is 31883/8192<4.
To bound logarithms by rational numbers, put z_j=(K_j-1)/(K_j+1).
For 0<=z_j<1 the integrated geometric series gives

    (1/2)*log K_j
      <=sum_(k=0)^15 z_j^(2*k+1)/(2*k+1)
                    +z_j^33/[33*(1-z_j^2)].               (10)

The positive tail in (10) follows by replacing each remaining
denominator by 33. Rounding this upper bound upward to multiples
of 10^(-12) gives the saved ell_j. The exact result is

    (1/N)*sum_j ell_j
      =7722432503711/25600000000000 <31/100.                (11)

There is no n-dependent quadrature error hidden here. Define g(t) as
(1/2)*log K_j on [j/N,(j+1)/N), assigning the final value at t=1.
It is nonnegative and nondecreasing. For every integer n>=1,

    sum_(k=0)^(n-1) g(k/n) <= n*integral_0^1 g(t) dt
                           <= (31/100)*n,                 (12)

by integrating g(t)>=g(k/n) separately on each [k/n,(k+1)/n].
Combining (7)--(12) over the actual grid, including t=0, proves

    |W_n(v,u)|<=exp(31*n/100), Re(v)<=-h_*.                 (13)

The certificate uses only Python Fraction arithmetic for all accepted
inequalities and the complete logarithm remainder. Its final failure
list is empty. A first run with the tighter requested envelope 3/10
failed that inequality and one nested-radical enclosure; it is preserved
as `scripts/one-sided-hankel/oblique-alias-tail-initial-failed.json`.
The corrected radical intervals and relaxed 31/100 bound above are
the ones used in (13). No conclusion relies on the failed certificate
or on the separate floating-point diagnostic.

### 3. Complete alias identity and summable remainder

On |lambda|=1 the function G(lambda)=W_n(v(lambda),u) equals
F_n(t,u) with lambda=exp(i*t). Its Laurent coefficients are the b_l.
The annular holomorphy from Section 1 justifies moving their integrals
to |lambda|=rho. The contour inequality and (13) give, for l>=0,

    |b_l|<=exp(31*n/100)*rho^(-l).                         (14)

Equivalently G(lambda)=G(1/lambda), so the negative coefficients
have the same bounds. All relevant Fourier series converge absolutely.

Apply C645l's elementary identity (23) with this value of r and with
f(v-x)=W_n(v,u). That algebraic identity holds for any r>0: its
polynomial has exactly the m nodes used here and simple zeros. The
residue integral on (5), which is allowed by Section 1, gives

    S_m=(1/(2*pi*i))*integral_(|lambda|=rho)
           G(lambda)*(lambda^(2m)-1)/(lambda^(2m)+1)
                                             *d lambda/lambda.

Expand its last factor as
1+2*sum_(h>=1)(-1)^h*lambda^(-2*m*h). The series is uniformly
absolutely convergent on this fixed circle; G is bounded there by
(13). Termwise integration is therefore justified and proves (2).
In particular the first sign is minus, and there are exactly m original
unit residues, not an enlarged pole count. From (14),

    2*sum_(h>=2)|b_(2*m*h)|
      <=2*exp(31*n/100)*rho^(-4m)/(1-rho^(-2m)).            (15)

Now log rho=asinh(3/10). Integrating
(1+t^2)^(-1/2)>=1-t^2/2 for 0<=t<=3/10 gives

    log rho>=3/10-(3/10)^3/6=591/2000.

For m>=5, 2m log rho>=591/200>1 and hence rho^(-2m)<1/2
(e>2). With n=3m,

    (4m/n)*log rho-31/100
       >=(4/3)*(591/2000)-31/100=21/250.

Equation (15) proves (3), uniformly throughout the fixed sector.

### 4. What this contributes to the detector

Every pole of q_u is in the open unit disk. Its geometric expansion
converges absolutely on the boundary, has only strictly negative
Fourier modes, and its first coefficient is

    (1/R)*sum_k W_n(a_k,u)=(m/R)*S_m(u).

Thus H_q_u 1=q_u, ||1||_2=1, and scalar Parseval implies
||q_u||_2>=(m/R)|S_m|. The reverse triangle inequality with (2)--(3)
proves (4). All sums over poles are finite; no operator-norm Parseval
or omitted signed cross term is involved.

If a later argument establishes
|b_0-2b_(2m)|>=c*n^(-A)*exp(-gamma*n), uniformly on (1), with
c>0, finite A and gamma<1/32, then (3) is exponentially smaller.
The sector has normalized measure epsilon/pi. Integrating (4) on
it would give the corresponding angular constant-input lower bound
with factor (m/R)*sqrt(epsilon/pi), and the strict margin would survive
C645u's polynomial comparison for the kernel test. This is a conditional
downstream use, not a lower bound established here. The leading signed
term, other admissible families, and all actual-Xi bridges remain open.

### Separate conceptual audit — 2 November 2026

The C645w audit, STEP_ID 2026-11-02-oblique-saddle-audit-01, checked
this complete load-bearing input, including the generator and all
512 exact rational cells. This is REPRODUCTION of the existing result,
not a new tail estimate. The source assessment and its precise imported
contour/Fourier results are reused; no general source proof was newly
audited and no stronger operator theorem is needed.

The nodes are distinct, include x for odd m, and satisfy the strict
clearance bound stated in Section 1. The ellipse has left real margin
h_*=136/125, while all rotated grid poles have real part at least
-.831471. Thus the entire filled ellipse, and not just its boundary,
is free of poles of W_n. The rational form correctly treats removable
zeros of the original quotient. No |v|<R assumption is imposed on that
ellipse. The nested-radical and Lipschitz enclosures were replayed;
the enlarged c,e rectangle is only a certificate domain, while the
identity c^2+e^2=1 used in (7) applies to the actual angular sector.

Expanding K_j D2 times the denominator of (7) minus D1 times its
numerator gives exactly Q(H,y), with y coefficient -2*t*e*D.
The five positive margins in (9) prove Q(h_*,y)>0 for every real y
and its positive H derivative for H>=h_*. This controls the entire
unbounded half-plane. The bisection retains a checked upper endpoint;
the final running maxima are checked again, so no monotonicity of
an interval predicate is assumed. All 2,560 final margins are positive.

The exact generator replay passes all 16 original comparisons.
The separate audit in `scripts/one-sided-hankel/oblique-saddle-audit.py`
also checks all 512 closed t cells, their indices, monotonic K_j,
every positive margin, and every full logarithm-tail upper bound and
upward rounding. The actual product exponent is
7722432503711/25600000000000 <31/100. Equation (12) uses a monotone
step majorant, so it bounds every actual grid size without a hidden
quadrature error. The original failed 3/10/radical certificate remains
preserved and supplies no premise.

The Joukowski circle winds once positively around the segment; the
Chebyshev logarithmic derivative (23) applies to this r as an exact
polynomial identity. Substitution gives d lambda/lambda and the ratio
(lambda^(2m)-1)/(lambda^(2m)+1), hence the first alias has coefficient
-2. Both the Laurent contour shift and the geometric expansion occur
on a fixed pole-free annulus, with absolute uniform convergence.
The whole remainder starts at 4m, not 2m. The bound
log rho>=591/2000 gives 2m log rho>1 for m>=5 and
(4/3)log rho-31/100>=21/250, proving the entire tail in (3).

Finally, every spatial pole lies strictly in the unit disk. Testing
H_q on the normalized constant function and retaining its first
negative Fourier coefficient gives precisely (m/R)|S_m|. No factor
of m, R or normalized angular measure is lost. This corollary alone
still supplies no lower bound on its leading signed term; C645w is
a later application, not an input to this proof. General pole families,
actual-Xi realization and signs remain outside its scope. No direct
mathematical dependency changed.

## Mathlib

Full matching coverage has not been checked; no absence claim is made.
The supporting mathematics is rational interval arithmetic, quadratic
positivity, contour/Laurent coefficient bounds, a geometric alias series
and scalar Fourier Parseval. No Mathlib theorem is asserted to contain
this evaluated sector or rate.
