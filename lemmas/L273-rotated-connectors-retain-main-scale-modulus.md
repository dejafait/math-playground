# Lemma 273: rotated connectors retain main-scale absolute mass

**Hypotheses.** Use the actual theta kernel, positive saddle, phase Φ_*, and quantities r,h,a,n of L269 and the coordinates p,q, angle θ, and d=n/r² of L272. Let a→∞ along parameters with h~√a(log a)² and 1≤n≤Ca. Fix 0<κ<1/4 and put R=κh/a. Rotate the square simultaneously by

p=e^(−iα)y, q=e^(iα)z, 0≤α≤θ, |y|,|z|≤R,

where u=(p+q)/√2, x=(p−q)/√2, s=r+u, t=x+iτ. A connecting face means one of y=±R or z=±R, parametrized by α and the remaining real coordinate. Integrate the absolute value of the pullback of the actual holomorphic two-form

ω=s^(2n)k(s+t)k(s−t)e^(2iat) ds∧dt.

**Conclusion.** Each of the four connecting faces has absolute integral comparable to exp(Φ_*)/a, with positive constants independent of a. In particular none is o(exp(Φ_*)/a). This is an obstruction to discarding these faces by absolute-value estimates, not a lower bound on their signed integrals or their signed sum.

**Proof.** The parameter identities of L272 give r~(log a)/2, d=O(h/r), θ→π/4. At this radius,

R→0, aR²~κ²(log a)^4→∞,
hR²~κ²(log a)^6/√a→0, aR³~κ³(log a)^6/√a→0.

The entire homotopy lies strictly inside the two theta strips: its maximum imaginary displacement is √2 sin θ R≤√2κh/a, whereas the clearance is asymptotic to h/(2a). Since √2κ<1/2, the remaining clearance is at least c h/a for some fixed c>0.

Write A=4h+d and b=A+4ia. In p,q coordinates the quadratic part of the negative phase is (bp²+2dpq+conj(b)q²)/2. On the homotopy its real part is exactly

T(α)(y²+z²)/2+d yz,
T(α)=A cos(2α)+4a sin(2α).

Uniformly for 0≤α≤θ, there are fixed positive constants c_1,C_1 such that

c_1(h+aα)≤T(α)≤C_1(h+aα).

For the upper bound use sin(2α)≤2α. For the lower bound, on 0≤α≤π/8 the cosine is bounded below and sin(2α)≥cα; on π/8≤α≤θ<π/4 the sine supplies a multiple of a, which also dominates h+aα. Also |d yz|≤dR²=o(1).

The actual integrand is uniformly its quadratic model times 1+o(1) on this whole homotopy. Here are the needed complex estimates. Both kernel arguments have real parts r+O(R). If v=πexp(2(s±t)), then |v| is comparable to a and Re v≥c_2 h: the strip clearance just proved bounds its argument away from ±π/2 by c h/a. The theta series used in L269 therefore gives k/k_0=1+O(1/a)+O(exp(−c_3 h)) uniformly. The analytic model phase is defined using the logarithm near r>0. All third derivatives on this complex neighborhood are O(a+n/r³)=O(a), so its Taylor remainder is O(aR³)=o(1). This last estimate follows as well by applying the one-variable Taylor formula along the complex line segment from the saddle to each point. Thus the modulus of ω equals

(8π²)² exp(Φ_*) exp(−T(α)(y²+z²)/2−d yz)(1+o(1)) |ds∧dt|

uniformly on every face.

On y=R, dp∧dq=−iR dα∧dz, and the orthogonal coordinate change has determinant of modulus one, so |ds∧dt|=R dα dz. The same formula with R in absolute value holds for every face. For this face the normalized absolute integral, apart from fixed constants and 1+o(1), is

J=R∫_0^θ∫_(−R)^R exp(−T(α)(R²+z²)/2−dRz) dz dα.

Its upper bound is

J≤C R(2R)∫_0^∞ exp(−c aαR²)dα≤C'/a.

For the lower bound restrict to 0≤α≤1/(aR²), which lies below θ eventually, and retain all |z|≤R. On this region T(α)(R²+z²)=O(hR²+1)=O(1), and |dRz|=o(1). Hence the integrand is bounded below by a fixed positive constant. Its parameter area, including the Jacobian, is 2R²/(aR²)=2/a. This proves J≥c'/a. Changing the face changes only the sign of the harmless cross term, proving all four assertions. ∎

The quadratic Gaussian scale is exp(Φ_*)/a by L272. The rotated square captures asymptotically all of that Gaussian mass since aR²→∞, yet its connectors retain that same absolute scale. Consequently strip clearance and a small local Taylor remainder do not justify their removal. Oscillatory integration or cancellation between faces might still yield smaller signed contributions; no such estimate is asserted. No actual-theta Laguerre sign is disproved.

**Mathlib.** Full statement: not checked. Supporting complex Taylor estimates, differential-form pullbacks, and Gaussian estimates: not checked. No library match is claimed. L269 supplies the theta-series model and phase; L272 supplies the rotation and strip geometry. The face estimates are proved here.
