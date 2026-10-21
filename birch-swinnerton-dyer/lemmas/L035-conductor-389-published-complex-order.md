# L035 — Published complex order two and the fixed arithmetic comparison

## Hypotheses

Let E/Q be y^2+y=x^3+x^2-2x, with coefficients [0,1,1,-2,0].
Let L(E,s) denote its full finite-Euler-factor Hasse--Weil L-function,
without an archimedean factor. Use m(E) for the order at one of the
incomplete series in [foundations/01](../foundations/01-target-and-scope.md).
Use exactly the characteristic series and primitive ordinary L_7(E,T)
of audited L034, including its coordinate and period normalization.

Import the published analytic-order determination in J. E. Cremona,
*Algorithms for Modular Elliptic Curves*, corrected online second edition
(CUP, 1997): Section 2.13, printed pp.42--44, especially p.44's final
verification paragraph; Chapter 4, printed pp.106--107; Table 1, printed
p.157, row 389A1; and Table 4, printed p.327, row 389A. The precise
scope and computational qualifications of this import are below.
L030 supplies the minimal model and conductor. Audited L034 supplies
rational rank two independently of any complex analytic-order premise.
No form of BSD or full Sha finiteness is assumed.

## Conclusion

For this single curve,

\[
\operatorname{ord}_{s=1}L(E,s)=m(E)
=\operatorname{rank}E(\mathbf Q)
=\operatorname{ord}_T f_X
=\operatorname{ord}_T L_7(E,T)=2.
\]

In particular L(E,1)=L'(E,1)=0 and L''(E,1) is nonzero.
The complex-order conclusion is a citation-based certificate of a
published computational result, not a newly computed numerical enclosure.
The arithmetic and p-adic conclusions retain L034's exact scope and
qualifications. This is a known fixed case, not progress beyond the
checked sources, a uniform comparison theorem or a BSD candidate.
Neither full Sha finiteness nor a refined leading-coefficient formula is
asserted. The separate critical audit below passes with those source
qualifications retained.

## Proof

