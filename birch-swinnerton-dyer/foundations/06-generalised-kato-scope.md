# Generalised Kato classes: source scope and the point gap

Checked 2026-09-25 against Henri Darmon and Victor Rotger,
[*Elliptic curves of rank two and generalised Kato classes*, Research in
the Mathematical Sciences 3 (2016), article 27](https://link.springer.com/article/10.1186/s40687-016-0074-9).
The references below use the published 32-page version, not the shorter
author manuscript. This is a paraphrased source audit with additional
deductions identified as such. The article is available under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Analytic-order convention

The paper uses the primitive complex L-function. Its order at s = 1
equals the notebook's m(E), which omits finitely many Euler factors.
Indeed, a good-prime inverse Euler factor has value
1-a_q/q+1/q = #E(F_q)/q != 0; a multiplicative one has value
1-1/q or 1+1/q; an additive one is 1. Thus the finite product of
removed inverse factors is holomorphic and nonzero at s = 1.
This identifies only the two complex conventions, not a p-adic order.

## Construction hypotheses retained

Sections 2 and 3.1 start with E/Q and two odd irreducible two-dimensional
Artin representations rho_1,rho_2 over a number field L, with reciprocal
determinants. Their weight-one forms are g,h; f is the weight-two form
of E. Write V_gh = V_g tensor V_h and V_fgh = V_p(E) tensor V_gh,
using the paper's Tate-twist conventions.

The paper's hypotheses (I)--(IV) require: p splits completely in L with
a chosen embedding into Q_p; each Artin representation is unramified
at p; its two Frobenius eigenvalues are distinct; and it is not induced
from a real quadratic field in which p splits. Also p does not divide
lcm(N_f,N_g,N_h), and the conductor of V_gh is coprime to that of E.
Coefficient fields contain the Frobenius eigenvalues. Projections pi
from the representations at the chosen common level are part of the
construction. No assertion that these choices are uniformly available
with every additional desired nonvanishing condition is imported.

Non-CM E and good-ordinary p >= 5 are additional restrictions when
connecting this construction with the notebook's L004 certificate.

## Proved statements and conjectures distinguished

[Theorem 3.1, Section 3.2](https://link.springer.com/article/10.1186/s40687-016-0074-9)
states, in the preceding setting, that all four classes for every
allowed pi lie in the Bloch--Kato Selmer group if and only if
L(E,V_gh,1) = 0. Membership alone supplies no nonzero class.

[Corollary 3.6, printed page 17](https://link.springer.com/content/pdf/10.1186/s40687-016-0074-9.pdf#page=17)
adds a useful but different conditional conclusion. If L(E,V_gh,1) = 0
and the triple-product value mathscr L_p^(g_alpha)(breve f,breve g*,breve h)
is nonzero for suitable test vectors, then kappa(f,g_alpha,h_alpha) and
kappa(f,g_alpha,h_beta) are independent in H^1_fin(Q,V_fgh), for a
suitable pi. This is a twisted Selmer space. Neither the extra
nonvanishing nor a two-dimensional rational Kummer image follows in
the source merely from m(E) = 2. The triple-product value is not the
degree-two coefficient of L004's cyclotomic L_p(E,T).

Conjecture 3.2 and Remark 3.3 explicitly place the equivalence between
analytic order two, Mordell--Weil multiplicity two, and Selmer dimension
two within the conjectural BSD comparison. Remark 3.3 does not even
predict that the four classes span that Selmer space. Conjecture 3.12
adds Mordell--Weil membership and an enhanced-regulator identity in
the rank-two setting; it is not a rational-point existence theorem.
See [the published statement, printed page 20](https://link.springer.com/content/pdf/10.1186/s40687-016-0074-9.pdf#page=20).
The two modular Selmer classes in the quoted Skinner--Urban Theorem 1.3
are also not asserted there to belong to the rational Kummer image;
that quoted theorem is not separately imported in this step.

## Adjoint rank-(2,0) test

In Section 4.5 take h dual to g. Then V_gh = Q_p direct-sum Ad^0(V_g)
and the complex L-function factors as L(E,s)L(E,Ad^0(V_g),s).
The relevant analytic rank-(2,0) case requires m(E) = 2 and the auxiliary
value L(E,Ad^0(V_g),1) != 0. Selecting a trivial summand does not itself
prove that the projected classes are nonzero or globally Kummer.

[Section 4.5.3, printed pages 30--31](https://link.springer.com/content/pdf/10.1186/s40687-016-0074-9.pdf#page=30)
already assumes a basis P,Q of the two-dimensional Mordell--Weil space.
Its enhanced regulators satisfy

\[
\widetilde{\operatorname{Reg}}_{\alpha\alpha}
=\widetilde{\operatorname{Reg}}_{\beta\beta}
=\log_p(P)Q-\log_p(Q)P,\qquad
\widetilde{\operatorname{Reg}}_{\alpha\beta}
=\widetilde{\operatorname{Reg}}_{\beta\alpha}=0.
\]

Our deduction: even granting the conjectural identification with these
regulators, the four stabilisations span at most one line. These
formulas therefore cannot be used as a construction of two independent
points from analytic rank alone. They also do not rule out a different
use of that line: L005 proves that a nonzero *globally Kummer* class
with zero localization at p already forces rational rank at least two.
The source audit establishes neither required property from m(E) = 2.

This rejects a direct import of the 2016 construction into L004's point
input. It neither refutes the construction's conjectures nor rules out
later results or additional arithmetic input.

## Mathlib

Full coverage of the generalised Kato construction, Theorem 3.1,
Corollary 3.6, and the rational Kummer identification: **not checked**.
No conjecture above is imported as a theorem. The cited results support
the scope audit, not a match for the missing two-rational-point claim.
