# L751: Complete killed ground-state specialization and sine midpoint obstruction

## Hypotheses

Put I=(0,L), L=9log3, b=L/2, a=pi/L, and let
h(x)=sin(ax) on I, extended by zero to htilde on R. All other
extensions below are also by zero. Use L744(6)'s smooth energy and
Fourier convention F_f(t)=integral f(x)e^(-itx)dx. Define

\[
\begin{split}
 m(t)&=\Re\psi(1/4+it/2)-\log\pi,\qquad m_0=m(0),\\
 k(u)&=\frac{2e^{-u/2}}{1-e^{-2u}},\quad u>0,\\
 c_n&=\Lambda(n)/\sqrt n,\quad d_n=\log n,\\
 B_L&=\sum_{2\le n<19683}c_n(T_{d_n}+T_{d_n}^*),\\
 Q_0(f)&=\int_{\mathbb R}m(t)|F_f(t)|^2\frac{dt}{2\pi}
                          -\langle B_Lf,f\rangle.
\end{split}                                                     \tag{1}
\]

Here 19683=3^9=e^L, T_d f(x)=1_(x>d)f(x-d), and Lambda is
the full von Mangoldt function. In particular all prime powers,
both adjoints and zero-extension killing are included. The tested
functions are complex f in C_c^infinity(I). For the neutral-energy
consequence require exactly

\[
 M_\pm(f)=\int_I e^{\pm x/2}f(x)dx=0.                       \tag{2}
\]

The reference h is not required or asserted to satisfy (2).
By L744(6), E_L(f)=Q_0(f) when (2) holds, and these smooth tests
belong to L740's actual generator domain. No sign theorem or
domain extension for arbitrary nonsmooth f is assumed.

