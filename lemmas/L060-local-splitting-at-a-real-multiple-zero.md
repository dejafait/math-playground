# Lemma 60: local splitting at a real multiple zero

**Hypotheses.** Let F(λ,z) be the exact heat-deformed theta transform of Lemma 58. Let λ₀,x₀ be real and suppose z↦F(λ₀,z) has a zero of exact finite multiplicity m≥3 at x₀. Write A=∂_z^m F(λ₀,x₀)≠0.

**Conclusion.** Define the monic polynomial

P_m(v)=Σ_{j=0}^{⌊m/2⌋} m!(-1)^j v^(m-2j)/(j!(m-2j)!).

Its m roots α₁<⋯<α_m are real and simple, symmetric about zero; zero is a root exactly when m is odd. There are r,ε,C>0 and holomorphic functions w_k(s) for |s|<ε such that the zeros of F(λ₀+s²,z) in |z-x₀|<r, counted with multiplicity, are exactly x₀+w_k(s), 1≤k≤m. Uniformly in this complex disc,

|w_k(s)-α_k s|≤C|s|².

For real 0<t<ε² all m nearby zeros are simple and real, with locations x₀+α_k sqrt(t)+O(t). For -ε²<t<0 they are simple with locations x₀+iα_k sqrt(|t|)+O(|t|). If m is even, all m are nonreal, in m/2 conjugate pairs. If m is odd, exactly one is real and the remaining m-1 form (m-1)/2 nonreal conjugate pairs. The real central zero for odd m is analytic in t through zero. Every neighborhood and bound is local to the assumed multiple zero.

## Proof

### The leading polynomial and its roots

Define P_n by the same finite formula for every n≥0. Coefficient comparison gives P_0=1, P_1=v and, for n≥1,

P_(n+1)(v)=vP_n(v)-2nP_(n-1)(v).

For completeness, at the monomial v^(n+1-2j) the two contributions, after taking out n!(-1)^j/[j!(n+1-2j)!], have factors n+1-2j and 2j. Their sum is n+1, as required; endpoint terms that are absent contribute zero. Thus the recurrence follows at all coefficients.

Inductively P_n has n simple real roots and the roots of P_(n-1) strictly interlace them. The base n=1 has one simple root, with the interlacing condition empty. Suppose the assertion holds at n and write its roots a₁<⋯<a_n. Then

P_(n+1)(a_k)=-2nP_(n-1)(a_k)≠0.

The signs on adjacent a_k alternate because P_(n-1) has exactly one simple root between them. Hence P_(n+1) has a root in every interior interval. Since P_(n-1) is monic and its roots lie inside (a₁,a_n), its sign at a_n is positive and at a₁ is (-1)^(n-1). The sign of P_(n+1) at a_n is negative, opposite to its sign near +∞; at a₁ its sign is (-1)^n, opposite to its sign near -∞, which is (-1)^(n+1). There is therefore also one root in each exterior interval. These n+1 distinct real roots exhaust its degree and are simple, proving strict interlacing for the next induction. This argument also works for n=1 with P_0=1.

The coefficient formula gives P_n(-v)=(-1)^n P_n(v). For even n its constant term is n!(-1)^(n/2)/(n/2)!≠0; for odd n parity gives a root at zero. The simplicity and symmetry assertions follow. This proves the needed root properties directly, without invoking any external facts about Hermite polynomials.

### Convergent rescaling and all local branches

We extend the weighted rescaling and local counting argument of Lemma 59. Lemma 58 gives joint holomorphy, the heat equation F_λ=-F_zz, and reality under conjugation. Commuting holomorphic derivatives and iterating that equation gives

∂_λ^j ∂_z^k F(λ₀,x₀)=(-1)^j ∂_z^(2j+k)F(λ₀,x₀).

In the convergent Taylor series in t=λ-λ₀ and w=z-x₀, all monomials t^j w^k of weight 2j+k<m therefore vanish. The terms of weight m sum to

