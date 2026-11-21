# Lemma 939: a positive eventual tail for the fixed actual H2 density

## Hypotheses

K is exactly L019's theta kernel. The continuous signed density v is
exactly L938 equations (5)–(9): all 34 signed rows, twelve labelled
factors per row, and the normalization M_0^12 are retained. No
multinomial multiplicities, kernel substitution or positive factor
change is made. Put, for E>0,

    r=sqrt(E/12), n=pi exp(2r), eta=1-1/(2r),
    C_*=1/371319795000,
    B(r)=(8pi^2)^12 r^23 exp(54r-12n) / 2^12
             * (2pi/n)^(11/2) / (sqrt(12) eta^(11/2)).              (1)

B(r)>0 for r>1/2. No contact, real-zero, endpoint, determinant-sign,
variation-count or RH hypothesis is used. This is an analytic
asymptotic; it does not depend on L938's Decimal arithmetic contracts.

## Conclusion

As E tends to infinity,

    v(E)=B(sqrt(E/12)) (C_*+o(1)).                                  (2)

In fact the absolute error inside parentheses is bounded, for all
sufficiently large r, by fixed constants times

    exp(-2r) + exp(-11(r-1)^2/4)
              + r^11 exp(11r-11r^2/32).                           (3)

Consequently v(E)>0 for every sufficiently large E. The error divided
by C_* tends to zero; a merely unsigned scale comparison is not used.
No explicit onset is asserted. The independent step54 conceptual audit
below accepts this specialization of a known Laplace method. It is not
a claimed new general asymptotic theorem or a proof of RH.

Finite-energy crossings, the parameter endpoint signs of det H2,
contacts, other degrees, initialization, realization and global
continuation remain unresolved. In particular (2) does not turn
L938's compact-cell evidence into an at-most-one-crossing theorem.

## Proof

### The complete signed coefficient

For each row alpha in L938 choose k_1,...,k_12 in increasing order
with alpha_k occurrences of k. Define the fixed polynomial

    P(w_1,...,w_12)=sum_alpha c_alpha
                         product_i w_i^(k_i)/(2k_i)! .             (4)

Every monomial has total degree twelve. This polynomial need not be
symmetric; using the same ordering in each row preserves its
convolution integral exactly. There is no sum over permutations.
At w_i=1 every row enters the complete signed coefficient

    P(1,...,1)=sum_alpha c_alpha/product_k ((2k)!)^(alpha_k)=C_*.     (5)

Here is an independent small rational evaluation of (5). Substitute
e_k=1/(2k)! in the Newton recurrence of L938 (3). It yields

    (S_1,...,S_6)=(1/2,1/6,1/15,17/630,31/2835,691/155925).

L938's exact polynomial identity (5) then gives

    C_*=(1/6)(17/630)(691/155925) -(1/6)(31/2835)^2
         -(1/15)^2(691/155925)
         +2(1/15)(17/630)(31/2835) -(17/630)^3
       =1/371319795000>0.                                         (6)

Thus the value of the polynomial in L938's simplex coordinates at
t_i=1/12 is 12^(-12) C_*. It does not cancel. The absolute coefficient
sum C_abs=sum_alpha |c_alpha|/product_k ((2k)!)^(alpha_k) satisfies
C_abs/C_*=3893731/1024. This fixed cancellation loss must be retained,
but does not prevent an asymptotic relative error from tending to zero.

The exact-rational script `scripts/heat/l938-balanced-coefficient-52.py`
checks all 34 rows, both degree conditions, and agreement with (6).
Its adjacent `.json` contains every rational summand and the six
Newton values. Reproduction: `python3 scripts/heat/l938-balanced-coefficient-52.py`.
The displayed recurrence and arithmetic are the proof; the script is
an additional finite check, not a numerical proof of (2).

### Full theta factor, including derivative and boundary bounds

