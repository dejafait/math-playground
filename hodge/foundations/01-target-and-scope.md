# Exact target and scope

Primary source checked on 2026-09-24: the [Clay Hodge page](https://www.claymath.org/millennium/hodge-conjecture/) links to Pierre Deligne, [The Hodge Conjecture, section 1, pp. 1–2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=1). The Clay page currently labels the problem unsolved.

Rechecked on 2026-09-25: the page and Deligne's rational formulation agree with the target below.

Let X be a smooth projective complex variety of complex dimension n. Work componentwise if X is disconnected. For 0 <= p <= n, define

\[
\operatorname{Hdg}^p(X)=H^{2p}(X,\mathbb Q)\cap H^{p,p}(X),
\qquad
A^p(X)=\operatorname{im}\bigl(\mathrm{cl}:\mathrm{CH}^p(X)_{\mathbb Q}
\longrightarrow H^{2p}(X,\mathbb Q)\bigr).
\]

The intersection uses the natural inclusion into complex cohomology. The exact target is A^p(X) = Hdg^p(X) for every X and p. Algebraic cycles give the inclusion from left to right; surjectivity is unresolved. Rational equivalence in the Chow-group formulation does not change the span of cycle classes.

Rational coefficients, projectivity, and smoothness remain hypotheses throughout. Integral counterexamples do not decide this target. No positivity or effectiveness requirement is imposed on the coefficients. Deligne's section 2(iv)–(v) explains the integral and nonprojective pitfalls.

## Notation for the first test

For an ample line bundle with first Chern class h, write L(alpha) = h cup alpha. On a fourfold,

\[
P_h^4(X,\mathbb Q)=\ker\bigl(L:H^4(X,\mathbb Q)\to H^6(X,\mathbb Q)\bigr).
\]

Write D^2(X) for the rational span of cup products of two divisor classes on X. Thus D^2(X) is contained in A^2(X). Equality D^2(X) = Hdg^2(X) is a stronger assertion than the Hodge conjecture and is only a proposed test, never an assumption.

## Mathlib

Coverage: **not checked** for the full target, rational cycle-class maps, Hodge decomposition, or the standard inputs used here. No Mathlib theorem match or absence is claimed.
