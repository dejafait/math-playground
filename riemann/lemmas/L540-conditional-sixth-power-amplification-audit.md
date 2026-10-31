# L540 — Conditional sixth-power amplification audit

## Hypotheses

Work in O=Z[omega], omega=exp(2 pi i/3), with ideal norms q and element
norm q_u=|u|^2. Fix a finite set S containing the primes above 6 and the
full defining-modulus support of a fixed finite-order ray character nu.
Ideal sums are over nonzero integral ideals outside S, with their unique
primary generators. Element rows retain all units and may meet S.
Use the ideal Mobius function mu and the zero-extended sextic symbols of
L539. Fix one common orientation e in {1,-1}; the negative orientation
means conjugation with the original zeros, not division at a zero. Set

\[
 \psi_u(n)=\nu(n)\chi_n(u)^e,\qquad
 M_u(X;V)=X^{-1/2}\sum_n\mu(n)\psi_u(n)V(q_n/X),\quad X>0.       \tag{1}
\]

Assume L539 with no slots, including its inherited L538 arithmetic,
support, source-witness, fibre/count, principal/tail and adjustable-
uniformity contracts. In particular its conclusion is uniform over the
bounded length ranges and fixed row-ball constants below, with finite
smooth-seminorm and fixed polynomial norm-twist height costs. Thresholds
are uniform in heights apart from those explicit costs. This assumption
includes the fixed-support derivative profiles used below, and compact
real norm twists. It does not assume a raw scale supremum, amplification,
or a bound for independently chosen row tests.

Retain the following primitive counting estimates as explicit contracts,
with constants independent of the indicated scale:

\[
\begin{split}
 \#\{n:q_n\le X\}&\le C X &&(X\ge1),\\
 \#\{u\in O:0<q_u\le X\}&\le C X &&(X\ge1),\\
 \#\{a:(a,S)=1,\ q_a\le P\}&\ge c_S P &&(P\ge1),\\
 d_O(a)&\le C_\delta q_a^\delta &&(\delta>0).
\end{split}                                                        \tag{2}
\]

Here d_O counts ideal divisors, c_S>0 depends on the fixed S, and the
third line counts all good ideals, not just primes or squarefree ideals.
The unit ideal is included. We do not audit these primitive estimates.
Unique ideal factorization, the primary representative convention and
the zero-extended multiplicative definition of the sextic symbol are
the arithmetic setting, not additional moment estimates.

Fix a smooth complex test W supported in [a,b] contained in (0,infinity),
enlarging b to at least 1 if necessary. Fix 0<C_-<=C_+<infinity. For
U,D>=1 the row set consists of elements with C_- U<=q_u<=C_+ U and
0<=v_p((u))<=5 for every prime ideal p, including those in S. Any subset
of these rows is also allowed. All constants may depend on this fixed
datum, the specified positive losses and finitely many test seminorms.

## Conclusion

For every fixed c>0 and epsilon>0, put

\[
 H=\max(2U,D^{1+c}),\qquad P=(H/U)^{1/6}.
\]

Under the hypotheses,

\[
 \sum_u|M_u(D;W)|^2
 \ll \frac HP(UD)^\epsilon
 \ll\max\{U,U^{1/6}D^{5(1+c)/6}\}(UD)^\epsilon.             \tag{3}
\]

For any fixed R>=0, uniformly over 0<=r<=R and D=U^r,

\[
 \sum_u|M_u(U^r;W)|^2\ll U^{e(r)+\epsilon},\qquad
 e(r)=\max\{1,(1+5r)/6\}.                                  \tag{4}
\]

Both statements allow the test W(y)y^(-sigma_u+i t_u) separately in each
row, with sigma_u in a fixed compact real interval and |t_u|<=T_1,
T_1>=0. The extra factor is (1+T_1)^A for one finite A fixed before
T_1,U,D and the choices of row parameters. It may depend on c and the
loss in (3), or on R and the loss in (4). There is no endpoint assertion
at c=0 and no arbitrary row-dependent prime or column coefficient.

