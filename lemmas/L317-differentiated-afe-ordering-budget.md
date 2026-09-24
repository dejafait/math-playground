# Lemma 317: differentiated approximate-functional-equation budget for level ordering

**Hypotheses.** Use the actual completion f=Ξ of L018 and the definitions H, θ, Z, B_1, B_2, κ=B_2/B_1>0 and J=B_2(R_2−R_1)/H² from L316. In particular,

Q(U)=U'²−UU'',       T(U)=UU''''−4U'U'''+3U''²,
Z(a)=exp(iθ(a))ζ(1/2+ia),       θ(a)=Im log Γ(1/4+ia/2)−a log(π)/2.

All derivatives are with respect to real height. Let a tend to +∞ through arbitrary real values, and set

X=sqrt(a/(2π)),       N=floor(X),       L=log X,
λ_n=θ'(a)−log n,      φ_n=θ(a)−a log n,       1≤n≤N,
P_κ(v)=v⁴−κv²,
U_a(x)=2Σ_(n≤N)n^(−1/2)cos(φ_n+λ_n x).

N, φ_n and λ_n are held fixed when differentiating U_a in x. No zero hypothesis, first-level sign, or ordering assumption is made. The classical approximate functional equation and third-derivative test recorded in the foundations are unconditional inputs.

**Conclusion.** Uniformly at all sufficiently large real heights, including cutoff transitions,

Z^(j)(a)=U_a^(j)(0)+O_j(a^(−1/4)(log a)^j),       0≤j≤4.       (1)

There is a decomposition

J(a)=D_κ(a)+E_κ(a)+O_κ(L⁴),                                  (2)
D_κ(a)=Σ_(n≤N)P_κ(2λ_n)/n=(16/5)L⁵+O_κ(L⁴),                 (3)
E_κ(a)=2Σ_(1≤n<m≤N)(nm)^(−1/2) {
  P_κ(λ_n+λ_m)cos(a log(m/n))
 +P_κ(λ_n−λ_m)cos(2θ(a)−a log(nm))}.                         (4)

Thus the diagonal is eventually positive and the analytic remainder is smaller than it. However, the coefficientwise absolute budget

B_κ(a)=2Σ_(1≤n<m≤N)(nm)^(−1/2)
          (|P_κ(λ_n+λ_m)|+|P_κ(λ_n−λ_m)|)                    (5)

satisfies c_κN≤B_κ(a)≤C_κN for some positive constants. In particular B_κ/D_κ tends to infinity, on the scale sqrt(a)/(log a)⁵. Keeping the oscillations and applying the recorded third-derivative test gives the smaller bound

|E_κ(a)|≤C_κ a^(1/3)L⁶,                                     (6)

whose error envelope divided by the diagonal still tends to infinity, on the scale a^(1/3)L. Neither certificate proves the required sign J≥0. These are limitations of the stated bounds, not lower bounds on |E_κ|, a negative actual-theta value, or a disproof of actual averaged ordering. No established sign or zero-exclusion range is extended.

**Proof.** The analytic Stirling remainder argument of L316 gives

θ'(a)=L+O(a^(−2)),       θ^(j)(a)=O_j(a^(1−j)),       2≤j≤4.  (7)

For example these follow by taking the imaginary part of L316's analytic expansion for β and its differentiated remainder; its real envelope does not contribute to θ. A holomorphic extension near the real height is

θ(z)=[log Γ(1/4+iz/2)−log Γ(1/4−iz/2)]/(2i)−z log(π)/2,

with conjugate branches on the real axis. Both gamma arguments have positive real part on a disk of sufficiently small fixed radius. The same Stirling estimates there give θ'(z)=O(log a). The symmetric functional equation in L018 gives the exact identity

χ(1/2+iz)=π^(iz)Γ(1/4−iz/2)/Γ(1/4+iz/2)=exp(−2iθ(z)).       (8)

Fix the height a and put ρ=1/log a. For |z−a|≤ρ, write s=1/2+iz=σ+it. Then |σ−1/2|≤ρ, |t−a|≤ρ and, for large a, σ∈[1/4,3/4]. In the approximate functional equation choose x=X fixed and y=t/(2πX). Its two errors are O(a^(−1/4)) on this whole disk: factors such as a^ρ are bounded, and x,y are comparable to sqrt(a). Also exp(±iθ(z))=O(1), since θ(a) is real and ρ sup|θ'|=O(1); hence χ(s)=O(1) there.

