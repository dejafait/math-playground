# Lemma 771: an explicit all-order full-theta smoothing threshold

## Hypotheses

Let r>=2 be an integer. For v>=0 use L019's exact kernel and first
summand, with the following normalization:

\[
 x(v)=\pi e^{2v},\quad H(v)=8\pi e^{5v/2-x(v)},\quad
 B(v)=H(v)(x(v)-3/2),\quad F_0(v)=H(v)x(v),
\]
\[
 K(v)=H(v)\sum_{n\ge1}n^2 e^{-(n^2-1)x(v)}(n^2x(v)-3/2).
\]

For an integer m>=2r-1, u>=0 and F in {F_0,B,K}, define

\[
 C_m(F;u)=\frac1{(m-1)!}\int_0^\infty t^{m-1}F(u+t)\,dt,
 \qquad S_{r,m}(F;u)=(-1)^{r(r-1)/2}
          \det[\partial_u^{i+j}C_m(F;u)]_{i,j=0}^{r-1}.
\]

The derivatives at u=0 may be read as right derivatives. All
logarithms below are natural. Define the following explicit positive
integers, depending only on r:

\[
\begin{aligned}
 Q&=3r!,& H_*&=2^rQ,& C&=r!H_*^r,\\
 R&=6Q(3r)^{r-1}(4r)^{2r-2}4^r(2r)!,
   &J&=r!(H_*+R)^r,\\
 F_*&=16r!r(H_*+1)^{r-1},\\
 A&=4r^2C+4RF_*,&U&=2r+1,\\
 D&=4U+1,&P&=D(1+DUA),\\
 M(r)&=\max\{2r-1,\ r+2A[UA+(r-1)P+16r(C+J+1)]\}.
\end{aligned}                                                    \tag{1}
\]

Thus M(r) is computable using integer arithmetic alone. There is
no asserted optimality or useful numerical size. The intentionally
coarse integer choices avoid any numerical logarithm or ceiling test.

## Conclusion

For every integer m>=M(r) and every real u>=0,

\[
 S_{r,m}(B;u)\ge\frac{11}{16}S_{r,m}(F_0;u)>0,\qquad
 |S_{r,m}(K;u)-S_{r,m}(B;u)|<\frac18 S_{r,m}(F_0;u),       \tag{2}
\]
and hence
\[
 \frac{|S_{r,m}(K;u)-S_{r,m}(B;u)|}{S_{r,m}(B;u)}
       <\frac2{11}<\frac12.                              \tag{3}
\]

The step406 conceptual audit accepts (2)–(3) as stated; the step403
proof and its constants required no repair. This is not an RH
candidate. It concerns eventual smoothing for each finite
order; it gives neither exceptional coefficient signs nor unshifted
Jensen hyperbolicity. The onset may grow rapidly with r. To obtain
the same conclusion simultaneously at all orders 2<=s<=r, take the
finite maximum of M(s); no monotonicity of the displayed M is assumed.

The comparison method has known precedent in John Nuttall,
*Cumulants, the Riemann Hypothesis, and Similar Problems*, author
manuscript, Sections4.2–4.3, pp.9–12, and Theorem5.6/(5.61)–(5.73),
pp.17–19, https://publish.uwo.ca/~jnuttall/cumanal_a.pdf.
That theorem treats a different Theta1 kernel and supplies no matching
effective full-B threshold. Nuttall's *Basic Wronskians in the Riemann
Hypothesis*, October2012, Theorem3.1/(3.1)–(3.12), pp.5–6,
https://publish.uwo.ca/~jnuttall/basicRH.pdf, gives an unsmoothed
single-variable polynomial formula. The step402 source comparison
found no matching effective statement in the inspected sources;
this is not a claim of originality or independent source-proof review.

The proof below develops the audited fixed-order method of L769/L770.
It does not assume either result outside order four, nor reprove the
source's closed-form polynomial theorem. The elementary determinant
and recurrence calculations are necessary to handle arbitrary-order
multivariable and confluent configurations with the original C_m
factorials. No conjectured full-base sign or numerical zero pattern is
an input. Only L019 supplies a mathematical input from the notebook;
the cited fixed-order lemmas and source theorems are method comparisons.

## Proof

### 1. Signed integral and positive reference

