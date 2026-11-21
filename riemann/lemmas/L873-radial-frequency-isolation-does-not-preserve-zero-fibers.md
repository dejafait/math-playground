# Lemma 873: radial frequency isolation does not preserve the zero-fiber constraint automatically

## Hypotheses

Retain the full actual-F class of L872, without using its unaudited
moving-error estimate. Explicitly, let

\[
G(z)=\tfrac18\xi(\tfrac12+\tfrac{\sqrt z}{2}),\quad G(0)>0,
\qquad F(z_1,z_2)=-C G(z_1)G(z_2)(z_1-z_2)^2/(z_1^2z_2^2),
\quad z_j=R e^{x_j+i y_j},\quad C,R,H>0.
\tag{1}
\]

The real functions h,q,r are global C1 on R2 times T2, periodic in
both angles, and satisfy

\[
h\geq0,\qquad q^2+r^2\leq |F|^2,\qquad
r_{x_j}=q_{y_j},\quad(q+h)_{x_j}=-r_{y_j}\quad(j=1,2).
\tag{2}
\]

Normalize angular integrals by (2pi)^(-2), put m=hhat_0, retain
the original ell=log(|a_*|/R) for the originally selected Hardy
zero, both means m(s,s)=m(ell,s)=H and the selected trace
q((ell,s),(pi,v))=r((ell,s),(pi,v))=0. For every n!=0 retain

\[
\widehat h_n(x)=U_n(n\cdot x),\quad
U_n\in C^1(\mathbb R;\mathbb C)\cap C_0(\mathbb R;\mathbb C),
\quad |U_n|\leq H,\quad
U_{-n}(t)=\overline{U_n(-t)},\quad U_n=B_n-B_n'',\quad B_n\in C^3.
\tag{3}
\]

At every x retain all finite opposite-index tests with a_0=H,
a_k=hhat_(k,-k)(x) for k!=0:
sum_(j,l=0)^N c_j conjugate(c_l) a_(j-l)>=0 for every N and c.
There is no growth condition on the lifts or radial mean, uniform
angular tail, summability, common profile support, spacing, RH or
graph-realization assumption. The C868b coefficient bound in (3)
is part of the unchanged class; no stronger norm is used below.

Let Lambda be the logarithmic radii of all negative real zeros of
G. L871's actual-zero argument makes this a nonempty, unbounded
set with no finite accumulation. Fix integers a,b with b!=0 and
define the classical C1 angular projection

\[
f_b(x,u)=\frac1{2\pi}\int_0^{2\pi}h(x,(u,v))e^{-ibv}\,dv.
\tag{4}
\]

Fourier transform on R^d means integral exp(-i x dot eta), with
inverse factor (2pi)^(-d). A radial multiplier acts on x, leaving
u unchanged. C0 denotes decay at both ends of the real line.

## Conclusion

The separate conceptual audit of 6 November 2026 below accepts the
following operational result under exactly these hypotheses. It does
not prove angular rigidity or exhibit an admissible nonzero profile.

1. The function (4), regarded locally as a distribution, has a
   tempered distribution realization on R2 times T, even though
   the zero mode and the lifts have not been made tempered. Its
   first-angle Fourier coefficients are exactly
   U_(k,b)(k x1+b x2).
2. If the selected U_(a,b) is nonzero, there is a smooth compact
   radial multiplier p supported away from eta2=0 such that

   \[
   p(D_x)f_b(x,u)=e^{iau}V(a x_1+b x_2),\qquad
   V\in C_0(\mathbb R),\quad V\ne0.
   \tag{5}
   \]

   Every other first-angle index is killed exactly. No infinite
   tail estimate is needed for this distributional identity.
3. The original constraints give

   \[
   f_b((\lambda,s),\pi)=c_\lambda\quad(s\in\mathbb R,
   \ \lambda\in\Lambda).
   \tag{6}
   \]

   If (6), even just constancy in s, survived (5), C0 decay would
   force V=0. But radial localization is not an operator preserving
   this trace constraint: for the very same nonzero multiplier p
   and any chosen lambda_* in Lambda, there is a complex smooth
   compactly supported W on R2, zero on every line x1 in Lambda,
   with

   \[
   (p(D)W)(\lambda_*,0)=1,
   \qquad p(D)W(\lambda_*,s)\longrightarrow0\quad(|s|\to\infty).
   \tag{7}
   \]

   Thus an identically zero trace can become nonconstant. W is an
   operator diagnostic, not a ridge-profile family or an actual-F
   triple; it supplies no counterexample to rigidity or RH.

