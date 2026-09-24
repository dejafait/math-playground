# Lemma 282: summable positive-sector nonstationary complements

**Hypotheses.** Use the shifted integral, exact theta summands T_j, and parameters r,h,τ,Φ_* of L269 and L280. Let a→∞, n≥1 be an integer, and log a≤h≤2 log a. Fix ε=1/100. For every positive integer pair j,k, put

b=log(jk)/2, d=log(k/j)/2,
p=(s−r+b+x−d)/√2, q=(s−r+b−x+d)/√2.

Let D={s+x>r/4, s−x>r/4}. Let Q_jk denote the square |p|,|q|≤ε, whether or not its center belongs to D. Define K_jk as the integral over D\Q_jk, with positive area measure, of

exp(−2aτ)s^(2n)T_j(s+x+iτ)T_k(s−x−iτ)exp(2iax).

**Conclusion.** There is an absolute C such that, uniformly for sufficiently large a,

Σ_(j,k≥1)|K_jk| ≤ C exp(Φ_*) h² a^(−3/2)
                    =o(exp(Φ_*)/a).

The theta series can be integrated termwise on D. The complements here are assigned separately to each summand; this is not an estimate for the full kernel outside a union of squares. Stationary contributions clipped to D and the other argument-sign sectors are not evaluated here.

**Proof.** The exact identities from L269 give n=r(h−9/2), r~(log a)/2. Set c=2√2, v=(p+q)/√2. Then

s=r−b+v,
s+x=r−log j+√2p, s−x=r−log k+√2q.

Consequently D becomes the rectangle of half-lines

p>α_j=(log j−3r/4)/√2, q>α_k=(log k−3r/4)/√2,

and s>r/4 throughout it. The coordinate change has absolute Jacobian one. Direct substitution into the exact summands, as in L280, gives the integrand

(8π²)²exp(Φ_*)exp(ia log(k/j)) H(p,q)exp(if(p)−if(q)),
f(y)=−(a/2)(exp(cy)−1−cy),
H=G E,
G=(jk)^(−1/2)(s/r)^(2n)exp(9v−(h/2)(exp(cp)+exp(cq)−2)),
E=(1−3exp(−cp)/(2V_+))(1−3exp(−cq)/(2V_-)),
V_±=πexp(2r±2iτ).

This formula uses s>0 and remains valid even when r−b≤0; no division by that center is made.

Define ψ(t)=exp(t)−1−t and g_h(y)=exp(−hψ(cy)/2). Since log(s/r)≤(s−r)/r=(v−b)/r, and 2n/r+9=2h,

0<G≤w_jk g_h(p)g_h(q),   w_jk=(jk)^(4−h).                (1)

This is a global estimate on D, not a local Taylor approximation. For h≥1 there are absolute bounds

sup_y (1+exp(cy))g_h(y)≤C,
∫_ℝ (1+exp(cy))g_h(y)dy≤C.                              (2)

Indeed ψ≥0, so it suffices to use h=1. At negative infinity ψ(cy)=−1−cy+o(1), giving integrable exponential decay; at positive infinity its exponential growth dominates the factor 1+exp(cy). Continuity handles the intervening compact interval.

Write S=log G. On D, n/s≤4h and n/s²≤16h/r. Differentiation gives

S_p=√2 n/s+9/√2−√2h exp(cp),
S_q=√2 n/s+9/√2−√2h exp(cq), S_pq=−n/s².

For sufficiently large a, r≥1 and h≥1. From (1) it follows that

|G_p|≤Ch w_jk(1+exp(cp))g_h(p)g_h(q),
|G_q|≤Ch w_jk(1+exp(cq))g_h(p)g_h(q),
|G_pq|≤Ch² w_jk(1+exp(cp))(1+exp(cq))g_h(p)g_h(q).       (3)

The prefactors cause no unbounded error. On D,

|exp(−cp)/V_+|=1/(πj²exp(2(s+x)))≤exp(−r/2)/(πj²),

and the analogous estimate holds for q,k. Each first derivative just multiplies the relevant exponential by −c. Thus E,E_p,E_q,E_pq are bounded by an absolute constant on D. By the product rule, H and its derivatives satisfy the corresponding bounds (1),(3), with a constant C.

For any finite rectangle J×K contained in D, with upper endpoints β,δ, estimates (1)–(3) and (2) imply

|H(β,δ)|+∫_J|H_p(u,δ)|du+∫_K|H_q(β,v)|dv
                  +∫_(J×K)|H_pq(u,v)|du dv ≤Ch²w_jk.    (4)

All constants are independent of j,k and of the rectangle endpoints.

Next the primitive of exp(±if(y)) on every finite real interval is O(a^(−1/2)), globally. On |y|≤a^(−1/2) this follows from length. On either remaining side, f'(y)=−√2a(exp(cy)−1) is monotone and has magnitude at least C^(−1)√a at the near endpoint. Integration by parts bounds the integral by its two reciprocal endpoint slopes plus ∫|f''|/|f'|², the latter being a difference of reciprocal slopes. This proves the bound without any assumption that y remains near zero. On intervals wholly in y≥ε or y≤−ε the same argument gives the stronger O(a^(−1)) bound, since |exp(cy)−1| is bounded below there. The fixed ε is absorbed into the constants.

Partition D\Q_jk into at most four rectangles: its intersections with p<−ε and p>ε (all q in D), then with |p|≤ε and q<−ε or q>ε. Every nonempty rectangle has one tail primitive O(a^(−1)) and the other primitive O(a^(−1/2)). Apply the finite-rectangle fundamental-theorem-of-calculus identity proved in L275, now to the complex amplitude H, and use (4). Each finite truncation of such a rectangle has signed integral at most Ch²w_jk a^(−3/2). Passing to the unbounded rectangles is valid by absolute integrability from (1),(2) and the bounded E. Thus

|K_jk|≤C exp(Φ_*) h²a^(−3/2) w_jk.                       (5)

For t=h−4≥2, integral comparison gives Σ_(m≥1)m^(−t)≤2. Hence Σ_jk w_jk≤4. Summing (5) proves the stated estimate; its ratio to exp(Φ_*)/a is O((log a)²/√a)→0.

Finally (1),(2) also bound the integral of the absolute value of each full summand on D by Cexp(Φ_*)w_jk. Their sum is finite. The pointwise theta expansions in the positive real half-plane and absolute integral summability therefore justify multiplication and termwise integration on D by Tonelli applied to absolute values, followed by Fubini. This does not interchange any uncontrolled asymptotic limits. ∎

L281 treats full stationary squares for a restricted set of centers. To assemble D one must still handle its clipped squares, including centers just outside the restriction. The estimates above do not identify those contributions with L281's full-square integrals. The two mixed-sign argument sectors also remain untreated. No new global Laguerre sign range or RH conclusion follows from this lemma alone; lower indices and bounded exterior heights in L266 are still missing.

**Mathlib.** Full statement: not checked. Supporting logarithmic inequalities, integration by parts, rectangular integration, and absolute-series Fubini: not checked. No library match is claimed. L269 and L280 supply the parameter convention and exact summand algebra; L275 supplies the finite-rectangle identity. The global amplitude envelope, variation bound, and summation estimate are proved here.
