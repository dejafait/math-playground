# Lemma 768: the fixed third/fifth full-first-summand comparison on the full domain

## Hypotheses

Let K and its complete first summand B be the kernel and function of
L019 and L767. For real u>=0 and integer m>=1 set

\[
 C_m(F;u)=\frac1{(m-1)!}\int_u^\infty(v-u)^{m-1}F(v)\,dv,
 \qquad S(F;u)=-\det[\partial_u^{i+j}C_5(F;u)]_{i,j=0}^2.
\]

Use x=pi exp(2u) and A=B(u)=4x(2x-3)exp(u/2-x)>0.
This is only the fixed pair r=3,m=5, with the stated factorial convention.

## Conclusion

For every real u>=0, including u=0,

\[
 S(B;u)>\frac{A^3}{10(2x)^9x^3}>0,
 \qquad
 |S(K;u)-S(B;u)|<\frac{37}{100}S(B;u)<\frac12S(B;u).
 \tag{1}
\]

In particular S(K;u)>63 S(B;u)/100>0. This is a fixed-order
quantitative development of the comparison program in John Nuttall,
[*Wronskians and the Riemann Hypothesis*](https://publish.uwo.ca/~jnuttall/wronskRH.pdf),
August 2012, Sections 3.1–4.1, printed pp.2–5, and
[*Structure of Wronskians Related to the Riemann Hypothesis*](https://publish.uwo.ca/~jnuttall/RHsplit.pdf),
November 2012, Sections 2–3, printed pp.2–3. The literature assessment
inspected no matching certified m=5 relative bound. No source numerical
table, conjectured sign, or unproved all-order theorem is used here.
No originality beyond the inspected sources is claimed.

The proof uses finite exact rational arithmetic and outward decimal
interval arithmetic, with explicit analytic integration and continuum
remainders below. Its certificate and analytic proof passed the separate
later-turn step397 audit recorded below. It proves no effective all-order
smoothing threshold, exceptional coefficient transfer, unshifted Jensen
hyperbolicity, or RH assertion.

## Proof

### Normalized moments and the signed polynomial

L019 supplies integrability and dominated differentiation; L767 gives
the exact normalization and the complete-summand change of variables.
For p=0,...,4 put

\[
 d_p(x)=\frac{(2x)^{p+1}}A C_{p+1}(B;u),\qquad
 t_p(x)=\frac{(2x)^{p+1}}A C_{p+1}(K;u).
\]

The derivative signs and reversal of both rows and columns leave the
determinant unchanged. Consequently

\[
 S(B;u)=\frac{A^3}{(2x)^9}s(d),\quad
 S(K;u)=\frac{A^3}{(2x)^9}s(t),
\]
\[
 s(d)=d_0d_3^2+d_2^3+d_4d_1^2-d_0d_2d_4-2d_1d_2d_3.
 \tag{2}
\]

Writing epsilon=1/x gives

\[
 d_p=\frac1{p!}\int_0^\infty e^{-q}L^pUV\,dq,
 \quad L=\frac{\log(1+\epsilon q)}\epsilon,
 \quad U=(1+\epsilon q)^{1/4},
 \quad V=1+\frac{\epsilon q}{1-3\epsilon/2}.
 \tag{3}
\]

At epsilon=0 use L=q. Formula (3), considered directly, also defines
the auxiliary d_p for x>=3. Certifying that slightly larger domain
includes every needed x>=pi; no theta identity at negative u is assumed.

### A refined analytic tail for x>=32

Here are finite formulas for all coefficients and remainder constants
used in the tail certificate. They avoid any assumption that epsilon q
is small. Put J=20, e_*=1/32, and

\[
 \ell_j=\frac{(-1)^j}{j+1},\quad
 \lambda_{p,k}=[z^k]\left(\sum_{j=0}^{21}\ell_jz^j\right)^p,
 \quad b_i=\binom{1/4}{i}.
\]

For p=0 use lambda_(0,0)=1 and lambda_(0,k)=0 for k>0.
Only indices up to 21 are used. Let v_0=1 and v_j=(3/2)^(j-1)
for j>=1. The coefficient of epsilon^k in d_p at zero is

\[
 a_{p,k}=\frac1{p!}\sum_{i+j+h=k}
 b_i v_j\lambda_{p,h}\,(p+h+i+\mathbf1_{j>0})!,
 \qquad 0\le k\le20.
 \tag{4}
\]

For 0<=epsilon<=e_* the following nonnegative polynomials bound the
normalized derivatives of U and V:

\[
 U_0(q)=1+e_*q/4,\quad U_i(q)=|b_i|q^i\ (i>=1),
\]
\[
 V_0(q)=1+\frac{e_*q}{1-3e_*/2},\quad
 V_j(q)=\frac{(3/2)^{j-1}q}{(1-3e_*/2)^{j+1}}\ (j>=1).
\]

These follow by differentiation and concavity. The representation
L=integral_0^q(1+epsilon s)^(-1)ds gives

\[
 |\partial_\epsilon^kL|/k!\le q^{k+1}/(k+1).
\]

The product rule therefore bounds the kth normalized derivative of
L^p by |lambda_(p,k)|q^(p+k): every term has the same derivative
sign before taking absolute values. Define the exact rational number

\[
 R_p=\frac1{p!}\int_0^\infty e^{-q}
 \sum_{i+j+h=21}U_i(q)V_j(q)|\lambda_{p,h}|q^{p+h}\,dq.
 \tag{5}
\]

It is computed by integrating each monomial q^a to a!. These
integrable polynomial bounds also justify differentiation under the
integral. Taylor's theorem gives the uniform real estimate

\[
 d_p=\sum_{k=0}^{20}a_{p,k}\epsilon^k+r_p,
 \qquad |r_p|\le R_p\epsilon^{21}.
 \tag{6}
\]

Use L767's determinant-preserving finite differences
delta_k=sum_(j=0)^k (-1)^(k-j)binom(k,j)d_j and scaled variables

\[
 (w_0,w_1,w_2,w_3,w_4)
 =(\delta_0,\delta_1/\epsilon,\delta_2/\epsilon,
   \delta_3/\epsilon^2,\delta_4/\epsilon^2).
\]

The constant or linear coefficients removed by these divisions vanish
exactly, as checked from (4). Evaluate the remaining polynomials by
interval Horner evaluation on 0<=epsilon<=1/32, adding the error
sum_(j=0)^k binom(k,j)R_j epsilon^(21-order_k), where
(order_0,...,order_4)=(0,1,1,2,2). The rational certificate verifies
the following outward rational bounds:

| variable | lower | upper |
|---|---:|---:|
| w0 | 999/1000 | 1041/1000 |
| w1 | 249/1000 | 263/1000 |
| w2 | -101/100 | -999/1000 |
| w3 | 37/10 | 43/10 |
| w4 | 154/100 | 301/100 |

These are finite rational inequalities obtained from (4)–(6);
the full coefficients, R_p and tighter enclosures are saved in the
certificate. L767's exact identity becomes

\[
 x^3s(d)=-w_0w_2w_4+w_2^3+
 \epsilon(w_0w_3^2+w_1^2w_4-2w_1w_2w_3).
\]

All epsilon-weighted terms are nonnegative. Thus

\[
 x^3s(d)\ge(999/1000)^2(154/100)-(101/100)^3
 =\frac{25331027}{50000000}>\frac12.
 \tag{7}
\]

For x>=4, L767 bounds the full theta remainder by
|s(t)-s(d)|<=26664660 exp(-3x); this includes every n>=2.
Using (7) and exp(3x)>=(3x)^30/30! yields, for x>=32,

\[
 \frac{|s(t)-s(d)|}{s(d)}
 \le\frac{2\cdot26664660\cdot30!}{3^{30}32^{27}}
 <10^{-14}.
 \tag{8}
\]

The final comparison in (8) is another exact rational check. The
weaker bounds required in (1) follow on this entire unbounded tail.

### Certified moment integration at compact-interval centers

It remains to cover the 29 closed cells [a,a+1], a=3,...,31.
Their centers are c=a+1/2. At each c evaluate (3) with epsilon=1/c
by integration on q in [0,96] and a bound for q>=96. The quadrature
has 96 unit panels with centers b=j+1/2, j=0,...,95.

For one panel write q=b+z. The Taylor coefficients through degree
N=36 of its integrand are obtained from

\[
 c\log(1+(b+z)/c)
 =c\log(1+b/c)+\sum_{k\ge1}
       \frac{c(-1)^{k+1}z^k}{k(c+b)^k},
\]
\[
 (1+(b+z)/c)^{1/4}
 =(1+b/c)^{1/4}\sum_{k\ge0}\binom{1/4}{k}\frac{z^k}{(c+b)^k},
\]

together with V=1+(b+z)/(c-3/2) and
exp(-b-z)=exp(-b)sum_(k>=0)(-z)^k/k!.
Multiply truncated polynomials, raise the first to p, and divide by p!.
Every retained coefficient is therefore enclosed by explicit interval
arithmetic, without quadrature-node assumptions. Odd powers integrate
to zero; an even power z^k integrates on [-1/2,1/2] to
1/(2^k(k+1)).

Here is a uniform analytic bound for the omitted Taylor terms. On
|z|<=2, for c>=3 and b>=1/2, all branches above are analytic, since
Re(c+b+z)>0. For the logarithm use its series around c+b:

\[
 |c\log(1+(b+z)/c)|
 \le c\log(1+b/c)+\frac{2c}{c+b-2}\le b+6.
\]

Also

\[
 |(1+(b+z)/c)^{1/4}|\le(b+5)/3,
 \quad |1+(b+z)/(c-3/2)|\le(2b+7)/3.
\]

Thus a bound for the pth integrand, including 1/p!, on this disk is

\[
 M_p(b)=\frac{e^{2-b}(b+6)^p(b+5)(2b+7)}{9p!}.
\]

Cauchy's coefficient estimate bounds its kth coefficient by
M_p(b)/2^k. On |z|<=1/2 the degree-36 remainder is consequently
at most M_p(b)4^(-37)/(1-1/4). The panel length is 1, so this is
also an absolute bound for its integral error. These are ordinary
Cauchy coefficient estimates, with the analytic disks and branch
conditions specified above, not an empirical quadrature estimator.

For the remaining infinite integral, positivity and concavity give

\[
 0\le e^{-q}L^pUV/p!
 \le e^{-q}\frac{q^p}{p!}(1+3q/4+q^2/18),\qquad c>=3.
\]

Each integral from Q=96 to infinity is evaluated using the elementary
integration-by-parts identity

\[
 \int_Q^\infty e^{-q}q^k\,dq
 =e^{-Q}k!\sum_{j=0}^k Q^j/j!.
\]

Add symmetric panel remainders and the nonnegative infinite-tail
interval to the integrated polynomials. This encloses all five exact
d_p(c); in every cell the computed enclosures lie strictly in (0,3).

### Continuum enclosure preserving determinant cancellation

Point values alone do not certify a cell. Differentiating the
normalization gives, with d_(-1)=1,

\[
 d_p'(x)=\left(1+\frac{p-1/4}{x}-\frac1{x-3/2}\right)d_p(x)-d_{p-1}(x),
 \qquad p=0,...,4.
 \tag{9}
\]

The p=0 boundary term is -1. For p>=1 use C'_(p+1)=-C_p
and dx/du=2x; A_x/A=5/(4x)+1/(x-3/2)-1. This proves (9).

Let d_p(c+t)=sum b_(p,k)t^k. Write alpha_(p,k) for the kth
Taylor coefficient at c of the parenthesized factor in (9):

\[
 \alpha_{p,k}=\mathbf1_{k=0}+(-1)^k
 \left(\frac{p-1/4}{c^{k+1}}-\frac1{(c-3/2)^{k+1}}\right).
\]

Starting with the certified b_(p,0)=d_p(c), the recurrence is

\[
 b_{p,k+1}=\frac1{k+1}
 \left(\sum_{j=0}^k\alpha_{p,j}b_{p,k-j}-b_{p-1,k}\right),
 \tag{10}
\]

with b_(-1,0)=1 and b_(-1,k)=0 for k>0. Use (10) through degree
64, p=0,...,4 in order; denote the resulting polynomials by P_p(t).

For completeness, the following bound controls every omitted term.
Formula (3) extends holomorphically in x to Re x>3/2, locally with
an integrable bound in q, using principal logarithms and powers.
It agrees with (9). On |x-c|<=1, c>=7/2, the coefficient in (9)
has absolute value at most

\[
 1+\frac{15/4}{c-1}+\frac1{c-5/2}\le7/2.
\]

Include d_(-1)=1 as a constant component. The row-sum norm of the
linear system is at most 9/2<6. Integrating along radial segments,
the elementary Gronwall bound gives max_p |d_p(x)|<=3 exp(6)<1500
on that disk, from the certified initial bound d_p(c)<3. This
Gronwall bound can equally be obtained by iterating its integral
inequality and summing the exponential series. Cauchy's estimate
therefore yields, on |t|<=1/2,

\[
 |d_p(c+t)-P_p(t)|\le1500\sum_{k\ge65}2^{-k}
 =\frac{3000}{2^{65}}=:\delta.
 \tag{11}
\]

Arithmetic uncertainty in retained coefficients is already included
in their intervals; (11) is the analytic truncation error in addition.

Form the entire degree-192 polynomial s(P_0,...,P_4) using (2)
*before* evaluating t in [-1/2,1/2] by interval Horner evaluation.
This retains coefficient cancellations. To include (11), first enclose
each P_p(t)+[-delta,delta] in an interval D_p. On their rectangular
product the gradient of s is enclosed by the explicit formulas

\[
 \nabla s(d)=(d_3^2-d_2d_4,
 2d_4d_1-2d_2d_3,
 3d_2^2-d_0d_4-2d_1d_3,
 2d_0d_3-2d_1d_2,
 d_1^2-d_0d_2).
 \tag{12}
\]

If G_p bounds the absolute value of the pth component, the remaining
determinant error is at most delta sum G_p, by integrating the
gradient along the segment from P(t) to d(c+t). The certificate
adds that symmetric error to s(P)'s interval. Its lower endpoint
is denoted L_a and is positive in every cell.

### Complete theta remainder on each compact cell

No theta sum is truncated without a remainder. L767's exact formula
for the nth normalized summand is

\[
 \frac{e^{-(n^2-1)x}}{p!}\int_0^\infty e^{-q}
 [x\log(1+q/(n^2x))]^p(1+q/(n^2x))^{1/4}
 \frac{2n^2x+2q-3}{2x-3}\,dq.
 \tag{13}
\]

All summands are nonnegative, so Tonelli applies. For n=2 use
x log(1+q/(4x))<=q/4 and concavity of the fourth root. The resulting
upper bound, decreasing with x>=3, can be evaluated at x=a:

\[
 E_{p,2}(a)=\frac{e^{-3a}}{4^p}
 \left[\frac{8a-3}{2a-3}\left(1+\frac{p+1}{16a}\right)
 +\frac{2(p+1)}{2a-3}\left(1+\frac{p+2}{16a}\right)\right].
 \tag{14}
\]

For n>=3 and x>=3 bound the three factors in (13) by
(q/n^2)^p, 1+q/12, and 2n^2(1+q/3), respectively. After integration
their product is at most

\[
 2n^{2-2p}\left[1+\frac{5(p+1)}{12}
                  +\frac{(p+1)(p+2)}{36}\right]
 \le\frac{47}{6}n^2<8n^2,\quad 0<=p<=4.
\]

For n>=4, n^2-9>=n and n^2<=4^(n-1); exp(3)>16. Hence

\[
 \sum_{n\ge3}n^2e^{-(n^2-1)x}
 \le e^{-8x}\left(9+\sum_{n\ge4}n^2e^{-3(n^2-9)}\right)
 < e^{-8x}(9+1/768)<10e^{-8x}.
\]

Thus the full entry differences satisfy, for x in [a,a+1],

\[
 0<=t_p-d_p<=\eta_{p,a}:=E_{p,2}(a)+80e^{-8a}.
 \tag{15}
\]

Evaluate (12) on D_p+[0,eta_(p,a)]. If H_p bounds its absolute
pth component there, the complete signed determinant difference is
bounded by E_a=sum H_p eta_(p,a). Again this follows by integrating
the gradient on a segment; it assumes no favorable tail cancellation.
The required check on this entire cell is E_a<L_a/2.

### Certificate, finite verification, and scope

Run from the notebook:

`python3 scripts/cumulant-comparison/compact-certificate-395.py`

The complete output is
`scripts/cumulant-comparison/compact-certificate-395.json`.
The script implements (4)–(15). Tail calculations use Python exact
fractions. Compact calculations use 55-digit Decimal intervals:
arithmetic rounds downward/upward; correctly rounded Decimal exp
and ln are enlarged by one adjacent representable value in each
direction. Positive fourth roots are exp(log(y)/4). Thus elementary
function evaluations also have outward bounds, rather than assumed
floating-point accuracy. The certificate records every panel integral
and error, all moment and Taylor coefficient intervals, every signed
polynomial coefficient, analytic remainders, theta entry bounds and
all 29 closed-cell comparisons. It has no failed cells.

The replay used Python 3.15.0. The installed Decimal exp and ln
docstrings were checked: each explicitly states correctly rounded
results in ROUND_HALF_EVEN mode. Enlarging their nearest-rounded
values as above is the implementation premise for the transcendental
enclosures; step397 below verifies the code against this contract.

The finite inequalities verified for the compact part are

\[
 \min_{3<=a<=31}a^3L_a>\frac{1005239}{10^7}>\frac1{10},
 \qquad
 \max_{3<=a<=31}\frac{E_a}{L_a}
 <\frac{364211}{10^6}<\frac{37}{100}.
 \tag{16}
\]

Both worst bounds occur in [3,4]; its signed lower endpoint is
greater than 0.0037231095. The certificate checks coverage in unit
steps, positive lower endpoints, and the stated thresholds. For
x in [a,a+1], x^3s(d)>=a^3L_a>1/10, and
|s(t)-s(d)|/s(d)<=E_a/L_a<37/100. Together with (7)–(8) this proves
the required normalized assertion for every x>=pi: the auxiliary base
is bounded down to x=3, and every physical x>=pi lies in the covered
cells or the analytic tail. Multiplication by the same positive
A^3/(2x)^9 proves (1).

The earlier `compact-first-cell-395.json` is a retained preliminary
first-cell run; the full-domain certificate is authoritative for this
lemma. Earlier step394 floating-point samples are not used. Separate
verification checked all 29 adjacent cells, all 2784 panels, the full
coefficient-array dimensions, finite ordered interval endpoints and
every recorded threshold. That structural check does not replace the
analytic proof above. The separate completed audit follows.

### Independent audit — 2026-11-04, step397

The full fixed statement (1), including u=0, passes this later-turn
audit. L767's normalization, finite differences, theta substitution
and complete x>=4 remainder were independently checked there.
For (4) here, the epsilon degree j>0 in V contributes exactly one
power of q, explaining the factorial's indicator. The normalized
derivatives of L all have sign (-1)^k on epsilon>=0. Every term
in a fixed derivative of L^p consequently has that same total sign,
so |lambda_(p,h)|, including p=0, gives the stated bound. The U/V
majorants dominate the full epsilon interval, not a q cutoff.
Their integrability justifies differentiation and the order-21 real
Taylor remainder. Independent bivariate polynomial multiplication
reproduced all 105 coefficients and five R_p in (4)–(6). The removed
finite-difference coefficients vanish exactly. All five rational
enclosures, the lower bound 25331027/50000000>1/2, and (8)'s
relative bound <10^(-14) were reproduced.

For a compact panel, c+b-2>=3/2, so the closed radius-2 disk has
an analytic neighborhood for the chosen logarithm and fourth root.
The log series has ratio |z|/(c+b)<1, and its absolute sum is bounded
by 2c/(c+b-2)<=6. Also |1+(b+z)/c|<=1+(b+2)/c<=(b+5)/3,
whose right side is >=1; taking a fourth root can only reduce this
upper bound. The V bound follows from c-3/2>=3/2. These facts prove
M_p(b), the geometric Cauchy remainder, and the integrated panel
error. The positive q>=96 tail is bounded by the displayed polynomial
majorant and exact incomplete-gamma identity. Every panel and tail
interval was recomputed; no sampled integral is an input.

The x-dependent integral is holomorphic on Re x>3/2: on a compact
subset, Re(1+q/x)>=1, all denominators stay away from zero, and the
integrand has a compact-set majorant C e^(-q)(1+q)^6; local derivative
bounds follow on smaller compact sets by Cauchy's estimate. The
normalization derivative gives (9) on the physical domain;
holomorphic continuation gives the same identity
on this half-plane. In particular d_(-1)=1 contributes only the
constant coefficient at p=0 in (10). For |x-c|<=1 and c>=7/2,
the diagonal coefficient has modulus <=7/2, the off-diagonal entry
has modulus 1, and the extra constant component has derivative zero.
Radial-segment Gronwall therefore gives sup |d_p|<=3 exp(6)<1500.
The disk has an analytic neighborhood, so the Cauchy bound and
the sum 3000/2^65 hold also at both real cell endpoints. The interval
polynomials enclose all retained exact coefficients. Their full
degree-192 signed combination is formed before evaluation; (12)
is the direct gradient of (2). Both P(t) and d(c+t) lie in the
rectangular D box, so the segment argument pays the analytic error.

For the theta error, (8x-3)/(2x-3)=4+9/(2x-3), 1/x and
1/(2x-3) are positive and decreasing on x>=3. Thus every factor
in (14) is legitimately bounded at the left endpoint. The n>=3
coefficient maximum before the n power is 47/6<8. The geometric
bound uses n^2-9>=n for n>=4 and exp(3)>16, giving 1/768;
the n=3 term remains explicit. Hence (15) includes the entire
theta series. The enlarged box contains the segment between d and
t, so its gradient estimate bounds the signed determinant difference
without assuming a favorable sign.

The implementation audit read every operation of
`scripts/cumulant-comparison/compact-certificate-395.py`.
Addition and multiplication use directed Context operations on the
extremal endpoints, including all mixed-sign branches; reciprocal
reverses the nonzero denominator endpoints. Exact copy_negate and
copy_abs avoid implicit ambient-context rounding. Integer powers
are repeated interval products; no Context.power approximation is
used. Every retained coefficient, convolution, gradient and threshold
is computed with these enclosing operations. The only ambient
Decimal arithmetic forms small exact half-integer centers or tests
the sign of a denominator product; that product cannot change sign
by rounding, and a zero result rejects rather than accepts a division.
No floating-point conversion enters an enclosure.

The primary software contract is Python's official
[Decimal.exp](https://docs.python.org/3.15/library/decimal.html#decimal.Decimal.exp),
[Decimal.ln](https://docs.python.org/3.15/library/decimal.html#decimal.Decimal.ln),
and [Context methods](https://docs.python.org/3.15/library/decimal.html#context-objects),
located in step396. The served 3.15.2 documentation is distinguished
from this replay's Python 3.15.0/libmpdec 4.0.1. Both installed method
docstrings explicitly give the same nearest-even correct-rounding
contract. With equal 55-digit precisions and exponent ranges,
next_minus/next_plus around those nearest-rounded endpoint values
enclose the exact monotone functions; exp(log(y)/4) encloses the
positive fourth root. All replay contexts had only Inexact/Rounded
flags, with no underflow, subnormal, overflow, invalid or clamped
results. An independent exact-rational check exercised 351 primitive
enclosures across the sign cases; convergent rational series enclosed
exp(1) and log(2) within the computed intervals. These extra tests
support the implementation audit; the stated software contract,
not two test values alone, justifies all transcendental calls.

`python3 scripts/cumulant-comparison/audit-397.py` recomputes all
29 cells, 2784 panels, 43598 ordered interval pairs and the complete
coefficient arrays, with exact equality to the archived finite evidence.
It separately checks every cell's thresholds with exact fractions and
checks adjacency, endpoints, dimensions and both tail certificates.
The exact results and runtime contracts are saved in
`scripts/cumulant-comparison/audit-397.json`; the full cell evidence is
`scripts/cumulant-comparison/compact-replay-397.json`. All original
scripts and certificates are unchanged, as recorded by their hashes.
The minimum a^3 L_a exceeds 0.100523957 and the maximum E_a/L_a is
less than 0.364210965. Thus x=pi is in the certified first cell and
x=32 is included in both the last closed cell and the analytic tail.
This accepts the advertised fixed-order quantitative reproduction,
with the documented software arithmetic premises. It supplies no
all-order smoothing estimate, exceptional coefficient transfer, or
claim of originality beyond the sources checked.

## Mathlib

Not checked. Availability of this full quantitative comparison or its
certificate implementation is unknown. Cauchy's coefficient estimate,
Taylor's theorem with remainder, Tonelli, elementary Gronwall, and
the product/chain rules are the standard analytic inputs used here;
no claim is made that a supporting formal theorem proves (1) outright.
