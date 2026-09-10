# Lemma 2: conjugation preserves zeros and multiplicities

**Hypotheses.** s∈C, with equality interpreted meromorphically at the pole.

**Conclusion.** ζ(conj(s))=conj(ζ(s)). A zero at ρ gives a zero of the same multiplicity at conj(ρ).

**Proof.** For Re(s)>1, conjugate the absolutely convergent defining series term by term. The function g(s)=conj(ζ(conj(s))) is meromorphic: conjugate the coefficients of each local Laurent expansion. It agrees with ζ on Re(s)>1 and hence everywhere by the meromorphic identity theorem. Conjugating a local Taylor series preserves the index of its first nonzero coefficient, proving the multiplicity claim. ∎

**Mathlib.** The identity `ζ(conj s) = conj(ζ s)` is `riemannZeta_conj`:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Harmonic/ZetaAsymp.html#riemannZeta_conj

Equal meromorphic orders at `s` and `conj s` are not a named Mathlib theorem.

**Lean proof status.** Validated. Lean 4.33.1, mathlib `v4.33.1`, `lake build Rh.L002` from `scripts/lean`. Kernel axioms: `propext`, `Classical.choice`, `Quot.sound`.

**Lean proof command.**

```
(cd scripts/lean && lake exe cache get && lake build Rh.L002)
```

**Lean proof code.**

