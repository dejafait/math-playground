# L057 — Fixed CM primitive quadratic-coefficient enclosure

## Hypotheses

Let E/Q be the globally minimal curve y^2=x^3+1, with minimal
differential dx/(2y), exact conductor 36 and normalized rational
weight-two trivial-character newform f from L050. Use the total real
minimal period Omega(E). L052 supplies the origin-preserving degree-one
optimal identification X_0(36)->E, with differential multiplier one
after choosing its sign, and the complete count #E(F_7)=12.

Use L056's audited exact functional on the full integral relative
module modulo torsion:

    F({a,b})=Re(2*pi*i integral_a^b f(z) dz)/Omega(E).

In particular 12F is integral on that entire module, including every
rational cusp-pair path. Set S(r)=F({infinity,r}) for every rational r.
This uses the actual normalized functional, not a sampled denominator
or an approximate period ratio.

Let alpha in Z_7^* be the ordinary unit root of X^2+4X+7. Use the
primitive untwisted ordinary series on the trivial Teichmuller branch,
with topological generator gamma satisfying kappa(gamma)=8, in the
finite-polynomial coordinate below. Write

    L_7(E,T)=sum_(i>=0) a_i T^i,    v_7(0)=+infinity.

For every k>=1 and d=1,...,6, let w_(k,d) be the unique integer in
[1,7^k-1] congruent to d modulo 7 and satisfying
w_(k,d)^6=1 modulo 7^k. For 0<=j<7^(k-1), let r_(k,d,j) be the
least positive residue of w_(k,d)*8^j modulo 7^k, and put

\[
A_{k,d,j}=S(r_{k,d,j}/7^k),\qquad
B_{k,d,j}=S(r_{k,d,j}/7^{k-1}),
\]
\[
P_k(z,T)=\sum_{d=1}^{6}\sum_{j=0}^{7^{k-1}-1}
\bigl(z^{-k}A_{k,d,j}-z^{-(k+1)}B_{k,d,j}\bigr)(1+T)^j.
\tag{1}
\]

Supply an integer n>=2 and exact rational unit u with u=-4 modulo 7,
and an integer M>=1 such that v_7(u^2+4u+7)>=M. At depth n all
residues and symbol values in (1) are exact. Define, without omitting
terms with j>2,

\[
b=\sum_{d=1}^{6}\sum_{j=0}^{7^{n-1}-1}\binom j2
\bigl(u^{-n}A_{n,d,j}-u^{-(n+1)}B_{n,d,j}\bigr)\in\mathbf Q.
\tag{2}
\]

These are conditional finite working data; no particular n,u,M or
finite sum is computed here. CM is allowed. No rational rank,
central vanishing or lower-coefficient vanishing is assumed.

## Conclusion

In the stated primitive normalization,

\[
\boxed{v_7(a_2-b)\ge N:=\min\{n-1,M\}.}
\tag{3}
\]

If N>v_7(b), then a_2 is nonzero and v_7(a_2)=v_7(b).
If b=0 or N<=v_7(b), this bound does not certify nonvanishing.
It supplies no actual coefficient, lower vanishing, rational direction,
Sha statement or complex-order comparison. In particular no arithmetic
conclusion of the non-CM L004 is transferred to this curve.

## Proof

