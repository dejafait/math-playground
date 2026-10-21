# L044 — The companion's boundary covariance correction vanishes at a² scale

## Hypotheses

Use L043's exact SU(2), fixed-box, straight-forest setting and its
ordinary dimensionless transverse matrices on the interior vertices
of (-4,4)^3, with a=8/N. Retain all pinned end edges. Let
Delta=Delta_3, G=Delta^(-1), A=bar A and F_i=N diag(P_i), for the
two original probes i=3,6 at tau=1/16. L043 supplies the uniformly
bounded smooth coefficient extensions, the uniformly bounded C²
extensions of F_i, and the compact support of all nonzero rows and
columns of A a fixed positive physical distance from the faces.
Use L041's form estimate |<x,A y>| <= C ||x||_E ||y||_E, where
||x||_E²=<x,Delta x> includes every edge to a pinned vertex.

Let g be L043(5)'s infinite-lattice Green kernel, b0=g(0),
G_infinity its restriction to the finite interior, and
D=G_infinity-G. All matrices here are at fixed mesh before taking
a limit. The positivity D>=0 and harmonicity of D on interior rows
are those proved in L043, not a continuum boundary assumption.

## Conclusion

For each fixed compact K contained in the open transverse cube,

\[
 \epsilon_a(K):=\max_{x_v\in K}D_{vv}\longrightarrow0.
                                                        \tag{1}
\]

In particular the physical-boundary correction to the first term of
L043(4) satisfies, for both probes,

\[
 \operatorname{Tr}(M_{F_i}A D)=o(a^{-1}),\qquad
 a^2N\operatorname{Tr}(M_{F_i}A D)\longrightarrow0.       \tag{2}
\]

Consequently that complete weighted-trace term has the reduction

\[
 a^2N\operatorname{Tr}(M_{F_i}A G)
 =\frac{a^2N}{12}\sum_v F_i(v)
       \sum_{j=2}^4(\Delta_j\bar w_j)(v)+o(1).           \tag{3}
\]

This removes only the boundary covariance correction to that term.
It gives no rate for (1) or (2), no value for the remaining sum in
(3), and no limit or value for the full a²-scaled companion. The
other two sums of L043(4), cancellation against L030/L039, subleading
powers and logarithms, other plaquettes and nonlinear jets, L019
compensation and the reflected-error threshold c_box/2 remain open.
It supplies neither a continuum Yang–Mills construction nor a mass gap.

## Proof

### 1. Approximate the monopole in energy, without assuming it is in l²

Use normalized Lebesgue measure dtheta/(2pi)^3 on [-pi,pi]^3 and
lambda(theta)=sum_j(2-2 cos(theta_j)). L043 proves
b0=integral 1/lambda < infinity. For finite real sequences h on Z³,
Fourier inversion, Plancherel and completion of the square give

\[
 b_0-\{2h(0)-\|h\|_E^2\}
   =\int\lambda\left|\widehat h-\lambda^{-1}\right|^2.
                                                        \tag{4}
\]

The integrals are finite: the cross term is integrable since h has
finite support, and the last term is 1/lambda. A Fourier convention
with hat h(theta)=sum_n h(n) exp(-i n dot theta) makes
h(0)=integral hat h; its real part is sufficient in (4).

We show that the right side can be made arbitrarily small by finite
h. For m>0 put hat k_m=(lambda+m)^(-1). This is bounded on the
torus, hence k_m is a real l² sequence. Moreover

\[
 \int\lambda\left|\widehat k_m-\lambda^{-1}\right|^2
 =\int\frac{m^2}{\lambda(\lambda+m)^2}\longrightarrow0. \tag{5}
\]

Indeed the integrand is at most 1/lambda and tends to zero except
at the single point lambda=0, a null set. Dominated convergence
applies. For fixed m truncate k_m to finite lattice cubes to obtain
real finite sequences h. They converge to k_m in l², and since
0<=lambda<=12 they also converge in the Fourier energy norm.
The triangle inequality in L²(lambda dtheta) and (5) prove that
the right side of (4) tends to zero along suitable such finite h.
This is an explicit energy approximation, not an l² truncation
of g itself; the infinite monopole need not be in l².

### 2. Translate a finite approximation into the pinned cube

For a source delta_v, the finite variational identity used in L043 is

\[
 G_{vv}=\sup_{f\text{ supported on the finite interior}}
          \{2f(v)-\|f\|_E^2\}.                         \tag{6}
\]

Here f is extended by zero to Z³. Its infinite-lattice energy is
exactly the finite Dirichlet energy, including edges to pinned
vertices. This follows by completing the finite positive quadratic
form, whose unique optimizer is G delta_v.

Fix eta>0. Choose the finite h in section 1 so that the right side
of (4) is less than eta, and fix its support radius R. For x_v in a
fixed compact K, the lattice distance from v to every pinned face
tends uniformly to infinity as a tends to zero. Thus the translated
h(n-v) is an admissible trial function in (6), simultaneously for
all these vertices, for every sufficiently small a. Translation
preserves energy. Hence, using L043's D>=0,

