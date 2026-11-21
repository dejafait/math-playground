# C744j: Exact-neutral Legendre complement and a full-covariance Schur test

## Hypotheses

Use C744i's ell=log(3)/2, d=log(2), a=d/sqrt(2), K_1, J_d,
X=K_1+a J_d, and exact complex two-moment-neutral smooth class N_neut.
Inner products are linear in their first argument. No RH is assumed.
The target remains a common positive L2 margin for E+2X and E-2X.

Let p_n(x)=sqrt((2n+1)/ell) P_n(2x/ell-1) be the orthonormal shifted
Legendre polynomials. Write H_0=0 and H_n=sum_(j=1)^n 1/j. Import
the regional Legendre spectrum from Gerontogiannis--Mesland,
*The logarithmic Dirichlet Laplacian on Ahlfors regular spaces*,
[arXiv:2309.16636v2](https://arxiv.org/pdf/2309.16636v2),
Proposition5.8, printed p19, with Section2's complexification and
affine interval specialization. In the normalization of C744i(11),
the regional difference form is diagonal with entries H_n, rather
than the operator eigenvalues 2H_n. This is a known input.

Put

    V(x)=-gamma-log(2pi)-1/2 log(x(ell-x)),
    v_min=-gamma-log(pi ell),
    q_0(t)=2e^(-t/2)/(1-e^(-2t))-1/t, q_0(0)=1/2,
    (Qf)(x)=integral_0^ell q_0(|x-y|)f(y)dy,
    B_s=-Q/2+s 2K_1+s 2a J_d, s in {-1,+1}.

Here gamma is Euler's constant. Let D p_n=H_n p_n. Define the closed
semibounded form F_s of D+V+B_s on

    V_form={h: sum_n H_n |<h,p_n>|^2<infinity,
                  integral_0^ell (V-v_min)|h|^2<infinity}.

Both nonnegative parts define closed forms on their intersection;
B_s and the scalar v_min are bounded perturbations. On neutral smooth
tests, C744i(11) gives F_s(h)=E(h)+s 2<Xh,h>. This equality is used
only on that class; no new identification of a generator domain is
assumed. Polynomials belong to V_form and Vp is in L2 for every
polynomial p, since powers of an endpoint logarithm are integrable.

The Carleman input, as used in C744i(8), is Perfekt--Pushnitski,
*On the spectrum of the multiplicative Hilbert matrix*, Ark. Mat.56
(2018),163-183, [Lemma2.1, p166](https://archive.intlpress.com/site/pub/files/_fulltext/journals/arkiv/2018/0056/0001/ARKIV-2018-0056-0001-a010.pdf).
The complete-covariance square completion is the standard form Schur
method, compared in the saved step483 assessment with Li, paper45
displayed v2 (9 November 2026),
[Sections4-5, (4.1)-(5.5)](https://rstation.ai/problems/riemann_hypothesis/papers/45).
Its application to the exact-neutral graph is justified below; no
source matrix or source sign certificate is imported.

## Conclusion

There is an explicit exact neutral graph over the Legendre coordinates
n>=2. In that graph, for every N>=2 its high-coordinate complement
r=T_N q satisfies, for both signs,

    F_s(r) >= gamma_N ||q||_2^2,
    gamma_N=H_(N+1)-c(1+epsilon_N^2),
    c=gamma+log(pi ell)+ell/4+pi+2a,                     (1)

where epsilon_N is the norm of the low-coordinate moment correction
defined in the proof. In particular

    gamma_256 > 36223/50000 > 18/25 = 0.72.             (2)

This is a positive bound for the entire exactly neutral complementary
form space, not for either complete form on all of N_neut.

For each sign, the finite matrix M_s and complete covariance R_s in
(8) below give the following sufficient certificate: if gamma_N>0 and
some 0<rho<1, delta>0 satisfy

    M_s - R_s/(rho gamma_N) >= delta I, both signs,     (3)

then C744i(6) holds with

    mu=min{delta,(1-rho)gamma_N}/(1+eta^2)>0,            (4)

where eta is the norm of the full low-coordinate moment graph.
No enclosed matrices satisfying (3) are established in this step.
The unenclosed degree256 locator is promising; it is not a certificate
of (3), beta_1<1/2, any global signs, or RH.

The spectral and Schur mechanisms are known. This is a quantitative
specialization/reproduction, not a claim of a new general theorem.

## Proof

### 1. Exact moment coordinates

Set t=ell/4, and for n>=0 define the positive numbers

    i_n(t)=t^n/(2n+1)!! * sum_(k>=0)
                  t^(2k)/(2^k k! product_(j=1)^k(2n+2j+1)).

The empty product is one. Rodrigues' formula and n integrations by
parts give

    integral_(-1)^1 e^(tu)P_n(u)du
      =t^n/(2^n n!) integral_(-1)^1 e^(tu)(1-u^2)^n du
      =2 i_n(t).

The boundary terms vanish because (1-u^2)^n has zeros of order n at
both endpoints. Expanding the exponential and integrating its even
powers proves the series; uniform absolute convergence on [-1,1]
justifies the integration. Changing x=ell(u+1)/2 gives, for sigma=+1,-1,

    integral_0^ell e^(sigma x/2)p_n(x)dx
       =sqrt(ell(2n+1)) e^(sigma t) sigma^n i_n(t).       (5)

For n>=2, let e(n)=n mod2 and put

    r_n=sqrt((2n+1)/(2e(n)+1)) i_n(t)/i_(e(n))(t),
    z_n=p_n-r_n p_(e(n)).

The two moment equations are exactly their even and odd sums.
Consequently every neutral L2 function has the unique representation

    h=sum_(n>=2) c_n p_n
         -sum_(e=0,1) [sum_(n>=2, n mod2=e) r_n c_n]p_e,
    c_n=<h,p_n> for n>=2.                               (6)

All sums converge: the moments are continuous L2 functionals, and the
bounds below show (r_n) is square summable. Conversely (6) is neutral.
These are exact equalities, not quadrature moment projections.

For N>=2 let P_N project onto p_0,...,p_N and Q_N=I-P_N. Define

    v_(e,N)=sum_(n>N, n mod2=e) r_n p_n,
    T_N q=q-sum_(e=0,1)<q,v_(e,N)>p_e, q in ran Q_N,
    epsilon_N^2=max_(e=0,1) ||v_(e,N)||_2^2,
    eta^2=max_(e=0,1) sum_(n>=2, n mod2=e) r_n^2.

Then ||T_N q||^2=||q||^2+sum_e |<q,v_(e,N)>|^2, between ||q||^2
and (1+epsilon_N^2)||q||^2. Every neutral h in V_form splits uniquely
as p+T_N q with p=sum_(n=2)^N c_n z_n and q=Q_N h. Subtracting
polynomials preserves this form domain, so both parts are admissible.

For an effective bound, the positive series and i_0>=1, i_1>=t/3 give

    r_n <= b_n=3sqrt(2n+1)t^(n-1) exp(t^2/6)/(2n+1)!!,
    epsilon_N^2 <= sum_(n>N)b_n^2 <= 2 b_(N+1)^2.         (7)

Indeed the k-th series factor is bounded by the exponential series
with parameter t^2/[2(2n+3)], hence by exp(t^2/6). The even case
uses t<1 and the odd case uses 3/sqrt(3)<3. Finally
b_(n+1)/b_n=t/sqrt((2n+1)(2n+3))<1/sqrt(2), so the squares sum
to at most twice the first square. This also proves eta<infinity.

### 2. Complementary floor with the endpoint potential retained

For 0<u<=ell<1, write k(u)=e^(u/2)/sinh u. Then

    0 <= q_0(u) <= 1/2.

For the lower bound, sinh u/u=int_0^1 cosh(su)ds<=cosh u
<=exp(u^2/2)<=exp(u/2). The middle inequality follows by integrating
tanh v<=v. For the upper bound, compare power series in
exp(u/2)<=sinh u/u+(sinh u)/2. For the even coefficient of u^(2j)
this is 2j+1<=4^j; for the odd coefficient it is 1<=4^j.
Both hold for j>=0. Dividing by sinh u proves the bound. Thus
||Q||<=ell/2 by the integral-kernel Schur bound.

For K_1 the elementary estimate in C744i(8) is
0<k_1(x+y)<=1/[2(x+y)], so the cited Carleman bound gives
||K_1||<=pi/2. J_d is the full partial reflection of norm one.
Consequently ||B_s||<=ell/4+pi+2a, for either sign. Also V>=v_min.
For r=T_N q the regional diagonal contributes at least
H_(N+1)||q||^2; its low p_1 contribution is nonnegative. Therefore

    F_s(r)>=H_(N+1)||q||^2-c||r||^2
           >=[H_(N+1)-c(1+epsilon_N^2)]||q||^2,

proving (1). This use of V>=v_min is confined to the complement;
it does not discard V's head or mixed terms.

For transparency, (2) uses only coarse exact rational inequalities.
The standard Archimedes bound is pi<22/7. Positive-series comparison
gives .693<log2<.694, ell<.55, sqrt2<1.415 and
log(pi ell)<.55. For the last logarithm, pi ell<121/70 and the
degree6 positive Taylor polynomial of exp(.55) exceeds 121/70.
The degree5 polynomial of exp(1.1) exceeds3, giving ell<.55.
For log2 use 2sum_(k>=0)1/[(2k+1)3^(2k+1)]; the tail from k=5
is at most [2/(11*3^11)]/(1-1/9). Since H_n-log n decreases to
Euler's constant and H_64<4.744, gamma<4.744-6(.693)=.586.
It follows that

    c < .586+.55+.1375+22/7+(1.415)(.694) < 27/5.

With t<1/7 and exp(t^2/6)<2, (7) implies
epsilon_256^2<72(515)/7^512<1/10000, even after dropping the
double-factorial denominator. Direct rational summation gives
H_257>49/8. Thus

    gamma_256>49/8-(27/5)(10001/10000)
             =36223/50000>18/25.

The exact-rational checks and their full operands are saved in
`scripts/adjacent-neutral/complement-rational-check-484.json`;
reproduce with `python3 scripts/adjacent-neutral/complement-rational-check-484.py`.
All eleven inequalities pass. This certifies the complementary floor
only, with no finite-matrix sign claim.

### 3. Complete covariance and sufficient positive margin

For i=2,...,N and each sign put

    b_(s,i)=D z_i+V z_i+B_s z_i in L2,
    f_(s,i)=Q_N b_(s,i)
               -sum_(e=0,1)<b_(s,i),p_e> v_(e,N),
    (M_s)_(ij)=F_s(z_j,z_i),
    (R_s)_(ij)=<f_(s,j),f_(s,i)>.                       (8)

Every summand in b is L2: D z_i is a polynomial, V z_i has at
worst logarithmic endpoint singularities, and B_s is bounded.
For every admissible q,

    F_s(z_i,T_N q)=<b_(s,i),T_N q>=<f_(s,i),q>.

Thus (8) charges the full endpoint-log, Hankel and partial-reflection
mixed terms, including the exact moment-graph correction.

The uncorrected covariance R_s^0 is exactly computable through
complete L2 scalar products and finitely many moments:

    (R_s^0)_(ij)=<b_(s,j),b_(s,i)>
         -sum_(k=0)^N <b_(s,j),p_k> overline(<b_(s,i),p_k>).

If D_s is the two-row matrix (D_s)_(ei)=<b_(s,i),p_e>, then for
every alpha>0 a valid matrix upper bound is

    R_s <= (1+alpha)R_s^0
                 +(1+1/alpha)epsilon_N^2 D_s^*D_s.       (9)

To prove this, apply ||u-v||^2<=(1+alpha)||u||^2+
(1+1/alpha)||v||^2 to the sum of f_(s,i) with arbitrary coefficients;
the norm of the map from the two low coefficients to sum_e d_e v_e
is epsilon_N. No numerical deletion of the moment correction is needed.
An enclosed upper bound in place of R_s in (3) is sufficient.

Write p=sum t_i z_i, h=p+T_N q. By (1), its quadratic value is at least

    t^*M_s t + 2Re<sum_i t_i f_(s,i),q>+gamma_N||q||^2.

Young's inequality pays the mixed term by
-t^*R_s t/(rho gamma_N)-rho gamma_N||q||^2. Under (3) the result
is at least delta|t|^2+(1-rho)gamma_N||q||^2. The exact graph (6)
gives ||h||^2<=(1+eta^2)(|t|^2+||q||^2), proving (4).
For neutral smooth h this is the desired complete form margin.
This proves the sufficient test, not that its hypotheses hold.

### 4. Bounded numerical attempt and remaining certificate

`python3 scripts/adjacent-neutral/weighted-section-diagnostic-484.py`
saves full matrices/eigenvalues in its adjacent JSON. It integrates the
action b_(s,i), splitting at the reflection's jump, and treats the
Carleman action through Q_n(1+2x/ell); its remaining kernel is bounded.
Here Q_n(z) denotes (1/2)int_(-1)^1 P_n(u)/(z-u)du for z>1:
change variables and use P_n(-u)=(-1)^n P_n(u) to get
int_0^ell p_n(y)/(x+y)dy=2(-1)^n sqrt((2n+1)/ell)Q_n(1+2x/ell).
The code's finite backward recurrence is only a locator for these
integrals, not their certified evaluation.
The backward recurrence, quadrature, covariance subtraction and matrix
eigenvalues have no rigorous enclosures. Its moment ratios implement
(5)-(6), but floating point is not exact neutral verification. The tiny
tail graph correction in (9) is not enclosed in this locator.

At degree128/order512 the coarse exact tail formula has locator value
0.0588755; the uncorrected rho=1 Schur locators are -26.8824 and
-37.2645. This does not refute the forms. At degree256/order768 and
1024 the tail locator is0.74621248. The smaller two-sign Schur locator
is respectively0.06527709 and0.06527692; the other is about0.2383715.
These are diagnostics, not lower bounds. Even the rigorous floor0.72
in (2) is not a certification of these numerical Schur matrices.
Using instead floor0.72 and rho=.95 gives smaller Schur locators
0.06523804 and0.06523784 at those two orders; the other sign is about
0.2383579. The order1024 finite-action symmetry residual is about
5.65e-7 and its uncorrected covariance has minimum eigenvalues about
-4.48e-11 and-4.36e-11. These are unresolved numerical errors; exact
covariance is positive semidefinite. Agreement between orders does
not bound any error or license changing a negative eigenvalue to zero.

Outstanding work is precisely enclosed action scalar products,
complete covariance (9), finite matrix lower bounds with rho<1,
and a resulting mu>0 for both signs. No smooth counterexample or
full positive margin has been obtained. Distant-cell, non-neutral,
odd and global propagation questions are outside this statement.
C744i as a whole still awaits its separate audit; only its utilized
form normalization and bounded-kernel estimates were checked here.

## Mathlib

Full matching coverage of this exact-neutral graph, complementary
constant and two-sign Schur application has not been checked.
Availability is unknown. The regional Legendre spectrum, Carleman
bound, Parseval and finite-dimensional square completion are supporting
mathematical inputs, not a formal certificate of the unresolved margin.
