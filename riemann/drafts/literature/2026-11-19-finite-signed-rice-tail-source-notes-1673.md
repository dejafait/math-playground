# Finite signed Rice tail: source comparison1673

19 November2026. LITERATURE / literature_comparison / REPRODUCTION.
This completes the missing comparison for nomination1672's unchanged
target. No Rice-tail identity, domain inclusion, derivative bound or
relative remainder estimate is proved in this review.

## Inspected primary statements and proof cases

M. Beck, G. Marchesi, D. Pixton and L. Sabalka, *A First Course in
Complex Analysis*, edition1.6 (August2025),
[author-hosted PDF](https://matthbeck.github.io/papers/complex.pdf),
Theorem4.2.5 and its complete proof, printed p65 (PDF p75), and
Exercise4.5.10, printed p76 (PDF p86). The theorem assumes a region G,
a piecewise smooth path in G, a continuous function on G and an
antiderivative there; its integral is the endpoint difference of the
antiderivative. The proof parametrizes the path and uses the chain
rule and real fundamental theorem of calculus. Exercise4.5.10 states
complex integration by parts for holomorphic f,g on G:

    integral_gamma f g' = [fg]_gamma(a)^gamma(b) - integral_gamma f' g.

Read the whole exercise statement. It is an exercise, not a separately
proved theorem in this text; the named fundamental theorem supplies
the proved underlying input. Import these standard calculus tools;
do not reprove an asymptotic theorem. They give an exact remainder,
not an automatic relative small-o estimate.

N. M. Temme, *Uniform Asymptotic Methods for Integrals*,
arXiv:1308.1547v1 (7August2013), dated8August2013,
[CWI primary PDF](https://ir.cwi.nl/pub/21470/21470B.pdf),
Section3, equation(3.1), printed p11, and all of Section3.1,
equations(3.3)--(3.6), printed p12. The phase and endpoints are real
and the large parameter is real. For a finite interval and nonzero
phase derivative, integration by parts produces both endpoints and
an integral remainder. Successive amplitudes are defined by
psi_(n+1)=-(psi_n/phi')'. Uniform bounds on these amplitudes control
the remainder. The displayed remainder after N operations has the
same parameter order as the last retained terms without additional
estimates. The first-operation proof case was read in full. This is
methodological overlap, not a complex, moving-degree endpoint theorem.
The later attempt should use exact calculus rather than infer
uniformity from this fixed-data expansion.

NIST DLMF [2.3(i), equations2.3.4--2.3.6](https://dlmf.nist.gov/2.3#i),
accessed19November2026. Read finite-interval hypotheses, both endpoint
series, the separate infinite-endpoint hypotheses, and the complete
error paragraph. On a finite fixed interval the amplitude is infinitely
differentiable; the Fourier parameter tends to positive infinity.
The error after n terms is bounded by x^(-n) times the variation of
q^(n-1), with variation integral_a^b |q^(n)(t)|dt. The infinite case
additionally requires uniform convergence of every differentiated
oscillatory integral at infinity. These are explicit remainder costs;
no infinite opening or degree-uniform version is imported here.
Olver(1997b), pp66--70,75--76, and Wong(1989), Chapter1, are references
listed by DLMF, not separately inspected book inputs.

NIST DLMF [2.4(iii), equations2.4.10--2.4.13](https://dlmf.nist.gov/2.4#iii),
accessed19November2026. Read all hypotheses(a)--(c), the endpoint
expansion and branch condition. For integral exp(-z p(t))q(t)dt,
p,q are analytic near the path apart from possible endpoint exceptions.
At the finite initial endpoint they have convergent power expansions
with Re(lambda)>0, mu>0 and p_0 nonzero, with specified continuous
branches. The parameter lies on a ray or sector of angular width less
than pi. Absolute convergence at the other endpoint is uniform in z.
Away from the initial endpoint, Re(e^(i theta)(p(t)-p(a))) is positive
and stays uniformly separated from zero towards the other endpoint.
The resulting endpoint expansion concerns this fixed phase/path data.
Neither these conditions nor their uniform degree-dependent version
are established for the Rice tail. A nonzero complex logarithmic
derivative alone does not check them. No contour deformation is needed
or approved for the present test.

R. Pemantle and M. C. Wilson, *Asymptotic expansions of oscillatory
integrals with complex phase*, arXiv:0903.3585v1 (20March2009),
[primary PDF](https://arxiv.org/pdf/0903.3585), Definitions2.1--2.2,
Theorem2.3 and Corollary2.4, printed pp4--5. Read these statements,
including the definition of stationary point. The main theorem uses a
compact real analytic stratified space, analytic amplitude and phase,
nonnegative real phase, and finitely many quadratically nondegenerate
stationary points. The corollary treats specified boundary stationary
points. This does not supply the requested nonstationary endpoint
expansion. No proof from later sections is imported, and none is
essential to the exact-calculus route. Do not cite the abstract as a
matching theorem.

## Existing coverage, duplicates and failures

Read C048j/m's exact functions, regions and conclusions and C048n's
entire proof through its uniform-onset argument; reuse audit1672 rather
than repeat it. C048n controls actual I and its first logarithmic
derivative using C048j's value bound on complete complex disks. Its
conclusion does not bound Q_d'. Reuse notes1670's inspected Nagel
Corollaries3.11--3.12, including the all-orders Cauchy estimate, and
notes1663's inspected DLMF5.11 digamma remainder. No new Cauchy or
digamma discovery is required. The full-circle/neighborhood requirement
persists for every further differentiation. Do not differentiate a
pointwise asymptotic without that justification.

The variable convention matters when comparing real-phase sources:
Q_d uses s-derivatives; the segment is parametrized by s=c+it.
A later application must retain the chain-rule factor i throughout.
In particular C048n's Im Q_d margin must not simply be called the
t-phase derivative and inserted into a real nonstationary-phase
theorem. This is a source-hypothesis warning, not a new Rice estimate.

Searched C048*.md and specifically the19November Rice/Mellin
assessments, source notes and stops for endpoint, integration by parts,
nonstationary and relative-tail coverage. No matching finite signed
tail result was found in those checked files. C048l's audited finite
rectangle controls the other edges, and C048n is a pointwise input;
neither pays this target. Reuse source-notes1663's Rice literature
comparison: its other coefficient observables and GRH-conditional Li
asymptotics are not unconditional theorems for the present F_d.
No novelty inference is drawn from these bounded searches.

Read stops1657/1665/1667 completely. They concern, respectively,
fixed-degree absolute infinite opening, an in-sector S stationary point,
and theta continuation across its boundary. Preserve each stop. The
present finite, degree-dependent segment and exact endpoint remainder
require none of those operations. Historical endpoint-import/review-loop
stops recorded in notes1660 are not overridden by an automatic theorem
import; the new specialization must explicitly pay its own remainder.

Queries issued: `complex non stationary phase endpoint expansion
integration by parts error bound logarithmic derivative complex phase`;
`site.dlmf.nist.gov 2.3 integration by parts Fourier integral error bounds`;
`site.math.ucla.edu tao oscillatory integrals nonstationary phase lemma
complex amplitude`; `complex contour integration by parts holomorphic f
g formula site:edu pdf`. Search snippets were discovery only. The
Drexel lecture_3_12.pdf source failed with HTTP502; it is not imported
and is nonessential because the author-hosted textbook was accessible.
No essential source blocker remains. No cross-notebook input is used.

## Decision and the exact remaining specialization

SPECIALIZE, provisionally REPRODUCTION, for the unchanged TARGET.
Known complex integration by parts and the reused derivative tools
cover the method. No inspected theorem directly proves the desired
uniform relative error. The difference is a concrete application to the
actual Rice kernel, with these obligations left entirely to a later
mathematical turn:

- Verify the whole closed segment and a common integer onset in
  C048a/j/m/n's domains with p=s+1/2. Retain both endpoint clearances
  and every gamma, finite-product and Mellin nonzero condition.
- Control the actual Q_d' uniformly, using explicit principal-main-term
  calculus and justified quotient derivatives. If Cauchy estimates are
  used, include the complete circles, their holomorphic neighborhoods
  and the value bounds there. The n=2 tool is already covered.
- Bound the reciprocal denominator throughout the segment and the
  logarithmic derivative at the lower endpoint as needed for comparison
  with exactly |F_d(c+ia_d)/Q_d(c+ia_d)|.
- Obtain an integrated amplitude comparison relative to that same
  lower endpoint, not just an unnormalized absolute integral bound.
  Apply the exact complex integration-by-parts formula with correct
  orientation and derivative variable, and estimate its full remainder.

No bound, rate or disk choice for these obligations is asserted here.
Using exact finite integration by parts avoids needing an uninspected
uniform asymptotic theorem. One bounded attempt is justified after the
separate source-scope approval. Continue only if its complete remainder
divided by the specified lower-endpoint scale tends to zero uniformly
as integer d tends to infinity. An upper bound that merely tends to
zero in absolute size, an unchecked d-dependent constant or an
uncontrolled denominator fails this test; record the precise unpaid
estimate and park this target instead of repeating numerical samples.

The possible use is control of one finite signed part of C048l's
vertical contour. The main L030--L032/C032a positivity gap, C028b's
height condition, C028g's limit condition, bounded-height core, other
segments, total cancellation and sufficient Xi bridge remain unpaid.
No justified creative mechanism at those central gaps is made ready
by this standard specialization. Full matching Mathlib coverage is
unchecked; no absence is inferred. No canonical lemma, mathematical
script, PROOF or DAG changes are called for by this literature turn.
