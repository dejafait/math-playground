# L026 — A conditional quadratic-coefficient certificate for Selmer corank

## Hypotheses

Let E/Q be non-CM and let p >= 5 be good ordinary. Assume that the
representation on E[p] is surjective, p divides neither #E(F_p), the
Manin constant nor any Tamagawa factor, and E(Q_p)[p] = 0. Assume a
nonzero residual Kurihara number at some square-free index in Sakamoto's
N_(1,0), with the compatible Neron plus period and discrete-logarithm
conventions. No minimality or prescribed number of auxiliary primes is
required. These are L025's arithmetic and residual-family hypotheses,
with its granted corank hypothesis removed.

Assume L(E,1) = 0 and root number w(E) = +1. In the primitive ordinary
cyclotomic normalization of
[the divisibility foundations](../foundations/05-kato-divisibility.md),
write L_p(E,T) = sum_(j>=0) a_j T^j and require a rigorously certified
a_2 != 0. Fix the generator and coordinate of that certificate. For
example, L004's proved enclosure v_p(a_2-b) >= N > v_p(b), with exact
b and a proved error bound, suffices. Removed Euler factors or an
uncertified numerical approximation do not suffice.

Put S = Sel(Q,E[p^infinity]), let X be the classical cyclotomic Selmer
dual, A = Z_p[[T]]_(T), M = X tensor A, and f_X its characteristic
generator. Rational rank, finite Sha and Selmer corank are not assumed.
The pre-existing source assessment is
[the approved comparison](../drafts/literature/2026-10-06-quadratic-coefficient-selmer-corank.md).

## Conclusion

With d = corank_Z_p S and ell = ord_T L_p(E,T),

\[
d = \operatorname{ord}_T f_X = \ell = 2,\qquad
TM=0,\qquad M\simeq (A/(T))^2.
\]

In particular a_0 = a_1 = 0 exactly. Also

\[
\operatorname{rank}E(\mathbf Q)
+\operatorname{corank}_{\mathbf Z_p}\Sha(E/\mathbf Q)[p^\infty]=2.
\]

This supplies the corank premise for L023-L025 on the other retained
hypotheses. It does not assert rational rank two, finite p-primary Sha,
zero finite quotient F = S/S_div, complex order two, or availability of
the coefficient certificate from complex order two. No BSD resolution
or progress beyond the checked source package is claimed.

## Proof

**Match the nonvanishing premise without assuming corank.** A prime ell
in P_(1,0) is a good-reduction prime with ell = 1 mod p and
E(F_ell)[p] cyclic of order p. Thus p divides
#E(F_ell) = ell+1-a_ell, so it satisfies Kim's auxiliary-prime conditions
ell = 1 and a_ell = ell+1 mod p. Kim's coefficient ring at the
square-free witness index has a quotient F_p. With the stated periods
and logarithm generators, reduction of his integral Kurihara number is
Sakamoto's residual modular-symbol sum. A nonzero residual sum implies
that the integral collection is nonzero. Changes of primitive roots
multiply these sums by units and preserve this implication.