Filtering only the tangential radial variable can annihilate the
constant trace when applied to that trace itself, but it multiplies
every profile U_(k,b) by the same one-dimensional multiplier. It
does not isolate k=a. For a distributional reconstruction, commuting
that filtering with angular restriction remains an additional
obligation, not a consequence asserted here.

## Proof

### Source imports and scope

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-06-actual-f-radial-frequency-isolation.md`.
It covers this bounded localization and trace-compatibility test.
Reuse Semyon Dyatlov, *Lecture notes for 18.155: distributions,
elliptic regularity, and applications to PDEs*, dated 2 November
2026, [Section 11.2, pp126-129, equations (11.38)-(11.39) and
Proposition 11.25 with proof](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf#page=126).
These provide the tempered Fourier transform, tensor/linear-change
rules and convolution with a Schwartz function. Each U_n is bounded,
so defines a tempered distribution. Compact smooth frequency
cutoffs have Schwartz inverse transforms. The explicit estimates
below verify the countable reconstruction and the needed nonzero
window, which the general imported statements do not supply.

For identification on compact radial sets reuse Loukas Grafakos,
*Classical Fourier Analysis*, third edition (2014), Definition
3.1.8, Remark 3.1.9, Proposition 3.1.10 and Corollary 3.2.2,
[pp180-183](https://www.math.stonybrook.edu/~bishop/classes/math638.F20/Grafakos_Classical_Fourier_Analysis.pdf),
with [corrected Theorem 1.2.19(2) and proof, pp27-29](https://grafakos.missouri.edu/Books_Correction_Pages/CFA-Page27-29.pdf).
Only continuous-slice Fejer convergence is imported. The compact
uniform version used below follows directly from uniform continuity
on that compact product and the same positive approximate identity.

Reuse L871's construction of the actual negative zeros, from
E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, second
edition revised by D. R. Heath-Brown (1986),
[Section 10.2, pp256-258](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=133).
Its a=-4 gamma^2 specialization and isolation of zeros use only the
actual entire G and G(0)>0, not compact forcing support. On each
bounded logarithmic interval the corresponding negative a lie in a
compact subset of the punctured plane, so Lambda has no finite
accumulation. No spacing theorem is needed here.

For comparison only, Brouder-Dang-Helein,
*Continuity of the fundamental operations on distributions having a
specified wave front set*, Studia Mathematica 232 (2016), 201-226,
[arXiv:1409.7662v2, Proposition 5.1, p13, proof pp15-17](https://arxiv.org/pdf/1409.7662v2#page=13),
is a sufficient wavefront-controlled pullback theorem. It does not
say that a convolution preserves a prescribed trace. No wavefront
condition, uniform pullback theorem or transform of q,r is invoked.
These are applications of known Fourier operations and an explicit
diagnostic, not a claimed new general Fourier theorem.

### A tempered reconstruction without the zero mode

Write n_k=(k,b). For a Schwartz test phi(x,u), periodic and smooth
in u, put phi_l(x)=(2pi)^(-1) integral phi(x,u)e^(-ilu) du.
Define, with normalized angular pairing,

\[
\langle T_b,\phi\rangle
 =\sum_{k\in\mathbb Z}\int_{\mathbb R^2}
       U_{(k,b)}(n_k\cdot x)\phi_{-k}(x)\,dx.
\tag{8}
\]

Twice integrating by parts in u shows, including k=0 separately,

\[
\int|\phi_{-k}(x)|\,dx\leq
 \frac{C}{1+k^2}\max_{j=0,2}\sup_{x,u}
 (1+|x|)^4|\partial_u^j\phi(x,u)|.
\tag{9}
\]

The constant is finite because (1+|x|)^(-4) is integrable on R2.
The bound |U_(k,b)|<=H and sum_k(1+k^2)^(-1)<infinity prove
absolute convergence and continuity of (8) in Schwartz seminorms.
This is a tempered distribution, not a pointwise Fourier sum.

For phi compactly supported in x, the classical f_b has the stated
coefficients by compact angular integration. Its u-Fejer sums
converge uniformly on the radial support times T: f_b is uniformly
continuous there, and the positive normalized Fejer kernels have
mass tending to zero outside every angular neighborhood of zero.
Integrating these finite polynomials against phi and using (9)
to pass their weights to one identifies their limit with (8).
Thus T_b agrees with the distribution defined by f_b on every
compact set. This proves the claimed tempered realization. It
does not assert a pointwise growth bound for f_b or h. The index
b!=0 is essential to excluding the unrestricted mean m.

### Detecting a nonzero C0 profile in a compact frequency band

Set U=U_(a,b) and suppose U(t0)!=0. Choose an even smooth compact
sigma with sigma=1 on [-1,1], supported in [-2,2]. Put
eta=Fourier-inverse(sigma), so eta is Schwartz and integral eta=1.
For d>0 write eta_d(t)=d^(-1)eta(t/d).

The following two uniform estimates justify the specific window;
they impose no rate of decay on U. Since U is continuous and tends
to zero at both ends, it is uniformly continuous and bounded.
Consequently eta_epsilon*U tends uniformly to U as epsilon decreases
to zero. Indeed the difference is the integral of
eta(v)[U(t-epsilon v)-U(t)]; split |v| at a fixed large number,
use uniform continuity on the bounded piece and bound the tail by
2||U||_infinity integral_tail |eta|.

Also eta_L*U tends uniformly to zero as L increases. Given delta>0,
choose T so |U(t)|<=delta outside [-T,T]. Then for every t,

\[
|(\eta_L*U)(t)|\leq
 \frac{2T\|\eta\|_\infty\|U\|_\infty}{L}
       +\delta\|\eta\|_1.
\tag{10}
\]

First increase L, then decrease delta. Choose 0<epsilon<L such
that each of these two approximation errors is less than
|U(t0)|/4. Define

\[
\chi(\xi)=\sigma(\epsilon\xi)-\sigma(L\xi),\qquad
V=\eta_\epsilon*U-\eta_L*U.
\tag{11}
\]

Then chi is smooth, compactly supported, zero for |xi|<=1/L,
and |V(t0)|>|U(t0)|/2>0. Each convolution is continuous and C0:
continuity follows from uniform continuity of U and the L1 kernel;
decay follows by dominated convergence in its convolution integral.
Hence V belongs to C0. The imported convolution identity gives
Vhat=chi Uhat. This avoids any assumed pointwise density for Uhat
or an additional theorem about distributions supported at zero.

### Exact index isolation

Choose rho smooth, compactly supported in (-1/3,1/3), with rho(0)=1.
Define

\[
p(\eta_1,\eta_2)=
 \chi(\eta_2/b)\rho(b\eta_1/\eta_2-a)
 \quad(\eta_2\ne0),\qquad p=0\text{ near }\eta_2=0.
\tag{12}
\]

The definitions agree on a full neighborhood of eta2=0 because
chi vanishes near zero. On its support eta2 is bounded and bounded
away from zero, while b eta1/eta2 lies within 1/3 of a. Thus p is
smooth and compactly supported in R2. On every ridge spectral line,

\[
p(k\xi,b\xi)=\chi(\xi)\rho(k-a)
 =\begin{cases}\chi(\xi),&k=a,\\0,&k\ne a.\end{cases}
\tag{13}
\]

The Fourier transform of U_(k,b)(n_k dot x) is supported on
eta=xi n_k. More precisely, its pairing with a radial Schwartz
test psi is 2pi times the pairing of Uhat_(k,b) with
xi -> psi(k xi,b xi). This follows from the tensor-product rule
and the invertible coordinates (x1,t=k x1+b x2); b!=0 makes
their determinant nonzero. Multiplying by p therefore gives the
one-dimensional multiplier p(k xi,b xi) on U_(k,b). Equivalently,
convolution by the Schwartz inverse transform of p gives the same
formula; it is absolutely defined on each bounded ridge function.

The finite angular partial sums in (8) converge in tempered
distributions by (9). Fourier transform and multiplication by this
fixed p are continuous there. Applying them to those sums kills
every k except a by (13). Their limit is exactly (5), with V from
(11). No restriction to a zero fiber was taken during this step.

### What the actual trace says, and what localization changes

At x1=lambda in Lambda and y1=pi, z1 is an actual negative
G-zero. Thus (1)-(2) give q=r=0 for every x2=s,y2=v. Tangential
differentiation gives q_x2=r_y2=0 there, hence h_x2=0 by (2).
For fixed v the C1 trace is therefore constant in s, by the
mean-value theorem. Compact v integration gives (6). This is a
direct consequence of the original constraints, independent of any
moving cutoff or Fourier reconstruction of the lifts.

The localized expression (5) has an ordinary continuous trace
there, namely (-1)^a V(a lambda+b s). Because b!=0, constancy
in s would make V constant on R; its C0 decay would make that
constant zero, contradicting (11). Hence, if this nonzero profile
were admissible, its localization could not preserve (6). To
conclude rigidity one would have to prove preservation from the
remaining actual-F structure, rather than from multiplier calculus.

Here is a direct diagnostic for the operator itself. Let
K=Fourier-inverse(p), a nonzero Schwartz function. It is nonzero
because p is nonzero by (11)-(13) and Fourier inversion is injective.
Fix lambda_* in Lambda. The set where K(lambda_*-x1,-x2)!=0 is
a nonempty open subset of R2. Since Lambda has no finite accumulation,
this open subset contains a point with x1 outside Lambda. Choose
a small open ball D around that point whose x1 projection misses
Lambda and on which |K(lambda_*-x1,-x2)|>=c>0. Choose a nonzero,
nonnegative smooth compactly supported psi in D and set

\[
J=\int |K(\lambda_*-x_1,-x_2)|^2\psi(x)\,dx
       \geq c^2\int\psi>0,\qquad
W(x)=J^{-1}\overline{K(\lambda_*-x_1,-x_2)}\psi(x).
\tag{14}
\]

This W is smooth and compactly supported, and vanishes in a
neighborhood of every zero line. Its convolution with K satisfies

\[
(K*W)(\lambda_*,0)=J^{-1}
  \int |K(\lambda_*-x_1,-x_2)|^2\psi(x)\,dx=1.
\tag{15}
\]

K*W is Schwartz, so its trace tends to zero as |s| increases.
It is consequently not constant. This proves (7), with exact
required value zero versus achieved value one at the selected point.
Multiplying W by e^(iau) gives the identical diagnostic with an
angular trace u=pi, up to the nonzero factor (-1)^a. W does not
satisfy the common ridge relations (3) in general; no h,q,r
satisfying (1)-(3) are constructed by (14). In particular this
diagnostic cannot refute the actual-F implication.

Finally a purely tangential multiplier chi(eta2/b) acts on the
k-th ridge line by chi(xi), for every k, so produces chi(D_t)U_(k,b)
at all those indices. Applied directly to (6), its L1 convolution
annihilates c_lambda because chi(0)=0. This last operation is on
the already restricted constant function. It does not identify it
with the angular trace of a transformed infinite reconstruction:
no bound justifying that restriction/interchange has been proved.
Even if that identity were justified, this multiplier has no
index-selecting factor rho(k-a). The normal factor in (12) is
precisely what supplies that factor and moves off the zero fiber.

For a selected n=(a,0), a!=0, interchange the two coordinate roles
in this test: project first onto angular frequency a in y1, take y2
as the remaining angle, and use the zero fibers x2=lambda,y2=pi.
The fixed nonzero component now plays the role of b, and the retained
index in the other component is zero. The same bound (3), both
closure equations and the symmetric actual coefficient (1) supply
every step. No transposed selected-mean hypothesis is needed: neither
selected mean was used in the localization or tangential constancy
argument. This covers any possible nonzero selected lattice index
without altering the originally fixed ell or either mean condition.

### Decision and remaining gap

The bounded test establishes a legitimate countable distributional
representation and exact spectral isolation, but not an admissible
localized trace. The explicit smooth diagnostic rules out automatic
preservation from the zero-fiber constraints alone. Stop this
spectral mechanism without adding a sampling theorem, a uniform
tail, lift growth or a presumed trace-preserving reconstruction.
This is different from L872's finite-cutoff moving-limit error.
It is not a theorem that every possible use of radial frequencies
fails: new actual-F compatibility controlling the localized trace
would be materially new input requiring its own assessment.

No radial-mean classification, bound K>=-|M|, graph realization,
Xi sign or all-degree mixed positivity is obtained. All full-class
constraints in the hypotheses remain unresolved in this respect.
The outcome is an operation-level negative result, not a resolution
of the main gap or a claim beyond the inspected general sources.

### Separate conceptual audit, 6 November 2026

The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-11-06-l873-operational-claims-conceptual-audit.md`.
This audit reproduces the existing argument and checks its exact scope;
it neither changes the hypotheses nor adds an actual-F counterexample.
The primary Fourier, approximate-identity and classical-calculus inputs
specified above and in that assessment are reused. The precise Fourier
imports are Dyatlov's Proposition 11.23, equations (11.38)-(11.39) and
Proposition 11.25/proof, printed pp128-129. The explicit checks below are
needed for this countable family and these conventions, rather than a
reproof of those general theorems. No mathematical defect was found.

