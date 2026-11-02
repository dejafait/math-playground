# Lemma 665: independent displacements defeat the inherited anchor approximation and its absolute kernel transfer

## Hypotheses

Retain L649's full product, conjugated denominator angle and original
unit residues. Thus x=-d=-5/4, R=11/8, U=121/64, t_j=j/n, and

    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a).

Take n=12q+3, q>=1, h=27/(5n), and delta=1/4 in L664.
Write H_0=h/2=27/(10n), tau=H_0/8=27/(80n), and Y_n=qh.
The nonanchor ordinates of its family are exactly

    Y_0={H_0*(m+1/2): -2q<=m<2q}.

Each real ordinate y may be displaced independently by epsilon_y,
|epsilon_y|<=tau. The anchor x is fixed. Restrict to distinct poles
on Re(a)=x with |a|<=R-1/100, as in L649. With M=4q+1=n/3 put

    T_M(v)=sum_(0<=k<M) v^k,
    G_e(u,zeta)=R^(-1) sum_(a in Z_e) W_a(u) T_M(a*zeta/R),
    D_e=sum_(a in Z_e) mean_u |W_a(u)|^2/(U-|a|^2).

Here Z_e contains x and all x+i*(y+epsilon_y), each with residue
one. The full product and every prescribed spatial moment are retained.
All circle measures and L2 norms are normalized. The subscript 0
denotes the undisplaced family, not a spatial coefficient.

Consider two different perturbations within these hypotheses:

1. **One node:** displace only y=H_0/2 outward by tau.
2. **Outward pairs:** set epsilon_y=tau*sign(y) for every y in Y_0.

For the second family define the finite node polynomials and kernels

    P_e(z)=product_(y in Y_0)(z-y-epsilon_y),
    K_e(z)=P_e'(z)/P_e(z),       Delta K=K_e-K_0.

Set b=1/50, c=1/200. Let Gamma_n be the positively oriented boundary
of [-Y_n,Y_n]+i[-b,c], with its lower edge running left to right.
The full absolute perturbation cost at u=-1 is

    A_e=(1/(2*pi*R)) integral_(Gamma_n)
         |W_(x+i*z)(-1) Delta K(z)|
         *||T_M(((x+i*z)/R)*zeta)||_2 |dz|.

This is the absolute cost of one specified contour representation;
it is not the norm of the signed difference or a minimum over contours.

## Conclusion

Both displayed perturbations are admissible. For the one-node family,
there is a real g with 9/5<g<11/5 such that, uniformly for |zeta|=1,

    G_e(-1,zeta)-R^(-1)T_M(x*zeta/R)
        -> A/[R*(1-x*zeta/R)],
    A=exp(27*i*g/16)-exp(27*i*g/20),       |A|>1/2.     (1)

Consequently a uniform o(1) version of L664's inherited-anchor error
is false for the approved independently displaced class. In particular
the constant-coefficient error has limit A/R, not zero. This is not
a smallness assertion about G_e itself.

For the outward-pair family and n>=3000 in the prescribed sequence,

    A_e >= exp(9*n/250-1)/(800*pi*R*n).                 (2)

Let sigma^2=137/5000, kappa=91/5000 and

    c_*=sqrt(3*sigma^2)*exp(-4)/(800*pi*R)>0.

The comparison with the actual squared-residue diagonal is

    A_e/(exp(-n/32)*sqrt(D_e))
          >=c_* n^(-3/2) exp(981*n/20000),              (3)
    A_e/(n*exp(-n/32)*sqrt(D_e))
          >=c_* n^(-5/2) exp(981*n/20000) -> infinity.  (4)

The additional factor n in (4) retains the logarithmic measure charge
in L658's sufficient threshold. These inequalities stop transfer from
L664 by an o(1) inherited-anchor error, and stop bounding this finite
kernel difference by its absolute cost on Gamma_n. They do not stop
all signed kernel estimates, upper-bound every allowed arc, refute
the paid-arc criterion, or give an RH counterexample. Arbitrary support,
Xi realization and signs remain open. This local method obstruction
has not received a separate critical audit; no certified originality
beyond the recorded source search is claimed.

## Proof

### 1. Gate, imports, and admissibility

The invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-independent-grid-displacement-paid-arc.md`
approves this finite-kernel perturbation test, including a quantitatively
decisive perturbation cost. Reuse its known-result comparison: perturbed
interpolation quadrature changes the weights, while the inspected
Mahler-continuity bound requires relative coefficient control and
retains growing term-count dependence. Neither supplies the desired
transfer. The scoped full-circle, endpoint-dominance and phase-census
stops concern other estimates and are not premises of this proof.

Import only the finite residue theorem and simple-pole rule from
R. W. Howell and J. H. Mathews, *Complex Analysis*, online edition,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
with the contour integral bound in
[Section 6.2, Theorem 6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html).
These primary statements are already covered by the ready assessment.
We specialize them to a finite polynomial logarithmic derivative;
no periodic quadrature or infinite alias identity is imported.
L664 supplies its audited exact-grid error and the product estimates
used below, L661 its audited general diagonal envelope, and L658 the
paid-localization threshold. No general theorem is reproved.

The positive base ordinates are H_0*(j+1/2), 0<=j<2q. Moving only
the first one by H_0/8 leaves it strictly between zero and the next
node. For outward pairs the spacing on each half remains H_0 and
the central gap increases. In that family the largest ordinate is

    Y_n-H_0/2+tau=Y_n-3*H_0/8<Y_n<9/20.

The same outer bound holds for the one-node family. Both have exactly
M=4q+1 distinct poles, all original residues one, and

    |a|^2<d^2+(9/20)^2=353/200<(273/200)^2.

This verifies L649 admissibility, with the actual squared census kept.

### 2. An actual nonvanishing anchor error

At u=-1, L664's exact product ratio at e=d is

    W_(x+i*y)(-1)=product_j (1+i*b_j*y)/(1-i*A_j*y),
    A_j=1/(d-t_j),       b_j=t_j/(U-d*t_j).

All A_j and b_j are nonnegative and at most 4. Define

    g=integral_0^1 [1/(d-t)+t/(U-d*t)]dt.

The monotone Riemann sums in L664 give
sum_j(A_j+b_j)/n -> g. Its monotonicity in e and certified bounds
g(R)>9/5 and g(123/100)<11/5 imply 9/5<g<11/5.

For either fixed v=27/20 or v=27/16, put y=v/n. For n>=15,
the arguments i*b_j*v/n and -i*A_j*v/n have modulus at most 1/2.
The convergent logarithm series on that disk gives

    |log(1+w)-w|<=|w|^2/[2*(1-|w|)]<=|w|^2.

Adding these logarithms of the finite product therefore gives

    log W_(x+i*v/n)(-1)
       =i*v*sum_j(A_j+b_j)/n+E_n(v),
    |E_n(v)|<=32*v^2/n.

Exponentiation proves W_(x+i*v/n)(-1)->exp(i*g*v). This argument
chooses the logarithm of each factor near one; it does not assume a
global logarithm of an angular function or interchange infinite products.

For the moved node, the old and new ordinates are respectively
27/(20n) and 27/(16n). The exact full-polynomial difference is

    G_e(-1,zeta)-G_0(-1,zeta)
      =R^(-1)[W_(x+27i/(16n))(-1)
                    *T_M((x+27i/(16n))*zeta/R)
               -W_(x+27i/(20n))(-1)
                    *T_M((x+27i/(20n))*zeta/R)].       (5)

Admissibility gives |a/R|<=rho=273/275<1. The finite geometric
sum differs from 1/(1-a*zeta/R) by at most rho^M/(1-rho), uniformly
on the spatial circle. The latter function tends uniformly to
1/(1-x*zeta/R), because a->x and both denominators are bounded
away from zero. Thus (5) tends uniformly to the expression in (1).
L664's uniform error 1000*n*exp(-n/3000)->0 identifies G_0 with
the stated anchor polynomial for this limit. Every moment was present
before this controlled limit was taken.

Finally set t=27*g/160. Then 243/800<t<297/800<3/8, and

    |A|=2*sin t,
    sin t>=t-t^3/6>(243/800)*(1-(3/8)^2/6)>1/4.

The sine bound follows by integrating cos s>=1-s^2/2 on this interval.
This proves |A|>1/2. Taking constant coefficients, or integrating (5)
over the spatial circle, proves the asserted constant-coefficient
limit. A nonzero limiting change is sufficient to disprove the o(1)
approximation; it says nothing by itself about all allowed arcs.

### 3. Exact finite kernel with all endpoints and moments

For the outward-pair family, all old and new ordinates lie strictly
between -Y_n and Y_n. Neither node polynomial has a boundary root.
Differentiating a finite product gives

    K_e(z)=sum_(y in Y_0) 1/(z-y-epsilon_y).

Every summand has residue one. The holomorphy checks of L664 apply
on a neighborhood of the full closed rectangle: if z=s+i*v, then
a=x+i*z=-e+i*s, 123/100<=e<=251/200, |a|<4/3<R, and its possible
variable denominator zeros a=-t_j lie outside the rectangle.
Thus the cited finite residue theorem gives exactly

    G_e(-1,zeta)-G_0(-1,zeta)
      =(1/(2*pi*i*R)) integral_(Gamma_n)
           W_(x+i*z)(-1) Delta K(z)
           T_M(((x+i*z)/R)*zeta) dz.                  (6)

The anchor cancels because it is unchanged. All four finite sides
remain in (6); no infinite periodic kernel has replaced P_e'/P_e.
The integral is a polynomial with exactly the prescribed M moments.

Finite Fourier orthogonality gives

    ||T_M((a/R)*zeta)||_2^2=sum_(0<=k<M)|a/R|^(2k)>=1.

The triangle inequality for this finite coefficient vector, applied
to Riemann sums and then their continuous contour integral, gives
||G_e(-1,.)-G_0(-1,.)||_2<=A_e. It also bounds each coefficient
error by A_e. There is no claim that this inequality is close to
equality. The following estimates lower-bound this absolute cost.

### 4. A nonvanishing lower-edge kernel difference

Pair the positive ordinate y with -y. At z=-i*b their contribution
to Delta K is

    2*i*b/(b^2+(y+tau)^2)-2*i*b/(b^2+y^2)
      =-2*i*b*(2*y*tau+tau^2)
                   /[(b^2+y^2)*(b^2+(y+tau)^2)].       (7)

Every such term has the same imaginary sign. For b<=y<=2b and
tau<=b, its modulus is at least

    2*b*(2*b*tau)/[(5*b^2)*(10*b^2)]
                       =2*tau/(25*b^2)=200*tau.

For n>=3000 the entire interval [b,2b] is inside the positive
finite grid range. Its lattice count is at least
b/H_0-1=n/135-1>=n/270. Hence

    |Delta K(-i*b)|>=200*tau*n/270=1/4.               (8)

This is a finite sum of same-sign contributions, not a quadrature
limit. It uses only a subset to lower-bound that sum.

For a single displaced real node, along the line Im z=-b,

    1/(z-y-epsilon)-1/(z-y)
                       =integral_0^epsilon (z-y-t)^(-2)dt.

Differentiating in z shows that its derivative has modulus at most
2*|epsilon|/b^3. There are 4q<n/3 displaced nodes. Therefore

    |(Delta K)'(s-i*b)|<=2*n*tau/(3*b^3)=28125

for every real s. For |s|<=1/(100n), n>=3000, the variation from
(8) is at most 28125/(100n)<=3/32. In particular

    |Delta K(s-i*b)|>=1/8.                            (9)

There are no hidden near-node singularities in this estimate: the
distance to every real displaced or original node is at least b.

### 5. Full-product growth and the paid comparison

On the segment in (9), a=x+i*(s-i*b)=-(d-b)+i*s. Put e=d-b.
For L664's real product W_e(0), logarithmic differentiation gives

    log W_e(0)=integral_e^d g_n(v)dv,
    g_n(v)=sum_j[1/(v-t_j)+t_j/(U-v*t_j)].

L664 proves that g_n decreases with v on this range, and
g_n(R)>=9*n/5-128/33. Consequently

    log W_e(0)>=b*(9*n/5-128/33)=9*n/250-64/825.

Its complete product ratio at real s is again
product_j(1+i*b_j*s)/(1-i*A_j*s), now with e=123/100.
Here A_j<=100/23 and b_j>=0. Since log(1+w)<=w for w>=0,

    log|W_e(s)/W_e(0)|
       >=-(1/2)sum_j A_j^2*s^2
       >=-10*n*s^2>=-1/(1000*n).

As 64/825+1/(1000n)<1, throughout the segment

    |W_(x+i*(s-i*b))(-1)|>=exp(9*n/250-1).            (10)

The segment has length 1/(50n). Restrict the nonnegative integral
defining A_e to it, and combine (9), (10) and the full spatial norm
bound >=1. This proves (2), including its factor 800*pi*R*n.
Other sides have not been removed from the signed identity (6);
restricting an absolute integral is legitimate for this lower bound.

The audited general envelope of L661 applies to this original family:

    D_e<=n*exp(2*kappa*n+6)/(3*sigma^2).

Dividing (2) by exp(-n/32)*sqrt(D_e), using this upper bound in
the direction required for a lower ratio, proves (3), because

    9/250+1/32-91/5000=981/20000>0.

Dividing again by n proves (4). L658's sufficient condition is
H_e>=log(D_e)/2-n/32+log n, so this factor n explicitly retains
its shrinking-arc measure charge. A fixed additive constant in that
condition does not change the exponential mismatch.

Subtracting the absolute error from the exact-grid anchor would give
only |c_0,e(-1)|>=1/R-1000*n*exp(-n/3000)-A_e, which is eventually
vacuous for this family. A_e is an upper bound on the actual error;
its large lower bound does not make the actual error large. The
separate one-node calculation in section 2, not this cost comparison,
establishes the genuine failure of an o(1) inherited-anchor claim.

No mathematical script, numerical experiment or external theorem
beyond the stated ready imports is a premise. The finite-product,
finite-sum and rational comparisons above prove the claimed local
obstructions. A signed angular noncancellation estimate remains an
independent possible route to the paid criterion.

## Mathlib

Full matching coverage for these displaced-node counterexamples and
the quantitative absolute-cost obstruction has not been checked.
The supporting Mahler and localization coverage recorded in L658/L664
remains qualified; no Mahler continuity theorem is applied here.
The finite rational kernel and scalar inequalities are informal proofs,
not Lean formalizations. Unknown coverage is not evidence of absence.
