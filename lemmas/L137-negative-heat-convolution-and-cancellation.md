# Lemma 137: negative heat convolution and cancellation

**Hypotheses.** F is the theta heat deformation of L058. For a>0 let g_a(v)=(4πa)^(-1/2)exp(-v²/(4a)), v real. For a complex center c and R>0 define

m_R(c+v)=max_{|w-(c+v)|≤R}|F(0,w)|,
A_a(c)=∫_R g_a(v)|F(0,c+v)|dv,
B_a(c,R)=∫_R g_a(v)m_R(c+v)dv.

Here integrals with subscript R denote integration over the real line.

**Conclusion.** For every a>0 and z∈C,

F(-a,z)=∫_R g_a(v)F(0,z+v)dv.                         (1)

All these integrals converge absolutely. A_a(c)>0 and B_a(c,R) is finite. Define the cancellation factor

q_a(c)=|∫_R g_a(v)F(0,c+v)dv|/A_a(c)∈[0,1].          (2)

Whenever q_a(c)>0,

max_{|z-c|≤R}|F(-a,z)|/|F(-a,c)| ≤ B_a(c,R)/(q_a(c)A_a(c)).       (3)

For every Y≥0 and a≥0 there is the uniform absolute estimate

sup_{|Im z|≤Y}|F(-a,z)-F(0,z)|≤a C_Y,
C_Y=∫₀^∞u²K(u)exp(Yu)du<∞.                          (4)

These statements establish no polynomial relative bound uniform in unbounded Re c and 0≤a≤a₀ for any fixed a₀>0. In particular positivity of g_a alone gives no positive lower bound for q_a, even for Fourier transforms of positive finite even measures, as the explicit comparison below proves. No claim of failure of such a bound for the actual theta function is made.

**Proof.**

L058 gives F(0,z+v)=∫₀^∞K(u)cos((z+v)u)du. Since v is real, the absolute value of this integrand is at most K(u)exp(|Im z|u). The L058 superexponential majorant is integrable. Its integral times ∫g_a=1 dominates the double integral, so Fubini applies, locally uniformly in z.

For completeness put J(u)=∫g_a(v)exp(iuv)dv. The elementary real Gaussian integral gives J(0)=1. Differentiation under the integral is dominated by |v|g_a(v). Using vg_a=-2ag_a' and integration by parts with vanishing Gaussian boundary terms yields J'(u)=-2auJ(u). Thus J(u)=exp(-au²). Applying this identity to both exponentials in the complex cosine proves (1), with the sign corresponding to negative λ.

For |Im w|≤Y the same theta integral bounds |F(0,w)| by T_Y=∫₀^∞K(u)exp(Yu)du. Hence A_a(c)≤T_|Im c| and B_a(c,R)≤T_(|Im c|+R). The function m_R is continuous: translate the fixed compact radius-R disk and use local uniform continuity of F. It is therefore measurable. A_a(c)>0, because otherwise positivity of g_a and continuity force F(0,c+v)=0 on the entire horizontal line; the identity theorem would contradict F(0,0)>0 from L058.

The triangle inequality proves 0≤q_a≤1. For every z in the specified disk, z+v is in the disk centered at c+v, and (1) gives |F(-a,z)|≤B_a(c,R). Division by the exact center modulus q_a(c)A_a(c) proves (3). This isolates two sufficient inputs for a polynomial ratio: polynomial control of B_a/A_a and a polynomial lower bound on q_a. Neither is asserted here on a nontrivial heat interval. A zero-free center would give q_a>0, but would not supply its quantitative rate by this calculation.

Finally |1-exp(-au²)|≤au² for a≥0. Subtracting the two theta integrals gives (4), and finiteness of C_Y follows from L058. This implies uniform absolute convergence even on a whole horizontal strip as a↓0. It does not give relative convergence there: at the centers c=t+3i/2, L136 shows that |F(0,c)| decays like |t|^(5/2)exp(-π|t|/4). Dividing the bound aC_Y by that modulus gives no uniform small relative error for fixed a>0. This is a limitation of the bound, not a lower estimate for the error.

## Exact comparison showing cancellation

Fix a_*>0, b>0 and y>0, and put d=exp(-a_*b²)cosh(by)>0. The entire even function

f(z)=d+cos(bz)

is the Fourier transform of the positive even finite measure dδ₀+(δ_b+δ_(-b))/2. The same Gaussian calculation gives

∫g_(a_*)(v)f(z+v)dv=d+exp(-a_*b²)cos(bz).

At c=π/b+iy, cos(bc)=-cosh(by). The last integral is exactly zero, whereas

f(c)=(exp(-a_*b²)-1)cosh(by)≠0.

Its absolute-mass integral is strictly positive by continuity and nontriviality, so its cancellation factor is exactly zero. The averaged entire function is nonzero (its value at zero is positive), hence its maximum on every disk of positive radius about c is positive. There can be no general positive center lower bound relative to that maximum based merely on a positive Gaussian weight and a positive even Fourier measure. The example can be chosen for arbitrarily small a_*, but its measure then depends on a_*.

This measure is not the theta kernel and is not asserted to satisfy the other theta estimates or a common strip hypothesis. Thus it refutes only the proposed positivity inference, not a theta-specific estimate, a strip-preservation theorem, or RH. ∎

## Verification and formalization obligations

Analytic checks cover Gaussian normalization, the integration-by-parts sign, uniform Fubini domination, measurability and finiteness of disk maxima, positivity of A, the exact ratio inequality, the strip-uniform absolute error and its distinction from relative error, and the explicit nonreal cancellation. No numerical certificate is required. Formalization would require these integral identities and estimates, the identity theorem, and the finite-measure comparison. A common zero strip and the nonzero-parameter logarithmic Jensen ratio remain unproved.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
