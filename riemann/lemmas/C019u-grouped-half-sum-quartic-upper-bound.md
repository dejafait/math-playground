# C019u — Grouped half-sum quartic bound, short of the required scale

## Hypotheses

Use exactly C019m/p/s/t's real normalized actual-Jensen value P,
reference V, positive gamma normalization, d,T,X,q,B,h,J,D and
finite mollifier M. In particular d tends through positive integers,

\[
 d=\frac{T}{2\pi}(\log(T/(2\pi))-1),\quad T>2\pi e,
 \quad X=T/\sqrt{2d},\quad q=\log X,\quad B=(\sqrt2-1)X,
 \quad h=3\pi/q,
\]
\[
 J=[X,\sqrt2X],\quad D=[X,\sqrt2X-h],\quad
 t(Z)=Z^2/(2d),\quad
 N(Z)=\left\lfloor\sqrt{Z/(2\pi)+Z^2/(32d)}\right\rfloor.
\]

Keep L=floor(X^(1/1000)), omega(n)=log(L/n)/log L,
and the real Euler-product coefficients alpha of zeta(s)^(-1/2)
defined on Re(s)>1. Set

\[
 M(Y)=\sum_{n\le L}\alpha(n)\omega(n)n^{-1/2-iY},\quad
 H(Y)=M(Y)M(Y+h),\quad W=|H|^2,\quad R=L^4,
\]
\[
 H(Y)^2=\sum_{r\le R}c_r r^{-1/2-iY},\qquad
 c_r=\sum_{uv=r;\ u,v\le L^2}b_ub_v,
\]

where b is C019p's exact shifted convolution. C019p/s give
|b_u|<=1 and |c_r|<=tau(r), with tau the ordinary divisor function.
All assertions are beyond one absolute existential integer onset.
Each shifted factor retains its own heat time and true source floor.
There is no RH, nonvanishing, simplicity, random-law or critical-line
reciprocal hypothesis.

## Conclusion

There is an exact grouped finite half-sum norm \(\mathscr J_d\),
defined in (3) below, such that

\[
 I_V:=\int_D V(Y)^2V(Y+h)^2W(Y)^2\,dY\le16\mathscr J_d,
 \qquad
 I_P=O\bigl(X^{251/250}q^{16}\bigr),\quad
 I_V=O\bigl(X^{251/250}q^{16}\bigr).                       \tag{1}
\]

The required bound is I_P=O(B), equivalently I_V=O(X) by C019t.
Thus (1) does not close the target: its upper-bound loss is
X^(1/250)q^16. It is not a lower bound or an obstruction to M2.
The grouped estimate below also gives explicit sufficient signed
coefficient budgets (8); neither is proved at the required scale.
Failure of these sufficient budgets or of the stronger half-sum norm
would not refute the original real-pair bound.

Later qualification (step1407): C019w proves that the second budget
in (8), (1+log Z_*) sum mathcal B_k^2=O(X), is impossible for
these exact coefficients. This does not change inequalities (1),(8)
or disprove the time norm; the weighted diagonal and direct signed
off-diagonal remain open. The earlier unpaid-budget language below
records the status at the time of this derivation.

Later qualification (step1408): C019x also rules out the separate
weighted diagonal budget, proving its high block is at least cXq^2.
Neither diagonal growth nor the failed variation budget lower-bounds
the grouped time norm: its signed off-diagonal is still unevaluated.
The real-pair M2 target remains open. Independent conceptual audit1409
retains C019x's weighted-diagonal obstruction; C019w's variation-budget
obstruction still awaits its own independent audit.

This is an elementary finite-sum reproduction within the unchanged
EXPLORE assessment1402, not an import of an ordinary zeta fourth
moment or a claim of progress beyond the literature checked. It
retains every moving entry and heat factor. C019t and this calculation
remain without an independent conceptual audit. No sign-density,
root-count, every-degree positivity or RH conclusion follows here.

## Proof

### Exact grouping before estimation

Write u(Z)=log(Z/(2*pi))/2, v_n(Z)=u(Z)-log n,
theta(Z)=Z log(Z/(2*pi))/2-Z/2-pi/8, and c_0=pi/8.
Define, for all n<=N_*=N(sqrt(2)X), including before entry,

\[
 E_n(Z)=\exp\{t(Z)(v_n(Z)^2-\pi^2/16)/4+i c_0t(Z)v_n(Z)\},
\]
\[
 F(Z)=e^{i\theta(Z)}\sum_{n\le N(Z)}E_n(Z)n^{-1/2-iZ}.
                                                               \tag{2}
\]

