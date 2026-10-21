# L014 — The degree-nine coarse enclosure holds for every strict nonunit scalar

## Hypotheses

Use K = Q_3(pi), pi^9 = 3, O = O_K, J = log(O^times), I = J/6, beta = 1 and G the Q_3-linear extensions of Aut_(Z_3)(I), as in L012. Normalize v_3(3) = 1 and |x|_3 = 3^(-v_3(x)). For a subset Y of K, GY is the union of g(Y) over g in G; hull(Y) is the smallest closed K-ball centered at zero containing Y.

Let a be any nonzero element of K with |a|_3 < 1, and put n = floor(v_3(a)). The separate unnumbered post-chain prescription in [Dupuy–Hilado, arXiv:2004.13108v2, §6.2, printed p. 20](https://arxiv.org/pdf/2004.13108v2#page=20) is

\[
C_{\rm coarse}(a)=D_K\left(0,\frac{\prod_i e_i}{|2p|_p}
p^{-\lfloor v_p(a)+\|\mathrm{diff}\|_\infty-\|\mathrm{diff}\|_1\rfloor}\right).
\]

The [prior SPECIALIZE assessment](../drafts/literature/2026-10-04-uniform-scalar-coarse-enclosure.md) covers every such a in this fixed one-factor packet. No original initial-theta-data realization, complete IUT image family or normalized A/B comparison is assumed.

## Conclusion

For every allowed a, including every unit factor in a,

\[
G\bigl(a(O\cup J)\bigr)\subseteq 3^n(I/3),\qquad
\operatorname{hull}\bigl(G(a(O\cup J))\bigr)
\subseteq 3^n\pi^{-27}O=C_{\rm coarse}(a).
\]

The achieved uniform upper radius and the required coarse radius are both 27 times 3^(-n). Equality of the full orbit with 3^n(I/3), and hence equality of its hull with the coarse container, holds for a = 3^n pi for every integer n >= 0. Thus the uniform constant 27 cannot be decreased in this packet.

This reproduces the source's coarse containment in the fixed field by an independent proof. It does not repair the stronger literal endpoint or rounded-hull assertions, or demonstrate an essential IUT flaw.

## Proof

L012 supplies the exact facts

\[
H=\pi^5O\subseteq J,\qquad
v_3(y)\geq-1\ (y\in J),\qquad
\operatorname{hull}(I)=\pi^{-18}O,
\]

and G(pi(O union J)) = I/3. The ideal inclusion follows from the log/exp bijection above valuation 1/2, and the minimum -1 follows from L012's full logarithm lattice, not from a sampled set of units. These are reused rather than recomputed.

Write a = 3^n b. Then 0 <= v_3(b) < 1; since K has value group (1/9)Z, b = pi^k u for k in {0,...,8} and u in O^times. If k = 0, strict nonunitness of a requires n >= 1. The proof below also covers that integer-floor boundary. It uses only v_3(b), so every u is included without assuming uJ = J or uI = I.

For z in O and y in J, valuation additivity gives

\[
v_3(18bz)\geq 2+v_3(b)\geq2,\qquad
v_3(18by)\geq2+v_3(b)-1\geq1.
\]

Zero presents no exception. Both lower bounds exceed 5/9, so

\[
18b(O\cup J)\subseteq H\subseteq J.
\]

Because I/3 = J/18 as sets, this is the genuine inclusion b(O union J) subset I/3. Here only the ideal H is used as an O-module; no O-module structure on J is inferred.

Every g in G preserves I/3: it preserves I and is Q_3-linear. The same linearity permits commuting the rational scalar 3^n, giving

\[
g\bigl(a(O\cup J)\bigr)
=3^n g\bigl(b(O\cup J)\bigr)\subseteq3^n(I/3).
\]

Taking the union over the entire group proves the first conclusion. Scaling the known hull of I by 1/3 gives hull(I/3) = pi^(-27)O, of radius 27. Rational scaling by 3^n gives its hull radius 27 times 3^(-n).

There is one ramification index e_1 = 9. The different vector has one entry, so its infinity and 1-norms agree, independently of that entry's value. Also |2p|_p = |6|_3 = 1/3. The source's coarse radius is therefore exactly

\[
\frac{9}{1/3}\,3^{-\lfloor v_3(a)\rfloor}=27\,3^{-n}.
\]

Its closed ball is 3^n pi^(-27)O. This proves the comparison at the actual required threshold without using the suspect rounded chain or treating field scalars as commuting with G.

For sharpness take a = 3^n pi, n >= 0. Its valuation floor is n, and Q_3-linearity together with L012 gives

\[
G\bigl(3^n\pi(O\cup J)\bigr)
=3^nG\bigl(\pi(O\cup J)\bigr)=3^n(I/3).
\]

L012's literal infinite-log witness pi log(1+pi) has a G-image of radius 27. Multiplying it by 3^n gives a literal witness attaining radius 27 times 3^(-n); the boundary is attained, not merely approached.

### Source comparison and scope

The known prescription and supporting setup are imported by the version-qualified citation above. The missing specialization is an independent inclusion for every scalar and every unit factor, since the printed coarse assertion follows the audited chain. [Remark 4.3.3, printed p. 18](https://arxiv.org/pdf/2004.13108v2#page=18), cautions against treating the logarithm image as an O-module; the valuation-ideal argument avoids precisely that assumption. Classification is **REPRODUCTION**: the resulting fixed-field containment agrees with the known coarse assertion, and no result beyond the checked literature is claimed.

This completes and closes this field's uniform coarse-bound objection. The separate auxiliary terminal failure remains recorded; original initial data, pilot membership, full-image coverage, essentiality and finite B >= A are still unresolved. No theorem for other fields or tensor packets is inferred.

The nine possible residual valuations k/9 were checked with exact rational inequalities for the two branch lower bounds. The proof covers arbitrary units and the entire group; no logarithm recomputation or sampled automorphism test is needed.

## Mathlib

Full fixed-field uniform coarse-enclosure statement: **not checked**. Supporting local-field valuation, logarithm/exp, lattice and closed-ball results: **not checked**. The named source supplies the coarse prescription and supporting setup, not a matching Mathlib theorem or formal verification. No absence from Mathlib is inferred.
