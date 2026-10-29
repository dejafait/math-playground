# Same-prime plectic localization: source coverage

Literature-only step 512, 2026-10-26. No new mathematical result is
claimed. The main gap remains arbitrary rational rank versus complex
order, with rational Kummer membership and nonvanishing still missing
even for the proposed strict-class route. The reviewed intermediate
target is the viability of a same-prime localization test on the actual
partially global class, not an import of its conjectural determinant.

## Sources and exact scope

Primary source: Michele Fornea, *Plectic Heegner classes*,
[arXiv:2603.28327v2, 13 April 2026](https://arxiv.org/html/2603.28327v2).
Newly inspected: Sections 4.1 and 4.2, including Theorem 4.13 and its
proof, Definition 4.17 and Proposition 4.18 with proof; Section 4.3's
action formula (64) and Theorem 4.22 with proof; Definition 4.23 and
Corollary 4.24 with proof; Sections 5.1.3–5.1.7, Proposition 5.9 with
proof, Remark 5.10, Corollary 5.12, and the complete Section 5.4 proof
of Theorem 5.3. Corollary 5.12's statement and its use were inspected;
this is not an independent audit of all its auxiliary proofs. Earlier
Theorems A–C/hypothesis coverage is reused from step 511's source notes.

Notation here: the curve is A/Q, the imaginary quadratic field is K
(the source calls it E), V=V_p(A), and U=H_f^1(K_p,V). Take
cal S={p}, auxiliary w=infinity, conductor one, trivial character.
The conductor is unramified in K; its inert part is square-free;
Definition 1.2's incoherence parity holds; p>=5 is inert and
multiplicative; residual image contains SL_2(F_p). For the comparisons
retain Assumption 1.5: each split-conductor exponent is at most two;
the inertia-degree/different conditions are automatic over Q. Do not
replace multiplicative reduction by good ordinary reduction.

## The actual defining operations

The following formulas are source definitions, not new lemmas.
For gamma represented by [(x_gamma,y_gamma),z_gamma], Section 4.1 sets

\[
 f_{\tau,\varpi}(\gamma)
 =\tfrac12\log_{\varpi}((x_\gamma-\tau y_\gamma)^2/z_\gamma).
\]

Definition 4.8 supplies a measure on X_v, v=red(tau), with its
coefficient twist chi(g_v). Equation (54) defines

\[
 \varphi^{\Box}_{\varpi}(h)(\tau_S)
 =\int_{\mathbb X_v}f_{\tau,\varpi}(\gamma)
       \,d\mu^{\varpi,\Box}_{(\tau_S,h)}(\gamma).
\]

At CM points Remark 4.20 permits v to be the standard vertex and
g_v=1. The integration convention preceding (54), or equivalently
(55), must still be used when changing the CM representative.
Definition 4.17 then applies exp_q^Tate tensor pr_A to the integral
after Hecke localization. Equation (63) defines pr_A on the
diamond-invariant subspace, not on arbitrary measure coefficients.
Corollaries 4.15–4.16 supply diamond invariance and independence of
uniformizers. Remark 4.11 explicitly requires integration before
Hecke localization. Corollary 4.24, equation (68), finally takes the
finite CM sum and supplies descent to L_1. Trivial-character descent
to K must be retained; L_1 need not equal K.

Thus an operational expression for the proposed diagnostic is:
perform (54), (63), Definition 4.17 and (68), descend the trivial
character factor, and only then project and localize. A purported
formula using pr_A on individual values of mu is not licensed by
these definitions. We have not constructed such a coefficient map.

## Actions and the exact unproved diagnostic

Theorem B acts by sigma_p on U, leaving the global tensor factor
alone. Section 1.1.1 identifies this with the natural nontrivial
Gal(K_p/Q_p)-action on H_f^1(K_p,V), with the curve's reduction sign
epsilon_p entering the projector 1-epsilon_p sigma_p. On a nonsplit
Tate model one must check the twist before identifying this action
with field conjugation of a scalar logarithm.

Let kappa_0 denote the trivial-character class after descent to
U tensor H^1(K,V). Define e_l^+=(1+sigma_p)/2 on U and
e_g^+=(1+c)/2 on global cohomology, where c is the outer conjugation
action of Gal(K/Q). For a fixed embedding at the unique inert prime,
the proposed quantity remains exactly

\[
 D^{++}=(1\otimes\operatorname{loc}_p)
           (e_l^+\otimes e_g^+)\kappa_0
 \quad\in U^+\otimes H^1(K_p,V).
\]

This is the definition of the test, not a zero identity or a claim of
local finite membership of the second factor. Source equation (64)
describes rec_K(u) for u in the anticyclotomic torus over K; it is not
a formula for the action of c on the complete integral. The source
does not state the c-transformation/cancellation required here.
A subsequent attempt must check restriction/conjugation compatibility
with actual cochain lifts, and derive any integral transformation it
uses. Neither the word plectic nor a hypothetical interchange of the
tensor factors supplies it.

## What the proved comparison controls

Theorem 5.3 identifies the restriction to degree-zero divisors in the
cal S-variable with the older Abel–Jacobi construction. In its complete
Section 5.4 proof, the difference of integrands and the change of
measure are separate summands. Corollary 5.12 and Proposition 2.28's
logarithmic U-eigenvalue derivative provide the Tate-parameter
correction; it is not legitimate to drop the second summand.
Proposition 5.9/Remark 5.10 likewise concern integrals after Hecke
localization, not an unconditional equality of coefficient measures.

Its mock consequence is precisely Theorem B's
(1-epsilon_p sigma_p)kappa=Q. Lemma 5.4's retraction argument instead
requires an auxiliary p-adic w outside cal S. Over Q with cal S={p}
it is not a same-prime local-finiteness argument. Theorem 4.13 requires
a constant component at an omitted integration coordinate; its
statement does not assert vanishing of the full logarithmic kernel.

Reuse the mock Selmer/rationality comparison from step 511. For an
action check, additionally inspected [Fornea–Gehrmann,
arXiv:2311.03100v2](https://arxiv.org/html/2311.03100v2), Corollary 2.9
with proof and Section 2.2.5, equations (10)–(13): its conjugation
eigenspace statement is for the projected mock invariant. Extending
it to the retained component is not a cited theorem. Proposition
2.11 gives Selmer membership of that mock class when the indicated
central L-value vanishes; it does not assert zero localization.

## Review decision and bounded continuation

No inspected theorem imports D^{++}=0. There is, however, an actual
unprojected integral, so the diagnostic is not merely a renaming of
Conjectures 1.9–1.10: it asks for zero localization of one specified
component, without first claiming Selmer membership of the entire
class or identifying it with points. We approve only bounded
exploration of this question, not the proposed vanishing assertion.

Concentrate next on split multiplicative p, where the plus component
is retained rather than recovered by Theorem B. The proposed test is
a transformation of the complete invariant integral under c and
local conjugation; retain the symmetrized logarithmic kernel and all
measure terms. Continue with an explicit proved cancellation or a
specific residual arithmetic term. Abandon this cancellation route
if its crucial equality is just conjectural determinant rationality,
if pr_A must be applied outside its defined domain, or if no
independently testable residual term survives the bounded attempt.
No computation or such transformation has been performed this turn.

Even successful strictness would require nonzero rational Kummer
membership, a justified multiplicative-prime replacement for L005,
and an independent complex-order comparison. No finite Sha premise
is supplied. This is local source progress, not a new BSD case.
Mathlib coverage for the full construction and diagnostic: not checked.

Searches: exact title with localization, complex conjugation, same
prime, same-prime, symmetric, and Selmer localization. Inspected the
primary text, not search snippets. A MathDB result relabels the
source's Conjecture 1.9 as a criterion; it is not theorem evidence.
Notebook-local searches of ATTEMPTS and the literature/source-note
folders found no separate same-prime proof. ATTEMPTS/003, /004, /030,
/058 remain relevant rationality warnings, not bans on this test.