A Σ_{2j+k=m} (-1)^j t^j w^k/(j!k!).

Substitute t=s²,w=sv. For v in any fixed bounded disc containing all α_k, and |s| sufficiently small, the substituted series converges normally. It is divisible by s^m as a holomorphic function: explicitly, the Taylor series after substitution has no powers of s below m, and division leaves a normally convergent series on smaller discs, by Cauchy estimates in s uniformly on smaller v discs. Consequently

G(s,v)=s^(-m)F(λ₀+s²,x₀+sv)=A P_m(v)/m!+s H(s,v)

extends holomorphically to s=0 with H holomorphic there. At each α_k its v derivative at s=0 is A P_m'(α_k)/m!≠0. The holomorphic implicit function theorem supplies v_k(s) with v_k(0)=α_k and G(s,v_k(s))=0. Set w_k(s)=s v_k(s). The removable quotients (w_k(s)-α_k s)/s² are holomorphic and bounded on a smaller closed s disc. Taking the maximum over the finitely many k yields C.

Choose r so F(λ₀,z) has only its multiplicity-m zero x₀ in the closed r disc and no boundary zero. The positive minimum of its boundary modulus and uniform convergence F(λ₀+s²,z)→F(λ₀,z) on that circle allow Rouché's theorem for small |s|. There are exactly m zeros with multiplicity inside. Shrink ε to put every constructed branch inside, and to make the v_k(s) pairwise distinct, using their distinct initial values. For s≠0 the m zeros w_k(s) are distinct, so the count proves simplicity and completeness. At s=0 they represent x₀ m times.

### Reality on the two sides, including the central branch

The Taylor coefficients are real. Thus G respects simultaneous conjugation, and uniqueness of each implicit branch through the real α_k gives v_k(conjugate(s))=conjugate(v_k(s)). In particular all w_k(s) are real for real s. Choosing s=sqrt(t) proves the positive-t assertion.

For negative t choose s=iρ with ρ=sqrt(|t|)>0. When α_k≠0, the uniform bound gives

Im w_k(iρ)=α_k ρ+O(ρ²),

which is nonzero for sufficiently small ρ, uniformly over the finitely many nonzero α_k. It remains to treat the single α_k=0 when m is odd; an O(ρ²) bound alone does not prove its reality.

From the definition of G and holomorphic extension,

G(-s,-v)=(-1)^m G(s,v).

Let v_c denote the branch with v_c(0)=0. The function -v_c(-s) is another root branch of G(s,·) through zero. Implicit-function uniqueness forces v_c(s)=-v_c(-s). Therefore w_c(s)=s v_c(s) is even and has real Taylor coefficients. Its convergent series contains only even powers, so w_c(s)=h(s²) for a holomorphic h near zero with real coefficients and h(0)=0. In particular w_c(iρ)=h(-ρ²) is real. This proves exactly one real zero on the negative side for odd m and none for even m. Conjugation preserves the original function at real λ and the r disc; the remaining nonreal simple zeros are consequently paired by conjugation. ∎

## Scope and formalization obligations

This conditional local theorem does not assert that a multiple zero exists for the exact theta family. It resolves every assumed finite real multiplicity into simple real zeros just above its parameter, and into nonreal pairs (with one real survivor for odd multiplicity) just below. It gives no exclusion of such parameters above zero, no uniform control over infinitely many zeros, and no global reality assertion at λ=0. The all-degree gap in the main argument remains open.

Formalization would require the polynomial coefficient recurrence and interlacing induction with endpoint signs, iteration of the heat equation for mixed derivatives, normally convergent weighted rescaling, the finitely many holomorphic implicit branches with uniform remainder, the Rouché multiplicity count, and the parity/uniqueness proof for the central branch. These are analytic and exact algebraic arguments; no numerical certificate is needed. Lemma 58 supplies the analytic family, and the rescaling and counting method of Lemma 59 is extended with the full general-multiplicity justification above.
