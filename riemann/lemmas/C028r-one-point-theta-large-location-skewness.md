# Corollary C028r: one-point theta large-location skewness

## Hypotheses

Let mu_0 be the full even theta probability of C028q:

    dmu_0(u)=K(|u|)du/(2*M_0), M_0=integral_0^infinity K(u)du,

where K is L019's positive kernel. Let p_n be its monic orthogonal
polynomials and h_n=integral_R p_n(u)^2 dmu_0(u)>0, with p_0=1
and h_0=1. For each real L>=0 let q_d(x;L) be the degree-d monic
orthogonal polynomial for nu_L=(mu_0+delta_L)/2. Fix one integer
d>=3. Write its d real zeros as z_i(L), and define

    m_d(L)=sum_i z_i(L)/d,
    M_r(d,L)=sum_i (z_i(L)-m_d(L))^r/d, r=2,3,
    g_d(L)=M_3(d,L)/M_2(d,L)^(3/2),
    B_d=(d-2)/sqrt(d-1).

These are equally weighted zero moments, not nu_L moments or weighted
Gauss quadrature moments. For the actual coefficient comparison use
Q_d, S_2,S_3>0 and gamma_d=-B_d*S_3/S_2^(3/2) from C028q(3)-(4).
No reality assumption on the actual Q_d zeros, RH, recurrence
asymptotic or uniform-in-d limit is imposed.

For the separate application after audit1919, additionally assume the
L917/L037 contracts retained in C028s's accepted certificate1917.
The theorem (1)-(2) and implication from (3) do not need those contracts.

## Conclusion

The function g_d is continuous on [0,infinity), g_d(0)=0, and

    lim_(L->infinity) g_d(L)=B_d.                         (1)

More precisely, as L tends to positive infinity at this fixed degree,

    M_2(d,L)=((d-1)/d^2)*L^2+O_d(1),
    M_3(d,L)=((d-1)*(d-2)/d^3)*L^3+O_d(L),
    g_d(L)=B_d+O_d(L^-2).                               (2)

Consequently the additional condition

    0<S_3<S_2^(3/2)                                    (3)

suffices, for every fixed d>=3, for a finite L>0 and a nonzero real
affine scale sigma such that the transformed q_d matches Q_d's mean,
quadratic coefficient and cubic coefficient. This is conditional on (3);
the application below supplies it under extra arithmetic contracts.
The same condition is sufficient for each
d, but no uniform bound on the selected locations or scales follows.

If S_3/S_2^(3/2)>=1, this limit and continuity argument alone give no
finite matching location. For a ratio greater than1 the absolute
skewness in the sufficiently large-L tail is below |gamma_d|; this
says nothing about an intermediate finite location. Equality at the
limit is not finite attainment. No converse, sharp universal skewness
bound, lower-coefficient estimate, full Schmeisser payment or H_d=o(d)
is asserted.

## Proof

### Imported formula, mixed-measure zeros and applicability

