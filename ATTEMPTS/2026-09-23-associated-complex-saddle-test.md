# Associated-kernel complex-saddle test — 2026-09-23

Gap: actual-theta exterior signs D_n(Ξ;a)≥0 through L266's cutoff K(a). The proposed intermediate target is uniform eventual positivity when n/a lies in a fixed compact subinterval of (0,∞). This would cover a proportional-index portion of K(a)~πa/(2 log 4), not the indices n=o(a) or bounded heights. The test is whether a contour-accessible positive saddle contribution admits total relative error less than one. Saddle location or a positive formal Gaussian alone does not pass that test.

Redundancy check: L267–L268 discard oscillation and fail uniformly through K(a). L239 supplies analytic-strip contour shifts but only absolute transform bounds. The stationary-phase calculations L182–L185 concern different arithmetic sums. None supplies the relative estimate tested here. Existing changes and stopped-route evidence are retained.

## Hypotheses

Take a>0, n≥1, and the actual even theta kernel k. L267 reduces the sign to that of

I_n(a)=∫∫ s^(2n) k(s+t)k(s−t) exp(2iat) ds dt.

Let λ_0≤n/a≤λ_1 for fixed 0<λ_0≤λ_1<∞, and consider a→∞. On the positive tail introduce the leading model

k_0(z)=8π² exp(9z/2−π exp(2z)).

This model is not an even replacement for k on the whole line.

## Conclusion of this exploration

The model has a unique saddle (s,t)=(r,iτ) with r>0 and 0<τ<π/4. Its two-dimensional Gaussian integral is positive. The saddle approaches the strip boundary, but its local theta-series tail remains exponentially small. Thus strip access does not immediately kill this mechanism. No bound on the total integral relative to this Gaussian is established here; no actual Laguerre sign is certified. Outcome: EXPLORATION, one of three consecutive unresolved exploration turns.

## Derivation and scope of the proof

First, an exact contour identity is available, for each fixed a,n and 0<τ<π/4:

I_n(a)=e^(−2aτ)∫∫ s^(2n) k(s+x+iτ)k(s−x−iτ) exp(2iax) ds dx.       (1)

For fixed real s, shift t upward in the strip supplied by L239. Its uniform bounds on each closed smaller strip make the vertical edges vanish. The absolute horizontal double integral is finite: under u=s+x,v=s−x, the factors have superexponential decay in |u| and |v|, dominating the polynomial s^(2n). The same bounds dominate the intermediate horizontal lines, so Fubini and dominated convergence justify integration in s. This is a parameterwise identity; its constants have not been made uniform as τ→π/4. Evenness of k and s^(2n) makes the integrand in (1) even in s. The negative-s saddle contributes equally and must not be silently omitted.

Where k is nonzero write g=k'/k. Exact stationary equations at s=r,t=iτ are

n/r+Re g(r+iτ)=0,    Im g(r+iτ)=−a.                  (2)

They follow by differentiating 2n log s+log k(s+t)+log k(s−t)+2iat, using conjugation. No assertion of a solution of (2) for actual k is made here.

For k_0 the phase, apart from the positive factor (8π²)², is

Φ(s,t)=2n log s+9s−2π exp(2s)cosh(2t)+2iat.

Put h=n/r+9/2. Its saddle equations are exactly

2π exp(2r)cos(2τ)=h,    2π exp(2r)sin(2τ)=a.        (3)

Consequently r is the unique positive solution of

(2π exp(2r))²=a²+(n/r+9/2)²,                       (4)

and τ=(1/2) arctan(a/h). Existence and uniqueness follow because the left side of (4) is strictly increasing, the right side strictly decreasing in r, the right side diverges at zero, and the left side diverges at infinity.

Uniformly in the prescribed λ range, r≥(1/2)log(a/(2π)), so h/a=O(1/log a). Taking logarithms of (4) yields

r=(1/2)log(a/(2π))+(1/4)log(1+(h/a)²)
 =(1/2)log(a/(2π))+O((log a)^(−2)).

It follows that h~2n/log a and

π/4−τ=(1/2)arctan(h/a)~n/(a log a).

In particular the saddle lies inside the strip, though no fixed smaller strip contains all these saddles. At z=r+iτ, v=π exp(2z) has Re v=h/2→∞ and |v|~a/2. The exact theta series of L019, extended as in L239, gives

k(z)/k_0(z)=1−3/(2v)+Σ_(m≥2)(m⁴−3m²/(2v))exp(−(m²−1)v).

The sum is O(exp(−3 Re v)) as Re v→∞: bound its modulus by a constant times Σ m⁴ exp(−(m²−1)Re v), factor out exp(−3 Re v), and bound the remaining sum at Re v≥1. Hence at this model saddle

k(z)/k_0(z)=1+O(1/a)+O(exp(−3h/2)).                (5)

This is a pointwise tail comparison, not an integrated relative-error estimate or a proof of an actual saddle.

The negative phase Hessian on the shifted real coordinates s=r+u,t=iτ+x is

B = [[2n/r²+4h, 4ia], [4ia, 4h]],
det B=16(h²+a²)+8hn/r²>0.

Its real part is positive definite. Successively integrating in u and x proves, by the elementary Fourier transform of a real Gaussian,

∫∫ exp(−(u,x)B(u,x)^T/2) du dx=2π/sqrt(det B)>0.

Thus the formal contribution of the positive-s saddle is

(8π²)² exp(Φ(r,iτ)) 2π/sqrt(det B),                (6)

which is positive since Φ(r,iτ)=2n log r+9r−h−2aτ is real. The reflected saddle gives an equal formal term. Equation (6) has not been proved asymptotic to the integral.

A significant quantitative loss must be addressed before claiming dominance. The integral of the modulus of this Gaussian is 2π/sqrt((2n/r²+4h)4h). Its ratio to the signed integral is

sqrt(det B/((2n/r²+4h)4h)) ~ a/h ~ a log a/(2n).

This diverges like log a in the proportional-index range. Therefore an absolute remainder o(1) relative to the Gaussian's modulus mass is insufficient by itself; it must be o(1/log a) to give o(1) relative error in (6). The remaining regions include |s| near zero and |x| comparable to |s|, where replacing both kernels by their positive-tail first term is invalid. Formula (5) at one point does not control these regions. The exact contour identity alone supplies no uniform relative estimate there.

## Assessment and continuation test

Continue once with a uniform remainder estimate for (1) in λ_0≤n/a≤λ_1: prove the local Taylor and kernel errors are o(1/log a) relative to the Gaussian modulus mass and the complementary contour integral is o((6)). A bound on only the local model is insufficient. If this fails because another region competes, record its size and reassess rather than repeating saddle-location algebra. Even success leaves n=o(a), bounded heights, and hence the full RH positivity gap open. No candidate proof is recorded and the overall argument is unchanged.

## Mathlib

Full statement and supporting contour-shift, Gaussian Fourier-transform, and asymptotic results: not checked. No library match is claimed. The calculations and the parameterwise identity are proved above; the uniform dominance assertion is explicitly unproved.