For u>=0 write

    K(u)=8pi^2 exp(9u/2-pi exp(2u)) q(u),
    q(u)=sum_(m>=1) [m^4-a m^2 exp(-2u)]
                              exp(-pi(m^2-1)exp(2u)), a=3/(2pi).   (7)

L019 gives positivity and this exact equality. In particular

    0<q(u)<=Q:=sum_(m>=1)m^4 exp(-pi(m^2-1))<infinity.              (8)

For j=0,1,2 there are fixed constants D_j such that, uniformly for
u>=0,

    |q^(j)(u)-1_(j=0)|<=D_j exp(-2u).                              (9)

To justify the differentiated full series, put t=exp(2u)>=1 and
A_m=pi(m^2-1). For m>=2, j differentiations by 2t d/dt bound the
absolute summand by a constant depending only on j times

    m^4 [1+(A_m t)^j] exp(-A_m t).

The factor [1+s^j]exp(-s/2) is bounded on s>=0. Moreover, since
A_m>=3pi and t>=1,

    A_m t/2 >= A_m/4 + (3pi/4)t.

The differentiated m>=2 sum is therefore at most a fixed multiple of
exp(-(3pi/4)t) sum_(m>=2)m^4 exp(-A_m/4). The latter series converges,
and exp(-(3pi/4)t)=O(t^(-1)). These are uniform derivative majorants,
so termwise differentiation through order two is valid. The m=1
summand is 1-a/t, whose corresponding derivatives have the same
O(t^(-1)) bound after subtracting the constant. This proves (9).
No large-u approximation is applied near a simplex face; there we
will use the full uniform bound (8).

### Exact change of variables and the constrained minimum

Use x_i=r^2+r y_i in L938's convolution integral, with

    y_12=-sum_(i=1)^11 y_i,
    D_r={y in R^11 : y_i>-r for all 1<=i<=12},
    w_i=1+y_i/r, u_i=r sqrt(w_i).

Thus sum x_i=12r^2=E, sum w_i=12 and dx_1...dx_11=r^11 dy.
The factors product x_i^(k_i-1/2) contribute r^12 because
sum k_i=12. Define

    f_r(s)=exp(2r(sqrt(1+s/r)-1)),
    h_r(s)=f_r(s)-1-s,
    z_r(y)=sum_(i=1)^12 h_r(y_i),
    g_r(y)=P(w) product_i w_i^(-1/2)
                * exp((9/2)sum_i(u_i-r)) product_i q(u_i).        (10)

Using sum y_i=0 and (7), the exact integral is

    v(E)=(8pi^2)^12 r^23 exp(54r-12n)/2^12
                          * integral_(D_r) g_r(y) exp(-n z_r(y))dy. (11)

All twelve factors remain present, and no approximation has yet
entered (11). The singular weights are locally integrable, as also
shown in L938.

For r>=2 and s>=-r, h_r(s)>=0. Indeed for s<=-1,
h_r(s)>=-1-s>=0. For -1<=s<=0 the function f_r is convex: writing
b=sqrt(1+s/r),

    f_r''(s)=exp(2r(b-1)) b^(-2)(1-1/(2rb)),                      (12)

and rb>=sqrt(r^2-r)>=sqrt(2)>1/2. The tangent at zero is 1+s,
so it lies below f_r on this interval. For s>=0, b>=1 and

    1-1/(2rb)>=3/4,
    exp(2r(b-1)) b^(-2)>=1,

the second inequality following from log b<=b-1 and r>=1.
Thus f_r''(s)>=3/4 and h_r(s)>=3s^2/8 on s>=0.

If y is nonzero with sum y_i=0, let S be the sum of its positive
coordinates. The sum of squares of the negative coordinates is at
most S^2, and S^2 is at most eleven times the sum of squares of
the positive coordinates. Consequently

    z_r(y)>=(3/8)sum_(y_i>0)y_i^2
            >=(1/32)sum_(i=1)^12 y_i^2.                           (13)

