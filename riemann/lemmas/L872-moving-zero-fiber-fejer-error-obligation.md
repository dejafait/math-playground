# Lemma 872: the moving-zero-fiber finite test leaves a quantified trace error

## Hypotheses

Retain the exact class assessed in
`drafts/literature/2026-11-06-actual-f-c0-infinite-profile-rigidity.md`.
In detail, use L871's actual entire function and coefficient

\[
 G(z)=\tfrac18\xi(\tfrac12+\tfrac{\sqrt z}{2}),\qquad G(0)>0,
 \quad F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
 \quad z_j=R e^{x_j+i y_j},\qquad C,R,H>0.
 \tag{1}
\]

The functions h,q,r are real global C1 functions on R2 times T2,
periodic in both angles. Normalize angular integrals by (2pi)^(-2)
and write m=hhat_0. Require h>=0, both equations

\[
 r_{x_j}=q_{y_j},\qquad(q+h)_{x_j}=-r_{y_j}\quad(j=1,2),
 \qquad q^2+r^2\leq |F|^2
 \tag{2}
\]

everywhere. Keep the original fixed Hardy zero a_*=-4 gamma_*^2,
ell=log(|a_*|/R), both means m(s,s)=m(ell,s)=H, and the selected
trace q((ell,s),(pi,v))=r((ell,s),(pi,v))=0 for all s,v.
For every nonzero n in Z2 require

\[
 \widehat h_n(x)=U_n(n\cdot x),\quad
 U_n\in C^1(\mathbb R;\mathbb C)\cap C_0(\mathbb R;\mathbb C),
 \quad |U_n|\leq H,
 \quad U_{-n}(t)=\overline{U_n(-t)},\quad U_n=B_n-B_n'',
 \tag{3}
\]

where B_n is complex C3 and C0 means decay at both infinite ends.
Keep all finite opposite-index tests: at every x put a_0(x)=H,
a_k(x)=hhat_(k,-k)(x) for k!=0 and require
sum_(j,l=0)^N c_j conjugate(c_l) a_(j-l)(x)>=0 for every N,c.
There is no angular summability, common radial tail, uniform C1
norm, lift-growth or finite-mode assumption. All original zeros,
homogeneous lift modes and zero modes remain allowed.

## Conclusion

The following is an exact finite-test reduction, **not a proof or
refutation of infinite-profile rigidity**. The separate conceptual
audit of 6 November 2026 below accepts the stated identities and
their angular-only diagnostic, with no stronger conclusion.

There is a sequence of actual negative G-zeros with logarithmic
radii lambda_j tending to +infinity. Fix integers a,b with b!=0
and a real t. Set

\[
 s_j=(t-a\lambda_j)/b,\qquad s'_j=\sqrt2\lambda_j,
 \qquad w_N(k)=\max\{1-|k|/(N+1),0\}.
 \tag{4}
\]

Define the b-th angular trace coefficient and its finite approximation by

\[
 \begin{split}
 c_j&=\frac1{2\pi}\int_0^{2\pi}
       h((\lambda_j,s),(\pi,v))e^{-ibv}\,dv,\\
 P_N(j,s)&=\sum_{|k|\leq N}w_N(k)(-1)^k
                         U_{(k,b)}(k\lambda_j+bs),\\
 E_N(j,s)&=P_N(j,s)-c_j.
 \end{split}
 \tag{5}
\]

The first line is independent of s. For each fixed j,s,
E_N(j,s)->0 as N->infinity. For each fixed N>=|a|, however,