Put d=r(r-1)/2 and p=m-r. Every fixed derivative of B and F_0 is
H times a polynomial in x. Every fixed derivative of an nth summand
of K is e^(5v/2-n^2*x(v)) times a fixed polynomial in n and x(v).
On compact v-intervals in [0,infinity), the derivative series is
uniformly absolutely convergent since x>=pi. For large v, splitting
the exponential absorbs every fixed polynomial in n and x, leaving
a constant times a power of e^v times e^(-x(v)/2), which is
integrable with any fixed polynomial weight in v. These estimates
justify termwise differentiation, differentiation under the shifted
integral on compact u-intervals, and the integrations by parts below,
including u=0. They also prove absolute convergence of the finite
determinant expansions and Fubini operations used here.

For 0<=i,j<=r-1, differentiating and integrating by parts i times
gives
\[
 \partial_u^{i+j}C_m(F;u)=
 \frac{(-1)^i}{(m-1-i)!}
       \int_0^\infty t^{m-1-i}F^{(j)}(u+t)\,dt.            \tag{4}
\]
All boundary terms at infinity vanish by the stated decay. At zero
the boundary powers are positive; in particular the final exponent
is at least m-r>=r-1>=1. Expanding two determinants and permuting
the integration variables proves the determinant integration identity:
the determinant of integrals equals 1/r! times the integral of the
two evaluation determinants. No infinite determinant identity is
used. Reversing the descending-power rows in
det[t_l^(m-1-i)] gives the sign (-1)^d and the factor
prod_l t_l^p Delta(t), where Delta(z)=prod_(i<j)(z_j-z_i).
This cancels the row-sign product (-1)^d in (4). Restricting the
symmetric integrand to the ordered chamber cancels 1/r!. Thus
\[
 S_{r,m}(F;u)=\frac{(-1)^d}{\prod_{i=0}^{r-1}(m-1-i)!}
  \int_{0<t_1<\cdots<t_r}
  \left(\prod_l t_l^p\right)\Delta(t)
  \det[F^{(j)}(u+t_l)]_{j,l}\,dt.                         \tag{5}
\]

Let T=x*d/dx-x and set
\[
 q_j(x)=T^j(x-3/2),\qquad p_j(x)=T^j x,\qquad 0\le j<r.
\]
Differentiation of H(v)a(x(v)) gives H(v)(5/2+2T)a. A triangular
row change therefore expresses the B derivative determinant as
2^d prod_l H_l det[q_j(x_l)], where x_l=x(u+t_l), H_l=H(u+t_l).
For F_0 replace q_j by p_j. The polynomial p_j/x has degree j
and leading coefficient (-1)^j, so
\[
 \det[p_j(x_l)]=(-1)^d\Delta(x)\prod_lx_l.                 \tag{6}
\]
For K the corresponding polynomials are replaced by
\[
 f_j(x)=\sum_{n\ge1}n^2 e^{-(n^2-1)x}q_j(n^2x).           \tag{7}
\]
Indeed T_x[e^(-(n^2-1)x)q_j(n^2x)]
=e^(-(n^2-1)x)q_(j+1)(n^2x). Thus the same triangular change
gives 2^d prod_l H_l det[f_j(x_l)].

Define on the ordered chamber
\[
 W=\left(\prod_l t_l^p H_l\right)\Delta(t),\qquad
 Z=\int W\Delta(x)\prod_l x_l\,dt.
\]
The integral Z is finite by the decay above and strictly positive,
since its integrand is positive on the open chamber. Let nu be the
probability measure obtained by dividing this integrand by Z. Then
S_(r,m)(F_0;u)=2^d Z/prod_i(m-1-i)!>0.

Set y_l=1/x_l, and on 0<y<=1/3 define
\[
 h_j(y)=y^r q_j(1/y),\qquad
 b_j(y)=\sum_{n\ge2}n^2 e^{-(n^2-1)/y}y^r q_j(n^2/y).
\]
The functions h_j are polynomials. Section3 proves that b_j extend
by zero to C^(r-1) functions at y=0. Since
\[
 \Delta(x)\prod_lx_l=(-1)^d\Delta(y)\prod_l y_l^{-r},
\]
the two signed ratios in (5) become
\[
 G_B(y)=\frac{\det[h_j(y_l)]}{\Delta(y)},\qquad
 G_K(y)=\frac{\det[(h_j+b_j)(y_l)]}{\Delta(y)}.
\]
Consequently the exact expectation identities are
\[
 \frac{S_{r,m}(B;u)}{S_{r,m}(F_0;u)}=\mathbb E_\nu G_B,
 \qquad
 \frac{S_{r,m}(K;u)-S_{r,m}(B;u)}{S_{r,m}(F_0;u)}
                         =\mathbb E_\nu(G_K-G_B).          \tag{8}
\]
Both signs (-1)^d have been retained; no even-order restriction is
implicit. Nodes in the chamber are distinct. All bounds below are
uniform as they coalesce, so no minimum separation is assumed.

