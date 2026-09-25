# L006 — The Kummer defect after generalised Kato nonvanishing

## Hypotheses

Let E, p, K, psi, f, g, g*, and kappa satisfy the full Theorem A
hypotheses recorded in [the Castella--Hsieh foundations](../foundations/07-castella-hsieh-nonvanishing.md).
In particular p >= 5 is good ordinary, L(E,1) = 0 with root number +1,
and the auxiliary nonvanishing, residual, ramification, and coefficient
conditions there are retained. Assume kappa != 0.

Use L005's rational Kummer injection j: W -> S, where
W = E(Q) tensor_Z Q_p, and its exact quotient q: S -> V_p Sha. The
cohomological Selmer group in Theorem A is this rationalized inverse
limit Selmer group, with the same local Kummer conditions. Put
r = rank E(Q), D = Sha(E/Q)[p^infinity], and
s = dim_Qp V_p Sha(E/Q).

## Conclusion

The class kappa is strict, and

\[
\dim_{\mathbf Q_p}S=r+s=2,\qquad 0\le r\le2.
\tag{1}
\]

Moreover, under these hypotheses,

\[
q(\kappa)=0
\quad\Longleftrightarrow\quad r=2
\quad\Longleftrightarrow\quad s=0
\quad\Longleftrightarrow\quad D\text{ is finite}.
\tag{2}
\]

Thus a nonzero rational Kummer class of this construction certifies
rational rank two without L004's extra cyclotomic coefficient. The
point-membership premise is essential and is not proved here.
If m(E) = 2 is independently known, (2) proves the rank assertion for
this E only after that premise is supplied. No assertion about the
cyclotomic regulator, the whole Sha, or the refined BSD formula follows.

If nonvanishing is instead obtained from Theorem B, its extra positive
rational-rank hypothesis improves (1) only to

\[
1\le r\le2,\qquad (r,s)\in\{(1,1),(2,0)\}.
\tag{3}
\]

These are the possibilities left by the stated bounds, not asserted
examples of elliptic curves with infinite Sha.

## Proof

**The proved upper bound and strictness.** Castella--Hsieh, Theorem A,
equation (1.9), gives dim S = 2. Their Remark 1.6 places a nonzero
diagonal class on ker(log_p) in this Selmer space; these statements
are cited precisely in the foundations above. L005 identifies the
logarithm on the completed local Kummer space with an isomorphism to
Q_p. Therefore log_p(kappa) = 0 means lambda_p(kappa) = 0, so kappa
is strict. This uses no finiteness assumption on D.

L005's Kummer exact sequence gives dim S = dim W + dim V_p Sha = r+s.
Both summands have nonnegative integer dimension, proving (1).

**Matching the rational lower bound.** If q(kappa) = 0, exactness gives
kappa in j(W). Its nonvanishing and strictness then give r >= 2 by
L005(1). Combining this with r+s = 2 yields r = 2 and s = 0. This
uses only L005's local-logarithm conclusion, not its coefficient-based
conclusion. Conversely, r = 2 gives s = 0, so q is zero and in
particular q(kappa) = 0. The same dimension identity proves
r = 2 if and only if s = 0.

**Finiteness at this prime.** The finite-generation and control inputs
in [the cyclotomic foundations](../foundations/03-cyclotomic-control.md)
show that D has finitely generated Z_p-dual: the dual of the base
Selmer group is finitely generated, and D's dual is its submodule.
The structure theorem over Z_p consequently gives
D isomorphic to (Q_p/Z_p)^s direct-sum F with F finite. Indeed, the
Tate module of a finite p-group is zero, while that of Q_p/Z_p is Z_p,
so this multiplicity equals dim V_p D = s. Hence s = 0 is equivalent
to finite D. This proves all of (2); finiteness was a conclusion,
not the starting reason to call kappa Kummer.

Under Theorem B's additional assumptions, r > 0 is already a premise.
Together with (1), it gives (3). Nothing in this deduction eliminates
the remaining s = 1 case. In particular, nonzero localization on S
is weaker than rational Kummer membership of its strict vector.

For an explicit check of this last linear-algebra distinction, take
S = Q_p e_1 direct-sum Q_p e_2, W = Q_p e_1,
lambda_p(x e_1+y e_2) = x, q(x e_1+y e_2) = y, and kappa = e_2.
The Kummer-type sequence is exact, W has positive dimension,
localization on W is nonzero, and kappa is nonzero and strict;
nevertheless q(kappa) = 1. This model checks only those linear data.
It is not an arithmetic realization of the hypotheses or a BSD
counterexample, and the paper's arithmetic theorem is not inferred
from the model.

## Mathlib

Coverage of this full arithmetic certificate: **not checked**.
Supporting exact-sequence dimension and finitely generated Z_p-module
structure results: **not checked**. Castella--Hsieh's Theorem A and
Remark 1.6 supply the named arithmetic input, not a Mathlib match;
the additional Kummer implications are proved above. No rank-two
point-existence or Sha-finiteness theorem is being assumed.
