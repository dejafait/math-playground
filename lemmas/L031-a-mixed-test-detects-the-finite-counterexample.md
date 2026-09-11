# Lemma 31: a mixed test detects the finite counterexample

**Hypotheses.** b=1/25, c=(10+i/4)^{-2}, and T_k=b^k+c^k+conj(c)^k, as in Lemma 29.

**Conclusion.** There is a real polynomial q of degree at most two such that

b²q(b)²+c²q(c)²+conj(c)²q(conj(c))²=-2.

Thus the 3-by-3 Hankel matrix (T_{m+n+2})_{0≤m,n≤2} is not positive semidefinite, although all T_k>0.

**Proof.** The three nodes b,c,conj(c) are distinct because b is real and c is nonreal. Define

L_c(X)=(X-b)(X-conj(c))/[(c-b)(c-conj(c))],

L_conj(c)(X)=(X-b)(X-c)/[(conj(c)-b)(conj(c)-c)],

q(X)=(i/c)L_c(X)-(i/conj(c))L_conj(c)(X).

The two Lagrange basis polynomials have conjugate coefficients, and the two scalar coefficients are conjugates, so q has real coefficients. Its values are q(b)=0, q(c)=i/c, and q(conj(c))=-i/conj(c). Substitution makes the three terms 0,-1,-1. The Hankel identity is the finite version of Lemma 30, proving the matrix claim. ∎

**Mathlib.** The explicit counterexample is proved below by exact rational arithmetic and a power-norm estimate; no prepackaged Mathlib proof of the full statement is used. Positive semidefiniteness is Mathlib's `Matrix.PosSemidef`, and its quadratic-form consequence is `Matrix.PosSemidef.dotProduct_mulVec_nonneg`:

https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/PosDef.html#Matrix.PosSemidef

https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/PosDef.html#Matrix.PosSemidef.dotProduct_mulVec_nonneg

**Lean proof status.** Validated. Lean 4.33.1, mathlib `v4.33.1`, `lake build Rh.L031` from `scripts/lean`. Kernel axioms: `propext`, `Classical.choice`, `Quot.sound`.

**Lean proof command.**

```
(cd scripts/lean && lake exe cache get && lake build Rh.L031)
```

**Lean proof code.**

