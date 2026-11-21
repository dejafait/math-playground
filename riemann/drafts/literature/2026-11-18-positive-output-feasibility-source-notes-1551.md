# Positive-output feasibility: source comparison1551

18 November 2026. Literature only. The target is assessment1550's
unchanged TARGET. No feasibility theorem, asymptotic, witness or new
mathematical statement about the actual kernel is established here.

## Exact question and reused coverage

C032q asks for a real finite signed mass-one measure eta on W=[1,2],
with arbitrary finite variation, positive output nu_eta on [0,infinity)
and J_eta=0 on the full complex plane. Its equivalent closed-cone
alternative is audited; C032r's moments are conditional conclusions,
not a construction. C032m supplies compact-disk uniformity, not a
signed tail approximation. C032j retains fixed-v1 preprint, actual
divisor, multiplicity, finite-zero, counting and heat qualifications.

Reuse ledgers1528/1532/1535, including Powers-Xu's generating-function
maps, signed scalar support recovery and signed Riesz/separation.
No repeated source-wide review of those results is claimed. Reused
stops: finite stop1302; scalar-recursion stop1534; audited direct
compact-transform stop1536/1538; criterion-only limit1546. These do
not ban other representations or continuum laws.

## Primary coverage actually inspected

1. Dung Le, Nicola Bariletto, Alessandro Rinaldo and Nhat Ho,
   *Partial Differential Equation Barriers to Identifiability in Infinite
   Mixture Models*, fixed [arXiv:2608.08597v1](https://arxiv.org/html/2608.08597v1),
   Section2, Definition5 and Proposition4, Section5.1; complete
   proof A.6. The source operator acts on finite signed Radon measures
   on a regular compact parameter set, with jointly measurable
   probability densities relative to a fixed sigma-finite measure.
   Definition5 requires
   f(x|theta)=h(x)gamma(theta)K(tau(x)-psi(theta)), positive continuous
   h,gamma, tau a homeomorphism onto Euclidean space, psi a
   homeomorphism onto its image, and K integrable. Proposition4 adds
   a Fourier transform nonzero almost everywhere. Its signed proof
   weights and pushes forward the input, then uses convolution and
   Fourier uniqueness. No density of the mixing measure is needed.
   This improves on probability-density-only mixing coverage1528,
   but no such representation is known for our output law or odd
   kernel. The source's change from almost-everywhere x to transformed
   coordinates would also require checking the null-set interface in
   any application. Proposition5 and its exponential-family argument
   were consulted as a further lead, not imported. No result here
   turns arbitrary nonlinear entire dependence into identifiability.

2. Maximillian Newman, *On rigidity of infinite exchangeable sequences*,
   fixed [arXiv:2610.18992v1](https://arxiv.org/html/2610.18992v1),
   Section1.2 equations(2)-(4), Definition1.14, Corollary1.15;
   Lemmas3.3-3.4 with proofs and the complete localization proof of
   Corollary1.15 in Section3.2. Proposition1.12 coverage is reused
   from ledger1535. The exponential family must have density
   exp(-<y,T(x)>)/Z(y) relative to a common sigma-finite m, with
   finite positive Z. The statistic-support grid must have separated
   exponents and divergent reciprocal sums. Strong localization
   starts from the two-sided measure domination
   0<=Q_nu[f]<=Q_nu[1_B], for f in L2(nu) and specified upper rectangles B.
   The proof tilts to a finite signed measure, obtains exponentially
   decaying sampled Laplace bounds from the upper domination, applies
   support recovery, and removes a strictly positive weight.
   C032q has neither that exponential-family representation nor that
   reference upper bound. Positivity alone is not the inspected
   theorem's hypothesis. A comparison law and its bound must be
   proved, not supplied by mass normalization. The underlying book
   support theorem is not independently re-audited here.

3. Yohann de Castro and Fabrice Gamboa, *Exact reconstruction using
   Beurling minimal extrapolation*, J. Math. Anal. Appl.395 (2012),
   336-354, doi:10.1016/j.jmaa.2012.05.011; inspected
   [author manuscript](https://ydecastro.github.io/research/paper4.pdf),
   Lemma1.1, printed pp5-6, and complete AppendixA.1, pp19-20,
   including LemmaA.1. A finite target support/sign pattern must admit
   a linear combination of continuous measurement functions that
   interpolates the signs, has absolute value strictly below one off
   the support, and has a full-column-rank evaluation matrix.
   The conclusion concerns uniqueness among total-variation minimizers
   with prescribed measurements. Its proof first uses TV equality,
   then strictness away from the support, then matrix rank.
   C032q imposes no TV-minimization property or finite support and
   supplies no such interpolant. Positive output is not positive
   mixing. This theorem therefore provides no actual cone certificate.
   Theorem2.1's homogeneous-M-system statement was read, but its
   separate proof was not audited and is not used. Manuscript version
   date is unspecified; these are its printed-page references.

4. Didier Henrion, Simone Naldi and Mohab Safey El Din,
   *Algebraic certificates for the truncated moment problem*, fixed
   [arXiv:2302.06927v1, 14 February 2023](https://arxiv.org/pdf/2302.06927),
   Lemma1 and proof, printed p6; Theorem3 statement and its
   certificate/converse proof cases, pp12-13. The algorithm needs
   polynomial data and an archimedean quadratic module, hence a
   compact basic semialgebraic support. Its unrepresentability
   certificate is a polynomial 1+q whose specified moment functional
   vanishes. C032q has arbitrary signed width weights, a noncompact
   output space, and nonpolynomial kernel constraints without a
   finite polynomial encoding. C032r gives no fixed input moment
   vector for this algorithm. Those are missing hypotheses, not an
   invitation to replace the target by a finite truncation. The full
   algorithm and complexity claims were not audited or imported.

## Comparison, decision and evidence limits

The first candidate remains parked as an immediate identifiability or
tail-support import. Signed-measure scope is available, but the actual
representation and a mixed remainder estimate are missing. The newly
inspected localization proof specifically spends an upper domination
bound absent from C032q. Its source theorem cannot supply that bound.
Here the missing bound means the specified localized reference bound,
not absence of every dominating measure: C032q's Jordan construction
already supplies its positive input component mu_+. That component
depends on the unknown eta and has no established upper-rectangle
support restriction in a suitable exponential-family coordinate.
Using the whole width interval as reference yields no support exclusion.
This is an additional precise mismatch, not an impossibility theorem
for another tail reduction. Do not rerun the direct compact-transform
bound or the scalar recurrence without the new input their stops require.

The second candidate remains parked as an automatic constructive
certificate import. Sparse recovery and polynomial algorithms require
additional structure and data, and neither produces a function Tf or
an approximating sequence for the actual Q. A finite-width reconstruction
would also be outside the remaining continuum question. A fixed numerical
residual still pairs with unbounded |eta|(W); none of these sources
removes criterion1546's problem. No new use of generic separation is
warranted. The decision is source-scope negative, not mathematical
infeasibility or an RH conclusion; no source-access blocker prevents
using the completed comparisons.

## Narrowly different nomination

A useful independent subquestion is whether output positivity admits
any genuinely signed two-width input at all. Nominate a finite-activity
Levy comparison of nu_1 and nu_2: ask whether either difference of their
Levy measures is nonnegative with finite total mass, and whether the
resulting standard compound-Poisson comparison can certify a signed
positive output. These are desired hypotheses and conclusions, not
claims derived here. The concrete comparison data are C032j's existing
ell_sigma(t)=H_sigma(t)/t and its exact H_sigma formula. The sign for
all t and integrability of a difference at both endpoints are unpaid.
No implication from positivity of each ell_sigma to their ordered
comparison is asserted. This avoids a growing signed-output test.

New source lead: Jean Bertoin, *Subordinators, Levy processes with no
negative jumps, and branching processes*,
[Maphysto course notes](https://www.maphysto.dk/oldpages/events/LevyBranch2000/notes/bertoin.pdf),
2000 course. Only title/scope and the indexed finite-Levy-measure lead
were retrieved in this step; the relevant theorem and Poisson
construction/proof were NOT read. Assessment1551 therefore nominates
separate literature review, not mathematics. Check source scope and
local duplicates before attempting any sign estimate.

A successful comparison could construct a signed positive output and
test the proposed sign-recovery shortcut; it would not solve J_eta=0.
Finite stop1302 already excludes two-width full cancellation. A failed
comparison would stop only this sufficient construction, not all signed
positive outputs. The core cone problem and actual-Xi transfer remain
unresolved. This is materially different from odd-kernel completeness,
PDE closure and direct-transform growth; no prior stop is erased.

## Search/access record and Mathlib

Queries: nonparametric mixture identifiability signed measure tail
infinitely divisible Laplace transform; the exact PDE-barriers title;
positive integral operator cone uniform approximation dual certificate
generalized moment problem compact support; signed mixtures tail
identifiability compact; constructive dual certificates integral positive
measures kernel; Henrion algebraic certificates truncated moment problem
exactmoments arxiv; de Castro Gamboa exact reconstruction positive measures
Chebyshev systems dual certificate; Bertoin subordinator finite Levy
measure compound Poisson atom zero lecture notes pdf; the exact smoothing
paper title with monotonic. No matching actual-family result was found;
this bounded search is not evidence of novelty.

Tallis-Chesson's 1982 primary paper was located and theorem-level excerpts
viewed, but its proofs were not inspected and it is not an input. A
publisher/author-hosted Henrion PDF fetch failed; arXiv supplied the
selected theorem/proof cases, so no essential blocker remained. No
paid access, API credential, source-wide preprint audit, sibling notebook,
mathematical script or lemma write occurred. Matching Mathlib coverage
of either proposed mechanism remains unchecked and unknown.

Local duplicate search used the compact-width, positive-output and
smoothed-law literature files, smoothed/signed-law ATTEMPTS and C032
lemma files for compound-Poisson, finite-activity, Levy-difference and
two-width domination terms; no matching comparison was located in those
paths. This is a bounded path check, not an archive-wide absence claim.
