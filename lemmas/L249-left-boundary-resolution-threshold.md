# Lemma 249: signed left-boundary resolution and its localization threshold

**Hypotheses.** Use F(z)=Ξ(i√z) and G=F′/F from L246. Write each squared zero representative as α_j²=A_j+iB_j, with multiplicity. Let t>0 and ε>0, and suppose −t+iε is not a zero of F.

**Conclusion.** The absolutely convergent boundary-resolution identity is

−π⁻¹ Im G(−t+iε)=π⁻¹ Σ_j (ε+B_j)/[(A_j−t)²+(ε+B_j)²].

A real squared node contributes ε/[π((A−t)²+ε²)]>0. A conjugate pair A±iB contributes

2ε[(A−t)²+ε²−B²] / {π[(A−t)²+(ε+B)²][(A−t)²+(ε−B)²]}.

For actual Ξ, F(−t+iε)≠0 and the total is strictly positive whenever ε²≥t+1/2. For t≥16 this threshold is sharp for positivity of each pair using only a>4 and |b|<1/2 for α=a+ib: whenever 0<ε²<t+1/2, some admissible pair gives a strictly negative contribution, away from its poles. No fixed ε>0 controls every t by these localization hypotheses alone.

**Proof.** L246 supplies the locally uniformly absolutely convergent expansion G(z)=Σ_j(z+α_j²)⁻¹ away from its poles. On each compact set its tail is bounded by 2Σ_j|α_j|⁻², so taking imaginary parts and conjugate pairing are legitimate. The imaginary part of one reciprocal gives the first formula; addition of two fractions gives the second.

By L026, α=a+ib has a>4 and |b|<1/2. Hence A=a²−b²>63/4 and B²=4a²b² satisfy

A+1/4−B²=(1−4b²)(a²+1/4)>0.

Consequently

(A−t)²+ε²−B² > (A−t−1/2)²+ε²−t−1/2.

If ε²≥t+1/2, every pair numerator is positive. There are no poles there: a pole would require A=t and |B|=ε, whereas B²<t+1/4. All real-node terms are positive too, and the zero set is nonempty by L246. Absolute convergence then proves strict positivity of the sum.

For sharpness fix t≥16 and ε²<t+1/2. Choose b in (0,1/2) tending to 1/2, and set a²=t+1/2+b². Then a>4, A=t+1/2, and B²=4b²(t+1/2+b²) tends to t+3/4. Thus

(A−t)²+ε²−B² → ε²−t−1/2<0.

For b sufficiently close to 1/2 the contribution is negative. Its denominators are nonzero because A−t=1/2. The even real polynomial P(w)=(1−w²/(a+ib)²)(1−w²/(a−ib)²) realizes precisely this admissible pair of squared nodes; its transformed logarithmic derivative therefore violates the sign at the chosen point. It satisfies the stated localization and finite reciprocal-square summability. It is not asserted to be a theta transform. Given any fixed ε, choose t≥16 with t+1/2>ε² and apply this construction.

For completeness, any actual nonreal squared node A+iB with B>0 would give a pole z₀=−A+iB of G with a positive integer residue m. In a disk containing no other distinct poles, G(z)=m/(z−z₀)+h(z) with h holomorphic. At z=z₀−iδ, 0<δ<B, one has Im G(z)=m/δ+O(1)>0 as δ tends to zero. Thus the required upper-half-plane sign fails just below such a pole; other zeros cannot hide it by cancellation there. This is a conditional diagnostic, not an assertion that such a zero exists. ∎

The required Stieltjes condition covers every ε>0 and t>0, together with holomorphy. The achieved resolution grows at least like √t; it does not approach the missing boundary. Pairwise positivity is stronger than total positivity, so sharpness of the pairwise threshold is not a sharpness assertion for actual Ξ. The polynomial only refutes extension based on localization alone. The local pole calculation explains why proving the total sign everywhere would genuinely exclude nonreal zeros, rather than establish merely another scalar test.

**Mathlib.** Not checked: coverage of the full statement and supporting logarithmic-derivative, Laurent-expansion, and rational identities was not checked. No matching theorem is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
