# L003 — Cyclotomic height and augmentation semisimplicity

## Hypotheses

Let E/Q be an elliptic curve and p an odd prime of good ordinary reduction.
Use the classical cyclotomic Selmer dual X and Lambda = Z_p[[T]] from
[the control foundations](../foundations/03-cyclotomic-control.md). Put

\[
\begin{gathered}
A=\Lambda_{(T)},\qquad M=X\otimes_\Lambda A,\qquad
\eta:M[T]\longrightarrow M/TM,\quad x\longmapsto x\bmod TM,\\
r=\operatorname{rank}E(\mathbf Q),\qquad
h=\operatorname{ord}_T f_X,\qquad
D=\Sha(E/\mathbf Q)[p^\infty].
\end{gathered}
\]

Let R_p(E) be the determinant of the canonical cyclotomic ordinary p-adic
height, with the conventions and precisely scoped named theorem in
[the height foundations](../foundations/04-cyclotomic-height-criterion.md).
No finiteness of D or nonvanishing of R_p(E) is part of these base
hypotheses; the additional assumptions for each implication are explicit.

## Conclusion

First, without a height assumption,

\[
h=r\quad\Longleftrightarrow\quad
\bigl(D\text{ is finite and }\eta\text{ is an isomorphism}\bigr).
\tag{1}
\]

Second, the arithmetic height criterion supplies the sufficient condition

\[
D\text{ finite and }R_p(E)\ne0
\quad\Longrightarrow\quad
h=r,\quad TM=0,\quad
M\simeq(A/(T))^r,\quad\eta\text{ an isomorphism}.
\tag{2}
\]

If E additionally has no complex multiplication and D is finite, the
checked converse gives

\[
R_p(E)\ne0\quad\Longleftrightarrow\quad
\eta\text{ is an isomorphism}.
\tag{3}
\]

The non-CM restriction in (3) preserves the scope of the particular
converse source checked here; it asserts no failure in the CM case.
These conclusions establish a conditional arithmetic criterion, not
rank equality with the complex analytic order m(E).

## Proof

**Corank zero is finiteness in this setting.** L002 identifies
D^vee as a submodule of the finitely generated Z_p-module S_0^vee, where
S_0 is the base p-primary Selmer group. Thus D^vee is finitely generated
over Z_p. By the structure theorem over the discrete valuation ring Z_p,

\[
D^\vee\simeq\mathbf Z_p^s\oplus F,
\]

where s = corank_Zp D and F is finite. Hence s = 0 if and only if D^vee
is finite. Pontryagin duality for discrete p-primary groups and compact
Z_p-modules identifies D with its double dual, so this is equivalent to
D being finite. This argument uses finite generation; it is not a
statement about arbitrary infinite p-primary groups of unspecified type.

**The exact threshold.** L002 gives

\[
h=r+s+\delta,\qquad
\delta=\operatorname{length}_A(TM)\ge0,\qquad s\ge0,
\]

and proves delta = 0 if and only if eta is an isomorphism, equivalently
TM = 0. Therefore h = r holds exactly when s = delta = 0. The preceding
paragraph converts s = 0 to finiteness of D and proves (1).

**Importing the arithmetic input.** Now suppose D is finite and R_p(E)
is nonzero. Apply the Schneider--Perrin-Riou theorem as stated in Ray,
Theorem 3.4, with K = Q. The hypotheses on p and reduction are the present
ones; its regulator hypothesis is nonvanishing, unchanged by the nonzero
normalizing scalar. Its finite-generation and cotorsion hypotheses for
the classical Selmer dual are supplied by the control foundations. Thus
the theorem applies to f_X and gives h = r.

Equation (1) then gives TM = 0 and the asserted property of eta. The
module decomposition in L002 is a direct sum of A/(T^e_i), and TM = 0
forces every e_i to be 1. The number of summands is h = r, proving the
stated isomorphism of M and completing (2), including r = 0.

**Converse in the checked scope.** Assume now that E is non-CM and D is
finite. If eta is an isomorphism, (1) yields h = r. Stein--Wuthrich,
Theorem 6.1, then implies nondegeneracy of the cyclotomic height and
therefore R_p(E) != 0. This invocation retains the paper's standing
non-CM hypothesis as well as p > 2 and good ordinary reduction. The
reverse implication follows from (2), proving (3).

**Meaning of the result.** The map eta is canonical, but the proof does
not identify the height pairing with eta itself: it passes through the
named order theorem and the exact defect calculation. It does not give
an identification of their radicals or a numerical formula for delta
from a degenerate height. Finite Sha alone leaves delta uncontrolled;
height nonvanishing alone is not substituted for the missing finiteness
hypothesis in (2). No complex or analytic p-adic L-function enters the
proof.

Without the extra arithmetic assumptions the achieved comparison remains
r <= h. With them it reaches the exact algebraic threshold h = r. The
target is still r = m(E) for every E/Q: neither these hypotheses at a
suitable prime for each curve nor a comparison h = m(E) is established.
This is an application of standard theorems to the isolated defect, not
a new general height nondegeneracy theorem or a candidate BSD resolution.

## Mathlib

Full statement, including the height implication and its arithmetic
scope: **not checked**. Supporting finite-generation, Pontryagin-duality,
and DVR-module facts: **not checked**. No library absence or full theorem
match is claimed. Precise published theorem names, sections, direct links,
and the limitation on access to the original source are retained in the
height foundations; the deductions from L002 are proved above.
