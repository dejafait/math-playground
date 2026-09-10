# Lemma 29: even all positive scalar power sums do not force real zeros

**Hypotheses.** Let a=10+i/4 and

P(z)=(1-z²/25)(1-z²/a²)(1-z²/conj(a)²),  F(z)=P(z)cos(z/100).

For a nonzero even entire function, a paired reciprocal-power sum means one term α^{-2k} per ± zero pair, with multiplicity.

**Conclusion.** P and F are even and real on R. Both have nonreal zeros, all their zeros satisfy |Re(z)|>4 and |Im(z)|<1/2, and all their paired reciprocal-power sums are strictly positive. F has infinitely many zeros, has order at most 1, has alternating strictly nonzero even Taylor coefficients, and is positive on the imaginary axis.

**Proof.** Put b=1/25 and c=a^{-2}. Then Re(c)>0 since Re(a)²>Im(a)², and |c|=1/(100+1/16)<b/4. The paired sums for P are

T_k=b^k+c^k+conj(c)^k ≥ b^k-2|c|^k > b^k[1-2(1/4)^k]>0.

Its roots are ±5, ±a, and ±conj(a), giving the claimed locations. Its coefficients are 1,-e_1,e_2,-e_3 with

e_1=b+2Re(c)>0, e_2=2b Re(c)+|c|²>0, e_3=b|c|²>0.

Also P(iy)=(1+y²/25)|1+y²/a²|²>0 for real y: the second factor cannot vanish because a² is nonreal. The additional zeros of cos(z/100) are exactly z=100π(n+1/2), n∈Z, all real with absolute value ≥50π>4. Their paired reciprocal-power sums converge and are positive for every k≥1 by comparison with Σ_{n≥0}(n+1/2)^{-2k}. Thus adding them preserves strict positivity of all T_k. Multiplicities, if any roots coincided, would simply add; here the listed sets are disjoint.

Multiplying P's alternating coefficients by the alternating cosine series shows that every even coefficient of F has sign (-1)^n and nonzero magnitude: its coefficient after removing this sign is a sum of positive terms, including the constant-coefficient contribution from P. Moreover F(iy)=P(iy)cosh(y/100)>0. Finally |F(z)|≤C(1+|z|)^6e^{|z|/100}, proving order at most 1. This example does not assert a positive Fourier-kernel representation for F. ∎
