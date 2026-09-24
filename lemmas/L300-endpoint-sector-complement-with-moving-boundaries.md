# Lemma 300: endpoint sector complement with moving boundaries

**Hypotheses.** Use L299's endpoint parameters h=5, integer n with 2n=r, a→∞, and r=(1/2)log(a/(2π))+(1/4)log(1+25/a²). Retain L288's exact summands, normalization C₀exp(Φ_*), and positive sector D={s+x>r/4, s−x>r/4}. For each j,k≥1, use its translated coordinates p,q and fixed square Q_jk={|p|,|q|≤ε}, ε=1/100. Let K_jk be the exact summand integral over D\Q_jk, and let C_jk be its clipped patch integral as in L299. All integrals use positive area measure.

**Conclusion.** The theta expansion is absolutely integrable termwise on D, and

Σ_(j,k≥1)|K_jk| ≤ C exp(Φ_*) (1+r)² a^(−3/2)
                  =o(exp(Φ_*)/a).                                      (1)

Consequently the whole sector integral satisfies

I_D=C₀exp(Φ_*) π/(2a) [T_r(a)+O(r a^(−1/10)+r exp(−r/32)+(1+r)²a^(−1/2))]. (2)

The additive normalized error is o(1). No positive lower bound for T_r(a), endpoint sector positivity, or global Laguerre sign is asserted.

**Proof.** We recheck the amplitude estimates at h=5; neither L282's logarithmic-h conclusion nor L288's h>5 summation is invoked at the endpoint. Put c=2sqrt(2), b=log(jk)/2, v=(p+q)/sqrt(2), and s=r−b+v. In these coordinates D is the rectangle

p>α_j=(log j−3r/4)/sqrt(2), q>α_k=(log k−3r/4)/sqrt(2).

The absolute Jacobian is one. The normalized exact summand from L288 is

exp(ia log(k/j)) H_jk(p,q) exp(if(p)−if(q)),
f(y)=−(a/2)(exp(cy)−1−cy), H_jk=G_jk E,
G_jk=(jk)^(−1/2)(s/r)^r exp(9v−(5/2)(exp(cp)+exp(cq)−2)),
E=(1−3exp(−cp)/(2V_+))(1−3exp(−cq)/(2V_-)),
V_±=πexp(2r±2iτ), |V_±|=sqrt(a²+25)/2.

On D, s>r/4. Applying log(s/r)≤(s−r)/r gives

0<G_jk≤(jk)^(−1) g(p)g(q),
g(y)=exp(−(5/2)(exp(cy)−1−cy)).                         (3)

Indeed the polynomial contributes at most exp(v−b); combining this with exp(9v) produces exp(10v), the linear term in g(p)g(q), while (jk)^(−1/2)exp(−b)=(jk)^(−1).

Let M(y)=(1+exp(cy))g(y). Uniformly on D, for d,e∈{0,1},

|∂_p^d ∂_q^e H_jk(p,q)|≤C(jk)^(−1) M(p)M(q).           (4)

Here is the derivative check. If S=log G_jk, then

S_p=r/(sqrt(2)s)+9/sqrt(2)−5sqrt(2)exp(cp),
S_q=r/(sqrt(2)s)+9/sqrt(2)−5sqrt(2)exp(cq),
S_pq=−r/(2s²).

Since r/s≤4 and r/s²≤16/r, the first derivatives and mixed derivative of G_jk have the bounds (4) for r≥1. Also

exp(−cp)/|V_+|=1/(πj²exp(2(s+x)))≤exp(−r/2)/(πj²),

and the analogous inequality holds for q,k. Each differentiation of these factors only multiplies them by −c, so E and its first and mixed derivatives are bounded. The product rule proves (4), including d=e=0. This uses the exact summand and does not divide by its possibly vanishing factor E.

For any real α define the finite quantity

B(α)=sup_(y≥α) M(y)+∫_α^∞ M(y)dy.

There is an absolute C such that

B(α)≤C for α≤0, and B(α)≤C exp(−exp(cα)) for α≥0.       (5)

To verify this, put t=exp(cy). Then

M(y)=exp(5/2)(1+t)t^(5/2)exp(−5t/2), dy=dt/(ct).

The supremum and integral are finite on the whole line: the integrand in t has order t^(3/2) near zero and exponential decay at infinity. For t≥t₀≥1, both (1+t)t^(5/2)exp(−5t/2) and (1+t)t^(3/2)exp(−5t/2) are bounded by C exp(−t). The latter integrates to C exp(−t₀), and the former has supremum at most C exp(−t₀). This proves (5).