The standard identity being specialized is Frank and Seiringer,
*Non-linear ground state representations and sharp Hardy inequalities*,
[arXiv:0803.0503v2](https://arxiv.org/pdf/0803.0503v2),
14 November 2008, Assumption2.1, Propositions2.2–2.3 and
Remarks2.4/2.8, pp5–6; the p=2 equality follows from Lemma2.6
and (2.17)–(2.19), pp8–11. We use its domain version and its
two-vertex weighted-graph identity, not a product-Lebesgue density
for a translation atom. Its required cutoffs and energies are
verified below. The scalar evaluation is
[NIST DLMF5.4.19](https://dlmf.nist.gov/5.4.E19), at p=1,q=4;
its applicability and normalization were already checked locally
in L748. No source positivity statement or RH premise is used.

## Conclusion

For every such compact smooth f, with g=f/h on I, the exact identity is

\[
\begin{split}
 Q_0(f)={}&\int_I R_h(x)|f(x)|^2dx\\
 &+\frac12\int_0^L k(u)\int_0^{L-u}
 h(x)h(x+u)|g(x+u)-g(x)|^2dx\,du\\
 &+\sum_{2\le n<19683}c_n\int_0^{L-d_n}
 h(x)h(x+d_n)|g(x+d_n)-g(x)|^2dx,                 \tag{3}\\
 R_h(x)={}&m_0+
 \frac1{2h(x)}\int_0^\infty k(u)
 [2h(x)-\widetilde h(x-u)-\widetilde h(x+u)]du\\
 &-\frac1{h(x)}\sum_{2\le n<19683}c_n
 [\widetilde h(x-d_n)+\widetilde h(x+d_n)],\quad x\in I.
                                                               \tag{4}
\end{split}
\]

Every term of (3) is finite. Its last two lines are nonnegative.
Moreover (4) is exactly the pole-free multiplier residual

\[
 R_h(x)=\frac{(m(D)\widetilde h)(x)-(B_Lh)(x)}{h(x)}.
                                                               \tag{5}
\]

The fixed midpoint has the rigorous one-sided enclosure

\[
 \boxed{\quad R_h(b)<-\frac{73}{162}<0.\quad}                  \tag{6}
\]

Thus this sine fails the sufficient pointwise condition R_h>=0
on I. This is a standard-identity reproduction and an analytic
negative test, not a new general ground-state formula, a negative
neutral-energy witness, or a disproof of RH. The identity and bound
passed the separate conceptual audit recorded below (step322).

## Proof

### Exact multiplier and killing

L744's proof of (5)–(8), using L741's full-line normalization, gives
r(u)=k(u)-e^(-u)/u in L1(0,infinity), with transform

\[
 \widehat r(it)=\log(1+it)-\psi(1/4+it/2)-\log2.
\]

Subtract its real part at t from its value at zero. Adding
integral_0^infinity e^(-u)(1-cos(tu))/u du=log(1+t^2)/2
then yields precisely

\[
 m(t)=m_0+\int_0^\infty k(u)(1-\cos(tu))du.                 \tag{7}
\]

The last elementary integral follows by differentiating in t
under the integrable exponential majorant and integrating
t/(1+t^2) from 0 to t. Thus no new scalar is introduced.
The integrals in (7) converge: k=O(1/u) at zero, while it decays
exponentially at infinity. This also follows from the explicit
bound in (13) below. Plancherel and Tonelli, with k>=0, give

\[
 \int m(t)|F_f(t)|^2\frac{dt}{2\pi}
 =m_0\|f\|_2^2+
 \frac12\int_0^\infty k(u)\int_{\mathbb R}
     |\widetilde f(x+u)-\widetilde f(x)|^2dx\,du.             \tag{8}
\]

For small u the inner integral is at most u^2||f'||_2^2;
for large u it is at most 4||f||_2^2. This verifies finiteness,
including the full exterior part of the quadratic form.
The factor 1/2 in (8) is required because the Fourier symbol of
the squared translation difference is 2(1-cos(tu)).

Splitting (8) into pairs inside I and pairs crossing its boundary
gives a regional pair energy with coefficient k(u)/2 and the
additional multiplication term

\[
 \kappa_I(x)=\frac12\left(\int_x^\infty k(u)du+
                           \int_{L-x}^\infty k(u)du\right).
                                                               \tag{9}
\]

It is locally finite and is never dropped. Its possible endpoint
growth causes no problem for compact smooth tests.

### Applicability of the sourced identity

The reference is positive and smooth on I; g=f/h has compact
support inside I and extends as a smooth compact function on R.
The zero extension htilde is globally Lipschitz, compactly
supported, and in H1(R). It has finite energy in (8), by the
same translation estimates as f. Its weak first derivative is
piecewise smooth with finite variation, so two integrations by
parts, retaining the endpoint derivative jumps, give
|F_htilde(t)|<=C/(1+t^2). L744(8)'s bound
|m(t)|<=C+log(2+|t|) implies m F_htilde is in L1 and L2.
Consequently m(D)htilde has an absolutely convergent Fourier
inverse and is also an L2 multiplier output. No guessed boundary
condition for L740's generator is being imposed on h.

To check the continuous cutoff required by the source, replace
k by k_epsilon=k 1_(u>epsilon). All pair integrals are then
ordinary absolutely convergent integrals. On each compact K
inside I, for u<dist(K,boundary I), the numerator in (4) is
2h(x)(1-cos(au))=O_K(u^2). At larger u, k is integrable away
from zero and htilde is bounded. Hence its cutoff integral
converges uniformly on K. Division by h is bounded on K.
This proves the source's local potential convergence, with
the multiplication term (9) retained.

The cutoff multiplier is m_0+integral_epsilon^infinity
k(u)(1-cos(tu))du. Its absolute value is at most
|m_0|+[m(t)-m_0], and this has logarithmic growth by L744(8).
Multiplication by F_htilde is integrable. Dominated Fourier
inversion therefore identifies its limit uniformly with
m(D)htilde. The locally uniform spatial limit just proved is
the integral in (4), proving the continuous part of (5).
This checks the pointwise match, not merely a formal symbol.
The locally uniform limits and continuous zero-extended shifts
also make R_h continuous on I; the strict midpoint failure
therefore persists on an interior neighborhood.

Apply Frank–Seiringer's p=2 equality on I to the positive
regional kernel, with (9) and m_0 retained as multiplication
terms. The resulting transformed continuous pair term is the
second line of (3). It is integrable: h is bounded, and
integral over R of |g(x+u)-g(x)|^2 is at most
u^2||g'||_2^2 for small u and 4||g||_2^2 otherwise.
The product h(x)h(x+u) only improves this bound. Thus cutoff
energies converge by domination, and the residual term
converges on the compact support of f. These verifications
discharge the sourced identity's p=2 limiting hypotheses;
no unknown eigenfunction or endpoint inverse-domain assertion
is needed. The coefficient remains 1/2 as in (8).

For an arithmetic edge of length d=d_n<L, use the same source's
two-vertex identity and integrate over 0<x<L-d. Explicitly,
for positive H=h(x), K=h(x+d), complex v=g(x), w=g(x+d),

\[
 c_n HK|v-w|^2-c_n[(K/H)|Hv|^2+(H/K)|Kw|^2]
             =-2c_n\Re(Hv\overline{Kw}).                    \tag{10}
\]

The right side integrates to minus the full Hermitian edge
energy. The left side is the last line of (3) and exactly its
arithmetic contribution in (4). This is the scalar p=2
identity, written to verify its complex factors and integration
measure, rather than treating a translation atom as an dxdy
density. All edge integrals are finite since there are only
finitely many n and g is bounded with compact support. This
also verifies potential terms: after multiplication by |f|^2
their quotients are bounded on its support. Edges whose endpoint
leaves I give zero in B_L by zero extension. The continuous
exterior killing remains (9), and both directed arithmetic
shifts remain in (4). A delay exactly L is the zero operator.

Combining the continuous sourced identity and (10) proves
(3)–(5). The reference need not be neutral. For neutral tests
the pole product in L744(6) vanishes exactly by (2), and only
then may E_L be replaced by Q_0. For general tests (3) is an
identity for Q_0 only. If R_h were nonnegative throughout I,
(3) would suffice for nonnegative Q_0 on these compact tests.
No closed-form-domain extension or all-window conclusion is
claimed from this statement.

### Complete midpoint expression and exact negative upper bound

At b, h(b)=1 and htilde(b-u)=htilde(b+u)=cos(au) for
0<=u<b; both values vanish for u>=b, including u=b.
Consequently (4) gives the exact expression

\[
\begin{split}
 R_h(b)={}&m_0+\int_0^b k(u)(1-\cos(au))du
                  +\int_b^\infty k(u)du-S,\\
 S={}&2\sum_{2\le n<19683}c_n\widetilde h(b-\log n)\\
   ={}&2\sum_{2\le n<81\sqrt3}
         \frac{\Lambda(n)}{\sqrt n}\cos(a\log n)\ \ge0.
\end{split}                                                     \tag{11}
\]

The first expression for S retains every prime-power shift in
the complete operator. Its terms at n>=81sqrt3 vanish exactly;
the second expression records this fact without replacing any
nonzero term. Every surviving cosine has argument in (0,pi/2)
and every c_n>=0. Thus S>=0 is a rigorous bound on the entire
finite arithmetic sum, not a prime-only truncation or an
approximate cancellation. We need no upper estimate on S for
this one-sided test. The second integral in (11) is the full
exterior killing at the midpoint, not an optional correction.

Since e^(2u)>=1+2u for u>0,

\[
 \frac1{1-e^{-2u}}=1+\frac1{e^{2u}-1}\le1+\frac1{2u},
 \qquad k(u)\le e^{-u/2}(2+1/u).                            \tag{12}
\]

Using 1-cos v<=v^2/2 and positive integrands, we obtain

\[
\begin{split}
 \int_0^b k(u)(1-\cos(au))du
 &\le\frac{a^2}{2}\int_0^\infty e^{-u/2}(2u^2+u)du
   =18a^2,\\
 \int_b^\infty k(u)du
 &\le(2+1/b)\int_b^\infty e^{-u/2}du
   =(4+2/b)e^{-b/2}.
\end{split}                                                     \tag{13}
\]

The two gamma integrals in the first line are respectively
integral u^2 e^(-u/2)du=16 and integral u e^(-u/2)du=4.
Thus its coefficient is (2*16+4)/2=18, with no numerical
quadrature or tail omission.

For complete elementary bounds use 3<pi<4 and e<3.
The latter follows by summing the exponential series and using
n!>=2^(n-1) for n>=1, with strict inequality for some n.
Hence log3>1, b>9/2 and

\[
 18a^2=\frac{2\pi^2}{9(\log3)^2}<\frac{32}{9},\qquad
 (4+2/b)e^{-b/2}<\frac{40}{9}\frac19=\frac{40}{81},       \tag{14}
\]

where e^(-b/2)=3^(-9/4)<1/9. The strict upper bound on the
two continuous integrals is therefore 328/81.

DLMF5.4.19 at the allowed integers p=1,q=4 yields
psi(1/4)=-gamma-pi/2-3log2: the cotangent is 1,
-log q=-2log2, and only k=2 contributes to the cosine-log
sum, contributing -log2. Harmonic–integral comparison gives
gamma>=0. Also log2=2 integral_0^(1/3) (1-t^2)^(-1)dt>2/3,
pi/2>3/2 and log pi>log3>1. Thus the complete scalar satisfies

\[
 m_0=-\gamma-\pi/2-3\log2-\log\pi<-\frac92.               \tag{15}
\]

Finally (11), (14), (15) and S>=0 give

\[
 R_h(b)<-\frac92+\frac{328}{81}-S
       =-\frac{73}{162}-S\le-\frac{73}{162}<0.
\]

This proves (6) entirely analytically. The required threshold
for this sufficient pointwise test was zero; its achieved
upper bound is strictly below zero. The auxiliary exact-arithmetic
replay is `python3 scripts/sine-supersolution/exact-bounds-320.py`,
with full output in `scripts/sine-supersolution/exact-bounds-320.json`.
It checks the rational arithmetic and integer cutoffs only, not
the analytic hypotheses. No numerical quadrature or residual
preview is part of the proof.

### Qualification of the negative result

A negative residual at this one point rules out this fixed h
as a pointwise supersolution. It does not imply that (3) can
be negative on a neutral f: its transformed remainder can
compensate negative residual, and (2) restricts the tests.
No inference about neutral positivity, the nonneutral
complement, other lengths or actual-Xi mixed signs follows.
There is no endpoint division and no profile-family search.
The earlier L749 direct-payment and L750 corrected-IMS stops
are contrasts, not premises of this argument. Reopening this
pointwise sine implementation requires materially new input;
merely reproducing the ground-state identity is not such input.

### Separate conceptual audit (4 November 2026, step322)

Equations (3)–(6) pass for precisely the stated complex compact
smooth tests. This verifies a local specialization and obstruction;
it is not a new general identity or a neutral sign theorem. The
invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-04-fixed-sine-midpoint-conceptual-audit.md`.
The cited source cases were checked directly against this application;
no additional literature search or enlarged hypotheses were used.

1. **Normalization and domain.** L744(5)–(8) and its separate audit
   give the stated multiplier, pole product and all delays at every
   fixed L. Its verification of L740's domain applies to each tested
   f: the logarithmic convolution derivative is bounded by
   ||f'||_infinity integral_0^L |log u|du. In the transform calculation,
   r-hat(0)-Re r-hat(it) equals
   m(t)-m_0-log(1+t^2)/2. Thus adding the exponential integral
   indeed gives (7), with no scalar or sign change. The reference h
   is used in a full-line multiplier, not asserted to belong to an
   inverse generator domain. Both pole moments vanish for the tested
   neutral f, including complex f; no neutrality of h is needed.

2. **Exact source kernel and killing.** In the source's double-integral
   convention the regional kernel is K(x,y)=k(|x-y|)/4 on I times I.
   Its integral counts both orders of each pair, hence the coefficient
   k(u)/2 in (3). At p=2 its potential is
   V_epsilon(x)=2/h(x) integral_I (h(x)-h(y))
   K(x,y)1_(|x-y|>epsilon)dy. Adding m_0 and the cutoff version
   of (9) gives exactly the continuous residual in (4). For any
   compact subset of I and sufficiently small epsilon the killing
   cutoff is already unchanged. The symmetric small-u numerator
   is O(u^2) uniformly there, so the combined potential, and hence
   V_epsilon itself, converges locally uniformly. The cutoffs are
   symmetric, nonnegative, dominated and converge off the diagonal.
   The potential's positive and negative parts are integrable against
   |f|^2 because its support is compact in I. The translation estimates
   in the proof establish both source energies as finite. These are
   the hypotheses of Assumption2.1 and Proposition2.3; Remarks2.4/2.8
   permit the domain and support-local formulation. Neither a global
   positive reference outside I nor a nonnegative potential is required.

3. **Pointwise identification and atoms.** The zero-extended sine has
   finite variation of its weak derivative, giving the displayed
   O((1+|t|)^(-2)) Fourier decay. The logarithmic multiplier bound
   therefore supplies an L1 majorant for cutoff Fourier inversion,
   and the interior spatial cutoff limit matches that inverse.
   The transformed continuous energy is finite since g is compact
   smooth and h is bounded. Expanding the complex modulus square in
   (10) leaves exactly -2c_n Re(f(x)conj(f(x+d_n))); its integral
   is minus the sum of a shift and its adjoint. Each finite edge
   has positive reference values in its open integration interval;
   exterior values are zero. No atomic density or endpoint quotient
   is used. This checks every term of (3), not just its symbol.

4. **Strict midpoint test.** At b the continuous killing is the full
   integral from b to infinity. All shifts with n>=81sqrt3 vanish;
   each remaining von Mangoldt coefficient and cosine is nonnegative.
   DLMF5.4.19 admits p=1,q=4; its sum contributes -log2 and yields
   the scalar in (15). Independently checking the elementary bounds
   gives continuous increment <32/9+40/81=328/81 and m_0<-9/2.
   Their difference is -73/162, before subtracting the nonnegative
   entire arithmetic contribution S. The existing exact-arithmetic
   script was replayed: all seven checks pass and there are no
   failures. Its complete checks and bound fields were inspected;
   it is only an arithmetic check, not the analytic audit.

No error changing the statement or bound was found. The only direct
local mathematical input remains L744; L740 enters through its
verified smooth-domain specialization. The DAG row is unchanged.
The fixed pointwise implementation remains stopped. A negative
residual, even on a neighborhood, does not dispose of the positive
transformed remainder on the two-moment constrained space. No
unrestricted-support, other-profile, closed-domain or RH conclusion
has been added. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage of this complete finite-window identity
and obstruction has not been checked. No absence or formal
verification claim is made. The supporting mathematical inputs
are the named p=2 ground-state identity, Plancherel/translation
identities and DLMF's rational digamma evaluation. L744 supplies
the existing complete-symbol bound and smooth neutral energy
normalization; L740 supplies its actual smooth domain through
that specialization. All factors, killing terms and elementary
bounds needed for this local application are displayed above.
