# Lemma 675: exact polynomial actions and a low-degree angular cost obstruction

## Hypotheses

Keep L666's complete rational product and normalized angular measure. Put

    q>=1 integer, n=12q+3, J=n-1, tau=J/n,
    x=-d=-5/4, R=11/8, U=R^2, t_j=j/n,
    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a), |u|=1,
    A(a)=mean_u conjugate(psi(u))*W_a(u), psi in L2(T).

Interpret W by its rational formula at removable singularities of the
quotient. The parameter domain is |a|>tau. Set

    s_j=t_j/R (1<=j<=J), lambda=R/x=-11/10,
    b(v)=product_(1<=j<=J) (v-s_j)/(1-s_j*v)
        =sum_(k>=0) beta_k*v^k,
    F(u)=b(lambda*u).

The coefficients beta_k are real. Their nonvanishing is not assumed.
Let P(w)=sum_(l=1)^m p_l*w^l be a real polynomial, 1<=m<=n;
degree smaller than m is allowed. For the cost conclusion assume P(1)=1
and the exact identity A(a)=P(x/a) throughout |a|>tau. All norms use
normalized circle measure. No sign condition, displacement vector,
original-residue sum, or Xi realization is assumed for the degree bound.

## Conclusion

The exact finite-polynomial range criterion is

    P(x/a) is such an L2 action
      iff p_(k+1)=0 whenever beta_k=0, 0<=k<m.        (1)

For nonzero beta_k put

    c_k=p_(k+1)/(beta_k*lambda^k),

and put c_k=0 when beta_k=0 (in the feasible case). An explicit full
preimage is

    conjugate(psi_P(u))=F(u)*sum_(0<=k<m) c_k*u^(-k). (2)

Every preimage, including those using additional Fourier modes, obeys

    ||psi||_2 >= (23/22)^J * (sum_(k<m)|c_k|^2)^(1/2),
    ||psi_P||_2 <= (41/22)^J * (sum_(k<m)|c_k|^2)^(1/2). (3)

Thus (2) is an exact inverse, not a claim of optimal norm. The exponential
gap between the two bounds is retained. For any normalized polynomial
action of degree at most m,

    ||psi||_2 >= (6/5)*(299/209)^(n-1)/((11/5)^m-1).  (4)

In particular, if m<=3*n/7, then

    ||psi||_2 > (1254/1495)*exp((1503/97790)*n),
    1503/97790 > 1/100.                              (5)

No absolute C and onset can make the required exp(n/100)*n^C norm bound
hold for a family of such low-degree normalized actions.

The specific cubic

    P_*(w)=w*(11*w-10)*(3-2*w)=-30*w+53*w^2-22*w^3    (6)

has P_*(0)=0, P_*(1)=1, P_*(10/11)=0 and strictly positive real part
at w=x/(x+i*y) for every |y|<=9/20. Its first three required beta_k
are nonzero for every allowed n, so (2) supplies an exact preimage.
Nevertheless every preimage of this cubic satisfies the stronger bound

    ||psi||_2 >= 30*(23/22)^J*(n*R)^J/J!
               >= 30*(23/8)^J.                      (7)

This establishes feasibility of the polynomial/sign/range requirements
and excludes low-degree solutions to the norm requirement. It does not
decide the saved degree-at-most-n target: degrees greater than 3*n/7,
possible coefficient zeros there, and their full inverse costs remain
open. It is not an obstruction to all segment-positive actions or to
the cone itself. Original unit-residue H, support, Xi realization and
all-degree mixed positivity remain unresolved. The portions of Sections
2--3 used by L677 (full factorization, moment identity, arbitrary-preimage
Bessel bound and pointwise lower bound on F) were independently audited
in L677 Section 7 on 2 November 2026. The later low-degree and cubic
conclusions here retain their separate unaudited qualification; no
certified originality is claimed.

## Proof

