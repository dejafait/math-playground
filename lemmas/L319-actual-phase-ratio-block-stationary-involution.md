# Lemma 319: stationary involution of the actual-phase ratio block

**Hypotheses.** Use L317's actual real height a→+∞, X=sqrt(a/(2π)), N=floor(X), L=log X, fixed κ>0, and θ'(a)=L+δ with δ=O(a^(−2)). For every real x>0 define λ_x=θ'(a)−log x and P_κ(v)=v^4−κv^2. Set

I={n∈Z: N/2<n≤N},
J={k∈Z: X^2/N≤k<2X^2/N},
μ_k=log(k/X)+δ,
C(a)=exp(i[a−a log(X^2)+π/4]).

For 0≤j≤4 put

W_j=Σ_(n∈I)n^(−1/2)λ_n^j exp(−ia log n),
V_j=Σ_(k∈J)k^(−1/2)μ_k^j exp(ia log k).

All cutoffs and coefficients are held fixed; no height derivatives of these sharp sums are taken. Define the ordered ratio form, including its diagonal, by

R_I=Σ_(n,m∈I)(nm)^(−1/2)P_κ(λ_n+λ_m)cos(a log(m/n)),
D_I=Σ_(n∈I)P_κ(2λ_n)/n,       E_I=R_I−D_I.

Define R_J, D_J and E_J by the same formulas with I replaced by J and λ defined on that exterior interval as above. Thus J lies near [X,2X]; it is not another subset of the original sum to N. No zero hypothesis or actual-theta sign is assumed. The named van der Corput B-process and third-derivative test in the foundations are supporting inputs.

**Conclusion.** Uniformly at all sufficiently large real heights, including integer or arbitrarily near-integer endpoint slopes,

W_j=C(a)V_j+O_j(N^(−1/2)log(2N)),       0≤j≤4,             (1)
R_I=R_J+O_κ(log(2N)),
E_I=E_J+O_κ(log(2N)).                                    (2)

In particular (E_I−E_J)/L^5=O_κ(L^(−4)), so E_I≥−o(L^5) holds if and only if the same assertion holds for E_J. At the stationary-main-term level the reciprocal map x↦X^2/x is an involution: transforming the dual sum with its exact μ weights returns W_j, up to the same error in (1). The common phases cancel in the ratio form, and the even polynomial kernel is preserved, with a δ-dependent correction smaller than the error in (2).

Both diagonals satisfy

D_I=d_κ+O_κ(N^(−1)),       D_J=d_κ+O_κ(N^(−1)),
d_κ=(16/5)(log 2)^5−(4κ/3)(log 2)^3.                      (3)

For K=I or J the off-diagonal absolute coefficient budget satisfies

c_κN≤Σ_(n,m∈K, n≠m)(nm)^(−1/2)|P_κ(λ_n+λ_m)|≤C_κN      (4)

with fixed positive constants. The recorded third-derivative test, applied separately to the weighted sums, gives the envelopes

|E_I|+|E_J|=O_κ(a^(1/3)),
E_I≥−C_κ[a^(1/3)+log(2N)]                               (5)

where the second is also the bound transferred from E_J by (2). The envelope a^(1/3)/L^5 tends to infinity, while log(2N)/L^5 tends to zero. Thus the stationary error meets the desired scale, but neither the transformation nor these bounds establish a lower bound E_I≥−o(L^5). This is a limitation of the tested signing mechanism, not a lower bound on |E_I|, a negative actual value, or an impossibility theorem for additional cancellation arguments. No established sign or zero-exclusion range changes.

