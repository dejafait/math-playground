# Lemma 452: fixed-half-plane logarithmic derivative and endpoint interfaces

**Hypotheses.** Use the cited zeta specialization of OpenAI,
*The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8*,
September 30, 2026, Theorem 1.1, at pinned commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`:
ζ(s) has no zeros in Re(s)>7/8, with its pole at s=1 allowed.
The [precise source and verification qualifications](../foundations/2026-10-quasi-riemann-input.md)
are load-bearing. No local build or complete external proof audit is
claimed. In particular, this lemma is a specialization using that
external theorem, not an independent proof of its hypothesis.

Put g=ζ′/ζ. For the endpoint applications use exactly L330's and
L331's notation: r=2n, a=a_n=sqrt(4π²exp(4r)−25),
V_r=log(r)/sqrt(r), σ=1+1/r, c=1/2+1/r,
σ₀=1+1/(2r), and x₀=(r+1)/(2r).

**Conclusion.** There are fixed C,t₀>0 such that

    |g(σ+it)| ≤ C(log t)^(1/3)                            (1)

for every t≥t₀ and 63/64≤σ≤2. This includes the requested strip
63/64≤σ≤65/64; the extra right-hand width ensures that the whole
L331 disk is covered.

Consequently L330's M_r=O(r^(1/3))=o(sqrt(r)), and its relative
freezing conclusion gives

    Z_r(a_n;c)/B_r(a_n) = 1+O(r^(−1/6)).                  (2)

For d=1/128, g is analytic on a neighborhood of the complete closed
disk |s−(σ₀+ia_n)|≤2d. Its supremum M is O(r^(1/3)), hence
M≤rd/4 eventually. Thus L331's local criterion applies: H_r has
exactly one stationary point x_* in [x₀−d,x₀+d],

    H_r″(x)≥r/2 on that interval,
    |x_*−x₀|≤M/r=O(r^(−2/3)).                            (3)

All constants and onsets are uniform in the stated variables, though
not numerically evaluated. This proves the two sufficient interfaces
under the cited external input. It does not assemble a new global
Laguerre sign range, prove a complete saddle asymptotic, settle any
smaller index or bounded exterior height, pass to every height, or
resolve RH. The separate critical audit below validates this
specialization and both interfaces, conditional on the pinned
external input; it does not audit that input's full proof.

**Proof.** The source mechanism is Littlewood's logarithm
interpolation, as presented in E. C. Titchmarsh, *The Theory of the
Riemann Zeta-function*, second edition revised by D. R. Heath-Brown
(1986), [Theorem 14.2 and proof, pp. 336–337](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=173),
and [Section 14.3, pp. 338–339](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=174).
The printed theorem assumes RH. We do not import that conclusion or
assumption; we specialize the inspected Borel–Caratheodory,
Hadamard three-circles and Cauchy mechanism to fixed disks under the
different cited zero-free boundary. The following details are needed
because that boundary and the required neighborhoods differ.

First record a uniform elementary growth bound, rather than assume
any smallness of the logarithm from nonvanishing alone. For Re(s)>1,
partial summation of the absolutely convergent defining series gives

    ζ(s)=s/(s−1)−s∫_1^∞ {u}u^(−s−1)du.                  (4)

Indeed ζ(s)=s∫_1^∞ floor(u)u^(−s−1)du, by integrating each
indicator 1_{u≥m}; absolute convergence justifies summation.
Writing floor(u)=u−{u} proves (4). The fractional-part integral
converges locally uniformly and is analytic for Re(s)>0, since
0≤{u}<1 and its compact majorants, including differentiated ones,
are integrable. Meromorphic continuation therefore proves (4) there
away from 1. If Re(s)≥113/128, s lies in a fixed-width strip, and
Im(s)=t+O(1) with large positive t, it follows that

    |ζ(s)|≤|s|/|s−1|+|s|/Re(s)≤C₁t.                    (5)

This elementary growth argument is included only to verify the
uniform input to the source mechanism, not as a new growth theorem.

For t sufficiently large put w_t=2+it and choose fixed radii

    R₀=255/256, R₁=131/128, R₂=71/64, R₃=143/128.

They satisfy 0<R₀<R₁<R₂<R₃<9/8. The closed R₃ disk has
Re(s)≥2−R₃=113/128>7/8 and positive imaginary part when
t>R₃; it therefore meets neither a zero nor the pole. It has a
slightly larger zero-free, pole-free disk as a neighborhood. On
this simply connected neighborhood choose an analytic logarithm
f_t of ζ, normalized by

    f_t(w_t)=L(w_t),

where L is L005's absolutely convergent Euler logarithm on Re(s)>1.
This normalization is possible because exp L(w_t)=ζ(w_t).
No Euler series is asserted to converge left of 1. On the R₀ disk,
whose minimum real part is 257/256>1, the two logarithms agree:
their difference is a continuous 2πi-integer-valued function on a
connected disk and vanishes at w_t. Thus

    max_(|s−w_t|≤R₀)|f_t(s)|≤log ζ(257/256)=C₀<∞.         (6)

Also |f_t(w_t)|≤log ζ(2). On the R₃ disk, (5) gives
Re f_t(s)=log|ζ(s)|≤log(C₁t). The named Borel–Caratheodory
inequality on the concentric R₃ and R₂ disks now gives

    max_(|s−w_t|≤R₂)|f_t(s)|≤C₂ log t,                   (7)

with C₂ independent of t. For example, with A the maximum of
Re f_t on the R₃ disk, the bound is
|f_t(w_t)|+2R₂·(A−Re f_t(w_t))/(R₃−R₂); all quantities
except A are bounded by fixed constants. The positive fixed gap
R₃−R₂=1/128 is essential.

Set M_t(R)=max_(|s−w_t|≤R)|f_t(s)|. Hadamard's named
three-circles theorem, (6), and (7) imply

    M_t(R₁)≤M_t(R₀)^(1−θ)M_t(R₂)^θ≤C₃(log t)^θ,
    θ=log(R₁/R₀)/log(R₂/R₀).                             (8)

Here θ<1/3 is an exact rational-radius comparison: in units 1/256,

    R₀=255/256, R₁=262/256, R₂=284/256,
    262³=17984728 < 18467100=255²·284.

Thus 3log(R₁/R₀)<log(R₂/R₀). Since log t≥1 eventually,
(8) in particular gives M_t(R₁)≤C₃(log t)^(1/3).

Fix s=σ+it with 63/64≤σ≤2. Its closed radius-ρ circle,
ρ=1/128, lies in the R₁ disk, because

    |s−w_t|+ρ=2−σ+1/128≤65/64+1/128=R₁.

The function f_t is analytic on a neighborhood of this circle.
Cauchy's derivative estimate and f_t′=ζ′/ζ give
|g(s)|≤ρ^(−1)M_t(R₁)≤128C₃(log t)^(1/3). This proves (1)
on the whole stated strip, including its endpoints, with uniform
constants. Agreement of different t-indexed branches is unnecessary:
each derivative is the same branch-independent g.

For L330, uniformly for |u|≤V_r,

    log(a_n+u)=2r+log(2π)+o(1),

since a_n=2πexp(2r)(1+O(exp(−4r))) and V_r/a_n→0.
For large r, 1+1/r belongs to [63/64,2] and a_n+u≥t₀.
Equation (1) yields M_r≤C₄r^(1/3). Its ratio to sqrt(r) is
O(r^(−1/6))→0, so the premise M_r≤sqrt(r) of L330's
estimate is actually satisfied. That estimate gives (2): its
remaining tail (r+1)^4exp(−(log r)²/8) is o(r^(−A)) for
every fixed A>0. This is a relative estimate against B_r first;
no comparison of that tail directly with exp(−r/256) is used.

For L331 take d=1/128, so 2d=1/64. The complete closed disk
has real parts in

    [63/64+1/(2r), 65/64+1/(2r)] ⊂ [63/64,2]

for r≥2, and imaginary parts within 1/64 of a_n. The upper
endpoint is slightly beyond 65/64, which is why (1) was proved
with extra right-hand width. The disk has a zero-free, pole-free
neighborhood under the cited half-plane input; g is analytic there.
Applying (1) at every point gives M≤C₅r^(1/3). The ratio of
this available upper bound to rd/4=r/512 is

    512C₅r^(−2/3)→0.

Thus L331's full disk hypothesis holds eventually. Applying its
proved local criterion, with 0<d≤1/8, proves (3). No new contour
shift or saddle approximation is being made here.

The historical L330/L331 countermodels obey the older shrinking
regional envelopes. They do not invalidate a consequence of the
newly proved fixed-domain logarithm bound with its Euler
normalization and uniform polynomial growth. Conversely, those
models remain valid obstructions under their original hypotheses.
The present specialization is local progress using cited sources,
not a claim of mathematical originality or of RH. ∎

### Critical audit — 2026-10-22

**Verdict and boundary.** Equations (1)–(3) pass the independent
mathematical audit with their stated quantifiers. No correction to
the argument or additional hypothesis is needed. This closes the
local correctness-review obligation, not a new theorem beyond the
known-source specialization. The September 30 Theorem 1.1 remains
an external input with the verification qualifications in the
Hypotheses; no audit of its manuscript or formal import closure is
implied. The final endpoint sector assembly is not audited here.

**Logarithm and growth.** The R₃ disk has minimum real part
226/256, exceeding the excluded boundary 224/256. It may even be
enlarged by 1/256 while remaining strictly inside the cited region.
At sufficiently large positive t the enlarged disk misses the pole.
The holomorphic-logarithm theorem therefore applies on an open
simply connected neighborhood of the complete closed disk, not only
on its diameter. L005 fixes f_t(w_t) including its imaginary part;
exp(f_t−L)=1 and connectedness fix the entire inner-disk branch.
Its real parts exceed 1, so no prime series is continued past its
domain of convergence. In (4), every derivative of the integral
on a compact subset of Re(s)>0 is dominated by a constant times
u^(−1−δ)(1+log^k u), δ>0. Thus continuation and the uniform O(t)
growth bound are legitimate. Only Re f_t is bounded by that growth
estimate; Borel–Caratheodory, with the bounded normalized center
value, supplies the missing bound on the complete logarithm.

**Radii, exponent and Cauchy transfer.** In units of 1/256 the
four radii are 255, 262, 284, 286. The outer interpolation margin
is 2/256, fixed independently of t. The exact cubic comparison in
(8) gives θ<1/3<1/2. The farthest target point is 260/256 from
the center; its radius-2/256 Cauchy circle fits the closed R₁ disk,
including the equality case. Analyticity holds on a neighborhood
of that disk, so touching its boundary is harmless. All growth,
center, interpolation and Cauchy constants depend only on these
fixed radii and real-strip bounds, not on t or σ. Recenter at the
actual imaginary part of each s when applying (1) to a complex
moving disk; no identification of different logarithm branches is
required because their derivatives are all ζ′/ζ.

**Complete freezing interface.** Rechecking L330's proof against
the inherited L303–L304 definitions retains the two factors at
a+v and −a+v. The second logarithmic derivative in its integrated
variation is the conjugate of the one at a−v. Hence the same M_r
controls both factors on the whole interval |v|≤V_r. With
p=M_r/sqrt(r)≤1, its central error is bounded by a fixed constant
times

    p ∫_ℝ |w| exp(−w²/4+2|w|) dw,

whose integral is finite independently of r. There is no window
supremum loss of log r. For the entire complement, absolute
Dirichlet convergence holds at σ=1+1/r for every v, even where
one shifted height is zero. The bounds |F_r|≤(r+1)² and
B_r≥(r+1)^(−2), together with the kernel tail, give exactly
O((r+1)^4 exp(−(log r)²/8)) in relative error. The kernel has
integral one by the inherited absolutely convergent inversion;
K_r(−v)=conj K_r(v) and F_r(−v,a)=conj F_r(v,a) also verify
reality without assuming a positive kernel. At the prescribed
coupled heights p=O(r^(−1/6)), so p≤1 eventually, and the full
tail is o(r^(−1/6)). This verifies (2), with one eventual onset
and one constant. It neither compares that tail directly with
the exponentially smaller sector error nor asserts a bound
uniform over all heights at a fixed r.

**Complete saddle interface.** For r≥2 the radius-1/64 disk has
real part between 63/64+1/(2r) and 65/64+1/(2r), with upper
endpoint below 2, and imaginary part a_n+O(1). Equation (1)
therefore bounds its entire supremum, not just the real diameter.
Its analytic neighborhood follows from the same strict half-plane
and pole exclusion. With d=1/128, M/(rd/4)=O(r^(−2/3))→0.
In L331's criterion, every radius-d circle centered on the
smaller real interval lies in this closed radius-2d disk. Cauchy
then gives |g′|≤M/d≤r/4. The interval is contained in (0,1),
so (r+1)/x²≥r and H_r″≥r/2. Its bare derivative has opposite
endpoint signs of magnitude at least 2rd, larger than 2M≤rd/2.
Strict increase gives the unique stationary point. The exact
stationary equation gives |x_*−x₀|=x_*|Re g|/r≤M/r,
verifying the stated O(r^(−2/3)) displacement. The conjugate
negative-height factor is retained in H_r throughout. No cubic
remainder, contour deformation or complementary saddle estimate
is inferred from this local criterion.

The old countermodels do not satisfy the combination of fixed-domain
polynomial growth and a uniformly bounded inner logarithm used here.
Their stated shrinking-region obstructions remain intact. Global
mixed positivity, lower indices, bounded exterior heights and
every-height passage remain unresolved.

**Mathlib.** The full fixed-half-plane specialization and its two
endpoint applications have not been checked for matching Mathlib
coverage; absence is not asserted. L005 records supporting
`riemannZeta_eulerProduct_exp_log` at its
[direct Mathlib link](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log).
The external register identifies the pinned supplied artifact
`OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`; this is not a claim
that it is in Mathlib or has been built locally. Supporting
logarithm-existence, Borel–Caratheodory, three-circles and Cauchy API
names have not been checked. Their standard named theorem statements
are the complex-analysis inputs to the complete specialization above.
