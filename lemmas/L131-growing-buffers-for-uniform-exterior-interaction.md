# Lemma 131: growing buffers for uniform exterior interaction

**Hypotheses.** Fix L≥0 and H>0. Assume that every zero of every real theta heat slice F(λ,·), |λ|≤L, lies in |Im z|≤H. This common strip hypothesis is an assumption, not a conclusion. Use full zero multisets with multiplicities. For A≥2 let d=d(A)>0 be arbitrary, put R=A+d, and let B_L and Q_L be the constants and function in L130. Define

V(A,d) = ((R²+H²)/d²) Q_L(R).

**Conclusion.** Uniformly for |λ|≤L and w=a+ib with |a|≤A and 0<b≤H,

Σ_{|Re ρ|>R}|Im(2/(w−ρ))| ≤ 4H V(A,d),             (1)

2Σ_{|Re ρ|>R, Im ρ>b}(Im ρ−b)/|w−ρ|²
 ≤ 2(H−b)V(A,d).                                   (2)

The following equivalence describes exactly when this majorant vanishes:

V(A,d(A))→0  if and only if  d(A)/sqrt(A log A)→∞.   (3)

Thus any buffer sqrt(A log A) g(A) with g(A)→∞ suffices; one may choose such buffers to be o(A), for example sqrt(A log A) log log A for sufficiently large A. There is no smallest diverging factor g. A fixed positive multiple of sqrt(A log A) does not make this majorant vanish. This is not a necessity assertion about the actual sums in (1) or (2).

If w is a zero of multiplicity m, and no zero in |Re z|≤R has height greater than b, its local forward cluster height rate satisfies

c(w) ≤ −m/b−mb/(a²+b²)+2(H−b)V(A,d).                (4)

## Proof

Apply L129 to each slice with the common H. The horizontal reciprocal-square tail is at most Q_L(R) by L130, with constants independent of λ. Substitution gives (1), (2), and (4), including absolute convergence and the local interpretation of c(w). No supremum derivative is taken.

The exact expression for the majorant is

V(A,d) = (1+H²/R²)[B_L+10R(log(5R)+1)]/(d² log 2).

Since H and B_L are fixed and R≥A→∞, the ratio of this expression to R log R/d² tends to 10/log 2, independently of how d varies. Hence V→0 is equivalent to R log R/d²→0.

Necessity in (3) follows from R≥A≥2 and monotonicity of x log x:

0≤A log A/d²≤R log R/d²→0.

For sufficiency assume A log A/d²→0. On the subset of A where d≤A, R≤2A and

R log R/d²≤2A log(2A)/d²→0.

On the complementary subset d>A, R<2d and therefore

R log R/d²≤2log(2d)/d→0,

because d>A→∞. These two estimates cover all A, including oscillatory buffers, and prove sufficiency without a regularity or monotonicity assumption on d.

For d=c sqrt(A log A), c>0 fixed, d/A→0 and R/A→1. The exact expression consequently gives V→10/(c² log 2), a positive number. Conversely every g→∞ gives vanishing by (3). No minimal such factor exists: replacing an eventually positive diverging g by sqrt(g) gives a smaller diverging factor eventually. The example with log log A is sublinear because sqrt(log A/A) log log A→0. ∎

## Qualifications and verification

The threshold is exact for the displayed L129–L130 majorant only. The inequalities used can overestimate local crowding severely. Necessity for actual theta interactions, or even for all zero multisets satisfying the same counting bound, has not been established here. A local zero-count estimate could yield a smaller sufficient buffer.

The strip assumption remains conditional. Even with a sublinear buffer, this result does not ensure that an inner zero maximizes height in the larger window, control positive interactions in the buffer annulus, or bound the time remainder uniformly over growing windows. Thus (4) is only a conditional local rate estimate and does not close the whole-plane continuation or RH gap.

Verification is analytic: substitution of the full-multiset tail, the exact simplification of V, its asymptotic comparison, both directions of (3) including nonmonotone d, and the critical-scale limit were checked. No numerical certificate is needed. Formalization would require these uniform inequalities, a two-case limit argument for arbitrary positive buffer functions, and the qualifications on the conditional local height rate.
