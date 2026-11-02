# Corollary 645r: a compact Chebyshev radius band has a larger angular response

## Hypotheses

Use C645g's normalized Hardy spaces and C645o's rotated symbol. In
particular, put d=5/4, x=-d, R=11/8, U=R^2, eta=1/100, and
t_j=j/n for 0<=j<n. For |u|=1 define

    B_u(v)=product_(j=0)^(n-1) R*(v-t_j*u)/(U-t_j*conjugate(u)*v),
    W(v,u)=B_u(x)/B_u(v).

Here u=i*exp(i*theta); the denominator has the conjugated angle.
Let m>=3 be odd, n=3m, 1/4<=r<=9/20, and take the distinct poles

    a_l=x+i*r*cos((2*l-1)*pi/(2*m)), 1<=l<=m,

with original simple-pole residues all equal to one. The same pole
set is used at every angle. Set

    q_u(zeta)=sum_l [W(a_l,u)/R]/(zeta-a_l/R),
    H_u f=P_-(q_u*f),
    E_op=mean_(|u|=1) ||H_u||^2,

using normalized angular measure and the largest operator norm.
No actual-Xi realization or independent upper bound is assumed.

## Conclusion

There are constants c>0 and n_0, independent of r, m and n, such that
all the stated families with n>=n_0 satisfy

    sqrt(E_op) >= c*sqrt(n)*exp(-gamma*n),
    gamma=61/2000+4/10^6=3813/125000=0.030504 < 31/1000 < 1/32. (1)

In fact the same lower bound, with another uniform c, holds for
||H_u|| at every u=exp(i*phi) with |phi|<=10^(-6). Consequently
exp(n/32)*sqrt(E_op) tends to infinity uniformly over this radius
band as n=3m tends to infinity through odd m. By C645q, (1) also
implies the nominated weaker bound for sqrt(E_HS), without needing
its rank loss: this proof directly tests the constant Hardy input.

This excludes angular countersequences within this compact Chebyshev
band. It does not establish the detector for other radii or arbitrary
admissible pole families. It supplies neither Xi realization nor signs.
The proof is a local quantitative calculation within the saved EXPLORE
scope; no certified originality is claimed. A separate conceptual audit
on 2 November 2026 verified the argument and replayed the exact rational
certificate without a mathematical correction; its checks are below.
The uniform constants/onset are existential, not numerically evaluated.

## Proof

### Source scope and the necessary specialization

The unchanged invocation-start
[assessment](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md)
covers Fourier/coefficient and residue/contour tests of exactly this
angular family. Its inspected source comparisons and the recorded
ellipse, inner-input, cross-entry and continuation-functional stops
are reused. Those stops do not imply a bound on this subfamily's full
angular response. C645q's preceding finite screen is motivation only.

