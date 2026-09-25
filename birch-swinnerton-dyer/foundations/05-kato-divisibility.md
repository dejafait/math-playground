# Ordinary p-adic L-function and Kato divisibility

## Conventions and checked scope

Let E/Q have no complex multiplication, and let p >= 5 be a prime of
good ordinary reduction. Use the classical cyclotomic Selmer dual X,
Lambda = Z_p[[T]], and T = gamma - 1 from
[the control foundations](03-cyclotomic-control.md). Put B = Lambda[1/p],
regarded as the subring of Q_p[[T]] with bounded coefficient denominators.

Write L_p(E,T) for the primitive ordinary p-adic L-function on the trivial
Teichmuller-character branch, with the same gamma. Use the unit root alpha
of x^2 - a_p x + p, the Neron real period, and the coordinate
T = kappa(gamma)^(s-1) - 1. These conventions are in
[Stein--Wuthrich, Sections 3, 3.2, and 3.3, printed pages 1761--1766](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=5).
In the ordinary case L_p(E,T) belongs to B. No Euler factors are removed
or an exceptional-zero factor divided out in this notebook's use of it.

## Named divisibility input

The needed form of **Kato's divisibility theorem** is

\[
L_p(E,T)=f_X(T)g(T),\qquad g(T)\in B.
\tag{1}
\]

An explicit elliptic-curve statement is
[Stein--Wuthrich, Proposition 7.2 and Kato's Theorems 7.3--7.4, printed page 1778](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=22).
Their Section 6, printed page 1775, defines the same classical Selmer
dual. Their standing non-CM restriction starts in Section 3 and is
retained here. The original reference is **Kazuya Kato, *p-adic Hodge
theory and values of zeta functions of modular forms*, Asterisque 295
(2004), 117--290, Theorem 17.4**:
[Numdam record and full text](https://www.numdam.org/item/AST_2004__295__117_0/).
The full PDF exceeded the retrieval tool's size limit; the elliptic
translation is checked directly in Stein--Wuthrich, not through a fresh
reading of Kato's original proof.

For clarity, (1) follows from the checked statements in both representation
cases. If the mod-p representation is surjective, Proposition 7.2 lifts
surjectivity to the p-adic representation because p >= 5. Good ordinary
reduction is semistable at p, so Theorem 7.3 gives (1) with g in Lambda.
If the mod-p representation is not surjective, Theorem 7.4 gives
p^a L_p = f_X d for some a >= 0 and d in Lambda; set g = p^(-a)d.
Thus no residual-surjectivity assumption remains in (1) within the stated
scope. No assertion beyond that scope is needed here.

When L_p is nonzero, taking T-orders in (1) yields
ord_T f_X <= ord_T L_p: g is a power series with no negative T-powers.
The unspecified power of p has T-order zero. This proves the same
order bound in both cases, but gives no integral leading-coefficient
valuation bound when the power of p is unspecified. It does not assert
the reverse divisibility or equality of characteristic ideals.

## Existing use and limits

[Stein--Wuthrich, Section 7.1, printed page 1779](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=23)
already uses independent points and an upper bound on p-adic order to
certify rank in an example. L004 records this standard mechanism with
the notebook's two defects explicit. No new general rank algorithm or
guaranteed termination theorem is claimed.

The order here is p-adic analytic order. Neither (1) nor the certificate
identifies it with the complex order m(E). The full p-adic BSD formula,
the reverse main-conjecture divisibility, finite Sha, and height
nondegeneracy are not assumptions of (1).

## Mathlib

Full coverage of Kato divisibility, the ordinary p-adic L-function, and
the point/coefficient certificate: **not checked**. Supporting power-series
order and p-adic valuation results: **not checked**. The cited names and
direct links are published mathematical inputs, not Mathlib matches or
claims of library absence.