### 1. Approved scope and standard input

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-inverse-parameter-polynomial-separator.md`.
The work is within its exact finite-polynomial action target, using the
complete product and elementary rational/Fourier coefficient analysis.

Import normalized scalar Fourier orthogonality and Parseval from
A. Levitt, *Analyse de Fourier et applications*,
[author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
version retrieved 2 November 2026, Theorem 1.3/Exercise 1.2 and
Theorem 1.11/Corollary 1.12, printed pp.6,8 (PDF pp.12,14), with the
completeness proof on printed p.53, as inspected in the reused assessment.
Dividing angular Lebesgue measure by 2*pi makes each exponential have
norm one. The Fourier coefficient bound below is a direct application
of this normalization to a uniformly convergent rational Taylor series.
No general Fourier theorem or range-factorization theorem is reproved.

The inspected Yang--Xie closed-arc theorem is not needed: the cubic's
real part will be an explicit rational function with a positive numerator
on the entire interval. This direct check is necessary for these precise
coefficients and endpoints, rather than a reproof of the general sign
characterization. C645o/C645p, L668, L673 and L674 are comparisons only.
In particular no positivity on L674's open parameter disk is assumed,
and no angular pole is discarded. The product-specific range and cost
estimates below are the uncovered specialization being tested.

### 2. Exact factorization and coefficient conditions

L666 Section 2 retains the j=0 factor and gives

    W_a(u)=(x/a)*product_(1<=j<=J)
       [(x-t_j*u)/(a-t_j*u)]*[(U*u-t_j*a)/(U*u-t_j*x)]. (8)

For each j,

    (R*u/a-s_j)/(1-s_j*R*u/a)
          =(U*u-t_j*a)/(R*(a-t_j*u)).

Taking the ratio of this identity at a and x proves

    W_a(u)=(x/a)*b(R*u/a)/b(R*u/x).                  (9)

The nearest possible pole of b has modulus R/tau>11/10, while all
its zeros have modulus s_j<8/11. Consequently F on |u|=1 is continuous,
bounded and bounded away from zero. In particular

    f(u)=conjugate(psi(u))/F(u)

belongs to L2. Write w=x/a. On every compact subdisk of |w|<d/tau,
the series b(lambda*u*w) converges uniformly in u. Cauchy--Schwarz
gives f in L1, so termwise integration is justified there. Equation (9)
therefore gives the full analytic action

    A(x/w)=w*sum_(k>=0) beta_k*lambda^k*w^k*m_k,
    m_k=mean_u f(u)*u^k.                             (10)

The right side extends to w=0 with value zero. Uniqueness of Taylor
coefficients proves the necessary condition in (1), without division
by a possibly zero beta_k. For a polynomial of degree at most m it
also requires beta_k*m_k=0 for all k>=m.

Conversely, if the condition in (1) holds, take
f_P(u)=sum_(k<m)c_k*u^(-k). Orthogonality makes its moments m_k=c_k
for k<m and zero for k>=m. Substitution in (10) proves (2) and the
action identity on the entire disk |w|<d/tau, equivalently on every
finite |a|>tau. This is not interpolation at a finite set of parameters.

For an arbitrary preimage, moments for nonzero beta_k are prescribed;
those for zero beta_k, and other Fourier modes, may be free. Parseval
still gives ||f||_2^2>=sum_(k<m)|c_k|^2. These free modes therefore
cannot invalidate the lower estimate obtained from a pointwise lower
bound on |F|. No minimum-norm identification is assumed.

### 3. Bounds using every grid point

Let s=11/10. For 0<h<1/s and |z|=s, the factor (z-h)/(1-h*z)
has minimum modulus (s+h)/(1+s*h), attained at z=-s, and maximum
modulus (s-h)/(1-s*h), attained at z=s. Indeed its squared modulus is

    (s^2+h^2-2*s*h*c)/(1+s^2*h^2-2*s*h*c), c=cos(arg z).

Its derivative with respect to c is positive because the numerator
minus denominator is (s^2-1)*(1-h^2)>0. Denominators stay positive.

The function g(h)=log((s+h)/(1+s*h)) is convex on this interval:

    g''(h)=-1/(s+h)^2+s^2/(1+s*h)^2>0,

where positivity follows from s*(s+h)>1+s*h. The exact grid average is

    (1/J)*sum_(j=1)^J s_j=1/(2*R)=4/11.

Applying the elementary finite convexity inequality to these J values
gives

    |F(u)| >= product_j (s+s_j)/(1+s*s_j)
            >= ((s+4/11)/(1+4*s/11))^J=(23/22)^J.    (11)

The maximum factor (s-h)/(1-s*h) increases with h, since its derivative
is (s^2-1)/(1-s*h)^2. As s_j<8/11,

    |F(u)| <= ((s-8/11)/(1-8*s/11))^J=(41/22)^J.     (12)

Combining (11)--(12) with the Parseval statements in Section 2 proves
(3), for all possible preimages in the lower bound.

For |v|=rho=1/2, the same squared-modulus calculation has the opposite
derivative sign, since rho<1. A factor of b has maximum modulus
(rho+h)/(1+rho*h), at v=-rho. The function

    h -> log((rho+h)/(1+rho*h))

is concave, because its second derivative is
-1/(rho+h)^2+rho^2/(1+rho*h)^2<0. Using the same exact grid average,

    max_(|v|=1/2)|b(v)|
       <= ((1/2+4/11)/(1+2/11))^J=(19/26)^J.        (13)

The Taylor series converges uniformly on this circle, which contains
no pole. Its kth Fourier coefficient is beta_k/2^k. Orthogonality
and the integral triangle inequality in normalized measure give

    |beta_k| <= (19/26)^J*2^k, k>=0.                 (14)

This bound permits zero coefficients. It neither omits high modes nor
uses an exponential surrogate for the finite product.

### 4. The complete lower cost for low degree

Every preimage has |m_k|<=||f||_2<=||psi||_2*(22/23)^J, by
Cauchy--Schwarz and (11). Since P(1)=1, (10) and (14) imply

    1 <= sum_(k<m) |beta_k|*(11/10)^k*|m_k|
      <= ||psi||_2*(209/299)^J*sum_(k<m)(11/5)^k.

Here (22/23)*(19/26)=209/299. The geometric sum proves (4), including
degree drops and any zero beta_k. If m<=3*n/7, dropping the negative
one in its positive denominator gives the strict bound

    ||psi||_2 > (1254/1495)*exp(gamma*n),
    gamma=log(299/209)-(3/7)*log(11/5).               (15)

The following elementary logarithm estimates give a rational margin.
For 0<z<1, integrate the geometric series for 1/(1-z^2) to obtain

    log((1+z)/(1-z))=2*sum_(r>=0) z^(2*r+1)/(2*r+1).

All terms are positive and the geometric majorant converges. Keeping
the first term, with z=45/254, gives log(299/209)>=45/127. Bounding
all denominators after the first by 3, with z=3/8, gives

    log(11/5) <= 2*(3/8+(3/8)^3/(3*(1-(3/8)^2)))
               =87/110.

Thus

    gamma >= 45/127-(3/7)*(87/110)=1503/97790,
    gamma-1/100 >= 5251/977900 >0.                  (16)

Equations (15)--(16) prove (5). For every fixed real C,

    log(||psi||_2/(exp(n/100)*n^C))
      > log(1254/1495)+(5251/977900)*n-C*log n
      -> infinity along n=12q+3.

This is a uniform cost obstruction for m<=3*n/7. It does not exclude
any higher degree by itself; in particular it is not a negative answer
to the full degree-at-most-n question.

### 5. A feasible cubic with an exact, expensive inverse

The values in (6) follow by substitution. For a=x+i*y put
t=4*y/5, so |t|<=9/25 and x/a=1/(1-i*t). Direct expansion gives

    Re P_*(1/(1-i*t))
       =(1+6*t^2-83*t^4)/(1+t^2)^3.                 (17)

The polynomial h(v)=1+6*v-83*v^2 is concave. On
0<=v<=81/625 it is at least the minimum of its endpoint values,

    h(0)=1, h(81/625)=149812/390625>0.

This proves the signs on the entire closed ordinate segment, including
both endpoints. It assumes no positivity on a two-dimensional domain.

It remains to establish the nonzero coefficients needed for (2).
J=n-1 is even and at least 14, so

    beta_0=product_j s_j=J!/(n*R)^J>0.

Expanding the finite product at zero, or differentiating its logarithm
locally where it has no zero, gives

    V=sum_j (s_j^(-1)-s_j)>0,
    T=sum_j (s_j^(-2)-s_j^2),
    beta_1=-beta_0*V,
    beta_2=(beta_0/2)*(V^2-T).                       (18)

For v_j=s_j^(-1)-s_j, one has v_j>=57/88 and
v_j^2-(s_j^(-2)-s_j^2)=-2*(1-s_j^2). Therefore

    V^2-T=2*sum_(i<j)v_i*v_j-2*sum_j(1-s_j^2)
          >= J*((J-1)*(57/88)^2-2)>0,                (19)

since at J=14 the bracket equals 26749/7744>0 and it increases
with J. This proves beta_0,beta_1,beta_2 are all nonzero. Hence (2)
with

    c_0=-30/beta_0,
    c_1=53/(lambda*beta_1),
    c_2=-22/(lambda^2*beta_2)

is a full exact preimage for the cubic, with finite norm bounded by (3).
These expressions specify every coefficient and retain the fixed F;
they do not identify it with a different Cauchy transform.

For any preimage, its prescribed zeroth moment alone and (11) give

    ||psi||_2 >= (23/22)^J*30/beta_0.

Finally the J numbers 1/n,...,J/n have mean 1/2. Their product is at
most (1/2)^J by the finite arithmetic-geometric mean inequality, so
beta_0<= (1/(2*R))^J=(4/11)^J. This proves (7). In particular
log(23/8)>=15/23>1/100, using log(1+z)>=z/(1+z), so no polynomial
factor repairs this cubic's exponential shortfall.

### 6. Verification and remaining target

Run `python3 scripts/one-sided-hankel/inverse-parameter-polynomial-check.py`.
It saves exact rational arithmetic for the cubic identity, prescribed
values, endpoint margin, first-three-coefficient margin and the cost
constants in `scripts/one-sided-hankel/inverse-parameter-polynomial-check.json`.
These arithmetic checks support the displayed calculations; they do not
replace the convergence, complete-range or norm proofs above, nor a
later independent audit.

Any norm-budget construction must eventually use degrees above
3*n/7 and must control all required beta_k, the weighted angular norm
and all closed-segment signs. Formula (1) settles membership only after
those coefficients are specified. Formula (2)'s upper bound can be too
large, while additional free modes may improve the inverse; neither
possibility is assumed resolved. No original-residue mass estimate or
Xi conclusion follows from the cubic or the low-degree obstruction.

## Mathlib

Full matching coverage for this product-specific action range, explicit
cubic specialization and quantitative degree obstruction has not been
checked. Scalar Fourier/Parseval is imported from the precise source
above; finite product algebra, elementary convexity, arithmetic-geometric
mean and normalized Cauchy--Schwarz supply the remaining steps. No
unverified Mathlib theorem name or absence claim is made.