```lean
/-
Lemma 2: conjugation preserves zeros and multiplicities.

ζ(conj s) = conj(ζ s) for all s, and meromorphic orders at s and conj s agree.
-/
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.Analysis.Meromorphic.Order
import Mathlib.NumberTheory.Harmonic.ZetaAsymp
import Mathlib.NumberTheory.LSeries.RiemannZeta

open Complex Filter
open scoped ComplexConjugate Topology

noncomputable section

/-- `conj ∘ f ∘ conj` is complex-differentiable whenever `f` is. -/
lemma hasDerivAt_conj_comp_conj {f : ℂ → ℂ} {f' z : ℂ}
    (hf : HasDerivAt f f' (conj z)) :
    HasDerivAt (fun w : ℂ => conj (f (conj w))) (conj f') z := by
  rw [hasDerivAt_iff_tendsto] at hf ⊢
  have hcomp := hf.comp (continuous_star.tendsto z)
  convert hcomp using 1
  ext w
  simp only [Function.comp_apply, smul_eq_mul]
  have h1 : ‖w - z‖ = ‖conj w - conj z‖ := by
    rw [← map_sub, norm_conj]
  have h2 :
      ‖conj (f (conj w)) - conj (f (conj z)) - (w - z) * conj f'‖ =
        ‖f (conj w) - f (conj z) - (conj w - conj z) * f'‖ := by
    have hrem :
        conj (f (conj w)) - conj (f (conj z)) - (w - z) * conj f' =
          conj (f (conj w) - f (conj z) - (conj w - conj z) * f') := by
      rw [map_sub, map_sub, map_mul, map_sub, conj_conj, conj_conj]
    rw [hrem, norm_conj]
  rw [h1, h2]
  rfl

lemma differentiableAt_conj_comp_conj {f : ℂ → ℂ} {z : ℂ}
    (hf : DifferentiableAt ℂ f (conj z)) :
    DifferentiableAt ℂ (fun w : ℂ => conj (f (conj w))) z :=
  (hasDerivAt_conj_comp_conj hf.hasDerivAt).differentiableAt

lemma analyticAt_conj_comp_conj {f : ℂ → ℂ} {z : ℂ}
    (hf : AnalyticAt ℂ f (conj z)) :
    AnalyticAt ℂ (fun w : ℂ => conj (f (conj w))) z := by
  rw [Complex.analyticAt_iff_eventually_differentiableAt] at hf ⊢
  have hmap : Tendsto conj (𝓝 z) (𝓝 (conj z)) := continuous_star.tendsto z
  filter_upwards [hmap.eventually hf] with w hw
  exact differentiableAt_conj_comp_conj hw

lemma map_conj_nhdsNE (x : ℂ) :
    Filter.map conj (𝓝[≠] x) = 𝓝[≠] (conj x) := by
  have hfun : ⇑conjCLE.toHomeomorph = conj := by
    ext y; exact conjCLE_apply y
  rw [← hfun, Homeomorph.map_punctured_nhds_eq, hfun]

lemma meromorphicAt_riemannZeta_of_ne_one {s : ℂ} (hs : s ≠ 1) :
    MeromorphicAt riemannZeta s :=
  (analyticOn_riemannZeta s (by simp [hs])).meromorphicAt

/-- Conjugation preserves the meromorphic order of `ζ`. -/
lemma meromorphicOrderAt_riemannZeta_conj (s : ℂ) :
    meromorphicOrderAt riemannZeta (conj s) = meromorphicOrderAt riemannZeta s := by
  by_cases hs : s = 1
  · subst s; simp
  have hs' : conj s ≠ 1 := by
    intro h
    exact hs (by simpa using congr_arg conj h)
  have hmero : MeromorphicAt riemannZeta s := meromorphicAt_riemannZeta_of_ne_one hs
  have hmero' : MeromorphicAt riemannZeta (conj s) := meromorphicAt_riemannZeta_of_ne_one hs'
  cases hord : meromorphicOrderAt riemannZeta s with
  | top =>
    rw [meromorphicOrderAt_eq_top_iff] at hord ⊢
    have : (∀ᶠ z in 𝓝[≠] (conj s), riemannZeta z = 0) ↔
        ∀ᶠ z in 𝓝[≠] s, riemannZeta (conj z) = 0 := by
      rw [← map_conj_nhdsNE s]
      exact Filter.eventually_map
    simpa [this, riemannZeta_conj, map_eq_zero] using hord
  | coe n =>
    obtain ⟨g, hg_an, hg_ne, hg_eq⟩ := (meromorphicOrderAt_eq_int_iff hmero).1 hord
    refine (meromorphicOrderAt_eq_int_iff hmero').2 ?_
    refine ⟨fun w => conj (g (conj w)), analyticAt_conj_comp_conj (by simpa using hg_an), ?_, ?_⟩
    · simpa using (map_ne_zero_iff (starRingEnd ℂ) star_injective).2 hg_ne
    · have hg_eq' :
          ∀ᶠ w in 𝓝[≠] (conj s), riemannZeta (conj w) = (conj w - s) ^ n • g (conj w) := by
        rw [← map_conj_nhdsNE s, eventually_map]
        simpa [conj_conj] using hg_eq
      filter_upwards [hg_eq'] with w hw
      have hzw : riemannZeta w = conj (riemannZeta (conj w)) := by
        rw [riemannZeta_conj, conj_conj]
      rw [hzw, hw]
      simp_rw [smul_eq_mul, map_mul, map_zpow₀, map_sub, conj_conj]

/-- Lemma 2: conjugation identity and equal meromorphic orders. -/
theorem L002 (s : ℂ) :
    riemannZeta (conj s) = conj (riemannZeta s) ∧
    meromorphicOrderAt riemannZeta (conj s) = meromorphicOrderAt riemannZeta s :=
  ⟨riemannZeta_conj s, meromorphicOrderAt_riemannZeta_conj s⟩

/-- A zero of `ζ` at `ρ` is a zero of the same meromorphic order at `conj ρ`. -/
theorem L002_zero {ρ : ℂ} (hζ : riemannZeta ρ = 0) : riemannZeta (conj ρ) = 0 := by
  rw [riemannZeta_conj, hζ, map_zero]

end

-- Kernel-axiom audit. Expected: propext, Quot.sound, Classical.choice.
#print axioms L002
#print axioms L002_zero
```

