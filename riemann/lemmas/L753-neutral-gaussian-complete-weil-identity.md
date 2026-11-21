# L753: Complete neutral Weil identity under Gaussian test smoothing

## Hypotheses

Let f belong to C_c^infinity(R;C), and assume the two exact conditions

\[
 \int_{\mathbb R}e^{x/2}f(x)\,dx
 =\int_{\mathbb R}e^{-x/2}f(x)\,dx=0.                 \tag{1}
\]

For tau>0 set G_tau(x)=(4 pi tau)^(-1/2)exp(-x^2/(4tau)),
f_tau=G_tau*f, and f_0=f. Fix any finite T>0. Derivatives at zero
below are right derivatives. Write

\[
 \begin{split}
 F(z)&=\int f(x)e^{-izx}\,dx,& F^\#(z)&=\overline{F(\bar z)},\\
 \widetilde f(x)&=\overline{f(-x)},& c&=f*\widetilde f,\\
 c_\tau&=f_\tau*\widetilde{f_\tau},&
 H_\tau(z)&=e^{-2\tau z^2}F(z)F^\#(z),\\
 m(u)&=\Re\psi(1/4+iu/2)-\log\pi,&
 z_\rho&=(\rho-1/2)/i.
 \end{split}                                               \tag{2}
\]

Here psi is the digamma function. Every nontrivial zeta zero rho is
included with its multiplicity. L018 identifies these z_rho with the
zeros of Xi and gives |Im z_rho|<1/2. L024 gives reciprocal-square
summability over these zeros, without assuming they are real.

The external inputs are imported, not reproved:

