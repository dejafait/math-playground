# Lemma 376: one fixed order-zero function with unbounded exact-shift common zeros

**Hypotheses.** Put A=10^6, a_n=A^n and D_n=2−32(n−1), for integers
n≥1. The comparison response of a real entire P, on the real axis, is

\[
 R_P(t)=\operatorname{Re}\frac{P(t-2i)}{5/2+it}.
\]

No theta representation, Fourier-kernel positivity, count asymptotic,
physical discriminant inequality or response Laguerre sign is assumed.

**Conclusion.** There exist real numbers d_n with |d_n−D_n|≤1 such
that, on putting b_n=(a_n²+d_n)^(1/2), the single fixed product

\[
 P(z)=\prod_{n=1}^{\infty}
       (1-z^2/a_n^2)(1-z^2/b_n^2)                         \tag{1}
\]

is even, real entire, P(0)=1, and has precisely the simple real zeros
±a_n, ±b_n, all outside [−40,40]. It satisfies
log M_P(r)=O((log(2+r))²), hence has order zero. At every n≥1,

\[
 P(a_n)=R_P(a_n)=0,\qquad
 P(a_n-2i)/(5/2+ia_n)\ne0.                              \tag{2}
\]

Thus a single function satisfying the literal geometric conditions can
have positive common zeros tending to infinity. Its divided shifted
value at each such point is nonzero and purely imaginary.

**Proof.** We solve all phase conditions together, rather than multiply
individually tuned factors.

### 1. Uniform boxes and phase formula

Allow any sequence in the boxes I_m=[D_m−1,D_m+1]. Then |d_m|≤32m,
and

\[
 \tfrac12a_m^2\le b_m^2\le2a_m^2.                       \tag{3}
\]

Indeed m/A^(2m)≤1/A² and 32/A²<1/2. Also n³/A^(2n)≤1/A²:
the ratio of successive terms is at most 8/A²<1. These elementary
bounds will be used uniformly, including for truncated sequences.

Fix n and write a=a_n. Define

\[
 \alpha_n=\arctan a-\arctan(2a/5)
 =\arctan\frac{(3/2)a}{a^2+5/2}.
\]

For m<n and r∈{a_m,b_m}, set

\[
 \theta_{nm}(r)=-\arctan\frac{4a}{a^2-r^2-4};
\]

for m>n set

\[
 \theta_{nm}(r)=\arctan\frac{4a}{r^2-a^2+4}.
\]

All arctangents here are principal real arctangents. The denominators
are positive. In fact, for m<n, (r²+4)/a²≤1/2 by (3), A≥4 and
n≥2; for m>n, r²≥a_(n+1)²/2>2a². Define

\[
 \phi_n(d)=\alpha_n+
 \sum_{m\ne n}\bigl(\theta_{nm}(a_m)+\theta_{nm}(b_m)\bigr).
                                                               \tag{4}
\]

The tail converges uniformly over all boxes, as bounded below.
For a finite product through N≥n, write φ_n^(N) for the truncated sum.

To verify the phase, at z=a−2i a quadratic factor with root r equals
(r²−a²+4+4ia)/r². Each earlier factor has argument π+θ_nm(r),
and each later factor has argument θ_nm(r). The two factors of each
earlier pair therefore contribute 2π plus the two displayed angles.
The factor at a itself is 4(1+ia)/a², whose argument after division
by 5/2+ia is α_n. The remaining own-pair factor is
(d_n+4+4ia)/(a²+d_n). Consequently the complete divided product is

\[
 K_n(d)e^{i\phi_n(d)}(d_n+4+4ia),\qquad K_n(d)>0,          \tag{5}
\]

once product convergence and nonvanishing are checked in part 4.
For finite products (5) already follows by multiplication, with
positive K_n^(N). Thus, whenever |φ_n|<1/2, its real part vanishes
exactly when

\[
 d_n=T_n(d):=4a_n\tan\phi_n(d)-4.                       \tag{6}
\]

The phase sum excludes the entire nth pair, so T_n is independent
of d_n itself. No independence between different equations is assumed.

### 2. Uniform solvability estimate

Let h_n=3/2−8(n−1). We prove, for either the infinite sum or any
truncation N≥n,

\[
 |a_n\phi_n-h_n|\le500/A^2.                             \tag{7}
\]

For x≥0, |arctan x−x|≤x³/3. Applying this with
x=(3/2)a/(a²+5/2) gives

\[
 |a\alpha_n-3/2|\le(15/4+9/8)/a^2<5/a^2.
\]

For an earlier root put v=(r²+4)/a²≤1/2 and
u=4/[a(1−v)]≤8/a. Then

\[
 |a\arctan u-4|
 \le8v+512/(3a^2)
 \le(8r^2+203)/a^2.
\]

