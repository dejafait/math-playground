# L909: a common large-real-zero profile excludes logarithmic L2 symmetry

## Hypotheses

Keep exactly the positive function w, operators D and L, and primitive
u_alpha of L906-L908, with no change of normalization or measure. Set

\[
W(x)=w(e^x),\quad q=W'/W,\quad U_\alpha(x)=u_\alpha(e^x),\quad
G_\alpha(x)=(Lu_\alpha)(e^x),\qquad x\in\mathbb R.
\]

Here alpha is a positive real exact zero of the completed Xi in L908.
The logarithmic norm and inner product are
\(\|f\|_2^2=\int_{\mathbb R}|f(x)|^2dx\) and
\(\langle f,g\rangle=\int_{\mathbb R}f(x)\overline{g(x)}dx\),
linear in the first argument. They correspond to measure dt/t.
Use the audited conclusions of L906, L907 and L908(1)-(3) only;
L908's step154 addition is not an input. No RH, zero simplicity,
zero indexing, spacing, pair symmetry or positive realization is assumed.

## Conclusion

Define the fixed profile

\[
F(x)=\frac1i\left(W''(x)-\frac{W'(x)^2}{W(x)}\right)
     =-iW(x)q'(x).
\tag{1}
\]

Then F belongs to L2(R), and m=||F||_2 is strictly positive. There
is a finite constant C depending only on W such that, for every
positive real exact zero alpha,

\[
\|\alpha^2G_\alpha-F\|_2\le C/\alpha.
\tag{2}
\]

Consequently, if A=max{1,4C/m}, every pair of positive real exact zeros
alpha,beta>=A satisfies

\[
\operatorname{Re}\langle G_\alpha,G_\beta\rangle
\ge\frac{7m^2}{16\alpha^2\beta^2}>0.
\tag{3}
\]

Hardy's theorem supplies arbitrarily large distinct positive real zeros,
so (3) is nonvacuous for distinct pairs. The logarithmic L2 metric on
the L-images therefore fails the pair-symmetry requirement of Hedenmalm,
Definition4.2.1/Theorem4.2.2(b), already on the span of two
real-zero generators. The conclusion rules out this particular metric,
not other metrics, the source's conditional theorem, or RH. The bound
does not evaluate the first pair or give a numerically evaluated A.
The step156 proof passes the separate step157 critical audit below.

## Proof

**Imported inputs and the application difference.** L906 gives W>0,
smoothness, evenness, W'(0)=0, W''(0)<-1/6 and, for each integer j>=0,
finite constants c_j>0 such that

\[
|W^{(j)}(x)|\le c_j
 \exp\big((2j+9/2)|x|-\pi e^{2|x|}\big).
\tag{4}
\]

In particular all derivatives are integrable and vanish at both ends.
L908 supplies |q(x)|<=20pi exp(2|x|) and the exact transform identity
\(\int_{\mathbb R}e^{i\alpha s}W(s)ds=\Xi(\alpha)/2\).
The factor 1/2 is retained, rather than the source's inconsistent
printed coefficient. L907 supplies the primitive and its ODE.

The standard endpoint expansion is imported from NIST DLMF,
[Section2.3(i), equations (2.3.4)-(2.3.6)](https://dlmf.nist.gov/2.3#i),
as inspected in the step155 assessment on 8 November 2026. Its
finite-order integration-by-parts remainder is bounded by the
corresponding power of the inverse frequency times the integral of
the absolute derivative. We apply its three-term formula to W and W'
on half-lines. All derivative integrals converge absolutely by (4),
uniformly in real frequency at a fixed endpoint, and all boundary
derivatives vanish at the infinite endpoint. These facts check the
half-line hypotheses; reflection/conjugation handles the negative
half-line and sign of the frequency. Below we retain the exact
remainder and endpoint signs for this application. We do not reprove
the general asymptotic theorem. The extra work is its uniform
whole-line application after multiplication by the unbounded q.

**Derivative primitives and both endpoints.** Fix such an alpha and
put z=i alpha. For h=W^(j), define

\[
T_\alpha h(x)=e^{-zx}\int_{-\infty}^x e^{zs}h(s)ds.
\]

Every integral is absolutely convergent by (4). Integration by parts
on finite intervals and passage to their endpoints, justified by the
same integrability and vanishing bounds, gives

\[
\int_{\mathbb R}e^{zs}W^{(j)}(s)ds
=(-z)^j\int_{\mathbb R}e^{zs}W(s)ds=0.
\tag{5}
\]

For j=0 this is the exact-zero transform identity; for every fixed
higher j the same integration by parts applies. Thus

\[
T_\alpha W^{(j)}(x)
=-e^{-zx}\int_x^\infty e^{zs}W^{(j)}(s)ds.
\tag{6}
\]

For r>=0 write H_j(r)=integral_r^infinity |W^(j)(s)| ds. On x>=0
use (6); on x<=0 use the defining lower primitive and the identity
W^(j)(-s)=(-1)^j W^(j)(s). Since alpha is real, both exponential
factors have modulus one. At every x, with r=|x|, this proves

\[
|T_\alpha W^{(j)}(x)|\le H_j(r).
\tag{7}
\]

This is a uniform estimate over exact real zeros, including at x=0.
It is not asserted for approximate zeros or nonreal parameters.

The ordinary fundamental theorem of calculus at finite x gives
\((T_\alpha h)'=h-zT_\alpha h\). The one-term endpoint identity also
gives T_alpha h'=h-zT_alpha h. In particular

\[
U_\alpha=T_\alpha W,\qquad U_\alpha'=T_\alpha W'.
\tag{8}
\]

No derivative is taken through an uncontrolled remainder. Applying
the cited three-term endpoint formula separately to h=W and h=W'
gives the exact identities

\[
T_\alpha h=\frac h z-\frac{h'}{z^2}+\frac{h''}{z^3}
                -\frac{T_\alpha h'''}{z^3}.
\tag{9}
\]

The signs in (9) can also be checked by substituting three times
the one-term identity T_alpha h=h/z-T_alpha h'/z. Every substitution
here involves an integrable derivative of W, through order four.

**Cancellation and the exact scaled error.** In logarithmic coordinates
L=(1/i)(partial_x-q), so G_alpha=(1/i)(U_alpha'-qU_alpha).
Substitution of (8)-(9) cancels the coefficient (W'-qW)/z exactly.
With B=W''-qW' and J=W'''-qW'', the remaining identity is

\[
G_\alpha=\frac1i\left[
 -\frac B{z^2}
 +\frac{J-T_\alpha W^{(4)}+qT_\alpha W'''}{z^3}
 \right].
\tag{10}
\]

Because z^2=-alpha^2, the first term of alpha^2 G_alpha is F=B/i.
Using (7) in the other term yields

\[
|\alpha^2G_\alpha(x)-F(x)|
\le\frac1\alpha\left(
 |W'''(x)|+|q(x)W''(x)|+H_4(r)+|q(x)|H_3(r)
 \right).
\tag{11}
\]

Both differentiation and the q multiplication have therefore been
controlled explicitly; pointwise asymptotics alone are not used.

**A common full-line L2 envelope.** For j=1,2,3,4 set

\[
M_j=c_j\sup_{s\ge0}
 \exp\big((2j+9/2)s-(\pi/2)e^{2s}\big)<\infty,
\qquad E(r)=\exp\big(- (\pi/2)e^{2r}\big).
\]

Each supremum is finite: its continuous exponent tends to minus
infinity. Equation (4) gives |W^(j)(x)|<=M_j E(|x|). For r,t>=0,
the inequality e^(2t)>=1+2t gives

\[
H_j(r)\le M_j\int_0^\infty E(r+t)dt
\le\frac{M_j}{\pi e^{2r}}E(r).
\tag{12}
\]

Indeed E(r+t)<=E(r) exp(-pi exp(2r)t), whose full t-integral
is exactly E(r)/(pi exp(2r)). Together with L908's denominator-based
q bound, (11)-(12) give the alpha-independent envelope

\[
|\alpha^2G_\alpha(x)-F(x)|\le\frac{\mathcal B(x)}\alpha,
\qquad
\mathcal B(x)=\left(21M_3+M_4/\pi+20\pi M_2e^{2|x|}\right)E(|x|).
\tag{13}
\]

Here H_4 contributes at most (M_4/pi)E, since r>=0, and |q|H_3
contributes at most 20M_3 E. The profile itself satisfies

\[
|F(x)|\le\left(M_2+20\pi M_1e^{2|x|}\right)E(|x|).
\tag{14}
\]

Both right sides are square integrable. More explicitly, for any
fixed nonnegative a,b, substitution y=e^(2r) gives

\[
\int_{\mathbb R}(a+be^{2|x|})^2E(|x|)^2dx
=\int_1^\infty\frac{(a+by)^2}{y}e^{-\pi y}dy<\infty.
\tag{15}
\]

This includes the entire line, with no cutoff depending on alpha.
Take C=||mathcal B||_2. Equations (13)-(15) prove (2) and F in L2.
Since q(0)=0 and W''(0)<-1/6 by L906, |F(0)|>1/6.
Smoothness of W and its strict positivity make F continuous. There
is therefore a nonempty interval about zero on which |F|>1/12,
so m=||F||_2>0. This proves norm convergence to a nonzero profile,
with a finite uniform constant, rather than a merely formal expansion.

**The joint Gram limit and its quantifiers.** Put
e_alpha=alpha^2 G_alpha-F. For any two positive real zeros,
Cauchy-Schwarz and (2) give

\[
\left|\alpha^2\beta^2\langle G_\alpha,G_\beta\rangle-m^2\right|
\le mC\left(\frac1\alpha+\frac1\beta\right)
       +\frac{C^2}{\alpha\beta}.
\tag{16}
\]

This follows by expanding the inner product of F+e_alpha and
F+e_beta; each mixed term is bounded by m times the relevant error
norm, and the last by their product. If alpha,beta>=A=max{1,4C/m},
the right side is at most (1/2+1/16)m^2=9m^2/16. Taking real
parts yields (3). The same A works for every pair, without any
relation between their sizes or separation. Distinctness is needed
only when testing the symmetry criterion.

The unbounded family is imported from **Hardy's theorem**:
G. H. Hardy, *Sur les zeros de la fonction zeta(s) de Riemann*,
C. R. Acad. Sci. Paris **158** (1914), pp1012-1014, unnumbered theorem
in section1 and the positive-t conclusion in section3; primary
transcriptions [p1012](https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_158,_1914.djvu/1014)
and [p1014](https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_158,_1914.djvu/1016).
The standard theorem gives infinitely many critical-line zeros,
including arbitrarily large positive ordinates. Its completion agrees
with the local xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2.
For s=1/2+i alpha, alpha real, the elementary factors are nonzero;
Gamma(s/2) is finite and nonzero by
[DLMF5.2(i), paragraph following (5.2.1)](https://dlmf.nist.gov/5.2#i).
Thus Hardy's zeros give exactly the required positive real Xi zeros.
The nonzero entire Xi has isolated zeros, so arbitrarily large
distinct choices exist. No simplicity or indexing is needed.
The step155 assessment records that Hardy was read in a primary-paper
transcription with damaged formula typesetting, not a visually audited
facsimile; only his standard named theorem is imported, not those
damaged proof formulas. No reproof of Hardy is attempted here.

Finally, H. Hedenmalm, *Spectral interpretation of Riemann zeta zeros*,
[arXiv:2606.17494v1](https://arxiv.org/html/2606.17494v1),
Definition4.2.1 and Theorem4.2.2(b), states that pair symmetry requires
orthogonality of L-images at distinct real zeros. The hypothesis is
\(\langle LDu,Lv\rangle_2=\langle Lu,LDv\rangle_2\) on the specified
finite spectral span. Our inner product is exactly the proposed
logarithmic L2 choice for that form. L908 proves its convergence on
these real-zero images, and the source primitive is unchanged.
Selecting distinct alpha,beta>=A violates the necessary orthogonality
by (3). Hence no extension agreeing with this form on these images
can satisfy that symmetry on the full spectral span. This invokes
only the necessary real-pair implication, not its all-zero converse
or a complex-zero boundary-value characterization.

**Qualifications and traps.** The achieved estimate is (2), with a
uniform O(1/alpha) full-norm error and positive limiting norm; these
are the thresholds required for this metric test. Every use of the
upper primitive depends on an exact transform zero, and every
improper derivative integral has the bounds (4) and (12). No
floating-point zeros, finite tail truncations, assumed orthogonality,
RH, or hidden target-equivalent positivity are used. This is a local
specialization of the assessed endpoint theorem and theta bounds,
classified REPRODUCTION, with no claim of mathematical originality
beyond the sources checked. The first-pair Gram value, other positive
metrics, all-zero symmetry/completion, zero simplicity and actual-Xi
all-degree mixed positivity remain unresolved. ∎

### Independent critical audit, 9 November 2026 (step157)

The audit passes for (1)-(3), with the constants, normalization, measure
and exact-real-zero hypotheses unchanged. This verifies a local metric
obstruction; it neither strengthens the theorem nor claims progress
beyond the assessed sources. The prior SPECIALIZE assessment is reused.
The complete proof above and the load-bearing proofs in L906-L908(1)-(3)
were inspected. Their prior source assessments and audits supply the
cited source statements; no fresh literature comparison or reproof of
Hardy's theorem is claimed. L908's step154 addition is not used.

**Primitive identities and endpoint hypotheses.** For fixed real alpha,
every W^(j) is absolutely integrable and tends to zero at both ends
by (4). Integration by parts over finite intervals therefore has a
vanishing boundary term at either infinite endpoint. The full transform
of W^(j) is (-i alpha)^j times that of W, and hence is exactly zero.
This checks (5) for every derivative needed, including j=4; the upper
primitive in (6) is available for all of them, not just for W.
For x<=0, reflection of the absolute lower integral gives H_j(-x),
using the parity (-1)^j of W^(j). For x>=0, the absolute upper integral
gives H_j(x). The unit-modulus factors use reality of alpha. Both bounds
include x=0 and hold uniformly over the exact real-zero family.

For h=W^(j), differentiating the finite endpoint gives
(T_alpha h)'=h-zT_alpha h, while integration by parts once gives
T_alpha h'=h-zT_alpha h. Thus (8) is exact. Iterating
T_alpha h=h/z-T_alpha h'/z three times yields precisely (9),
including the last negative sign and the power z^(-3). Applying
this identity to W' uses W^(4), whose full derivative-tail bound
has already been checked. There is no differentiated asymptotic error,
no uniformity in a complex parameter, and no use of approximate zeros.

**Cancellation, signs and full norm control.** The convention
phi(e^x)=-log W(x) gives L=(1/i)(partial_x-q). The leading z^(-1)
coefficient is W'-qW=0. The next coefficient inside the brackets is
-(W''-qW')/z^2, and the last is
(W'''-qW''-T_alpha W^(4)+qT_alpha W''')/z^3.
Since z^2=-alpha^2 and |z|=alpha, this gives F=-i(W''-qW')
and exactly the magnitude bound (11). In particular the sign of F
does not come from treating D as an ordinary real derivative.

Each M_j is finite for j=1,2,3,4, by the displayed continuous exponent
tending to minus infinity. For every r,t>=0,
E(r+t)/E(r)<=exp(-pi exp(2r)t); its full t-integral gives (12).
Multiplication by |q|<=20pi exp(2r) turns H_3 into at most 20M_3 E,
whereas W''' contributes M_3 E. The other two terms are bounded by
(M_4/pi)E and 20pi M_2 exp(2r)E. This independently checks every
coefficient in (13), retaining the unbounded q factor throughout.
The same calculation with W'' and qW' gives (14).

The full-line norm integral in (15) has no omitted factor: reflection
gives 2 integral_0^infinity, and y=exp(2r) contributes dy/(2y).
Its remaining integrand is (a+by)^2 exp(-pi y)/y on [1,infinity),
which is integrable at both ends. This establishes a single finite C
independent of alpha, with no moving cutoff or unproved exchange of a
norm limit and an integral. Positivity of W makes F continuous.
The audited L906 curvature bound and q(0)=0 give |F(0)|>1/6;
continuity supplies an interval of positive length where |F|>1/12.
Thus m is finite and strictly positive, without a numerical norm bound.

**Joint threshold and the form domain.** Expanding
<F+e_alpha,F+e_beta> with the stated first-argument-linear convention
gives two cross terms of absolute values at most m||e_alpha|| and
m||e_beta||, and one term at most ||e_alpha||||e_beta||.
At alpha,beta>=max{1,4C/m}, each error norm is at most m/4, so
the total deviation from m^2 is at most 9m^2/16. Hence its real part
is at least 7m^2/16. Dividing by the positive alpha^2 beta^2 proves
(3). The same threshold works for all pairs simultaneously; no bound
on their ratio or spacing is present. Hardy's cited infinitude theorem
and the nonzero entire completion provide distinct pairs beyond it.
The completion factors at s=1/2+i alpha are finite and nonzero, so
the audited Xi/2 normalization does not change this zero family.

There is no hidden invariance requirement D(H_finite) subset H_finite.
Indeed L907's exact ODE gives Du_alpha=-alpha u_alpha+w/i, and
L906 gives Lw=0. Therefore LDu_alpha=-alpha Lu_alpha directly in
the smooth domain. Both LDu_alpha and Lu_alpha belong to logarithmic
L2, the former being a scalar multiple of the latter. The same holds
for any finite combination of the two selected real-zero generators,
so every inner product used in the symmetry test is defined.
For distinct real alpha,beta, the two sides of pair symmetry would be
-alpha <G_alpha,G_beta> and -beta <G_alpha,G_beta>, respectively.
They cannot agree because (3) makes this Gram entry nonzero. This
checks the necessary implication of the cited Definition4.2.1 and
Theorem4.2.2(b) at precisely the tested domain, without assuming the
source's all-zero converse, a closed realization, or RH.

Consequently the previously provisional logarithmic L2 metric stop
can be retained as audited. Other metrics, the first-pair Gram value,
all-zero symmetry/completion and actual-Xi mixed positivity remain
open. The argument neither excludes all nonlocal forms nor establishes
that an unbounded metric is necessary. No additional lemma, numerical
threshold, mathematical script or dependency is introduced by this audit.

## Mathlib

Full matching coverage for this theta common-profile and symmetry
obstruction is not checked. Supporting endpoint-expansion, improper
integration and Hilbert-norm implementation coverage is also unchecked;
no absence claim is made. This proof uses the cited standard theorems
and the canonical local estimates, not a Lean implementation.