```lean
/-
Lemma 31: a mixed test detects the finite counterexample.
An explicit rational polynomial replaces the Lagrange interpolation formula.
-/
import Rh.L034
import Mathlib.LinearAlgebra.Matrix.PosDef

open Complex Polynomial Matrix
open scoped ComplexConjugate

noncomputable section

def L031_b : ℝ := 1 / 25

def L031_T (k : ℕ) : ℝ := L031_b ^ k + (L034_c ^ k).re * 2

def L031_q : Polynomial ℝ :=
  C (4914140794001 / 1848321280) +
  C (-758169934387323 / 2274856960) * X +
  C (39452764147173995 / 5914628096) * X ^ 2

/-- The real power sums agree with the complex node sums. -/
theorem L031_T_eq (k : ℕ) : (L031_T k : ℂ) =
    (L031_b : ℂ) ^ k + L034_c ^ k + conj L034_c ^ k := by
  simp only [← map_pow]
  apply Complex.ext <;>
    simp only [L031_T, Complex.add_re, Complex.add_im, Complex.conj_re,
      Complex.conj_im, Complex.ofReal_re, Complex.ofReal_im,
      Complex.ofReal_add, Complex.ofReal_mul, Complex.ofReal_pow,
      Complex.mul_re, Complex.mul_im, Complex.ofReal_ofNat] <;> norm_num <;> ring

/-- The polynomial has degree at most two. -/
theorem L031_degree : L031_q.natDegree ≤ 2 := by
  unfold L031_q
  compute_degree

/-- The three interpolation values, proved using exact rational arithmetic. -/
theorem L031_values :
    L031_q.eval₂ Complex.ofRealHom (L031_b : ℂ) = 0 ∧
    L031_q.eval₂ Complex.ofRealHom L034_c = I / L034_c ∧
    L031_q.eval₂ Complex.ofRealHom (conj L034_c) = -I / conj L034_c := by
  have hcj : conj L034_c = (25584 / 2563201 : ℝ) + (1280 / 2563201 : ℝ) * I := by
    apply Complex.ext <;>
      simp only [Complex.conj_re, Complex.conj_im] <;>
      norm_num [L034_c_value]
  rw [hcj, L034_c_value]
  norm_num [L031_q, L031_b, Polynomial.eval₂_add, Polynomial.eval₂_mul,
    Polynomial.eval₂_pow, Complex.div_re, Complex.div_im, Complex.normSq,
    Complex.mul_re, Complex.mul_im, pow_two, Complex.ext_iff]

/-- The mixed form of this real polynomial is exactly minus two. -/
theorem L031_form :
    (L031_b : ℂ) ^ 2 * (L031_q.eval₂ Complex.ofRealHom (L031_b : ℂ)) ^ 2 +
    L034_c ^ 2 * (L031_q.eval₂ Complex.ofRealHom L034_c) ^ 2 +
    (conj L034_c) ^ 2 * (L031_q.eval₂ Complex.ofRealHom (conj L034_c)) ^ 2 = -2 := by
  rw [L031_values.1, L031_values.2.1, L031_values.2.2]
  have hc : L034_c ≠ 0 := by
    intro h
    have := congrArg Complex.im h
    norm_num [L034_c_value] at this
  have hcj : conj L034_c ≠ 0 := by simpa only [_root_.map_ne_zero] using hc
  field_simp
  simp [I_sq]
  ring

/-- Every scalar power sum remains strictly positive. -/
theorem L031_positive (k : ℕ) (hk : 1 ≤ k) : 0 < L031_T k := by
  have hn : ‖L034_c‖ < 1 / 100 := by
    have hs : ‖L034_c‖ ^ 2 = (256 / 2563201 : ℝ) := by
      rw [Complex.sq_norm, L034_c_value]
      norm_num [Complex.normSq]
    nlinarith [norm_nonneg L034_c]
  have hb : 0 < L031_b := by norm_num [L031_b]
  have hpow : ∀ n : ℕ, 1 ≤ n → 2 * ‖L034_c‖ ^ n < L031_b ^ n := by
    intro n
    induction n with
    | zero => omega
    | succ n ih =>
      intro hn1
      by_cases hn0 : n = 0
      · subst n
        norm_num only [pow_one]
        dsimp [L031_b]
        linarith
      · have hprev := ih (by omega)
        have hmul := mul_lt_mul_of_pos_right hprev hb
        have hrb : ‖L034_c‖ ≤ L031_b := by dsimp [L031_b]; linarith
        rw [pow_succ, pow_succ]
        calc
          2 * (‖L034_c‖ ^ n * ‖L034_c‖) ≤
              (2 * ‖L034_c‖ ^ n) * L031_b := by
                nlinarith [pow_nonneg (norm_nonneg L034_c) n]
          _ < L031_b ^ n * L031_b := hmul
  have hre := Complex.abs_re_le_norm (L034_c ^ k)
  rw [norm_pow] at hre
  have hlow := (abs_le.mp hre).1
  have hstrict := hpow k hk
  dsimp [L031_T]
  linarith

/-- The Hankel matrix formed from these scalar power sums. -/
def L031_H : Matrix (Fin 3) (Fin 3) ℝ := fun m n => L031_T (m.val + n.val + 2)

/-- An explicit coefficient vector witnesses failure of positive semidefiniteness. -/
theorem L031_not_posSemidef : ¬ L031_H.PosSemidef := by
  intro h
  let v : Fin 3 → ℝ := ![4914140794001 / 1848321280,
    -758169934387323 / 2274856960, 39452764147173995 / 5914628096]
  have hv := h.dotProduct_mulVec_nonneg v
  norm_num [v, dotProduct, mulVec, Fin.sum_univ_succ, L031_H, L031_T,
    L031_b, L034_c_value, Complex.mul_re, Complex.mul_im, pow_succ] at hv

end

#print axioms L031_T_eq
#print axioms L031_degree
#print axioms L031_values
#print axioms L031_form
#print axioms L031_positive
#print axioms L031_not_posSemidef
```
