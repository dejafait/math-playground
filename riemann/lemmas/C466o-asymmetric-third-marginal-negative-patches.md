# Corollary 466o: negative patches of the asymmetric third marginal

## Hypotheses

Use C466k/C466l's actual entire function
\(h(z)=\xi(1/2+\sqrt z)/c_0\), \(c_0=\xi(1/2)>0\), and
\(p=\theta_1\). Thus \(p\in C^\infty(\mathbb R)\) has mass one,
vanishes on \(( -\infty,0]\), is positive on \((0,\infty)\), and
has Laplace transform \(1/h(z)\) for \(\operatorname{Re}z>0\).
Retain the inherited C466a density, critical-strip, zero-symmetry,
paired-product, zero-counting and verified-low-zero qualifications.
Those external inputs are not independently replayed here. No RH,
global PF assertion, simplicity, extra verified zeros, finite-core
replacement or independence after conditioning is assumed.

Put \(B(s)=\log h(s)\), \(x=B'(1)\), \(S=3x\), and retain
C466l's definitions
\[
 F(t)=\frac{e^{x(1+it)}}{h(1+it)},\qquad
 M(a,b)=\int_{\mathbb R}F(t+a)F(t+b)F(t-a-b)\,dt.
\]
Use C466m's full-completion expansion and C466n(15)'s certified
bound \(0<S<1\). Only that bound on S, not its density lower bound
or opposed-slice onset, is used from C466n. Its elementary outward
interval implementation remains a computational trust assumption.

## Conclusion

Define the strictly positive real number
\[
 A=2\pi\int_0^S p(u)p(S-u)\cos(S-2u)\,du>0.                 \tag{1}
\]
Then, as \(r\to+\infty\),
\[
 e^{iSr}h(1-3ir)M(r+1,r-1)\longrightarrow A.                 \tag{2}
\]
There are arbitrarily large \(r>1\) for which
\(\operatorname{Re}M(r+1,r-1)<0\). Each yields an open patch
where the real marginal and its squared-Vandermonde-weighted version
in C466l(1) are strictly negative.

This refutes sufficient pointwise nonnegativity of that real marginal
at the selected actual x. It does not sign its full weighted integral,
refute a density minor, settle higher orders/all x, supply density-to-Xi
transfer, or resolve L030-L032/C032a or RH. The witnesses are selected
by a continuous phase; no numerical frequency or effective onset is
claimed. The result of approved attempt941 passes the separate
step943 critical audit below under the retained inputs; it is not a
complete RH candidate.

## Proof

### Source reuse, normalization and the candidate coefficient

Nomination939/approval940 was EXPLORE before this attempt and covers
this exact ray, actual law and analytic test. The known Fourier
identities below are imported with their qualifications; their
specialization supplies constants, not a new convolution theorem.
The asymmetric domination and phase inference require a new argument:
C466l/C466m's opposed-slice bounds do not imply them.

Write \(h_t=h(1+it)\), \(b(t)=\log|h_t|\), and set \(R=3r\).
The change of variable \(v=t+r\) is real and has Jacobian one.
Since the three shifts sum to zero, the exact normalization is
\[
 e^{iSr}h_{-R}M(r+1,r-1)
 =e^S\int_{\mathbb R}J_R(v)\,dv,\qquad
 J_R(v)=\frac{e^{iSv}}{h_{v+1}h_{v-1}}
                         \frac{h_{-R}}{h_{v-R}}.           \tag{3}
\]
For each fixed R this is absolutely convergent by C466k's
polynomially weighted decay. No contour has moved.

For each fixed real v,
\[
 \frac{h_{-R}}{h_{v-R}}\longrightarrow1.                    \tag{4}
\]
Here is the needed complex, rather than modulus-only, justification.
C466m(5) gives on the large closed right-half-plane region
\[
 D(z):=\log h(z)-\log h(1)=G(z)+C+E(z),\quad
 G(z)=\frac{\sqrt z}{2}\left(\log\frac{\sqrt z}{2\pi}-1\right)
                         +\frac78\log z,
 \quad C\in\mathbb R,\quad |E(z)|\le3|z|^{-1/2}.           \tag{5}
\]
These are compatible analytic logarithms, real on the positive axis.
This imports the full-completion estimate, ultimately using
[DLMF 5.11.1 and 5.11(ii)](https://dlmf.nist.gov/5.11) for the analytic
log-Gamma remainder and [DLMF 25.2.1/6](https://dlmf.nist.gov/25.2)
for the absolutely convergent zeta/Euler series in its stated domain.
The relevant proof cases were inspected in review935 and reused by
approval940; no estimate for zeta outside that domain is introduced.

Along the bounded vertical segment from \(1-iR\) to
\(1+i(v-R)\), for sufficiently large R,
\[
 G'(z)=\frac{\log(\sqrt z/(2\pi))}{4\sqrt z}+\frac7{8z}
                =O(\log R/\sqrt R).
\]
The segment stays in the region of (5) and has modulus at least R/2.
Its explicit-part difference is \(O_v(\log R/\sqrt R)\), and
the two remainder values have total modulus \(O(R^{-1/2})\).
Their log difference tends to zero, proving (4) including its phase.
No derivative of E has been used.

If the integral limit is justified, its value is
\[
 e^S\int_{\mathbb R}\frac{e^{iSv}}{h_{v+1}h_{v-1}}\,dv=A.   \tag{6}
\]
To establish this identity with its constants, put
\(f(u)=e^{-u}p(u)\) and \(f_\pm(u)=e^{\mp iu}f(u)\).
C466k's inversion makes f bounded and uniformly continuous, and
\(f\in L^1\). With angular Fourier convention
\(\widehat f(t)=\int e^{-itu}f(u)du\), one has
\(\widehat {f_\pm}(v)=1/h_{v\pm1}\).
Import the complex L1 convolution theorem, Christopher Heil,
*The Fourier Transform on L1(R)*, Fall 2009,
[Theorem 1.23, pp.16-17](https://heil.math.gatech.edu/7338/fall09/convolution.pdf),
with his frequency replaced by \(v/(2\pi)\); and pointwise inversion
from David Jerison, *Fourier Integrals on L2(R) and L1(R)*,
MIT18.103 Fall 2013,
[Corollary 4/Proposition 2/Theorem 2, pp.2-4](https://math.mit.edu/~jerison/103/handouts/fourierint1.13.pdf).
These are the inspected inputs in review930/recovery931, reused by
approval940. The convolution \(f_+*f_-\) is continuous, bounded
and in L1, hence also L2; its transform \(1/(h_{v+1}h_{v-1})\)
is L1 and L2 by C466k's decay. Thus inversion holds at the specified
point S, rather than only almost everywhere, and gives
\[
 \int_{\mathbb R}\frac{e^{iSv}}{h_{v+1}h_{v-1}}\,dv
 =2\pi e^{-S}\int_0^S p(u)p(S-u)e^{i(S-2u)}\,du.            \tag{7}
\]
The convolution integral is absolutely convergent, since its factors
are bounded on [0,S]. Substitution \(u\mapsto S-u\) shows that its
imaginary part is zero. Since \(|S-2u|\le S<1<\pi/2\), its
cosine is strictly positive; p is positive on (0,S). This proves
(1) and (6), including finiteness and nonvanishing of A.

For completeness, the only numerical input here is C466n(15), whose
proof and step939 audit justify S by full-completion derivative
enclosures and Cauchy remainder bounds. The complete selected value
at `/constants/S` in `scripts/reciprocal-tail/density-939-recomputed.json`
has lower endpoint
\(6028509235395205208152929012285026630367\,2^{-136}\)
and upper endpoint
\(3014254617697602604076464508972100526449\,2^{-135}\).
They lie strictly between 0 and 1. This invocation inspected that
selected value and its canonical justification, and imports the
already audited bound; it does not claim a fresh replay of the
special-function computation or its elementary interval library.

### Uniform domination on the whole moving-frequency integral

The function b is continuous, even and nonnegative. Indeed C466m(3)
gives \(|h_t|\ge h(1)\ge1\) from the tilted probability law.
C466l(10), or C466m(8) with the real normalization constant restored,
gives for \(u\to+\infty\)
\[
 b(u)=g(u)+\rho(u),\qquad
 g(u)=\kappa\sqrt u\log u+\lambda\sqrt u+\tfrac78\log u+C_b,
 \quad \rho(u)=O(\log u/\sqrt u),                          \tag{8}
\]
where \(\kappa=1/(4\sqrt2)>0\),
\(\lambda=-(\log(2\pi)+1+\pi/4)/(2\sqrt2)\), and C_b is real.
Let \(W(u)=\sqrt u\log u\) for \(u\ge e\). Choose T large enough
that, for every \(|v|\ge T\),
\[
 b(v+1)+b(v-1)\ge\tfrac32\kappa W(|v|),\qquad
 b(u)\le\tfrac{11}{10}\kappa W(u)\quad(u\ge T).             \tag{9}
\]
The first inequality follows because each of
\(b(v\pm1)/(\kappa W(|v|))\) tends to one as \(|v|\to\infty\),
using evenness and \(W(|v\pm1|)/W(|v|)\to1\). The second follows
directly from (8). Neither asserts monotonicity of b.

Define
\[
 E_R(v)=b(v+1)+b(v-1)+b(v-R)-b(R),\qquad
 |J_R(v)|=e^{-E_R(v)}.                                    \tag{10}
\]
We prove that fixed positive constants R0,T,c,C1 can be chosen with
\[
 |J_R(v)|\le C_1\quad(|v|\le T),\qquad
 |J_R(v)|\le C_1e^{-cW(|v|)}\quad(|v|\ge T),\quad R\ge R_0. \tag{11}
\]

First consider \(|v|\le\epsilon R\), where \(0<\epsilon<e^{-1}\)
will be fixed below. On [R/2,3R/2], explicit differentiation of g
gives \(|g'(u)|\le M\log R/\sqrt R\) for a fixed M and all
sufficiently large R. Applying the mean-value bound to g and only
the value bound to the two remainders in (8) gives
\[
 b(R-v)-b(R)\ge
       -M|v|\log R/\sqrt R-C_2\log R/\sqrt R.              \tag{12}
\]
This holds for both signs of v; \(b(v-R)=b(R-v)\) in this range.
For \(T\le|v|\le\epsilon R\), put \(y=R/|v|\ge1/\epsilon\).
Since \(\log|v|\ge1\),
\[
 \frac{|v|\log R/\sqrt R}{W(|v|)}
 =y^{-1/2}\frac{\log R}{\log|v|}
 \le y^{-1/2}(1+\log y)
 \le\sqrt\epsilon(1+\log(1/\epsilon)).                    \tag{13}
\]
The final inequality uses that \(y^{-1/2}(1+\log y)\) decreases
for \(y\ge e\). Fix epsilon small enough that M times the final
expression is at most \(\kappa/2\); it tends to zero with epsilon.
Equations (9), (12) and (13) imply
\(E_R(v)\ge\kappa W(|v|)-C_3\), since \(\log R/\sqrt R\)
is bounded for large R. For \(|v|\le T\), (12), the same boundedness
and continuity of the two fixed-shift b values give
\(E_R(v)\ge-C_4\), after increasing R0 so T<=epsilon R0.
This proves (11) on the entire small range, including v=+/-1.

Next let \(\epsilon R\le|v|\le2R\), and write s=v/R.
The already proved uniform scaling C466l(18) states
\[
 \sup_{0\le a\le3}
 \left|\frac{b(aR)}{\kappa\sqrt R\log R}-\sqrt a\right|
                       \longrightarrow0.                 \tag{14}
\]
It includes a=0 by a separate compact-argument bound, so may be used
at the moving frequency zero. The three arguments in (10) correspond
to \(|s+1/R|,|s-1/R|,|s-1|\), all in [0,3] for large R and
\(|s|\le2\). Since \(|\sqrt{|s\pm1/R|}-\sqrt{|s|}|\le R^{-1/2}\),
(14) gives the uniform limit
\[
 \frac{E_R(v)}{\kappa\sqrt R\log R}
       = f(s)+o(1),\qquad
 f(s)=2\sqrt{|s|}+\sqrt{|1-s|}-1.                          \tag{15}
\]
For s<0 one has \(\sqrt{1-s}>1\), so f(s)>0. For
\(0<s\le1\), \(\sqrt{1-s}\ge1-s\), whence
\(f(s)\ge2\sqrt s-s>0\). For s>=1,
\(f(s)\ge2\sqrt s-1\ge1\). Thus the minimum m of f on the compact
set \([-2,-\epsilon]\cup[\epsilon,2]\) is strictly positive.
For all sufficiently large R, (15) is at least m/2 throughout this
set. Since \(W(|v|)\le W(2R)\le2\sqrt2\sqrt R\log R\) for
R>=2, it follows that
\[
 E_R(v)\ge\frac{\kappa m}{4\sqrt2}W(|v|)
                    \quad(\epsilon R\le|v|\le2R).         \tag{16}
\]
In particular this pays the entire competing neighborhood v=R,
equivalently t=2r, where the third original factor has zero frequency.

Finally let \(|v|\ge2R\), with R>=T. Using (9), b(v-R)>=0,
and \(W(R)\le W(|v|)/\sqrt2\), gives
\[
 E_R(v)\ge\kappa\left(\frac32-\frac{11}{10\sqrt2}\right)W(|v|)
                         >\frac25\kappa W(|v|).           \tag{17}
\]
The inequalities involving W use its explicit monotonicity on [e,infinity).
Combining the three ranges proves (11) with fixed constants, for both
signs of v. Its majorant is integrable, since W(u)>=sqrt(u) for u>=e.
Every moving small-frequency region and the unbounded complement are
therefore paid. This argument does not infer integral domination from
a fixed-v asymptotic or from a nonnegative convolution-tail theorem.

Apply dominated convergence to (3), using (4), (11) and (6). This
proves the full complex normalized limit (2).

### A surviving phase gives actual negative values and open patches

Let \(\beta(R)=\operatorname{Im}D(1+iR)\) for sufficiently large R,
using the analytic logarithm in (5). It is a continuous unwrapped
phase, not a principal argument selected separately at each R.
Since log h(1) is real,
\[
 h_R=\exp\{b(R)+i\beta(R)\},\qquad
 h_{-R}=\overline{h_R}=\exp\{b(R)-i\beta(R)\}.
\]
Equation (5) gives \(\beta(R)=O(\sqrt R\log R)\): each explicit
term has this bound and its remainder tends to zero. Consequently
\[
 \vartheta(r):=\beta(3r)-Sr=-Sr+O(\sqrt r\log r)
                         \longrightarrow-\infty,          \tag{18}
\]
because S>0. This uses no differentiated error or monotonicity of beta.
By (2) there is a complex error \(\eta(r)\to0\) such that
\[
 M(r+1,r-1)=e^{-b(3r)}e^{i\vartheta(r)}(A+\eta(r)).         \tag{19}
\]
Choose \(r_*>1\) large enough for this continuous phase to be defined
and \(|\eta(r)|<A/2\) for every r>=r_*. For each sufficiently
large integer n with \(-(2n+1)\pi<\vartheta(r_*)\), continuity
and (18) give some finite \(r_n>r_*\) with
\(\vartheta(r_n)=-(2n+1)\pi\). For example the first point where
the phase is at most that level exists and attains equality by
continuity. Such points tend to infinity as n does, since the phase
is bounded on every compact interval. At each one,
\[
 \operatorname{Re}M(r_n+1,r_n-1)
 =-e^{-b(3r_n)}\bigl(A+\operatorname{Re}\eta(r_n)\bigr)
 <-\tfrac A2 e^{-b(3r_n)}<0.                               \tag{20}
\]
Thus the argument produces actual phase-defined negative values,
rather than merely a possible oscillatory leading term.

At a=r_n+1, b=r_n-1 the squared Vandermonde in C466l(1) is
\[
 (a-b)^2(2a+b)^2(a+2b)^2
       =4(3r_n+1)^2(3r_n-1)^2>0,                           \tag{21}
\]
since r_n>1. C466l's proved continuity of M and continuity of this
polynomial provide an open neighborhood in the real (a,b)-plane
where both required strict signs persist. This proves the conclusion.

The stops in C466k and attempt932 remain separate: no common-product
phase choice or conditional iid factorization entered this argument.
The weighted integral may still be positive despite these negative
patches. The present proof only removes pointwise marginal
nonnegativity as a sufficient mechanism, under the explicitly retained
external and computational inputs. Approval940's bounded search did
not establish coverage for this asymmetric result; that is not a
certification of originality.

### Critical audit, 14 November 2026, step943

The claimed limit and negative patches pass under the exact hypotheses.
This verifies the existing local obstruction, without strengthening it
or certifying originality. The ready SPECIALIZE assessment is
nomination941/approval942, with the inspected primary convolution,
inversion and full-completion sources retained above. In particular
this audit does not replace the inherited density theorem or its
external counting/low-zero inputs with an independent verification.

In (3), v=t+r gives frequencies v+1,v-1,v-R. The product numerator
is exp(S) exp(iSv) exp(-iSr), since S=3x and R=3r. Multiplication
by exp(iSr)h_{-R} therefore leaves exactly the displayed integral:
there is no extra h(1), c0, Jacobian or conjugation. For fixed v,
the segment used in (4) has modulus at least R/2 once R>2|v|.
C466m(5) is valid throughout it, with the same analytic branch at
both endpoints. Integrating G' and bounding the two values of E
gives a vanishing complex logarithm difference. A differentiated
remainder is neither assumed nor needed.

Here is the order of choices for the majorant, making its uniform
quantifiers explicit. First fix T>=e so that (8)-(9) hold, and fix
M,C2 for (12). Such constants can be chosen independently of epsilon
on [R/2,3R/2]. Indeed
\[
 g'(u)=\frac{\kappa(\log u+2)+\lambda}{2\sqrt u}
                       +\frac7{8u},
\]
and each remainder value there is O(log R/sqrt R). Next fix
0<epsilon<e^(-1)<1/2 satisfying (13)'s required coefficient bound.
This single epsilon works for both signs of v. Finally choose R0
at least max{2T,T/epsilon,2} and all the finitely many subsequent
asymptotic thresholds; in particular epsilon R0>=T. For
T<=|v|<=epsilon R, (9) contributes (3/2)kappa W(|v|) and (12)
costs at most (1/2)kappa W(|v|)+C3. For |v|<=T it costs only
a fixed constant. Thus the entire small range has the stated
uniform lower bound on E_R, including v=+/-1.

The invocation of C466l(18) in (14) is valid at the moving zero.
For aR>=T, subtracting kappa sqrt(R)log(R)sqrt(a) from b(aR)
leaves terms uniformly O(sqrt R), O(log R) and O(1): the crucial
sqrt(a)log(a) is bounded on [0,3] after extension at zero. For
aR<T, continuity bounds b(aR) on [0,T], while the subtracted term
is at most kappa sqrt(T)log R. Division by kappa sqrt(R)log R
makes both bounds tend uniformly to zero. This checks the complete
small-argument case, rather than substituting a large-argument
asymptotic at a=0.

Consequently (15) is uniform for epsilon<=|v|/R<=2, including
v=R and both signs of v. Its limiting function is positive on
that fixed compact set by the three explicit cases following (15),
so its minimum m is positive. Once epsilon is fixed, m is fixed
before enlarging R0. The conversion W(2R)<=2sqrt(2)sqrt(R)log R
is valid for R>=2, giving (16). In the far range, W(R)<=W(|v|)/sqrt(2)
and b(v-R)>=0 give (17). In particular
3/2-11/(10sqrt(2))>2/5, since sqrt(2)>1. One can therefore take
\[
 c=\min\left\{\kappa,\frac{\kappa m}{4\sqrt2},
                         \frac25\kappa\right\}>0
\]
and a fixed C1 large enough for the compact and small-range constants.
This gives one integrable bound for every R>=R0 on the whole real
axis. No region escapes between the ranges and neither monotonicity
of b nor an opposed-slice majorant is substituted for this argument.

For (7), f and both modulations are bounded uniformly continuous
L1 functions. Their convolution is continuous, belongs to L1 and
is bounded, hence belongs to L2. Its transform is exactly the product
of the two shifted reciprocal h values, in L1 and L2 by C466k's
decay. The cited inversion theorem therefore identifies continuous
functions at S, not merely an almost-everywhere representative.
The angular-frequency inverse factor is 1/(2pi), so (7)'s factor
2pi and the cancellation exp(S)exp(-S) are correct. Reflection
u -> S-u cancels the sine term. The remaining integrand is positive
on (0,S), since p is positive there and cos(S-2u)>=cos(S)>0
when 0<S<1. Thus A is finite and strictly positive.

The complete `/constants/S` value in
`scripts/reciprocal-tail/density-939-recomputed.json` was inspected
using `python3 ../scripts/loop/inspect_json.py scripts/reciprocal-tail/density-939-recomputed.json --pointer /constants/S --full`.
Its exact endpoints agree with those displayed above. The lower
mantissa is positive; the upper mantissa is less than
2^135=43556142965880123323311949751266331066368, so 0<S<1.
C466n(14)-(15) and its step939 audit justify identifying this enclosure
with 3B'(1), including both Cauchy derivative remainder bounds.
This audit reuses that proved enclosure and its elementary interval
trust base; it does not rerun its special-function implementation,
density quadrature or unrelated opposed-slice onset certificate.

Finally, the logarithm supplied by (5) defines one continuous beta
for all sufficiently large R. Its imaginary part is O(sqrt R log R),
so theta(r)=beta(3r)-Sr tends to minus infinity. This conclusion
uses only S>0 and no derivative or monotonicity of beta. The full
complex dominated-convergence limit produces eta(r)->0 after the
normalization in (19), which is essential since exp(-b(3r)) also
tends to zero. Choose a single r_* after which |eta|<A/2.
Continuity crosses each sufficiently negative odd multiple of pi;
the crossings escape every compact interval because theta is bounded
there. At them (20) has the stated strict negative bound. The
Vandermonde at (r+1,r-1) is exactly (21) and is nonzero for r>1.
C466l's compact-shift domination proves continuity of M, so both
strict signs persist on open neighborhoods.

No failed implication or mathematical correction was found. The
direct inputs remain C466k/C466l/C466m/C466n; C466a is inherited
through them, so the existing DAG row is unchanged. Stop941 is now
validated only for sufficient pointwise nonnegativity. Full signed
integration, higher orders/all x and actual-Xi transfer remain open;
no negative density determinant or RH counterexample follows.

## Mathlib

Full matching coverage has not been checked. The imported convolution,
Fourier inversion, dominated convergence, complex conjugation and real
intermediate-value facts are supporting mathematics; no matching
formalization of (2) or (20) is claimed. Unknown coverage is not evidence
of absence. No declaration names or formal-verification claims are made.
