# Large-real-zero common-profile test: source approval

TARGET: Test whether alpha^2 times Hedenmalm's L-image converges to one nonzero profile in logarithmic L2 as alpha tends to infinity through positive real zeros, forcing a nonzero Gram entry for every sufficiently large distinct pair.
CHECKED: 2026-11-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step155 searched the exact identifier/title with asymptotic, high frequency, L2, Gram and nonorthogonality, plus oscillatory Volterra/weighted-L2 endpoint asymptotics and Hardy's original infinitude paper; compared the scoped local assessments and stops below. No inspected theorem supplies this whole-line common-profile conclusion; failed searches imply no novelty claim.
SOURCE_EVIDENCE: Hedenmalm2606.17494v1 (1.2.3), (2.2.2), (3.3.2), Definition4.2.1 and Theorem4.2.2 including both proof cases; DLMF2.3(i), Fourier cases (2.3.4)-(2.3.6) and complete remainder hypotheses; Hardy1914, C.R.158 pp1012-1014, sections1-3 in primary-paper transcription; DLMF5.2(i) gamma nonvanishing; audited L906-L908. Precise links, access limits and applicability below.
COMPARISON: Hardy supplies an unconditional unbounded real-zero family; standard endpoint expansion supplies finite-order coefficients and a variation remainder for fixed endpoints. Neither it nor Hedenmalm supplies weighted whole-line norm convergence, the proposed alpha^2 scaling or nonzero profile. Those explicit application differences justify SPECIALIZE with prospective REPRODUCTION, not an import of the target or a creative construction.
GAP: Derive the actual L-image leading term and test alpha^2; control the full remainder after multiplication by W'/W on both half-lines uniformly along exact real zeros; prove the resulting profile belongs to L2 and has positive norm; then justify the all-sufficiently-large distinct-pair conclusion. None is established in this source-only turn.
REASON: Approve the unchanged nominated target for one mathematical attempt using the inspected endpoint theorem and audited theta bounds. The primary infinitude input and relevant theorem scope are now covered; the remaining uniform weighted estimate is the identified specialization, not a missing-source blocker. Preserve the first-pair and positive-realization stops.
LITERATURE_REASON: At turn start the step154 nomination changed the indexed two-root test to a uniform unbounded real-zero family, with its essential Hardy input and endpoint-remainder theorem unread; this separate comparison completes that missing coverage.
SCOPE: The exact TARGET only, with the unchanged source normalization of u_alpha, measure dt/t and positive real exact zeros. Covers finite-order endpoint expansion, theta-specific whole-line remainder bounds, the proposed scaling/profile test and its conditional Gram consequence. No changed eigenfunction normalization, metric, complex-zero family, completed realization, RH claim or audit of L908 step154 is covered.

## Original step154 nomination and scope (historical)

Retain exactly w,D,L,u_alpha, W and G_alpha of L906-L908 and measure
dt/t, so G_alpha(x)=(Lu_alpha)(exp(x)). The expression alpha^2 G_alpha
is a proposed normalization to test, not an established asymptotic.
Seek a fixed, nonzero F in L2(R) with a rigorous uniform norm error
||alpha^2 G_alpha-F||_2 tending to zero along the positive real zeros.
No formula for F, convergence or error estimate is derived here.

The prospective downstream use is to decide nonorthogonality for all
sufficiently large distinct real-zero pairs. This would reject this
specific logarithmic L2 metric on the actual spectral span while
leaving the first-pair Gram value unknown. It would not supply a
different positive metric, all-zero symmetry, a completed realization,
RH, simplicity or actual-Xi mixed positivity.

The next turn must be literature-only: search the exact statement,
the source's title/identifier with high-frequency asymptotics and
nonorthogonality, and standard integration-by-parts/resolvent
asymptotics for the first-order inhomogeneous ODE in a weighted L2
norm. Retrieve primary hypotheses and proof cases before deciding
whether to IMPORT, SPECIALIZE or EXPLORE. In particular inspect a
precise standard Hardy infinitude theorem and its applicability to
the local completion and positive real parameter, without assuming
all zeros real. A merely formal inverse-power expansion is not
uniform L2 control. No numerical root labels or certified interface
are needed if an adequate analytic theorem applies.

Essential prospective local inputs are audited L906 (complete
derivative estimates, positivity and its nonzero curvature test),
L907 (the exact ODE) and L908 (normalization, exact-zero upper tail,
denominator and norm bounds). L908's unaudited step154 commutator
calculation is historical motivation only, not an input to this
proposed asymptotic target. No cross-notebook result is proposed.
The previous first-pair numerical and phase stops remain intact.

