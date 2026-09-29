# Lemma 353: the signed Mellin correlation retains its nonconstant poles

**Hypotheses.** Retain L349–L350's r≥2, delta=r^(-1/2),
sigma=1+delta, complex kernel k_r, coefficients b_r^w and samples
a_n=sqrt(4 pi² exp(8n)−25). The coefficient functions below may
also use an independent real sigma>1; only their sampled application
couples sigma to r. For Re alpha>1 define

P_sigma(alpha;a)
 =zeta(alpha+ia)zeta(alpha−ia)/|zeta(sigma+ia)|²,
e_alpha(m)=sum_(j|m) j^(-alpha) mu(m/j)(m/j)^(-sigma).

For Re alpha, Re beta>1 let d_(alpha,beta)=e_alpha*e_beta,
where * is divisor convolution. For coprime positive A,B put

U_sigma(alpha;A,B)=sum_(h≥1)e_alpha(hA)e_alpha(hB),
F_sigma(alpha,beta;A,B)
 =sum_(h≥1)d_(alpha,beta)(hA)d_(alpha,beta)(hB),
J_sigma(alpha,beta;A,B)
 =F_sigma(alpha,beta;A,B)−U_sigma(alpha;A,B)
                         −U_sigma(beta;A,B)+1_(A=B=1).       (1)

The products in these coefficient functions are algebraic products,
not modulus squares. Complex conjugation will be encoded by beta.
The tested mechanism is automatic removal of nonconstant ratio poles
by the Möbius Euler factors before estimating the nonlinear samples.

**Conclusion.** With alpha_r(t)=sigma+i delta t and
beta_r(u)=sigma−i delta u, the exact centered correlation is

|R_r^w(a)|²=sum_((A,B)=1)h_r(A,B)exp(ia log(B/A)),
h_r(A,B)=integral_R² k_r(t) conjugate(k_r(u))
             J_sigma(alpha_r(t),beta_r(u);A,B) dt du.        (2)

All coefficient sums and integrals in (2) converge absolutely.
Their absolute budget is O(1), uniformly as r tends to infinity.
In particular, retaining the common index and moving parameters gives

D_N^w=(1/N)sum_(n=N)^(2N−1)sum_((A,B)=1)
 exp(ia_n log(B/A)) integral_R² k_(2n)(t)conjugate(k_(2n)(u))
 J_(sigma_n)(alpha_(2n)(t),beta_(2n)(u);A,B) dt du,           (3)

where sigma_n=1+(2n)^(-1/2). No average over height or over prime
phases occurs in (3). Its constant-frequency contribution is
C_w log(2)/(2N)+O(N^(-3/2)), with C_w as in L349.

For each fixed reduced pair A,B, the diagonal restriction
s ↦ J_sigma(s,s;A,B) has a meromorphic continuation to a
neighborhood of s=1/2. It has a pole of order exactly four there:

lim_(s↓1/2)(2s−1)^4 J_sigma(s,s;A,B)=L_sigma(A,B)>0.         (4)

The limit is uniform for 1≤sigma≤2, where sigma=1 denotes only
the boundary coefficient function, not an evaluated reciprocal zeta
series. L_sigma(A,B) is continuous and strictly positive on this
compact interval. Thus

L_(sigma_n)(A,B) → L_1(A,B)>0.                            (5)

This includes every nonconstant pair A≠B. The two subtractions in
(1) have at most first-order poles on this slice; they cannot remove
the fourth-order pole. In particular, the nonconstant local factors
do not provide an identically vanishing factor at the joint boundary.

Equations (4)–(5) stop this automatic pole-annihilation mechanism.
They do not justify moving the full Fourier sum to Re s=1/2, give a
lower bound for h_r or D_N^w, or preclude cancellation after Mellin
integration and summation at a_n. The required D_N^w=o(1), the
pointwise endpoint margin and the lower Laguerre signs remain open.

**Proof.** First work on the original contours. The absolutely
convergent reciprocal and Euler expansions recorded in L349 give

zeta(alpha+ia)/zeta(sigma+ia)
 =sum_(m≥1)e_alpha(m)exp(−ia log m).

At a prime p the generating function of e_alpha(p^j) is
(1−p^(-sigma)X)/(1−p^(-alpha)X). Multiplication therefore gives
the exact local generating function

sum_(j≥0)d_(alpha,beta)(p^j)X^j
 =(1−p^(-sigma)X)^2
   /[(1−p^(-alpha)X)(1−p^(-beta)X)].                      (6)

Multiplying each Dirichlet series by its opposite-height series
and using the unique reduction m=hA, l=hB gives U and F in (1).
Thus J is precisely the fully grouped coefficient of
(P_sigma(alpha;a)−1)(P_sigma(beta;a)−1). This is not an
independent-prime-phase replacement for the actual a.

