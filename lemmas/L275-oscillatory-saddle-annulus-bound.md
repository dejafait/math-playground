# Lemma 275: oscillatory control of the unrotated saddle annulus

**Hypotheses.** Use the actual theta kernel and saddle quantities of L269, and the real coordinates p=(s−r+x)/√2, q=(s−r−x)/√2 of L272 on t=x+iτ. Let a→∞ with h~√a(log a)². Fix 0<κ<1/4 and M>0, and put R=κh/a and ε=√(M log a/h). Let E be the real square [−ε,ε]² with [−R,R]² removed. Integrals below use positive real area measure after the orthogonal coordinate change.

**Conclusion.** The actual shifted theta integral over E is o(exp(Φ_*)/a). More explicitly its modulus is at most

C exp(Φ_*) [1/(a^(3/2)R) + (a^(−1)+exp(−c h))/h].

Thus its relative error at the saddle scale is O((log a)^(−2)+h^(−1)+(a/h)exp(−c h)). This is an annular estimate, not by itself a global positivity theorem.

**Proof.** We retain the exact positive-tail model phase of L269 rather than Taylor expanding its imaginary part. Write c₀=2√2 and v=(p+q)/√2. Its normalized exponential on the real square is exactly

exp(Φ−Φ_*)=A(p,q) exp(i f(p)−i f(q)),
f(y)=−(a/2)(exp(c₀y)−1−c₀y),
A=exp(S),
S=2n log(1+v/r)+9v−(h/2)(exp(c₀p)+exp(c₀q)−2).

The imaginary identity follows from 2πexp(2r)sin(2τ)=a; the real identity uses the corresponding cosine identity with h. The saddle relation h=n/r+9/2 gives S(0,0)=0 and ∇S(0,0)=0. Since ε→0 and r→∞, direct differentiation on this square gives

−C h I ≤ Hess S ≤ −c h I,
|∇S|≤C h(|p|+|q|),   |S_pq|≤C h.

Indeed the exponential contribution to −Hess S is diagonal with entries 4h exp(c₀p), 4h exp(c₀q); the logarithmic contribution is the positive semidefinite matrix with every entry n/(r+v)². Its norm is O(n/r²)=O(h/r). Consequently

0<A≤exp(−c h(p²+q²)),
|A_p|+|A_q|≤C h(|p|+|q|)exp(−c h(p²+q²)),
|A_pq|≤C[h+h²(p²+q²)]exp(−c h(p²+q²)).                 (1)

In particular, uniformly for any rectangle J×K contained in the square, with upper endpoints β,δ, the quantity

|A(β,δ)| + ∫_J |A_p(u,δ)|du + ∫_K |A_q(β,v)|dv
             + ∫_(J×K)|A_pq(u,v)|du dv

is bounded by an absolute constant. For the line integrals use √h|δ|exp(−c hδ²)≤C (and likewise β); for the double integral scale both variables by √h in (1).

Here is the elementary oscillatory estimate needed with this bound. On every subinterval of [−ε,ε],

|∫ exp(±if(y))dy|≤C/√a.                                  (2)

On every subinterval wholly in [R,ε] or [−ε,−R], the stronger bound is

|∫ exp(±if(y))dy|≤C/(aR).                                (3)

To prove these without an unstated stationary-phase theorem, note f''(y)=−4a exp(c₀y), so |f''| is comparable to a and f' is monotone with its only zero at zero. Outside |y|≤a^(−1/2), integration by parts with (exp(if))'=if'exp(if) gives a bound C/min|f'|: the boundary terms have this bound, and ∫|f''|/|f'|² is a difference of reciprocal endpoint slopes. The middle interval has length at most 2/√a. This proves (2); |f'(y)|≥c aR on either tail proves (3) by the same calculation. Both bounds hold on all subintervals and for either sign.

For completeness, bounded primitives multiply against A as follows. The fundamental theorem of calculus expresses A(p,q) on J×K as

A(β,δ) − ∫_p^β A_p(u,δ)du − ∫_q^δ A_q(β,v)dv
                 + ∫_p^β ∫_q^δ A_pq(u,v)dv du.

Insert this identity in the oscillatory double integral and use Fubini on the finite rectangles. Each resulting oscillatory factor is a primitive on a subinterval. Thus the integral is bounded by the product of the two uniform primitive bounds times the bounded quantity following (1). No oscillatory derivative estimate for the theta error is needed.

Partition E, up to null boundaries, into four rectangles: the two p tails with all q, and the two q tails with |p|≤R. On each rectangle one factor satisfies (3) and the other (2). The exact model integral over E is therefore O(1/(a^(3/2)R)).

Finally, on the entire outer square both kernel arguments have real part r+O(ε), and v_±=πexp(2(s±t)) satisfy |v_±| comparable to a and Re v_± comparable to h. The exact series estimate in L269 gives the complex relative model error O(a^(−1)+exp(−c h)), uniformly. By (1), the model modulus integral on the square is O(1/h). Multiplying these bounds controls the actual-minus-model integral, including over E, by the second term in the conclusion. The fixed normalization (8π²)² is absorbed in C. Since √a R~κ(log a)² and h→∞, both errors are little-o of 1/a. ∎

This retains the cancellation lost by the absolute envelope at the inner boundary, where hR²→0. L274 controls the complementary local connector issue at this same scale. Assembly with the inner patch and the far exterior still needs to be written and checked before claiming a new sign range; uniformity over an interval of indices is not asserted here. The full L266 witness target also includes smaller indices and bounded heights.

**Mathlib.** Full statement: not checked. Supporting integration by parts, finite-rectangle Fubini, Gaussian bounds, and the fundamental theorem of calculus: not checked. No library match is claimed. The oscillatory primitive and amplitude estimates are proved here. L269 supplies the exact model phase and theta-series estimate; L272 supplies the coordinate convention.