This verifies a source-claimed interface conditionally; it neither
establishes a new estimate beyond that source nor audits its primitive
arithmetic. In particular it can replace the amplification contract in
L534 only under the present retained inputs. Other moment families,
full external import closure and actual-Xi positivity are unresolved.

## Proof

The primary source is OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, September 30, 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[pinned build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
The exact assertion is `lem:inverse-amplification`; its full proof and
qualification are at retrieval lines 11664–11788. The arithmetic
conventions are 520–588. We import `lem:smooth-calculus`, specifically
`eq:parameter-sobolev` (1056–1066, proof 1141–1154): for a unit box I
in R^d and F smooth on its fixed enlargement,

\[
 \sup_I|F|^2\le C_d\sum_{\alpha\in\{0,1\}^d}
       \int_{I+[-1,1]^d}|\partial^\alpha F|^2.             \tag{5}
\]

This elementary calculus input is used with its exact domain below.
L539 supplies the marked conclusion conditionally; neither the source's
`eq:raw-moment` nor `lem:inverse-amplification` is an assumed estimate.
Reproduction is necessary to verify this application interface in the
qualified external manuscript, rather than citing the conclusion whose
applicability is being checked. The saved SPECIALIZE assessment supplies
the prior literature comparison; generic arbitrary-coefficient sextic
operator norms are not substitutes for (1)'s fixed Mobius vector.

### All-row raw bound and all positive scales

For K>=2, X>=1 and K>=X^(1+c), apply L539 with base Z=K, m=1, no
slots and r=log_K X. Then

\[
 0\le r\le\frac1{1+c},\quad
 1-r\ge\frac c{1+c},\quad 3-2r\ge3-\frac2{1+c}>0.         \tag{6}
\]

These are fixed positive margins on a bounded range. Thus for every
rho>0 and fixed C_row, including the permitted derivatives of V,

\[
 \sum_{0<q_v\le C_{\rm row}K}|M_v(X;V)|^2
       \ll K^{1+\rho}\le K(KX)^\rho.                    \tag{7}
\]

This includes r=0: L539 requires no positive lower column length.
The source's separate short-column branch is also valid: (2) gives
|M_v(X;V)|<=C_V sqrt(X) for X>=1, and hence a squared row sum O(KX).
If X<=K^(rho/4) this is at most O(K^(1+rho/4)). Bounded 1<=K<2
with K>=X^(1+c) has bounded X and is handled by the same direct count.
No missing lower-length interval is hidden in (7).

We now establish, for H>=max(2,D^(1+c)) and D>=1,

\[
 \sum_{0<q_v\le C H}\sup_{0<X\le D}|M_v(X;V)|^2
       \ll H(HD)^\kappa \quad(\kappa>0),                 \tag{8}
\]

where V has the fixed support [a,b]. If X<1/b the sum is empty. For
1/b<=X<=1 it contains only ideals with q_n<=b, and X^(-1/2)<=sqrt(b).
Consequently both |M_v(X;V)| and the analogous expression for any
fixed derivative test are uniformly bounded, giving a squared all-row
bound O(H) by (2). This covers all small nonempty scales.

Write s=log X. At fixed row v, local finiteness of the annular sum gives

\[
 \frac{d}{ds}M_v(e^s;V)=M_v(e^s;TV),\qquad
 TV(y)=-V(y)/2-yV'(y).                                   \tag{9}
\]

Cover [-log b,log D] by integer unit intervals. There are
O_b(log(2+D)) of them, and their enlargements in (5) have
e^s<=e^2D. Set K=e^(2(1+c)) H. For all enlarged scales with e^s>=1,
K>=(e^s)^(1+c), so (7) applies to V and TV with loss rho=kappa/2.
The old row set is contained in the fixed ball q_v<=C K. Since K/H
is fixed and e^s<=e^2D, the integrands summed over rows are bounded
by C H(HD)^rho. Enlarged scales below 1 use the preceding direct
bound or are empty. Applying (5) in dimension one, summing its
nonnegative row expressions before integrating in s, and summing the
intervals bounds the left side of (8) by

\[
 C H(HD)^{\kappa/2}\log(2+D)\le C_\kappa H(HD)^\kappa.
\]

Every interval and integration measure here is common to all rows.
The suprema below 1/b are zero. Derivatives do not enlarge the annular
support and use finitely many additional smooth seminorms. Polynomial
norm-twist dependence is preserved by (9); all scale and parameter
orders are fixed once the final loss and compact ranges are fixed.

### Multiplier identity with every original zero

Fix any good ideal a, using its primary generator in ua^6. For each
squarefree n there is a unique factorization n=dm with
d|rad(a) and (m,a)=1: d is the product of the primes of n dividing a.
Then (d,m)=1, mu(n)=mu(d)mu(m), and psi_u(n)=psi_u(d)psi_u(m).
For every ideal m, including nonsquarefree ones,

\[
 \psi_{ua^6}(m)=\psi_u(m)1_{(m,a)=1}.                    \tag{10}
\]

Indeed, if a prime divisor of m divides u or a, the corresponding
original local zero makes both sides zero. Otherwise each local
sextic value on a is a sixth root of unity, so its sixth power is
one. This holds for both orientations. In particular (u,a)=1 is
unnecessary, and a six-divisible exponent has not erased a zero.

Inserting the unique split into (1), using (10), and noting
D^(-1/2)=q_d^(-1/2)(D/q_d)^(-1/2), proves the exact identity

\[
 M_u(D;V)=\sum_{d\mid\operatorname{rad}(a)}
          \mu(d)\psi_u(d)q_d^{-1/2}M_{ua^6}(D/q_d;V).     \tag{11}
\]

The terms with d meeting u have zero coefficient. The remaining column
is automatically coprime to a through (10), so d and that column cannot
overlap. All manipulations are finite sums; scales D/q_d below one are
legitimate by (1) and (8). The coefficient mass in (11) satisfies

\[
 \sum_{d\mid\operatorname{rad}(a)}
       |\mu(d)\psi_u(d)|q_d^{-1/2}
 \le 2^{\omega(a)}\le d_O(a)\le C_\delta q_a^\delta.       \tag{12}
\]

Thus for q_a<=P, triangle inequality followed by squaring gives

\[
 |M_u(D;V)|^2\le C_\delta P^{2\delta}
                       \sup_{0<X\le D}|M_{ua^6}(X;V)|^2. \tag{13}
\]

### Supply, element fibres and all losses

Let A(P) be the good ideals of norm at most P. Since P>=2^(1/6)>1,
(2) gives |A(P)|>=c_S P. For bounded P this retains the unit ideal;
large P uses the contracted fixed-S positive-density count. There is
no condition of primality, squarefreeness, or coprimality to u.

The map (u,a) to ua^6 is injective on the pairs under consideration.
For every prime p, an equality of two image elements gives an equality
of valuations

\[
 v_p((u))+6v_p(a)=v_p((u'))+6v_p(a').
\]

Both row valuations lie in {0,1,2,3,4,5}, so reduction modulo six
recovers their equality; division by six then gives v_p(a)=v_p(a').
This includes p in S (where both multiplier valuations are zero).
Unique factorization recovers a=a', and their fixed primary generators
are equal. Cancelling that nonzero generator's sixth power in the
original element equality gives u=u', including its unit. Recovering
only the row ideal would not have sufficed. Moreover
q_(ua^6)=q_u q_a^6<=C_+ U P^6=C_+ H.

Average (13) over A(P), sum over the physical rows, use injectivity,
and then enlarge the nonnegative sum to the whole last ball. Equation
(8) gives

\[
 \sum_u|M_u(D;V)|^2
 \le C_\delta\frac{P^{2\delta}}{P}
       \sum_{0<q_v\le C_+H}\sup_{0<X\le D}|M_v(X;V)|^2
 \ll \frac HP P^{2\delta}(HD)^\kappa.                    \tag{14}
\]

For an explicit loss allocation put L=UD>=1. Since H<=2L^(1+c),
HD<=2L^(2+c) and P^(2delta)=(H/U)^(delta/3)<=C L^(delta(1+c)/3).
Given the desired epsilon in (3), choose

\[
 \kappa=\frac{\epsilon}{4(2+c)},\qquad
 \delta=\frac{3\epsilon}{4(1+c)}.
\]

The extra exponent in (14) is at most epsilon/2, and hence at most
epsilon. Constants from fixed enlargements are scale independent.
Finally

\[
 H/P=U^{1/6}H^{5/6}
     =\max\{2^{5/6}U,U^{1/6}D^{5(1+c)/6}\},              \tag{15}
\]

which proves (3). No multiplication of the common row bound by the
number of original rows or by a second multiplier count has occurred.

For (4), let epsilon be its desired final loss and fix R. Use (3) with

\[
 c=\min\{1,3\epsilon/[10(1+R)]\}>0,\qquad
 \epsilon_0=\epsilon/[4(1+R)].                            \tag{16}
\]

For 0<=r<=R, the exponent of the maximum in (3) differs from e(r)
by at most 5cr/6<=epsilon/4, because the function max(1,x) is
1-Lipschitz. The remaining (UD)^epsilon_0 contributes at most
epsilon/4 to the U exponent. This proves (4) with slack, uniformly
even when r crosses one. The same positive c works throughout the
range; it is not sent to zero after U is chosen. U=1 implies D=1 and
is covered by the bounded case already proved.

### A common integral for separately selected row tests

For fixed sigma,t write
F_u(sigma,t)=M_u(D;W(y)y^(-sigma+i t)). For alpha,beta in {0,1},
local finiteness permits differentiation and gives

\[
 \partial_\sigma^\alpha\partial_t^\beta F_u
 =(-1)^\alpha i^\beta
 M_u\bigl(D;W(y)(\log y)^{\alpha+\beta}y^{-\sigma+i t}\bigr). \tag{17}
\]

There are only the three fixed profiles W(y)(log y)^j, 0<=j<=2.
On any fixed enlargement of the compact sigma interval their supports
remain [a,b]. Their finite Euler seminorms have polynomial growth in
|t|; (9) adds only a fixed derivative and a factor linear in sigma,t.
The uniformity assumed from L539 and preserved in (7)–(14) therefore
provides one finite B such that, for all four derivatives in (17),

\[
 \sum_u|\partial_\sigma^\alpha\partial_t^\beta F_u(\sigma,t)|^2
 \ll \frac HP(UD)^\epsilon(1+|t|)^B.                     \tag{18}
\]

Here (3) is used for each fixed common pair of parameters; no rowwise
estimate has been assumed. Cover the compact sigma interval times
[-T_1,T_1] by O(1+T_1) unit boxes. Apply the imported (5) in dimension
two to each row on each box. Sum over rows before integrating the
four nonnegative squared derivatives. The enlarged boxes stay in a
fixed larger real interval and satisfy |t|<=T_1+2. Their total volume
is O(1+T_1), so (18) gives

\[
 \sum_u\sup_{\sigma\in I,\ |t|\le T_1}|F_u(\sigma,t)|^2
 \ll \frac HP(UD)^\epsilon(1+T_1)^{B+1}.                  \tag{19}
\]

This proves the row-test claim in (3); using (16) proves its (4)
version. Set A=B+1 (or a larger fixed integer). Every row is bounded
through the same boxes and Lebesgue derivative integrals. No Fourier
measure is selected at a row's chosen parameters, and no Minkowski
argument is applied to different row measures. The coefficient vector
in (1) remains unchanged. If a later application sets T_1=Z^tau and
reserves a loss lambda>0 for this factor, it must choose tau>0 only
after A is fixed, with A tau<lambda. Such an external choice is not
part of the present proof of the other application contracts.

## Mathlib

Full matching coverage has not been checked. Finite-sum algebra,
ideal factorization, Cauchy–Schwarz and Sobolev calculus are supporting
facts; none by itself verifies the conditional arithmetic/uniformity
inputs or this complete application. No formal verification or absence
claim is made.
