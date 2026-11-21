# C019v — Signed low-index heat coefficients have bounded mass and variation

## Hypotheses

Use C019u's exact finite coefficients G_k(Y) and
mathcal B_k=sup_D|G_k|+Var_D(G_k), defined there in (4),(7),
with C019p's real Euler-product coefficients alpha of zeta(s)^(-1/2)
on Re(s)>1. Retain all of the following parameters:

\[
 d=\frac{T}{2\pi}(\log(T/(2\pi))-1),\quad T>2\pi e,
 \quad X=T/\sqrt{2d},\quad q=\log X,\quad h=3\pi/q,
\]
\[
 J=[X,\sqrt2X],\quad D=[X,\sqrt2X-h],\quad
 L=\lfloor X^{1/1000}\rfloor,\quad \ell=\log L,
 \quad\omega(n)=1-\log n/\ell\quad(1\le n\le L).
\]

Here ell is the fixed mollifier logarithm, not log(Y/(2*pi)).
As in C019u, set

\[
 t(Z)=Z^2/(2d),\quad u(Z)=\tfrac12\log(Z/(2\pi)),
 \quad c_0=\pi/8,
\]
\[
 E_n(Z)=\exp\{\tfrac14t(Z)((u(Z)-\log n)^2-\pi^2/16)
                    +ic_0t(Z)(u(Z)-\log n)\},
\]

and keep the source floor
N(Z)=floor(sqrt(Z/(2*pi)+Z^2/(32d))). Both shifted factors
use their own time and floor. All conclusions are for sufficiently
large positive integers d, with absolute constants and an existential
common onset. No RH, nonvanishing, random-law, critical-line reciprocal
or ordinary-to-heat moment theorem is assumed.

## Conclusion

For exactly the signed coefficients of C019u,

\[
 \sum_{k\le L}\frac{\mathcal B_k^2}{k}=O(1).                 \tag{1}
\]

Consequently this part of the grouped diagonal and the complete
low-index norm satisfy

\[
 \int_D\sum_{k\le L}\frac{|G_k(Y)|^2}{k}\,dY=O(X),
 \qquad
 \int_D\left|\sum_{k\le L}G_k(Y)k^{-1/2-iY}\right|^2dY=O(X).
                                                               \tag{2}
\]

The difference between the second integral and its diagonal is
O(L(1+log L))=o(X). No bound for the high-index block L<k<=Z_*,
or its interaction with this block, is asserted. Thus the full grouped
norm, the exact real-pair moment I_V, and the actual-Jensen moment
I_P remain unproved at O(X). Failure of this stronger grouped method
would not refute the original real-pair target.

This is a local finite-coefficient development under unchanged ready
assessment1402. It reproduces elementary coefficient-norm methods;
it is not a claimed advance beyond the sources checked. In particular
it imports no mollified fourth-moment theorem. This proof and the
inherited C019s/t/u calculations await independent conceptual audit.

## Proof

### Exact low-index range and eventual constants

For k<=L, every factor in mnr=k and every factor in the fourfold
convolution defining c_r is at most L. Since
N(X)>=floor(sqrt(X/(2*pi))) and L<=X^(1/1000), eventually
L<N(X). Monotonicity of N then makes every entry indicator in
C019u (4) equal to one throughout D. No floor has been approximated
or differentiated. In this range every G_k is smooth on D.

We need numerical bounds on the scale of the heat, rather than just
an unspecified O(q^(-2)). Put z=log(T/(2*pi)). Directly from the
hypotheses,

\[
 d=e^z(z-1),\quad X=\frac{\sqrt2\pi e^{z/2}}{\sqrt{z-1}},
 \quad q=z/2-\tfrac12\log(z-1)+\log(\sqrt2\pi),
\]
\[
 t(Z)=\frac{\pi^2(Z/X)^2}{(z-1)^2}.
\]

Thus q/(z-1)->1/2, uniformly 1<=Z/X<=sqrt2. In particular,
after increasing the absolute onset,

\[
 t(Z)q^2\le10,\quad |u(Z)|\le q,\quad
 \ell\le q/1000,\quad d\asymp X^2q^2.                     \tag{3}
\]

These deliberately loose constants will leave a strict integration
margin. Throughout a Y-derivative, d,X,L,q,h are fixed.

