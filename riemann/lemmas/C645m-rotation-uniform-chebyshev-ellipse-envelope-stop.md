# Corollary 645m: the rotation-uniform Chebyshev ellipse majorant fails

## Hypotheses

Retain C645l's common pole family: odd m, n=3m>=39,
x=-d=-5/4, R=11/8, r=1/2, eta=1/100, and

    a_k=x+i*r*cos((2k-1)*pi/(2m)),  1<=k<=m,

with original residues all one. These poles are fixed as the grid rotates.
Use the saved angular product, including its conjugated denominator angle,

    B_theta(v)=product_(0<=j<n)
        R*(v-i*exp(i*theta)*t_j)/(R^2+i*exp(-i*theta)*t_j*v),
    t_j=j/n.

At theta=pi/2 this is exactly

    B_*(v)=product_j R*(v+t_j)/(R^2+t_j*v).

For 0<s<=1/10 let E_s be the ellipse centered at x with horizontal
semiaxis s and vertical semiaxis sqrt(r^2+s^2), and put

    rho_s=(sqrt(r^2+s^2)+s)/r,
    F_z(v)=B_*(x)/(B_*(v)*(z-v)),  |z|=R.

Define the particular global-supremum quadrature majorant

    U_(n,s)(z)=2*sup_(v in E_s)|F_z(v)|/(rho_s^(2m)-1).       (1)

Here E_s denotes the boundary ellipse. The corresponding continuous
arcsine average is

    A_(n,*)(z)=(1/pi)*integral_(-r)^r
                  F_z(x+i*y)/sqrt(r^2-y^2) dy.

## Conclusion

For every stated n,s,z the usual Chebyshev contour estimate gives

    |m^(-1)*sum_k F_z(a_k)-A_(n,*)(z)| <= U_(n,s)(z),       (2)

but its right side satisfies the opposite of the needed smallness:

    U_(n,s)(z) > (1/R)*exp(s*n/12) = (8/11)*exp(s*n/12).    (3)

Thus this ellipse-supremum majorant cannot establish an exponentially
small rotation-uniform quadrature error, even by choosing s=s_n>0:
it is always greater than 8/11. For fixed positive s it grows
exponentially. The required full angular detector scale is exp(-n/32).

This is a lower bound on an UPPER BOUND, not a lower bound on the
quadrature error, on the Hankel norm, or on its angular mean. It neither
proves nor refutes the saved angular target. It only prevents extending
C645l by this particular uniform envelope. The result is unaudited;
it is a local informative obstruction, with no certified novelty or RH
resolution claim.

## Proof

### Source scope and applicability of the existing quadrature estimate

The invocation-start EXPLORE assessment is
[the angular comparison](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md).
It covers this exact common-pole family, correlated weights, and a
Fourier/residue attempt. The target and assessment's TARGET match
verbatim; no new source hypothesis is introduced here.

C645l supplies admissibility of the poles and the exact finite-node
Chebyshev identity, its equations (22)--(24). Its fixed-grid product
gain and imaginary-axis ellipse bound are NOT inputs to (3).
The imported contour rules are Howell--Mathews, *Complex Analysis*,
online edition (front matter updated 22 August 2025),
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
and [Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html),
as inspected in the reused assessments. No general contour theorem or
quadrature theorem is reproved. The calculation below evaluates the
specific majorant left open when the grid rotates.

The ellipses E_s are nested for 0<s<=1/10. C645l's geometric calculation
at s=1/10 gives max |v|^2=377/200<R^2, so all these closed ellipses
are strictly inside the disk. Their real parts are at most x+s<=-23/20.
The zeros -t_j of B_* have real parts greater than -1. Its poles,
when t_j>0, are -R^2/t_j, outside the disk. Thus F_z is holomorphic
in a neighborhood of each closed ellipse for every |z|=R.

