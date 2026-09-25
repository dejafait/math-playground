# Castella--Hsieh: nonvanishing and its exact scope

Checked 2026-09-25 against Francesc Castella and Ming-Lun Hsieh,
[*On the nonvanishing of generalised Kato classes for elliptic curves
of rank 2*, Forum of Mathematics, Sigma 10 (2022), e12](https://doi.org/10.1017/fms.2021.85).
References use the published 32-page version. The article is licensed
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); the statements
below are paraphrased, and notebook deductions are identified separately.

## Theorem A setting

Keep the following hypotheses from Section 1.2 and the beginning of
[Section 5, printed page 25](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=25).

- E/Q has conductor N, good ordinary reduction at p > 3, root number
  +1, and L(E,1) = 0. Let f be its weight-two newform.
- K is imaginary quadratic, its discriminant is coprime to N, and
  p = mathfrak p times overline{mathfrak p} splits in K. Let tau be
  complex conjugation and psi a finite-order ray class character of K
  with conductor coprime to Np. Put chi = psi/psi^tau,
  g = theta_psi, and g* = theta_(psi^(-1)).
- alpha = psi(overline{mathfrak p}) and beta = psi(mathfrak p) are
  distinct, equivalently chi(overline{mathfrak p}) != 1. Work in the
  Q_p coefficient case: assume the relevant Hecke fields and these
  eigenvalues embed in Q_p. This restriction is retained throughout.
- L(E^K,1)L(E/K,chi,1) != 0. This is L(E,ad^0(g),1).
- E[p] is irreducible; the maximal factor N^- of N supported on primes
  inert in K is squarefree with an odd number of prime factors; E[p]
  is ramified at each of those primes.

Here it is the auxiliary form g that has CM. No uniform availability
of these auxiliary data for every E/Q is assumed. The complex order
uses the same convention as m(E), by the finite Euler-factor argument
in [the earlier source audit](06-generalised-kato-scope.md).

## Precisely imported results

Write S = Sel(Q,V_p E) and kappa = kappa_(alpha,alpha^(-1))(f,g,g*),
projected to the E summand. **Lemma 5.1** identifies its Selmer
membership. **Theorem A**, equations (1.9)--(1.10), printed page 5, gives

\[
\kappa\ne0\ \Longrightarrow\ \dim_{\mathbf Q_p}S=2,
\qquad
\bigl(\dim_{\mathbf Q_p}S=2\ \text{and}\ \operatorname{Loc}_p|_S\ne0\bigr)
\ \Longrightarrow\ \kappa\ne0.
\tag{CH-A}
\]

The source is [Theorem A and Remarks 1.5--1.6](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=5).
The off-diagonal classes vanish. Remark 1.6 identifies the nonzero
diagonal classes with the same line ker(log_p) in the two-dimensional
Selmer space. The logarithm factors through the completed local Kummer
space, where it is injective after tensoring with Q_p, as proved in
L005. Thus this is the strict line in the notebook's terminology.

**Theorem B**, on that same page, adds the hypothesis rank E(Q) > 0
and proves

\[
\operatorname{ord}_{T_{\rm ac}}\Theta_{f/K}=2
\ \Longrightarrow\ \kappa\ne0.
\tag{CH-B}
\]

The variable here is anticyclotomic: Theta_(f/K) is the theta element
(a square-root anticyclotomic p-adic L-function) of Section 2.4.
Neither its order nor its degree-two coefficient is L004's ordinary
cyclotomic coefficient. Theorem B does not identify its order with
the complex order m(E).

## What the proofs actually bound

[Section 5.5, printed page 28](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=28)
proves CH-A's forward implication using derived Selmer heights and
anticyclotomic characteristic divisibility. With a nonzero kappa, the
source obtains positive integers r_i and dimensions d_i >= 2 satisfying

\[
\sum_i r_i d_i\le\mathfrak r\le2r_t,
\qquad \dim S=\sum_i d_i,
\qquad \mathfrak r=\operatorname{ord}_{T_{\rm ac}}\Theta_{f/K}.
\]

These force one block and d_1 = 2. The dimension here remains that of
S; the proof has not substituted E(Q) tensor Q_p for S.

The beginning of **Section 5.7**, printed page 28, expressly adds
finite Sha(E/Q)[p^infinity]. [**Theorem 5.5**, printed page 29](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=29), then
expresses the class using a rational-point basis and a derived
regulator. That application does not prove Kummer membership without
its added finiteness hypothesis. Remark 1.3 already distinguishes
Selmer dimension two from the conjectural complex-order comparison.

## Mathlib

Full coverage of Theorems A, B, 5.5, Lemma 5.1, and derived Selmer
heights: **not checked**. The named citations match the restricted
Selmer statements above. They do not match the missing implication
from m(E) = 2 to a nonzero rational Kummer class. No theorem from the
article is used with a conjectural premise silently removed.