The first sum ends at N. Since |y−X|≤ρ/(2πX)<1, the second sum differs from the sum to N by at most one endpoint term, with modulus O(a^(−1/4)) after multiplication by χ(s). This remains true when X is an integer. Consequently the fixed-cutoff analytic function

F_a(z)=Z(z)−2Σ_(n≤N)n^(−1/2)cos(θ(z)−z log n)

is O(a^(−1/4)) throughout the disk. This is a pointwise application of the approximate functional equation to bound an already analytic function; no analyticity of the auxiliary moving cutoff y is asserted. Cauchy's estimate on the disk gives

F_a^(j)(a)=O_j(a^(−1/4)(log a)^j),       0≤j≤4.              (9)

In particular the derivative claim is justified without differentiating a real big-O or the function floor(X).

We will use, for each fixed integer 0≤j≤4,

A_j:=Σ_(n≤N)n^(−1/2)(1+|λ_n|)^j=O_j(sqrt(N)).              (10)

To see this, partition the indices into intervals X/2^(k+1)<n≤X/2^k, stopping when the interval contains the smallest indices. On this block |λ_n|≤C(1+k) by (7), and the sum of n^(−1/2) is at most C sqrt(X)2^(−k/2). Summing the convergent series Σ_k 2^(−k/2)(1+k)^j proves (10), with the last one-point block obeying the same bound up to an absolute constant.

Put S_a(z)=Z(z)−F_a(z). Its derivatives at a differ from U_a's only because the phase θ(z) is not affine. For one summand, write λ=θ'(a)−log n and μ=θ''(a), ν=θ'''(a), ξ=θ''''(a). For orders two, three and four the differences from the affine-phase derivatives of cos φ are, respectively,

−μ sin φ,
−3λμ cos φ−ν sin φ,
−(3μ²+4λν)cos φ+(6λ²μ−ξ)sin φ.

Orders zero and one agree exactly. By (7) their absolute values are at most C a^(−1)(1+|λ|²). After multiplying by 2n^(−1/2), (10) bounds the summed correction by O(a^(−1)sqrt(N))=O(a^(−3/4)). Combine this with (9) to prove (1).

Write u_j=U_a^(j)(0). Equation (10) gives u_j=O_j(sqrt(N)) for 0≤j≤4. In a quadratic product of derivative orders j,k with j+k≤4, replacing Z^(j), Z^(k) by u_j,u_k therefore costs at most

O(sqrt(N)a^(−1/4)((log a)^j+(log a)^k)
       +a^(−1/2)(log a)^(j+k))=O((log a)⁴).

For Q the same reasoning gives O((log a)²). L316's remaining real gamma correction is bounded by C a^(−2)(|Q(Z)|+Z²). Here (1) and (10) give |Q(Z)|+Z²=O(N), so that correction is O(a^(−3/2)). It follows that

J(a)=T(U_a)(0)−κQ(U_a)(0)+O_κ(L⁴).                        (11)

The passage to (11) uses absolute errors; it does not divide by Z or its derivatives and is valid at real zeros.

For a finite exponential sum U(x)=Σ_b c_b exp(i(ψ_b+ν_b x)), symmetric expansion of the two quadratic forms gives

T(U)(0)−κQ(U)(0)
 = (1/2)Σ_(b,c)c_b c_c P_κ(ν_b−ν_c)exp(i(ψ_b+ψ_c)).        (12)

Indeed the symmetric kernel for Q is (ν_b−ν_c)²/2, while the one for T is (ν_b−ν_c)⁴/2. This follows by expanding (ν_b−ν_c)⁴, including the two mixed cubic terms. Apply (12) to the 2N modes indexed by (n,ε), ε=±1, with coefficient n^(−1/2), frequency ελ_n and phase εφ_n. Opposite signs give P_κ(λ_n+λ_m)cos(φ_n−φ_m); equal signs give P_κ(λ_n−λ_m)cos(φ_n+φ_m), each in a sum over ordered n,m. The equal-index equal-sign term is zero because P_κ(0)=0. The other equal-index term is precisely D_κ. Grouping the two orders for n<m gives (4), since φ_n−φ_m=a log(m/n). This proves (2) with all factors in its diagonal and cross terms.

For p=2 or 4, monotone integral comparison for the nonnegative decreasing function x^(−1)(log(X/x))^p on [1,X] gives

Σ_(n≤N)n^(−1)(L−log n)^p
 = ∫_1^X (log(X/x))^p dx/x+O(L^p)
 = L^(p+1)/(p+1)+O(L^p).                                (13)

The incomplete final interval [N,X] contributes no larger error. Replacing L−log n by λ_n changes this sum by O(a^(−2)(L^p+L)), using (7) and the lower power sums from the same integral comparison. Therefore