**Proof.** The supporting transform is J. Vandehey, [*Error term improvements for van der Corput transforms*, Theorem 1.1, pp. 2–3](https://arxiv.org/pdf/1205.0090#page=2), recording Huxley's Lemma 5.5.3. Its C^4 phase and real bounded-variation amplitude hypotheses, and its error uniform in endpoint slopes, are checked explicitly below. It is a finite stationary transform; we do not apply an unqualified Poisson identity to a discontinuous cutoff.

Write e(t)=exp(2πit). On [N/2,N] apply the theorem with

f(x)=−X^2 log x,       g_j(x)=x^(−1/2)λ_x^j,
M=N,       T=X^2.

Here N≤X<N+1, so X/N→1 uniformly. The derivatives are

f'(x)=−X^2/x,       f''(x)=X^2/x^2,
f'''(x)=−2X^2/x^3,       f''''(x)=6X^2/x^4.               (6)

Thus f'' is positive and comparable to T/M^2, while the next derivatives are O(T/M^3) and O(T/M^4). On the whole interval |λ_x|≤C, and

g_j'(x)=x^(−3/2)[−λ_x^j/2−jλ_x^(j−1)],

where the second term is absent when j=0. Consequently

|g_j(N/2)|+Var(g_j)=O_j(N^(−1/2)).                        (7)

The range of f' has length X^2/N, so the cited theorem gives error

O_j(N^(−1/2)[N/X+log(2+X^2/N)])
 =O_j(N^(−1/2)log(2N)).                                  (8)

At frequency −k the stationary point is x_k=X^2/k. Its amplitude and phase are exactly

g_j(x_k)/sqrt(f''(x_k))
 =k^(−1/2)[θ'(a)−log(X^2/k)]^j
 =k^(−1/2)μ_k^j,
2π[f(x_k)+kx_k+1/8]
 =a log k−a log(X^2)+a+π/4.                              (9)

The reciprocal interval is precisely the displayed J apart from endpoint conventions. The theorem's closed sums may be changed to I and J by altering at most one term on each side. All such terms are O_j(N^(−1/2)), since both primal and dual variables are comparable to N and their logarithmic factors are bounded. If starred conventions are used, at most two terms on each side change by the same bound. This is uniform even when a slope is exactly an integer or crosses one. Equations (8)–(9) prove (1) with the stated half-open intervals.

For the reverse transform use the phase +X^2 log k on the dual interval and amplitude k^(−1/2)μ_k^j. Its curvature is negative. Conjugating the positive-curvature theorem changes +1/8 to −1/8. Its stationary point for positive frequency n is k_n=X^2/n, and

μ_(k_n)=log(X/n)+δ=λ_n,
(k_n^(−1/2)μ_(k_n)^j)/sqrt(X^2/k_n^2)=n^(−1/2)λ_n^j,
2π[X^2 log(k_n)−nk_n−1/8]
 =−a log n+a log(X^2)−a−π/4.                            (10)

The new common phase is conjugate(C(a)). For this reverse application take M=2N and T=X^2; its interval length X^2/N is at most 2N for all sufficiently large N. The derivative and amplitude-variation estimates have the same orders because all its points are comparable to N. Its reflected half-open interval is I, with the already bounded endpoint adjustments. Thus V_j=conjugate(C(a))W_j+O_j(N^(−1/2)log(2N)). This is an asymptotic involution, not an exact equality of finite integer sums.

To pass to the quadratic form, for a five-component vector z define

H_κ(z)=Σ_(j=0)^4 binom(4,j)z_j conjugate(z_(4−j))
          −κΣ_(j=0)^2 binom(2,j)z_j conjugate(z_(2−j)).    (11)

Each sum in (11) is real by pairing j with its complementary index. Expanding the finite products gives R_I=H_κ(W) exactly: the binomial identity supplies P_κ(λ_n+λ_m), and pairing n,m replaces the phase by its cosine. In particular no modulus-square substitution is made for an indefinite polynomial kernel.

The direct absolute bounds |W_j|+|V_j|=O_j(sqrt(N)) follow by summing n^(−1/2) over their intervals; the logarithmic factors are bounded. Inserting (1) in (11), and using |C(a)|=1, therefore gives

R_I=Σ_(k,l∈J)(kl)^(−1/2)P_κ(μ_k+μ_l)cos(a log(k/l))
                  +O_κ(log(2N)).                         (12)

Indeed each mixed error is O(sqrt(N)·N^(−1/2)log(2N)), and the error-error products are O(N^(−1)log^2(2N)) and can be absorbed. This controls the full ordered sum, including the diagonal.

Now μ_k=−λ_k+2δ, so μ_k+μ_l=−(λ_k+λ_l)+4δ. All these arguments lie in a fixed bounded interval. P_κ is even and its derivative is bounded on that interval, giving

|P_κ(μ_k+μ_l)−P_κ(λ_k+λ_l)|≤C_κ|δ|.

Summing the coefficients costs O(N|δ|)=O(a^(−3/2)), since (Σ_(k∈J)k^(−1/2))^2=O(N). Replacing the kernel in (12) and using the evenness of cosine proves the first formula in (2). The exact μ transformation is what makes (10) an involution; replacing it by λ uses the explicitly bounded small correction.

For the diagonals, the functions x^(−1)P_κ(2λ_x) on [N/2,N] and x^(−1)P_κ(2μ_x) on [X^2/N,2X^2/N] have size O_κ(N^(−1)) and derivative O_κ(N^(−2)). Comparing a sum with its integral one unit interval at a time, including the two partial endpoint intervals, costs O_κ(N^(−1)). Substitution x=X^2/y makes the two integrals equal, because dx/x=−dy/y and λ_(X^2/y)=μ_y. Their common value is

∫_(log(X/N))^(log(2X/N)) P_κ(2u+2δ)du
 =∫_0^(log 2) P_κ(2u)du+O_κ(N^(−1)+|δ|),                (13)

as log(X/N)=O(N^(−1)). Replacing μ by λ in the dual diagonal costs only O_κ(|δ|), since Σ_(k∈J)1/k=O(1). Integrating 16u^4−4κu^2 proves (3). In particular D_I−D_J=O_κ(N^(−1)), so subtracting these diagonals from the first formula in (2) proves its off-diagonal version.

The upper bounds in (4) follow from boundedness of the polynomial arguments and Σ_(n∈K)n^(−1/2)=O(sqrt(N)). For the lower bounds choose u_0 strictly between 0 and log 2 with P_κ(2u_0)≠0. Such a point exists because this nonzero polynomial has only finitely many roots. Choose a sufficiently small fixed ε>0 with [u_0−ε,u_0+ε]⊂(0,log 2) so that |P_κ(u+v)| is bounded below by a positive constant whenever u,v lie in that interval. The same lower bound, reduced by a fixed factor if necessary, holds after the O(|δ|) shifts. There are a positive constant times N integers n∈I with log(X/n) in this interval, and equally many k∈J with log(k/X) there, for all sufficiently large a. On the latter block λ_k=δ−log(k/X), and evenness of P_κ gives the same conclusion. Retaining pairs of distinct such indices gives a positive constant times N^2 terms, each at least a positive constant divided by N. This proves (4); it is a lower bound for the absolute budget, not for the actual oscillatory sum.

Finally, on either interval the real phase ±a log x/(2π) has third derivative of size comparable to a/N^3. The recorded third-derivative test bounds every partial unweighted sum there by

O(a^(1/6)N^(1/2)+a^(−1/6)N).                            (14)

This bound is valid for shortened subintervals by enlarging their length to O(N), with empty and singleton sums treated separately. For any of the weights x^(−1/2)λ_x^j or x^(−1/2)μ_x^j, its supremum plus total variation is O_j(N^(−1/2)). Finite partial summation in (14) gives

O_j(a^(1/6)+a^(−1/6)sqrt(N))=O_j(a^(1/6))                 (15)

for every corresponding weighted sum, since N is comparable to sqrt(a). Insert (15) in the finite polynomial (11) to obtain O_κ(a^(1/3)) for both ratio forms. Subtracting the bounded diagonals (3) proves (5). This near-cutoff estimate has no dyadic logarithmic loss, but its power of a still exceeds every fixed power of L. ∎

The actual target in the full L317 decomposition is a lower bound for its complete off-diagonal term leaving a positive surplus below (16/5)L^5 and above the O(L^4) analytic remainder. A bound E_I≥−o(L^5) would be a useful contribution, with the other blocks and product terms still unresolved. Equations (1)–(2) remove the stationary-error issue for this particular block, but they transfer its unsigned main form to an exterior reciprocal interval with comparable length, the same polynomial kernel, and the same available estimates. Applying this transform again returns the starting form. This stops direct repeated B-process transformation as the proposed source of a lower bound. It does not rule out cancellation involving the product sector or a genuinely additional estimate for the actual dual phases. The separate endpoint arithmetic margin, low-index signs, all sign/exclusion ranges and RH status are unchanged.

Verification checks the four phase derivatives, the real bounded-variation amplitudes, both signs of the stationary phase, endpoint changes, common-phase cancellation, the polynomial reflection, diagonal substitution, and both quadratic error products in the displayed proof. No numerical sign computation is used. Earlier L175 and L178 concern different heat-route quantities and are historical comparisons, not mathematical inputs to this calculation.

**Mathlib.** Full statement: not checked. Supporting B-process, partial summation, finite polynomial identities and third-derivative test: not checked for Mathlib coverage; no matching theorem is asserted. The supporting stationary theorem is [Vandehey, Theorem 1.1](https://arxiv.org/pdf/1205.0090#page=2), whose phase, variation and endpoint hypotheses were checked directly. The supporting exponential-sum bound is Olivier Robert, [*On van der Corput's k-th derivative test for exponential sums*, derivation preceding Theorem 2](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf), already recorded in the foundations. Neither source is a match for the full ratio-block statement. The [Mathlib reference portal](https://leanprover-community.github.io/mathlib4_docs/) is retained without a coverage claim.