- E. Carneiro and M. B. Milinovich, *On Littlewood's estimate for the
  modulus of the zeta function on the critical line*,
  [arXiv:2403.17803v1, Section 2.2, Lemma 4](https://arxiv.org/html/2403.17803v1#S2.SS2),
  the unconditional Guinand-Weil formula. Its hypotheses are analytic
  continuation to |Im z|<=1/2+epsilon for some epsilon>0 and uniform
  O((1+|z|)^(-1-delta)) decay on that strip, for some delta>0.
  It uses exp(-2 pi i u xi) as its Fourier convention and attributes
  its proof to Iwaniec--Kowalski, *Analytic Number Theory* (2004),
  Theorem 5.12. The book proof is not independently reproduced.
- J. K. Hunter, *Notes on Partial Differential Equations*,
  [revision 18 June 2014, Proposition 5.3 and Theorem 5.4, printed
  pp.129-130](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf#page=135):
  Schwartz initial data have a C^infinity([0,infinity);S) heat
  evolution, Gaussian convolution and multiplier exp(-tau u^2).
  Apply the real-data statement separately to real and imaginary
  parts. Exponential weights are verified below, not inferred from
  Schwartz convergence.
- Fourier convolution/inversion, the Gaussian exponential integral,
  dominated convergence, and the fundamental theorem of calculus.
  For m use L744(8)'s bound |m(u)|<=C+log(2+|u|), obtained there
  from [DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2) and its sector
  remainder. L744(6) is used only for the compact initial comparison.

The previously saved SPECIALIZE assessment is
`drafts/literature/2026-11-04-neutral-gaussian-domain-differentiation.md`.
This is a standard specialization/REPRODUCTION, not a mathematical
novelty claim. The full-line pairing is defined by the formula below;
no positive-time extension of a finite-window generator is assumed.

## Conclusion

Both exponential moments of f_tau vanish for every tau>=0. The real
full-line pairing

\[
 \begin{split}
 \mathcal E_f(\tau)
 &=\int_{\mathbb R}m(u)|F_{f_\tau}(u)|^2\frac{du}{2\pi}
   -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                    [c_\tau(\log n)+c_\tau(-\log n)]\\
 &=\sum_\rho H_\tau(z_\rho)                             \tag{3}
 \end{split}
\]

is C^2 on [0,T]. For j=0,1,2 its derivatives satisfy the complete
identities

\[
 \begin{split}
 \mathcal E_f^{(j)}(\tau)
 &=\sum_\rho(-2z_\rho^2)^j H_\tau(z_\rho)\\
 &=\int_{\mathbb R}m(u)(-2u^2)^j H_\tau(u)\frac{du}{2\pi}
 -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,2^j
       [\partial_x^{2j}c_\tau(\log n)
        +\partial_x^{2j}c_\tau(-\log n)].                 \tag{4}
 \end{split}
\]

All displayed series converge absolutely and uniformly for
tau in [0,T]; all integrands have uniform integrable absolute
majorants. In particular (3)-(4) have the stated right limits at
zero, with no omitted arithmetic tail. At tau=0, after translating
the compact support into any sufficiently large fixed (0,L),
mathcal E_f(0) equals L744(6)'s neutral compact energy E_L.

No nonnegative sign for (3), derivative sign, starting sign,
backward comparison, uniformity over f or unbounded times, or RH
consequence is asserted. This is a local domain-and-differentiation
input, not a resolution of complete neutral positivity.

The independent conceptual audit of 4 November 2026 (step 329) accepts
this fixed-f, fixed-[0,T] conclusion, including complex tests and both
right derivatives at zero. Section 5 records its checks. No statement,
constant or mathematical input required correction. This validates a
known-formula specialization locally; it claims no advance beyond the
checked source mathematics and no sign result.

## Proof

### 1. Weighted heat evolution and exact neutrality

For b>=0 put ||g||_(1,b)=integral exp(b|x|)|g(x)|dx. For every
compact smooth g and every tau in (0,T], absolute Fubini and
exp(b|x+y|)<=exp(b|x|)exp(b|y|) give

\[
 \|G_\tau*g\|_{1,b}
 \le 2e^{Tb^2}\|g\|_{1,b},                              \tag{5}
\]

because integral exp(b|u|)G_tau(u)du<=2exp(tau b^2).
The factor two is harmless also at tau=0. This applies to every
spatial derivative of f or c, all of which are compact smooth.

These convolutions are continuous at zero in this weighted L1 norm.
Indeed weighted translations of a compact smooth g are continuous,
and

\[
 \|g(\cdot-u)-g\|_{1,b}\le (e^{b|u|}+1)\|g\|_{1,b}.
\]

Write the convolution difference as the integral of these
translations with u=sqrt(tau)v and measure G_1(v)dv. The displayed
bound is dominated, for tau<=T, by
2exp(b sqrt(T)|v|)||g||_(1,b), integrable against G_1.
Dominated convergence proves the assertion. At positive times,
continuity follows directly from continuity of G_tau in weighted
L1: on a neighborhood of any tau_0>0 its kernels are bounded by a
fixed Gaussian times exp(b|u|). Weighted convolution then preserves
that continuity.

Hunter's theorem gives the heat identity in S. In particular,
pointwise,

\[
 G_\tau*g-g=\int_0^\tau G_s*g''\,ds.                    \tag{6}
\]

The weighted bounds (5) make the right side absolutely integrable
in (s,x), and the weighted continuity just proved makes it a
weighted-L1 continuous integral. Thus (6) also proves weighted
differentiability at zero and at every positive time. Iterating
with g'', g'''' gives two weighted continuous time derivatives,
respectively G_tau*g'' and G_tau*g''''. The same reasoning applies
to the time parameter 2tau, with its corresponding factors of two.

For any real a, (5) justifies absolute Fubini in the moment integral:

\[
 \int e^{ax}f_\tau(x)\,dx
 =e^{\tau a^2}\int e^{ay}f(y)\,dy.                      \tag{7}
\]

The Gaussian exponential integral gives the first factor, including
its normalization. Taking a=+/-1/2 proves exact neutrality, with
two continuous derivatives also justified by the weighted result.
At tau=0 the identity is immediate.

For every fixed complex z, absolute Fubini with b=|Im z| likewise
gives the entire Fourier transform

\[
 F_{f_\tau}(z)=e^{-\tau z^2}F(z).                       \tag{8}
\]

Entirety can also be checked by differentiation under the integral:
on each compact set of z the polynomial factors in x are dominated
by a slightly larger exponential weight. Reflected conjugation
in (2) is holomorphic. Consequently H_tau=F_(f_tau)F_(f_tau)^#,
and H_tau(u)=|F_(f_tau)(u)|^2 only when u is real. At the poles,

\[
 H_\tau(i/2)
   =F_{f_\tau}(i/2)\overline{F_{f_\tau}(-i/2)}=0,
 \qquad H_\tau(-i/2)=0.                               \tag{9}
\]

Their first two time derivatives vanish as well. No pole is dropped
before this exact calculation.

### 2. Uniform strip bounds and the complete zero sum

Choose R>=1 with supp(f) contained in [-R,R]. For integer N>=0
and b>=0, integration by parts in the compact integral for F gives

\[
 |F(x+iy)|\le A_{N,b}(1+|x|)^{-N}\quad(|y|\le b),
 \quad
 A_{N,b}=2^N e^{Rb}(\|f\|_1+\|f^{(N)}\|_1).             \tag{10}
\]

For |x|>=1 use (iz)^N F(z)=integral f^(N)(v)exp(-izv)dv;
there are no boundary terms and |z|>=|x|. For |x|<=1 use the
L1 bound and (1+|x|)^N<=2^N. These prove (10), also at z=0.
The same bound holds for F^# on this symmetric strip.

For j=0,1,2, differentiation of the explicit entire expression gives

\[
 \begin{split}
 \partial_\tau^j H_\tau(z)&=(-2z^2)^j H_\tau(z),\\
 |\partial_\tau^j H_\tau(x+iy)|
 &\le 2^j(1+b)^{2j}e^{2Tb^2}A_{N,b}^2
                 (1+|x|)^{2j-2N}.                       \tag{11}
 \end{split}
\]

Here |exp(-2tau z^2)|=exp(-2tau x^2+2tau y^2)<=exp(2Tb^2)
and |z|<=(1+b)(1+|x|). Choose N=j+2. The power is -4, so
every differentiated test meets Lemma 4's analytic-strip decay
hypothesis, for example with b=1 and epsilon=1/2. There is no
uniformity claim in b, N, T or f.

For zeros use b=1/2. Since |Im z_rho|<1/2,
(1+|Re z_rho|)^(-4) is bounded by a constant multiple of
(1+|z_rho|)^(-4). L024 supplies sum_rho |z_rho|^(-2)<infinity;
the finite head and comparison of these powers therefore give a
summable majorant in (11) for each j<=2. This controls every zero
with multiplicity, including all complex ordinates.

The Weierstrass majorant test and dominated convergence show uniform
absolute convergence and continuity of all three zero-side series.
Applying the fundamental theorem of calculus to individual terms
and interchanging its bounded time integral with these uniformly
summable series proves termwise differentiation twice, including
the right derivatives at zero. No ordering-dependent zero limit is
needed. The bound on m from the hypotheses and (11) similarly
dominate every gamma/scalar integral by
C(1+|u|)^(-4)(1+log(2+|u|)), integrable on R. The same integral
argument justifies its two time derivatives.

### 3. Spatial convolution and complete prime-power domination

The real even heat kernel commutes with reflected conjugation.
Fourier convolution, or absolute spatial Fubini and the Gaussian
semigroup law, gives

\[
 c_\tau=G_{2\tau}*c,\qquad
 \partial_\tau^j c_\tau
   =2^jG_{2\tau}*c^{(2j)}
   =2^j\partial_x^{2j}c_\tau\quad(j=0,1,2),              \tag{12}
\]

with c_0=c and the corresponding compact derivatives at zero.
Hunter's theorem applied to c proves these pointwise identities
and continuity, including zero; Section 1 also gives weighted
versions. Every function here is Schwartz. In particular Fourier
inversion and (8) give

\[
 c_\tau(a)=\int H_\tau(u)e^{iua}\frac{du}{2\pi}.
                                                               \tag{13}
\]

It remains essential to dominate values at all log n uniformly
down to zero; pointwise convergence or Schwartz control alone
would not establish that arithmetic assertion.

Put A=2R, so all c^(2j) are supported in [-A,A]. If
|x|>=A+1, write d=|x|-A>=1. For |y|<=A and s=2tau in (0,2T],

\[
 \begin{split}
 G_s(x-y)
 &\le(4\pi)^{-1/2}s^{-1/2}
                e^{-d^2/(8s)}e^{-d^2/(8s)}\\
 &\le(\pi e)^{-1/2}e^{-d^2/(16T)}.                      \tag{14}
 \end{split}
\]

The last bound uses sup_(s>0) s^(-1/2)exp(-1/(8s))=2/sqrt(e)
and s<=2T. Thus with

\[
 \begin{split}
 B_j&=2^j\max\{\|c^{(2j)}\|_\infty,
                         \|c^{(2j)}\|_1/\sqrt{\pi e}\},\\
 w_T(x)&=\begin{cases}
           1,&|x|\le A+1,\\
           \exp(-(|x|-A)^2/(16T)),&|x|>A+1,
         \end{cases}
 \end{split}
\]

the contraction bound for convolution by a probability kernel on
the inner region, and (14) on the outer region, prove

\[
 |\partial_\tau^j c_\tau(x)|\le B_j w_T(x)
          \quad(0\le\tau\le T,\ j=0,1,2).                \tag{15}
\]

At zero the outer values are exactly zero, so this same majorant
holds there. For log n>=max{2A,A+1,128T},

\[
 (\log n-A)^2/(16T)\ge(\log n)^2/(64T)\ge2\log n.
\]

Consequently w_T(log n)<=n^(-2) in this tail. Using
0<=Lambda(n)<=log n gives the explicit summable domination

\[
 \frac{\Lambda(n)}{\sqrt n}
 |\partial_\tau^j c_\tau(\pm\log n)|
 \le B_j\frac{\log n}{n^{5/2}}                          \tag{16}
\]

there; the remaining finite head is bounded by (15). This proves
absolute uniform convergence of the complete arithmetic sums and
their two derivative series. Applying the fundamental theorem of
calculus as in Section 2 proves termwise differentiation and the
right limits at zero. All prime powers occur. The finite head in
this domination argument is not an arithmetic cutoff in (3)-(4).

### 4. Importing the formula, normalization and initial comparison

For clarity, Lemma 4 in its own Fourier convention is

\[
 \begin{split}
 \sum_\rho h(z_\rho)
 &=h(i/2)+h(-i/2)
   -\frac{\log\pi}{2\pi}\widehat h(0)
   +\frac1{2\pi}\int h(u)\Re\psi(1/4+iu/2)\,du\\
 &\quad-\frac1{2\pi}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
    [\widehat h(\log n/(2\pi))
      +\widehat h(-\log n/(2\pi))],\\
 \widehat h(v)&=\int h(u)e^{-2\pi iuv}\,du.              \tag{17}
 \end{split}
\]

Sections 1-2 verify its hypotheses for H_tau and each of its two
time derivatives, even at zero. Formula (13) shows explicitly

\[
 \widehat {H_\tau}(\pm a/(2\pi))=2\pi c_\tau(\mp a).
                                                               \tag{18}
\]

For the differentiated tests the same relation holds after j time
derivatives, justified by (11)-(13). Combine the scalar term with
the gamma integral to obtain exactly m(u); its coefficient is
du/(2pi). Substitute (9) and (18) in (17) to obtain (3).
All three pairings have the justified differentiated limits proved
above, yielding (4). Equivalently one can apply (17) directly to
each differentiated test; both arguments retain its zero poles.

For complex f, c_tau(-a)=overline(c_tau(a)), while H_tau is real
on the real line. Thus the arithmetic and gamma expressions in
(3) are real. On the zero side this also follows from the
conjugation invariance of Xi's zero multiset (L018),
H_tau(bar z)=overline(H_tau(z)), and absolute convergence. This
uses no real-zero or positive-measure assumption. In particular
nonnegativity of H_tau on the real line is not a sign argument for
its values at nonreal z_rho.

Finally translate f into some fixed (0,L), writing g(x)=f(x-b).
Its two moments are multiplied by e^(+/-b/2) and remain zero.
F_g(z)=e^(-ibz)F(z), so F_g F_g^#=F F^#; its autocorrelation
and real-frequency modulus square are unchanged. L744(6) therefore
applies at zero. Its pole product vanishes by (1). With the
first-slot-linear inner product and the delay T_a of L744,

\[
 \langle T_a g,g\rangle=c(-a),\quad
 \langle(T_a+T_a^*)g,g\rangle=c(-a)+c(a).
\]

The compact correlation is zero for |a|>=L. Thus its finite delay
sum equals the full arithmetic sum at tau=0, including the zero
endpoint contribution, and E_L(g)=mathcal E_f(0). At positive
times use (3), with its full infinite sum, rather than extending
that finite-window identity. This completes the specialization.

### 5. Independent conceptual audit of the specialization

The audit uses the previously saved SPECIALIZE scope in
`drafts/literature/2026-11-04-neutral-gaussian-identity-audit.md`.
The following checks concern the applicability of the imported theorems,
not new proofs of those theorems or an extension of the conclusion.

**Complex tests and the source formula.** Direct comparison with
Carneiro--Milinovich v1, Section 2.1 and Lemma 4, confirms the Fourier
convention and every term of (17). Lemma 4 is unconditional and imposes
neither evenness nor reality of h. Its entire printed proof attributes
the formula to Iwaniec--Kowalski Theorem 5.12; that attribution is not
an independent audit of the book proof. The neighboring RH-dependent
Lemma 5 is not used. For the present test,
F^#(z)=integral overline(f(x)) exp(izx) dx is entire and is the
Fourier transform of tilde f. Thus the product is the transform of
the autocorrelation, with no conjugation of the complex ordinate.
At i/2 its factors are the +1/2 moment and the conjugate of the
-1/2 moment. At -i/2 their roles reverse. Equations (7)-(9) pay
both pole evaluations and their time derivatives exactly. Replacing
this holomorphic product by |F(z)|^2 off the real axis would invalidate
the argument; no such replacement occurs here.

**Weighted endpoints.** The dominating translation bound after (5)
is integrable against G_1 because a Gaussian times any fixed
exp(b sqrt(T)|v|) is integrable. It applies separately to g, g''
and g''''. Equation (6), together with continuity of these three
weighted convolutions, is an identity in the weighted L1 space.
Taking its difference quotient at zero gives g'', and applying it
to g'' gives g'''': no negative-time heat evolution or weighted
conclusion from the unweighted Schwartz theorem is required.
The same argument on a positive-time subinterval gives continuity
and differentiation there. Taking b=1/2 pays the moment functionals;
taking any larger fixed b also pays the polynomial factors needed
for holomorphic differentiation in (8).

**Zero and gamma tails.** One may take the single choice N=4 in
(10)-(11) for all j=0,1,2: the powers are -8,-6,-4, respectively.
For the zero sum take b=1/2, retain exp(2T b^2), and use L018's
strip without imposing Im z_rho=0. L024's sum over paired
representatives becomes the sum over all zeros by a factor two;
all multiplicities are retained. On the strip, (1+|Re z|)^(-4)
is bounded by a constant times (1+|z|)^(-4), whose zero sum is
finite by reciprocal-square summability and the finite compact
head. For source applicability instead take b=1, which gives
epsilon=1/2 and uniform decay stronger than Lemma 4 requires.
L744(8) pays the gamma integral also for bounded u: no singular
log|u| approximation is used near zero. Multiplication by its
logarithmic bound leaves the worst power -4 integrable.

**Complete arithmetic tail.** In (14) the first Gaussian factor
uses d>=1. The function s^(-1/2)exp(-1/(8s)) has its global
maximum 2/sqrt(e) at s=1/4, so its multiplication by
(4pi)^(-1/2) gives exactly 1/sqrt(pi e). The other factor is
at most exp(-d^2/(16T)) for s<=2T. For log n>=2A and
log n>=128T, the exponent in (15) is at least 2 log n.
The additional A+1 threshold ensures that the outer bound applies.
Thus (16) controls both signs of log n and all three derivative
orders by a convergent sum over every integer n>=2, hence over
every prime power. At tau=0 the compact correlation derivatives
are identically zero in the outer region; on the finite head
the same convolution contraction bound holds. There is no
uncontrolled boundary layer as tau decreases to zero. The bound
is for the doubled heat time, so (12) supplies exactly 1,2,4,
not 1,1,1, in the three arithmetic expressions.

For each series in (4), let S_j denote its jth displayed termwise
series. Its continuous individual terms and the uniform majorants
above imply continuity of S_j on [0,T]. Absolute domination pays
the time integral in
S_j(tau)-S_j(0)=integral_0^tau S_(j+1)(s) ds for j=0,1.
The same reasoning applies to the gamma integral. These identities
prove the two right derivatives, not merely their formal expressions
or their convergence along positive times.

**Normalization and compact comparison.** Equation (13) gives
widehat(H_tau)(a/(2pi))=2pi c_tau(-a); multiplying by the source's
1/(2pi) therefore leaves exactly the arithmetic coefficient in
(3). The scalar -log(pi) term joins the gamma integral with
measure du/(2pi). The differentiated transform uses the same
normalization, with factors 2^j partial_x^(2j) from (12).
Real-valuedness follows from c_tau(-a)=overline(c_tau(a)) and
the real gamma symbol. Conjugation symmetry and absolute convergence
give the identical reality conclusion on the zero side, without
making any individual complex-zero contribution positive.
For g(x)=f(x-b), reflected conjugation changes exp(-ibz) to
exp(ibz), so the product and correlation are unchanged. Direct
substitution in the first-slot-linear inner product gives
<T_a g,g>=c(-a). With support strictly inside (0,L), the
correlation vanishes for |a|>=L, including equality. L744(6)'s
pole product is zero and its arithmetic sum is exactly the full
sum at tau=0. Its arbitrary-fixed-L smooth calculation is the
only compact-generator conclusion used.

All acceptance tests are met for the stated family and j<=2.
Constants and the finite arithmetic head depend on f and T;
this audit proves no estimate uniform over initial data or as
T tends to infinity. The identity supplies neither an initial
positive sign nor a backward comparison. The separate absorption
obstruction in L751/L752 is not altered or used as a premise.

## Mathlib

Full matching coverage of this complex neutral Gaussian
Guinand-Weil specialization and its two differentiated complete
pairings has not been checked. Supporting heat/Fourier facts are
used here by the cited mathematical theorems; no matching Mathlib
theorem or absence claim is asserted.