### 2. An arbitrary-order signed base bound

If a polynomial of degree at most j+1 has coefficient absolute sum
Q_j, then T applied to it has coefficient absolute sum at most
(j+2)Q_j. Starting at ||x-3/2||_1=5/2 gives
\[
 \|q_j\|_1\le(5/2)(j+1)!\le Q=3r!\quad(0\le j<r).        \tag{9}
\]
The degree of q_j is j+1 and its leading coefficient is (-1)^j.
Thus h_j has degree at most r, least occurring degree r-j-1, and
coefficient (-1)^j at that least degree. Its coefficient norm is
also bounded by Q. For every 0<=k<=r and 0<=y<=1/3,
\[
 |h_j^{(k)}(y)|/k!\le2^rQ=H_*;                           \tag{10}
\]
this follows monomial by monomial from binom(a,k)<=2^r and y<=1.

For any distinct real nodes in [0,b], b<=1/3, Newton interpolation
replaces an evaluation determinant divided by Delta(y) by the
determinant whose column k is the vector of divided differences
g_j[y_1,...,y_(k+1)], for k=0,...,r-1. To see the normalization,
the Newton polynomials prod_(i=1)^k(y-y_i) have a triangular
evaluation matrix with determinant Delta(y). Repeated Rolle applied
to a function minus its interpolation polynomial gives
\[
 g[y_1,\ldots,y_{k+1}]=g^{(k)}(\xi)/k!
\]
for some xi between the nodes (k=0 is evaluation). This both bounds
the entries by sup |g^(k)|/k! and controls arbitrarily close nodes.
For h_j, (10) and the mean-value theorem therefore give
\[
 \left|h_j[y_1,\ldots,y_{k+1}]-h_j^{(k)}(0)/k!\right|
                \le b(k+1)H_*\le brH_*.                 \tag{11}
\]
Every entry of both matrices is at most H_* in absolute value.

Let A0 have entries h_j^(k)(0)/k!. Reversing its r rows makes it
upper triangular, with diagonal entries (-1)^(r-1-k), k=0,...,r-1.
The row reversal and diagonal product each have sign (-1)^d.
Hence det A0=1. Expanding determinants by permutations gives the
global bound |G_B|<=C. Telescoping the r columns between the
divided-difference matrix and A0, and using (11) in the changed
column, gives
\[
 |G_B(y)-1|\le r\,r!\,(brH_*)H_*^{r-1}=br^2C.            \tag{12}
\]
In particular,
\[
 |G_B|\le C\quad(x_l\ge\pi),\qquad
 G_B\ge3/4\quad(\min_l x_l\ge A),                        \tag{13}
\]
because A>=4r^2C. No sign is imposed on the complementary region.
This avoids requiring an unsmoothed full-base sign at every height.

### 3. Full-series reciprocal derivatives and the confluent error

For 0<=b<=r, a=n^2-1 and 0<=k<=r-1, differentiate
y^b e^(-a/y). Removing the exponential leaves
\[
 \sum_{l=0}^k c_{k,l}(b)a^l y^{b-k-l},\quad
 c_{0,0}=1,\quad
 c_{k+1,l}=(b-k-l)c_{k,l}+c_{k,l-1},                     \tag{14}
\]
with missing coefficients zero. In each step used here
|b-k-l|<=2r. Thus the coefficient absolute sum is at most
(2r+1)^k<=(3r)^k. For 0<y<=1/3, x=1/y, every power
y^(b-k-l) is at most x^(2r-2) in absolute value; also
a^l<=n^(2r-2). Combining (9) with the extra n^(2d+2)
from a degree-d term of q_j gives
\[
 |b_j^{(k)}(y)|\le Q(3r)^{r-1}x^{2r-2}
        \sum_{n\ge2} n^{4r}e^{-(n^2-1)x}.               \tag{15}
\]

