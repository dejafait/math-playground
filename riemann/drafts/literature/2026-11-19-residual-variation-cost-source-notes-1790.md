# Fixed-interval variation-cost source review1790

19 November 2026. Working source record for assessment1789; literature only.
No mathematical bound is established and no lemma or script is changed.

## Purpose and current comparison

Main gap: L030-L032/C032a actual-Xi all-degree positivity. Intermediate
target: an explicit positive dependence on a finite width-variation cap
for the original residual's uniform Laplace approximation error on [1,2].
This would constrain cancellation costs for approximate law realizations;
actual-Xi realization and signed-height payment would still be missing.

Read C033i/j/l hypotheses and conclusions and C033r's parameter selection,
kernel, signed-tail, residual-side and transform-division proof passages;
read C033p's local Lipschitz conclusion. Reused Gaver source/proof coverage
in notes1774 and the qualified range-exclusion framework, without a new
source-wide or zero-data audit. The fixed cap2 result and freely located
Gaver samples are not already a rate on the prescribed interval [1,2].

Primary statements inspected: Lederman--Steinerberger,
arXiv:1605.03866v1, Theorems1/2, pp2-3, and relevant Sections4/5 proof
cases; Saitoh--Tuan--Yamamoto, ZAA20 (2001), pp193-202,
Theorems1/2, p194, and Section3's global-data bound, pp198-200;
Trefethen, BIT60 (2020), pp901-915, Lemma2.1, Theorem3.1 with proofs,
pp904-906, Theorems4.1/5.2 and Section7. These give different hypothesis
interfaces. Global Sobolev/weighted inverse estimates cannot simply be
applied to signed measures with atoms and a local density jump.

Bounded analytic continuation is a prospective alternative: use known
strip and disk estimates on the original transform difference, then
connect to a separately justified variation-dependent Gaver witness.
No new exponent, variable-cap extension or assembled lower bound is
established here. This source review is complete; its narrower continuation
requires separate approval before research.

## Inspected primary statements and essential proof cases