**Reconstruction and topology.** Use bilinear distributional pairing,
with normalized integration in u. For k!=0, twice integrating the
periodic Fourier coefficient by parts bounds its absolute value by
k^(-2) sup_u |partial_u^2 phi(x,u)|. For k=0 use sup_u |phi|.
Integration against (1+|x|)^(-4) gives (9). If P(phi) denotes the
seminorm on its right, the discarded part of (8) obeys

\[
 |\langle T_b-T_{b,N},\phi\rangle|
 \leq CH P(\phi)\sum_{|k|>N}(1+k^2)^{-1}\longrightarrow0.
 \tag{16}
\]

The estimate is uniform on bounded sets of Schwartz tests, so even
strong tempered-distribution convergence holds. For each compact radial
set Q, f_b is continuous on Q times T, hence bounded and uniformly
continuous there. The positive Fejer kernels give uniform convergence
on that product by splitting a small angular neighborhood from its
complement. Testing these finite sums and using (9) with their weights
bounded by one gives precisely (8). This identifies T_b with the
classical f_b locally and proves its tempered realization globally.
No unbounded radial uniformity or trace of the series is used. Since
b!=0, even k=0 is a bounded nonzero angular mode; m never enters.

**Bandpass and regularity.** C0 continuity implies uniform continuity
and boundedness of U on R. The L1 Schwartz kernel eta therefore gives
the uniform small-scale approximation, while (10) proves the large-scale
convolution tends uniformly to zero without a rate for U's tail. Choose
epsilon and L with epsilon<L and both errors strictly below |U(t0)|/4.
Then |V(t0)|>|U(t0)|/2. Dominated convergence applied to
integral eta_d(v) U(t-v) dv proves decay at either end for fixed d;
uniform continuity proves continuity. Thus V is nonzero C0.
These statements concern functions even if Uhat is only a distribution.
In particular chi cannot vanish identically. The neighborhood on which
chi=0 makes (12) smoothly zero across eta2=0; its other support bounds
make p compact. At (a*xi,b*xi), p=chi(xi), so p is nonzero as well.

