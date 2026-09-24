# Lemma 239: full-transform decay and the moving-sector smoothing ratio

**Hypotheses.** Use F, F_N, ε_N, and B=π(N+1)² as in L237, the profile p(t)=4/(4+t²) of L238, and R_N and a_N^* of L236.

**Conclusion.** For j=0,1,2,

sup_{3≤t≤4} B^j |F^(j)(Bt)|/ε_N = O(B^j exp(−B/2)).

Consequently F_N(Bt)/ε_N=−p(t)+O(B^(−1)) in C²([3,4]), where derivatives in this last assertion are in t. For sufficiently large N, F_N has no zeros on this sector and

B² R_N(Bt)=(t²−4)/(t²+4)²+O(B^(−1))

uniformly there. In particular

sup_{3≤t≤4} R_N(Bt)=B^(−2)(1/32+O(B^(−1))),
a_N^* ≥ B^(−2)(1/32−C/B)

for an absolute constant C and all sufficiently large N. This is a sector estimate, not an upper bound for the global threshold.

**Proof.** First establish exponential Fourier decay with derivative control without a zero-distribution assumption. On the strip S={z: |Im z|<π/4}, define

A(z)=exp(z/2) Σ_{n≥1} exp(−πn² exp(2z)),
k(z)=2A''(z)−A(z)/2.

The series and every fixed derivative converge locally uniformly: on each compact subset of S, Re(exp(2z)) has a positive minimum, and all derivative factors are bounded by a fixed polynomial in n. Thus A and k are holomorphic. The real theta transformation in L016 gives

A(−u)=A(u)+sinh(u/2)  (u real).

Both sides are holomorphic on S, so the identity theorem extends the equality to S. Applying 2d²/dz²−1/2 annihilates sinh(z/2) and gives k(−z)=k(z). By L019, k(u)=K(u) for u≥0, so k on the real axis is precisely the even kernel defining F in L237.

Fix 0<a<π/4. For r≥0 and |v|≤a, the differentiated series gives

|k(r+iv)| ≤ C_a exp(9r/2) exp(−π cos(2a) exp(2r)).

Indeed each summand is bounded by (8π²n⁴ exp(9r/2)+12πn² exp(5r/2)) exp(−πn² cos(2a) exp(2r)); factor out the n=1 exponential and sum the remaining polynomial times exp(−π cos(2a)(n²−1)). Evenness gives the same bound with |r| for r≤0. Therefore, for each j=0,1,2, (1+|r|)^j |k(r+iv)| has a common integrable bound on |v|≤a and tends to zero superexponentially at both ends.

For fixed real x≥0, apply Cauchy's integral theorem on the rectangle with vertices −R,R,R+ia,−R+ia to (iz)^j k(z) exp(ixz). The vertical edges tend to zero by the preceding bound and |exp(ixz)|≤1 on these edges. Absolute domination on the horizontal edges gives

F^(j)(x)=∫_R (i(r+ia))^j k(r+ia) exp(ix(r+ia))dr.

Here the formula for F^(j) on the original real line follows by dominated differentiation of its Fourier integral. Thus |F^(j)(x)|≤C_{a,j} exp(−ax). There is no differentiation of an asymptotic remainder. Choose a=1/2<π/4. L238 gives ε_N bounded below by a positive constant times exp(−B) for large N. Since x=Bt≥3B, division yields the first asserted estimate. In particular B^j exp(−B/2)=O(B^(−1)) for all three fixed j.

Put Q_N(t)=F_N(Bt)/ε_N. The identity F_N=F−E_N, the first bound, and L238 show Q_N=−p+O(B^(−1)) with two derivatives uniformly on [3,4]. Since p≥1/5 there, Q_N is bounded away from zero for large N. The chain rule now gives

B² R_N(Bt)=[Q_N Q_N''−Q_N'²]/(2Q_N²)
=(log p)''/2+O(B^(−1))
=(t²−4)/(t²+4)²+O(B^(−1)).

The function h(t)=(t²−4)/(t²+4)² has derivative 2t(12−t²)/(t²+4)³, so its maximum on [3,4] is h(√12)=1/32. Uniform errors commute with taking a supremum up to their uniform bound. Finally a_N^* is the supremum over every real nonzero point of F_N, and hence is at least this sector supremum. ∎

The achieved sector contribution tends to zero at rate B^(−2). It supplies neither a nonvanishing obstruction nor the required global upper bound a_N^*→0. Frequencies outside this sector, including near-zero transition regions, can dominate the supremum. Even a vanishing global threshold would prove only first associated-spectrum positivity, not the all-degree mixed positivity needed for RH.

**Mathlib.** Not checked for the full statement or supporting holomorphic-series, identity-theorem, contour-shift, and differentiation-under-integral results. No matching theorem is claimed. General documentation: https://leanprover-community.github.io/mathlib4_docs/
