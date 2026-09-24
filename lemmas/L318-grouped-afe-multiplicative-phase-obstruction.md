# Lemma 318: multiplicative-phase obstruction after complete AFE regrouping

**Hypotheses.** Use L317's real height a, X=sqrt(a/(2π)), N=floor(X), L=log X, θ'(a)=L+O(a^(−2)), λ_n=θ'(a)−log n and fixed κ>0. Put

P_κ(v)=v^4−κv^2,
Q(U)=U'^2−UU'',       T(U)=UU''''−4U'U'''+3U''^2.

Let η be any complex number of modulus one, and let ω be a completely multiplicative function on the positive integers with |ω(n)|=1. Define the real finite sum and its quadratic form

W_(a,η,ω)(x)=2Re[η Σ_(n≤N)n^(−1/2)ω(n)exp(iλ_n x)],
F_a(η,ω)=T(W)(0)−κQ(W)(0).

The height, cutoff, coefficients and frequencies are fixed when differentiating in x. The actual L317 sum is obtained from η=exp(iθ(a)), ω(n)=n^(−ia). The other phase assignments below are tests of a uniform representation, not replacements justified for actual Z.

**Conclusion.** All equal reduced-ratio and product phases group exactly as follows:

A_a(p,q)=(pq)^(−1/2) Σ_(1≤d≤N/max(p,q)) d^(−1)
                    P_κ(2θ'(a)−log(pq)−2log d),
B_a(k)=k^(−1/2) Σ_(nm=k, 1≤n,m≤N) P_κ(log(m/n)),

F_a(η,ω)=Σ_((p,q)=1, p,q≤N) A_a(p,q)ω(p)conjugate(ω(q))
                +Re[η^2 Σ_(k≤N^2) B_a(k)ω(k)].                  (1)

The first sum is real. Its diagonal A_a(1,1) is precisely L317's D_κ=(16/5)L^5+O_κ(L^4).

For every sufficiently large a and every η, there is a real τ_a with

|τ_a−1/3|≤π/L,       ηX^(iτ_a)=1,       ω_a(n)=n^(iτ_a),       (2)

for which

Q(W_(a,η,ω_a))(0)=q_0X+O(X/L+sqrt(X)(1+L^2)),
F_a(η,ω_a)=−c_κX+O_κ(X/L+sqrt(X)(1+L^4)),                  (3)
q_0=466560/28561>0,
c_κ=1390722048/4826809+κ·466560/28561>0.

The constants are uniform in η. Thus these phase assignments have Q(W)>0 and F_a≤−c_κX/2 for all sufficiently large a, including when η is held at its actual value exp(iθ(a)).

Consequently any function G_a(η,ω) that is nonnegative for every multiplicative unit phase ω must, for each fixed η, have

sup_ω |F_a(η,ω)−G_a(η,ω)|≥c_κX/2.                         (4)

The conclusion still holds if the supremum and nonnegativity requirement are restricted to assignments with Q(W)>0. In particular no nonnegative quadratic or square-sum representation uniform over these phases can have error o(L^5). No negative value at the actual phase assignment n^(−ia) is asserted, and no established actual-theta sign or zero-exclusion range changes.

**Proof.** L317's finite polarization identity applies to arbitrary phases. With b_n=ηω(n), its real form is

F_a(η,ω)=Σ_(n,m≤N)(nm)^(−1/2) {
 P_κ(λ_n+λ_m)Re[b_n conjugate(b_m)]
 +P_κ(λ_n−λ_m)Re[b_n b_m]}.                               (5)

Both sums here are ordered. The terms with n=m in the second vanish because P_κ(0)=0; the first diagonal is Σ_n P_κ(2λ_n)/n. The signs and factors in (5) also follow by using the modes with frequencies ±λ_n in the symmetric kernel P_κ(ν_b−ν_c)/2.

In the first sum put n=dp and m=dq with d=gcd(n,m), so (p,q)=1. Complete multiplicativity and unit modulus give

ω(n)conjugate(ω(m))=ω(p)conjugate(ω(q)),
(nm)^(−1/2)=1/(d sqrt(pq)),
λ_n+λ_m=2θ'(a)−log(pq)−2log d.

The allowed d are exactly those in A_a(p,q). Since A_a(p,q)=A_a(q,p), the grouped sum is real and its real-part symbol can be omitted. The only diagonal coprime pair is (1,1). In the second sum put k=nm. Then ω(n)ω(m)=ω(k), the amplitude is 1/sqrt(k), and λ_n−λ_m=log(m/n). This proves (1), including all multiplicities, square products and endpoint terms. Every sum is finite; no convergence argument is used in this regrouping.

We next test the complete form at fixed amplitudes while respecting every multiplicative phase relation. Write η=exp(iψ), with any real argument ψ. Choose an integer h nearest to (ψ+L/3)/(2π) and set

τ_a=(2πh−ψ)/L.

This proves (2). In particular τ_a lies in a fixed compact neighborhood of 1/3 for all large a, independently of η. The common phase is now exactly canceled by X^(iτ_a); it has not been changed from its prescribed value.

Put δ=θ'(a)−L=O(a^(−2)). For 0≤j≤4 and τ in that compact neighborhood, define

h_j(t)=t^(−1/2)exp(iτ log(t/X))(log(X/t)+δ)^j,       0<t≤X.

We claim the uniform sum-integral comparison

Σ_(n≤N)h_j(n)=∫_0^X h_j(t)dt+O_j(1+L^j).                 (6)

Here and below L is positive and large. On 1≤t≤X, differentiation gives

|h_j'(t)|≤C_j t^(−3/2)(1+log(X/t))^j,
∫_1^X |h_j'(t)|dt≤C_j(1+L^j).                            (7)

For j=0 the derivative of the polynomial factor is simply absent. The bounds use |δ|≤1 and bounded |τ|. Compare h_j(n), for 2≤n≤N, with its integral on [n−1,n]; the sum of these discrepancies is at most the variation integral in (7). The remaining value at n=1 is O_j(1+L^j). On (0,1), substitute t=exp(−u); the resulting bound is an integral of exp(−u/2)(1+L+u)^j, hence O_j(1+L^j). Finally ∫_N^X |h_j(t)|dt=O_j(1) since X−N<1 and X≥2. This proves (6), including integer and noninteger cutoffs.

In its integral substitute t=X exp(−u). For c=1/2+iτ, the base integral is ∫_0^∞exp(−cu)du=1/c. Repeated integration by parts then gives ∫_0^∞u^m exp(−cu)du=m!/c^(m+1): the terms at infinity vanish since Re c>0, and at zero they vanish for m≥1. Consequently

∫_0^X h_j(t)dt
 =sqrt(X)∫_0^∞ exp(−(1/2+iτ)u)(u+δ)^jdu
 =sqrt(X)[j!/(1/2+iτ)^(j+1)+O_j(|δ|)].                   (8)

The error is uniform for τ in the indicated compact set, by expanding the integer power and bounding its finitely many exponential moments. Its size sqrt(X)|δ| is O(a^(−7/4)), and can be absorbed in (6).

For the phase assignment (2), differentiation of the finite sum for W therefore yields

W^(j)(0)=sqrt(X)v_j(τ_a)+O_j(1+L^j),
v_j(τ)=2Re[i^j j!/(1/2+iτ)^(j+1)],       0≤j≤4.          (9)

These are exactly the derivatives at zero of

V_τ(x)=2Re[1/(1/2+i(τ−x))]
      =1/(1/4+(τ−x)^2).                                  (10)

The functions v_j(τ) and their first derivatives in τ are bounded on the compact set. Products in Q and T computed from (9) have, respectively, errors O(sqrt(X)(1+L^2)) and O(sqrt(X)(1+L^4)); the products of two error terms also fit these bounds. Moreover |τ_a−1/3|≤π/L changes either limiting quadratic form by O(1/L).

For completeness the exact five derivatives of (10) at τ=1/3 are

(v_0,v_1,v_2,v_3,v_4)
 =(36/13, 864/169, 7776/2197, −1866240/28561,
                                          −222829056/371293).

They can be found either from (9) or by multiplying the Taylor series of V by 13/36−(2/3)x+x^2 and equating the result to one. Substituting them into Q and T gives

Q(V_(1/3))(0)=466560/28561,
T(V_(1/3))(0)=−1390722048/4826809.                         (11)

Equations (9)–(11) prove (3). Both remainders in (3) are o(X), since L→∞ and L^4/sqrt(X)→0. The signs and the stated eventual negative bound follow. Evaluating any nonnegative G at this particular ω_a gives (4), also under the restriction Q(W)>0. ∎

The achieved obstruction is of order X, hence of order sqrt(a); the sought uniform representation error was o(L^5), and X/L^5 tends to infinity. This tests the entire diagonal-plus-cross-term sum after every product and reduced-ratio collision has been retained. It is stronger than an arbitrary-vector minor test or an arbitrary local analytic germ: the amplitudes remain n^(−1/2), and the phases are completely multiplicative, even with the actual common phase fixed. Nevertheless the test twist has τ_a near 1/3, whereas the actual twist is −a at this same cutoff. Estimates using that actual relation remain untested; multiplicativity alone cannot supply the claimed uniform representation. Nothing here shows that the obstructing assignment occurs for actual Z. No negative Laguerre coefficient, off-line zero, or RH candidate follows.

The command `python3 scripts/laguerre/check_grouped_afe_obstruction.py` checks the finite regrouping coefficients and computes (11) by two independent exact rational jet constructions. It checks finite algebra, not the actual-zeta sign; the uniform asymptotic and error comparisons are proved above.

**Mathlib.** Full statement: not checked. Supporting finite multiplicative regrouping, sum-integral comparison, integer exponential moments and rational Taylor identities: not checked for Mathlib coverage; no matching theorem is asserted. The proof is supplied here. L317 supplies the supporting frozen-frequency reduction and theta-phase estimate, not a match for this obstruction. The [Mathlib reference portal](https://leanprover-community.github.io/mathlib4_docs/) is retained without a coverage claim.