Import the residue theorem, simple-pole rule and contour-integral
inequality from R. W. Howell and J. H. Mathews, *Complex Analysis*,
online edition (front matter updated 22 August 2025),
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
and [Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html).
These are the previously inspected inputs, not theorems reproved here.
Use the normalized Hankel convention from L. Baratchart, S. Chevillard
and T. Qian, *Minimax principle and lower bounds in H2-rational
approximation*, J. Approx. Theory 206 (2016), 17--47, preprint v2,
[Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Scalar Fourier Parseval is imported from A. Levitt, *Analyse de Fourier
et applications*, [author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
version retrieved 2 November 2026, Theorem 1.11/Corollary 1.12,
printed p.8 (PDF p.14); our measure is divided by 2*pi.

C645l supplies its exact finite-node identity (23)--(24). We specialize
that identity to the coefficient integrands below. We do not import
its fixed-direction product gain. No unread steepest-descent or
quadrature asymptotic theorem is used: the uniform error for these
n-dependent products is proved directly. The elementary Laplace
integral is evaluated by the already imported contour theorem, keeping
its positive constant unevaluated. None of the cited general identities
provides the quantitative lower estimate (1).

### 1. Geometry, coefficients, and a fixed angular interval

The nodes are distinct, include x since m is odd, and have

    |a_l|^2 <= d^2+r^2 <= 29/16 < (R-eta)^2,
    (R-eta)^2-29/16=2029/40000.

They avoid every rotated grid because |a_l|>=d>1>t_j. Thus M=m=n/3
and all original family hypotheses hold. As in C645g/C645o, the
symbol has the absolutely convergent exterior expansion

    q_u(zeta)=sum_(k>=0) c_k(u)*zeta^(-k-1),
    c_k(u)=sum_l W(a_l,u)*a_l^k/R^(k+1),
    ||H_u|| >= ||q_u||_2 >= (|c_0(u)|^2+|c_1(u)|^2)^(1/2).   (2)

For each fixed family this follows from |a_l|/R<1, finite sums,
H_u 1=q_u, and scalar Parseval. No uniform bound on all coefficients
is needed to retain the first two nonnegative square terms.

Set epsilon=10^(-6) and restrict for now to u=exp(i*phi),
|phi|<=epsilon. All contours used below lie in

    Re v <= -23/20, |Im v|<=1/2, |v|<2.                     (3)

The anchor also lies there. On this region, cos(phi)>99/100 and
|sin(phi)|<=epsilon give

    |v-t*u| >= 23/20,
    Re(U-t*conjugate(u)*v) >= U,

for 0<=t<=1. In particular W is holomorphic as a function of v
on and inside the contours: its only possible poles are v=t_j*u,
which are to the right. The possible poles of B are zeros of W
and do not create a singularity in W; in (3) they are absent anyway.

For a single disk factor b_(t,u)(v)=R*(v-t*u)/(U-t*conjugate(u)*v),

    |partial_phi log b_(t,u)(v)|
       <= t/|v-t*u|+t*|v|/|U-t*conjugate(u)*v| < 2.

Integrate this logarithmic derivative along the angular interval,
for v and for x separately. No choice of a global logarithm is
necessary for the real logarithm of the modulus. Uniformly on (3),

    |log|W(v,exp(i*phi))|-log|W(v,1)|| <= 4*n*epsilon.          (4)

This will give a fixed positive angular measure, not an exponentially
shrinking neighborhood inferred from a large absolute derivative.

### 2. Both endpoint weights have rate less than 0.030504

Write a_+=x+i*r and a_-=x-i*r; these are segment endpoints, not added
poles. At u=1 their logarithmic product gain is

    -log|W(a_+,1)|=-log|W(a_-,1)|=sum_j f_r(t_j),
    f_r(t)=1/2*[log(1+r^2/(d+t)^2)
                    -log(1+r^2*t^2/(U+d*t)^2)].             (5)

Since U>t^2, f_r>=0 and is increasing in r: after differentiation
in r the required comparison is U+d*t>t*(d+t). It is decreasing
in t, since the first logarithm decreases and the second increases.
For a decreasing nonnegative function, comparison on each interval
[j/n,(j+1)/n] gives the finite, nonasymptotic inequality

    sum_j f_r(j/n) <= n*integral_0^1 f_r(t) dt + f_r(0).       (6)

Here f_r(0)<=r^2/(2*d^2)<=81/1250. At r=9/20, put

    A=r^2/(d+t)^2, B=r^2*t^2/(U+d*t)^2,
    g(t)=(A-A^2/2+A^3/3-B+B^2/2)/2.

The alternating logarithm bounds, or integration of their polynomial
derivatives, give f_r(t)<=g(t). Throughout [0,1], 0<=B<A<1.
The polynomial A-A^2/2+A^3/3 is increasing in A, while B-B^2/2
is increasing in B. As A decreases and B increases with t, g is
decreasing. Its left Riemann sum is therefore a rigorous upper bound
for its integral. The exact rational certificate gives

    integral_0^1 f_(9/20)(t) dt
      <= integral_0^1 g(t) dt
      <= (1/512)*sum_(k=0)^511 g(k/512)
      <= 15559465959309/512000000000000 < 61/2000.             (7)

Each rational g(k/512) was rounded upward to a multiple of 10^(-12)
before summation; the displayed bound is that rounded sum. The strict
margin is 56534040691/512000000000000. This is an exact bound, not
uncontrolled quadrature. The full algorithm and parameters are in
`scripts/one-sided-hankel/angular-endpoint-rate-certificate.py`; its
certificate is the adjacent `.json`. Reproduce from this notebook with

    python3 scripts/one-sided-hankel/angular-endpoint-rate-certificate.py

Combining (4)--(7), uniformly for both signs, r in the closed band
and |phi|<=epsilon, yields

    |W(a_+,u)|, |W(a_-,u)| >= exp(-81/1250)*exp(-gamma*n).     (8)

The signs and complex phases of these two weights are not identified.

### 3. Continuous coefficient averages and the connecting segment

For k=0,1 define

    F_k(v,u)=W(v,u)*v^k/R^(k+1),
    A_k(u)=(1/pi)*integral_(-r)^r
                     F_k(x+i*y,u)/sqrt(r^2-y^2) dy.          (9)

Deform the vertical segment to the three sides of the rectangle on
its left with horizontal width s=1/2: travel from a_- to a_--s,
then upwards to a_+-s, then to a_+. Throughout its interior choose

    S(v)=sqrt((v-x)^2+r^2)

with positive real part. The radicand has positive real part there,
and on the open original segment S=sqrt(r^2-y^2)>0. Both endpoint
zeros are simple. Truncating small endpoint neighborhoods and applying
the residue theorem with no enclosed poles gives

    A_k(u)=(1/(pi*i))*integral_(three sides) F_k(v,u)/S(v) dv. (10)

The omitted endpoint arcs are O(sqrt(h)) for each finite n; their
integrals vanish. The endpoint integrals are absolutely convergent.
This verifies the branch and orientation in (10). Unlike a boundary
resolvent, F_k has no pole at a boundary point z: the left rectangle
may extend outside |v|<R without creating a singularity.

At u=1, for v=-h+i*y and h>0,

    |b_(t,1)(v)|^2=R^2*((h+t)^2+y^2)/((U+h*t)^2+t^2*y^2)

is increasing in y^2 because U>t^2. At y=0, its logarithmic
derivative in h is (U-t^2)/((h+t)*(U+h*t))>0. For t<=1/2,

    log(|b_(t,1)(x-s)|/|b_(t,1)(x)|)
      =integral_d^(d+s) (U-t^2)/((h+t)*(U+h*t)) dh
      >= (1/2)*(U-1/4)/((9/4)*(U+7/8))=70/531.

At least n/2 grid indices have t_j<=1/2, and the other gains are
nonnegative. Hence on the entire connecting segment v=x-s+i*y,

    |W(v,1)|<=exp(-35*n/531),
    |W(v,u)|<=exp(-(35/531-4*epsilon)*n)<=exp(-3*n/50).        (11)

Here |S(v)|>=s=1/2 and |v|<2, so the connecting contribution to
each A_k is O(exp(-3*n/50)), with an absolute uniform constant.

### 4. Endpoint expansions with uniform, relative error

Define the normalized logarithmic derivative

    p_n(v,u)=-B_u'(v)/(n*B_u(v))
       =(1/n)*sum_j [-1/(v-t_j*u)
                    -t_j*conjugate(u)/(U-t_j*conjugate(u)*v)].

On both horizontal segments v=x-h+i*y, 0<=h<=1/2, y=+r or -r,
we claim uniformly

    Re p_n(v,u)>=1/100, |p_n(v,u)|<=2, |partial_v p_n(v,u)|<=2. (12)

For the lower bound first put u=1, q=d+h, A=q+t, B=U+q*t.
The real part of the single summand is exactly

    (U-t^2)*(A*B-t*y^2)/((A^2+y^2)*(B^2+t^2*y^2)).

Its numerator exceeds 19/10 since
(U-1)*(d*U-(9/20)^2)>19/10. Its denominator is less than 105,
using A<=11/4, B<=233/64 and |y|<=9/20. Thus it exceeds
19/1050. The angular derivative of a single summand has modulus
at most (20/23)^2+1/U<2, so angular perturbation subtracts at
most 2*epsilon; the result still exceeds 1/100. The other bounds
in (12) follow from |v-t*u|>=d and |U-t*conjugate(u)*v|>=U:
1/d+1/U<2 and 1/d^2+1/U^2<2. These estimates are uniform in n.

Put p_+=p_n(a_+,u), p_-=p_n(a_-,u), and

    J=integral_0^infinity exp(-t)*t^(-1/2) dt > 0.

This integral is finite. For Re p>0 its scaled version is

    integral_0^infinity exp(-p*t)*t^(-1/2) dt=J*p^(-1/2),    (13)

with the principal square root. To justify the complex p case using
the imported contour theorem, substitute z=p*t and rotate the ray
arg z=arg p to the positive real ray in the slit plane. The small
arc is O(sqrt(h)); the large arc tends to zero because the sector
is strictly inside |arg z|<pi/2. Equation (12) keeps arg p uniformly
away from its boundary. No asymptotic theorem is used here and no
value of J, beyond positivity and finiteness, is required.

On a horizontal segment parameterized by v=a_+-h or a_--h, let

    G(h)=integral_0^h p_n(a_+-t,u) dt

or the corresponding expression with a_-. Exactly, W(v,u)=
W(a_+,u)*exp(-n*G(h)), with the analogous lower formula. From (12),

    Re G(h)>=h/100, Re(p_+*h)>=h/100,
    |G(h)-p_+*h|<=h^2,

and likewise for the lower endpoint. Interpolation between the two
exponentials therefore gives

    |exp(-n*G(h))-exp(-n*p_+*h)|
                  <= n*h^2*exp(-n*h/100).                  (14)

The square roots on the horizontal pieces are, with the branch in (10),

    S(a_+-h)=sqrt(h)*sqrt(h-2*i*r),
    S(a_--h)=sqrt(h)*sqrt(h+2*i*r).

After taking out h^(-1/2), the remaining amplitude
(a_+-h)^k/(R^(k+1)*sqrt(h-2*i*r)), or its lower version,
has uniformly bounded value and first derivative for 0<=h<=s,
1/4<=r<=9/20 and k=0,1. This follows directly from
|h+/-2*i*r|>=2*r>=1/2 and |a_+/- -h|<2. Replacing that amplitude
by its value at zero costs O(h). By (14), integration of the two
errors is bounded by constants times

    integral_0^s [n*h^(3/2)+h^(1/2)]*exp(-n*h/100) dh
                                                     =O(n^(-3/2)).

Extending the leading integral to infinity costs
O(exp(-n*s/100)/n), which is also O(n^(-3/2)) uniformly for n>=1.
Multiplying back by the endpoint weight gives a relative error
O(n^(-3/2))*|W(a_+,u)| for the upper endpoint and the corresponding
lower one. All constants are independent of n,r,u in the stated sets.

Keeping the orientations in (10) now yields, for k=0,1,

    A_k(u)=J/(pi*i*sqrt(n))*[
        W(a_+,u)*a_+^k/(R^(k+1)*sqrt(-2*i*r)*sqrt(p_+))
       -W(a_-,u)*a_-^k/(R^(k+1)*sqrt( 2*i*r)*sqrt(p_-))]
       +O(n^(-3/2))*(|W(a_+,u)|+|W(a_-,u)|)
       +O(exp(-3*n/50)).                                    (15)

The last error is (11). The minus sign before the lower term comes
from travel away from a_-; the upper horizontal piece travels towards
a_+. Neither contribution has been discarded or made positive.

### 5. Two spatial coefficients prevent phase cancellation

Let V be the two-column matrix with columns (1/R,a_+/R^2) and
(1/R,a_-/R^2). Its determinant is -2*i*r/R^3, of modulus at
least 1/(2*R^3)>1/6. Since |a_+/-|<R and R>1, its Frobenius norm
is less than 2. The smaller singular value is therefore greater
than 1/12: the product of its two singular values is |det V|,
and the larger is at most its Frobenius norm. This is elementary
two-dimensional linear algebra, not a lower bound for a Hankel
least singular value substituted for its largest norm.

By (12), each diagonal endpoint multiplier
1/(sqrt(+/-2*i*r)*sqrt(p_+/-)) has modulus at least 1/sqrt(2).
Consequently the norm of the leading vector in (15), for k=0,1,
is at least

    J/(24*pi*sqrt(n))*(|W(a_+,u)|+|W(a_-,u)|).                (16)

This holds for arbitrary phases of both weights. In particular, it
does not require a nonvanishing cosine or selection of a phase-dependent
subsequence. The two relative errors in (15) have vector norm at
most C*n^(-3/2) times the same sum. For sufficiently large n,
uniformly in r,u, they are at most half of (16). By (8), the
connecting error O(exp(-3*n/50)) can then be absorbed as well.
Thus for some uniform c_1>0 and one uniform onset,

    (|A_0(u)|^2+|A_1(u)|^2)^(1/2)
                          >= c_1*n^(-1/2)*exp(-gamma*n).     (17)

### 6. The finite Chebyshev remainder is smaller

Use the ellipse centered at x with horizontal semiaxis s_e=1/10
and vertical semiaxis b=sqrt(r^2+s_e^2), and put

    rho=(sqrt(r^2+s_e^2)+s_e)/r>1.

This ellipse lies in (3) because b<=sqrt(17/80)<1/2 and |v|<2.
F_k is holomorphic on and inside it. C645l (23)--(24), with
w=v-x=i*r*(lambda+lambda^(-1))/2, therefore gives exactly

    mu_k(u)=(1/m)*sum_l F_k(a_l,u)=c_k(u)/m,
    |mu_k(u)-A_k(u)| <= 2*sup_ellipse |F_k(v,u)|/(rho^(2*m)-1). (18)

Its normalization and factor 2m are unchanged. Changing r and using
F_k in place of a boundary resolvent affects neither the polynomial
logarithmic derivative identity nor the residue calculation.

For u=1, write v=-h+i*y. The modulus of a disk factor increases
with y^2 as in Section 3 and, on the negative real line, with h.
Here h>=d-s_e=23/20. If h>=d the ratio |b_(t,1)(x)/b_(t,1)(v)|
is at most one; if 23/20<=h<d, it is at most

    (d+t)/(h+t)*(U+h*t)/(U+d*t) <= d/h <=25/23.

Hence, by (4) and log(25/23)<2/23,

    sup_ellipse |F_k(v,u)| <=2*exp((2/23+4*epsilon)*n).        (19)

Also

    log rho=integral_0^(s_e/r) (1+t^2)^(-1/2) dt
       >= s_e/sqrt(r^2+s_e^2) >= 2/sqrt(85) > 8/37.

Since n=3m, 2*m*log rho >16*n/111. For n>=9 this exceeds one,
so (rho^(2m)-1)^(-1)<2*rho^(-2m). Finally

    16/111-2/23-4*epsilon > 11/200 > gamma.

Equations (18)--(19) imply the uniform bound

    |mu_k(u)-A_k(u)| <=8*exp(-11*n/200), k=0,1.              (20)

As 11/200>gamma, (20) is o(n^(-1/2)*exp(-gamma*n)) uniformly
in r,u. Absorb its vector norm into (17), multiply by m=n/3,
and use (2). For all sufficiently large n in the stated sequence,

    ||H_u|| >= (|c_0(u)|^2+|c_1(u)|^2)^(1/2)
                         >= c_2*sqrt(n)*exp(-gamma*n),       (21)

uniformly in the entire closed radius band and |phi|<=epsilon.
There is one onset because every error constant above is uniform.

The interval |phi|<=epsilon has normalized measure epsilon/pi;
the change from theta to phi preserves measure. Squaring (21),
integrating only over this interval, and taking a square root proves
(1), with c=c_2*sqrt(epsilon/pi). These operations involve continuous
finite-family symbols and a nonnegative integrand. No limit is
interchanged with an unbounded angular integral. The positive gap
1/32-gamma implies the stated uniform divergence.

### Verification and limits

The exact rational script checks (7) and the rational margins used in
(11), (12) and (20), writing complete values and failures to its JSON
certificate. It does not certify the analytic deformation, asymptotic
error, phase separation or infinite-family conclusion independently
of this proof. Those arguments were checked in the separate audit below.
No prior diagnostic screen is used as proof. The full angular target
and all bridges to actual Xi remain unresolved.

### Separate conceptual audit — 2 November 2026

This audit verifies the existing restricted-family estimate (1), not
the full angular detector. The ready source comparison is unchanged.
No theorem about a general pole distribution or new radius interval is
being asserted. The following checks found no mathematical correction.

1. **Admissibility and the constant input.** Odd m supplies exactly one
   anchor node; all m cosine nodes are distinct with unit residues, so
   M=m=n/3. The clearance calculation uses the conservative bound
   d^2+r^2<=29/16, valid throughout this smaller radius band. Since
   |a_l|>=d>1, no grid rotation hits a pole. Substituting
   u=i exp(i theta) gives exactly C645o's conjugated-angle denominator.
   The finite pole sum and |a_l|/R<1 justify its exterior Fourier
   expansion. In C645g's normalized spaces, ||1||_2=1 and H_u1=q_u;
   (2) is consequently a lower bound for the largest norm. Only the
   definitions and Fourier identities from those corollaries are used.

2. **The two branches and endpoint orientations.** Write v-x=-h+i*y
   in the rectangle. The radicand has real part h^2+r^2-y^2>0 in
   its interior, so the square root with positive real part continues
   from the original segment without crossing a cut. Removing small
   endpoint disks leaves an analytic integrand and closed contour;
   each removed arc is O(sqrt(h)) for fixed n. Uniformity in n is not
   needed for this exact deformation. The bottom horizontal path runs
   away from a_- with dv=-dh; the top runs towards a_+. This gives
   precisely the minus and plus signs in (15), with principal roots
   sqrt(h+2*i*r) and sqrt(h-2*i*r), respectively. The rectangle may
   leave |v|<R: its only possible W poles are the grid zeros to its
   right, and F_k has no boundary-resolvent pole.

3. **Uniform angular and horizontal estimates.** Throughout (3),
   Re(conjugate(u)*v)<0 and Re(v-t*u)<=-23/20, proving the stated
   denominator bounds. On the endpoint segments the latter improves
   to -d. Differentiating a summand of p_n in phi has modulus at most
   t/|v-t*u|^2+t*U/|U-t*conjugate(u)*v|^2, which is bounded by
   (20/23)^2+1/U. At u=1 its real part is exactly the rational
   expression displayed in Section 4; its numerator lower bound and
   denominator upper bound give (12) after the angular perturbation.
   Both Re G(h) and Re(p_+/-*h) are at least h/100. Every convex
   combination has that lower bound, so the integral identity for the
   difference of exponentials gives (14) with its decaying factor.
   The amplitude and its first derivative are uniformly bounded
   because r>=1/4. Substitution t=n*h in the two error integrals gives
   n^(-3/2) times finite integrals independent of n,r,u; the tail
   from s to infinity is bounded by C*n^(-1)*exp(-n*s/100).
   These are relative errors multiplied by the corresponding endpoint
   weight, even when the two endpoint moduli differ exponentially.
   For (13), Re p>=1/100 and |p|<=2 keep the rotated ray uniformly
   inside the right half-plane. The small/large contour arcs vanish
   with the stated principal-root convention.

4. **Phases and uniform absorption.** The determinant calculation for
   V uses 2r/R^3>=1/(2R^3)>1/6 and ||V||_F<2, so its smaller
   singular value exceeds 1/12. Each endpoint diagonal multiplier
   has modulus >=1/sqrt(2), since 2r*|p_+/-|<=4r<2. Combining
   this with (|z_+|^2+|z_-|^2)^(1/2)>=(|z_+|+|z_-|)/sqrt(2)
   gives the coefficient 1/24 in (16), for arbitrary complex phases.
   The ratio of the relative error to this leading norm is O(1/n).
   From (8), the ratio of the connecting error is at most a uniform
   constant times sqrt(n)*exp(-(3/50-gamma)*n), which tends to zero.
   Thus (17) has one onset, rather than a subsequence chosen to avoid
   phase cancellation.

5. **Finite nodes and their distinct square-root branch.** C645l's
   identity (23)--(24) applies to every positive r and holomorphic f;
   its derivation, read in full for this audit, does not depend on its
   earlier choice r=1/2 or on the boundary-resolvent form of f. Here
   lambda on |lambda|=rho parameterizes the ellipse positively, and
   S_0=ir*(lambda-lambda^(-1))/2 satisfies dw/S_0=d lambda/lambda.
   This exterior branch is distinct from the rectangle branch S.
   The contour identity and deformation in the lambda annulus yield
   the same arcsine average A_k, with m simple residues and exponent
   2m. There is no extra factor from traversing the segment twice.
   The modulus comparison on the ellipse is valid for every factor;
   (19) and the lower bound log rho>8/37 give the uniform remainder
   (20). Its ratio to (17) is at most a uniform constant times
   sqrt(n)*exp(-(11/200-gamma)*n), also tending to zero. The original
   node coefficients are c_k=m*mu_k, so multiplication by m=n/3
   produces the sqrt(n) in (21).

6. **Exact rates and angular measure.** Reviewed the rational script
   before replay. Its logarithm majorant is pointwise valid; its two
   constituent polynomials are increasing in A,B in their stated
   ranges, making g decreasing. Thus its 512 left samples, rounded
   upwards as exact rationals, rigorously bound the integral. Replay
   reproduced the upper bound and strict margin in (7), and all nine
   auxiliary inequalities passed. The full selected upper-bound,
   margin, auxiliary-check and failure fields of
   `scripts/one-sided-hankel/angular-endpoint-rate-certificate.json`
   were inspected with the shared JSON inspector; failures are empty.
   The resulting gamma=3813/125000 has exact margin
   1/32-gamma=373/500000>0. The interval |phi|<=10^(-6) has fixed
   normalized measure 10^(-6)/pi. The finite-family symbol is
   continuous in angle in the uniform boundary norm, hence H_u is
   continuous in operator norm. Integrating its nonnegative squared
   norm on that interval proves (1), with no angular sampling or
   exchange of an uncontrolled limit.

The auxiliary implication for E_HS uses only ||H_u||<=||H_u||_HS,
verified from the convergent coefficient series and finite-rank argument
in C645q; none of its numerical screen is an input. This audit does not
certify all other claims of C645o or C645q. Constants and onset in (1)
remain existential. There is no improvement of the exponent or radius
scope, no new source import and no actual-Xi positivity conclusion.

## Mathlib

Full matching coverage has not been checked; no absence claim is made.
Supporting ingredients are scalar Fourier Parseval, the residue/contour
theorem, elementary product differentiation and two-dimensional linear
algebra. The checked literature supplies those general tools, not the
uniform quantitative Chebyshev-band estimate (1).
