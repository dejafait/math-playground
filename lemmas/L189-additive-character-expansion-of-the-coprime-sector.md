# Lemma 189: additive-character expansion of the coprime sector

**Hypotheses.** Use L188's notation, hypotheses and exact closed intervals
J_(u,r), with real bounded profiles. All sums below have integer indices.
Write e(x)=exp(2πix). For N²≤u≤4N², 0<|r|≤R and gcd(r,u)=1 set

F_(u,r)(m)=Q(floor((m²+r)/u)) H_m(r),
S_(u,r)(a)=Σ_(m∈J_(u,r), gcd(m,u)=1) F_(u,r)(m)e(am²/u).

The floor is an explicit extension away from the congruence; it does not
replace any original weight on the congruence. Q is zero outside its
actual pair-product support. Empty intervals give zero sums.

**Conclusion.** The following finite identities are exact:

Z_N=Σ_(u,r) P(u) S_(u,r)(0)/u,
E_N=Σ_(u,r) P(u)/u Σ_(a=1)^(u−1) e(ar/u) S_(u,r)(a),
B_N^(g=1)=Z_N+E_N.                                             (1)

Both Z_N and E_N are real. Every cutoff, coprimality condition, square
exclusion and signed weight of L188 is retained. For every epsilon>0,

|Z_N|=O_epsilon(N^(3+epsilon)).                                (2)

The precise necessary and sufficient nonzero-frequency condition is

B_N^(g=1)=o(Nh)  iff  E_N=−Z_N+o(Nh).                         (3)

This decay is **unproved**. In particular E_N=o(Nh) alone is sufficient
only if Z_N=o(Nh) is also established; neither estimate is proved here.

**Proof.**

For integers k and u≥1 the finite geometric sum gives

(1/u)Σ_(a=0)^(u−1)e(ak/u)=1 if u divides k, and 0 otherwise.

Indeed if e(k/u)=1 every summand is one; otherwise the sum is
(1−e(k))/(1−e(k/u))=0. Insert this identity with k=m²+r in
the finite sum over J_(u,r) with gcd(m,u)=1. On its surviving terms,
floor((m²+r)/u)=(m²+r)/u, so the weight is exactly the weight
in L188. Splitting a=0 from the remaining frequencies proves (1).
All rearrangements are finite. In particular no smooth interpolation,
uniform distribution of roots, or limiting interchange has been used.

Since F is real, S_(u,r)(u−a) is the complex conjugate of S_(u,r)(a).
The same holds for the factor e(ar/u). Pairing a with u−a makes E_N
real; when u is even its self-paired a=u/2 term is real as well.
Z_N is visibly real.

There are O(N²) moduli, O(N^(3/2)) displacements, and O(h) integers
in each J. By the exact interval support bounds, (m²+r)/u lies in
[N²,4N²]. Its floor, if it contributes, belongs to Q's support.
The divisor bounds and bounded weights inherited in L188 therefore
bound |P(u) F_(u,r)(m)| by O_epsilon(N^epsilon), after choosing
the divisor exponent small enough. H_m(r)=O(1) holds throughout this
interval: m≍N², |r|=O(N^(3/2)), and the bounded coefficients defining
H have the same bounds used in L187. These bounds do not require the
congruence. The factor 1/u≤N^(−2) now gives

|Z_N|≤C_epsilon N² N^(3/2) h N^(−2) N^epsilon
     =O_epsilon(N^(3+epsilon)).

Finally subtract Z_N in (1) and divide by Nh to obtain (3). Since
Nh≍N^(5/2), (2) is not a vanishing normalized estimate. ∎

## Qualifications

The zero-mode splitting depends on the chosen extension. If real values
D_(u,r)(m) vanishing whenever u divides m²+r are added to F, the
full sum is unchanged by orthogonality. The zero mode changes by
Δ=Σ_(u,r) P(u)/u Σ_m D_(u,r)(m), and the nonzero part changes by
−Δ. Thus the zero mode cannot be declared an intrinsic main term
without specifying the extension. The floor convention above fixes it
unambiguously but does not make Q smooth or remove its arithmetic support.
A bound for unweighted quadratic sums alone is not an estimate of the
weighted, sharply truncated sums S in (1).

This result concerns only g=1; even proving (3) would leave other gcd
sectors and the broader analytic problem unresolved. RH is not proved.

## Verification and formalization obligations

`python3 scripts/heat/check_additive_character_expansion.py` checks the
identity with signed pair weights and exact rational cutoffs, conjugate
pairing, and the compensating change under a second extension. Character
values use floating-point arithmetic with a stated tolerance; these are
regression checks, while finite orthogonality above is the proof.
Formalization requires finite character orthogonality, floor agreement
on integers, exact interval restrictions, conjugation, and the divisor
and interval counts supplying (2).

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