Summing both roots in all earlier pairs uses
Σ_(m<n)(a_m²+b_m²)≤3a_n²/(A²−1). Their total error from
−8(n−1) is at most

\[
 24/(A^2-1)+406(n-1)/a_n^2.
\]

For a later root, 0≤θ_nm(r)≤8a_n/r². Since
1/a_m²+1/b_m²≤3/a_m², all later pairs contribute, after multiplying
by a_n, at most

\[
 24a_n^2\sum_{m>n}a_m^{-2}=24/(A^2-1).                 \tag{8}
\]

This also proves the asserted uniform convergence. The combined
error is bounded by

\[
 48/(A^2-1)+(406(n-1)+5)/a_n^2
 \le48/(A^2-1)+406/A^2<500/A^2,
\]

proving (7). Removing some later terms preserves the same bounds,
so the estimate holds for every finite truncation.

As |h_n|≤8n and 500/A²<1, (7) gives |a_nφ_n|≤9n, hence
|φ_n|≤9/A<1/2, since n²/A^(2n)≤n³/A^(2n)≤1/A².
On |x|≤1/2, |tan x−x|≤2|x|³: indeed cos t≥1−t²/2≥7/8
and |sin t|≤|t| give |tan t|≤2|t| there. Integrating
(tan t)'−1=tan²t gives the stronger bound (4/3)|x|³.
Since D_n=4h_n−4, (7) yields

\[
 |T_n(d)-D_n|
 \le4\left(500/A^2+2(9n)^3/a_n^2\right)
 \le7832/A^2<1/2.                                      \tag{9}
\]

Every finite map T^(N) is continuous and maps the closed rectangle
I_1×⋯×I_N strictly into itself. This is a uniform estimate, not a
numerical residual or a claim that earlier cancellations are preserved
by freely adjoining factors.

### 3. Simultaneous solution and limiting equations

By the standard **Brouwer fixed-point theorem** (a continuous self-map
of a nonempty compact convex subset of finite-dimensional Euclidean
space has a fixed point), each T^(N) has a fixed point d^(N).
Extend it by d_m^(N)=D_m for m>N. Successive applications of the
Bolzano–Weierstrass theorem to the bounded real coordinates, followed
by a diagonal subsequence, give N_j→∞ and limits d_m∈I_m for every m.
Explicitly choose nested infinite index sets J_m⊂J_(m−1) on which
coordinate m converges, starting with J_0 equal to the positive
integers. Put N_0=0 and choose N_j∈J_j with N_j>max(N_(j−1),j).
For each fixed m,
all N_j with j≥m belong to J_m and tend to infinity. Thus every
coordinate converges along this same sequence, and eventually N_j≥n
for each equation n. Closedness of I_m retains the box constraints.

For a fixed n and M≥n, the first M terms in (4) are continuous in
these finitely many coordinates. Uniformly in every choice of the
remaining coordinates, the tail of a_nφ_n beyond M has modulus at most

\[
 24a_n^2\sum_{m>M}a_m^{-2}
 =\frac{24a_n^2 A^{-2(M+1)}}{1-A^{-2}}\longrightarrow0.  \tag{10}
\]

The same bound controls the omitted tail of a finite product. It
follows, first passing j→∞ on the finite head and then M→∞, that
φ_n^(N_j)(d^(N_j))→φ_n(d). Because |φ_n|≤9/A, tangent is continuous
throughout this passage. The exact finite equations therefore give

\[
 d_n=4a_n\tan\phi_n(d)-4
\]

for every n, simultaneously, in this one limit sequence. No assertion
about approximate equations or a sequence of different functions is
substituted for these identities.
More explicitly, for N_j≥M the difference of the two phases is bounded
by the finite-head difference plus twice the right side of (10)
divided by a_n. The head difference tends to zero for fixed M by
coordinate convergence and positivity of every phase denominator.
The remaining bound then tends to zero with M. This order of limits
is for fixed n; no uniformity in a moving n is assumed or needed.

### 4. Product, zero set, growth and exact cancellation

By (3), Σ_n(a_n^(−2)+b_n^(−2))≤3Σ_n A^(−2n)<∞. On every disc
|z|≤R, the corresponding sum of |z²/r²| converges uniformly. In a
sufficiently remote tail these terms are at most 1/2, so the power-series
logarithms converge absolutely uniformly using |log(1−u)|≤2|u|.
Their exponential is holomorphic and nonzero. Multiplying the finite
head proves that (1) is entire and that it has no zeros except the
listed factors' zeros. This argument also proves the nonvanishing
of its residual product at any listed zero after removing that factor.

