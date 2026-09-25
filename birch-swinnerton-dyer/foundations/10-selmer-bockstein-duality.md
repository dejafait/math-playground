# Ordinary Selmer complexes and the first Bockstein

Checked 2026-09-25. Work over F = Q_p, with p > 3, and V = V_p E
at good ordinary reduction. The base field K is imaginary quadratic
with p split. A superscript minus on a local quotient below denotes
the ordinary quotient, not a complex-conjugation eigenspace.

## Standard inputs and conventions

Use the ordinary filtration 0 -> V_v^+ -> V -> V_v^- -> 0 at v | p.
For a first-order character xi = 1 + epsilon d, deform this filtration
by tensoring every term with xi. Let A = F[epsilon]/(epsilon^2).
At v | p use the local cochain complex C(G_v,V_v^+ tensor xi).
Away from p use the unramified condition. Let C_f(V tensor xi) be
the mapping fiber of global and permitted local cochains mapping to
all local cochains. Its H^1 is denoted S_A. Here "ordinary" describes
this deformed local condition; it does not assert that the deformation
is a crystalline representation. At epsilon = 0 the condition equals
the usual finite/Kummer condition.

The named input is **Poitou--Tate duality for Selmer complexes**:
Jan Nekovar, *Selmer complexes*, Asterisque 310 (2006), Theorem 6.3.4;
the Bockstein construction is Section 11.1.3, and comparison with
ordinary Selmer groups is Lemma 9.6.3. [Original volume](https://www.numdam.org/item/AST_2006__310__R1_0/).
The web reader could not load its 43 MB PDF; the accessible account
checked here is Kazim Buyukboduk, *Height pairings, exceptional zeros
and Rubin's formula: the multiplicative group*, Definitions 2.1--2.2,
Propositions 2.3 and 2.5, Remark 2.6, and Section 2.1.3,
[printed pages 77--80](https://ems.press/content/serial-article-files/43278#page=7).
Only its general formalism is used, not its later multiplicative-group
specializations. This is a supporting reference, not the full statement
of L009.

For self-dual finite local conditions, the Weil pairing and global
duality give, after inverting p,

\[
H^2(C_f(V))\simeq H^1(C_f(V))^\vee.
\]

This is equivariant under automorphisms of K; the scalar invariant map
in global duality is invariant under complex conjugation. It does not
require finite Sha. In the present good-ordinary setting there are no
extra local H^0 terms: the ordinary quotient has unramified Frobenius
eigenvalue alpha (up to the Frobenius convention), where alpha != 1.
Indeed alpha = 1 in X^2-a_p X+p would imply a_p = p+1, contradicting
Hasse's bound. Thus H^0(K_v,V_v^-) = 0. The identification of H^1 of
the Selmer complex with the ordinary Selmer group is the comparison
just cited. The local and global checks are written out in L009.

The exact coefficient sequence 0 -> epsilon V_A -> V_A -> V -> 0
gives a connecting map beta_f: H^1(C_f(V)) -> H^2(C_f(V)) after
identifying epsilon V_A with V. Its kernel is the image of S_A.
One must keep epsilon's conjugation action when discussing signs.

## Independent check against the anticyclotomic height source

Castella--Hsieh, [Theorem 4.1(a),(d), printed pages 19--20](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=19),
gives the first-height radical and conjugation sign, retaining its
squarefree and residual ramification hypotheses. Their [Section 5.4,
equations (5.6)--(5.8), printed page 27](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=27)
already uses the vanishing of odd heights in the (2,0) Selmer setting.
This checks the symmetry conclusion; it is not a new height theorem
and does not establish the strict local derivative or point membership.
The vanishing Sel(Q,V_p E^K) = 0 used here is also explicit in the
proof of their [Lemma 5.1, printed page 25](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/72ED842AB428A7ED619B1B84287A6864/S2050509421000852a.pdf/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2.pdf#page=25),
under the auxiliary central-value hypothesis. This is the standard
analytic-rank-zero theorem (including finite Sha) for the quadratic twist;
no corresponding finiteness for E/Q is imported.

## Mathlib

Full coverage of Selmer-complex duality, the comparison, and the
Bockstein construction: **not checked**. Supporting results on
mapping cones, connecting homomorphisms, and eigenspaces: **not checked**.
The named sources support the stated arithmetic formalism; no source
match for a Kummer-membership criterion is asserted.
