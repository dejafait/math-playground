# Rational-grid fourth-moment input

For a finite 1-separated set A in an interval of length T≥2, put
R_A(v)=Σ_(t∈A)v^(it), s=|A|, and
E(A)=#{(t₁,t₂,t₃,t₄)∈A⁴: |t₁+t₂−t₃−t₄|≤1}.
Guth–Maynard, *New large value estimates for Dirichlet polynomials*,
[arXiv:2405.20552v2, Lemma 11.6, pp. 41–42](https://arxiv.org/pdf/2405.20552v2#page=41),
gives, for M≥1,

Σ_(k,l∼M)|R_A(k/l)|⁴
 ≤C_ε T^ε[s⁴M+M²E(A)+E(A)^(3/4)s T^(1/2)M].

Here ε>0 is fixed and C_ε is independent of A,T,M. The notation
is specified in §1.2. The proof uses separation and energy; a
large-value hypothesis on another Dirichlet polynomial is unnecessary.
Translation of A preserves the modulus and energy.

This statement and its proof were read in the prior assessment and
rechecked on 2026-09-27. It is imported, not reproved. It supplies
neither the notebook's maximum weights nor its required logarithmic
saving in the height parameter.

Mathlib coverage of this full input: **not checked**.
