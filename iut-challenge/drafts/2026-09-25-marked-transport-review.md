# Marked transport review — 2026-09-25

The initial reasoning and the intermediate local-global calculation were saved before completion. This one review obtained an informative negative result about the proposed local-marking test. The previous three-turn exploration sequence remains recorded as exhausted; no new exploration sequence or runner-state change is made.

## Gap, target, and discriminating test

The exact gap is still the inference to finite B ≥ A in IUT III, Corollary 3.12(xi-f), with A and B as fixed in the source record. This review examines the proposed marked transport, not another unmarked quotient model. The intermediate target is to type the local structure poly-morphism from the transported q-pilot to the output determinant in Remark 3.9.5(ix)(cQ3)–(cQ4), including its allowed ambiguity. A source-supported transport of that marking could isolate the remaining numerical realization problem; a demonstrable incompatibility could obstruct the inference. Neither implication is assumed.

The test is whether the actual cited construction specifies and preserves the marking on the distinguished input, or only closes a loop on the ambient prime-strip. Any proposed ordinary categorical replacement must preserve both the marking and the admitted pull-back morphisms. A missing construction in this review is not an IUT flaw. If the review yields no new source-specific evidence or useful mathematical correction, retain the stop and report STALLED, not a fourth exploration turn.

## Redundancy check and initial source observations

L001 concerns a fixed-valuation power map; L002 concerns unmarked path cancellation and common determinant normalization; L003 concerns subgroup collapse and membership of a distinguished degree class. Their limitations remain in force. ATTEMPTS/001–003 exclude repeating these as counterexamples to IUT. The new issue is the simultaneous retention of structure morphisms and unit/Galois actions during the actual formal transport.

The official announcement and prize page were rechecked on 2026-09-25 with unchanged scope. The author-hosted IUT III is still the 199-page May 2020 version. The initial source read locates the local structured objects at printed pp. 141–142, and distinguishes them from the passage to degrees at pp. 143–144.

## Source distinction: a local marking is not yet a global comparison

The exact local marking in (cQ3) is an Aut(D)-orbit of a Frobenioid-linear morphism X → D, where D is the indicated determinant of the output hull. The cited [Frobenioids I, Definition 1.2(i), p. 21](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I.pdf#page=21) defines linearity by Frobenius degree one, separately from the zero-divisor condition defining an isometry. The local-global objects in (cQ3) also include a global object and localization isomorphisms; morphisms must respect these. Thus merely finding local markings cannot substitute for constructing a compatible global morphism or another valid degree comparison.

The local-global typing makes the remaining obligation more precise. Write Q_gl for a proposed global input object, D_gl for the global output determinant, X_v for a proposed transported local input, and D_v for the local determinant. Let R_v denote local realification, and let λ_Q,v : R_v(X_v) → loc_v(Q_gl) and λ_D,v : R_v(D_v) → loc_v(D_gl) be the localization isomorphisms. In an ordinary realization, representatives f_v : X_v → D_v of the marking orbits would come from a global morphism h : Q_gl → D_gl only if

λ_D,v ∘ R_v(f_v) = loc_v(h) ∘ λ_Q,v

at every v, with the stipulated orbit ambiguities accounted for. This equation is a type-correct test for such a proposed realization, not an assertion that the source has constructed h or that IUT must admit this particular realization. For the original q-pilot, the choice of X_v and transport of its marking through (cQ4) also remain unchecked. The formal quotient could conceivably supply the numerical comparison without a single ordinary h.

## Completed local-global test

[L004](../lemmas/L004-local-markings-and-global-degree.md) proves the full statement. For ordinary rank-one lattice systems over ℚ and local marking multipliers c_v, put Δ(c) = Σ_v log |c_v|_v. The actual bound supplied by local inclusions is

d(input) + Δ(c) ≤ d(output).

The target-unit orbits preserve Δ(c). If all the local multipliers arise from one nonzero rational scalar, the product formula gives Δ(c) = 0 and therefore the desired direction of inequality. A nonnegative total defect would also suffice; a global scalar is only one sufficient mechanism.

The decisive example uses the globally defined metrized modules ℓℤ and ℓ²ℤ, with the usual real norm. Multiplication by ℓ at the prime ℓ and by 1 elsewhere, including infinity, gives local isomorphisms, preserves unit actions, and is compatible with finite local scalar extensions and Galois actions. Both objects have their ordinary global-to-local identifications. Nevertheless, their degrees are −log ℓ and −2 log ℓ, respectively. The total defect is −log ℓ. No nonzero rational scalar can give even contracting maps at every place: finite places force a nonzero integer divisible by ℓ, whereas infinity forces absolute value at most 1.

This addresses a different missing compatibility from the earlier tests. The maps are actual local linear lattice isomorphisms; no power-map renormalization is being used. The object data already has global localizations. What fails is gluing the local arrows into an admissible global arrow. L002's one-prime determinant formula did not test this inter-place condition, and L003 did not retain markings. No identification of this example with the full IUT data is made.

## Assessment against the main gap

The proposed test of simply finding a local structure poly-morphism is insufficient, even with the extra local equivariance and object localization retained above. This is new evidence that changes the test: the global compatibility equation, or some other valid control of the total degree defect, must be checked before local markings yield numerical information. The source itself retains global morphism compatibility; the example must not be advertised as satisfying that requirement.

The required IUT conclusion remains finite B ≥ A. The achieved model bound in the example is only A ≤ B + log ℓ, and equality holds in that weaker bound while B < A. This gives neither an estimate for the actual B nor a counterexample under the initial Θ-data and log-theta-lattice hypotheses. No complete candidate exists.

Outcome: NEGATIVE for the local-marking sufficiency test, not a negative verdict on IUT. The reason to turn to the full local-global transport is the demonstrated inter-place obstruction, rather than another generic quotient or normalization example. The prior exploration usage remains 3/3 and no new allowance is claimed. The current route decision and the sole concrete action are in PROGRESS.md.

## Checks and limits

Qualification added on 2026-09-26: the statement above that the example omits global morphism compatibility must be read as absence of a particular global comparison arrow. It is not a failure of the category's compatibility axiom for arrows that exist. The [subsequent test](2026-09-26-compatible-marked-category-test.md) establishes this distinction and its exact degree consequence. The original L004 counterexample and its hypotheses are unchanged.

The checks were exact valuation inequalities, the real norm condition, the product formula over ℚ proved from prime factorization, preservation of the unit orbits, and compatibility of the example under local scalar extension. No numerical search was needed. L004 is independent of the other notebook lemmas; its new DAG row has no inputs. Mathlib coverage is **not checked**. The source definitions and the ordinary model have been kept separate throughout. Documentation validation is recorded in the dated history after execution.