C019m (7) gives V=F+conj(F) exactly. Since |V|<=2|F|,
and W^2=|H^2|^2, the first inequality (1) holds with

\[
 \mathscr J_d=\int_D |F(Y)F(Y+h)H(Y)^2|^2\,dY.
                                                               \tag{3}
\]

No real-pair channel is dropped: (3) is a pointwise majorant for
their complete sum. It need not be comparable from below to I_V.

Let rho_n>0 solve rho_n/(2*pi)+rho_n^2/(32d)=n^2.
Monotonicity of this function makes n<=N(Z) exactly Z>=rho_n.
Put Z_*=N_*^2R, an integer; this symbol is a length, not a height
argument in (2). For 1<=k<=Z_* and Y in D define

\[
 G_k(Y)=\sum_{\substack{m,n\le N_*,\ r\le R\\mnr=k}}
 c_r n^{-ih}E_m(Y)E_n(Y+h)
 \mathbf1_{\{Y\ge\max(\rho_m,\rho_n-h)\}}.                 \tag{4}
\]

The exact finite product identity is

\[
 F(Y)F(Y+h)H(Y)^2
 =e^{i\{\theta(Y)+\theta(Y+h)\}}
       \sum_{k\le Z_*}G_k(Y)k^{-1/2-iY}.                  \tag{5}
\]

Indeed m^(-iY)n^(-i(Y+h))r^(-iY)=k^(-iY)n^(-ih),
and all square-root denominators multiply to sqrt(k).
The indicator in (4) preserves the exact joint entry. Its
intersection with D may be empty or a singleton; the latter has
zero integral. The common phase in (5) has modulus one.
In particular the frequencies in the grouped norm are exact
logarithms of integers. No approximate heat phase separation is used.

### Moving coefficient variation and the signed budgets

C019m/p supply d comparable to X^2q^2, N_*=O(sqrt X),
t=O(q^(-2)), and |v_n|=O(q) uniformly for every n<=N_*
and every Z in J, including before entry. Thus |E_n|<=C.
For explicit control of its derivative, t'=Z/d and v_n'=1/(2Z)
give