A. M. Delgado, L. Fernandez, T. E. Perez and M. A. Pinar,
*Multivariate Orthogonal Polynomials and Modified Moment Functionals*,
SIGMA12(2016),090, DOI10.3842/SIGMA.2016.090,
[arXiv:1601.07194v2, Section2 p7 and Section3 pp8-10,
Theorem3.1, (3.1)-(3.14)](https://arxiv.org/pdf/1601.07194v2),
gives the arbitrary-site Uvarov modification formula. In one variable,
with one added mass equal to1, it specializes to

    q_d(x;L)=p_d(x)-A_L*sum_(j=0)^(d-1) p_j(L)*p_j(x)/h_j,
    A_L=p_d(L)/(1+K_(d-1)(L,L)),
    K_(d-1)(L,L)=sum_(j=0)^(d-1) p_j(L)^2/h_j.          (4)

The complete relevant source proof and arbitrary-site hypotheses were
inspected in source-notes1908. This formula is imported, not reproved.
The subsequent coefficient limit is the specialization needed here;
the source's formula does not itself state (1).

L019/L021 give all absolute moments, positive density on every interval
and finite positive M_0. Thus all finite polynomial Gram matrices of
mu_0 are positive definite: a nonzero polynomial has positive squared
integral. Adding delta_L preserves this property, and the denominator
in (4) is at least1. Scalar multiplication by1/2 does not change monic
orthogonal polynomials, so (4) applies to nu_L as stated. No division
by p_d(L) is made. The support has convex hull R; L is not asserted
to be exterior to it, and no fixed-site/increasing-mass theorem is used.

[NIST DLMF18.2(i), (18.2.4_5)](https://dlmf.nist.gov/18.2#i)
allows a mixed measure with infinite support and finite moments;
[18.2(vi), opening zero theorem](https://dlmf.nist.gov/18.2#vi)
gives simple real zeros of its orthogonal polynomials. Apply this to
nu_L. In particular its d zeros are distinct, so M_2(d,L)>0. These
facts concern the reference only.

### Exact coefficients and fixed-degree orders

Evenness and uniqueness of the monic orthogonal polynomials imply
p_n(-x)=(-1)^n*p_n(x): the monic polynomial (-1)^n*p_n(-x)
has the same orthogonality conditions. For n>=2 put
kappa_n=[x^(n-2)]p_n(x), and put kappa_0=kappa_1=0.
Thus p_n(L)=L^n+O_d(L^(n-2)) for n>=2, while p_1(L)=L and
p_0(L)=1 exactly. With d fixed, (4) gives

    1+K_(d-1)(L,L)=L^(2d-2)/h_(d-1)*(1+O_d(L^-2)),
    A_L=h_(d-1)*L^(2-d)*(1+O_d(L^-2)).                (5)

Indeed the j=d-1 summand supplies the leading power and every other
summand has degree at most2d-4; the added1 also has that bound for
d>=3. All orders are as L tends to positive infinity, so no assertion
about division by L at zero is involved.

Write q_d=x^d+c_1(L)x^(d-1)+c_2(L)x^(d-2)+c_3(L)x^(d-3)+... .
Parity and (4) give exactly

    c_1=-A_L*p_(d-1)(L)/h_(d-1),
    c_2=kappa_d-A_L*p_(d-2)(L)/h_(d-2),
    c_3=-A_L*(kappa_(d-1)*p_(d-1)(L)/h_(d-1)
                                      +p_(d-3)(L)/h_(d-3)).

The d=3 last term uses p_0=1 and h_0=1, so no negative index is
present. There is no contribution from p_d to c_3 or from p_(d-2)
to c_3 because of parity. Equation (5) yields

    c_1=-L+O_d(L^-1),
    c_2=kappa_d-h_(d-1)/h_(d-2)+O_d(L^-2),
    c_3=-kappa_(d-1)*L+O_d(L^-1).                    (6)

As a consistency description, L^(-d)*q_d(L*x;L) tends coefficientwise
to x^d-x^(d-1). Directly in (4), p_d(L*x)/L^d tends to x^d,
the j=d-1 correction tends to x^(d-1), and every lower correction
has coefficients O_d(L^-2) or smaller. No assertion about tracking
individual zeros is required for the moment calculation.

### Newton centering and endpoint continuity

For the uncentered zero sums r_k=sum_i z_i^k, Newton's identities give

    r_1=-c_1=L+O_d(L^-1),
    r_2=c_1^2-2*c_2=L^2+O_d(1),
    r_3=-c_1^3+3*c_1*c_2-3*c_3=L^3+O_d(L).

The centered empirical moments are exactly

    M_2=r_2/d-r_1^2/d^2,
    M_3=r_3/d-3*r_1*r_2/d^2+2*r_1^3/d^3.

The leading constants are (d-1)/d^2 and
1/d-3/d^2+2/d^3=(d-1)*(d-2)/d^3, proving the first two estimates
in (2). Dividing by M_2^(3/2), whose leading constant is positive,
proves the last estimate and (1). These are finite polynomial
identities and fixed-degree asymptotics, without a sum-limit interchange.

The coefficients in (4) are continuous for all L>=0 because the
denominator is positive. Newton's identities show continuity of the
centered moments without choosing continuous zero labels. Their
variance is everywhere positive by the zero theorem, hence g_d is
continuous. At L=0 the modified measure is even, so q_d has parity d.
Its zero multiset is symmetric about zero, giving m_d(0)=M_3(d,0)=0
and therefore g_d(0)=0.

### Conditional cubic matching and the unproved actual input

Put R=S_3/S_2^(3/2)>0. If (3) holds, then 0<B_d*R<B_d. By (1)
there is a finite L_1>0 such that g_d(L_1)>B_d*R. Continuity on
[0,L_1] and g_d(0)=0 give a finite L in (0,L_1) with

    g_d(L)=B_d*R=|gamma_d|.

The affine-moment argument of C028q(3)-(4) applies to any real reference
zero multiset with positive variance, so choose

    sigma=-sqrt((d-1)*S_2/M_2(d,L)), a=-sigma*m_d(L).

Then sigma^d*q_d((x-a)/sigma;L) is monic, centered, and has second
empirical moment (d-1)*S_2. Its third standardized moment is
-g_d(L)=gamma_d. Newton's identities give equality of the first three
subleading coefficients with Q_d, including d=3. For d=3 these exhaust
the coefficients; for higher degrees they do not. This conditional
observation supplies no proof of (3), no conclusion uniform in d and
no bound for the remaining coefficient residuals.

If R>1, convergence |g_d(L)|->B_d<B_d*R implies the stated strict
inequality in a sufficiently large-L tail. If R=1, convergence itself
does not imply any finite equality. Neither case rules out intermediate
finite-L matching. In particular positivity of S_2 and S_3 from the
existing inputs is not the missing ratio bound, and real zeros of q_d
do not prove any inequality for Q_d's formal zero moments.

### Conceptual audit1913 — 20 November 2026

The fixed-degree statement and its conditional finite matching argument
pass the combined audit under assessment1911. The cited arbitrary-site
formula applies separately at every L: both moment functionals are
positive definite, and probability normalization changes no monic
polynomial. The mixed-measure zero theorem applies on R, giving strict
variance without any assertion about actual Q_d roots.

The only terms contributing to c_1,c_2,c_3 are those displayed above.
At d=3 the last kernel term is p_0/h_0=1; its contribution to c_3 is
O(L^-1), so it cannot alter the leading centered cubic. In (5), the
leading denominator degree is 2d-2, while all remaining terms have
degree at most 2d-4. Thus the errors in (6), and consequently the
O(1), O(L), O(L^-2) errors in (2), hold at each fixed d. No estimate
with a d-independent constant was used.

Independently replaying Newton's identities gives M_2's leading factor
(d-1)/d^2 and M_3's leading factor (d-1)(d-2)/d^3. Continuity follows
from coefficients and positive variance, without labeling zeros. With
R in (0,1), convergence supplies a finite L_1 with g_d(L_1)>B_d*R;
IVT then gives equality at a strictly positive finite L. Negative sigma
has the required cubic sign, and sigma^d makes the transformed
polynomial monic also for odd d. Its mean is zero and its formal
second and third sums equal C028q(3), so all three subleading
coefficients match. For d=3 this would match the entire polynomial.

The combined unconditional conclusion does NOT pass: C028s's audit1913
finds a gap in the source-proof step used to exclude R=1. Its scaling
and finite coefficient algebra pass, but the asserted strict input is
not certified. This does not contradict (1)-(2) or the conditional
matching theorem. The condition (3) remains unpaid in this route;
neither finite attainment at R=1 nor a contrary actual inequality is
inferred. Lower residuals, full cost and uniform parameter control
remain independent gaps even if the strict input is later supplied.

### Application of the accepted scalar certificate — audit1919

Audit1913 above records the failed analytic strictness import; that
source defect remains. C028s's separate saved-moment certificate1917
now passes independent audit1919 under L917/L037's contracts, including
assumed Decimal-library correctness. It gives H>0 and hence (3), by
H/gamma_0^4=4*(S_2^3-S_3^2), gamma_0>0 and L027's S_2,S_3>0.

Consequently, for every fixed integer d>=3 the finite positive L and
nonzero real sigma asserted here exist under those same contracts.
This is exactly the proved IVT application with 0<B_d*R<B_d and the
negative affine scale; reference variance stays positive. It asserts
neither actual Q_d root reality for d>3 nor uniform parameter control,
lower-residual bounds, full Schmeisser payment or H_d=o(d). For d=3
the three matched coefficients exhaust the polynomial, as already
qualified in the original theorem.

## Mathlib

Full matching theorem not checked; availability is unknown. The imported
Uvarov formula and mixed-measure zero theorem are precisely cited above.
The coefficient specialization, empirical centering and conditional
intermediate-value application are proved here. No Mathlib absence claim
or formal verification is made. See the
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
