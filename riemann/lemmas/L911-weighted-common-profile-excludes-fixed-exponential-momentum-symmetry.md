# L911: the common profile excludes the fixed exponential-momentum symmetry

## Hypotheses

Keep the functions and normalization of L906-L908 unchanged. Thus
W(x)=w(e^x), q=W'/W, U_alpha(x)=u_alpha(e^x), and
G_alpha(x)=(Lu_alpha)(e^x), with

\[
L=\frac1i(\partial_x-q),\qquad
U_\alpha(x)=e^{-i\alpha x}\int_{-\infty}^x e^{i\alpha s}W(s)\,ds,
\qquad \int_{\mathbb R}e^{i\alpha s}W(s)\,ds=\Xi(\alpha)/2.
\]

Use L910's unitary Fourier convention and fixed form domain

\[
Q=\left\{f\in L^2(\mathbb R):
  \int_{\mathbb R}e^{-k/4}|\mathcal F f(k)|^2\,dk<\infty\right\},
\quad
b(f,g)=\int_{\mathbb R}e^{-k/4}\mathcal F f(k)
                     \overline{\mathcal F g(k)}\,dk,
\quad \|f\|_Q^2=b(f,f).
\]

This is the positive form of M=exp(-P/4), linear in its first
argument; Q denotes Dom(M^(1/2)), not Dom(M). No completeness for
the displayed form norm alone is assumed. Retain the full finite
span of generators at every complex Xi zero, as in L907 and L910.
The asymptotic estimates below concern positive real exact zeros
alpha. No RH, simplicity, spacing, numerical zero approximation,
pair symmetry or completion is assumed. L908(1), not its step154
addition, supplies the normalization. L909 and L910 are used with
their audited qualifications.

## Conclusion

The unchanged profile of L909,