### A signed six-factor coefficient estimate

For a six-vector of complex numbers w=(w_1,...,w_6), define the
entire coefficient function (a finite exponential sum)

\[
 K_k(w)=\sum_{n_1\cdots n_6=k}
       \alpha(n_3)\alpha(n_4)\alpha(n_5)\alpha(n_6)
       \prod_{j=1}^6 n_j^{w_j/\ell}.
                                                               \tag{4}
\]

For a vector a=(a_k)_(k<=L), write
||a||_ell2=(sum_(k<=L)|a_k|^2/k)^(1/2). This subscript denotes
the weighted finite-dimensional norm, not the parameter ell.
We claim that, with r=max_j|w_j|,

\[
 \|K(w)\|_{\ell^2}\le C\exp(r+64r^2),                    \tag{5}
\]

where C is independent of L>=2 and w. The cancellation in (5)
is essential; the absolute d_4 envelope alone grows with log L.

To prove (5), put v_j=w_j-r. Then Re(v_j)<=0, |v_j|<=2r,
and K_k(w)=k^(r/ell)K_k(v). Since k<=L, the multiplier is
at most e^r. For fixed v the coefficients K_k(v) are multiplicative.
Their prime-power generating function, as a formal power series, is

\[
 \sum_{e\ge0}K_{p^e}(v)x^e
 =\prod_{j=1}^2(1-p^{v_j/\ell}x)^{-1}
       \prod_{j=3}^6(1-p^{v_j/\ell}x)^{1/2}.              \tag{6}
\]

At v=0 the right side is exactly 1. In particular its prime
coefficient has the cancellation

\[
 K_p(v)=p^{v_1/\ell}+p^{v_2/\ell}
                  -\tfrac12\sum_{j=3}^6p^{v_j/\ell},
 \qquad |K_p(v)|\le 8r\frac{\log p}{\ell}.                \tag{7}
\]

Indeed subtract the corresponding constant terms, whose sum is zero.
For Re(a)<=0, the identity e^a-1=a integral_0^1 e^(sa)ds
gives |e^a-1|<=|a|. This proves (7), including complex v.

For higher prime powers, C019p's exact binomial-coefficient argument
gives (|alpha|*|alpha|)(n)<=1. Since |p^(v_j/ell)|<=1, convolution
of the two ordinary factors and the two such paired alpha factors
therefore gives

\[
 |K_{p^e}(v)|\le d_4(p^e)=\binom{e+3}{3}.                 \tag{8}
\]

This use of C019p is only its coefficient inequality, not its mean
or stationary-phase conclusions. For p>=2,

\[
 \sum_{e\ge2}\frac{d_4(p^e)^2}{p^e}
 \le\frac{C_1}{p^2},\qquad
 C_1=\sum_{e\ge2}\binom{e+3}{3}^2 2^{-(e-2)}<\infty.
                                                               \tag{9}
\]

The elementary factorial bound supplies all prime summation needed:

\[
 \sum_{p\le L}\lfloor L/p\rfloor\log p\le\log(L!)
       \le L\log L,
 \qquad \lfloor L/p\rfloor\ge L/(2p),
\]
\[
 \sum_{p\le L}\frac{(\log p)^2}{p}\le2\ell^2.             \tag{10}
\]

The first inequality counts only the first powers in the prime
factorization of L!, so it does not require a prime number theorem.
To obtain (10), first bound sum log p/p by 2 log L and then use
log p<=ell. Expanding the finite product over primes p<=L, with
nonnegative terms, and dropping the product cutoff k<=L gives

\[
 \sum_{k\le L}\frac{|K_k(v)|^2}{k}
 \le\prod_{p\le L}\left(1+\frac{|K_p(v)|^2}{p}
                        +\frac{C_1}{p^2}\right)
 \le C_2\exp(128r^2).                                    \tag{11}
\]

Here C_2=exp(C_1 sum_(n>=2)n^(-2)) is finite and absolute.
The infinite prime-power sums in a finite prime product converge by
(9); alternatively every inequality follows first for finite exponent
cutoffs and then by monotone convergence. No Dirichlet series on a
critical line is used. Taking square roots and restoring e^r proves
(5).

### The exact taper and two scalar Gaussian identities