L350 (4) gives R_r^w(a)=integral k_r(t)(P_sigma(alpha_r(t);a)−1)dt.
Here integral k_r(t)dt=1, by L349's scalar inversion at zero.
Since the denominator is a positive modulus square and sigma is real,
conjugation changes alpha_r(u) to beta_r(u). The product of these
two integral identities gives (2).

For justification in the coefficient l¹ norm, write E_r(t) for the
exact one-sided ratio norm in L350 (6); E_r(−t)=E_r(t)≥1. The
ungrouped centered product has norm at most

(E_r(t)^2+1)(E_r(u)^2+1).                              (7)

Ratio grouping is an l¹ contraction. L349–L350 prove
integral |k_r(t)| E_r(t)^2 dt≤C uniformly, so (7) is integrable
against |k_r(t)k_r(u)| with uniform bound C'. Tonelli for the
absolute majorant and then Fubini justify (2), all collisions,
and the finite average (3). No coefficient is frozen in n.

The same estimates also control the full contour tails, not only
compact t,u sets. On |delta t|≤1/2+delta their majorant is
C exp(−t²/4+C|t|); on the remaining contour the integral is
O(r^(5/2)2^(-r/4)), as proved in L349–L350. Therefore the l¹
norm of the portion of (2) outside |t|,|u|≤T is bounded by

C integral_(|t|>T)exp(−t²/4+C|t|)dt
                         +O(r^(5/2)2^(-r/4)).             (8)

The union of the two tails costs only a fixed extra factor. For
2N≤r<4N this tends to zero as T tends to infinity after N tends
to infinity, uniformly throughout the sample block. Formula (3)
uses the full integral, so this tail control is not a truncation
assumption. Its constant frequency is the squared coefficient norm
in L349 (4). Summing C_w/(2n)+O(n^(-3/2)) and using
sum_(n=N)^(2N−1)1/n=log 2+O(1/N) proves the stated constant term.

We now test the proposed Euler-factor zero. This is a calculation
of coefficient functions, not a contour shift in (3). Restrict to
alpha=beta=s real with 1/2<s<sigma and write
t=p^(-s), q=p^(-sigma), x=q/t. Thus 0<x<1. The local coefficients
of (6) and of its single-ratio counterpart are

d_0=1,
d_j=t^j[(j+1)−2jx+(j−1)x²]
   =t^j[(1−x²)+j(1−x)^2]  for j≥1,
e_0=1,   e_j=t^j(1−x)  for j≥1.                       (9)

In particular 0<d_j≤(j+1)t^j and 0<e_j≤t^j. This proves
0<d(m)≤tau(m)m^(-s) and 0<e(m)≤m^(-s). The correlation sums
for every fixed A,B are absolutely convergent for s>1/2. Indeed
tau(hA)≤tau(h)tau(A) and the corresponding B inequality reduce
the d sum to a constant times sum_h tau(h)^2 h^(-2s).
For any z>1, this last series converges: its positive Euler
factors sum to (1+p^(-z))/(1−p^(-z))^3, whose logarithms are
O_z(p^(-z)), and the finite products exhaust the positive series.
The e sum is simpler. Thus these sums continue the original
coefficient functions, with overlap 1<s<sigma when sigma>1.

For k≥0 define local correlation factors

T_(p,k)(s,sigma)=sum_(j≥0)d_(j+k)d_j,
V_(p,k)(s,sigma)=sum_(j≥0)e_(j+k)e_j.                  (10)

Every factor is positive on the real interval just specified.
The sums converge geometrically even at s=1/2. They have analytic
expressions in t for |t|<1, obtained by summing powers times
polynomials in j. For example, with z=t², A_0=1−x²,
B_0=(1−x)^2, and

S_0=z/(1−z), S_1=z/(1−z)^2, S_2=z(1+z)/(1−z)^3,

one has

T_(p,0)=1+A_0²S_0+2A_0B_0S_1+B_0²S_2,
T_(p,k)=t^k[(A_0+kB_0)+A_0(A_0+kB_0)S_0
                    +B_0(2A_0+kB_0)S_1+B_0²S_2], k≥1,
V_(p,0)=(1−2tq+q²)/(1−t²),
V_(p,k)=(t−q)t^(k−1)(1−tq)/(1−t²), k≥1.             (11)

These formulas retain all common prime powers in h. Unique prime
factorization and absolute convergence give, with k_p=v_p(AB),

F_sigma(s,s;A,B)
 = product_p T_(p,0) product_(p|AB) T_(p,k_p)/T_(p,0),
U_sigma(s;A,B)
 = product_p V_(p,0) product_(p|AB) V_(p,k_p)/V_(p,0). (12)

Coprimality ensures only one of A,B has p-adic exponent k_p.
Empty finite products equal one. Division in (12) is legitimate
on the real interval because both zero-exponent factors are positive.

Extract the exact singular factors by setting

