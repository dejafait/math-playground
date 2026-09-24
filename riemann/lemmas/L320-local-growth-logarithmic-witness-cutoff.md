# Lemma 320: local completed-zeta growth gives a logarithmic witness cutoff

**Hypotheses.** Let Ξ(z)=ξ(1/2+iz) be the actual completion of L018, and write

H_a(y)=Ξ(a+iy)Ξ(a−iy)=Σ_(n≥0) D_n(Ξ;a)y^(2n),

for real a. Fix real numbers R>η>1/2. Put T=2+|a|, σ_η=1/2+η and

A_η(a)=[(a²+σ_η²)(a²+(σ_η−1)²)/(4π^(σ_η)ζ(σ_η)²)]
                         |Γ(σ_η/2−ia/2)|²,
p=η²/R².

All constants below may depend on the fixed R,η, but not on a, a putative zero's imaginary part, or the value or multiplicity of Ξ at a. Logarithms are natural.

**Conclusion.** A_η(a)>0 and H_a(η)≥A_η(a). There is a constant C_(R,η)≥1 such that

max_(|y|=R)|H_a(y)| / A_η(a) ≤ C_(R,η) T^(R−η).             (1)

Consequently every nonreal zero a+ib of Ξ forces D_n(Ξ;a)<0 for some

1≤n≤K_(R,η)(a),
K_(R,η)(a)=ceil(log(2C_(R,η)T^(R−η)/(1−p))
                                  / (2log(R/η))).         (2)

In particular K_(3,3/2)(a)=(3/(4log 2))log T+O(1). More generally, for every fixed c>1/4 there is a constant B_c>0 such that every such zero forces a negative coefficient at an index

1≤n≤ceil(c log(2+|a|)+B_c).                                (3)

The constants are proved to exist but are not numerically evaluated here. This is a height-only asymptotic reduction, not a new certified cutoff on a bounded height interval, and not a proof of any of the required signs.

**Proof.** We first prove the uniform completed-zeta strip bound

|ξ(σ+it)|≤B_R(2+|t|)^(7/4+R/2) exp(−π|t|/4),
                  1/2−R≤σ≤1/2+R, t∈R.                    (4)

It is necessary to control the strip interior, not just its two vertical sides. Here is an elementary preliminary growth estimate. For Re s>1, absolute summation of the counting integral gives

ζ(s)=s∫_1^∞ floor(x)x^(−s−1)dx
    =s/(s−1)−s∫_1^∞ {x}x^(−s−1)dx.                       (5)

For example, expand floor(x)=Σ_(n≥1)1_(x≥n) and integrate; the sum of the absolute integrals is finite in this half-plane. The last integral in (5) converges locally uniformly for Re s>0, since 0≤{x}<1. Meromorphic continuation and the identity theorem therefore extend (5) there, away from its displayed pole. For 1/2≤Re s≤1/2+R and |Im s|≥1 it gives |ζ(s)|≤C_R(1+|Im s|). No lower bound in the critical strip is being used.

The standard complex Stirling formula, in the positive-real-part vertical strips used here, gives uniformly

|Γ(σ/2+it/2)| ≍_R |t|^(σ/2−1/2) exp(−π|t|/4)

for 1/2≤σ≤1/2+R and sufficiently large |t|. This is the named input recorded in the foundations; see [NIST DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3), with its sector condition. L018's completed-zeta identity and (5) now bound ξ by a fixed power of 2+|t| times exp(−π|t|/4) on that half of the strip. Reflection ξ(s)=ξ(1−s) gives the same type of bound on the other half. Bounded |t| is harmless because ξ is entire. In particular, on the full closed strip, ξ(s)exp(−iπs/4) has at most polynomial growth as |Im s|→∞: for t≥0 the two exponential moduli cancel, and for t<0 their product decays.

On the right boundary σ=1/2+R>1, absolute Dirichlet convergence gives |ζ(σ+it)|≤ζ(σ). The polynomial factor s(s−1)/2 and Stirling therefore give

|ξ(1/2+R+it)|≤C_R(2+|t|)^q exp(−π|t|/4),
q=7/4+R/2.

Reflection gives the same bound on σ=1/2−R. To propagate it through the strip, set b_R=R+1 and define the holomorphic function

G(s)=ξ(s)exp(−iπs/4)(s+b_R)^(−q).

The power uses the analytic logarithm on Re(s+b_R)>0; on the strip that real part is at least 3/2. Since q is real, the modulus of the last factor is |s+b_R|^(−q). Hence G is bounded by some D_R on both vertical sides and has at most polynomial growth throughout the strip.

For ε>0 apply the maximum modulus principle on the rectangle with these vertical sides and Im s=±Y to G(s)exp(εs²). On the vertical sides its modulus is at most D_R exp(εd_R), where d_R=max((1/2−R)²,(1/2+R)²). On the horizontal sides its modulus tends to zero as Y→∞, uniformly in Re s, since polynomial growth is dominated by exp(−εY²). Thus, for any fixed point of the strip,