**Exact Jacobian and multiplier action.** For every integer k and either
sign of b, write

\[
 A=\begin{pmatrix}1&0\\ k&b\end{pmatrix},\qquad
 (s,t)=Ax,\qquad |\det A|=|b|,
 \qquad U(kx_1+bx_2)=(1\otimes U)(Ax).
\]

The Fourier transform of 1 tensor U in (s,t) is 2pi delta_0 tensor
Uhat. The linear-change formula gives |b|^(-1) times its pullback by
A^(-T). When paired with a Schwartz psi, that pullback contributes
|b| and evaluates psi at A^T(0,xi)=(k*xi,b*xi). Hence exactly

\[
 \left\langle\mathcal F_x[U(kx_1+bx_2)],\psi\right\rangle
   =2\pi\left\langle\widehat U,
                     \xi\mapsto\psi(k\xi,b\xi)\right\rangle.
 \tag{17}
\]

Restriction of psi to this nonzero line is Schwartz since b!=0.
Replacing psi by the pointwise product p psi in (17) multiplies Uhat
by p(k*xi,b*xi).
Equation (13) is an identity of smooth functions on the entire line,
including its zero neighborhood; it is therefore valid for arbitrary
Uhat, without a density or an origin-supported remainder. Fourier
transform, multiplication by p and inverse transform are continuous
on the mixed Schwartz-distribution space. Apply them to (16): once
N>=|a| the transformed sum has exactly its a term. The limit is (5),
with no determinant factor left over and no angular restriction taken.

