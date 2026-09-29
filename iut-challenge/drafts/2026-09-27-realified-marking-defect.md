# Realified marked localization — 2026-09-27

Completed one research step under the prior [SPECIALIZE assessment](literature/2026-09-26-current-target.md). Initial reasoning was saved before the full proof. Existing notebook changes are retained.

## Gap and test

The main gap is finite B ≥ A in IUT III, Corollary 3.12(xi-f). The intermediate question is whether the global object, local marking orbits, and realified localization isomorphisms in (cQ3) retain the defect measured by L005. A formula in these retained data could support a later test of marked q-pilot transport. The formal quotient, log-Kummer transport, hull, full initial data, and numerical normalization remain separate obligations.

Continue if the defect has a well-defined expression in a specialization of the cited Frobenioid construction, compatible with the localization diagrams and agreeing with L005 on its image. Abandon this invariant if its value depends on a discarded choice. The sufficient sign threshold remains δ ≥ 0, while the exact model inequality is d(input) ≤ d(output) − δ. Repeating the old category-axiom counterexample or just allowing real lattice exponents would not meet this test.

## Construction and result

Use the arithmetic fiber over ℚ and arrows over identity base maps, with the standard arithmetic degree normalization. Frobenioids I, Theorem 5.2(i), gives a model arrow by nα + E = β + h, where E is effective. Proposition 5.3 supplies the realified global rational-function space, whose degree quotient is imported from Theorem 6.4(i). Frobenioids II, Example 5.6(iii)–(iv), supplies restriction to each local divisor coordinate. This tests the cited arithmetic construction without asserting an equivalence with the full IUT prime-strip.

For a collection (G, X_v, [m_v], ι_v), compose the realified local marking with ι_v : loc_v(G) ≅ X_v^rlf. An isomorphism has zero divisor. The effective divisor e_v of this composite equals that of m_v and is unchanged by target automorphisms. The defect is

δ = d(D) − d(G) − Σ_v e_v.

The full proof is [L006](../lemmas/L006-marking-defect-in-realified-localization.md). It constructs the functor from L005 and proves δ = Δ on its image. It checks the source's corrected archimedean sign, compatibility with the localization squares, invariance under target-unit orbits, and changes of global and local representatives. The separate local contact functor is compared after realification; it is not confused with the global contact functor. The global arithmetic degree theorem is imported without reproof.

The invariant survives in the complete arithmetic collection even though every local realified fiber has just one isomorphism class over the fixed base object. A family with all local objects equal to the target and all local markings the identity still realizes every defect value by varying the global object. This exposes precisely why local triviality does not eliminate the global discrepancy. It also explains why a sum of raw local marking scalars alone is inadequate when the localization identifications are allowed to vary.

## Scope and route decision

Outcome: ADVANCE, limited to a relevant local specialization. Classification: REPRODUCTION. The source constructions cover the global degree and local models; the completed calculation relates the previously separate marked-category invariant to those constructions. No result beyond the checked literature is claimed. This is neither an improved numerical bound nor a demonstrated IUT flaw.

The discriminating test succeeds in the arithmetic fiber over ℚ, with identity base maps and finite support. It does not establish an equivalence with the entire prime-strip, include arbitrary changes of base, or analyze log-Kummer transport. In particular, a defect constant along the marked-category arrows is not automatically a function on the formal quotient (fQ2) modulo (fQ1). The required finite B ≥ A remains unestablished and unrefuted.

The reason for the subsequent direction is now precise: local realification alone does not remove the defect, so the effect of the formal quotient and the actual comparison identifications must be assessed. That new target has a REVIEW_REQUIRED assessment; no work on its mathematics was performed here. The sole concrete action is in PROGRESS.md. No full candidate exists.

Exploration usage is 0 since this local ADVANCE; the preceding sequence used 1. The historical 3/3 sequence remains assessed. No runner state was edited.

## Checks

The mathematical checks are exact: the model-arrow relation, addition of divisors under linear composition, zero divisor for isomorphisms, the degree-zero global parameter, cancellation in the localization diagrams, agreement with the original finite and real norms, and the family attaining each defect value. No numerical experiment or new mathematical script is needed. The only new DAG input is L005, whose category is mapped by the construction; global and local Frobenioid inputs are named citations. Mathlib coverage remains not checked.
