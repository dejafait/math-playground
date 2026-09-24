# Lemma 298: endpoint Mellin representation and finite-head curvature

**Hypotheses.** Use the finite set J_r and phase sum T_r(a) of L297, with r>1 and a real. For a finite set J of positive integers define P_J(s)=Σ_(j∈J) j^(−s). Powers on the right half-plane use the analytic logarithm real on the positive axis.

**Conclusion.** For every c>0 there is an absolutely convergent identity

T_r(a)=Γ(r+1)/(2r)^r · (1/(2πi)) ∫_(c−i∞)^(c+i∞)
 exp(2rz) z^(−r−1) P_(J_r)(1/2+z+ia) P_(J_r)(1/2+z−ia) dz.       (1)

For integer r and Q_J(σ,a)=|P_J(σ+ia)|², the interior sum also satisfies the exact finite differential identity

T_r(a)=[(1+(1/(2r))∂_σ)^r Q_(J_r)(σ,a)]_(σ=1/2).              (2)

For each fixed N, the sum T_(r,N) restricted to 1≤j,k≤N has, uniformly for all real a as r→∞,

T_(r,N)(a)=Q_N(1,a)−(1/(8r))∂_σ²Q_N(1,a)+O_N(r^(−2)),        (3)

where Q_N uses J={1,…,N}. For every N≥2 the correction in (3) is strictly negative at a=0. The relative weight replacement underlying (3) is not uniform on J_r: there exist j=k in J_r for which W_r(j,k)/(jk)^(−1)→exp(−1/8), rather than 1.

These identities do not establish a sign for T_r(a), a lower bound at the theta-related values of a, or an endpoint stationary-phase error estimate.

**Proof.** For t real and c>0, Fourier inversion of the continuous integrable function

f(t)=1_(t≥0) exp(−ct)t^r/Γ(r+1)

gives

t_+^r/Γ(r+1)=(1/(2π))∫_ℝ exp((c+iv)t)(c+iv)^(−r−1) dv.     (4)

Indeed its Fourier transform, with kernel exp(−ivt), is (c+iv)^(−r−1). This follows from the gamma integral for positive real c and then analytic continuation to Re z>0; differentiation under the integral is justified on compact subsets by exponential decay. The transform is integrable since r>0, so the ordinary Fourier inversion theorem applies at every t, including zero. This also proves absolute convergence of the integral in (4).

Apply (4) with t=2r−log(jk), multiply by Γ(r+1)(2r)^(−r)(jk)^(−1/2)exp(ia log(k/j)), and sum over the finite set J_r². This is precisely W_r(j,k) times its phase. Finite summation factors the two Dirichlet polynomials and proves (1). For fixed r, the polynomials are bounded on Re z=c, and the remaining integrand has modulus at most a constant times (c²+v²)^(−(r+1)/2). Thus no conditionally convergent interchange is involved.

For (2), expand

Q_J(σ,a)=Σ_(j,k∈J) exp(−σ log(jk))exp(ia log(k/j)).

Each ∂_σ multiplies a term by −log(jk). The binomial differential operator therefore supplies (1−log(jk)/(2r))^r. For j,k∈J_r, log(jk)<3r/2<2r, so this agrees with the cutoff weight and proves (2). Here the index set is held fixed when differentiating; no differentiation in r is intended.

For (3), write L=log(jk). On a fixed finite head, Taylor's theorem uniformly gives

r log(1−L/(2r))=−L/2−L²/(8r)+O_N(r^(−2)),

W_r(j,k)=(jk)^(−1)[1−L²/(8r)+O_N(r^(−2))].

Summing and using the displayed expansion of Q proves (3), with an error uniform in a because every phase has modulus one. At a=0, the second derivative is the finite sum

∂_σ²Q_N(1,0)=Σ_(1≤j,k≤N) (log(jk))²/(jk)>0

for N≥2. Thus the first correction is strictly negative there; it cannot be treated as a nonnegative added term. This test at a=0 is algebraic, not an assertion about the large theta-related height.

Finally take j=k=floor(exp(sqrt(r)/2)). These indices lie in J_r for large r and L/sqrt(r)→1. Consequently

log(W_r(j,k)/(jk)^(−1))=L/2+r log(1−L/(2r))→−1/8.

This proves the nonuniformity assertion. ∎

On z=c+iv the two factors in (1) have imaginary parts v+a and v−a; they are conjugates only when v=0 (apart from accidental equalities). The complex kernel in (1) is not a nonnegative measure. Thus (1) itself is not a nonnegative average of modulus squares. It does not rule out an alternative arithmetic representation. Equation (3) only controls fixed N; it cannot be substituted for the full growing sum without an additional tail estimate. L297 gives total absolute mass 4r+o(r), so an interior per-pair error ε_r W_r still needs ε_r=o(1/r) for additive o(1) control, and positivity would additionally need an appropriate positive lower bound.

**Mathlib.** Full statement: not checked. Supporting Fourier inversion, gamma integral, and finite differential identities: not checked. No library match is claimed. Fourier inversion is the standard inversion theorem for an integrable continuous function with integrable Fourier transform, with its hypotheses verified above. The remaining identities and estimates are proved here.