\[
F(z)=\frac1i\left(W''(z)-\frac{W'(z)^2}{W(z)}\right),
\tag{1}
\]

has its trace on the real line in Q, with 0<m=||F||_Q<infinity.
There is a finite C, depending only on W and the fixed form, such that
every positive real exact Xi zero alpha satisfies

\[
\|\alpha^2G_\alpha-F\|_Q\le C/\alpha.                    \tag{2}
\]

With A=max{1,4C/m}, every pair of positive real exact zeros
alpha,beta>=A satisfies

\[
\operatorname{Re}b(G_\alpha,G_\beta)
\ge\frac{7m^2}{16\alpha^2\beta^2}>0.                    \tag{3}
\]

Hardy's theorem provides distinct such pairs. Consequently this fixed
form fails Hedenmalm's necessary pair-symmetry condition on the full
finite spectral span, although L910 retains every complex-zero image
in its domain. This is a metric obstruction, not a disproof of RH or
of the source's conditional theorem. No effective numerical onset,
claim about another metric, or actual-Xi mixed-positivity result is
obtained. The separate step164 conceptual audit below passes for these
claims, with the hypotheses, constants and conclusions unchanged.

## Proof

**Source use and the application difference.** Reuse the approved
step162 SPECIALIZE assessment. The standard inputs are NIST DLMF
[2.3(i), (2.3.4)-(2.3.6)](https://dlmf.nist.gov/2.3#i), the finite-order
Fourier endpoint expansion with its absolute derivative remainder;
[1.9(iii), (1.9.29)-(1.9.31)](https://dlmf.nist.gov/1.9#iii), Cauchy's
theorem and derivative formula; and G. Teschl, *Mathematical Methods
in Quantum Mechanics*, February 12, 2009 version, GSM99,
[(3.50)-(3.51), p97, Theorem7.5 and its preceding L1/L2 compatibility
paragraph, p164](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
The positive spectral form and its domain are already fixed in L910.
These sources do not themselves supply (2). The application work is
the uniform derivative/tail estimate after multiplication by q, and
the justified Fourier transfer of the profile and its error. No
general endpoint, spectral-calculus or Plancherel theorem is reproved.

**Uniform derivatives in a narrower strip.** L910 proves that W is
holomorphic on |Im z|<pi/4, has no zeros on |Im z|<=1/4, and, with
c=7pi/8 and r=|x|, obeys

\[
|W(x+iy)|\le4\pi^2 e^{9r/2-c e^{2r}},\qquad
|q(x+iy)|\le24\pi e^{2r}\quad (|y|\le1/4).              \tag{4}
\]

Set delta=1/16 and a=c exp(-2delta)/2>0. For |Im z|<=1/8, the
closed circle of radius delta about z lies in |Im z|<=3/16<1/4.
If Re z=x, r=|x|, and zeta is on or inside that circle, then

\[
|\operatorname{Re}\zeta|\le r+\delta,\qquad
|\operatorname{Re}\zeta|\ge r-\delta.
\]

The second inequality remains useful when r<delta: exponentiation
still gives exp(2|Re zeta|)>=exp(2r-2delta). Consequently (4) bounds
W on that whole circle by

\[
K\exp(9r/2-2a e^{2r}),\qquad K=4\pi^2e^{9\delta/2}.
\]

All Cauchy-formula hypotheses hold on these disks. For j=0,1,2,3,4,
put

\[
S=\sup_{r\ge0}\exp(9r/2-ae^{2r})<\infty,\qquad
M_j=j!\delta^{-j}KS,\qquad E(r)=e^{-a e^{2r}}.
\]

The supremum is finite because its continuous exponent tends to
minus infinity. The derivative formula (and the direct bound for
j=0) therefore gives, uniformly on the entire narrower closed strip,

\[
|W^{(j)}(x+iy)|\le M_j E(|x|),\qquad |y|\le1/8.         \tag{5}
\]

These envelopes are integrable, and all the derivatives vanish at
both real endpoints uniformly in y. Their full tails satisfy

\[
\int_0^\infty M_j E(r+t)\,dt
\le\frac{M_j}{2a e^{2r}}E(r),\qquad r\ge0,               \tag{6}
\]

because exp(2t)>=1+2t implies
E(r+t)<=E(r) exp(-2a exp(2r)t). No tail is truncated.

**Exact shifted derivative primitives.** Fix a positive real exact
zero alpha and a height |y|<=1/8. Write lambda=i alpha and
h_j(x)=W^(j)(x+iy). L910's horizontal contour identity gives

\[
\int_{\mathbb R}e^{i\alpha x}h_0(x)\,dx
=e^{\alpha y}\Xi(\alpha)/2=0.
\]

For 1<=j<=4, integration by parts on finite intervals, followed by
the absolutely convergent endpoint limits justified by (5), gives

\[
\int_{\mathbb R}e^{\lambda x}h_j(x)\,dx
=(-\lambda)^j\int_{\mathbb R}e^{\lambda x}h_0(x)\,dx=0.   \tag{7}
\]

Define the absolutely convergent primitives

\[
T_j(x)=e^{-\lambda x}\int_{-\infty}^x e^{\lambda s}h_j(s)\,ds
      =-e^{-\lambda x}\int_x^\infty e^{\lambda s}h_j(s)\,ds.
\tag{8}
\]

Their equality follows from (7), including for j=4. The lower
primitive in L910(7), after factoring out the common imaginary-height
phase, is precisely U_alpha(x+iy)=T_0(x). There is no surviving
exp(alpha y) factor in T_0. For x<=0 use the first integral in (8),
and for x>=0 the second. The real-frequency phase has modulus one,
and the real part of the argument runs toward an endpoint with
absolute value r+t. Equations (5)-(6) prove the joint uniform bound

\[
|T_j(x)|\le\frac{M_j}{2a e^{2r}}E(r),\qquad
0\le j\le4,\quad r=|x|,\quad |y|\le1/8.                \tag{9}
\]

The contour equality used to obtain (7) is a fixed-alpha identity
already justified in L910; no uniform contour error is assumed.
The final bound (9) is independent of alpha and y, because only
horizontal unit-modulus phases remain. Exact transform zeros are
essential to the upper-end representation.

Differentiating the finite endpoint of the lower primitive gives
T_j'=h_j-lambda T_j. A one-step endpoint integration by parts also
gives T_(j+1)=h_j-lambda T_j for j<=3. Thus
U_alpha'(x+iy)=T_1(x), with the prime the holomorphic derivative.
The hypotheses of the cited three-term endpoint formula hold:
the requisite derivatives vanish at the infinite endpoint and their
Fourier integrals converge absolutely, uniformly in real frequency,
by (5). Its complex amplitudes can be treated componentwise. Its
exact remainder here is

\[
T_j=\frac{h_j}{\lambda}-\frac{h_{j+1}}{\lambda^2}
     +\frac{h_{j+2}}{\lambda^3}-\frac{T_{j+3}}{\lambda^3},
\qquad j=0,1.                                           \tag{10}
\]

The signs follow by three substitutions of
T_j=h_j/lambda-T_(j+1)/lambda. Formula (10) is applied separately
to W and W'; no asymptotic remainder is differentiated.

**Cancellation and the full weighted-tail envelope.** At z=x+iy,
put B=W''-qW' and J=W'''-qW''. Substituting (10) in
G_alpha=(U_alpha'-qU_alpha)/i cancels W'-qW exactly and gives

\[
G_\alpha(z)=\frac1i\left[
  -\frac{B(z)}{\lambda^2}
  +\frac{J(z)-T_4(x)+q(z)T_3(x)}{\lambda^3}\right].       \tag{11}
\]

Since lambda^2=-alpha^2, the leading scaled term is F=B/i, with
the same sign and normalization as L909. Combining (4), (5) and
(9), define

\[
b_0=\left(1+\frac{12\pi}{a}\right)M_3+\frac{M_4}{2a},
\qquad b_1=24\pi M_2,\qquad
\mathcal B(x)=(b_0+b_1e^{2|x|})E(|x|).
\]

Then for every such alpha and every |y|<=1/8,

\[
|\alpha^2G_\alpha(x+iy)-F(x+iy)|\le\mathcal B(x)/\alpha,
\tag{12}
\]

because W''' contributes M_3 E, qW'' contributes
24pi M_2 exp(2r)E, T_4 contributes at most M_4 E/(2a),
and qT_3 contributes 12pi M_3 E/a. In particular the unbounded
q factor has been included in both places where it occurs. Also

\[
|F(x+iy)|\le(M_2+24\pi M_1e^{2|x|})E(|x|).              \tag{13}
\]

For any nonnegative finite d_0,d_1, the full-line norm integral is

\[
\int_{\mathbb R}(d_0+d_1e^{2|x|})^2 E(|x|)^2\,dx
=\int_1^\infty\frac{(d_0+d_1t)^2}{t}e^{-2at}\,dt<\infty.
\tag{14}
\]

Splitting into two half-lines and substituting t=exp(2r) gives this
identity, including its factor. The unsquared integral is likewise
integral_1^infinity (d_0+d_1t)exp(-at)dt/t<infinity. Both envelopes
tend to zero at either endpoint uniformly in y.

**Fourier transfer for the new functions and positive profile norm.**
The function F is holomorphic on |Im z|<1/4 by the nonvanishing of W.
For each fixed alpha, so is e_alpha=alpha^2G_alpha-F, by L910.
Equations (12)-(14) give real and shifted L1/L2 traces of both
functions and vanishing vertical limits uniformly for |y|<=1/8.
For each of these two functions f, apply Cauchy's theorem to
f(z)exp(-ikz) on the finite rectangle with endpoints +/-T and
heights 0,y, where 0<=y<=1/8 and k is fixed real. On a vertical
side the extra factor has modulus at most exp(|k|/8); the preceding
envelopes make its integral tend to zero. Both horizontal integrals
converge absolutely. Thus the orientations and exp(-ik(x+iy))=
exp(ky)exp(-ikx) give the pointwise L1-transform identity

\[
\mathcal F(f(\,\cdot+iy))(k)=e^{-ky}\mathcal F(f|_{\mathbb R})(k).
\tag{15}
\]

L1/L2 compatibility and Plancherel from the cited Teschl theorem
apply to the already established L1/L2 traces. At y=1/8, (15)
therefore proves, for f=F and f=e_alpha separately,

\[
f|_{\mathbb R}\in Q,\qquad
\|f\|_Q=\|f(\,\cdot+i/8)\|_2.                          \tag{16}
\]

There is no interchange of a k integral with a limiting contour, and
no assumption of a formal imaginary translation for arbitrary L2
functions. Squaring exp(-k/8) yields exactly the form weight
exp(-k/4). Equations (12), (14) and (16) prove (2) with the single
finite constant C=||mathcal B||_2, independent of alpha.

L909 proves that the real-line profile F is nonzero in L2, using
W'(0)=0 and W''(0)<-1/6 from L906, followed by continuity. If
m=||F||_Q were zero, the strictly positive Fourier weight would
force mathcal F F=0 almost everywhere. Plancherel would then force
F=0 in L2, a contradiction. Thus 0<m<infinity. This argument
does not require a numerical lower bound for the shifted trace.

**Simultaneous Gram bound and the fixed-metric obstruction.**
Cauchy-Schwarz holds for b by its weighted-L2 representation,
regardless of completeness of Q in the form norm. For two positive
real exact zeros, expanding b(F+e_alpha,F+e_beta) gives

\[
\left|\alpha^2\beta^2 b(G_\alpha,G_\beta)-m^2\right|
\le mC\left(\frac1\alpha+\frac1\beta\right)
       +\frac{C^2}{\alpha\beta}.                        \tag{17}
\]

At alpha,beta>=A=max{1,4C/m}, the right side is at most
(1/2+1/16)m^2=9m^2/16. Taking real parts and dividing by the
positive alpha^2 beta^2 proves (3). The same threshold works for
all pairs, with no restriction on their ratio or spacing.

Import **Hardy's theorem**, G. H. Hardy, *Sur les zeros de la fonction
zeta(s) de Riemann*, C. R. Acad. Sci. Paris **158** (1914),
pp1012-1014, the unnumbered theorem in section1 and positive-t
conclusion in section3. Primary-paper transcriptions:
[p1012](https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_158,_1914.djvu/1014),
[p1014](https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_158,_1914.djvu/1016).
Reuse L909's audited applicability argument: the local completion's
elementary and gamma factors are finite and nonzero at the positive
critical-line ordinates, and the nonzero entire Xi has isolated zeros.
Hardy therefore supplies arbitrarily large distinct positive real
exact Xi zeros. The source assessment inspected a transcription with
damaged formula typesetting, not a visually audited facsimile; only
the standard named theorem is imported, not those damaged proof
formulas. No simplicity, zero count or effective onset is imported.

H. Hedenmalm, *Spectral interpretation of Riemann zeta zeros*,
[arXiv:2606.17494v1, Definition4.2.1 and Theorem4.2.2](https://arxiv.org/html/2606.17494v1#S4.SS2),
requires pair symmetry
b(LDu, Lv)=b(Lu, LDv). L907's exact ODE and L906's Lw=0 give
LDu_alpha=-alpha Lu_alpha. By L910 every complex-zero image and
its scalar multiple belongs to Q, so both sides of the test are
defined on the full finite span. For a pair of generators symmetry
would imply

\[
(\overline\beta-\alpha)b(G_\alpha,G_\beta)=0.             \tag{18}
\]

For the distinct real pair just obtained, (3) contradicts (18).
Thus no extension agreeing with this fixed form on these images can
meet the specified symmetry. D-invariance of H_finite is unnecessary:
LDu_alpha is defined in the smooth domain and is already the stated
scalar multiple. Nonreal generators have not been discarded or
assumed absent; their domain membership is precisely L910's input.

**Qualifications.** The achieved O(1/alpha) full form-norm estimate
and the actual nonzero distinct-zero Gram entry meet the proposed
diagnostic threshold. This is not a failed-estimate argument or a
finite-frequency observation. All improper derivative endpoints and
Fourier rectangles have complete integrable envelopes, and the
normalization and q factors are retained. This is REPRODUCTION of an
assessed endpoint/Fourier mechanism specialized to this theta family;
no originality beyond the sources checked is claimed. Other metrics,
completion, multiplicities beyond the specified repeated generators,
all-zero symmetric realizations, and actual-Xi all-degree mixed
positivity remain open. The dt/t stop of L909 is preserved separately.

### Independent conceptual audit, 9 November 2026 (step164)

The audit passes for (1)-(3) and the stated fixed-form obstruction.
This validates the previously provisional local specialization; it is
not a new metric theorem, a stronger estimate or progress beyond the
sources assessed in step162. That unchanged SPECIALIZE coverage is
reused. The complete L911 and L910 proofs, L909's nonzero-profile and
Hardy applicability arguments, and the defining/ODE/normalization
ranges of L906-L908 were checked. L908's step154 addition is excluded.

**Strip geometry and complete derivative tails.** The radius 1/16 disk
about a point of |Im z|<=1/8 stays in |Im zeta|<=3/16, strictly inside
the zero-free closed strip from L910. Analyticity on an open neighborhood
of the disk, including its boundary, is therefore available. If r=|Re z|,
the two real-part bounds used in the proof hold also when r<delta;
in particular exp(2|Re zeta|)>=exp(2r-2delta) does not require a positive
lower bound for r-delta. Substitution in L910's envelope gives exactly
K exp(9r/2-2a exp(2r)), with 2a=c exp(-2delta). Splitting off
exp(9r/2-a exp(2r)) and taking its finite supremum proves (5) by
the cited Cauchy derivative formula, including j=4. The j=0 case
uses the same upper bound without differentiation.

The full tail ratio is E(r+t)/E(r)=exp(-a exp(2r)(exp(2t)-1)),
which is bounded above by exp(-2a exp(2r)t) for every r,t>=0.
Integrating this majorant on [0,infinity) gives exactly (6), including
the factor 2a exp(2r). It proves absolute integrability and uniform
vanishing of all four derivative endpoints. No unbounded spatial
interval or joining point r=0 is omitted.

**Exact phases, derivative cancellation and the endpoint remainder.**
In L910(7), for real alpha and z=x+iy, the outside factor is
exp(-i alpha x)exp(alpha y), whereas the horizontal integrand contains
exp(i alpha s)exp(-alpha y)W(s+iy). These height factors cancel
exactly before taking absolute values. Thus U_alpha(x+iy)=T_0(x),
not exp(alpha y)T_0(x). The full shifted W transform is
exp(alpha y)Xi(alpha)/2, hence is zero at the assumed exact zero.
Applying finite-interval integration by parts successively, with the
vanishing boundaries and absolute integrability just verified, proves
(7) through j=4. In particular the T_4 upper primitive is justified;
no fifth derivative is needed for this cancellation.

For x<=0 the lower primitive integrates only positions whose real
absolute value is r+t, and for x>=0 the upper primitive has the same
property. Unit modulus of the horizontal phase uses alpha real.
This proves (9) uniformly in both alpha and y, even though the earlier
contour identity was proved for each fixed alpha. For j<=3, integration
by parts gives T_(j+1)=h_j-lambda T_j; differentiating the finite
endpoint gives the identical expression for T_j'. Three substitutions
therefore give (10), with the negative remainder T_(j+3)/lambda^3.
Its j=1 application uses only the already bounded T_4. The two endpoint
expansions are exact identities; neither differentiates a remainder.

Substituting them in (U'-qU)/i cancels the coefficient
(W'-qW)/lambda and leaves -B/lambda^2 plus
(J-T_4+qT_3)/lambda^3. Since lambda^2=-alpha^2 and
|lambda|=alpha>0, the scaled leading term is B/i, with error at most
(|J|+|T_4|+|qT_3|)/alpha. The four contributions to its envelope are
M_3 E, 24pi M_2 exp(2r)E, M_4 E/(2a exp(2r)), and
12pi M_3 E/a. Replacing exp(-2r) by 1 in the third term gives
exactly b_0,b_1 as printed. Both unbounded q factors are retained;
there is no use of a bound on q alone that is uniform in x.

**Whole-line norms and the Fourier passage.** The same envelopes give
(13). In (14), the two equal half-lines supply a factor 2, while
t=exp(2r) supplies dt/(2t). These cancel, leaving precisely the
displayed integral over [1,infinity). The unsquared integral has the
same cancellation. The resulting exponential-polynomial functions
are integrable and vanish at both spatial ends. Thus F and, for each
fixed alpha, e_alpha have both L1 and L2 traces and uniform vertical
decay on the full band between 0 and 1/8. Their holomorphic extensions
come from the zero-free denominator and L910, not from a formal L2
translation operation.

For each fixed real k, the additional factor on the vertical sides is
bounded by exp(|k|/8); the established envelope still tends to zero.
The rectangle orientation gives the real-line transform as exp(ky)
times the shifted-line transform, so the multiplier in (15) is
exp(-ky). First proving this identity for the absolutely convergent
L1 transforms avoids any interchange with an integral over k.
The cited L1/L2 compatibility and Plancherel then apply to the already
L2 shifted trace. At y=1/8 the squared multiplier is exp(-k/4).
This verifies (16) separately for F and e_alpha, on the form domain
Dom(M^(1/2)), without needing Dom(M) or completeness in ||.||_Q.
Consequently the single C=||mathcal B||_2 proves the advertised uniform
rate (2), on the whole line and for every positive real exact zero.

L906 gives W'(0)=0 and W''(0)<-1/6, so F(0) is nonzero; L909's
continuity argument establishes a nonzero real-line L2 function.
The Fourier weight is strictly positive everywhere, so zero form
norm would force its Fourier transform to vanish almost everywhere.
Plancherel would contradict that nonzero function. This checks
0<m<infinity without assuming F is real-valued or needing an effective
numerical norm lower bound.

**Joint quantifiers and the actual pair test.** Weighted Cauchy-Schwarz
bounds the two mixed terms by mC/alpha and mC/beta, and the error-error
term by C^2/(alpha beta). For both zeros beyond max{1,4C/m}, each
error norm is at most m/4, giving total deviation at most 9m^2/16
from m^2. Its real part is therefore at least 7m^2/16. Dividing by
alpha^2 beta^2 yields (3) for every such pair simultaneously, without
a relation between their sizes or a simplicity/spacing premise.
Hardy's precise named theorem and the completion qualification quoted
above supply arbitrarily large distinct positive real exact Xi zeros.
Only the theorem is imported; the damaged primary-transcription proof
formulas remain unused.

The smooth ODE gives Du_alpha=-alpha u_alpha+w/i, and Lw=0 gives
LDu_alpha=-alpha G_alpha. L910 places every complex-zero G_alpha in Q;
scalar multiples and finite combinations are also in Q. Both sides
of the required pair symmetry are thus defined. With the form linear
in its first argument their difference is
(conjugate(beta)-alpha)b(G_alpha,G_beta), exactly (18). For the
distinct real pair provided by Hardy, (3) makes it nonzero. This uses
no D-invariance of the finite primitive span and no restriction of
that span to a conjecturally real zero set.

The fixed exp(-P/4) form is therefore retired at its stated scope.
L906-L910 remain exactly the direct local inputs recorded in the DAG;
the audit adds none. No error, changed constant, effective onset,
numerical certificate, or new general theorem was found or supplied.
Other metrics, completion, generalized vectors and actual-Xi all-degree
mixed positivity remain unresolved. The distinct dt/t stop is preserved.

## Mathlib

Full matching coverage for this weighted theta profile and metric
obstruction is unchecked. Supporting Cauchy-formula, endpoint,
Fourier-domain and weighted-inner-product coverage is also unchecked;
no absence claim is made. This is an informal analytic proof using
the precise cited inputs, not a Lean implementation.
