# L027 — Conditional finite enclosure of the primitive quadratic coefficient

## Hypotheses

Let E/Q be non-CM and p>=5 be good ordinary. Write t=a_p(E), so
p does not divide t, and let alpha be the unit root of X^2-tX+p.
Use the primitive untwisted ordinary series on the trivial Teichmuller
branch, the real Neron period, and kappa(gamma)=1+p, exactly as in
[the divisibility conventions](../foundations/05-kato-divisibility.md).
Write L_p(E,T)=sum_(i>=0) a_i T^i and put v_p(0)=+infinity.

The plus symbol map S(r)=[r]^+ is supplied exactly, with its equality
to that Neron-normalized map already certified. Grant an integer C>=0
such that v_p(S(r))>=-C for every symbol argument at every level of the
construction below. This is a uniform proved input; a list of sampled
denominators or an approximate period ratio does not meet it.

For k>=1 and d=1,...,p-1, let w_(k,d) be the unique integer in
[1,p^k-1] with w_(k,d)=d modulo p and
w_(k,d)^(p-1)=1 modulo p^k. At working depth n>=2 these integers are
supplied with these exact checks. Let r_(k,d,j) be the least positive
residue of w_(k,d)(1+p)^j modulo p^k, for 0<=j<p^(k-1). Set

\[
A_{k,d,j}=S(r_{k,d,j}/p^k),\qquad
B_{k,d,j}=S(r_{k,d,j}/p^{k-1}),
\]

and use Stein--Wuthrich's ordinary finite polynomial

\[
P_k(z,T)=\sum_{d=1}^{p-1}\sum_{j=0}^{p^{k-1}-1}
 (z^{-k}A_{k,d,j}-z^{-(k+1)}B_{k,d,j})(1+T)^j.
\tag{1}
\]

Here z is a nonzero parameter; P_k(alpha,T) is their P_k in the fixed
coordinate. All A and B at depth n are exact rational numbers. The
symbol and polynomial conventions, including integer representatives
of the measure's cosets, are imported from Stein--Wuthrich,
*Algorithms for the arithmetic of elliptic curves using Iwasawa theory*,
Math. Comp. 82 (2013), 1757--1792,
[Section 3, pp. 1762--1763](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=6).

Supply u in Q with v_p(u)=0, u=t modulo p, and an integer M>=1 with
v_p(u^2-tu+p)>=M. Define the exact rational number

\[
b=\sum_{d=1}^{p-1}\sum_{j=0}^{p^{n-1}-1}\binom j2
 (u^{-n}A_{n,d,j}-u^{-(n+1)}B_{n,d,j}).
\tag{2}
\]

## Conclusion

Without assuming any lower coefficient vanishes,

\[
\boxed{v_p(a_2-b)\ge N:=\min\{n-1-C,M-C\}.}
\tag{3}
\]

If N>v_p(b), then a_2 is nonzero and v_p(a_2)=v_p(b).
This supplies L004's degree-two coefficient certificate, and can supply
L026's coefficient premise only when all its additional arithmetic,
residual-family, central-vanishing and sign hypotheses hold separately.
If N<=v_p(b), this enclosure gives no nonvanishing certificate; b=0
gives none. No actual data, uniform nonvanishing, rational rank two,
finite Sha, or comparison with complex analytic order is asserted.

## Proof