Write L=2r-2. Maximizing x^L e^(-a*x/2) on x>0 gives
(2L/(ae))^L<=(4r)^L for a>=3. In the remaining exponential
split a second time and use x>=3:
\[
 n^{4r}e^{-a x/4}\le n^{4r}e^{-3(n^2-1)/4}
 \le e^{3/4}(4/3)^{2r}(2r)!<3\,4^r(2r)!.               \tag{16}
\]
The middle bound is the single positive term of degree 2r in
the series for exp(3n^2/4). The last uses e<3. The remaining
series sum_(n>=2)e^(-(n^2-1)x/4) is at most
2e^(-3x/4), because consecutive terms have ratio at most
e^(-15/4)<1/2, using e>2. Thus the explicit R of (1) gives
\[
 |b_j^{(k)}(y)|\le R e^{-3x/4},\qquad
       x=1/y\ge3,\quad 0\le k<r.                       \tag{17}
\]

These differentiations of the series are justified, rather than
formal. Before the second split, each summand and its derivatives
through order r-1 are bounded uniformly for x>=3 by a constant
depending on r times n^(4r)e^(-3(n^2-1)/2), a summable sequence.
Every individual summand and each such derivative tends to zero as
y decreases to zero. Uniform convergence, applied successively to
the functions and derivatives, gives the claimed C^(r-1) extension
with all these derivatives zero at the endpoint. Estimate (17)
continues there. No finite theta truncation has been used.

For nodes in an interval where all these derivatives are bounded by
R0, the Newton columns for b_j are bounded by R0 (division by k!
only improves the bound). Expanding by the nonempty sets of changed
columns gives
\[
 |G_K-G_B|\le r!\sum_{k=1}^r\binom rk H_*^{r-k}R0^k
              =r!\bigl((H_*+R0)^r-H_*^r\bigr).           \tag{18}
\]
Consequently |G_K-G_B|<=J globally. If all x_l>=A, their
reciprocal nodes lie in [0,1/A], so (17) allows
\[
 R0=R e^{-3A/4}<1/F_*\le1.
\]
Indeed A>=4RF_* and exp(3RF_*)>RF_*.
Using (H_*+R0)^r-H_*^r<=rR0(H_*+1)^(r-1) in (18) gives
\[
 |G_K-G_B|<1/16\quad(\min_lx_l\ge A),\qquad
 |G_K-G_B|\le J\quad(x_l\ge\pi).                         \tag{19}
\]
These are bounds on the determinant quotient itself, not entrywise
errors divided by an unbounded inverse separation.

### 4. Uniform payment of every low-coordinate configuration

Put x0=pi*exp(2u)>=pi>3. Changing variables
t_l=(1/2)log(x_l/x0) in nu gives, up to a positive normalizing
constant, the density
\[
 \prod_{l=1}^r\bigl[\log(x_l/x0)^p x_l^{5/4}e^{-x_l}\bigr]
 \prod_{i<j}(\log x_j-\log x_i)(x_j-x_i),\quad x_l\ge x0. \tag{20}
\]
In fact H_l*x_l*dt_l=H_l*dx_l/2 and H_l is a positive
constant times x_l^(5/4)e^(-x_l); Delta(t)=2^(-d)Delta(log x).
The omitted constants cancel on normalization. The displayed density
is symmetric and nonnegative on the unordered region. Its total
integral is finite and positive. Passing from the chamber to this
region does not change the probability of a symmetric event.

Let delta=nu{min_l x_l<=A}. If x0>=A, delta=0; boundary
sets have measure zero. Otherwise fix arbitrary other coordinates
a_1,...,a_(r-1)>=x0. The unnormalized density of the remaining
coordinate is
\[
 \phi(x)=\log(x/x0)^p x^{5/4}e^{-x}
       \prod_{i=1}^{r-1}|x-a_i|\,|\log x-\log a_i|,
       \qquad x\ge x0.                                 \tag{21}
\]
It has a positive finite integral for every such fixed tuple.
Among the r intervals [2kA,(2k+1)A], k=1,...,r, choose one I
whose distance from every a_i is at least A/4. This is possible
because their closed A/4 enlargements are pairwise disjoint and
there are only r-1 conditioning coordinates. The interval I has
length A, lies above x0, and has z<=UA for z in I.