|G(s)|exp(εRe(s²))≤D_R exp(εd_R).

First let Y→∞ as just justified, then let ε decrease to zero. This proves |G(s)|≤D_R. For t≥0, multiply back and use |s+b_R|≤C_R(2+t) to obtain (4). For t<0 use ξ(conj s)=conj ξ(s), from L018. This proves the claimed symmetric exponential decay throughout the strip without a zero-free or RH assumption.

Write y=u+iv on |y|=R. The two factors in H_a are exactly

ξ(1/2−u+i(a−v)),       ξ(1/2+u+i(a+v)).

Both real parts lie in the strip of (4). Also

|a−v|+|a+v|≥2|a|,
2+|a±v|≤(1+R/2)(2+|a|).

Their product therefore satisfies, for every real a,

max_(|y|=R)|H_a(y)|≤E_R T^(7/2+R) exp(−π|a|/2).          (6)

For |a|≥R the first of these inequalities is equality. Thus the circle estimate retains the common gamma decay even though y ranges over a complex circle. The constants absorb the bounded height shifts, and no assumption that Ξ(a) is nonzero occurs.

At the real anchor y=η, L018's reality and reflection give

H_a(η)=|Ξ(a+iη)|²=|ξ(σ_η−ia)|².

By L001's absolutely convergent reciprocal series, |ζ(σ_η−ia)|≥1/ζ(σ_η), because σ_η>1. Substituting the completed-zeta formula gives H_a(η)≥A_η(a). All factors defining A_η are strictly positive: σ_η>1, both real quadratic factors are positive, and Γ has no zero or pole in this half-plane. Stirling also gives

A_η(a) ≍_η |a|^(7/2+η) exp(−π|a|/2)

as |a|→∞. The quotient by T^(7/2+η)exp(−π|a|/2) is positive and continuous on each bounded interval, and has a positive limit at infinity. Consequently some e_η>0 satisfies

A_η(a)≥e_η T^(7/2+η) exp(−π|a|/2)                       (7)

for every real a. Dividing (6) by (7), and increasing E_R/e_η to at least one, proves (1).

L018 places every nonreal zero within 0<|b|<1/2. Conjugation allows b>0, so b<η<R. Use the general witness comparison in L266 with anchor s=η, lower bound A=A_η(a), and circle majorant

M=C_(R,η)T^(R−η)A_η(a).

This is a valid majorant by (1). All hypotheses of that comparison hold, including when Ξ(a)=0, and its formula is exactly (2). Alternatively, its finite-sum proof needs only p^K≤(1−p)/(2C_(R,η)T^(R−η)), which follows directly from (2). Thus no central-value normalization has been reintroduced.

The coefficient of log T in (2) is

c_(R,η)=(R−η)/(2log(R/η)).                                (8)

At R=3, η=3/2 this is 3/(4log 2). For comparison, L266's original height-independent majorant and the same anchor have cutoff

K_old(a)=π|a|/(2log 4)−5log|a|/log 4+O(1)

as |a|→∞, directly from its formula and the anchor asymptotic above. Thus (2) lowers its order of growth.

For a given c>1/4, choose 1/2<η<2c, then take R>η sufficiently close to η. Since (R−η)/log(R/η)→η as R decreases to η, this makes c_(R,η)<c. The constant term in (2), together with any desired positive enlargement, is B_c in (3). The ceiling preserves the inequality. This choice fixes R and η before allowing a to vary; no uniformity as they approach 1/2 is asserted.

Finally log(R/η)<(R−η)/η implies c_(R,η)>η/2>1/4, and successive fixed choices approaching 1/2 make its infimum 1/4. This is the limit of this fixed-radius bound, not an impossibility result for other witness arguments. ∎

The required sign target is now the entire initial segment in (3). For each fixed c>1/4, nonnegativity at every one of those indices at a would exclude a nonreal zero with that real center. L296's established signs on bands c₀log|a|≤n≤c₁log|a| with 1/4<c₀<c₁ do not supply that initial segment: indices near or below (log|a|)/4, including fixed indices, remain uncovered. This comparison uses L296 only to identify the gap, not as an input to the witness proof. The endpoint arithmetic margin and all bounded exterior gaps also remain unresolved. No sign or exclusion interval is extended by this lemma alone, and there is no RH candidate.

**Mathlib.** Full statement: not checked. Coverage of the strip maximum-modulus argument, gamma estimates and optimized cutoff is not checked; no match is claimed. The supporting reciprocal identity and its summability input are recorded as present in L001, whose library sources were not rechecked here: [`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius) and [`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff). These support the anchor only, not the full statement. The direct DLMF Stirling reference above was checked for its complex sector; it is a classical supporting input, not a Mathlib coverage claim. Euler summation in the needed half-plane, the strip interpolation and the coefficient optimization are proved above.
