/-
Lemma 8: residue at 1 and the value at 0.

The residue of ζ at s = 1 is 1, and ζ(0) = -1/2.
-/
import Mathlib.NumberTheory.LSeries.RiemannZeta

open Complex Filter
open scoped Topology

noncomputable section

/-- The residue of `ζ` at the simple pole `s = 1` is 1. -/
theorem L008_residue :
    Tendsto (fun s : ℂ => (s - 1) * riemannZeta s) (𝓝[≠] 1) (𝓝 1) :=
  riemannZeta_residue_one

/-- `ζ(0) = -1/2`. -/
theorem L008_zero : riemannZeta 0 = -1 / 2 :=
  riemannZeta_zero

/-- Lemma 8: residue 1 at s = 1, and ζ(0) = -1/2. -/
theorem L008 :
    Tendsto (fun s : ℂ => (s - 1) * riemannZeta s) (𝓝[≠] 1) (𝓝 1) ∧
      riemannZeta 0 = -1 / 2 :=
  ⟨L008_residue, L008_zero⟩

end

#print axioms L008
#print axioms L008_residue
#print axioms L008_zero