It also holds at zero. This controls the entire closed simplex,
including its faces, despite possible concavity of f_r near s=-r.
Zero is the unique constrained minimum. In the eleven independent
coordinates its Hessian is

    H_r=eta(I_11+J_11), det H_r=12 eta^11,
    ||y||_(H_r)^2=eta sum_(i=1)^12 y_i^2,                          (14)

where J_11 is the all-ones matrix. Its eigenvalues are eta (ten
times) and 12eta (once), so it is positive definite for r>=2.

### Actual outer integral and every boundary face

Since 0<w_i<12, (4) gives |P(w)|<=12^12 C_abs. Concavity of the
square root gives sum u_i<=12r, so the exponential factor in g_r
is at most one. Euler's beta integral, with all twelve parameters
equal to 1/2, gives

    integral_(D_r) product_i w_i^(-1/2)dy
        =r^11 12^5 Gamma(1/2)^12/Gamma(6)
        =r^11 12^5 pi^6/120.

This is the same iterated positive-parameter beta identity used in
L938; it applies to all faces simultaneously. Therefore

    integral_(D_r)|g_r(y)|dy<=B_0 r^11,
    B_0=Q^12 C_abs 12^17 pi^6/120.                                (15)

Choose the radius R=r in the cited Laplace theorem (r>=40). Its
local ball is U_r={||y||_(H_r)<=r sqrt(11/n)}. By (13)–(14),
outside U_r, n z_r>=11r^2/32. Hence the normalized actual outer
integral, including every boundary neighborhood, obeys

    sqrt(det H_r)(n/(2pi))^(11/2)
          * integral_(D_r outside U_r)|g_r| exp(-n z_r)dy
       <= (sqrt(12) B_0/2^(11/2))
                        r^11 exp(11r-11r^2/32) -> 0.             (16)

This uses (8), not a truncated theta series. It pays the actual
outer integral separately from any Gaussian tail estimate.

### Local regularity and application of the known signed expansion