\[
 0\le D_{vv}=b_0-G_{vv}
 \le b_0-\{2h(0)-\|h\|_E^2\}<\eta.                   \tag{7}
\]

This proves (1). No Green decay estimate or exchange of continuum
and infinite-volume limits is used. Positivity also gives the
covariance Cauchy–Schwarz inequality

\[
 |D_{vw}|\le\sqrt{D_{vv}D_{ww}}\le\epsilon_a(K)
 \quad(x_v,x_w\in K).                                \tag{8}
\]

### 3. Upgrade the harmonic cutoff estimate by the small covariance

Choose a fixed smooth cutoff chi, compactly supported in the open
transverse cube, equal to one on every nonzero row and column of A
and their neighbors for all sufficiently small a. Choose a larger
fixed compact K containing supp chi and a fixed neighborhood of it.
Every endpoint of an edge with a nonzero chi value or nonzero chi
difference then lies in K for sufficiently small a. Write
epsilon_a=epsilon_a(K), which tends to zero by (1).

Realize the positive semidefinite matrix D as the covariance of a
finite centered real Gaussian vector f. As in L043, Delta f(v)=0
almost surely on the full interior rows meeting supp chi: every
such row has (Delta D)(v,y)=0 for all interior y, so the variance
of Delta f(v) is zero. The finite collection of identities holds
simultaneously. Extend f by zero to pinned vertices and put h=chi f.
L043's exact full-edge identity is

\[
 \|h\|_E^2=\langle\chi^2f,\Delta f\rangle
   +\sum_{(v,w)}(\chi(v)-\chi(w))^2 f(v)f(w).           \tag{9}
\]

The first term is zero. Taking expectations in the second, bounding
the absolute value of each covariance by (8), and using
|chi(v)-chi(w)|<=C a and O(a^-3) edges gives

\[
 E\|h\|_E^2\le C\epsilon_a a^{-1},\qquad
 E\|h\|_2^2\le C\epsilon_a a^{-3}.                   \tag{10}
\]

The second estimate follows directly from E f(v)^2=D_vv. No
off-diagonal sign assumption occurs. The bounded value and first
physical derivative of F_i give the edge product estimate

\[
 \|F_i h\|_E^2
   \le C_i(\|h\|_E^2+a^2\|h\|_2^2),
 \qquad E\|F_i h\|_E^2\le C_i\epsilon_a a^{-1}.       \tag{11}
\]

This holds also at pinned endpoints by zero extension. Since chi=1
on both the row and column supports of A, L041's bilinear form
estimate, followed by expectation Cauchy–Schwarz, implies

\[
\begin{split}
 |\operatorname{Tr}(M_{F_i}A D)|
 &=|E\langle F_i f,A f\rangle|
  =|E\langle F_i h,A h\rangle|\\
 &\le C(E\|F_i h\|_E^2)^{1/2}(E\|h\|_E^2)^{1/2}
 \le C_i\epsilon_a a^{-1}=o(a^{-1}).                 \tag{12}
\end{split}
\]

The first equality follows directly from E f_v f_w=D_vw and
symmetry of D. With N=8/a, its a²N multiple is at most
8 C_i epsilon_a, proving (2). All edges remain in (9); compactness
is used to control the coefficients and cutoff, not to discard
physical-boundary rows of the original Green inverse.

Finally G=G_infinity-D and L043(8)'s exact infinite diagonal
(A G_infinity)_vv=(1/12)sum_j Delta_j bar w_j(v) give (3).
The sign of this retained finite sum is not assigned here.

### 4. Scope, source reuse and the remaining test

Reuse the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`. Its supporting bulk
flow input is Lüscher–Weisz, *Perturbative analysis of the gradient
flow in non-abelian gauge theories*,
[arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2), sections
7.1–7.4, equations (7.1)–(7.8), and section 8.2. Its ordinary
renormalization and R⁴ hypotheses do not supply this finite-box
unflowed estimate, and its general flow theorem is not reproved.
The specialization above uses elementary Fourier energy completion,
dominated convergence, a finite variational formula and L043's
already established covariance cutoff argument. This is local
standard-method progress, classified REPRODUCTION, with no claim
of originality beyond the sources checked. No numerical certificate
or finite-mesh extrapolation is needed for the qualitative limit.

The vanishing in (2) is not vanishing of the full companion. In
particular it says nothing about R=G A G on its diagonal or neighbor
entries. L043(4)'s other products still require their own justified
scaled limits with all end edges, signed weights and both probes.
Only after combining these with (3) can one compare the companion
coefficient with +48 I_i. Neither that value nor cancellation is
assumed. An o(a^-2) discarded term here can still contain a slower
power or a logarithm in the unscaled response.

## Mathlib

Coverage of the full fixed-box scaled boundary-covariance statement:
**not checked**. Coverage of supporting lattice Fourier energy
approximation, variational Green identities, covariance ordering and
discrete cutoff estimates: **not checked**. No matching Mathlib
theorem is asserted; unknown coverage is not evidence of absence.