Import these definitions and their comparison from Chan-Ho Kim,
*The structure of Selmer groups and the Iwasawa main conjecture for
elliptic curves*, publisher-hosted author text dated 2025-05-12,
[Sections 1.2.2/1.4, printed pp. 4--6](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=4),
and Ryotaro Sakamoto, *p-Selmer group and modular symbols*, Documenta
Math. 27 (2022), 1891--1922,
[Section 1.1, pp. 1892--1894](https://ems.press/content/serial-article-files/29299?nt=1#page=2).
This is the same witness matching recorded in L021, but does not invoke
L021's corank-two theorem or its conclusions. No finite-quotient
elimination is used.

**Infinitude becomes positive classical corank.** Kim's
[Corollary 1.11, printed pp. 8--9](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=8)
states, on p >= 5, residual surjectivity, prime-to-p Manin constant and
nonzero integral Kurihara collection, that S is finite if and only if
L(E,1) != 0. All these hypotheses have been checked above. Hence S is
infinite. Import the corollary without reproof; it assumes neither
finite Sha nor positive rational rank.

L002's arithmetic control argument gives finite generation of S^vee
over Z_p: X/TX is finitely generated over Z_p, and its control map to
S^vee has finite kernel and cokernel. By the structure theorem over
Z_p, S^vee is a free module of rank d plus finite torsion. If d=0 it
would be finite and its Pontryagin dual S would be finite. Therefore
infinitude implies d>=1; infinitude alone without this finite-generation
input would not justify that implication.

**Parity gives the required lower bound.** Kim's
[Corollary 1.12, printed p. 9](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=9)
has the same nonvanishing hypotheses and states
d = ord_(s=1)L(E,s) mod 2. It is classical Selmer-corank parity, not
rational-rank parity or residual-Selmer-dimension parity. Let
m = ord_(s=1)L(E,s), which is finite: the analytic continuation is not
identically zero, since its defining Dirichlet series has first
coefficient one. The completed L-function's factors are analytic and
nonzero at 1, so it has the same order. Its functional equation reads
Lambda(E,1+t) = w(E) Lambda(E,1-t). Comparing the first nonzero Taylor
term gives w(E)=(-1)^m. Thus w(E)=+1 gives even m, and Kim gives even d.
Combined with d>=1 this yields d>=2. This comparison proves no upper
bound on m and does not identify m with a p-adic order.

**The coefficient gives the matching upper bound.** Apply L004 with
k=0 and n=2: the point premise is empty and a_2 != 0 is the supplied
certificate. Its Kato-divisibility argument uses precisely this
primitive classical cyclotomic normalization and gives

\[
\operatorname{ord}_T f_X\le\ell\le2.
\]

The imported divisibility is Kato, *p-adic Hodge theory and values of
zeta functions of modular forms*, Asterisque 295 (2004), Theorem 17.4,
in the checked elliptic-curve form of Stein--Wuthrich, *Algorithms for
the arithmetic of elliptic curves using Iwasawa theory*, Math. Comp.
82 (2013), 1757--1792,
[Proposition 7.2 and Theorem 7.3, p. 1778](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=22).
Residual surjectivity at p>=5 lifts to p-adic surjectivity; good ordinary
reduction is semistable at p. No reverse divisibility is imported.

L002 gives ord_T f_X = d + length_A(TM), with nonnegative second term.
We therefore have

\[
2\le d\le \operatorname{ord}_T f_X\le\ell\le2.
\]

All terms equal two. The nonnegative length is zero, so TM=0 and
L002's decomposition gives M=(A/(T))^2. The order ell=2 forces the
two lower coefficients to vanish; their vanishing was not a premise.
Finally L002's Kummer identity d=r+s gives the displayed rank/Sha
corank sum. Neither s=0 nor F=0 follows from this chain. The achieved
threshold is precisely classical corank two, which suffices for the
conditional downstream construction but leaves rational membership
and the complex-order comparison unresolved.

**Critical audit (2026-10-06).** The approved audit found no failed
implication and makes no change to the statement. In the witness
comparison, reduction is taken in the coefficient ring at the same
index, then termwise through the finite modular-symbol sum. It commutes
with products of the discrete logarithms. Thus a nonzero residual
scalar cannot come from a zero integral scalar; no converse, unit at
the first integral index, or minimal-prime-count assertion is used.
The compatible period and generator conventions are hypotheses, not
deduced from nonvanishing. This uses only the cited definitions, not
L021's corank-dependent conclusion.

For the finite-generation step, X/TX is a finitely generated module
over Lambda/(T) = Z_p. The image of the dual control map is therefore
finitely generated, and adjoining lifts of generators of its finite
cokernel generates S^vee. Its finite kernel is needed for the rational
dimension identification in L002, not to assume finiteness of S.
Neither Kim's finite-Sha clauses in Theorem 1.8(4)--(6) nor the
global prime-selection assertion following Corollary 1.11 enters.
The fixed-prime witness is supplied independently.

The coefficient audit uses only L004's general inequality with k=0,
not its matching k=n conclusion. At (T), p is a unit, so inverting p
in Kato's divisibility preserves the T-order inequality, but division
by T or removal of a vanishing Euler factor would not. The same
primitive series and coordinate occur in the supplied certificate and
the divisibility. Classical corank parity supplies the lower bound
independently of any Taylor parity assertion for that p-adic series.
Consequently no lower coefficient was presumed zero. The vanishing
of length_A(TM) follows from equality of the two bounds, whereas
vanishing of the Sha corank would require the still absent lower bound
on rational rank. The finite quotient F is not measured by these
rationalized dimensions. This is verification of the existing
known-source specialization, not a new bound or a BSD candidate.

## Mathlib

Full combined arithmetic statement and the imported Kim/Kato theorems:
not checked. Supporting finite-generation structure, Taylor parity,
power-series order and valuation results: not checked. No absence or
formalization claim is made. Named inputs are imported by the precise
citations above; only their applicability and the elementary matching
bounds are proved here, as authorized by SPECIALIZE.