Continuation test: approve a mathematical attempt only after sources
cover the family-level scope. That attempt must establish a uniform
vanishing L2 error and a strictly positive limiting norm, or a precise
failure of the proposed normalization. A pointwise expansion, assumed
orthogonality or uncontrolled tail is insufficient. Do not recycle
the stopped first-pair phase identity or label elementary asymptotic
specialization creative. No justified central positive-realization
mechanism has yet emerged. Full and supporting Mathlib coverage for
this new family statement is unchecked, not asserted absent.


## Separate source approval, 8 November 2026 (step155)

The nomination above is preserved as history. Its pending-review language
is superseded by this approval for the unchanged TARGET. This turn
establishes source coverage only: no local asymptotic, profile formula,
weighted remainder estimate, Gram verdict or new lemma is asserted.

### Sources actually inspected and their precise scope

1. Hedenmalm, *Spectral interpretation of Riemann zeta zeros*,
   [arXiv:2606.17494v1](https://arxiv.org/html/2606.17494v1),
   submitted 16 June 2026. The inspected version record lists v1.
   Reused step149 and read the defining series, completion, ODE,
   Definition4.2.1, Theorem4.2.2 and both proof cases. Theorem4.2.2(b)
   requires pair symmetry and distinct real zeros; it then requires
   orthogonal L-images. It chooses no particular metric and gives no
   large-alpha profile or unconditional nonorthogonality result.
   Part(a) retains possible complex zeros; restricting this diagnostic
   to real zeros cannot establish its full symmetry premise.

2. NIST DLMF, [Section2.3(i)](https://dlmf.nist.gov/2.3#i),
   live text accessed 8 November 2026, Fourier cases (2.3.4)-(2.3.6).
   For a smooth amplitude h on a finite interval [a,b], (2.3.4)
   gives the endpoint expansion of integral exp(i lambda s)h(s) ds
   as lambda tends to positive infinity. The half-line case (2.3.5)
   instead requires smoothness on [a,infinity) and uniform convergence
   of every derivative Fourier integral for sufficiently large lambda.
   After n endpoint terms its error is bounded by

       lambda^(-n) integral_a^b |h^(n)(s)| ds,  n>=1,

   with b=infinity in the half-line case. The definition of variation
   is (2.3.6), including its recorded 1.1.1 correction. Both cases and
   the full error statement were read. This is a scalar endpoint
   bound, not a theorem about the whole-line norm of L-images.
   DLMF cites Olver, *Asymptotics and Special Functions* (1997 reprint),
   pp66-70,75-76; that book passage was not independently inspected.
   DLMF's explicit statement is the imported result, not an assumed
   stronger book theorem. No stationary-phase or resolvent estimate
   with different hypotheses is substituted.

3. G. H. Hardy, *Sur les zeros de la fonction zeta(s) de Riemann*,
   **Comptes rendus de l'Academie des sciences 158 (6 April 1914),
   pp1012-1014**, sections1-3. Read the primary-paper transcription:
   [p1012](https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_158,_1914.djvu/1014),
   [p1013](https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_158,_1914.djvu/1015),
   [p1014](https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_158,_1914.djvu/1016).
   The unnumbered theorem announced in section1 is **Hardy's theorem**:
   zeta has infinitely many zeros on Re(s)=1/2. Sections2-3 use a theta
   summability limit and contradict an eventually constant sign of
   Xi(2t) for positive t. This supplies arbitrarily large positive
   real zeros, without RH, simplicity, indexing or a spacing estimate.
   The reading includes the positive-t final contradiction, rather
   than inferring a one-sided statement from a search snippet.

   Applicability: the completion on p1012 is the same
   xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2 used in Hedenmalm (2.2.2)
   and audited L908. For s=1/2+i alpha, the elementary prefactors do
   not vanish; Gamma(s/2) is finite and nonzero by
   [DLMF5.2(i)](https://dlmf.nist.gov/5.2#i), the paragraph following
   (5.2.1), inspected here. Thus the cited real-zero family has the
   required completion. L908(1), not the source's printed Mellin
   coefficient, supplies its exact-zero transform condition. Hardy's
   positive-t sign formulation avoids assuming that an infinity of
   zeros consists of one repeated point; Xi is nonzero entire and
   has isolated zeros. No effective threshold is imported.

   Access qualification: the primary transcription has visibly
   damaged mathematical typesetting (including the differentiated
   integral on p1013). Those formulas are not imported or repaired
   here; only the standard named infinitude theorem, its completion
   and its positive-t scope are used. Facsimile links were exposed
   by the web connector, but no actual image payload was available
   for visual inspection. A local three-image download failed DNS;
   no scan was saved and no visual proof audit is claimed. These
   limits do not block citing the plainly stated standard theorem.
   A later Hardy-Littlewood full-paper lead at
   [UBC's primary PDF](https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1916.Hardy.pdf)
   was opened only in its front matter; a targeted search then timed
   out. Its relevant theorem/proof is **unread** and is not an input.

### Comparison with the local record and search limits

The targeted reads used audited L906's full derivative estimates and
curvature test, L907's exact ODE/primitive and L908's normalization,
positive denominator, logarithmic-derivative bound and exact-zero
tails. Step149's ready fixed-pair assessment was reused for common
operator conventions; its indexed-root/quadrature coverage is not a
claim of uniform-family coverage. The exact Hedenmalm ATTEMPTS files
for the positive-pair import, enlarged-domain inverse, numerical
certification and step154 analytic sign stop were checked. The new
family target was compared with their stated scopes, not with sibling
notebooks or unrelated historical proof collections.

The positive-pair stop still concerns an absent metric and symmetry
premise; L906's V obstruction still concerns a different domain. The
numerical stop still has no certified root/Gram enclosure. Step154's
signed-phase integral is inconclusive and is not an input here.
None supplies this uniform norm limit or bans a separately bounded
large-parameter test. No stopped first-pair calculation or package
access attempt is reopened.

Queries included `"2606.17494" "asymptotic"`, the exact title with
`orthogonality asymptotics` and `"high frequency"`, the identifier
with `"L2"`, `"Gram"` and `"nonorthogonality"`, `oscillatory Volterra
asymptotic integration by parts weighted`, and `oscillatory integrals
asymptotic expansion weighted L2 endpoint`. Hardy searches used his
name, 1914, the original title and pages1012-1014. The strongest
inspected quantitative asymptotic input applicable at the starting
scalar-integral level is the DLMF variation remainder above. Generic
Volterra numerical-method abstracts and unrelated spectral proposals
were returned, but their theorem statements were not read and are
not inputs. No exact or stronger whole-line common-profile theorem
was found among the inspected sources; this bounded comparison does
not establish originality or an exhaustive literature census.

### Approved mathematical specialization and stopping test

The exact TARGET is now approved as SPECIALIZE, with prospective
classification REPRODUCTION. The remaining work is a finite-order,
theta-specific application of the cited endpoint expansion. Do not
reprove Hardy's theorem, the general endpoint expansion or a general
spectral theorem. A full theorem import alone does not settle the
local target because the expansion's endpoint varies with the spatial
variable, L includes the unbounded factor q=W'/W, and the required
conclusion is a norm limit on the entire real line.

One next mathematical attempt may:

- Use the unchanged primitive normalization and audited L906-L908 to
  determine the leading L-image term and test the proposed alpha^2
  scaling. Do not assume a leading coefficient or profile formula.
- Apply the inspected finite-order remainder with the lower primitive
  on one half-line and the exact-zero upper primitive on the other.
  Verify all endpoint and derivative-integrability hypotheses using
  the complete theta bounds. Local L908's denominator/q estimate is
  available; rapid decay alone cannot control division by W.
- Establish a spatially square-integrable remainder bound independent
  of the chosen real zero, tending to zero after the proposed scaling.
  Control differentiation and multiplication by q separately. A fixed
  cutoff expansion, fixed-pair tail estimate growing with alpha, or
  pointwise convergence cannot replace this whole-line estimate.
- Prove the putative profile is in L2 and has strictly positive norm,
  then justify the proposed sufficiently-large distinct-pair Gram
  conclusion by norm continuity and the cited unbounded zero family.
  Until these checks are complete, that conclusion is conditional.

Success requires a vanishing full norm error and a nonzero profile,
or a rigorous failure of the proposed scaling/convergence. A merely
formal expansion is inconclusive; save the unpaid estimate and stop
rather than repeat the first-pair phase mechanism or tune root access.
No particular convergence rate or effective large-zero threshold is
asserted in this approval. A genuinely changed scaling, metric or
new mechanism outside this SCOPE needs its own source review.

This is source progress and approval for an elementary asymptotic
specialization, not a new mathematical result, positive realization
or RH claim. No justified creative construction addressing full
symmetry has emerged; absent independent metric/symmetry data is the
blocker, not a literature quota. All-zero symmetry, completion,
simplicity and actual-Xi all-degree mixed positivity remain open.
Full matching and supporting Mathlib coverage is unchecked; no
absence claim is made. No lemma, DAG row, proof overview or mathematical
script was changed in this literature-only step. The newly completed
coverage is to be reused for mathematics next turn, not re-reviewed
without a specific new essential source or changed hypothesis.