\[
 \lim_{j\to\infty}\{E_N(j,s_j)-E_N(j,s'_j)\}
       =(-1)^a w_N(a)U_{(a,b)}(t).
 \tag{6}
\]

Consequently, writing
T_N(j)=|E_N(j,s_j)|+|E_N(j,s'_j)|, one has

\[
 \liminf_{j\to\infty}T_N(j)\geq w_N(a)|U_{(a,b)}(t)|,
 \qquad
 \liminf_{j\to\infty}\max\{|E_N(j,s_j)|,|E_N(j,s'_j)|\}
       \geq\tfrac12w_N(a)|U_{(a,b)}(t)|.
 \tag{7}
\]

Thus the sufficient error estimate

\[
             \lim_{N\to\infty}\limsup_{j\to\infty}T_N(j)=0
 \tag{8}
\]

would isolate this profile value and prove it zero. Estimate (8)
has **not** been established from the original hypotheses. Every
fixed-j limit T_N(j)->0 is already known and does not imply (8).
The same reduction with coordinates interchanged addresses n=(a,0),
a!=0; no profile has been proved zero by this reduction.

An explicit pair of sequences of smooth nonnegative angular slices
below has mean H, values between H/2 and 3H/2, identical constant
traces at y1=pi and every finite opposite-index positivity test,
yet has the analogue of the left side of (8) equal to H/8.
This disproves only an inference of (8) from these angular
properties. These slices are not asserted to be restrictions of
one global triple satisfying (1)-(3). In particular, they are not
a counterexample to actual-F rigidity or RH.

## Proof

### Imported inputs and their scope

The original calculation used the EXPLORE assessment
`drafts/literature/2026-11-06-actual-f-c0-infinite-profile-rigidity.md`.
The separate audit uses the unchanged SPECIALIZE assessment
`drafts/literature/2026-11-06-l872-finite-error-conceptual-audit.md`.
Reuse the sources assessed there; no new literature theorem or
novelty claim is introduced. L871's Hardy specialization supplies actual zeros
a_j=-4 gamma_j^2<0 with |a_j| unbounded, using E. C. Titchmarsh,
*The Theory of the Riemann Zeta-function*, second edition, revised
D. R. Heath-Brown (1986),
[Section 10.2, pp256-258](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=133).
The same proof checks the two square roots via xi reflection and
rules out finite accumulation by G(0)>0 and the holomorphic identity
theorem. None of its compact-profile hypotheses is used in that
zero construction. Pass to an unbounded sequence and put
lambda_j=log(|a_j|/R). This does not move the originally fixed ell.
No spacing, simplicity, effective-height or RH premise is imported.

Use Loukas Grafakos, *Classical Fourier Analysis*, third edition
(2014), [Definition 3.1.8, Remark 3.1.9, Proposition 3.1.10 and
Corollary 3.2.2, pp180-183](https://www.math.stonybrook.edu/~bishop/classes/math638.F20/Grafakos_Classical_Fourier_Analysis.pdf),
with [corrected Theorem 1.2.19(2)/proof, pp27-29](https://grafakos.missouri.edu/Books_Correction_Pages/CFA-Page27-29.pdf).
The required case is uniform Fejer convergence of one continuous
periodic function, normalizing its argument by 2pi. Every application
below is at fixed finite radial coordinates. This named theorem is
imported, not reproved or strengthened to moving slices.

Tangential C1 constancy uses the same mean-value theorem as L871:
Jiří Lebl, *Basic Analysis I*,
[Theorem 4.2.4](https://www.jirka.org/ra/html/sec_mvt.html),
on each finite radial interval. All complex integrals below are
compact integrals of continuous functions; finite sums can be
integrated term by term. No distributional trace is invoked.

### Exact trace identity before any radial limit

At x1=lambda_j,y1=pi, z1=a_j, so (1)-(2) force q=r=0 for
every x2=s,y2=v. Differentiating only along this fiber gives
q_x2=0 and r_y2=0. The second equation in (2) implies h_x2=0
there. The mean-value theorem makes h((lambda_j,s),(pi,v))
independent of s for every v. This proves the assertion about c_j.
No normal derivative or Fourier reconstruction of q,r is used.

For completeness, C868b also applies separately to every a_j:
its fixed-fiber argument uses the diagonal mean H of this same
triple and gives m(lambda_j,s)=H for every s. Its proof subtracts
two finite Fejer sums at fixed points; choosing a different actual
zero for an application adds no growth hypothesis and does not
alter the original ell. The transposed application gives
m(s,lambda_j)=H. These are necessary mean restrictions available
to the present test, not estimates of a moving approximation error.

For fixed j,s form the continuous periodic function

\[
 f_{j,s}(u)=\frac1{2\pi}\int_0^{2\pi}
               h((\lambda_j,s),(u,v))e^{-ibv}\,dv.
 \tag{9}
\]

Its k-th coefficient is exactly hhat_(k,b)(lambda_j,s), by
compact double integration, hence (3) gives the coefficient in (5).
The Fejer polynomial of (9) evaluated at u=pi is P_N(j,s).
Its limit is f_(j,s)(pi)=c_j. If

\[
 \epsilon_N(j,s)=\|\sigma_N f_{j,s}-f_{j,s}\|_\infty,
\]

then |E_N(j,s)|<=epsilon_N(j,s)->0 for each fixed pair j,s.
Because b!=0, there is no radial zero-mode term in (9).
Taking the difference at the two finite points s_j,s'_j cancels
c_j exactly, before taking any limit.

### Finite coefficient isolation and the remaining error

At s=s_j the argument of U_(k,b) is
t+(k-a)lambda_j. For k=a it is t; for every other fixed k it
tends to one of the two infinite ends, so that term tends to zero
by C0 decay. At s=s'_j the argument is (k+b sqrt2)lambda_j.
Its coefficient is never zero for integers k and b!=0, by
irrationality of sqrt2, so every fixed term tends to zero there.
For fixed N these are finite sums. Their limits give (6), with
the phase (-1)^a and the Fejer weight unchanged.

The triangle inequality gives T_N(j)>=|E_N(j,s_j)-E_N(j,s'_j)|
and twice the maximum in (7) is at least the same modulus. Taking
the indicated lower limits proves (7). If (8) held, (7), together
with w_N(a)->1, would give |U_(a,b)(t)|=0. Conversely, a nonzero
value requires at least the errors in (7); no convergence of the
individual errors in j has been assumed. For each fixed j, both
s_j and s'_j are finite, so their two errors do tend to zero as
N increases. This is the opposite order from (8).

For n=(a,0), a!=0, use x2=lambda_j,y2=pi, integrate in y1 at
frequency a, and sum the remaining y2 frequencies. The free radial
coordinate is x1=u. More explicitly, put

\[
 \begin{split}
 \widetilde c_j&=\frac1{2\pi}\int_0^{2\pi}
       h((u,\lambda_j),(v,\pi))e^{-iav}\,dv,\\
 \widetilde P_N(j,u)&=\sum_{|k|\leq N}w_N(k)(-1)^k
                       U_{(a,k)}(au+k\lambda_j),\\
 \widetilde E_N(j,u)&=\widetilde P_N(j,u)-\widetilde c_j.
 \end{split}
\]

Tangential closure makes tilde c_j independent of u, and the
nonzero frequency a excludes the radial zero mode. At u=t/a the
arguments are t+k lambda_j; at u=sqrt2 lambda_j they are
(a sqrt2+k)lambda_j. The retained summation index is k=0,
whose phase and weight are both 1. Every other fixed term on the
first path escapes, and every fixed term on the second path escapes,
including k=0 since a!=0. Consequently, for each fixed N>=0,

\[
 \lim_{j\to\infty}
 [\widetilde E_N(j,t/a)-
  \widetilde E_N(j,\sqrt2\lambda_j)]=U_{(a,0)}(t).
\]

The sum-of-errors and maximum lower bounds are therefore respectively
|U_(a,0)(t)| and |U_(a,0)(t)|/2. Fixed-j errors still vanish as N
increases, and the transposed version of (8) would force this value
to vanish. Only the symmetric actual zero fibers and equations (2)
are used; the original selected-fiber hypothesis is not transposed.

### Angular diagnostic: positivity and mass do not supply (8)

This diagnostic concerns angular functions only. Set eta=H/4 and
let K_j be positive integers tending to infinity, larger than
2|a|+2. Define on T2

\[
 \begin{split}
 g_j(y)&=H+\eta\cos(a y_1+b y_2)
       -\eta\cos((a+K_j)y_1+b y_2-K_j\pi),\\
 g'_j(y)&=H.
 \end{split}
 \tag{10}
\]

Both are real C-infinity, have mean H because b!=0, and satisfy
H/2<=g_j,g'_j<=3H/2. At y1=pi the two cosines agree exactly,
so both traces are identically H. Their y2 marginals are also
identically H. Every Fourier coefficient is bounded by H, since
each function is nonnegative of mean H. For every finite vector
c, the opposite-index test with zero coefficient H equals

\[
 (2\pi)^{-2}\int g_j(y)
       \left|\sum_l c_l e^{-il(y_1-y_2)}\right|^2dy\geq0,
 \tag{11}
\]

and the same holds for g'_j. Thus these tests impose no hidden
exception on the diagnostic.

The b-th y2 coefficient of g_j is the one-variable polynomial

\[
 \tfrac\eta2 e^{ia u}
       -\tfrac\eta2 e^{i(a+K_j)u-iK_j\pi}.
 \tag{12}
\]

The b-th coefficient of either exact trace is zero. Its Fejer
approximation at u=pi therefore has error exactly

\[
 \tfrac\eta2(-1)^a\{w_N(a)-w_N(a+K_j)\},
 \tag{13}
\]

while the error for g'_j is zero. For fixed N>=|a|, the second
weight is zero for all sufficiently large j. Thus the sum of
absolute errors tends to (eta/2)w_N(a) as j increases, and then
to eta/2=H/8 as N increases. For each fixed j the error instead
tends to zero as N increases, directly from (13). These are exact
values, not a numerical preview. The required threshold in (8)
is zero; the angular diagnostic yields H/8>0.

This also shows that adding a uniform bound on the values of the
angular slices would not by itself justify the interchange. Their
angular derivatives need not be uniformly bounded. More crucially,
(10) does not assign one set of global C0 profiles or construct
q,r meeting (2) and actual-F domination. Therefore the diagnostic
does not show that (8) fails for the original class. The complete
actual-F and radial compatibility constraints could still rule out
this kind of error, and that issue is unresolved.

### Decision and limits

The proposed finite-test isolation has reached the quantified
obligation (8), not rigidity. No new estimate for it follows from
the imported fixed-slice theorem or from positivity and the common
mean alone. Stop this attempt without adding summability, uniform
radial tails or lift growth. A subsequent attempt needs a different
use of full radial/actual-F compatibility, with source coverage
for that mechanism; the diagnostic cannot be promoted to a global
counterexample. General forcing, period control, graph realization
and actual-Xi all-degree mixed positivity remain open.

### Independent conceptual audit, 6 November 2026

Step `2026-11-06-l872-finite-error-audit-33` reproduces the existing
reduction under the prior SPECIALIZE assessment cited above. No
mathematical defect was found. The explicit transposed formulas
above expand the previously stated same-proof case; they do not
extend its hypotheses or conclusion. This is local verification,
not a new rigidity result or a claim of progress beyond the sources
checked. The original finite-test stop is retained.

**Class and inherited inputs.** The global real C1 class (1)-(3),
both original means, conjugation with argument reversal, the C3
profile relation and every finite positivity test remain unchanged.
C868b and L871 are the direct mathematical inputs. L871 supplies
only its actual-zero construction and tangential trace reasoning;
its eight-frequency compact-support rigidity is not applied to this
infinite C0 family. L018/L847's actual-zero correspondence enters
through these inputs. Neither L873 nor an angular diagnostic is
an input to the actual-F implication. There is no cross-notebook
input. The class is nonempty: h=H, q=r=0, U_n=B_n=0 satisfies
every condition, including the finite tests.

**Zero and trace quantifiers.** Hardy gives infinitely many distinct
ordinates; squaring identifies at most two of them. L871's identity-
theorem argument therefore gives a sequence with lambda_j tending
to positive infinity, without a spacing, simplicity or RH premise.
The same sequence works for every finite cutoff. It does not change
ell. Since z1,z2 never vanish, either actual G-zero makes F zero
without a denominator exception. On the first fiber the derivatives
q_x2 and r_y2 are tangential derivatives of zero functions. Closure
then gives h_x2=0, and finite-interval constancy gives the same c_j
at both selected points. The transposed derivatives are q_x1 and
r_y1. No normal derivative, regularity beyond C1, or limit of c_j
as j grows is required. C868b's finite subtraction proof of the
fiber mean uses the diagonal mean of the same triple, so its use
at each new zero does not add a selected-mean hypothesis.

**Finite projection and the two limit orders.** Compact Fubini
integration in (9), with normalized measures, gives exactly the
(k,b) coefficient. There is just one Fejer weight, because only u
is approximated. The imported theorem applies to this complex
continuous periodic function, equivalently to its real and imaginary
parts, at each fixed j,s. It supplies no common modulus as those
parameters escape. Subtracting at two finite s values cancels c_j
before any limit. At s_j the only nonescaping argument is t for
k=a, including a=0; at s'_j every coefficient k+b sqrt2 is nonzero,
including for negative b. For fixed N there are finitely many
terms, so C0 decay at both ends suffices. No quantitative irrational
approximation or bound uniform in k is used. This proves (6) with
the sign (-1)^a and nonnegative weight w_N(a), including N=|a|.

The complex difference has the limit in (6), hence its modulus
converges to w_N(a)|U_(a,b)(t)|. The triangle inequality and twice
the maximum give both lower limits in (7) without assuming limits
of the separate errors. Since limsup is at least liminf, (8) and
w_N(a) tending to 1 force the stated profile value to be zero.
For each fixed j, the two radial points are finite and independent
of N, so their errors tend to zero in the reverse order. These
facts establish a conditional implication, not (8). The explicit
transposed computation above checks all remaining nonzero indices;
its retained index is 0, not a, so its weight is exactly 1.

**Diagnostic and its admissibility boundary.** For either sign of
b!=0 the two cosines in (10) have zero mean and are distinct from
their conjugate frequencies. With eta=H/4 their combined absolute
variation is at most H/2. At y1=pi their phases agree; integrating
in y2 also leaves H for every y1. Thus reality, nonnegativity,
the stated range, both means and the common trace all hold. The
finite square expansion in (11) has exponent -i(j-l)(y1-y2),
which gives exactly a_(j-l), including a_0=H. It proves every
finite opposite-index test and uses no factorization or infinite
sum. Positivity and mean H bound every Fourier coefficient by H.

Projection against e^(-ibv) selects the positive exponential of
each cosine; the other exponential integrates to zero because
2b!=0. Evaluation at pi multiplies the shifted term by
e^(i(a+K_j)pi-iK_j pi)=(-1)^a. This recovers (12)-(13), with
the factor eta/2. For fixed N, |a+K_j| eventually exceeds N,
so the two-slice absolute error tends to (eta/2)w_N(a), and its
subsequent N limit is H/8>0. For fixed j both weights tend to 1,
so the error tends to zero. These are exact finite identities;
no numerical script or asymptotic remainder is needed.

The diagnostic realizes only the listed angular constraints. It
does not supply global profiles, their C0 tails or C3 lifts, radial
closure, all other zero fibers, or domination by actual F. Therefore
its H/8 cannot refute estimate (8) in the full actual-F class. It
only rules out deducing the zero threshold from those angular
constraints alone, even with the common value bound. Passing this
audit neither restarts the unchanged interchange nor settles the
period, graph-realization or actual-Xi positivity gaps.

## Mathlib

Full matching and supporting Mathlib coverage has not been checked.
No absence claim is made. Hardy, the mean-value theorem and fixed
continuous-slice Fejer convergence are precise imported inputs;
the finite sums, their limits and the angular diagnostic above have
passed the independent informal conceptual audit. This is not Lean
verification or a proof of RH.
