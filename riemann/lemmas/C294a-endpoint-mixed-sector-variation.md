# Corollary 294a: endpoint mixed-sector variation

**Hypotheses.** Use the mixed-sector coordinates and exact summands T_jk of L292, now at h=5, with integer n, r=2n→∞, and 2πexp(2r+2iτ)=5+ia. In particular a→∞, 0<τ<π/4 and r~(log a)/2. Retain L294's normalization Φ_* and C₀=(8π²)². All area measures are positive.

**Conclusion.** For γ=log 2−1/2>0,

(1/2) Σ_(j,k≥1) |∫₀^∞∫₀^∞ T_jk(u,v) du dv|
 ≤ C exp(Φ_*) exp(−γr)/a = o(exp(Φ_*)/a).

The exact theta series is absolutely integrable termwise on this sector for each parameter value. The opposite mixed sector satisfies the same bound. No endpoint Laguerre positivity or arithmetic lower bound is asserted.

**Proof.** This extends the whole-sector portion of L294, not its core-subtraction conclusion. Its stated h>5 hypothesis cannot simply be invoked at equality, so we check the estimates at equality. L292's summand algebra uses only evenness, positive real arguments and cos(2τ)>0; all remain valid at h=5. Put

q(u)=(5/2)exp(2(u−r)),
E_j(u)=1−3/(2πj²exp(2u+2iτ)),
B_j(u)=j⁴exp(9u/2−q(u)j²)E_j(u),
φ_j(u)=au−πsin(2τ)j²exp(2u),
Ā_jk(u,v)=exp(−9r+5)((u−v)/(2r))^r B_j(u)B_k(v).

Then exactly, with L294's normalization,

T_jk=C₀exp(Φ_*)exp(9iτ)Ā_jk exp(iφ_j(u)+iφ_k(v)).       (1)

Since u≥0, E_j and E'_j are uniformly bounded. Thus

|B_j(u)|+|B'_j(u)|
 ≤ C j⁴exp(9u/2)(1+q(u)j²)exp(−q(u)j²).

The Gaussian moment estimate proved in L294,

Σ_j j⁴(1+qj²)exp(−qj²)≤Cq^(−5/2)exp(−q/2),

holds for every q>0 with an absolute constant. Consequently

Σ_j (|B_j(u)|+|B'_j(u)|)≤C exp(5r)W(u),
W(u)=exp(−u/2)exp(−(5/4)exp(2(u−r))).                  (2)

For ℓ=0,1,2, polynomial differentiation and maximization give

|[d/dw]^ℓ(w/(2r))^r|≤C2^(−r)exp(−r)exp(|w|).          (3)

Indeed for t=|w|/r, divide the derivative by the right side. The ratio is (r)_ℓ/r^ℓ times t^(r−ℓ)exp(r−rt), maximized at t=1−ℓ/r. Its value is bounded by exp(ℓ); at w=0 continuity gives the same bound for r>2. No division by w occurs. Applying (2)–(3) and the product rule yields, for b,d∈{0,1},

Σ_jk |∂_u^b ∂_v^d Ā_jk|
 ≤ C2^(−r)exp(|u−v|)W(u)W(v).                         (4)

The factor exp(r) from exp(−9r+5)exp(10r) cancels exp(−r) in (3). Now exp(|u−v|)≤exp(u−v)+exp(v−u), and

∫₀^∞ exp(u)W(u)du
 = exp(r/2)∫_(−r)^∞ exp(t/2−(5/4)exp(2t))dt
 ≤ Cexp(r/2),
∫₀^∞ exp(−u)W(u)du ≤ ∫₀^∞ exp(−3u/2)du=2/3.

The first t-integral converges on the whole real line, with exponential decay at negative infinity and superexponential decay at positive infinity. Integrating (4) therefore proves

Σ_jk ∫₀^∞∫₀^∞ |∂_u^b ∂_v^d Ā_jk| du dv
 ≤ C exp(−(log 2−1/2)r).                              (5)

This is the actual endpoint summability estimate. For b=d=0, Tonelli and (1) justify termwise integration of the pointwise absolutely convergent theta expansion for each a. No uniform interchange of the a-limit with a series is required.

For completeness, translation y=u−r+log j changes φ_j, up to a constant, into a(y−exp(2y)/2). Every interval primitive of its exponential is O(a^(−1/2)), uniformly in its translated endpoints: remove |y|≤a^(−1/2), estimate this interval by length, and integrate by parts on either side. There the monotone derivative a(1−exp(2y)) has magnitude at least c sqrt(a); the integral of the absolute second derivative divided by the squared first derivative is a difference of reciprocal slopes. This gives the asserted bound including intervals crossing the stationary point.

Choose U_j(u)=∫₀^u exp(iφ_j(t))dt, so U_j(0)=0 and |U_j|≤C/sqrt(a). Two integrations by parts give

∫∫ Ā_jk exp(iφ_j+iφ_k)=∫∫ (∂_u∂_v Ā_jk)U_jU_k.

To justify this identity, first use finite rectangles, then pass their endpoints to infinity. Lower-edge terms vanish by U_j(0)=0. For fixed j,k the amplitude and its first derivatives are polynomials times superexponentially decaying factors in either variable, so upper edges and corners vanish. The derivatives are integrable by (5); this also justifies the limiting double integral. Taking moduli and summing (5) gives Cexp(−γr)/a. Restore (1) and the coordinate Jacobian 1/2. Reflection x↦−x conjugates the original shifted integrand and preserves positive area, proving the opposite-sector assertion. Finally log 2=∫₁² dt/t>1/2, so γ>0 and the required normalized error tends to zero. ∎

The endpoint is the admissible sequence r=2n; no neighboring-index uniformity is asserted. Together with L300 and L301 this removes the listed endpoint sector omissions, but a whole-plane normalization and a positive arithmetic lower bound exceeding its additive error still need assessment. Smaller indices and bounded exterior heights remain unresolved.

**Mathlib.** Full statement: not checked. Supporting Gaussian moment sums, polynomial derivative bounds, Tonelli/Fubini and integration by parts: not checked. No library match is claimed. L294 supplies the normalized amplitude and Gaussian-moment/primitive method, whose endpoint constants and boundaries are checked here; L292 supplies the exact mixed-sector expansion and reflection geometry. No core estimate from L293 is needed.
