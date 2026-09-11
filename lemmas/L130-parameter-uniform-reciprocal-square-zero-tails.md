# Lemma 130: parameter-uniform reciprocal-square zero tails

**Hypotheses.** Let F(λ,z) be the theta heat deformation of L058 and fix L≥0. All zero counts and sums below use the full zero multiset of the real slice F(λ,·), including multiplicities. Put

q=e^(−π),    C=8π²(1+11q+11q²+q³)/(1−q)^5,

m_L=4π(2π−3)exp(−L−πe²),

B_L=max(0, log(C/(2m_L))+2L²/π).

**Conclusion.** Uniformly for real |λ|≤L and t≥1, the number N_λ(t) of zeros in |z|≤t satisfies

N_λ(t)≤[B_L+5t log(5t)]/log 2.                         (1)

For every R≥1,

Σ_{|ρ|>R}|ρ|^(−2) ≤ Q_L(R)
 := [B_L/R²+10(log(5R)+1)/R]/log 2.                   (2)

Consequently the horizontal tail Σ_{|Re ρ|>R}|ρ|^(−2) is also at most Q_L(R). Both tails tend to zero uniformly over |λ|≤L. No strip hypothesis or parameter-dependent enumeration is required. For pair representatives the radial and horizontal bounds can each be divided by two.

## Proof

First establish an explicit normalization lower bound. By L019 every kernel summand is positive. For the first summand write v=πe^(2u). On 0≤u≤1,

4v(2v−3)e^(u/2)e^(−v) ≥ 4π(2π−3)e^(−πe²).

Indeed v≥π, 2v−3≥2π−3>0, e^(u/2)≥1 and v≤πe². Also e^(λu²)≥e^(−L) for the indicated real parameters. Integrate over this unit interval in the definition from L058 to obtain F(λ,0)≥m_L>0.

Let M_λ(s)=max_{|z|≤s}|F(λ,z)|. L063 gives for s≥1

log M_λ(s)−log F(λ,0)
 ≤ B_L+(s/2+4)log(s/2+4).                            (3)

Fix λ and t≥1. Apply the standard named Jensen formula on a circle of radius s>2t containing no zero on its boundary. Every zero with |ρ|≤t contributes at least log(s/t) to its nonnegative Jensen sum, so

N_λ(t)log(s/t) ≤ log M_λ(s)−log F(λ,0).

Such radii can be chosen decreasing to 2t: a nonzero entire function has a locally finite zero multiset. Use (3) and continuity of its explicit upper bound to conclude

N_λ(t)log 2≤B_L+(t+4)log(t+4).

Since t+4≤5t and x log x is increasing on x≥1, this proves (1), including zeros on |z|=t. Jensen's multiplicities are precisely those in N_λ.

For each zero of modulus r>R, write r^(−2)=2∫_r^∞t^(−3)dt. Tonelli's theorem for nonnegative summands gives

Σ_{|ρ|>R}|ρ|^(−2)
 =2∫_R^∞ #{ρ:R<|ρ|≤t} t^(−3)dt
 ≤2∫_R^∞ N_λ(t)t^(−3)dt.

This argument does not assume a uniform summability statement in advance. Substituting (1) and using

∫_R^∞t^(−3)dt=1/(2R²),

∫_R^∞log(5t)t^(−2)dt=(log(5R)+1)/R

proves (2). The second integral follows by integration by parts, with log(5t)/t→0 at infinity. The bound is independent of λ and tends to zero. The set |Re ρ|>R is contained in |ρ|>R, proving the horizontal assertion. Finally evenness from L058 pairs ρ and −ρ with equal multiplicities; neither is zero, and both cutoff conditions are invariant under negation. Each full sum is twice its pair-representative sum. ∎

## Qualifications and verification

This is an explicit unconditional uniform tail bound for compact real heat-parameter intervals. The lower bound m_L is deliberately coarse. There is no claim for complex parameter intervals, where the positive integral normalization need not hold. No zero simplicity, separation, or consistent moving labels are used.

The bound does not supply a uniform strip height, a uniform local motion remainder, or control of interactions across a vanishing horizontal buffer. In particular it does not resolve the annulus limitation of L129 or a whole-plane supremum derivative, and it proves no new zero reality assertion.

Verification is analytic: the four positive factors in the normalization lower bound, Jensen's radius limit, the full-multiset count, nonnegative Tonelli interchange, and the two elementary integrals were checked explicitly. No computational or numerical certificate is needed. Formalization would require Jensen's formula with multiplicities, local finiteness of zeros of a nonzero entire function, the explicit lower bound, Tonelli for the zero counting measure, and the displayed integral evaluations.