Write B_j=B(α_j) and J=exp(3r/4). Since exp(cα_j)=(j/J)², (5) implies

Σ_(j≥1) B_j/j ≤ C(1+log J)+C Σ_(j>J) j^(−1)exp(−(j/J)²)
                ≤ C(1+r).                             (6)

For the last inequality, the summand function x^(−1)exp(−(x/J)²) is decreasing. Its tail sum is bounded by its first term plus ∫_J^∞ x^(−1)exp(−(x/J)²)dx. After x=Jt this integral is ∫₁^∞ t^(−1)exp(−t²)dt, independent of J. The head uses the elementary harmonic-sum bound. The moving boundary, rather than a summable infinite harmonic series, is essential here.

For every finite rectangle R=[u₀,u₁]×[v₀,v₁] contained in the translated D, (4) gives the rectangular variation bound

|H_jk(u₁,v₁)|+∫_(u₀)^(u₁)|∂_p H_jk(p,v₁)|dp
 +∫_(v₀)^(v₁)|∂_q H_jk(u₁,q)|dq+∫_R|∂_p∂_q H_jk|
 ≤ C(jk)^(−1) B_j B_k.                                (7)

This holds for every choice of endpoints, including endpoints at ±ε or at the sector boundary by continuity. Moreover (4) for d=e=0 and (6) prove

Σ_jk ∫_D |H_jk| ≤ C(Σ_j B_j/j)² ≤ C(1+r)².             (8)

The coordinate domains in this formula depend on j,k. Their changes of variables each have Jacobian one, so (8) is precisely a bound for the absolute integrals of the original summands on the same sector D. The exact pointwise theta series there and Tonelli/Fubini now justify termwise integration for each a. No limit a→∞ is exchanged with a nonuniform series.

For clarity, the elementary oscillatory bounds used in L282 are uniform over the whole real line: the primitive of exp(±if(y)) on any interval is O(a^(−1/2)), and on intervals entirely in y≤−ε or y≥ε it is O(a^(−1)). To check this directly, f'(y)=−sqrt(2)a(exp(cy)−1) is monotone. Remove |y|≤a^(−1/2), whose length is O(a^(−1/2)); on either side integration by parts bounds the primitive by reciprocal endpoint slopes and the integral of |f''|/|f'|², a difference of reciprocal slopes. These slopes have size at least a constant times sqrt(a), or a constant times a on the fixed tails. This proves both estimates independently of j,k.

Partition D\Q_jk into at most four rectangles, first taking p<−ε and p>ε with all admissible q, then |p|≤ε with q<−ε and q>ε. On each rectangle one primitive has the tail bound and the other has the unrestricted bound. On a finite truncation choose primitives vanishing at the lower endpoints. Two integrations by parts bound the integral by their suprema product times the variation on the left of (7). This identity includes the upper corner and both upper edges; the lower terms vanish by the choice of primitives. Hence every truncated complementary rectangle has integral bounded by

C a^(−3/2)(jk)^(−1)B_j B_k.

Absolute integrability from (8) permits passage to unbounded rectangles. Restore C₀exp(Φ_*), sum the at most four pieces and then the indices using (6). This proves (1). In particular its ratio to exp(Φ_*)/a is O((1+r)²/sqrt(a))→0 because r~(log a)/2.

Finally termwise integrability and the summand-wise partition give I_D=Σ_jk(C_jk+K_jk). L299 evaluates the first sum with its stated normalized error. Applying (1) to the second sum gives (2). This is an additive approximation to the signed exact phase sum, not a relative approximation to a known positive number. ∎

Other sectors at the endpoint, an arithmetic lower bound exceeding the full error, lower indices, and bounded exterior heights remain unresolved. The endpoint is the admissible subsequence 2n=r; no rounding to a neighboring integer index or uniform h-neighborhood is asserted.

**Mathlib.** Full statement: not checked. Supporting logarithmic inequalities, harmonic-sum comparison, exponential tail integration, rectangular integration by parts, and Tonelli/Fubini: not checked. No library match is claimed. L288 supplies the exact summand algebra and normalization; L282 supplies the complementary partition and primitive mechanism, rechecked here at h=5 with moving-domain variation; L299 supplies the clipped stationary sum used in (2). All new tail and summed-variation estimates are proved above.
