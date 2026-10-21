# Lemma 440: a compact-height quadratic occupation test separates L438

## Hypotheses

Use exactly L438's complete conditional law nu_(H,t), height marginal
dt/H on [H,2H], all three rare components and its translated six-state
bulk. Keep any one admissible original L429 cutoff j(H), without adding
tests to its thresholds. Write ell=log H, L(t)=log(2+t), E_H for
H^(-1) integration over [H,2H], and omega=log 2. The ordinary trajectory
coordinates are x=f, y=f'/L, z=f''/L^2, for real f in C^2([H,2H]).
Set

    eta(u)=(u-1)^2(2-u)^2 on [1,2], zero elsewhere,
    e_H(t)=eta(t/H),
    phi_H(t,x)=e_H(t) sin(omega t) x^2/L(t).

The zero extension of eta is C^1. H is fixed during every height
derivative: neither the law, j(H), its calibration coefficients nor its
selected basis is differentiated. All limits below are through real H.

## Conclusion

Define the explicit quadratic transport polynomial

    T_H(t,X)=[e_H'(t) sin(omega t)/L(t)
              +omega e_H(t) cos(omega t)/L(t)
              -e_H(t) sin(omega t)L'(t)/L(t)^2] x^2
                    +2e_H(t) sin(omega t)xy.                 (1)

Every stated C^2 trajectory satisfies E_H T_H(t,X(t))=0 exactly.
For L438's unchanged complete law, however,

    E_nu T_H = log(2)/(30 sqrt(2))+o(1)>0 eventually.          (2)

In particular that law fails this one necessary trajectory identity.
More generally, any trajectory law agreeing with it on this entire
H-dependent polynomial observable to o(1) is excluded. This does not
assert that matching its previously selected moments requires such
agreement. It does not refute L438's selected-moment construction,
exclude another law, or evaluate actual clipping, capped nondegeneracy,
L413's full-error regulator margin, global mixed positivity or RH.
This is a local REPRODUCTION specialization of covered calculus and
finite-product tools. The separate step-259 critical audit below validates
this stated scope; no originality beyond the sources checked is claimed.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-19-prime-two-quadratic-occupation-test.md`.
Its necessary-identity input is J. B. Lasserre, D. Henrion, C. Prieur
and E. Trelat, *Nonlinear optimal control via occupation measures and
LMI-relaxations*, SIAM J. Control Optim. 47 (2008), 1643--1666,
DOI 10.1137/070685051, inspected
[arXiv:math/0703377v1, 2007-03-13](https://arxiv.org/pdf/math/0703377v1),
Sections 2.1--2.3, (2.7), (2.10)--(2.12), pp. 3--5. At each fixed H
the continuous trajectory and the conditional states have finite bounded
boxes, so its C^1 finite-interval necessary identity applies. We use no
optimization, no-gap, sufficiency or uniform-integrability theorem.
The p=2 integrability comparison in Henrion--Korda--Kruzik--Rios-Zertuche,
*Occupation measure relaxations in variational problems: the role of
convexity*, [2023-03-04 manuscript](https://optimization-online.org/wp-content/uploads/2023/03/convexcov-1.pdf),
Definitions 2.4/2.7, (6)--(8), pp. 3--4 and Lemma B.1, pp. 17--18,
is supporting coverage; we do not apply its smooth-test statement to
the merely C^1 cutoff. L424 supplies the ordinary dynamics. The explicit
derivatives and law-specific signed estimates below are the required
specialization, rather than a reproof of either general theorem.

The finite Poisson character formula is imported through L429 from
C. Aistleitner, I. Berkes and K. Seip, *GCD sums from Poisson integrals
and systems of dilated functions*, JEMS 17 (2015), 1517--1546,
DOI 10.4171/JEMS/537, section 3, p. 1527, identity preceding Lemma 1
and (23), [published primary text](https://ems.press/content/serial-article-files/32047?nt=1).
Its radii are p^(-1/2)<1 and each product is finite. A separate direct
estimate below supplies the moving height weight under the existing
cutoff; fixed-test Haar convergence alone would not do so. No new
actual-zeta moment theorem, infinite critical-line Euler product or
independence hypothesis is used.

### Exact derivatives and the full raw second matrix

The partial derivatives, with x held fixed in the first, are

    partial_t phi_H
      =[e_H' sin(omega t)/L+omega e_H cos(omega t)/L
                              -e_H sin(omega t)L'/L^2] x^2,
    partial_x phi_H=2e_H sin(omega t)x/L.

L424 gives x'=Ly. Thus the total derivative is exactly (1).
Both endpoint values of phi_H vanish. The imported identity yields
E_H T_H=0; alternatively these displayed derivatives give its direct
finite-interval specialization by the fundamental theorem of calculus.
The term containing L' and the factor 1/H in e_H' are retained.

In L438 notation put

    R_H(t)=pYY^T+k_+Z_+Z_+^T+k_-Z_-Z_-^T,
    C_H(t)=R_H(t)+w(t)[ell g_H(t)K+A_H+m(t)m(t)^T].    (3)

This is the exact conditional raw second matrix, because the centered
six-state bulk has covariance ell g_H K+A_H. No property of either
selected basis branch is needed beyond that exact covariance.
In particular q_11=(C_H)_11>=0 and q_12=(C_H)_12. L438 proves

    E_H C_H=ell K, K_11=1, K_12=0,
    E_H tr R_H=O(sqrt(ell)), ||A_H||=O(sqrt(ell)),
    m=O(1), E_H(1-w)=O(ell^(-5/2)), E_H(wg_H)=1.     (4)

All constants are uniform in the saved cutoff stages. Equations (3)--(4)
give the absolute, rather than merely signed, comparison

    E_H |q_11-ell wg_H|=O(sqrt(ell)).                (5)

Indeed R_H is positive semidefinite and its 11 entry is at most its
trace; the other error entries are w(A_11+m_1^2). The two slow
coefficients in (1) cost, using E_H q_11=ell,

    |E_H[(e_H' sin/L-e_H sin L'/L^2)q_11]|<=C/H.     (6)

Here ||e_H'||<=C/H, L>=ell and L'<=1/H. Also ell/L=1+O(1/ell)
uniformly on this interval. Thus (5) and the positive measure wg_H dt/H
of mass one yield

    E_nu T_H
      =omega E_H[e_H cos(omega t)wg_H]
         +2E_H[e_H sin(omega t)q_12]
         +O(ell^(-1/2)+H^(-1)).                     (7)

The second term is not discarded by K_12=0. Its complete evaluation is
the signed estimate below.

### The height-weighted Poisson limit with the original cutoff

Let y=p_j, r_p=p^(-1/2), and M_j be L429's finite-product supremum.
The cutoff gives M_j<=ell^(1/8). The geometric expansion gives

    M_j>=product_(p<=y)(1-r_p)^(-1)
       >=sum_(n<=y)n^(-1/2)>=sqrt(y),

since every integer at most y has all prime factors at most y.
Hence y<=ell^(1/4). This implication follows from the old cutoff and
does not add a condition to its thresholds.

The exact absolutely convergent Fourier expansion is

    P_j(t)=sum_(k in Z^j) a_k exp(it sum_(p<=y) k_p log p),
    a_k=product_(p<=y)r_p^|k_p|>=0, sum_k a_k=M_j.    (8)

Take K0=ceil(16 log(ell)/log 2) and truncate to |k_p|<=K0 for
every retained prime. A union bound on the omitted coefficient mass
gives, with an absolute constant,

    ||P_j-P_j,trunc||_infinity
       <=C M_j y 2^(-K0/2)=O(ell^(-61/8)).          (9)

For one coordinate the omitted geometric sum is
2r_p^(K0+1)/(1-r_p); multiply by the complete sums of the other
coordinates and use 1-r_p>=1-2^(-1/2). This proves (9) even though
the number of primes grows.

Put D_j=product_(p<=y)p^K0. Each retained frequency is log(n/m)
with n,m<=D_j. After multiplication by cos(t log 2) both numerator
and denominator are at most 2D_j. If the resulting frequency is
nonzero, its absolute value is at least 1/(2D_j), by integrating
1/v between distinct positive integers. Furthermore

    log D_j<=K0 y log y
           =O(ell^(1/4)(log ell)^2)=o(ell).          (10)

For any nonzero frequency u, integration by parts, including both
endpoints, gives

    |E_H[e_H(t) exp(iut)]|
       <=[2||eta||_infinity+integral_1^2|eta'(v)|dv]/(H|u|).

Summing the retained nonzero frequencies costs at most C D_j M_j/H,
which tends to zero by (10). Once j>=1 and K0>=1 the constant
coefficient of P_j,trunc cos(t log 2) is exactly 1/sqrt(2): its
two contributions are k_2=1 and k_2=-1 with all other exponents
zero, and the cosine halves sum. Unique prime factorization excludes
any other zero frequency. Finally

    integral_1^2 eta(v)dv=integral_0^1 s^2(1-s)^2 ds=1/30.

Together with (9), this proves the complete moving-test limit

    E_H[e_H cos(omega t)P_j]=1/(30 sqrt(2))+o(1).     (11)

L438 keeps N_H=E_H(wP_j)=1+o(1) and g_H=P_j/N_H.
For any U_H with uniformly bounded supremum, the exact estimate is

    |E_H[U_H wg_H]-E_H[U_H P_j]|
      <=||U_H||_infinity
            (|1-N_H|+E_H[(1-w)P_j])=o(1),          (12)

because E_H[(1-w)P_j]=O(ell^(-19/8)). Unlike a fixed-test
convergence assertion, this normalization estimate applies to the
present moving U_H directly. Equations (11)--(12) evaluate the first
term in (7), with every high/intermediate mass loss retained.

### A quantitative zero-angle-mean bound

Use L369's actual phase R=exp(i varphi), with
varphi'=log(t/(2pi))/2+O(t^(-2)) and varphi''=O(1/t).
Put Z=zeta(5/2+it)=rho exp(i chi), choosing the smooth phase from
the absolutely convergent Euler logarithm on this line, and

    alpha=varphi+chi, a=rho cos alpha, h=rho sin alpha,
    c=1/(4pi).

The absolute Dirichlet series for Z,Z',Z'' and the Euler-product
lower bound used in L419 imply

    0<rho_min<=rho<=rho_max, |rho'|<=C,
    |chi'|+|chi''|<=C,
    alpha'=ell/2+O(1), |alpha''|<=C                 (13)

on [H,2H]. The derivative series converge because
sum_(n>=1)n^(-5/2)(log n)^d<infinity for d<=2; division by Z is
safe by its positive uniform lower bound. No critical-line division
is used. In particular alpha is increasing eventually.

For any bounded Lebesgue-measurable periodic real function g of zero circle mean, let G
be its bounded periodic Lipschitz primitive. If an absolutely continuous
amplitude A obeys ||A||_infinity+||A'||_infinity<=C_A uniformly,
integration by parts in the absolutely continuous sense gives

    E_H[A(t)g(alpha(t))]
      =[A G(alpha)/alpha']_H^(2H)/H
           -E_H[(A'/alpha'-A alpha''/(alpha')^2)G(alpha)]
      =O(C_A/ell).                                  (14)

The identity holds almost everywhere, including for the piecewise
angular functions below. It uses both derivative bounds in (13), not
only the speed of the phase. A bounded indicator can also be treated
by subtracting its circle mean and using its Lipschitz primitive.
In particular for fixed C0,

    E_H 1_{|sin(2alpha)|<=C0/ell}=O(1/ell).         (15)

Its circle mean is O(1/ell), and the mean-zero primitive is uniformly
bounded, so the same integration by parts, with A=1, proves (15).
This estimate includes every tie neighborhood rather than assuming
generic branch selection.

### Both signed intermediate cross entries

The rational density W_3 in L435 (3)--(4) is smooth on its three
circles: the listed poles have radii 1,p,p^(-2),p^3, none sqrt(p).
Its derivatives on this compact torus are bounded. L438's correction
F_H=beta W_3+a_H^T(1,cos(theta_2),P) has bounded a_H and P is
one fixed trigonometric polynomial. Consequently

    ||F_H||_infinity+||gradient F_H||_infinity<=C.    (16)

Here derivatives concern the torus coordinates only. Along
theta(t)=(t log 2,t log 3,t log 5), both (F_H(theta(t)))_+ and
(F_H(theta(t)))_- are uniformly Lipschitz, with a.e. derivative
bounded independently of H. Differentiation in H is unnecessary.

Write F_+,F_- for these two functions along theta(t). The two
intermediate raw cross entries in L438 are exactly

    k_s (Z_s)_1(Z_s)_2
        =sqrt(ell) F_s(t) (n_s)_1(n_s)_2/h_s(t), s=+,-. (17)

For the negative direction, L437 defines
U=(a+h,(a-h)/2,-(a+h)/4), n_-=U/|U|. Define the positive
periodic function v by

    v(alpha)^2=(21+13 sin(2alpha))/16, |U|=rho v(alpha).

At the leading response, with the exact leading quadratic forms,

    B_0(n_-)=c rho/(2v), D_0(n_-)=-c^2 rho^2/(4v^2),
    h_-,0=c^3 rho^3/(8v^3),
    (n_-)_1(n_-)_2=cos(2alpha)/(2v^2).

L419/L437 give uniform O(1/L) coefficient errors in B and D;
their leading denominators are uniformly positive. Thus

    (n_-)_1(n_-)_2/h_-
      =rho^(-3) g_-(alpha)+O(1/ell),
    g_-(alpha)=4v(alpha)cos(2alpha)/c^3.             (18)

This angular function has zero circle mean: it is a constant multiple
of the derivative of (21+13 sin(2alpha))^(3/2). This conclusion does
not replace the negative direction by a projection sign choice.

For the positive direction keep L421's exact rule: choose between
N_sigma=(2/3,sigma/3,2/3), sigma=+1,-1, by larger absolute exact
B, use its specified tie rule, then reverse the whole vector if needed
to make B>0. The reversal leaves its raw cross entry unchanged.
At leading response B_0(N_sigma)=c(-a/2-sigma h/3). Away from
ah=0 the leading selected sign is sigma=sign(ah). Put

    A(alpha)=|cos alpha|/2+|sin alpha|/3 >=1/3.

For that leading selected direction, B after reversal is c rho A,
its ell_F at zero curvature is -1/3, C_0=c^2 rho^2/4, and hence

    h_+,0=c^3 rho^3 A(A^2+1/3),
    g_+(alpha)=2 sign(cos alpha sin alpha)
                         /[9c^3 A(alpha)(A(alpha)^2+1/3)].

Assign arbitrary bounded values at the finitely many axes. The
function g_+ is bounded, piecewise smooth and odd under alpha -> -alpha,
so its circle mean is zero. Exact selection disagrees with the leading
one only if |sin(2alpha)|<=C0/ell: indeed the leading difference of
squared projections is (2/3)c^2 a h, bounded away from zero off this
neighborhood, whereas both exact squared projections have O(1/ell)
errors. L421 gives an exact uniform lower bound for h_+. Thus

    |(n_+)_1(n_+)_2/h_+-rho^(-3)g_+(alpha)|
       <=C/ell+C 1_{|sin(2alpha)|<=C0/ell}.         (19)

This controls the complete tie rule in L1 by (15). For the two
main terms use (14) with amplitudes
e_H(t)sin(omega t)F_s(t)rho(t)^(-3). Their suprema and a.e.
derivatives are bounded by (13), (16), and the fixed prime frequencies.
Equations (15), (18)--(19) then yield, for each of the two signs,

    E_H[e_H sin(omega t)F_s (n_s)_1(n_s)_2/h_s]
         =O(1/ell).

Multiplication by sqrt(ell) in (17) proves that the complete
intermediate signed cross contribution is O(ell^(-1/2)).
This is a signed estimate specific to these directions. Their absolute
second budget is O(sqrt(ell)) and has not been called negligible.

### High, translation and full covariance cross entries

The high component satisfies
E_H|pY_1Y_2|<=E_H[p|Y|^2]/2=O(ell^(-2)), by L438 (9).
It requires no angular averaging or hypothesis on its actual jets.

The bulk covariance cross entry is w A_12 because K_12=0.
The entire A_H, including its rare second correction, is constant in t.
Integration by parts at the fixed nonzero frequency omega gives
E_H[e_H sin(omega t)]=O(1/H). By (4),

    |E_H[e_H sin(omega t)w A_12]|
      <=C sqrt(ell)[H^(-1)+E_H(1-w)]
      =O(sqrt(ell)/H+ell^(-2)).                    (20)

No conditional covariance cancellation has been inferred from the
integrated second identity.

Finally m=d_H b/|b|^2 with bounded d_H fixed during integration.
Let D0(alpha)=(17/16)cos(alpha)^2+sin(alpha)^2. From
b=c rho(cos(alpha)/4,-sin(alpha),-cos(alpha))+O(1/ell) and
its uniform norm lower bound,

    m_1m_2=d_H^2 rho^(-2) g_m(alpha)+O(1/ell),
    g_m(alpha)=-cos(alpha)sin(alpha)/(4c^2 D0(alpha)^2).

The function g_m is smooth, bounded and odd under alpha -> -alpha.
Its mean is zero. Apply (14) to
A=e_H sin(omega t)d_H^2 rho^(-2), whose derivative is uniformly
bounded. Multiplication by w changes this bounded mean product by at
most C E_H(1-w). Hence

    E_H[e_H sin(omega t)w m_1m_2]=O(1/ell).          (21)

Together (17)--(21) and the high bound retain every term of (3) and
establish

    E_H[e_H sin(omega t)q_12]=O(ell^(-1/2)).        (22)

### Residual and scope

Insert (11)--(12) and (22) into (7). The full remainder is o(1):
it consists of O(ell^(-1/2)+sqrt(ell)/H), the vanishing normalization
error bounded in (12), the Fourier tail (9), and C D_j M_j/H from
(10). All constants precede H and its cutoff stage. The required
comparison scale is one, and its retained coefficient is the strictly
positive log(2)/(30 sqrt(2)). Thus (2) follows, with an existential
common onset. No effective rate for N_H-1, no new threshold, and no
actual fixed-prime sine moment is required.

This evaluates a necessary finite-H identity, not an assertion of
weak-limit realization. The full law may obey every moment condition
listed in L438 while failing this added test. Its selected-information
obstruction and the narrower historical stops remain valid. No proof
of an RH-equivalent positivity condition is asserted.

### Separate critical audit — 2026-10-20, step 259

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-19-prime-two-quadratic-occupation-audit.md`.
This RESEARCH / REPRODUCTION audit validates (2) for precisely the
unchanged complete law and original cutoff. The only textual
qualification is measurability of g in (14); every angular function
used here is Borel. No coefficient, observable, law, threshold or
claimed remainder is changed. The inspected general theorems are
imported with their hypotheses; the checks below concern their local
specialization, not a new general averaging theorem.

**Exact identity and raw moments.** The zero extension of eta and its
first derivative vanish at both endpoints. For fixed H, phi_H is C^1,
x'=Ly, and its total derivative is exactly (1), with the factor 2
in the cross term and both explicit slow derivatives. Endpoint
subtraction therefore gives zero, without any distributional boundary
term. A trajectory in C^2 has bounded state and control on this compact
interval, as required by the cited finite-interval occupation identity.
No uniform compact box as H grows is used.

L438 (9)--(18) gives precisely R_H and C_H in (3): the centered bulk
has mean zero and covariance Sigma, hence its translated raw matrix
is Sigma+mm^T. Its integrated identity is ell K, with K_11=1 and
K_12=0 from L419. Positivity of R_H gives
E_H(R_H)_11<=E_H tr R_H=O(sqrt(ell)). The remaining x-square
error is bounded by ||A_H||+sup|m|^2=O(sqrt(ell)), proving (5)
in absolute value. The slow terms cost C ell/(H ell) and
C ell/(H ell^2), respectively. Also L(t)-ell is uniformly bounded.
Since wg_H dt/H is positive of mass one, replacing ell/L by one
costs O(1/ell). This checks (7) without substituting an integrated
cross equality for its conditional value.

**Moving finite Fourier series.** For every original stage, the
nonnegative series for product (1-r_p)^(-1) includes all integers
n<=y, and their sum n^(-1/2) is at least sqrt(y). It is bounded
above by M_j. Thus y<=ell^(1/4) follows from the existing condition
M_j<=ell^(1/8), regardless of how slowly the stages increase.
For one omitted coordinate, division of its omitted coefficient sum
by its full sum gives 2r_p^(K0+1)/(1+r_p). Summing these ratios
over at most y coordinates bounds the entire omitted mass by
2M_j y 2^(-K0/2). The exponent is 1/8+1/4-8=-61/8,
as in (9); the estimate includes simultaneous omissions.

Every retained numerator and denominator is an integer at most D_j.
The prime-2 cosine changes these bounds to 2D_j; cancellation can
only reduce them. If n!=m, integrating 1/v between the two integers
gives |log(n/m)|>=1/max(n,m)>=1/(2D_j). The sum of absolute
coefficients after multiplying by cosine is at most M_j. Integration
by parts with e_H therefore bounds the complete nonzero-frequency
contribution by C D_j M_j/H, independently of collisions. Meanwhile
log D_j<=K0 y log y=O(ell^(1/4)(log ell)^2)=o(ell), so this
bound tends to zero on every stage. Only the two prime-2 exponents
of size one give zero frequency, with total coefficient 1/sqrt(2).
Their eta integral is exactly 1/30. This proves (11) with the full
tail, not just a finite preview or a fixed-test convergence argument.

For U=e_H cos(omega t), the normalization identity is exactly

    E_H(Uwg_H)-E_H(UP_j)
      =(N_H^(-1)-1)E_H(UwP_j)-E_H(U(1-w)P_j).

The first integral in absolute value is at most ||U||_infinity N_H.
The second costs at most C M_j E_H(1-w)=O(ell^(-19/8)).
Thus qualitative N_H->1 suffices at scale one. The finite-Fourier
comparison has not added tests to the original threshold list.

**Absolutely continuous angular averaging, including ties.** The
right-line series through Z'' converge absolutely and uniformly and
|Z| has a fixed positive lower bound. In particular
rho'=Re(Z' conjugate(Z))/rho,
chi'=Im(Z'/Z), and chi''=Im(Z''/Z-(Z'/Z)^2) are uniformly bounded.
L369 (6) supplies the separate phase and curvature bounds, so (13)
holds with alpha'>=ell/4 eventually and bounded alpha''. For each
fixed H the phase map and its inverse are Lipschitz on their compact
intervals. Its inverse therefore pulls back null sets to null sets.

Import the fundamental theorem for absolutely continuous functions
from T. Tao, *An Introduction to Measure Theory*, GSM 126 (AMS,
2011), Theorem 1.6.40, printed pp. 172--174 in the inspected
[author preliminary text](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-126-tao5-measure-book.pdf).
The supporting Lipschitz and product/integration-by-parts statements
are Exercises 1.6.44--45 and 1.6.48(iii),(vi)--(vii), pp. 168--172;
these exercises are stated with hints, rather than claimed as separate
printed proofs. Their relevant specialization is explicit: for bounded
measurable mean-zero g, G(u)=integral_0^u g(v)dv is periodic,
Lipschitz and has G'=g almost everywhere. The null-set property above
gives (G composed with alpha)'=g(alpha)alpha' almost everywhere.
For absolutely continuous A with bounded value and a.e. derivative,
A/alpha' is absolutely continuous, with derivative
A'/alpha'-A alpha''/(alpha')^2. Apply the endpoint fundamental
theorem to its product with G(alpha). This is exactly (14), with
bound C||G||_infinity[C_A/(H ell)+C_A/ell+C_A/ell^2].
No angular jump is differentiated.

For the indicator in (15), its circle support is a union of finitely
many intervals about the axes of total length O(1/ell). Subtract its
circle mean. The resulting periodic primitive has uniformly bounded
supremum, so the same calculation with A=1 proves (15). This applies
to all four axes and both choices at a tie, even though this is an
H-dependent indicator. No uniform theorem for arbitrary moving functions is
being invoked: the primitive norm is explicitly uniform.

L435 (3) has poles only at 1,p,p^(-2),p^3, all off the circle of
radius sqrt(p). Its rational expression thus has bounded derivatives
on each of the three compact circles. In L438 (6), a_H is bounded
and is held fixed under height differentiation; P is one fixed finite
polynomial. Hence (16) gives a uniform Lipschitz bound along the
actual prime phases. Taking positive or negative parts preserves
that bound. This justifies every amplitude used in (14), including
at zeros of F_H; boundedness alone would not have sufficed.

**Both intermediate directions and translation.** L369 gives
q=O(t^-2), so r=q/L^2 is O(1/ell) or smaller on this interval.
Together with L419's uniform O(1/L) response error and the exact
polynomial forms in L437, this makes both B-B_0 and D-D_0 uniformly
O(1/ell) on unit vectors. This is stronger than the o(1) sufficient
for the support margin in L437 and follows from the cited quantitative
inputs, without differentiating their remainder.

For U in L437, direct expansion gives
|U|^2/rho^2=(21+13 sin(2alpha))/16=v^2, with 1/2<=v^2<=17/8.
Dividing B_0(U)=c rho^2/2 and D_0(U)=-c^2 rho^4/4 by the
appropriate powers of |U| verifies h_-,0 and the cross entry in (18).
Their quotient is rho^(-3)4v cos(2alpha)/c^3. The derivative of
(21+13 sin(2alpha))^(3/2) is 39 sqrt(21+13 sin(2alpha))cos(2alpha),
so the circle integral of g_- is zero. All denominators stay uniformly
positive, including at a=0 and h=0; no negative-direction switch is
introduced.

For the positive direction, the squared leading projection difference
is (2/3)c^2 ah. Its sign selects sigma=sign(ah). Both exact squared
projections differ from their leading ones by O(1/ell), so a changed
selection is confined to (15), using rho>=rho_min. Reversing the
chosen vector leaves its cross entry 2sigma/9 unchanged. Its leading
ell_F=-1/3 and C_0=c^2 rho^2/4 give
D_0=c^2 rho^2(A^2+1/3), and hence exactly the denominator and
g_+ in (19). Here A>=1/3. Reflection alpha->-alpha preserves A
and reverses the numerator, proving zero circle mean. At the ties
both exact and comparison quotients are bounded by the uniform h_+
margin, so their entire discrepancy has the L1 bound O(1/ell).
Applying (14) to e_H sin(omega t)F_s rho^(-3) and then multiplying
by sqrt(ell) proves O(ell^(-1/2)) for each complete intermediate
contribution. The absolute O(sqrt(ell)) budget is never discarded.

For the translation, the leading squared norm of b is
c^2 rho^2 D0(alpha), with D0>=1. Its leading cross product is
-c^2 rho^2 cos(alpha)sin(alpha)/4. Division by |b|^4 gives
exactly g_m in (21), and the uniform lower bound for |b| controls
the O(1/ell) error. The scalar d_H is bounded and fixed during t
integration. Oddness of g_m and (14) give O(1/ell); inserting w
costs O(E_H(1-w)). No smoothness of w or of the six-state basis
is needed. The high term costs O(ell^-2) by its full second budget.
Finally A_12 is constant in t, so its unweighted sine integral costs
O(sqrt(ell)/H), and its mass-loss part costs
O(sqrt(ell) ell^(-5/2))=O(ell^-2). These are every cross term
in (3), proving (22) with the complete covariance correction.

**Decision and scope.** The total error is bounded by a fixed constant
times ell^(-1/2)+sqrt(ell)/H+ell^(-61/8)+D_j M_j/H,
plus a fixed multiple of |N_H-1|+ell^(-19/8). Every term tends
to zero for all real H on the original eventual ray. Thus (2) has
the stated positive constant, whereas the trajectory identity is
exactly zero. This independently validates one additional-identity
separation of the unchanged law. It neither retracts L438's selected
moment feasibility nor excludes a corrected or different law.
No actual sine limit, independence, conditional actual moment,
cutoff rate, clipping conclusion or RH consequence is used or proved.

## Mathlib

Full matching Mathlib coverage of this H-dependent complete-law
comparison has not been checked. Supporting ingredients are the cited
finite-interval occupation identity, finite Poisson character formula,
ordinary calculus, absolute geometric series and finite matrix raw
moments. They are distinguished from a formalization of (2). Unknown
coverage is not evidence of absence; no numerical certificate or
critical-line moment extrapolation is used.