In C645l's identity replace s by the present s, and use
w=v-x=(i*r/2)*(lambda+lambda^(-1)), |lambda|=rho_s.
The semiaxes are precisely s and sqrt(r^2+s^2); the identity
P_m'/(m*P_m)=1/S_0-2/[S_0*(lambda^(2m)+1)] is independent
of the function F_z. The just-checked holomorphy is the only changed
applicability condition. The same contour integral therefore gives
(2), with the normalization in (1). This is a specialization of the
already proved finite identity, not an assertion about the true size
of its contour integral.

### The rightmost point already forces a large envelope

The point v_s=x+s is on E_s. Set U=R^2. Since 0<s<=1/10 and
0<=t<1, all numbers d-t, d-s-t, U-d*t, U-(d-s)*t are positive.
Exact division of each factor gives

    |B_*(x)/B_*(x+s)|
      = product_j [(d-t_j)/(d-s-t_j)]
                    *[(U-(d-s)*t_j)/(U-d*t_j)].             (4)

Both ratios are >=1. The first one's logarithm is
-log(1-s/(d-t_j))>=s/(d-t_j), since the fraction is in (0,1).
Consequently

    log |B_*(x)/B_*(x+s)| >= s*S_n,
    S_n=sum_(j=0)^(n-1) 1/(d-j/n).                         (5)

The function f(t)=1/(d-t) is increasing on [0,1]. Comparing its
integral to the right Riemann sum, then subtracting the difference
between right and left sums, gives the finite-n bound

    S_n >= n*integral_0^1 f(t)dt - (f(1)-f(0))
        = n*log(5)-16/5.                                  (6)

There is no limiting Riemann-sum assertion in this estimate.
For an explicit strict logarithm bound, substitute u=(v-1)/(v+1)
in integral_1^5 dv/v. Since 1/(1-u^2)>1+u^2 for 0<u<=2/3,

    log(5)=2*integral_0^(2/3) du/(1-u^2)
          >2*[(2/3)+(2/3)^3/3]=124/81>3/2.                (7)

For n>=39, n/12>=13/4>16/5. Hence (6)--(7) yield

    S_n > (17/12)*n,
    |B_*(x)/B_*(x+s)| > exp(17*s*n/12).                    (8)

For |z|=R, |z-v_s|<=R+|v_s|<2R. Thus

    sup_(E_s)|F_z| >= |F_z(v_s)|
                    > (1/(2R))*exp(17*s*n/12).            (9)

On the other hand

    log(rho_s)=asinh(s/r)<=s/r=2s,
    2m*log(rho_s)<=(4/3)*n*s.                             (10)

The first inequality follows by integrating
(1+u^2)^(-1/2)<=1 from 0 to s/r; no asymptotic approximation in s
is used. Since rho_s>1, its denominator satisfies
rho_s^(2m)-1<rho_s^(2m). Combining (1), (9), (10) proves

    U_(n,s)(z) > (1/R)*exp((17/12-4/3)*s*n)
               = (1/R)*exp(s*n/12),

which is (3). It holds for every positive s in the specified interval,
including sequences tending to zero.

### Meaning and verification limits

The initial exploratory endpoint/ellipse screens suggested the same
Chebyshev poles as a possible all-angle countersequence. Equation (3)
instead shows that its proposed global-ellipse error bound cannot
certify that conclusion. It does not exclude cancellation in the
contour integral, another contour, an exact angular coefficient
argument, or another pole family. No inequality for a true error is
obtained by reversing (2). C645l's audited fixed-angle conclusion and
C645g's smaller-census theorem are unaffected.

Exact constant checks and full exploratory-screen output are in
`scripts/one-sided-hankel/rotation-ellipse-envelope-check.json`.
Reproduce from the notebook with
`python3 scripts/one-sided-hankel/rotation-ellipse-envelope-check.py`.
The rational checks support (6)--(10); the numerical screens are
explicitly uncertified and have no role in the proof. The analytic
argument above, not the screen or the arithmetic certificate alone,
establishes (3). A later independent proof audit remains outstanding.

## Mathlib

Full matching coverage has not been checked. No Mathlib absence claim
is made. Only elementary rational/product/integral inequalities and
C645l's specialized finite Chebyshev contour identity are used; neither
a library homepage nor a numerical check is treated as a theorem.
