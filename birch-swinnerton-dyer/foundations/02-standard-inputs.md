# Standard inputs for the first descent audit

## Established boundary

Mordell's finite-generation theorem gives E(Q) = Z^r direct-sum T, with T
finite. Modularity of elliptic curves over Q gives the analytic continuation
used in the target. The Gross–Zagier–Kolyvagin theorem, together with
modularity, proves r(E) = m(E) when m(E) is 0 or 1. These named inputs are
recorded in [Wiles's official description, printed pages 1, 2, and 4](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf).
The low-rank hypothesis here is **analytic** rank. These are sufficient
baseline results for this step, not an exhaustive survey of later work.

## Selmer and Tate–Shafarevich groups

For n >= 1 and a prime p, E[p^n] denotes geometric p^n-torsion. Define

\[
\begin{aligned}
\operatorname{Sel}_{p^n}(E/\mathbf Q)
 &=\ker\!\left(H^1(\mathbf Q,E[p^n])
                 \longrightarrow\prod_v H^1(\mathbf Q_v,E)\right),\\
\Sha(E/\mathbf Q)
 &=\ker\!\left(H^1(\mathbf Q,E)
                 \longrightarrow\prod_v H^1(\mathbf Q_v,E)\right).
\end{aligned}
\]

The product includes the real place. The first map composes localization
with E[p^n] -> E; thus its kernel imposes the local Kummer conditions.
For an abelian group A, A[p^n] is the subgroup killed by p^n and
A[p^infinity] is the union of these subgroups.

The Kummer exact sequence is

\[
0\longrightarrow E(\mathbf Q)/p^nE(\mathbf Q)
\longrightarrow\operatorname{Sel}_{p^n}(E/\mathbf Q)
\longrightarrow\Sha(E/\mathbf Q)[p^n]\longrightarrow0.
\]

It does **not** require finiteness of the whole Tate–Shafarevich group.
The Selmer group at each fixed level is finite. Precise references:
J. S. Milne, *Elliptic Curves*, second edition (2021),
[Chapter IV, equation (29), printed page 113](https://www.jmilne.org/math/Books/EC2.pdf#page=118),
and [Theorem IV.3.1, printed page 114](https://www.jmilne.org/math/Books/EC2.pdf#page=119).

The downward map on Selmer groups induced by
[p]: E[p^(n+1)] -> E[p^n] acts by reduction on the rational-point quotients
and by multiplication by p on Sha. This is the diagram on
[Milne, printed page 129](https://www.jmilne.org/math/Books/EC2.pdf#page=134).

## Pairing and the existing descent limitation

Cassels's alternating pairing on Sha takes values in Q/Z and has divisible
subgroup as its kernel: [Milne, Theorem IV.5.4, printed page 130](https://www.jmilne.org/math/Books/EC2.pdf#page=135).
In particular, if the p-primary part is finite, the pairing restricted to
that part is nondegenerate. Nondegeneracy on the entire finite p-primary
group does not assert nondegeneracy on its p^n-torsion subgroup.

[Milne, Proposition IV.5.1 and Remark IV.5.2, printed pages 129–130](https://www.jmilne.org/math/Books/EC2.pdf#page=134)
already explain the higher-descent strategy. Under finiteness of Sha[p^infinity],
the images of Sel_{p^n} in Sel_p eventually equal the rational Kummer image.
This qualitative eventual statement supplies no numerical stopping depth.
The local finite-tower test is an explicit audit of this known issue, not a
claim to have discovered a new general obstruction theorem.

## Mathlib

Full coverage of these arithmetic inputs: **not checked**. The cited texts
supply standard mathematical inputs, not Mathlib theorem matches.
