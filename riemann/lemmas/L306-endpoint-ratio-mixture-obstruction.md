# Lemma 306: endpoint reduced-ratio obstruction to positive zeta-square mixtures

**Hypotheses.** Let r>1 tend to infinity, and use the full finite sum S_r(a) and weights W_r from L303 and L297. For coprime positive integers p,q define

c_r(p,q)=Σ_(d≥1) W_r(dp,dq).

For fixed m≥1 write c_r(m)=c_r(1,m). Put Z=Σ_(d≥1)d^(−2)=ζ(2), μ=Z^(−1)Σ d^(−2)log d, and ν=Z^(−1)Σ d^(−2)(log d)². These series converge. A positive zeta-square mixture here means

F_r(a)=∫_(σ>1) |ζ(σ+ia)|² dη_r(σ),

where η_r is a positive measure with ∫ ζ(σ)² dη_r(σ)<∞. The measure may depend on r. This is a particular representation, not the class of all nonnegative Fourier polynomials.

**Conclusion.** Exact reduced-ratio grouping gives

S_r(a)=Σ_((p,q)=1) c_r(p,q) exp(ia log(q/p)).                 (1)

Every coefficient is nonnegative, so S_r is positive definite as a function of the additive variable a; this does not mean S_r(a)≥0. For each fixed m,

c_r(m)=Z/m · [1−((log m)²+4μ log m+4ν)/(8r)+O_m(r^(−2))].   (2)

Consequently, with ℓ=log 2,

c_r(1)c_r(4)−c_r(2)²=−Z²ℓ²/(16r)+O(r^(−2))<0             (3)

for sufficiently large r. No positive zeta-square mixture of the stated kind equals S_r for all real a. More strongly, any such mixture with sup_(a∈ℝ)|F_r(a)−S_r(a)|=ε_r must have ε_r≥κ/r for all sufficiently large r, for an absolute κ>0. Thus this class cannot approximate S_r uniformly with error o(1/r), in particular not at the exponentially small scale in L302. Nothing here determines the sign at the prescribed a_n or excludes other positive representations or estimates specifically at a_n.

**Proof.** Each pair (j,k) has a unique decomposition (dp,dq) with (p,q)=1; W_r has finite support. This proves (1), without a limiting interchange. For any real a_i and complex b_i the positive-definiteness test is

Σ_(i,j) b_i conjugate(b_j) S_r(a_i−a_j)
 =Σ_((p,q)=1) c_r(p,q)|Σ_i b_i exp(ia_i log(q/p))|²≥0.

Pointwise positivity does not follow from this identity.

Write Q_r(t)=exp(t/2)(1−t/(2r))_+^r as in L297. Direct substitution gives

c_r(m)=m^(−1)Σ_(d≥1)d^(−2)Q_r(log m+2log d).              (4)

We justify expansion of this entire sum, rather than just its first few terms. For 0≤t≤r the Taylor series for log(1−t/(2r)) gives

log Q_r(t)=−t²/(8r)−E_r(t),  0≤E_r(t)≤C t³/r².

For x≥0, |exp(−x)−1+x|≤x²/2, and |exp(−x−E)−exp(−x)|≤E when E≥0. Hence

|Q_r(t)−1+t²/(8r)|≤C(t³+t⁴)/r²,  0≤t≤r.                (5)

For t>r we use 0≤Q_r(t)≤1, including t≥2r where it vanishes, so the same absolute difference is at most 2+t²/(8r). For fixed m, this tail corresponds to d>exp((r−log m)/2). Integral comparison gives, for each fixed integer k≥0,

Σ_(d>D) d^(−2)(log d)^k=O_k(D^(−1)(1+log D)^k).

For large D this follows by eventual monotonicity and substituting x=exp(u) in the integral; the resulting exponential moment tail has the stated bound by repeated integration by parts. The tail error in (4) is therefore O_m((1+r)exp(−r/2))=O_m(r^(−2)). Summing (5) against d^(−2), whose logarithmic moments through degree four converge, proves

Σ d^(−2)Q_r(log m+2log d)
 =Z−[Z(log m)²+4Zμ log m+4Zν]/(8r)+O_m(r^(−2)).

This is (2). If A(L)=L²+4μL+4ν, then A(0)+A(2ℓ)−2A(ℓ)=2ℓ². Substitution into the determinant, including the factors 1/m, proves (3).

We now establish the necessary inequality for a mixture, not merely for an arbitrary coefficient matrix. Absolute Dirichlet convergence for σ>1 and the integrability hypothesis imply an absolutely summable frequency expansion of F_r, since the sum of the absolute coefficients before grouping is ∫ζ(σ)²dη_r. Its coefficient at log m is

b_r(m)=∫ ζ(2σ)m^(−σ) dη_r(σ).                         (6)

Indeed the pairs with k/j=m are precisely (d,dm), contributing Σ d^(−2σ)m^(−σ). In particular b_r(1), b_r(2), b_r(4) are the zeroth, first and second moments of x=2^(−σ) for the finite positive measure ζ(2σ)dη_r. Cauchy–Schwarz gives

b_r(1)b_r(4)−b_r(2)²≥0.                               (7)

Frequency coefficients are uniquely recoverable by the averages

lim_(A→∞) (1/(2A))∫_(−A)^A F_r(a) exp(−ia log m) da.

For a single exponential the limit is one at equal frequency and zero otherwise. Absolute summability justifies passage through the expansion by dominated convergence; the same argument for S_r is finite. The uniform error hypothesis therefore implies |b_r(m)−c_r(m)|≤ε_r for m=1,2,4. Equation (4) and Q_r≤1 give 0≤c_r(m)≤Z/m. If ε_r≤1, expansion of the two determinants consequently yields

|(b_r(1)b_r(4)−b_r(2)²)−(c_r(1)c_r(4)−c_r(2)²)|≤C₁ε_r

with an absolute constant C₁, independent of r and η_r. Equations (3) and (7) imply C₁ε_r≥Z²ℓ²/(32r) for all sufficiently large r. If ε_r>1, the claimed κ/r bound holds as well after reducing κ. Equality is the case ε_r=0 and is impossible. This proves all assertions. ∎

The negative minor in L297 allowed arbitrary vectors in the original index matrix and did not test the coefficients after equal-frequency grouping. Here all gcd multiples have been summed, and the obstruction concerns moments of a proposed positive mixture. Positive Fourier coefficients already hold in (1); confusing positive definiteness with pointwise nonnegativity would still hide the missing sign. The quantitative uniform obstruction is of order 1/r, whereas L302 needs a positive endpoint margin dominating (1+r)²exp(−r/256). The latter is o(1/r). Failure of this uniform mixture comparison supplies neither a negative value of S_r nor any lower bound at a_n. A coarser mixture approximation with a proved positive margin larger than its error is not excluded. Smaller indices and bounded exterior heights also remain unresolved.

**Mathlib.** Full statement: not checked. Supporting coprime factorization, Cauchy–Schwarz, positive definiteness of Fourier transforms of positive finite measures, and absolutely convergent Dirichlet series: not checked. No library match is claimed. All regrouping, expansion, coefficient recovery, and quantitative obstruction arguments are proved above. The zeta series is used only on σ>1; no zero-free estimate or analytic continuation is needed.
