# Corollary C032e: no nonzero compact exact branch profile at the fixed test point

## Hypotheses

Use the full theta kernel K of L019 and Xi of L018-L020, with
Phi(t)=K(t)/2 for t>=0 and Psi(s)=Phi(s/2)=K(s/2)/2 for s>=0.
In particular this is not a finite-mode or corrected kernel. Fix

\[
 \omega=\tfrac14,\qquad z=i,\qquad
 c=\frac{\Xi(3i/4)}{\Xi(5i/4)}.
 \tag{1}
\]

For a complex-valued f in C_c^infinity((0,infinity)), define, for
u>=0 and sigma in {-1,+1},

\[
 G_{\sigma,\pm}f(u)=\int_0^\infty
 \frac{f(s)}{\Psi(s)}(1\pm(s+u))
 e^{\sigma(s+u)/8}\Psi(s+u)\,ds.
 \tag{2}
\]

These are ordinary integrals over the compact support of f. L019
makes their denominators strictly positive. By L018,
Xi(5i/4)=xi(-3/4) is nonzero, since -3/4 lies outside the open
critical strip; thus c is a finite scalar, without any RH assumption.

## Conclusion

If

\[
 G_{\sigma,-}f(u)=cG_{\sigma,+}f(u)
 \quad\hbox{for every }u\geq0\hbox{ and both }\sigma,
 \tag{3}
\]

then f=0. In fact the proof uses just one fixed sigma in (3).
Thus the specified equation has no nonzero complex compact solution,
including no nonzero compact common-nullspace example.

This is an obstruction only to the additional compact exact
single-profile ansatz. It does not rule out completed noncompact
profiles, approximate realization, nonisometric pullbacks or limits
of cones, and gives no quantitative lower bound on approximation
defects. It supplies no actual-Xi positivity, graph realization,
initialization, Weyl bridge or RH conclusion. The conceptual audit1270
below accepts precisely this compact exact obstruction, including the
one-sigma strengthening, without extending its scope.

## Proof

### Checked inputs and purpose of the specialization

The invocation-start assessment is
`drafts/literature/2026-11-17-compact-core-branch-compatibility-review-1266.md`,
DECISION EXPLORE, with (1)-(3) as an explicit COVERED_TARGET. It
permits the analytic-continuation and transform-uniqueness reduction
below. This is a specialization of classical uniqueness, not a claim
of a new uniqueness theorem or of originality beyond checked sources.

