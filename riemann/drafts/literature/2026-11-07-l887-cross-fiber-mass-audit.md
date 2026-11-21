# L887 crossing-mass calculation — completed audit source comparison

TARGET: Assess source coverage for a conceptual audit of L887's positive crossing-mass expansion, especially the full-J trace coefficient, zero linear term, and uniform O(t^2) remainder.
CHECKED: 2026-11-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the completed crossing-mass-variation searches and stationary-graph-phase-components/L879-audit source comparisons; read the complete L887 proof, L879's relevant variation/contact argument and accepted audit, L847's exact hypotheses/density, and attempt71/65/69 failure records. No new external query or novelty inference; precise scope comparison below.
SOURCE_EVIDENCE: Reuse Wachsmuth-Wachsmuth, JNSAO3(2022),8733, Section3.2 Lemmas3.3/3.5, Theorem3.4 and Example3.6, pp10-14, https://jnsao.episciences.org/9596/pdf ; DLMF19.2.5/19.2.8 and19.12.2/19.12.3, https://dlmf.nist.gov/19.12#E2 ; Guillemin-Sternberg, Semi-classical analysis, 13Jan2010, Sections13.13-13.14.1 (13.7)-(13.9), pp449-455, https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf ; Lebl CA v1.10, 5Nov2026, Theorem2.4.7/factorization pp49-50, https://www.jirka.org/ca/ca.pdf . Inspected-source evidence is retained in the named existing assessments, not newly retrieved here.
COMPARISON: Existing variation/factorization inputs cover the underlying smooth pullback and isolated-zero facts. The real-kink theorem and DLMF logarithmic model do not cover the submitted complex variable-coefficient expansion. L887 writes its own application estimate, so these differences are concrete proof-audit obligations rather than an essential missing source theorem; no sign or estimate is accepted in this review.
GAP: Audit L887 (3)-(15): conditional clean rectangle, full-J trace and two-sided normalized coefficient, zero integrated first variation despite crossing Q=0, nonlinear-density and inner/outer/freezing O(t^2) errors, and fixed-direction quantifiers. Graph existence, arbitrary directions and Xi positivity remain outside scope.
REASON: The separate literature-only comparison is sufficient for one conceptual audit of the written application under EXPLORE. No essential unread theorem is needed to inspect its explicit estimates; approval of this new scope is separate from acceptance of the mathematics. No new lemma, expansion, script or proof repair was produced.
LITERATURE_REASON: The new audit target concerns L887's previously unwritten actual-J coefficient and O(t^2) proof. Reuse the existing primary coverage where adequate; do not repeat searches just to fill a literature turn.
SCOPE: One conceptual audit of L887 under unchanged L847/L879 hypotheses: actual G,R,C,F; smooth real periodic u; J nowhere zero; off-zero stationarity; one conditional simple off-diagonal contact; fixed real chi compactly supported in a clean rectangle with nonzero fiber trace. No uniform bump-family estimate, zero-trace/coupled direction, higher multiplicity, graph/minimizer existence or Xi transfer is covered.
COVERED_TARGET: Critically audit L887's positive simple-fiber crossing-mass expansion, including the full-J trace coefficient, zero integrated linear term, and fixed-bump O(t^2) remainder under unchanged L847/L879 hypotheses.

## Completed comparison, 7 November 2026

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target is the correctness of L887's
submitted conditional mass expansion, not a new lowering direction.
If accepted, its positive leading term would justify stopping this
fixed nonzero-trace single-coordinate bump class as a descent route.
It would not prove local minimality or exclude a contact. Existence
and compactness of stationary/minimizing graphs, sharp mass bounds,
other directions and contacts, higher signs and Xi transfer remain open.

Read the complete submitted L887, including its nonlinear density,
interface argument and all cutoff estimates. Read L879's exact
hypotheses, variation formula and relevant contact proof, including
its accepted conceptual audit, and L847's original G,R,C,F and angular
orientation. These reads compare scope; they do not replay or accept
the new estimates. L847 and L879 are the actual mathematical inputs.
L882 is an optional conditional setting, not a necessary premise;
L886 supplies no sign input.

### Reused primary coverage and application differences

The completed `2026-11-07-cross-fiber-mass-variation.md` records
the exact searches, primary statements and essential proof cases.
Its Wachsmuth-Wachsmuth Lemma3.5 concerns a real C1 regular zero
set in a bounded open domain, real perturbations converging uniformly
with common compact support, and positive parameters tending to zero.
Its proof uses Lemma3.3 and Theorem3.4's sliced regular-level charts;
Example3.6 warns against dropping the common-support condition.
That theorem does not cover the imaginary trace, nonlinear path or
two-sided complex norm in L887. It must remain a comparison, not a
certificate for the claimed coefficient or its sign.

