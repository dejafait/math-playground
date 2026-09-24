# Lemma 268: a variance lower bound blocks the quadratic cosine test

**Hypotheses.** Let k be the positive smooth even theta kernel of L048, let W=−log k, and let V_n be the variance in L267, for integers n≥1. Let K(a) be the actual-theta witness cutoff of L266.

**Conclusion.** There is a constant C>0, independent of n and a, such that

V_n ≥ 1/[C(2n+4)].

Consequently, for all sufficiently large |a|, every integer 1≤n≤K(a) satisfies 2a²V_n>1. The sufficient quadratic cosine test in L267 certifies none of those indices at those heights. This does not assert that any actual D_n(Ξ;a) is negative, and does not decide the sharper conjecture V_n of order log n/n.

**Proof.** We first establish the pointwise bound

0<W''(u)≤C(1+uW'(u))  (u∈R).                         (1)

L048 gives smoothness, W''>0, evenness of W, and uW'(u)≥0. For completeness the needed upper tail estimate follows directly from L019's series. Write v=πe^(2u) for u≥0 and factor its first term:

k(u)=4v(2v−3)e^(u/2)e^(−v)(1+r(v)),
r(v)=Σ_(m≥2) [m²(2m²v−3)/(2v−3)] e^(−(m²−1)v).

For v≥π, the rational prefactors and their first two v derivatives are bounded by constants times m⁴. Termwise application of (v d/dv)^j, j≤2, therefore gives

|(v d/dv)^j r(v)|≤C_j v² e^(−3v).

To see summability uniformly, factor out e^(−3v), and bound the remaining polynomial in m by its convergent sum against e^(−(m²−4)π). Factors v^j are at most v² here. This also justifies the differentiated series. Since r≥0, logarithmic differentiation has no small denominator. Differentiating the displayed first term now gives

W'(u)=2v−9/2−6/(2v−3)+O(v²e^(−3v)),
W''(u)=4v+24v/(2v−3)²+O(v²e^(−3v)).

Thus W'(u) is asymptotic to 2v and W''(u) to 4v. In particular W''(u)/(1+uW'(u)) is bounded as u→∞. On bounded intervals its denominator is at least one and its numerator is continuous; evenness handles u<0. This proves (1) for some finite C>0.

Use the probability density on R² proportional to

p_n(s,t)=s^(2n) exp(−W(s+t)−W(s−t)).

Its normalizing integral is positive and finite, and its t second moment is V_n. Set u=s+t and v=s−t (v here is a coordinate, no longer the tail variable above), and put J=W'(u)−W'(v). Differentiation in t gives ∂_t p_n=−Jp_n and ∂_t J=W''(u)+W''(v). Integration by parts yields

E[tJ]=1,
E[J²]=E[W''(u)+W''(v)].                             (2)

These identities can be obtained by integrating ∂_t(tp_n) and ∂_t(Jp_n). There is no division by s and no boundary at s=0. All boundary terms vanish: the established tail formulas bound W', W'' by O(e^(2|u|)), while L019 bounds k by a polynomial in e^|u| times exp(−πe^(2|u|)); the same holds for v. After the invertible linear change of variables, these dominate every polynomial factor in s,t and all differentiated integrands. Cutoff integration followed by dominated convergence is therefore valid.

Integrating the divergence ∂_s(sp_n)+∂_t(tp_n) gives a second exact identity:

E[uW'(u)+vW'(v)]=2n+2.                             (3)

Indeed the polynomial s^(2n) has Euler derivative 2n s^(2n), the two coordinate divergences contribute 2, and
s(W'(u)+W'(v))+t(W'(u)−W'(v))=uW'(u)+vW'(v).
This is a polynomial differentiation identity even on s=0. The same domination justifies this integration.

By (1)–(3), E[J²]≤C(2n+4). Cauchy–Schwarz applied to E[tJ]=1 then gives

1≤E[t²]E[J²]≤V_n C(2n+4),

which proves the lower bound.

It remains to compare it with the actual required cutoff. In L266's formula, the standard Gamma reflection identity and Γ(1+z)=zΓ(z) give

|Γ(1+ix)|²=πx/sinh(πx),

with continuous value one at x=0. Consequently
log A(a)=−π|a|/2+5log|a|+O(1),
K(a)=π|a|/(2log 4)−5log|a|/log 4+O(1).

The fixed constant M in L266 is positive. Thus K(a)=O(|a|) and tends to infinity. Uniformly over 1≤n≤K(a),

2a²V_n≥2a²/[C(2K(a)+4)]→∞.

In particular the left side is eventually greater than one for every required index. This is failure of a sufficient lower estimate for the Fourier integral, not failure of Fourier positivity itself. ∎

**Mathlib.** Full statement: not checked. Supporting integration-by-parts, Cauchy–Schwarz, Gamma reflection, and Gamma recurrence coverage: not checked. No full-statement library match is claimed. The Gamma identities used above are the standard named reflection and functional equations; the variance and tail arguments are proved here.
