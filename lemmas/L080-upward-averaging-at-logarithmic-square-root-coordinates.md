# Lemma 80: upward averaging at logarithmic square-root coordinates

**Hypotheses.** Fix α>1/2. For integers n≥1 put x_n=sqrt(n)(log(n+1))^α, where log is the natural logarithm. Let 0<b_1<b_2<⋯ tend to H<∞, put w_n=x_n+i b_n, and define

f(z)=Π_{n≥1}(1−z²/w_n²)(1−z²/conjugate(w_n)²).

**Conclusion.** This is a nonzero even real entire function whose zeros are exactly the simple zeros ±w_n, ±conjugate(w_n). For the full upward contribution over zeros counted with multiplicity,

E_f(w_n)=2Σ_{Im ρ>b_n}(Im ρ−b_n)/|ρ−w_n|²,

and q=1−1/sqrt(2)>0, every integer N≥2 satisfies

0≤(1/N)Σ_{n=N}^{2N−1} E_f(w_n)
 ≤32H(1+log(4N))/(log(N+1))^{2α}
   + (2H/(2α−1)) · (q^{-2}(log(4N))^{1−2α}+(log N)^{1−2α}).       (1)

In particular the block averages tend to zero, with bound O_α(H(log N)^{1−2α}), and liminf_n E_f(w_n)=0. No height-tail rate is required.

## Proof

For real t>0, x(t)=sqrt(t)(log(t+1))^α is strictly increasing and tends to infinity. For M≥2 the decreasing positive function 1/(t(log t)^{2α}) gives

Σ_{j>M} x_j^{-2}
 ≤Σ_{j>M} 1/(j(log j)^{2α})
 ≤∫_M^∞ dt/(t(log t)^{2α})
 =(log M)^{1−2α}/(2α−1).                              (2)

Consequently reciprocal squares are summable. Lemma 74 supplies the product and exact simple zero set. Strict height monotonicity shows that the higher zeros are precisely w_j and −conjugate(w_j) for j>n. Hence E_f(w_n)=U_n+V_n, where

U_n=2Σ_{j>n}(b_j−b_n)/((x_j−x_n)²+(b_j−b_n)²),

V_n=2Σ_{j>n}(b_j−b_n)/((x_j+x_n)²+(b_j−b_n)²).

If j>2n, monotonicity of log gives x_n/x_j≤sqrt(n/j)<1/sqrt(2), so x_j−x_n≥q x_j. Equation (2) thus proves convergence of U_n and V_n for each fixed n; there are only finitely many remaining terms.

Fix N≥2 and N≤n<2N. Split U_n into A_n for n<j≤4N and B_n for j>4N. Direct differentiation gives

x'(t)=(log(t+1))^α/(2sqrt(t))
       +α sqrt(t)(log(t+1))^{α−1}/(t+1).

The second term is positive. For N≤t≤4N the first is at least (log(N+1))^α/(4sqrt(N)). Integrating this lower bound between n and j, and dropping the vertical square, yields

A_n≤32N (log(N+1))^{-2α} Σ_{j=n+1}^{4N}(b_j−b_n)/(j−n)².       (3)

Apply the finite increment-crossing argument from Lemma 78. Explicitly, write Δ_r=b_{r+1}−b_r>0 and expand b_j−b_n as Σ_{r=n}^{j−1}Δ_r. For each fixed r and separation k=j−n, at most k possible integers n satisfy n≤r<n+k. All separations are at most 4N. Thus the coefficient of each Δ_r in the double sum over N≤n<2N and n<j≤4N is at most Σ_{k=1}^{4N}1/k≤1+log(4N). All sums here are finite. The increments involved sum to b_{4N}−b_N≤H, so averaging (3) gives the first term of (1).

For j>4N and n<2N the same ratio estimate gives x_j−x_n≥q x_j. Uniformly over the averaging block, (2) implies

B_n≤2Hq^{-2}Σ_{j>4N}x_j^{-2}
 ≤2Hq^{-2}(log(4N))^{1−2α}/(2α−1).

Similarly, x_j+x_n≥x_j and n≥N give

V_n≤2HΣ_{j>n}x_j^{-2}
 ≤2H(log N)^{1−2α}/(2α−1).

These bounds hold for finite partial sums and pass to their increasing limits. Combining them proves (1). Since 1−2α<0, all three terms tend to zero with the stated bound for fixed α. Choosing a minimum in each finite block 2^m≤n<2^{m+1} gives indices tending to infinity whose nonnegative E_f values tend to zero. This proves the lower-limit assertion. ∎

## Qualifications

The result answers the specified logarithmic-coordinate question for every fixed α>1/2. Constants need not remain bounded as α decreases to 1/2. No assertion for arbitrary increasing coordinates, pointwise convergence, penalty maximizers, theta zeros, signed zero velocities, or RH follows. Lemma 79 is a comparison, not a mathematical input to this proof.

## Verification and formalization obligations

This analytic proof requires no numerical certificate. Verify the derivative lower bound on the whole finite block, the log ratio and horizontal separation, the decreasing-integrand tail and its evaluation, the at-most-k crossing count, finite rearrangement, telescoping, and passage to monotone limits. Formalization also needs Lemma 74's product and zero identification, higher-zero enumeration, and finite dyadic minimum selection. Both infinite remainders are explicitly bounded uniformly over each averaging block.
