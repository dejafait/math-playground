# Lemma 256: exact second-level zero-block compensation

**Hypotheses.** Let Ξ have the product and summability of L024 and localization of L026. Fix real x with Ξ(x)≠0. Group its zeros, with multiplicity, into real roots r and nonreal conjugate pairs a±ib. Use D₂ as defined in L255. Assign each block coefficients (A,B) by

(A,B)=((x−r)^(−2),0)

for a real root, and, writing u=x−a,

(A,B)=(2(u²−b²)/(u²+b²)², 1/(u²+b²)²)

for a conjugate pair. Let P be the blocks with A≥0 and N those with A<0. Define

S=Σ_P A, T=Σ_N |A|,
E_P=Σ_P B+Σ_{i<j in P} A_i A_j,
E_N=Σ_N B+Σ_{i<j in N} |A_i A_j|.

**Conclusion.** All these sums converge absolutely, N is finite, and

D₂(Ξ;x)/Ξ(x)² = E_P+E_N−ST.

Thus the exact compensation threshold is E_P+E_N≥ST. Moreover E_N≥T²/4, so E_P+T²/4≥ST is sufficient, but is not asserted necessary. Positive first coefficients alone do not ensure compensation: even adding a single real-root block to a positive second-level block can make the total second coefficient negative.

**Proof.** L255's factor calculation gives the normalized factor 1+A y²+B y⁴ for each block (B=0 for real roots). For sufficiently large |ρ|, |x−ρ|≥|ρ|/2. Thus |A|=O(|ρ|^(−2)) and B=O(|ρ|^(−4)); finitely many remaining denominators are nonzero by the hypothesis on x. L024's reciprocal-square summability proves Σ|A| and ΣB finite, hence also absolute convergence of all pair sums. Negative A requires |x−a|<|b|<1/2. Such zeros lie in a bounded rectangle and are finite by discreteness of zeros of the nonzero entire function Ξ.

Exhaust the product by finite sets closed under negation and conjugation. As in L255, normalized products converge locally uniformly in complex y, and their coefficients converge by the Cauchy integral formula. In a finite product the y⁴ coefficient is ΣB+Σ_{i<j}A_iA_j. Absolute convergence permits separation into P–P, N–N and P–N pairs; the last sum equals −ST. This proves the identity without rearranging a conditionally convergent zero sum.

For a negative block, t=|A|=2(b²−u²)/(u²+b²)² satisfies

B−t²/4 = 4u²b²/(u²+b²)⁴ ≥0.

Consequently

E_N≥(1/4)Σ_N t_i²+Σ_{i<j in N}t_i t_j
    =T²/4+(1/2)Σ_{i<j in N}t_i t_j≥T²/4.

For the final assertion take any b>0 and d≠0 and the real polynomial J(z)=(z²+b²)(z−d), at x=0. Its nonreal block has A=−2/b², B=1/b⁴, so by itself its second coefficient is positive. The added real root has S=1/d² and E_P=0. Exactly,

D₂(J;0)/J(0)²=1/b⁴−2/(b²d²),

which is negative whenever d²<2b². For example d=b gives −1/b⁴. The product coefficients also follow directly from (1−2y²/b²+y⁴/b⁴)(1+y²/d²). This is a counterexample to monotonic compensation by positive blocks, not an example satisfying the theta hypotheses. ∎

At real zeros of Ξ the normalized formula is not defined; the unnormalized D₂ remains continuous, so a sign proved at every nonzero real point would extend to them. No such global sign is obtained here. The strip bounds imply neither a positive lower bound on |b| for possible nonreal zeros nor the needed comparison between E_P, E_N and ST. The identity supplies an exact target, not an estimate meeting it. Even global D₂ positivity would leave higher levels and mixed reciprocal-node positivity unresolved.

**Mathlib.** Not checked for either the full statement or supporting product-coefficient and absolute-convergence results. No matching theorem is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