**Classical trace and the diagnostic's quantifiers.** L871's zero
construction uses Hardy infinitude and the entire nonzero G, without
its later finite-support assumption. The coordinate specialization
a=-4*gamma^2 and logarithmic change preserve absence of finite
accumulation. Thus Lambda is closed and discrete in R and unbounded
above. At any one lambda in Lambda, actual-F domination gives q=r=0
for every s,v. Only tangential derivatives q_x2 and r_y2 are set to
zero. The second closure equation then gives h_x2=0; the real C1
mean-value theorem on any finite s interval and compact v integration
prove (6). No normal derivative or distributional pullback is invoked.
The trace of the already isolated continuous function is
(-1)^a V(a*lambda+b*s). Since b!=0, constancy on this line would
make V constant everywhere, and C0 would force V=0.

Fix the particular nonzero p already constructed and then any chosen
lambda_* in Lambda. Its inverse transform K is nonzero Schwartz. The
open nonvanishing set of K(lambda_*-x1,-x2) cannot lie in Lambda times
R, since this latter set has empty interior. Choose a point in that
nonvanishing set with x1 outside Lambda.
Closedness of Lambda and continuity of K give a ball whose projected
closure avoids Lambda and on which |K|>=c>0. A nonzero nonnegative
smooth bump psi with compact support in that ball gives finite J>0
in (14). Its W is complex C_c^infinity, with all zero-line traces zero.
Convolution has no extra (2pi) factor because K is the inverse
transform of p with the stipulated normalization. Thus (15) is exactly
one. Both K and W are Schwartz, so K*W is Schwartz: differentiation
under the convolution and each polynomial weight are controlled by
their Schwartz seminorms (or by the compact support of W). Its selected
line trace tends to zero at both ends and cannot be constant. W may
depend on p and lambda_*; no single W works at all selected points by
assertion, and no admissible triple or common ridge family is inferred.