mathcal A_sigma(s)=product_p (1−p^(-2s))^4 T_(p,0),
mathcal B_sigma(s)=product_p (1−2p^(-s−sigma)+p^(-2sigma)).

For s>1/2 these give

F_sigma(s,s;A,B)=zeta(2s)^4 mathcal A_sigma(s)
                       product_(p|AB)T_(p,k_p)/T_(p,0),
U_sigma(s;A,B)=zeta(2s) mathcal B_sigma(s)
                       product_(p|AB)V_(p,k_p)/V_(p,0). (13)

To check the boundary and exclude a hidden zero, first take real
1/2≤s≤5/8 and 1≤sigma≤2. From d_1=2(t−q), and the sum of
the terms j≥2 in (10), bounded by C t^4 uniformly for t≤2^(-1/2),

T_(p,0)=1+4t²−8tq+4q²+O(t^4),
(1−t²)^4 T_(p,0)=1+O(tq+q²+t^4)=1+O(p^(-3/2)).        (14)

Constants are uniform on this rectangle. Every factor on the left
is positive. The summable bound in (14) proves uniform convergence
of the tail logarithms; each finite initial product is positive and
continuous on the compact rectangle. Consequently mathcal A_sigma(s)
is continuous and bounded above and away from zero there. Similarly,
1−2tq+q²=(1−q)^2+2q(1−t)>0 and differs from one by O(p^(-3/2));
mathcal B_sigma(s) has the same properties.

For completeness, these are meromorphic pole statements, not only
one-sided real asymptotics. For |s−1/2|<1/16, the rational formulas
(11) are analytic, and the left side of (14) differs from one by
O(p^(-Re s−sigma)+p^(-2sigma)+p^(-4 Re s)) in absolute value.
This has a summable uniform majorant since Re s>7/16 and sigma≥1.
Thus mathcal A and mathcal B extend analytically by locally uniform
product convergence. The finitely many denominators in (13) are
nonzero in a neighborhood of s=1/2, by their positive value there;
compactness permits such a neighborhood uniform in sigma for fixed A,B.
Equation (13) supplies the asserted continuation. It does not continue
the full sampled Fourier series term by term.

The standard simple pole zeta(z)=1/(z−1)+O(1), recorded in L349's
pole-factor calculation, now gives

L_sigma(A,B)=mathcal A_sigma(1/2)
                  product_(p|AB)
                   T_(p,k_p)(1/2,sigma)/T_(p,0)(1/2,sigma). (15)

This is strictly positive: at the boundary q≤p^(-1)<p^(-1/2)=t,
so every d_j in (9), and hence every T_(p,k), is positive. All
finite factors are continuous for 1≤sigma≤2. The product argument
already bounded mathcal A away from zero, proving positivity,
continuity and a positive minimum of (15) for each fixed A,B.
The Laurent limit for F is uniform in sigma. Equation (13) gives
U_sigma(s;A,B)=O_(A,B)((2s−1)^(-1)) uniformly there, so neither
the two U terms nor the constant in (1) affects that limit. This
proves (4) and (5).

The positive leading coefficient is a pole coefficient on the
diagonal slice, not a claim about the one-variable residue of the
full kernel-weighted integrand. Off this slice the Mellin variables
remain independent. In particular, no positive-integrand argument
has replaced the complex kernels in (3). On the original contours
the calculation supplies only the already available O(1) absolute
budget; the required sampled bound is o(1). A new estimate of the
joint signed sum could still succeed. What fails here is the proposed
automatic elimination of its nonconstant pole by a local Möbius zero.

The closest inspected source is Li–Radziwiłł, *The Riemann zeta
function on vertical arithmetic progressions*, arXiv:1208.2684v1,
[Theorem 3, p. 2](https://arxiv.org/pdf/1208.2684v1#page=2) and
[Section 3, Lemma 1, pp. 8–10](https://arxiv.org/pdf/1208.2684v1#page=8).
Their mollifier correlation and arithmetic sampling are different.
The source's theorem is not reproved or applied here; (6)–(15) test
the changed correlation that the prior assessment left uncovered.
This is a local reproduction of elementary Euler-product methods,
not a claim of a new theorem beyond the checked literature or a
resolution of the sampled mean.

Finite verification: `python3 scripts/laguerre/check_signed_mellin_poles.py`
checks (11) by an independent rational residue calculation on a unit
circle, and checks the centered two-variable grouping for finite signed
two-prime polynomials. These are exact algebra checks; the infinite
product, continuation and uniformity assertions are proved above. ∎

**Mathlib.** Full statement: **not checked**. The two-variable grouped
correlation, its continuation, and the nonvanishing pole coefficient
have not been matched to library theorems. L349 records as present
the supporting
[`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius),
[`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff),
[`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re), and
[`riemannZeta_eulerProduct_exp_log`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log).
These inherited links were not rechecked. They support expansions in
Re s>1, not (4), the sampled target, or termwise contour shifting.