**The checked residues introduce no symbol error.** For
h(X)=X^(p-1)-1, each supplied w=w_(n,d) is integral, has
v_p(h(w))>=n and has derivative (p-1)w^(p-2) a unit.
Import Keith Conrad, *Hensel's Lemma*,
[Theorem 4.1, p. 6](https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf#page=6):
for f in Z_p[X] and x in Z_p, |f(x)|_p<|f'(x)|_p^2 gives a unique
root beta with |beta-x|_p<|f'(x)|_p, and
|beta-x|_p=|f(x)/f'(x)|_p. Thus w agrees modulo p^n with the
Teichmuller root in residue class d. If the residual is zero, the
root is already w and the same conclusion holds.

This also proves uniqueness of the checked residue modulo p^n:
two such integers in residue class d are within p^n of the unique
root in that class, hence are congruent modulo p^n and equal in the
specified interval. Existence at each level follows by applying the
same theorem at d modulo p and reducing the resulting root. Therefore
the cosets used in (1) are exactly the source's cosets. Evaluating the
symbols at the specified rational representatives is exact; there is
no continuity estimate for a symbol evaluated at a nearby argument.
Changing an integer representative by p^k changes each rational
argument by an integer, and leaves these periodic symbols unchanged,
as in the source's measure definition.

**Bound every polynomial coefficient with the uniform input.**
Since v_p(alpha)=0, each measure value
alpha^(-k)A_(k,d,j)-alpha^(-(k+1))B_(k,d,j) has valuation at least -C.
Every coefficient of (1+T)^j is an integer. Each coefficient of
P_k(alpha,T), a finite sum of these products, consequently has
valuation at least -C. In particular, if
c_k=max(0,-min_i v_p([T^i]P_k(alpha,T))), then c_k<=C at every k.
For the zero polynomial put c_k=0. The argument uses both families
of symbol arguments and the bound at every level, not only n and n+1.

Import Stein--Wuthrich,
[Propositions 3.1/3.5, pp. 1763--1765](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=7):
P_k(alpha,T) converges coefficientwise to this L_p, and with
q_k=[T^2]P_k(alpha,T),

\[
v_p(q_{k+1}-q_k)\ge e_{k-1,2}-\max(c_k,c_{k+1}),\quad
e_{h,2}=\min_{1\le i\le2}v_p\binom{p^h}{i}.
\tag{4}
\]

These are cited inputs; modular-symbol convergence is not reproved.
Their monic-divisor argument applies to the ordinary unit-root
polynomials with integral coefficients after multiplication by p^C.
Explicitly, set D_k=(1+T)^(p^(k-1))-1 and
G_k=p^C(P_(k+1)(alpha,T)-P_k(alpha,T)). Corollary 3.3 gives
D_k dividing G_k in Q_p[T]. Here G_k is in Z_p[T] and D_k is
monic in Z_p[T]. Polynomial long division by a monic polynomial
uses no nonintegral coefficient divisions, so it produces quotient
H_k and remainder R_k in Z_p[T]. Uniqueness of division in Q_p[T]
and the cited divisibility give R_k=0. Since D_k has zero constant
term,

\[
[T^2]G_k=p^{k-1}[T]H_k+\binom{p^{k-1}}2[T^0]H_k.
\]

Both coefficients of H_k are integral (absent coefficients are zero).
This verifies the precise monic case needed for (4), including a zero
difference polynomial, without an unrestricted integral-quotient claim.
We do not use the source's concluding two-level tail constant or its
Lemma 3.6 denominator discussion: the stronger all-level input here
already bounds every c_k.

For k>=n>=2, h=k-1>=1. The two binomial coefficients are p^h and
p^h(p^h-1)/2. Since p>=5, both have valuation h. Hence (4) gives
v_p(q_(k+1)-q_k)>=k-1-C. For any integer K>n, finite telescoping
then puts q_K-q_n in p^(n-1-C) Z_p. This lattice is closed, including
when the exponent is negative: it is a nonzero scalar multiple of
the closed set Z_p. Coefficientwise convergence gives q_K -> a_2,
so

\[
v_p(a_2-q_n)\ge n-1-C.
\tag{5}
\]

This proves the infinite tail by a finite-sum bound followed by a
closed-lattice limit, without exchanging an unbounded sum with a limit.

**Certify the correct unit root and its finite substitution error.**
For f(X)=X^2-tX+p, ordinary reduction gives t a unit and
f'(u)=2u-t=t modulo p, also a unit. The polynomial has integral
coefficients, u is in Z_p, and M>=1 gives |f(u)|_p<1=|f'(u)|_p^2.
Conrad's same theorem gives a root in the residue class of u, with
v_p(alpha-u)=v_p(f(u))>=M. This root is the ordinary unit root:
it is a unit, and the other quadratic root has valuation one, since
their product is p. If f(u)=0, the conclusion holds with infinite
distance valuation.

For any positive integer ell, factorization gives

\[
\alpha^{-\ell}-u^{-\ell}
=\frac{u^\ell-\alpha^\ell}{\alpha^\ell u^\ell}
=\frac{(u-\alpha)\sum_{i=0}^{\ell-1}u^{\ell-1-i}\alpha^i}
 {\alpha^\ell u^\ell}.
\tag{6}
\]

The denominator is a unit and the sum is integral, so the valuation
is at least M. In particular there is no loss proportional to ell;
any additional divisibility of the sum only improves the estimate.
Multiply (6), for ell=n and ell=n+1, by the corresponding exact
symbols and by the integer binomial(j,2). Each resulting term has
valuation at least M-C. The finite sum in (2) therefore gives

\[
v_p(q_n-b)\ge M-C.
\tag{7}
\]

There is no loss from the number of summands: the nonarchimedean
inequality bounds their sum by their minimum valuation.

**Coefficient extraction and the final threshold.** For every j>=0,
the coefficient of T^2 in (1+T)^j is exactly binomial(j,2), with zero
for j=0,1. Thus (2) retains all summands of P_n(u,T). Computing each
power modulo T^3 or discarding the polynomial's monomials of degree
greater than two does not change b. Dropping summands with exponent
j>2 would change it and is not justified. No p-adic floating-point
rounding occurs in the exact rational b.

Combining (5) and (7) by the strong triangle inequality proves (3).
If N>v_p(b), b is nonzero and the error has strictly larger valuation
than b. L004's enclosure argument yields v_p(a_2)=v_p(b)<infinity.
No assumption a_0=a_1=0 entered any estimate. The achieved bound is
the stated conditional N; exceeding v_p(b) remains a separate test
on supplied data. All-level denominator and exact-normalization
certification, uniform availability of coefficient witnesses, rational
Kummer membership and complex-order comparison remain unresolved.
This is elementary finite-precision bookkeeping for known convergence
and root-distance theorems, not progress beyond those sources or a
candidate resolution of BSD.

**Normalization audit.** The symbol hypothesis uses the source's total
real Neron period, not an unconverted least positive real period.
The cosets and exponents in (1) use 1+p; hence their coefficientwise
limit is in the coordinate fixed in foundations/05. There is no twist
character in the sum. The ordinary measure is used without rescaling:
in particular the interpolation multiplier (1-alpha^(-1))^2 of
Stein--Wuthrich, Sections 3.1--3.3, pp. 1765--1766, is retained.
These are exact matches of the granted inputs to the cited construction;
they do not certify a numerical period ratio or produce a normalized
symbol map. Thus the coefficient here is the primitive a_2 required
by L004 and, conditionally on its other hypotheses, L026.

## Mathlib

Full matching arithmetic enclosure, Stein--Wuthrich convergence and
Conrad's theorem: not checked in Mathlib. Supporting valuation,
binomial-coefficient, polynomial and closed-lattice results: not
checked. No absence or formalization claim is made. The named inputs
are cited above; their applications and the conditional error
bookkeeping are written out here.