**Tangential filtering and the coordinate swap.** The inverse kernel
of eta2 -> chi(eta2/b) in the x2 variable is |b| eta_chi(b*x2),
where eta_chi is the one-dimensional inverse transform of chi. It is
L1 and has integral chi(0)=0. It annihilates each already restricted
constant c_lambda and acts by chi(xi) on every ridge index k, without
selecting a. These facts do not commute the infinite reconstruction
with angular restriction. For n=(a,0), a!=0, interchange the two radial
and angular coordinates; the fixed nonzero frequency is a and the
selected remaining index is zero. The symmetric F, uniform bound on
all nonzero modes, and the j=1 closure equation give the same proof.
No transposed mean or additional hypothesis is required.

All three operational conclusions pass. The exact generic discrepancy
is still required zero versus achieved one in (15). This validates
the partial result locally, not a new sign theorem beyond the sources
checked. L872's moving-error estimate remains unproved, and an
actual-F-specific preservation result is neither assumed nor refuted.
The spectral shortcut stays parked at that precisely stated gap.

## Mathlib

Full matching and supporting Mathlib coverage has not been checked;
no absence claim is made. This is an informal Fourier calculation
with precise imported inputs, not Lean verification. The symbolic
certificate (14)-(15) requires no mathematical script or numerics.