Import Fourier uniqueness for continuous absolutely integrable
complex functions on R from [NIST DLMF, Section 1.14(i),
Uniqueness](https://dlmf.nist.gov/1.14.i), as inspected in that
assessment: equality of transforms at every real frequency implies
equality of the functions. We use the unnormalized convention

\[
 \widehat v(\xi)=\int_{\mathbb R}v(t)e^{-i\xi t}\,dt.
 \tag{4}
\]

The source uses the positive exponential; frequency reversal and its
nonzero constant normalization convert its transform to (4), without
changing equality at every real frequency or the uniqueness conclusion.
The standard identity theorem for
holomorphic functions is used on a connected strip and on C. These
theorems are not reproved. Neither Titchmarsh support addition nor
the sampled Laplace theorem is needed. The work below is necessary
to establish the full-theta continuation and the applicability of
Fourier uniqueness; the original half-line equation is not itself
a Fourier transform.

### Full theta continuation, evenness, and real-axis bounds

For a complex v in S={v: |Im v|<pi/4}, define

\[
 A(v)=e^{v/2}\sum_{n\geq1}e^{-\pi n^2e^{2v}},\qquad
 K_{\rm ext}(v)=2A''(v)-\tfrac12A(v).
 \tag{5}
\]

On every compact Q in S, Re(e^{2v}) has a positive minimum d_Q,
and |e^{v/2}|, |e^{2v}| are bounded. The series for A and its
first two termwise derivatives are bounded there by a constant
times the summable series
sum_{n>=1}(1+n^4)exp(-pi d_Q n^2). Uniform convergence and
holomorphy of the summands give a holomorphic A and justify (5).
Direct differentiation gives, throughout S,

\[
 K_{\rm ext}(v)=\sum_{n\geq1}
 \left(8\pi^2n^4e^{9v/2}-12\pi n^2e^{5v/2}\right)
 e^{-\pi n^2e^{2v}}.
 \tag{6}
\]

For real v>=0 this agrees with L019. No uniform lower bound on
Re(e^{2v}) over the whole strip is asserted or required.

For every real v, apply L016 at x=e^{2v}>0 to get

\[
 \psi(e^{2v})=e^{-v}\psi(e^{-2v})+\tfrac12(e^{-v}-1),
 \qquad A(v)-A(-v)=-\sinh(v/2).
 \tag{7}
\]

Both sides are twice differentiable by the compact convergence
just proved. Applying 2d^2/dv^2-1/2 to (7) annihilates sinh(v/2);
the second derivative of A(-v) is A''(-v). Therefore
K_ext(v)=K_ext(-v) on the entire real axis. Both functions are
holomorphic on the connected strip S, so the identity theorem
also gives this equality throughout S. In particular there is
no join or differentiability assumption hidden at v=0.

Define Psi_ext(t)=K_ext(t/2)/2, holomorphic on
T={t: |Im t|<pi/2}. It agrees with Psi on the positive real axis
and is even. L019 and evenness give Psi_ext(t)>0 for every real t
and, for some finite C,

\[
 |\Psi_{\rm ext}(t)|\leq
 C\exp\left(\tfrac94|t|-\pi e^{|t|}\right)
 \quad(t\in\mathbb R).
 \tag{8}
\]

Indeed L019 gives its stated bound for K(r) on r>=0; substitute
r=|t|/2. Consequently every fixed exponential and polynomial
weight times Psi_ext is integrable on both real tails.

For completeness this continuation respects the full Fourier
normalization: with Phi_ext(v)=K_ext(v)/2, evenness and the
two-sided decay give

\[
 \int_{\mathbb R}\Phi_{\rm ext}(v)e^{izv}\,dv
 =\int_0^\infty K(v)\cos(zv)\,dv=\Xi(z)
 \quad(z\in\mathbb C),
 \tag{9}
\]

by L020. The decay dominates exp(|Im z| |v|), so splitting and
changing variable in this integral are justified. Only this full
theta density is used; no identification with a truncated source
model is involved.

### The half-line equation is a holomorphic convolution

If f=0 there is nothing to prove. Otherwise choose finite
0<alpha<beta with supp(f) contained in [alpha,beta]. Define
h(s)=f(s)/Psi(s) for s>0 and extend it by zero for s<=0.
The positive smooth denominator has a positive minimum on
[alpha,beta], and f vanishes in neighborhoods of 0 and infinity.
Thus h belongs to C_c^infinity(R). Put H(v)=h(-v), so H has
support in [-beta,-alpha]. Fix either of the two signs sigma,
put a=sigma/8, and define the holomorphic kernel on T

\[
 k(t)=\big((1-c)-(1+c)t\big)e^{at}\Psi_{\rm ext}(t).
 \tag{10}
\]

Equation (8) shows that the real restriction of k is continuous
and in L1(R): its absolute value is bounded by a constant times
(1+|t|)exp((9/4+|a|)|t|-pi e^{|t|}). Also k is not identically
zero on R. The affine factor in (10) cannot vanish identically,
since 1-c=0 and 1+c=0 cannot both hold. The remaining factors
are nonzero on R, by positivity of Psi_ext and nonvanishing of
the exponential. This covers even c=1 or c=-1 without an
unstated sign assumption on c or f.

For w in T define

\[
 F(w)=\int_{\mathbb R}H(v)k(w-v)\,dv.
 \tag{11}
\]

This integral is only over the fixed compact support of H. For
each compact Q in T, the set of w-v with w in Q and
v in [-beta,-alpha] is a compact subset of T. The holomorphic
k and k' are bounded on a slightly enlarged compact subset.
These bounds times |H(v)| justify differentiation under the
integral, so F is holomorphic on T. No complex-tail domination
or analytic continuation of f is being assumed.

For real u>=0, change variable v=-s in (11). All arguments
s+u are positive, where Psi_ext=Psi, and (2) gives exactly

\[
 F(u)=\int_0^\infty\frac{f(s)}{\Psi(s)}
 \big((1-c)-(1+c)(s+u)\big)e^{a(s+u)}\Psi(s+u)\,ds
 =G_{\sigma,-}f(u)-cG_{\sigma,+}f(u).
 \tag{12}
\]

By (3), F vanishes on [0,infinity), which has an accumulation
point in the connected open strip T (for example at 1).
The identity theorem gives F identically zero throughout T,
in particular on the whole real line.

### Fourier uniqueness with complex cancellation retained

Both H and k are in L1(R), and

\[
 \int_{\mathbb R}\int_{\mathbb R}
 |H(v)k(u-v)|\,dv\,du=\|H\|_1\|k\|_1<\infty.
 \tag{13}
\]

Tonelli for the absolute values and Fubini therefore justify
the convolution formula for (4), with no distributional or
conditional interchange:

\[
 0=\widehat F(\xi)=\widehat H(\xi)\widehat k(\xi)
 \quad(\xi\in\mathbb R).
 \tag{14}
\]

The transform of k is continuous by dominated convergence.
It is not identically zero: otherwise the cited Fourier
uniqueness theorem, applied to the continuous L1 functions k
and 0, would contradict the nonvanishing established after
(10). Hence some real xi_0 has hat(k)(xi_0) nonzero. Continuity
gives a nonempty open real interval I on which hat(k) is nonzero.
Equation (14) forces hat(H)=0 throughout I.

Compact support of H makes

\[
 B(\zeta)=\int_{-\beta}^{-\alpha}H(v)e^{-i\zeta v}\,dv
 \tag{15}
\]

entire. On every compact set of zeta the integrand and its
zeta derivative are dominated by a constant times |H(v)|,
since v lies in a bounded interval. This proves holomorphy
by dominated differentiation. On real zeta, B=hat(H), so B
vanishes on I. The identity theorem on C gives B identically
zero. The cited Fourier uniqueness theorem now applies to
the continuous L1 functions H and 0 and gives H=0 everywhere.
It follows that h=0 and f=Psi h=0 on (0,infinity), as claimed.

Every transform argument is complex-linear; no positivity of
f, first nonzero endpoint asymptotic, or absence of cancellation
was assumed. Compact support is essential to the entireness
step (15) and to the holomorphic integral argument (11) as
written. The proof makes no assertion that evaluation profiles
in a completed source space have this support property.

### Independent conceptual audit — 17 November 2026, step1270

Under the unchanged SPECIALIZE scope in
`drafts/literature/2026-11-17-compact-branch-obstruction-audit-review-1268.md`
(approved1269), the following checks accept the proof as written.
The uniqueness theorem is reused; no broader injectivity theorem is
being introduced. These are verification details for (5)-(15).

For the differentiation in (5), set q=pi*n^2*exp(2v) in one summand
b(v)=exp(v/2-q). Then

\[
 b'(v)=(1/2-2q)b(v),\qquad
 b''(v)=(1/4-6q+4q^2)b(v).
 \tag{16}
\]

Thus (2D^2-1/2)b=(8q^2-12q)b, with exactly the powers and constants
in (6). The compact majorant preceding (6) controls these two
derivatives, including at every finite negative real v. It requires
no bound as Re(v) tends to minus infinity. In (7), the second
derivative of A(-v) has positive sign; the operator sends
sinh(v/2) to zero. The identity theorem applies on S because S is
connected, invariant under v -> -v, and contains the real zero set.
This verifies the passage through v=0 without joining separately
defined half-line functions. Rescaling by t/2 doubles the strip width
and divides 9/2 in the real exponential by two, as (8) requires.

For either real tail in the L1 estimate for k, set x=exp(|t|).
The majorant's integral is bounded by a constant times

\[
 \int_1^\infty (1+\log x)
 x^{9/4+|a|-1}e^{-\pi x}\,dx<\infty.
 \tag{17}
\]

The same substitution with any fixed additional exponential weight
only changes the finite power of x. Its integral against exp(-pi*x)
is still finite, which verifies the arbitrary fixed z weights in (9).
L019 gives positivity at zero as well as at every positive point;
evenness gives it on the negative axis. Compact division therefore
uses a strictly positive minimum, and extension by zero is smooth
because f is zero on a neighborhood of zero. No positive lower bound
for Psi on the entire line is needed. L018 gives the finite c at
xi(-3/4); its numerator, sign and magnitude are not needed to show
the affine factor in (10) is nonzero.

For (11), fix any compact Q in T. The translated compact set
Q-[-beta,-alpha] has a positive distance to the boundary of T.
Choose a smaller positive enlargement radius. On the resulting
compact neighborhood, bounds for k and k' times |H(v)| dominate the
integrand and its difference quotients. This justifies the complex
derivative of F locally at every w in T. The substitution v=-s has
both reversed bounds and dv=-ds, giving exactly the positive integral
and the minus-c-plus sign in (12). The real interval (1/2,3/2) is
inside T, so zero continuation is an interior identity-theorem use.
Only compact real translations are involved, not contour deformation.

Equation (13) follows by integrating the nonnegative absolute value
first in u, substituting t=u-v, and then integrating |H(v)|.
It also gives F in L1(R). For real xi, the Fourier exponential has
absolute value one, so the same absolute double-integral bound pays
Fubini in (14); the change u=t+v produces precisely
exp(-i*xi*t)exp(-i*xi*v). No Fourier inversion assumption or
integrability of either Fourier transform has been used. The cited
DLMF theorem applies to k and 0 because both are continuous L1
functions. Hence the nonzero k has a transform nonzero at some real
point. Continuity supplies an open interval, which is stronger than
the accumulating zero set needed for B.

Finally, for |zeta|<=R and |v|<=beta, the integrand in (15) is bounded
by exp(R*beta)|H(v)| and its derivative by
beta*exp(R*beta)|H(v)|. These integrable bounds hold for every finite
R, proving entireness rather than merely holomorphy near the real
axis. B vanishes on the interval from (14); the identity theorem on
the connected domain C makes it zero everywhere. DLMF uniqueness
then applies to the continuous compactly supported H and 0, giving
pointwise zero, not merely a formal transform cancellation. The
argument retains arbitrary complex f throughout and uses only one
sigma. The independent checks found no failed hypothesis or sign,
scale, boundary, or interchange error.

Audit result: the exact compact route stop is accepted. This is
verification of a local specialization of classical results, not
progress beyond the checked literature or a new positivity mechanism.
In particular no estimate of an approximate defect, no identification
of a completed source norm/domain, and no actual-Xi sign follows.
The direct local inputs remain L016,L018,L019,L020: respectively
modularity, the definition of c, positivity/tails, and the consistency
normalization (9). L020 is used for that consistency check and is not
needed for the injectivity implication itself. No dependency was added.

## Mathlib

Full matching theorem and Fourier-uniqueness formalization: not
checked; availability is unknown. L016 records supporting theta
and smooth-series references, including
[the Gaussian Poisson-summation result](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gaussian/PoissonSummation.html#Real.tsum_exp_neg_mul_int_sq).
Those are supporting results, not a formalization of this proof.
No Lean verification or numerical certificate is claimed.