1. Roy R. Lederman and Stefan Steinerberger, *Stability Estimates for
Truncated Fourier and Laplace Transforms*,
[arXiv:1605.03866v1, 12 May 2016](https://arxiv.org/pdf/1605.03866).
Theorem1, pp2-3, assumes a real H^1 function on a compact positive
time interval and observes its transform on the whole positive axis.
Theorem2, p3, observes the transform on [a,b], 0<a<b, but assumes a real
H^2 function on the whole positive time axis. Its exponential lower bound
depends on the ratios of ||t f''||_2, ||t f'||_2, ||t f||_2 and ||f||_2.
Read Section4's derivative-energy/root and no-root cases, pp7-9, and
Section5, pp9-10: the latter uses weighted second-derivative energy and
low spectral mass. These are load-bearing global assumptions. Neither
the TV of a measure nor a local Lipschitz density bound supplies them.
No theorem from this paper is imported into the argument.

2. S. Saitoh, Vu Kim Tuan and M. Yamamoto, *Conditional Stability of a
Real Inverse Formula for the Laplace Transform*, Z. Anal. Anwend.20(1)
(2001), 193-202, DOI10.4171/ZAA/1010,
[publisher PDF](https://ems.press/content/serial-article-files/35168?nt=1).
Theorems1/2, p194, control a function on an interior time interval using
supremum transform data on (0,infinity), not [1,2]. Theorem1 imposes two
Bergman--Selberg bounds, with 1/4<q<1 and
max{1/2,2q-1}<alpha<min{1,2q}; Theorem2 gives sufficient C^1,
F(0)=0 and weighted L^2 derivative hypotheses. Read (1.1)-(1.6),
Propositions1/2, pp195-196, and Section3, pp198-200: the finite inversion
integral and its bound (3.1) use the entire positive data axis; (3.2)
balances that global error against the regularity remainder. This is
not an interval-data theorem for an atomic signed measure. No import.

3. Lloyd N. Trefethen, *Quantifying the ill-conditioning of analytic
continuation*, BIT Numer. Math.60 (2020), 901-915,
DOI10.1007/s10543-020-00802-7,
[published author PDF](https://people.maths.ox.ac.uk/trefethen/trefethen_ac.pdf).
Read Lemma2.1 and complete proof, p904: a holomorphic function bounded
by one in 0<Re w<1, with uniform limiting bound epsilon on Re w=0,
obeys |h(w)|<=epsilon^(1-Re w). The proof uses bounded-strip
Phragmen--Lindelof after exponential normalization; a bare unbounded-domain
maximum principle would not suffice. Read Theorem3.1 and complete proof,
pp904-905: inside a disk of radius R>1, a holomorphic function bounded
by one and bounded by epsilon on the unit disk obeys
|g(z)|<=epsilon^(1-log|z|/log R), 1<|z|<R. The proof composes
with z=exp(w log R) and applies Lemma2.1. These exact known estimates
are the proposed imports, rather than new theorems to reprove.

Also read Section4's conformal map, (4.1)-(4.5)/Theorem4.1, pp906-907,
and Theorem5.2 with proof, p908. The former starts from a vertical end
segment, not our real interior segment. The latter supplies a positive
geometry-dependent exponent through a thin tube and an unspecified
conformal map, not the requested explicit node dependence. Therefore
neither is by itself the complete rate application. Section7,
Theorem7.1/proof, pp911-912, assumes initial disk data and sufficiently
small epsilon, and invokes a numerical search for an auxiliary
inequality. It is unnecessary here and is not imported. Finite exact
applications of Theorem3.1 avoid that asymptotic/numerical passage.

4. Ante Mimica, *Laplace transform*, Dresden course, 27 April-1 May2015,
[author notes](https://web.math.pmf.unizg.hr/~amimica/lt.pdf),
Remark1.2(i), Proposition1.4(i) and its proof, printed pp5-7.
Coverage1756 is reused; the source was checked again specifically for a
complex-extension statement. The inspected theorem states real smoothness
and exponentially damped derivatives for positive measures. It must not
be cited as already stating holomorphy for arbitrary signed measures.
That routine applicability obligation remains: apply the standard
holomorphic differentiation-under-the-integral theorem (or Morera with
Fubini and dominated convergence) to a finite variation measure on
compact subsets of Re z>0. No moments at zero may be substituted.

## Hypothesis comparison and bounded continuation

The width parameter's compact support is not compact support of a law
on the time half-line. The forward kernel in width is exp(-B_sigma(s)),
not exp(-sigma*s), so the truncated-Laplace theorem cannot be applied
with width as its time variable. C033j/r give signed deconvolution,
a zero atom and one-sided density information; they give no global H^2
or Bergman--Selberg norm for the relevant difference. Applying the
theorem to the original laws instead would require separate global
regularity and tail proofs, and would not avoid paying deconvolution.
These mismatches reject direct import, not the existence of d(V)>0.

The nominated intermediate test is instead a generic finite-node
propagation bound for the Laplace transform of a finite real signed
measure on [0,infinity). Desired inputs are a positive TV allowance M,
an error epsilon on [1,2], and an arbitrary prescribed finite positive
node set. Desired output is an explicitly specified exponent in (0,1]
controlling all those node values in terms of M and epsilon/M. This is
a target, not a bound derived or verified in this source-review turn.

The inspected strip lemma permits an interval-to-small-complex-region
test through a Joukowski/annular parametrization; Theorem3.1 permits
finite disk propagation from that region. The remaining application
must give all maps, domains, branch/boundary checks, disk overlaps,
iteration counts, endpoint cases and norm normalization explicitly.
It must handle nodes below1 as well as nodes above2, without leaving
Re z>0. This is why merely citing Theorem5.2 is insufficient. The standard
source estimates are imported; only this application is proposed.

If successful, the bridge could later combine with a separately proved
cap-V version of C033r and its coefficient/division allowance to constrain
d(V). C033r is currently only stated for cap2. Neither changing2 to V
nor selecting shrinking centers is authorized by its conclusion. The
dependence of its local modulus/parameters on V, full signed-tail and
atom bounds, and amplification by 1/d(s_i) remain future obligations.
Even a parameterized rate in existing generally nonnumerical constants
would not be a numerically evaluated or universal V-only rate.

Continue the nominated proof only if it produces a finite positive
explicit exponent for every finite node set and finite M, with full
domain and boundary justification. Abandon that construction if it
requires unknown moments, global density regularity, an unspecified
conformal map, or an unquantified sufficiently-small-data threshold.
No observable, quadrature, adaptive cutoff or Xi transfer is involved.

## Searches, duplicates, failures and limitations

Queries actually issued: `inverse Laplace transform conditional stability
finite interval measure bounded variation logarithmic stability`;
`truncated Laplace transform stability estimates Lederman Steinerberger
lower bounds`; `Trefethen quantifying ill conditioning analytic continuation
theorem harmonic measure slit 2020 pdf`; `analytic continuation small
interval bounded half plane harmonic measure two constants theorem
quantitative Laplace transform measures`; `"Laplace" "signed measures"
"stability" "interval"`; `"Laplace transform" "jump" "analytic continuation"
stability`; `bounded analytic function small real interval Bernstein
ellipse two constants theorem`. Search results are leads only.

Optional leads: *Regularization of the inverse Laplace transform by
Mollification*, arXiv:2304.08057, HTMLv2 returned404; theorem/proof unread.
Grabovsky--Hovsepyan, *Analytic continuation in an annulus and in a
Bernstein ellipse*, arXiv:1812.07068, PDF returned404; theorem/proof
unread. A Temple dissertation ellipse theorem appeared in search results
but was not inspected and is not imported. Neither failed access is
essential to the strip/disk test; do not repeat access attempts merely
to broaden this review. No novelty or optimality inference is made.

Local duplicate/failure checks were confined to November19 residual
assessments, November18 bounded-variation assessments, C033i/j/l/p/r,
notes1774/1756 and selected stop files. C033l gives qualitative freely
located separation; C033n concerns nearby real data perturbations;
C033r has freely located finite nodes. None of those inspected statements
is the proposed fixed-interval propagation estimate. Stops1571/1576 and
1781/1782 remain preserved; read the exact common-disk1576 and
midpoint1781/common-prime1782 stop paragraphs. This test involves no
complex heat evaluator or prime quadrature, despite use of complex
function theory. No historical computational stop is reinterpreted as
a global impossibility theorem.

All inherited actual-divisor, conjugation/multiplicity, excluded ordinate
zero, strict strip, gamma>14, counting, through100, retained-real-zero,
reciprocal-square-tail, heat positivity, separate fixed-j heat errors,
Gaussian half-variance and both fixed-v1 qualifications remain whenever
the generic bridge is later applied to this notebook's laws. The bridge
alone does not certify any of them. Full matching Mathlib coverage is
unchecked and unknown. PROOF and DAG have no changed argument.

Decision: direct import of the inspected global inverse estimates is
parked for the available hypotheses. Prepare a SPECIALIZE continuation
for the explicit finite-node analytic bridge, with separate approval
before invocation. No actual e(V) has been established. Central creative
work remains blocked by discovery1747's missing independent actual-theta
representation, weighted-height transfer or quantitative signed majorant;
this routine analytic specialization is not labeled creative.