Set

\[
 \mathcal T=\prod_{j=3}^6(1-\partial_{w_j}).
\]

In (4), each factor 1-partial_(w_j) inserts exactly
1-log(n_j)/ell. This is the prescribed linear taper for k<=L,
including a possible factor equal to L. It is not a change of
coefficients to a different mollifier.

The standard Cauchy integral formula, applied on unit circles in
the differentiated variables, and the triangle inequality for the
finite weighted norm give

\[
 \|\mathcal T K(w)\|_{\ell^2}
 +\|\partial_{w_1}\mathcal T K(w)\|_{\ell^2}
 +\|\partial_{w_2}\mathcal T K(w)\|_{\ell^2}
 \le48C\exp((r+1)+64(r+1)^2).                             \tag{12}
\]

For detail, expand T into its 16 subsets of {3,4,5,6}. Each
mixed derivative differentiates each selected variable only once;
the derivative in w_1 or w_2, if present, is also only once. Its
Cauchy integral has unit absolute prefactor and lies in the
polydisc max|w_j'|<=r+1. Apply (5) under that integral and sum.
There is no dependence on the number L of vector coordinates.

Define

\[
 A(Z)=-\tfrac12t(Z)u(Z)-ic_0t(Z),\qquad
 a(Z)=\sqrt{t(Z)/2}=Z/(2\sqrt d),
 \qquad C(Y)=E_1(Y)E_1(Y+h).
\]

Completing a square in the usual real Gaussian integral, with
d gamma(x)=(2*pi)^(-1/2)exp(-x^2/2)dx, gives the scalar identity

\[
 E_n(Z)=E_1(Z)\int_{\mathbb R}
              n^{A(Z)+a(Z)x}\,d\gamma(x).                \tag{13}
\]

Indeed E_n/E_1=exp(A log n+t(log n)^2/4), while
integral exp(a x log n)d gamma(x)=exp(a^2(log n)^2/2),
and a^2=t/2. The other factor exp(A log n) is constant in x.
Thus (13) is proved individually for each integer n; it is not
an assertion that a zeta moment or an infinite source can be
averaged over heat. Its only standard input is the named Gaussian
integral, and all later coefficient sums are finite.

For real x,y and Y in D put

\[
 w(Y;x,y)=\bigl(
   \ell(A(Y)+a(Y)x),
   \ell(A(Y+h)+a(Y+h)y-ih),
   0,-i\ell h,0,-i\ell h\bigr).
\]

Expanding c_r into its four alpha factors, and using (13) twice,
gives the exact finite identity, for every k<=L,

\[
 G_k(Y)=C(Y)\iint_{\mathbb R^2}
           (\mathcal T K_k)(w(Y;x,y))\,d\gamma(x)d\gamma(y).
                                                               \tag{14}
\]

To check all shifts, assign n_1=m, n_2=n, and n_3,n_4,n_5,n_6
to the two copies of b in c. The factors with the shift h are
n_2,n_4,n_6; their product contributes (n_2 n_4 n_6)^(-ih),
exactly n^(-ih) times the two shifted factors from c_r. All six
indices are at most k<=L, so no convolution truncation was removed
outside its range of validity. Each heat time in (14) remains the
time at its own Z=Y or Z=Y+h. Finite expansion and the scalar
Gaussian integrals justify (14) without an infinite interchange.

### Uniform domination, derivative and variation

From (3), for all Z in J and all large d,

\[
 \ell(|A(Z)|+h)\le1,\qquad
 0<\ell a(Z)\le b:=1/100.                                \tag{15}
\]

For example ell|A|<=5/1000+10c_0/(1000q), ell h<=3*pi/1000,
and ell a<=sqrt(5)/1000<1/100. Consequently, with
S=|x|+|y| and R_2=x^2+y^2,

\[
 r:=\max_j|w_j(Y;x,y)|\le1+bS,
\]
\[
 (r+1)+64(r+1)^2
 \le515+257b^2 R_2.                                      \tag{16}
\]

Here (2+bS)^2<=8+2b^2S^2<=8+4b^2R_2, while
2+bS<=3+b^2S^2/4<=3+b^2R_2/2. These yield even the
slightly smaller coefficient 256.5. The crucial strict inequality is