For x in [x0,A] and z in I,
\[
 \frac{|x-a_i|}{|z-a_i|}\le1+4U=D.                       \tag{22}
\]
Also |log z-log a_i|>=1/D. If a_i>=z, use
log(a_i/z)>=log(1+1/(4U))>=1/(4U+1); if a_i<z, use
-log(1-(z-a_i)/z)>=(z-a_i)/z>=1/(4U).
The triangle inequality and x>=x0>3 now give
\[
 \frac{|\log x-\log a_i|}{|\log z-\log a_i|}
       \le1+D\log(UA/3)\le1+DUA,                       \tag{23}
\]
so each pair of factors costs at most the integer P of (1).
With L0=log(A/x0)>0, put q=log(A/3)/(log(A/3)+log2), which
satisfies 0<q<1 since A>=4. Then
\[
 \frac{\log(x/x0)}{\log(z/x0)}
 \le\frac{L0}{L0+\log2}
 \le\frac{\log(A/3)}{\log(A/3)+\log2}=q.                 \tag{24}
\]
Further, x^(5/4)<=z^(5/4) and e^(z-x)<=e^(UA). Combining
(22)–(24) yields
\[
 \phi(x)\le P^{r-1}e^{UA}q^p\phi(z).                    \tag{25}
\]
Integrate first over z in I (length A) and then over x in
[x0,A] (length at most A). This bounds the low-coordinate
integral by P^(r-1)e^(UA)q^p times the full one. Multiplying
by the nonnegative factors involving only the other coordinates
in (20) and applying Tonelli proves the same marginal probability
bound. This argument also covers coincident conditioning coordinates,
whose other-coordinate density is zero. No measurable selection of
I or independence assumption is needed: the final integral inequality
is the same for every tuple. The union bound gives
\[
 \delta\le rP^{r-1}e^{UA}q^{m-r}.                        \tag{26}
\]
It includes mixed small/large configurations and unbounded other
coordinates. All constants are independent of x0 and therefore of u.

### 5. Explicit onset, integrated sign and relative comparison

The elementary inequalities log2>1/2 (from e<3<4) and
log(2A/3)<A show
\[
 1-q=\frac{\log2}{\log(2A/3)}>\frac1{2A},\qquad
 q^p\le e^{-p/(2A)}.
\]
Set V=16r(C+J+1). For m>=M(r), (1) gives
p=m-r>=2A[UA+(r-1)P+V]. Since log P<=P and exp(V)>V,
(26) implies
\[
 \delta\le r\exp((r-1)(\log P-P)-V)
       \le r e^{-V}<r/V=\frac1{16(C+J+1)}.
\]
In particular,
\[
 \delta\le\frac1{16(C+J+1)}.                            \tag{27}
\]
Using (13) on the high region and G_B>=-C on its complement,
\[
 \mathbb E_\nu G_B
 \ge\tfrac34(1-\delta)-C\delta
 =\tfrac34-(C+\tfrac34)\delta\ge\tfrac{11}{16}.          \tag{28}
\]
This explicitly pays any negative base contribution instead of
discarding it. Equations (19) and (27) similarly give
\[
 |\mathbb E_\nu(G_K-G_B)|
 \le\mathbb E_\nu|G_K-G_B|
 \le\tfrac1{16}+J\delta<\tfrac18.                        \tag{29}
\]
Combining (8), (28) and (29) proves (2)–(3). The estimates hold
for every integer above the explicit threshold, every real u>=0
and every fixed integer r>=2, without a limiting exchange between
r, m and u. The low-height full-B sign is not assumed; the
complete-series derivatives and coalescing-node costs were paid
before dividing by the integrated base.

### Verification and scope of acceptance

The proof of the universal quantifiers is the analytic argument
above. The finite exact check
`python3 scripts/cumulant-comparison/all-order-normalization-403.py`
tests r=2,...,7, including odd d, for the recurrence coefficient
bound, the confluent determinant one, the signed leading determinant,
and the reciprocal ratio identity at distinct rational nodes. Its
full certificate is
`scripts/cumulant-comparison/all-order-normalization-403.json`.
It does not establish the all-order estimates or replace the
separate analytic audit recorded below. No numerical estimate of an
infinite determinant, smoothing onset or beta root is used.

The elementary standard inputs proved or explained where used are
finite determinant expansion, Newton interpolation, repeated Rolle,
Tonelli/Fubini with the supplied domination, and the exponential
series and elementary calculus. The elementary constants 2<e<3
follow from that series, and pi>3 suffices throughout. No unreviewed
paper theorem supplies a sign. The result is local development of
an established method; novelty beyond the inspected sources has not
been certified. Exceptional coefficients, the unsmoothed signs and
the main RH gap remain unresolved.