**Published input and exact identification.** In the convention
y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6, the displayed model has
coefficients [0,1,1,-2,0]. Cremona's
[Table 1, p.157, row 389A1](https://johncremona.github.io/book/fulltext/table1.pdf#page=49)
has exactly these coefficients. L030 independently gives minimal
discriminant and conductor 389. The
[Table 4 introduction, p.313](https://johncremona.github.io/book/fulltext/table4.pdf#page=1)
assigns class NX to curve NX1, except 990H, so its 389A entry concerns
this precise curve.

Import the analytic order two reported for that entry in
[Table 4, p.327](https://johncremona.github.io/book/fulltext/table4.pdf#page=15),
with its verification described in
[Section 2.13, p.44](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=38)
and [Chapter 4, pp.106--107](https://johncremona.github.io/book/fulltext/chapter4.pdf#page=3).
Section 2.13 separates algebraic central vanishing and sufficiently
precise derivative nonvanishing, and reports the eighteen order-two
cases up to level 1000. Chapter 4 p.107 identifies 389A among them and
explains that the preliminary BSD-motivated rank guesses were confirmed
analytically by derivative computations and arithmetically by two-descent.
The guess is not the imported result or a premise here. The rounded
derivative column and the conjectural Sha column supply no error bound
or exact leading coefficient used in this proof.

The authors' reviewed reliability documentation,
[Cremona--Sutherland, Reliability of elliptic curve data over Q](https://www.lmfdb.org/knowledge/show/rcs.rigor.ec.q),
last edited 2024-03-08, section “Mordell-Weil group and generators, and
BSD invariants”, states that analytic ranks at most three and conductors
at most 500000 are rigorous. The order-two conductor-389 result lies
in that scope. It separately disclaims guaranteed precision of the
special-value approximations and treats positive-rank Sha predictions
as approximate. This supporting documentation is not an independent
execution transcript. The ready assessment inspected the corrected
edition and the author's
[errata of 26 September 2003](https://johncremona.github.io/book/errata.pdf);
no relevant correction was found. The original derivative execution and
its detailed error transcript were not replayed here. The input has
the usual published computational-result qualification concerning the
correctness of its implementation and data. Reproving its derivative
algorithm is unnecessary for this citation-based import.

**Full versus incomplete conventions.** Cremona
[Section 2.8, equations (2.8.3)--(2.8.5), p.29](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=23)
identifies the newform L-function with the full finite-Euler-factor
L(E,s) and distinguishes its archimedean completion. For the standard
elliptic local polynomials put

\[
P_q(u)=
\begin{cases}
1-a_q u+q u^2,&\text{good reduction},\\
1-a_q u,&\text{multiplicative reduction},\quad a_q\in\{1,-1\},\\
1,&\text{additive reduction}.
\end{cases}
\]

Thus L(E,s)=product_q P_q(q^(-s))^(-1) initially in Re(s)>3/2.
For a good prime the named Hasse bound |a_q|<=2 sqrt(q) gives

\[
P_q(q^{-1})=1-a_q/q+1/q
\ge (\sqrt q-1)^2/q>0.
\]

For a multiplicative prime its value is 1-a_q/q>0; for an additive
prime it is one. These polynomials evaluated at q^(-s) are holomorphic
near one and have nonzero value there. This checks both possible
multiplicative signs without needing a splitness calculation at 389.

For an explicit integral short model of this E take
X=36x+12 and Y=216y+108. Completing the square and translating the
cubic gives

\[
Y^2=X^3-3024X+46224.
\]

Indeed with u=x+1/3 and v=y+1/2 one has
v^2=u^3-(7/3)u+107/108, and X=36u, Y=216v gives the displayed
coefficients. Its cubic discriminant is
-4(-3024)^3-27(46224)^2=2^8 3^12 389, nonzero. Consequently
foundations/01 can use S={2,3,389}; outside S the change of coordinates
is invertible integrally and the good-prime point counts agree with E.
This is a Q-isomorphism with rational inverse, so the rational rank
does not change either.

In the initial common half-plane the incomplete series is therefore

\[
L^S(E,s)=L(E,s)\prod_{q\in S}P_q(q^{-s}).
\]

Analytic continuation preserves this identity near one. The finite
product is holomorphic and nonzero there, by the preceding bounds;
hence ord_(s=1) L^S = ord_(s=1) L. The same proof handles any
additional finitely many good primes omitted by another short integral
model. Archimedean completion multiplies by
389^(s/2)(2 pi)^(-s) Gamma(s), holomorphic and nonzero near one since
Gamma(1)=1, so it also preserves the order. None of these observations
transfers a refined leading coefficient without the actual factor values.

**Lower vanishing and fixed assembly without BSD.** Independently of
the imported order-two computation, audited L034 gives rational rank
two. Modularity supplies holomorphic continuation, and the normalized
Dirichlet series is not identically zero (its first coefficient is one,
and L(E,s) tends to one as real s tends to infinity in its convergence
region). Its order at one is a finite nonnegative integer. If that order
were zero or one, the convention check would give the same incomplete
order, and the named analytic-rank-zero/one theorem in
[foundations/02](../foundations/02-standard-inputs.md) would give rational
rank zero or one, contradicting L034. Thus the lower bound two, and
the exact lower derivative vanishings, do not require BSD. The cited
analytic determination supplies exact order two, including the upper
bound; no p-adic order was used to obtain that bound.

Finally the convention check makes m(E)=2 and L034 gives the other
three orders/ranks equal to two in precisely its retained normalization.
Combining these independently established fixed conclusions proves the
displayed comparison. By the definition of analytic order, the second
derivative is nonzero and both lower derivatives vanish. The achieved
and required fixed complex-order thresholds are both two. General
production of certificates, complex/p-adic comparison for arbitrary
curves, full Sha finiteness and the refined formula remain unresolved.
ATTEMPTS/022--023 and the stopped L033 precision schedule are unaffected.

**Separate critical audit, 2026-10-08.** The approved audit passes for
this exact fixed comparison. It reuses the inspected Table 1/4 model
identification and the completed L034 audit. Targeted primary retrieval
checked Section 2.8 p.29, Proposition 2.13.1 p.43 and the verification
paragraph p.44, Chapter 4 pp.106--107, and Wiles's named theorem p.4.
Chapter 4 p.107 explicitly includes 389A in the analytically verified
order-two cases, separately from the initial guess and arithmetic descent.
No table decimal was promoted to an error enclosure. The original
analytic and descent executions remain unreplayed; this audit validates
the cited-result application, not those implementations independently.

Here are the complete elementary checks of the potentially sensitive
conventions. Substituting x=u-1/3 and y=v-1/2 into the minimal equation
gives v^2=u^3-7u/3+107/108. Scaling X=36u and Y=216v therefore gives
the claimed short equation; its inverse is
x=(X-12)/36, y=(Y-108)/216, with infinity preserved. For the cubic
discriminant, -3024=-2^4*3^3*7 and 46224=2^4*3^3*107 give

\[
-4(-3024)^3-27(46224)^2
=2^8 3^9(64\cdot343-107^2)
=2^8 3^9\cdot10503
=2^8 3^{12}\cdot389.
\]

This is the cubic discriminant used in foundations/01, not the minimal
Weierstrass discriminant 389. Its excluded set is exactly {2,3,389}.
The map and inverse are integral away from 2 and 3, where their scale
factors are units. Thus all retained good-prime point counts agree.
At 2 and 3 the original minimal E has good reduction by L030; the
singular reduction of this short model must not be used for its factors.

For every good q, (q+1-2 sqrt(q))/q=(sqrt(q)-1)^2/q is strictly
positive even at q=2. Hasse therefore checks all omitted good factors
without a large-characteristic restriction. The two multiplicative
possibilities give 1-1/q and 1+1/q, both positive; an additive factor is
one. Since q^(-s)=exp(-s log q) is entire, each nonzero value at one
gives a holomorphic unit on some neighborhood of one. The finite
intersection of those neighborhoods works for their product. Removing
inverse Euler factors multiplies the full series by P_q, not by P_q^(-1).
The identity on Re(s)>3/2 then continues to one, where multiplication
by this unit preserves the vanishing order. The archimedean multiplier
has value sqrt(389)/(2 pi) at one and is holomorphic there, so it also
preserves order. A unit need not have value one: no equality of leading
coefficients or refined BSD formula is inferred.

For the logical audit, modularity gives an entire, nonzero full
L-function, hence finite nonnegative order. If the order were zero or
one, Wiles's stated analytic-low-order theorem would contradict L034's
independently established rational rank two. This is a valid use of the
contrapositive and proves only order at least two. Proposition 2.13.1
requires a weight-two newform, a lower order bound and the specified
Fricke sign; this audit does not apply that formula anew or infer its
nonzero output from a sign. The published determination supplies the
upper bound. L034 supplies its unchanged primitive p-adic and algebraic
orders without using that complex determination. Thus no complex upper
bound comes from the p-adic order, and no circular hypothesis enters
the assembly. Required and achieved fixed complex order are both two.

No error or missing direct mathematical input was found. The existing
L030 and L034 inputs in DAG.md suffice. This is local verification of a
known fixed case, not progress beyond the cited results. Arbitrary-curve
rank equality, uniform certificate production, full Sha finiteness and
the refined formula remain unresolved. Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage for the published conductor-389 analytic-order
computation and this fixed arithmetic/p-adic comparison: **not checked**.
Supporting Hasse bounds, local Euler factors, analytic order and
change-of-model coverage: **not checked**. No absence claim is made.
The result is an informal source import and applicability proof, not a
formalization or independent replay of Cremona's computation.