\[
 257b^2=257/10000<1/2,\qquad
 1/2-257b^2=4743/10000>0.                                \tag{17}
\]

It follows that the right side of (12), and that bound times any
fixed polynomial in |x|,|y|, is integrable against the two standard
Gaussian measures, with an absolute bound uniform in Y,d. The large
constant exp(515) is harmless for this O(1) statement; no small or
effective final moment constant is claimed.

Direct differentiation of the elementary functions, with d fixed,
gives on J

\[
 t'=Z/d=O(1/(Xq^2)),\quad u'=1/(2Z),\quad
 A'=-t'u/2-t/(4Z)-ic_0t'=O(1/(Xq)),
 \quad a'=1/(2\sqrt d)=O(1/(Xq)).                         \tag{18}
\]

Also |C(Y)|<=C and |C'(Y)|<=C/X. The first assertion follows
from t u^2=O(1); the second follows by differentiating
log E_1=t(u^2-pi^2/16)/4+ic_0 t u and using (18).
Thus only w_1,w_2 depend on Y, and

\[
 |\partial_Y w_1|\le C(1+|x|)/X,\qquad
 |\partial_Y w_2|\le C(1+|y|)/X.                          \tag{19}
\]

Differentiate (14), using the product rule for C and the chain rule
with (19). Equations (12),(16),(17) dominate both the integral and
its derivative by an integrable function, including their factors
1+|x|+|y|. The dominated differentiation theorem therefore applies
on the whole compact interval; one-sided derivatives at its endpoints
are the corresponding limits. This establishes the uniform bounds

\[
 \|G(Y)\|_{\ell^2}\le C,\qquad
 \|G'(Y)\|_{\ell^2}\le C/X.                              \tag{20}
\]

The finite-dimensional triangle inequality under an integral used
here follows by duality and Cauchy--Schwarz, or directly from
Minkowski's integral inequality. No coefficientwise supremum has
been interchanged with an infinite sum.

Since each low-index G_k is smooth with no entry jumps, its total
variation is integral_D|G_k'(Y)|dY. The fundamental theorem of
calculus implies

\[
 \mathcal B_k\le |G_k(X)|+2\int_D|G_k'(Y)|\,dY.
\]

Apply the triangle inequality in the weighted finite vector norm
and then (20). As |D|<=B=(sqrt2-1)X, this gives

\[
 \left(\sum_{k\le L}\frac{\mathcal B_k^2}{k}\right)^{1/2}
 \le\|G(X)\|_{\ell^2}+2\int_D\|G'(Y)\|_{\ell^2}dY
 \le C+2C|D|/X=O(1),                                    \tag{21}
\]

proving (1), with the coefficientwise supremum and variation both
paid. Its diagonal consequence in (2) is immediate. Applying the
finite integration-by-parts and logarithmic-kernel bound proved in
C019u (8)--(10) to the restricted index set 1<=k<=L bounds the
low-index off-diagonal by

\[
 C(1+\log L)\sum_{k\le L}\mathcal B_k^2
 \le C L(1+\log L)\sum_{k\le L}\mathcal B_k^2/k
 =O(L(1+\log L))=o(X).                                  \tag{22}
\]

This completes (2). The low/high cross integral and high-index
integral are absent from (22) and remain obligations for the full
norm. In particular none of the arguments justifies replacing
the true cutoffs in the high-index coefficients by the unrestricted
Euler product (6).

The ready assessment1402 explicitly permits a direct finite-sum
attempt with paid heat and cutoff comparisons. Its inspected ordinary
fourth-moment sources do not supply (14) or (21); no application of
them is being asserted. The explicit coefficient proof is needed
precisely to retain the fractional alpha, four linear tapers and two
different heat times. Cauchy's integral formula, the Gaussian integral,
dominated differentiation and finite norm inequalities are standard
named supporting results; their hypotheses and every specialization
used above have been checked in the proof. No new source coverage is
being approved during this research step.

## Mathlib

Full matching coverage is unchecked. Finite Dirichlet convolution,
Cauchy's integral formula, Gaussian exponential integration and finite
norm inequalities are supporting mathematics, not a claimed Mathlib
formalization of this moving-heat coefficient budget or the full
squared-pair moment. No absence or formal-verification claim is made.