We use Anya Katsevich, *The Laplace asymptotic expansion in high
dimensions*, [arXiv:2406.12706v3](https://arxiv.org/pdf/2406.12706v3),
12 June 2025, Theorem 2.12 (printed p11), Assumptions 2.1–2.2 and
Remark 2.5 (pp8–9), with L=1 and d=11. It requires a unique minimum
with positive Hessian, local C^2 amplitude/C^4 phase and a controlled
outer integral. Remark 2.5 permits the latter to replace Assumption
2.3's pointwise growth bounds. The theorem retains a signed amplitude
and separates local, Gaussian-complement and actual-outer errors.
These are imported results, not reproved here. The local/outer split
is explicit in Lemmas 4.1/4.4; the alternative outer bound replaces
only Lemma E.1's estimate. No BKR convolution theorem is used.

For the R^11 domain, extend g_r by zero outside D_r, including its
boundary, and set z_r=1+||y||_(H_r)^2 there. The extension is
measurable, has the same unique minimum, and leaves (11) unchanged.
Neither global continuity nor boundary differentiability is required
by the cited local regularity assumptions. The local ball lies wholly
inside D_r: from (14), on U_r,

    max_i |y_i| <= r sqrt(11/(eta pi)) exp(-r) < 1/2               (17)

for r>=40, since eta>=3/4. Thus the extended functions have the
required smoothness on a neighborhood of that closed ball.

We check uniform derivative bounds, not just pointwise smoothness.
For |s|<=1 and r>=40, w=1+s/r is bounded away from zero and

    psi_r(s)=2r(sqrt(1+s/r)-1)=2s/(sqrt(1+s/r)+1).

This last expression and its derivatives through order four are
continuous on the compact set (s,1/r) in [-1,1]x[0,1/40]. They
are uniformly bounded, including at 1/r=0. The same is true of
exp(psi_r(s)) and of psi_r(s)/2=u-r. It follows that z_r has
uniformly bounded derivatives through order four in the fixed
eleven coordinates near (17).

For g_r, the fixed polynomial P(w), the powers w_i^(-1/2), and
exp((9/2)sum_i(u_i-r)) have uniformly bounded derivatives through
order two on max_i|y_i|<=1. The derivatives of u_i through order
two are uniformly bounded there by the preceding formula. Bounds
(8)–(9) and the chain rule give the same conclusion for product
q(u_i). All dimensions and linear coordinate maps, including
y_12=-sum y_i, are fixed. Thus the ordinary derivative bounds are
uniform in r. Since the smallest eigenvalue of H_r is >=3/4,
the H_r-normalized derivative bounds c_3(R), c_4(R), c_(j,g)(R),
0<=j<=2, in the cited Definition 2.6 are uniformly bounded as well.

Set epsilon=11/sqrt(n). The barred bounds in (2.9), and hence
the quantity A_2(R) in (2.14), are bounded uniformly. Applying
Theorem 2.12 at each r with the outer replacement (16) gives

    sqrt(det H_r)(n/(2pi))^(11/2)
         * integral_(D_r) g_r exp(-n z_r)dy
       =g_r(0)+kappa_1+nu_1+nu_outer,                             (18)

where its local estimate (2.16) yields

    |kappa_1|<=C_1 exp(C_2(r^4+1)/n)/n=O(n^(-1)),

and its Gaussian-complement estimate (2.17) yields

    |nu_1|<=C_3 exp(-11(r-1)^2/4).

The constants are independent of r: the theorem's constants depend
only on L, and all quantities just checked are uniformly bounded.
The actual outer error satisfies (16). This application allows
r-dependent phase and amplitude because the estimates, including
their normalized derivative dependence, are nonasymptotic.

Finally, (5), (9) and (10) give

    g_r(0)=C_* q(r)^12=C_*+O(exp(-2r)).

Substitute this into (18), multiply by the exact prefactor in (11),
and use (14). The positive scale is precisely (1), proving (2)–(3).
Every error in (3) tends to zero; division by the fixed C_*>0 is
legitimate. For sufficiently large r their sum is <C_*/2, which
proves the asserted eventual strict positivity. This does not
assert any sign on the finite remaining energy interval.

### Independent conceptual audit — step54, 9 November 2026

The audit accepts (2)–(3), including the signed coefficient and all
relative errors. It reuses the pre-existing SPECIALIZE coverage in
`drafts/literature/2026-11-09-l939-tail-conceptual-audit-scope-52.md`.
The following are checks of the existing specialization, not new
lemmas, additional signs or a reproof of the general Laplace theorem.

**Complete finite algebra.** The independent checker
`scripts/heat/l939-balanced-audit-54.py` constructs the six-variable
truncated formal series log(1+sum_(k=1)^6 (-1)^k e_k t^k) through
weight six, extracts -n[t^n] for every S_n, forms the determinant,
and homogenizes with e_k=A_k/A_0 and A_0^12. All 34 resulting rows
agree exactly with L938's table. This differs from the coefficient
producer's exact-rational Newton recurrence. Each saved summand,
factorial denominator, both degree conditions, all six Newton values,
the determinant, absolute sum and simplex value agree exactly. All
77 checks pass. The complete old row evidence was inspected, and
the new exact certificate is `scripts/heat/l939-balanced-audit-54.json`.
Reproduce with `python3 scripts/heat/l939-balanced-audit-54.py`.
A preliminary parser mistakenly included the table header and aborted
before mathematical checks; its failure record is preserved alongside
the certificate. It was repaired by requiring an integer row coefficient.

**Normalization and localization.** The audit traces (11) directly
from L938(6)–(9). The twelve powers give r^(24-12)=r^12, the eleven
independent differentials r^11, and the twelve factors 1/2 give 2^-12.
The full theta prefactor gives (8pi^2)^12 exp(54r-12n). The determinant
Jacobian is sqrt(12) eta^(11/2), with no surface-measure factor: both
integrals use the first eleven coordinates. No permutation factor is
introduced. In (13), at most eleven coordinates are positive for a
nonzero zero-sum vector; negative squares are at most S^2 and positive
squares at least S^2/11. Combined with the positive-coordinate 3/8
bound this gives exactly 1/32, even on the boundary. Thus the only
minimum is zero, and the Hessian (14) is the constrained Hessian.

**Boundary and full series.** The beta integral in (15) has twelve
parameters 1/2 and sum six, producing 12^(6-1) Gamma(1/2)^12/Gamma(6).
It covers simultaneous faces, not just one face at a time. The full
q and its first two differentiated series have the uniform summable
majorant displayed before (10); for m=1 the correction is exactly
-a exp(-2u). Local derivative bounds therefore do not replace the
kernel by its first term. Outside the local ball the proof uses Q,
not the large-u approximation. Since eta<=1, (13) on that complement
gives n z_r >= 11r^2/(32eta) >= 11r^2/32. Multiplication by the full
normalizer gives precisely (16), with no missing power of n or eta.
The zero-amplitude measurable extension is integrable, preserves the
minimum and changes no integral. Smoothness at its distant faces is
not invoked.

**Uniform local data and theorem matching.** The closed local ball
is strictly inside max_i|y_i|<1/2, including the dependent coordinate.
For example its bound in (17) is <3r exp(-r)<1/2 for r>=40. The compact
(s,1/r) expression for psi has no singularity at 1/r=0. Composition
with the fixed coordinate maps controls all local ordinary derivatives;
H_r>=3I/4 controls their H-normalized norms. This justifies uniformity
for the whole closed ball, rather than only derivatives at the saddle.

Reinspection of the cited v3 Theorem2.12, Assumptions2.1–2.2,
Remark2.5 and Definitions2.6–2.11 confirms the local/outer split.
The relevant proof cases were also checked: Lemma4.1 and its AppendixE
change of variables, Corollary4.3, Lemma4.4 and (4.26), with LemmaE.1
used only to identify the default outer bound being replaced.
At L=1 the precise barred bounds are

    cbar_3(R)=c_3(0)+epsilon c_4(R),
    cbar_(1,g)(R)=c_(1,g)(0)+epsilon c_(2,g)(R),
    A_2(R)=c_(0,g)(R)(cbar_3(R)^2+c_4(R))
            +(cbar_(1,g)(R)cbar_3(R)+c_(2,g)(R))/11.

All are bounded uniformly. Also A_0(0) and epsilon A_1(0) are bounded,
which explicitly checks the prefactor in the Gaussian error (2.17).
With epsilon^2=121/n and R=r the local error is bounded by
C exp(C'(r^4+1)/n)/n. Its exponential factor is bounded because
(r^4+1)/n -> 0. The actual outer error is (16), not the theorem's
default outer estimate and not a Gaussian-complement surrogate.
The source's use of a signed amplitude is essential and is retained.

**Relative sign.** At the saddle the amplitude is exactly C_*q(r)^12,
not C_abs. Dividing (18) by C_* gives an error bounded by a fixed
multiple of the three functions in (3), since C_*>0 is fixed.
Their limits are zero: the local factor is exp(-2r), the Gaussian
exponent is a negative quadratic, and the logarithm of the outer
factor is 11 log r+11r-11r^2/32 -> -infinity. Thus the relative error
is eventually less than 1/2. The proof establishes v(E)>0 beyond an
unspecified finite onset, without numerical asymptotics or an exchange
of an uncontrolled limit with an integral. Neither a finite-energy
crossing count nor any parameter endpoint sign follows. The direct
DAG inputs remain L019 and L938; L037 is not an analytic premise.

## Mathlib

Full and supporting Mathlib coverage for this asymptotic and the
cited nonasymptotic theorem has not been checked. Unknown availability
is not a claim of absence. The rational coefficient check is Python
integer/Fraction arithmetic, not a Lean formalization. The analytic
specialization passed the independent step54 conceptual audit above;
this does not constitute formal verification of the source theorem.