D_κ=16Σ_(n≤N)λ_n⁴/n−4κΣ_(n≤N)λ_n²/n
   =(16/5)L⁵−(4κ/3)L³+O_κ(L⁴),                          (14)

which implies (3) and eventual positivity. The cubic term in (14) is displayed only to identify its source; the stated error is larger than that term.

For the upper bound in (5), |P_κ(v)|≤|v|⁴+κ|v|² and the elementary power inequalities imply

B_κ≤C_κ A_0(A_4+A_2)=O_κ(N).                             (15)

For a lower bound put c=exp(−sqrt(κ)−3). For all sufficiently large N the interval [cN,2cN] contains at least cN/2 integers. For two distinct indices in it,

λ_n+λ_m≥2log(X/(2cN))+O(a^(−2))>sqrt(κ)+1.

Thus P_κ(λ_n+λ_m)>1 for large a. There are at least a positive constant times c²N² pairs n<m in this interval, and (nm)^(−1/2)≥1/(2cN). Keeping just these positive terms of the absolute budget proves B_κ≥c_κN. This is a lower bound for the budget itself, with no assertion that the actual cosines align or that |E_κ| has comparable size.

For completeness, one can use the phases to improve the bound, but the recorded low-order derivative estimate is still insufficient. Define

W_j=Σ_(n≤N)n^(−1/2)λ_n^j exp(−ia log n),       0≤j≤4.

On a dyadic block M≤n<2M, the real phase g(x)=−a log x/(2π) has |g'''(x)| comparable to a/M³, with a fixed comparability constant. The third-derivative test in the foundations bounds every partial sum in the block by

C(a^(1/6)M^(1/2)+a^(−1/6)M).

Singletons obey the same bound for large a. The supremum plus total variation of the weight x^(−1/2)(θ'(a)−log x)^j on the truncated block is at most

C_j M^(−1/2)(1+log(X/M))^j.

This follows by differentiating this polynomial weight; it also holds if λ changes sign near the last endpoint. Partial summation therefore bounds the block's weighted sum by

C_j(a^(1/6)+a^(−1/6)sqrt(M))(1+log(X/M))^j.

Since M≤N≤X, the second term is O(a^(1/12)), and summing O(log a) blocks yields

W_j=O_j(a^(1/6)L^(j+1)).                                  (16)

Now u_j=2Re(exp(iθ(a))i^j W_j). Products in T(U_a) are consequently O(a^(1/3)L⁶), and those in Q(U_a) are O(a^(1/3)L⁴). By the exact finite identity D_κ+E_κ=T(U_a)−κQ(U_a), subtracting (3) proves (6). No height averaging, zero-location theorem or cancellation not contained in the third-derivative test has been used. ∎

The actual target is J≥0 at every sufficiently large height, with the remaining finite range and later levels still requiring proof. In (2) the missing input is a one-sided lower bound for E_κ: for example E_κ≥−(1−η)D_κ for a fixed η>0 would give a positive surplus exceeding the O_κ(L⁴) remainder. The obtained bounds give no such surplus: B_κ/D_κ is comparable to sqrt(a)/L⁵, and the upper envelope in (6) divided by D_κ has order a^(1/3)L. This stops diagonal dominance from these absolute or third-derivative estimates, not a different phase-sensitive estimate. The separate endpoint arithmetic margin is unaffected.

The command `python3 scripts/laguerre/check_afe_polarization.py` checks the pairwise polynomial kernel in (12) and the factors in its real cosine grouping with exact rational arithmetic. It is an independent finite algebra check, not a numerical zeta sign test; the analytic bounds and uniformity are proved above.

**Mathlib.** Full statement: not checked. Supporting approximate functional equations, Cauchy derivative estimates, finite-sum polarization, integral comparison and exponential-sum bounds: not checked for Mathlib coverage; no matching theorem is asserted. The supporting named input is the Hardy–Littlewood approximate functional equation, in Titchmarsh–Heath-Brown, [Theorem 4.15 and equation (4.12.4)](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=44), checked for its strip and cutoff hypotheses. The other supporting analytic inputs are logarithmic complex Stirling, [DLMF 5.11.1](https://dlmf.nist.gov/5.11.E1), and the third-derivative test in Olivier Robert, [*On van der Corput's k-th derivative test for exponential sums*, derivation preceding Theorem 2](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf), as recorded in the foundations. None is a match for the full level-ordering budget. The [Mathlib reference portal](https://leanprover-community.github.io/mathlib4_docs/) is retained without a coverage claim.
