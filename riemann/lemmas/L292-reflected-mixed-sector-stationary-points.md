# Lemma 292: reflected mixed-sector stationary points

**Hypotheses.** Use k, F, a,n,r,h,τ and Φ_* from L269, with a tending to infinity and h in a fixed compact subinterval of (5,∞). Work on x>|s| and set u=x+s>0, v=x−s>0. Let j,k be positive integers and C₀=(8π²)². Here an exponential phase means the explicit real phase below; the lower-degree complex factors are retained in the amplitude.

**Conclusion.** The exact (j,k) theta summand in F is

C₀ exp(−2aτ) ((u−v)/2)^(2n) j⁴k⁴
 · exp(9(u+v)/2−π cos(2τ)(j²exp(2u)+k²exp(2v)))
 · E_j(u)E_k(v) exp(iΨ_jk(u,v)),

E_j(u)=1−3/(2πj²exp(2u+2iτ)),
Ψ_jk=a(u+v)−π sin(2τ)(j²exp(2u)+k²exp(2v))+9τ.

The absolute Jacobian for integration in u,v is 1/2. The unique stationary point in the unrestricted real plane is

u_j=r−log j, v_k=r−log k.

It is interior to this sector exactly when j,k<exp(r). The phase Hessian there is −2a times the identity. For j≠k the exact amplitude there is nonzero. Consequently no uniformly nonzero first directional derivative of this phase can hold throughout the sector for every summand.

In contrast, on the box B_r of L291, the derivative Ψ_u is at most −a(exp(4)−1) for every j,k. This box has no stationary point of these exponential phases. Neither assertion estimates its summed integral or the total mixed-sector integral.

**Proof.** Evenness gives k(s−x−iτ)=k(v+iτ), while s+x+iτ=u+iτ and 2ax=a(u+v). The theta series from L269 reads, for positive real u,

k(u+iτ)=8π² Σ_(j≥1) j⁴ exp(9(u+iτ)/2−πj²exp(2u+2iτ))E_j(u).

For each fixed τ<π/4 this series converges absolutely locally on u≥0, since cos(2τ)>0 gives Gaussian decay in j, including every displayed polynomial factor. Multiplication therefore gives the asserted exact double series pointwise. No uniform-in-a integration or interchange is claimed. The coordinate inverse s=(u−v)/2, x=(u+v)/2 gives the stated Jacobian. Separating real and imaginary parts yields precisely the amplitude and phase above.

The identity 2πexp(2r)sin(2τ)=a gives

Ψ_u=a[1−j²exp(2(u−r))],
Ψ_v=a[1−k²exp(2(v−r))].

Each expression is strictly decreasing in its own variable and vanishes exactly at the stated coordinate. Its derivative there is −2a and mixed derivatives vanish. Positivity of the coordinates is equivalent to j,k<exp(r). At this point s=log(k/j)/2, nonzero for unequal indices. Both lower-degree factors become

1−3/(h+ia),

using 2πexp(2r+2iτ)=h+ia. They are nonzero since a>0. All other amplitude factors are positive real numbers, proving nonvanishing. For example j=1,k=2 gives an interior nonzero-amplitude stationary point for all sufficiently large r. At a stationary point every finite first directional derivative is zero. This refutes the claimed whole-sector derivative certificate, but does not imply a large integral: the polynomial amplitude may be small.

Finally write B_r as s=r/2+α, x=r/2+β with 0≤α≤1 and 2≤β≤3. Then u=r+α+β≥r+2 and v=β−α>0. Thus j²exp(2(u−r))≥exp(4), proving the derivative bound uniformly in both indices. This supplies phase geometry only; integration by parts still requires boundary, amplitude-variation, and index-summation estimates before it can give o(exp(Φ_*)/a). ∎

**Mathlib.** Full statement: not checked. Supporting theta-series identities, coordinate changes, and phase differentiation: not checked. No full or supporting library match is claimed. L269 supplies the exact theta summands, evenness and parameter identities; L291 supplies the box whose phase is tested here.