For n=1, d_1∈[1,3]; for n≥2, d_n≤D_n+1≤−29. Thus b_n≠a_n
and all these positive roots are nonzero. The nth pair lies in
[a_n/√2,√2a_n]; these intervals are disjoint for different n because
A>2. All positive roots exceed a_1/√2>40. Each quadratic has simple
roots ±r, and its residual product is nonzero there, proving simplicity
and the complete asserted zero set. The real even finite products and
compact convergence show P is real and even, and P(0)=1.

For r≥A put N=floor(log_A r). From (3),

\[
 \log M_P(r)\le2\sum_{n\ge1}\log(1+2r^2/A^{2n})
 \le2N\log(1+2r^2)+4r^2\sum_{n>N}A^{-2n}
 \le2N\log(1+2r^2)+\frac4{1-A^{-2}}.
\]

Here r<A^(N+1) bounds the tail. This proves O((log(2+r))²).
The nonconstant entire function P has order zero by the definition
limsup log log M_P(r)/log r, and in particular order at most one.
For completeness, nonconstancy follows from its zeros and P(0)=1.
A nonzero positive-degree Taylor coefficient c_k gives
M_P(r)≥|c_k|r^k by Cauchy's coefficient estimate, so the order is
at least zero; the displayed upper bound gives the reverse inequality.

At z=a_n−2i, no factor vanishes since all factor zeros are real, and
the logarithmic-tail argument proves P(z)≠0. The divisor 5/2+ia_n
is also nonzero. The magnitudes in the finite version of (5) tend
to a positive limit: their product is the modulus of this nonzero
divided value divided by |d_n+4+4ia_n|. The phases converge by (10),
so (5) is valid with positive K_n for the limiting product.
Equation (6) now makes its real part exactly zero. The factor at a_n
in (1) gives P(a_n)=0, completing (2). ∎

Qualifications and source comparison: this is a comparison-function
obstruction to geometry-only eventual disjointness. It asserts no
common zero of actual F_0 and G, no physical D≤0 or response sign,
no Riemann–von Mangoldt count and no RH counterexample. The separate
critical audit of 2026-10-07 passed: the branch and complete divisor,
uniform bounds on every box and truncation, finite self-map hypotheses,
one increasing diagonal subsequence, uniform tails before tangent,
complete simple zero set, nonzero shifted values and order bound all
hold. The added diagonal and lower-order details make the limit and
growth checks explicit; no conclusion or constant required correction.
This verifies the existing comparison obstruction, not a new
actual-theta input or a result beyond the sources already compared.
The finite-family
L375 and the different nonreal-root product L068 motivated the test;
neither is a mathematical premise of this self-contained construction.
The logarithmic-tail and growth estimates are written explicitly to
check the changed root hypotheses uniformly over all simultaneous
choices. They do not reprove an imaginary-shift preservation theorem.

The prior EXPLORE comparison inspected Laine, *Nevanlinna Theory and
Complex Differential Equations* (1993), Theorems 1.2.3–1.2.4, pp. 7–8,
which give standard canonical-product existence/factorization inputs,
but not the simultaneous phase conditions. The direct bounds above
supply the needed specialization and uniform control without any
stronger unstated product theorem. Brouwer and Bolzano–Weierstrass
are used in their standard named forms explicitly stated above.
For the finite-dimensional fixed-point statement see R. S. Laugesen,
*Linear Analysis and Partial Differential Equations*, 22 December 2020,
[Theorem 1.16, printed p. 23](https://publish.illinois.edu/rlaugesen/files/2023/07/554-Lectures.pdf).
Each domain here is a nonempty closed bounded convex rectangle in R^N;
(9) and the positive denominators verify the whole-domain self-map
and continuity hypotheses. The logarithmic tails converge locally
uniformly, so the standard Weierstrass theorem on locally uniform
limits of holomorphic functions applies to their sums and to the
finite products. Exponentiating the tail, rather than convergence
alone, proves its nonvanishing.
No claim of originality beyond the bounded inspected comparison is made.

**Mathlib.** Full matching coverage was not checked; availability is
unknown. No formal verification or absence claim is made. Supporting
coverage was checked in Mathlib commit
`4beb549110aa44b87d699166cece6e3642bddf34`:
[`tendsto_subseq_of_bounded`](https://github.com/leanprover-community/mathlib4/blob/4beb549110aa44b87d699166cece6e3642bddf34/Mathlib/Topology/MetricSpace/Sequences.lean)
gives a convergent strictly indexed subsequence in the closure of a
bounded set in a proper pseudometric space. The real closed intervals
used here satisfy those hypotheses; the countable diagonal selection
is written above. This supporting theorem does not formalize the
phase equations, simultaneous construction or product estimates.
The inspected Mathlib theorem index points to an external Brouwer
formalization, but no Mathlib declaration for it was established.
