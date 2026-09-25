# Cyclotomic Selmer control

## Conventions

Fix an elliptic curve E/Q and an odd prime p at which E has good ordinary
reduction. Let Q_infinity/Q be the cyclotomic Z_p-extension, with degree-p^n
layer Q_n. Put Gamma = Gal(Q_infinity/Q), choose a topological generator
gamma, and identify

\[
\Lambda=\mathbf Z_p[[\Gamma]]=\mathbf Z_p[[T]],\qquad T=\gamma-1.
\]

Write S_0 = Sel_{p^infinity}(E/Q) for the classical p-primary Selmer group,
S_infinity = Sel_{p^infinity}(E/Q_infinity), and
X = Hom_cont(S_infinity,Q_p/Z_p) for its Pontryagin dual. The Selmer groups
are discrete; X is compact. At a finite layer the p-primary Selmer group is
the direct limit of the p^a-Selmer groups under the maps induced by inclusion
E[p^a] into E[p^(a+1)]. At the infinite layer take the direct limit under
restriction along Q_n. These conventions are those of
[Greenberg, *Iwasawa Theory for Elliptic Curves*, printed pages 3-5](https://arxiv.org/pdf/math/9809206#page=3).

For a discrete p-primary group D with finitely generated Z_p-dual, define
corank_Zp D = dim_Qp(D^vee tensor_Zp Q_p).

## Named arithmetic inputs

**Mazur's Control Theorem:** for every n, restriction
Sel_{p^infinity}(E/Q_n) -> S_infinity^(Gal(Q_infinity/Q_n)) has finite
kernel and cokernel, bounded in order as n varies.
See [Greenberg, Theorem 1.2, printed page 4](https://arxiv.org/pdf/math/9809206#page=4).
Only n = 0 and finiteness of these errors are used here.

The dual X is finitely generated over Lambda. Modularity of E/Q and the
**Kato–Rohrlich cotorsion theorem** make it a torsion Lambda-module in this
good-ordinary setting. See [Greenberg, Theorem 1.5 and the preceding finite-generation discussion, printed page 5](https://arxiv.org/pdf/math/9809206#page=5).

The direct limit of the finite Kummer sequences in
[the standard inputs](02-standard-inputs.md) gives

\[
0\longrightarrow E(\mathbf Q)\otimes\mathbf Q_p/\mathbf Z_p
\longrightarrow S_0
\longrightarrow\Sha(E/\mathbf Q)[p^\infty]\longrightarrow0.
\]

No finiteness of Sha is assumed. The direct-limit and corank calculation
used below is written out in L002.

## The additional condition is not a control conclusion

[Greenberg, Conjecture 1.12 and its discussion, printed pages 8-9](https://arxiv.org/pdf/math/9809206#page=8),
separates complete reducibility of the rationalized Iwasawa module from
control. L002 isolates only the condition at the prime (T). The source's
conjecture is not imported as a theorem. No Iwasawa main conjecture or
comparison of complex and p-adic vanishing orders is used in this audit.

## Mathlib

Full coverage of good-ordinary control, cotorsion, and the Selmer conventions:
**not checked**. The named results above are mathematical references, not
claims of corresponding Mathlib theorem matches.