### Separate conceptual audit — step406, 2026-11-04

The audit checked the entire proof for every integer r>=2, integer
m>=M(r), and real u>=0. It accepts the stated inequalities without
changing their hypotheses, constants or direct notebook input L019.
This is verification of the existing local result, not a further
theorem, a new literature discovery or a formal proof certificate.

In (4)–(8), the row signs from integration by parts and from reversing
the powers each contribute (-1)^d. The sign in the definition of S
remains in (5) and is then canceled by the reciprocal Vandermonde.
The product of the original factorials remains unchanged. The last
power at the origin is p=m-r>=r-1>=1, so every integration boundary
term vanishes. The complete-K derivative series is locally normally
convergent, and its polynomial factors are absorbed by the double
exponential at infinity before any integral or derivative is
interchanged. The positive reference mass Z is finite and nonzero
for each u, even when u is arbitrarily large; no uniform lower bound
on Z is required for the exact normalized identity (8).

In (9)–(12), the reversed coefficient matrix is upper triangular
with diagonal product (-1)^d. Reversing back therefore gives
det A0=1 for both parities. The divided-difference mean-value formula
holds for nodes in either order; their reciprocal reversal introduces
no further sign. The derivative of h_j^(k)/k! is bounded by
(k+1)H_*, including k=r-1, since (10) includes derivative r.
Thus the column telescoping costs exactly br^2 C, uniformly near
all confluent configurations.

For (14)–(17), a degree-a0 monomial of q_j contributes
n^(2a0+2)y^(r-a0)exp(-(n^2-1)/y), with 0<=a0<=r.
After k<=r-1 derivatives, the reciprocal power costs at most
x^(2r-2) and the additional n power at most n^(2r-2).
This gives n^(4r), as required in (15). Splitting the exponential
into halves and then quarters gives exactly the displayed R.
Before the second split the derivative of each summand is bounded
on 0<y<=1/3 by
Q(3r)^(r-1)(4r)^(2r-2)n^(4r)exp(-3(n^2-1)/2).
This summable majorant applies through order r-1. Each summand
extends smoothly with those derivatives zero at y=0; uniform
convergence of the derivatives therefore supplies the claimed
C^(r-1) extension. In (18), all nonempty changed-column sets are
paid in absolute value. A>=4RF_* gives R0<1/F_*, so the high-region
error is strictly below 1/16; no signed cancellation is assumed.

For (20)–(26), the Jacobian leaves x^(5/4), not x^(9/4).
The r enlarged candidate intervals are pairwise disjoint, so r-1
arbitrary conditioning points leave one free. Its distance bound
gives (22). For a>=z the logarithmic gap is at least
log(1+1/(4U))>=1/(4U+1); for a<z it is at least 1/(4U).
This checks (23) even for unbounded conditioning coordinates.
The low interval has length at most the free interval's length A,
which justifies integrating (25) without a lost length factor.
The conditional integral inequality is uniform in the fixed tuple;
Tonelli needs no measurable choice of free interval. The zero-density
coincidences, the case x0>=A and the endpoint u=0 are all included.

Finally, log(2A/3)<A and log2>1/2 yield the stated q cutoff.
For every m>=M(r), not just the threshold, p is at least
2A[UA+(r-1)P+V]. Consequently delta<1/[16(C+J+1)].
The possibly negative low-region contribution is bounded below by
-C delta in (28); it is never omitted. Equations (28)–(29) give
the required 11/16 and strict 1/8 bounds, hence strict 2/11 in (3).
No interchange of the r, m and u limits is present or needed.

The finite script was replayed: 30 exact checks at r=2,...,7 passed
with no failures, preserving the certificate path above. These
checks confirm algebra only; the preceding audit of the full
analytic argument establishes the universal scope claimed here.
The separate coefficient restriction k>=r-1+ceil(m/2) in the
assessed source transfer is unchanged. Nothing in this audit signs
its exceptional indices, unsmoothed determinants or Xi itself.

## Mathlib

Full matching coverage of this effective full-theta statement was
not checked. Supporting divided differences, determinant integration,
and parameter-uniform measure estimates were not checked in Mathlib;
availability is unknown, not established absent. This is an informal
proof with a limited exact algebra check, not a formal verification.