\[
 \frac{E_n'}{E_n}
 =\frac{t'}4(v_n^2-\pi^2/16)+\frac{t v_n}{4Z}
       +i c_0\{t'v_n+t/(2Z)\}=O(1/X).                   \tag{6}
\]

Every E_m(Y)E_n(Y+h) therefore has bounded supremum and total
variation on D, with absolute bounds. Multiplication by its single
entry indicator adds at most one bounded jump. This treats the
floors by their actual jumps, never by differentiating a floor.

Let Var_D denote total variation, including jumps, and put
\(\mathcal B_k=\sup_D|G_k|+\operatorname{Var}_D(G_k)\).
For d_j(k), the number of ordered factorizations of k into j
positive integers, (4), (6), and |c_r|<=tau(r) imply

\[
 \mathcal B_k\le C\sum_{mnr=k}\tau(r)=C d_4(k).           \tag{7}
\]

The signs and phases in G_k are retained in the definition of
mathcal B_k; (7) is where the estimate discards them.
Define the exact grouped diagonal
\(\mathscr D_d=\int_D\sum_{k\le Z_*}|G_k(Y)|^2/k\,dY\).
We will prove

\[
 |\mathscr J_d-\mathscr D_d|
 \le C(1+\log Z_*)\sum_{k\le Z_*}\mathcal B_k^2.
                                                               \tag{8}
\]

Consequently sufficient conditions for M2 through this majorant
are mathscr D_d=O(X) and
(1+log Z_*) sum mathcal B_k^2=O(X). They are independent unpaid
arithmetic budgets in this argument, not assumptions of (1).
The simpler sufficient diagonal condition
sum mathcal B_k^2/k=O(1) also follows from |D|<=B=O(X).

To prove (8), expand (5) inside (3); all sums are finite. For
k!=l put g=G_k conj(G_l) and omega=log(l/k). On the finitely
many smooth entry pieces, ordinary integration by parts, with
the interior boundary terms collected as jumps, gives

\[
 \left|\int_D g(Y)e^{i\omega Y}\,dY\right|
 \le\frac{2\sup_D|g|+\operatorname{Var}_D(g)}{|\omega|}
 \le\frac{4\mathcal B_k\mathcal B_l}{|\log(l/k)|}.
                                                               \tag{9}
\]

Endpoint jumps can only increase the displayed bound. The product
variation inequality follows by subtracting successive products
on a partition and using the two suprema. Thus (9) is valid also
for complex coefficients and for every entry placement.

For completeness, the needed finite logarithmic-kernel bound has
no unverified rational-frequency premise. Set
A_kl=1/(sqrt(kl)|log(l/k)|) for k!=l, A_kk=0, and w_k=k^(-1/2).
Then

\[
 \frac1{w_k}\sum_{l\le Z_*} A_{kl}w_l
 =\sum_{l\ne k}\frac1{l|\log(l/k)|}
 \le5(1+\log Z_*).                                       \tag{10}
\]

For l>k, log(l/k)>=(l-k)/l bounds the summand by 1/(l-k).
For k/2<=l<k, log(k/l)>=(k-l)/k bounds it by 2/(k-l).
For l<k/2 use log(k/l)>=log 2 and the harmonic sum in l.
These three sums are at most
(3+1/log 2)(1+log Z_*)<5(1+log Z_*).
Finally apply
2x_k x_l<=x_k^2 w_l/w_k+x_l^2 w_k/w_l, for nonnegative x,
and use the symmetry of A. This proves
sum_(k,l) A_kl x_k x_l<=5(1+log Z_*)sum_k x_k^2.
Apply this with x_k=mathcal B_k in the full off-diagonal sum
from (9), including its factors 1/sqrt(kl), to obtain (8).

### Actual bound and comparison with the required threshold

We use the elementary divisor inequality d_4(k)^2<=d_16(k).
Both sides are multiplicative. At p^e, d_j(p^e)=binom(e+j-1,j-1).
The ratio d_16(p^e)/d_4(p^e)^2 starts at 1 and its ratio from
e to e+1 is
(e+16)(e+1)/(e+4)^2>=1, since the numerator exceeds the
denominator by 9e. This proves the inequality for every k.
Writing H_Z=sum_(n<=Z)1/n<=1+log Z, ordered factorization gives

\[
 \sum_{k\le Z}\frac{d_4(k)^2}{k}\le H_Z^{16},\qquad
 \sum_{k\le Z}d_4(k)^2\le Z H_Z^{15}.                     \tag{11}
\]

For the first inequality, expand d_16 and relax the product cutoff
to sixteen independent cutoffs n_i<=Z. For the second, sum first
over fifteen factors; the number of choices of the last is at
most Z divided by their product, and then relax those cutoffs.

Equations (7), (8), (11), and |D|<=B prove

\[
 \mathscr D_d\le C X(1+\log Z_*)^{16},\qquad
 |\mathscr J_d-\mathscr D_d|
       \le C Z_*(1+\log Z_*)^{16},
\]
\[
 \mathscr J_d\le C(X+Z_*)(1+\log Z_*)^{16}
       =O(XR q^{16})=O(X^{251/250}q^{16}).                 \tag{12}
\]

Here Z_*=N_*^2R=O(XR), R<=X^(1/250), and log Z_*=O(q).
This proves (1)'s I_V bound. C019t's full transfer gives
|sqrt(I_P)-sqrt(I_V)|=o(sqrt X). Squaring the triangle bound
gives I_P<=2I_V+o(X), proving the remaining assertion in (1).

This differs from C019s's unsuccessful termwise sixteen-channel
estimate: the complete real product is bounded before expansion,
and the grouped frequencies are exact integers with paid coefficient
variation. Nevertheless (12) loses both the signed divisor
cancellation in (7) and the distinction between the length Z_*
and the integration length X. Neither (8)'s diagonal nor its
variation budget is paid at O(X). Moreover they are sufficient
for the stronger norm (3), not necessary for the original moment.

The relevant ready source comparison is assessment1402. Its inspected
BBLR arXiv:1609.02539v1 Theorems 1.1--1.2 concern ordinary shifted
zeta fourth moments, not this moving finite norm; no such formula
has been invoked. The proof above uses only elementary finite
products, integration by parts, harmonic sums and the already local
C019m/p/s/t inputs. The explicit calculations are needed to handle
the moving entries and heat coefficients, rather than reproving a
known source conclusion as a discovery. There is no infinite
coefficient identity at the critical line or exchange of limits.

## Mathlib

Full matching coverage is unchecked. Finite Dirichlet convolution,
integration by parts, total variation and the elementary weighted
square inequality support this argument; they are not a claimed
formalization of the exact moving-heat quartic or M2. No absence
claim is made.
