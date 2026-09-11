# Lemma 159: exact resonant cutoff contribution

**Hypotheses.** Use L158's finite window I, positive real amplitudes
A_n=T^(3/4)b_n(t), centered frequencies λ_n=log(n/N), Q, K, χ, M>0,
and normalized expectation E_T on [T,2T]. Here N=sqrt(T/(2π)); the
window endpoints 0<a<b are fixed. Constants may depend on a,b,χ.

**Conclusion.** Put

D(t)=Σ_{n∈I} A_n²,
F(t)=Σ_k (Σ_{r,m∈I,rm=k} A_r A_m)²,
Z(t)=F(t)−D(t)².

The exact zero-total-frequency part of K is K_res=−Z, and

0≤Z(t)≤C log(2T).                                      (1)

Writing K_non=K−K_res, the cutoff remainder in L158 is exactly

R=R_amp+R_res+R_non,
R_res=(1/M)E_T[χ'(Q/M)Z],
R_non=−(1/M)E_T[χ'(Q/M)K_non].                         (2)

In particular,

0≤R_res≤C log(2T) min(1,1/M)/M.                        (3)

The weight in (2) is retained exactly. Bound (3) does not establish a
small fixed-M tail as T tends to infinity and does not assert that
R_res grows. No estimate sufficient for R_non is proved here.

**Proof.**

The total frequency of a term indexed by (r,s,m,n) is
λ_r−λ_s+λ_m−λ_n=log(rm/(sn)); it is zero exactly when rm=sn.
On this set, with r≠s and m≠n, the two nonzero gaps x,y satisfy y=−x.
L158's kernel (x/y+y/x)/2 therefore equals −1. The phase factor is
exp(i(t−π/2)log(rm/(sn)))=1. It follows that

K_res=−Σ_{r,s,m,n∈I,rm=sn,r≠s,m≠n} A_r A_s A_m A_n.

Expanding F enumerates all ordered solutions rm=sn, with their exact
multiplicities. Among these solutions r=s if and only if m=n. Thus
the excluded terms have sum Σ_{r,m∈I}A_r² A_m²=D², counted once.
This proves K_res=−(F−D²) and Z≥0, including empty windows.

To bound Z, first use Z≤F. Positivity permits enlarging each inner
sum to all positive integer factors. Therefore

F(t)≤T³ Σ_k (Σ_{rm=k} b_r(t)b_m(t))².

The pointwise estimate proved in L151 is
Σ_k(Σ_{rm=k}b_r b_m)²≤C N_t^(−6)(1+log N_t), where
N_t=sqrt(t/(2π)). For t∈[T,2T], T³N_t^(−6)≤C and
1+log N_t≤C log(2T). This proves (1). This use is of the
pointwise bound in that proof, not an inference from its integrated
conclusion. The full nonnegative Gaussian sums converge as justified
there; all window sums here are finite.

Substitute K=−Z+K_non in L158's expression for R to obtain (2).
Since χ is nondecreasing and C¹, χ'≥0. Since χ is constant on
(−∞,1] and [2,∞), continuity of its derivative implies χ'=0 outside
(1,2), including the endpoints. Hence

0≤R_res≤(||χ'||∞/M) E_T[Z 1_{M<Q<2M}]
         ≤(C log(2T)/M) P_T(M<Q<2M).

L156 gives E_T Q≤C. Markov's inequality and the probability bound one
give P_T(M<Q<2M)≤min(1,C/M). Absorbing the fixed constant proves
(3). No independence between Z and the cutoff is assumed. ∎

## Scope and verification

The resonant contribution has the unfavorable nonnegative sign in R.
This sign does not give a lower bound on the full remainder, because
R_non can have either sign. A nonzero frequency in K_non does not make
its weighted time average vanish: χ'(Q/M) depends on the same phases,
and even the amplitudes vary with time. Neither replacing the cutoff by
its mean nor applying unweighted orthogonality is justified.

Analytic verification checks the ordered multiplicities, the equivalence
of the two excluded equalities on rm=sn, both minus signs, T³N_t^(−6),
and the transition support. A finite integer enumeration regression is
provided in scripts/heat/check_resonant_quartic.py. It checks the algebra,
not asymptotic estimates or any assertion about zeta zeros.
Formalization would require finite product regrouping, positivity of the
Gaussian weights, L151's pointwise diagonal estimate, the cutoff support,
and Markov's inequality. No RH conclusion follows.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