The same assessment records DLMF's definition of complete E and its
convergent complementary-modulus series near k=1 (real 0<k'<1),
including the logarithm convention and the full E-series. This is
an inspected singular model. It contains neither L887's full
Jacobian nor a variable-coefficient compact-cutoff error theorem.
No transfer from that series to L887 is approved. The existing
unread Levy and inaccessible Taylor leads remain nonessential:
the submitted proof claims a direct elementary estimate, not a
theorem whose hypotheses must be recovered from either lead.

Reuse `2026-11-06-stationary-graph-phase-components.md` and
`2026-11-06-l879-stationary-phase-line-audit.md` for the inspected
Guillemin-Sternberg and Lebl passages. Smooth parameter maps and
compact support fit the former's pullback differentiation framework;
it gives no nonsmooth mass derivative across Q=0. Lebl's analytic
function on a connected domain is not identically zero here because
G is entire and G(0)>0. Its isolated-zero factorization does not
assert simplicity or a graph fiber. L879's accepted conditional
whole-fiber assertion is the local input for that part of L887.

Lawrence-Yamauchi, arXiv:2311.13002v2, Section II B (11)-(16),
pp3-4, is already inspected in those assessments. Its unrestricted
off-zero phase condition is not a justification for stationarity
of a variation crossing Q=0. L887 instead offers a divergence and
zero-interface-flux argument; that argument must be audited directly.
No contour-existence, sufficiency or global-perfection claim is used.

The other tools claimed in L887 are Taylor's theorem for the
Euclidean norm away from its origin, the modulus Lipschitz inequality,
dominated convergence and integration by parts. Their application
conditions are explicit audit questions below. An additional general
singular-integral theorem is not essential to checking a submitted
proof using those standard tools. No theorem is reproved in this
source turn. Full matching and supporting Mathlib coverage remain
unchecked; no absence claim or formal-verification claim is made.

### Duplicate/failure check and one bounded audit

Reuse the recorded exact/stronger-result searches rather than repeat
browsing with unchanged hypotheses. The read attempt71 history and
stop identify L887 as the new submitted calculation, not an already
audited result. Attempts65/69 concern the unsigned conjugate kernel
and corrected chord moments; their signed-compensation gaps are
preserved. The named finite-graph-mass-descent assessment concerns
support away from Q=0. None supplies the crossing calculation or
licenses another bump test. No cross-notebook input was used.

The later audit should check the following submitted claims, without
adding a sign, realization or uniform-family premise:

1. The rectangle isolates exactly one simple factor and includes both
   sides of its fiber; the other G factor, diagonal factor and J do
   not vanish on its compact closure. The angular lift and the
   nonzero real h0 used in L887 must follow from the stated inputs.
2. Replay L887 (5)-(10), keeping the derivative of the full J, all
   cutoff derivatives and the complex trace. Check the power of
   1+a^2, the nonvanishing factors and the normalization in (3)-(4).
3. Check that L879's smooth density identity (7), unlike its
   off-zero mass derivative, applies on the fiber. Audit both
   half-rectangle boundary fluxes, the bounded vector field and the
   dominated-convergence argument in L887 (11)-(12). Forbidden
   stationarity for a zero-crossing support cannot be assumed.
4. Check the uniform second-parameter-derivative bound in (8)-(9),
   the Lipschitz control of its integrated effect, the inner-strip
   bound, the third-order outer remainder on balls avoiding zero,
   the coefficient-freezing error, and both sides of the logarithmic
   integral. Every constant must be fixed before t tends to zero;
   include cutoff transitions and points where the trace vanishes.
5. Check J_t preservation, unchanged exterior density, both signs
   of t, positivity only for nonzero trace, and the quantifier
   "for each fixed chi." No family-uniform onset is asserted.

Accept the scoped stop only if the coefficient and integrated error
survive these checks. A sign, factor, support or remainder failure
requires a precise error report and a repaired/narrowed claim before
using the stop. Zero trace or coupled directions require a different
assessed target; they are not fallbacks within this audit. This turn
is EXPLORATION in source comparison, not a mathematical advance or
an independent proof audit. The newly ready scope receives separate
supervisor approval next turn; L887 remains unaudited meanwhile.

## Original nomination — retained; source gate superseded above

Read the complete canonical L887 proof, then reuse the supplied
crossing-mass assessment and L879's audited full variation/fiber
arguments. Its actual inputs are L847 and L879. L882 is an optional
source of a conditional simple-fiber setting and is not required;
L886 is not a premise. No further source access is presumed essential.

The proposed audit should check that the rectangle really has only
one simple divisor; that the trace formula includes the actual J;
that the divergence identity and zero interface flux remove the
integrated linear term without assuming stationarity for a forbidden
support; and that the inner-strip, outer Taylor, coefficient-freezing
and nonlinear-density errors are each O(t^2), with constants fixed
before t tends to zero. The two sides of the fiber and normalization
must give exactly the coefficient written in L887.

Accepting the positive coefficient would confirm the scoped stop
for each fixed field (chi,0) with nonzero trace. It would not imply
uniform control over a bump family, local minimality, exclusion of a
contact, a stationary graph's existence, or an RH result. A sign,
factor or remainder error must be repaired before that stop is used.
A source or scope gap leaves the audit unapproved. This file records
no completed audit and no approval of new mathematics.