**Known analytic input and fixed applicability.** Import Jennifer S.
Balakrishnan, J. Steffen Muller and William A. Stein, *A p-adic analogue
of the conjecture of Birch and Swinnerton-Dyer for modular abelian
varieties*, Math. Comp. 85 (2016), 983--1016, DOI 10.1090/mcom/3029,
[Sections 2.1--2.2, pp.987--993, equations (2.4), (2.6)--(2.9)
and Proposition 2.9 with its proof](https://wstein.org/papers/mcom3029.pdf#page=5).
Proposition 2.9 gives coefficientwise convergence of these ordinary
finite polynomials and explicitly retains the coefficient bounds in
the proof of Stein--Wuthrich's Proposition 3.1. The latter bounds use
the finite-character congruence and monic divisor in Stein--Wuthrich,
*Algorithms for the arithmetic of elliptic curves using Iwasawa theory*,
Math. Comp. 82 (2013), 1757--1792,
[Section 3, Lemma 3.2, Corollary 3.3 and Proposition 3.5,
pp.1763--1765](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=7).
The CM-inclusive authority for using that construction and its bounds
here is the 2016 Proposition 2.9, not removal of the 2013 paper's
standing non-CM hypothesis. We import the measure/convergence theorem;
we do not reprove it or invoke a main conjecture.

Here the coefficient field is Q, which is totally real, even though E
has CM. L050 supplies the required normalized level-36 newform and its
minimal target. L052's degree-one Jacobian identification makes E its
optimal quotient; its differential multiplier can be chosen to be one.
This meets the running c_A=1 hypothesis of the 2016 source, rather
than assuming a general Manin conjecture. Equation (2.4) in dimension
one permits the plus period to be the total real minimal period
Omega(E). L050's discriminant -432 is prime to seven, and L052's count
gives t=7+1-12=-4, prime to seven. Thus seven is good ordinary and its
unit-root polynomial is exactly the polynomial in the hypotheses.

L028's orientation identity (5), using real Fourier coefficients,
identifies the cited sources' plus-symbol numerator as

\[
\lambda^+(r)=-\pi i\left(\int_r^{i\infty}f(z)dz
                          +\int_{-r}^{i\infty}f(z)dz\right)
=\operatorname{Re}\left(2\pi i\int_{i\infty}^r f(z)dz\right).
\tag{4}
\]

Consequently their symbol is precisely S(r)=F({infinity,r}). A stored
path {r,infinity} must be negated; no table entry is silently reversed.
L056's full integral generation and normalized functional give
12S(r) in Z for every rational r. Since seven does not divide 12,
v_7(S(r))>=0 uniformly, for both symbol families at every k: C=0.
Neither the cusp denominator nor the length of a path decomposition
causes a loss. The actual table, not a finite sample, supplies this
input. L056 retains L051's total-period convention; no
least-positive-period conversion or additional factor two is made.

**Exact cosets and integral coefficients.** Apply the simple-root form
of Hensel's lemma, Keith Conrad, *Hensel's Lemma*,
[Theorem 4.1, p.6](https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf#page=6):
if f is in Z_p[X] and x in Z_p satisfies
|f(x)|_p<|f'(x)|_p^2, there is a unique root beta with
|beta-x|_p<|f'(x)|_p, and
|beta-x|_p=|f(x)/f'(x)|_p. An already exact root is treated separately.
For X^6-1 at each checked w_(k,d), the derivative 6w_(k,d)^5 is a
seven-adic unit and the residual has valuation at least k.
Thus w_(k,d) agrees modulo 7^k with the unique Teichmuller root of
residue d. Existence follows by lifting d modulo seven; uniqueness of
the checked integer follows from the unique root and the prescribed
interval. The r_(k,d,j) are therefore the exact source cosets in the
coordinate 8=1+7. Their symbols are evaluated at those exact rational
representatives, not at nearby approximations. Changing a representative
by 7^k changes both rational arguments by integers; the source symbols
are periodic, so it changes neither value in (1).

Since alpha is a unit and every A and B is seven-adically integral,
every measure value alpha^(-k)A-alpha^(-(k+1))B is integral.
Every coefficient of (1+T)^j is an integer, so
P_k(alpha,T) is in Z_7[T] for every k. This includes the zero
polynomial; no minimum valuation of its empty support is needed.

**Uniform limiting error.** Put q_k=[T^2]P_k(alpha,T). The cited
convergence gives q_k->a_2. In this C=0 case the cited adjacent
coefficient bound is

\[
v_7(q_{k+1}-q_k)\ge
\min_{1\le i\le2}v_7\binom{7^{k-1}}i.
\tag{5}
\]

For clarity, the integral-division step of that bound is valid in
exactly the monic case here. The finite-character congruence carried
over in the cited Proposition 2.9 proof gives divisibility in Q_7[T]
of G_k=P_(k+1)(alpha,T)-P_k(alpha,T) by
D_k=(1+T)^(7^(k-1))-1. Both polynomials are integral and D_k is monic.
Long division by a monic integral polynomial has integral quotient and
remainder; uniqueness of division over Q_7 makes the remainder zero.
Hence G_k=D_k H_k with H_k in Z_7[T], including G_k=0, for which
H_k=0. As D_k has zero constant term,

\[
[T^2]G_k=7^{k-1}[T]H_k+\binom{7^{k-1}}2[T^0]H_k.
\tag{6}
\]

Absent coefficients are zero. For k>=n>=2, both displayed binomial
coefficients have valuation k-1: the second is
7^(k-1)(7^(k-1)-1)/2. Thus (5)--(6) give
v_7(q_(k+1)-q_k)>=k-1. Finite telescoping shows
q_K-q_n in 7^(n-1)Z_7 for every K>n. This lattice is closed, so
coefficientwise convergence, without interchanging infinite sums,
gives

\[
v_7(a_2-q_n)\ge n-1.
\tag{7}
\]

This uses the proved all-level denominator, not a two-level denominator
estimate or the unrestricted integral-quotient assertion excluded in
L027's bookkeeping discussion. L027 is a template for these elementary
steps, not a theorem applied outside its stated non-CM hypotheses.

**Certified root substitution.** For h(X)=X^2+4X+7, u is in Z_7^*,
u=-4 modulo seven and h'(u)=2u+4=-4 modulo seven is a unit. The
residual hypothesis M>=1 meets Hensel's strict condition. It gives
a root alpha with v_7(alpha-u)=v_7(h(u))>=M; if h(u)=0, the distance
valuation is infinite. The root is a unit in that residue class and
the other root is 7/alpha, of valuation one, so it is the required
ordinary unit root. For each positive integer ell,

\[
\alpha^{-\ell}-u^{-\ell}
=\frac{(u-\alpha)\sum_{i=0}^{\ell-1}u^{\ell-1-i}\alpha^i}
       {\alpha^\ell u^\ell}.
\tag{8}
\]

The numerator sum is integral and the denominator is a unit. The
valuation is therefore at least M, with no loss depending on ell.
Apply (8) for ell=n and n+1, multiply by each corresponding integral
symbol and by the integer binomial(j,2), and sum. Every term has
valuation at least M; the nonarchimedean inequality incurs no loss
from the number of terms. The coefficient of T^2 in (1+T)^j is
binomial(j,2), so (2)
is exactly [T^2]P_n(u,T), including zero contributions at j=0,1 and
all contributions at j>2. Thus

\[
v_7(q_n-b)\ge M.
\tag{9}
\]

Combining (7) and (9) proves (3). If N>v_7(b), the error has strictly
larger valuation than the nonzero b, so the strong triangle inequality
gives v_7(a_2)=v_7(b)<infinity. No vanishing of a_0 or a_1 entered
the proof. No numerical b or strict-threshold success is claimed.

**Primitive normalization and limits of the result.** Equation (1)
is the untwisted source measure, summed over all six Teichmuller
classes, with no extra rescaling. Equation (2.9) of the 2016 source
retains the interpolation multiplier (1-alpha^(-1))^2; in particular
the constant-term convention is
L_7(E,0)=(1-alpha^(-1))^2 L(E,1)/Omega(E).
No multiplier is divided away and no finite bad-prime Euler factor is
omitted from the newform. The generator remains 8, so no coordinate
change rescales a_2. These checks concern the same primitive series,
not an arithmetic comparison theorem. The separate non-CM implications
of L004 and L026 are not inputs and are not asserted here. This is a
fixed specialization of known convergence and finite-precision
bookkeeping. Uniform useful coefficients, lower vanishing, rational
directions, divisible/full Sha and complex-order comparison remain
unresolved; arbitrary-curve BSD remains open in this notebook.

**Separate critical audit, 2026-10-13, BSD-196.** The fixed proof passes
under its stated local inputs. The approved scope is
`drafts/literature/2026-10-13-cm-quadratic-enclosure-critical-audit.md`.
The following checks supplement the proof without changing its bound.

1. The primary 2016 Section 2 hypotheses, running hypothesis on p.988,
   period convention (2.4), symbol definition p.991, measure and
   polynomial p.992, and complete Proposition 2.9 proof and (2.9) p.993
   were reopened. They cover this rational-coefficient ordinary newform.
   The CM endomorphism field is not its coefficient field. In dimension
   one the primitive integral Fourier basis is f itself: its coefficients
   are integral and its first coefficient is one. Thus L052's absolute
   differential multiplier one verifies the required c_A=1. The source's
   plus period integrates over all real points, matching Omega(E).
   No nonvanishing hypothesis is needed for this choice of period.

2. L050's explicit minimality and conductor argument and L052's
   degree-one identification, differential theorem application and full
   count at seven were checked in their canonical proofs. The seven
   affine y-counts are [2,2,2,1,2,1,1]; adjoining infinity gives twelve,
   hence t=-4. The discriminant is nonzero modulo seven. L028's conjugation
   identity fixes the infinity-to-r sign, and L056's audited full-module
   statement makes every symbol integral at seven. This audit uses that
   established table contract; it does not claim a fresh replay of its
   476280 Fourier terms or of its upstream implementations.

3. The source polynomial has precisely the two root powers -k and
   -(k+1) and argument denominators 7^k and 7^(k-1). Its cosets match
   the exact Teichmuller residues and generator 8 in (1). The complete
   finite-character proof of Stein--Wuthrich Lemma 3.2 and Corollary 3.3
   applies to the imported measure, including the trivial character:
   evaluation at T=0 is its total mass at either partition depth.
   Thus the difference vanishes at every root of D_k, including zero.
   These roots are distinct in characteristic zero. This checks the
   divisibility used in (6), not merely equality at primitive roots.

4. The integral quotient in (6) follows from monicity, including a zero
   difference. No unrestricted integral-divisor assertion is needed.
   For k>=2 both coefficients in (6) have valuation k-1; absent H_k
   coefficients contribute zero. Every later difference lies in
   7^(n-1)Z_7. Closure of that lattice and the imported coefficient limit
   prove (7). This does not infer a tail bound from only two sampled
   denominators. The stronger-looking two-level estimate following the
   source's Lemma 3.6 is unnecessary.

5. For the supplied rational unit, h'(u) is 3 modulo seven and is a
   unit, so the strict Hensel condition holds for M>=1. Theorem 4.1's
   exact-distance assertion matches (8)--(9), with an already exact
   root treated separately. The factorization in (8) has a unit
   denominator and an integral numerator sum for every positive
   exponent. Thus neither the exponent, number of summands nor any
   binomial weight introduces a precision loss. The zero-symbol and
   zero-polynomial cases are retained.

6. The sum uses all six Teichmuller classes, with no average, and the
   multiplier (1-alpha^(-1))^2 remains present. Both source and local
   coordinate use kappa(gamma)=8. No bad-prime factor, sign, period
   factor or change of generator intervenes. The strict test excludes
   zero only when N>v_7(b); equality and b=0 remain inconclusive.
   Neither a_0 nor a_1 is assumed zero. No actual b or arithmetic rank
   implication was produced or imported.

This is verification of known-method reproduction, not a stronger
estimate or a new mathematical discovery. The direct mathematical inputs
remain L028, L050, L052 and L056. L027 is a comparison only. Their
published-source and fixed-instance qualifications remain in force.

## Mathlib

The full matching CM analytic enclosure and the cited general-newform
convergence theorem have not been checked in Mathlib. Supporting Hensel,
valuation, binomial, monic-division and closed-lattice results have not
been checked there. Unknown coverage is not absence. No formalization
claim is made; the source theorem is imported and its fixed applicability
and finite-error specialization are written out above. The separate
fixed critical audit above passes; it does not change Mathlib coverage.
