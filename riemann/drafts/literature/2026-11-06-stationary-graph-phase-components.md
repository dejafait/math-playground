# Stationary radial graphs and phase components — completed source comparison

TARGET: Assess whether every smooth radial graph for L847's actual form with J_u nowhere zero and zero first mass variation for all real radial variations supported off Q_u=0 must satisfy B(u)=|M|, checking phase compatibility across G-zero fibers and the squared diagonal.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded stationary/local-perfect/global-perfect, zero-multiplicity and actual-Xi radial-graph searches; reused the named full-phase/descent assessments and checked the relevant product, period and contact failures. No inspected theorem resolves the exact actual-F implication; search failure is not novelty evidence. Exact queries and scope below.
SOURCE_EVIDENCE: Lawrence-Yamauchi 2311.13002v2 II B (11)-(16), pp3-4, VI A (44)-(51), pp9-10, Appendix B (76)-(79), p13, https://arxiv.org/pdf/2311.13002v2 ; 2101.05755v2 IV B-C (19)-(21) and fixed-point/conditional-continuation cases, pp5-7, IV D cosine discussion, pp7-8, https://arxiv.org/html/2101.05755v2#S4 ; reuse Lebl CA v1.10 Theorem2.4.7 pp49-50, https://www.jirka.org/ca/ca.pdf , and Guillemin-Sternberg Sections13.13-13.14.1 pp449-455, https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf , from the named ready assessments. Qualifications below.
COMPARISON: Known unrestricted stationarity gives phase constancy only off density zeros, and the generic cosine case retains cancellation. Neither result decides L847's actual divisor. L878 covers coordinate-torus descent; L864-L866 require nonnegative density and cannot establish it here. General-Du radial accessibility and actual cross-component alignment are application obligations, not imported results.
GAP: A bounded actual-F attempt must justify the constrained stationarity reduction and then test phase matching through single/simultaneous G contacts and the squared diagonal with their full multiplicities. No inspected source supplies this compatibility, a stationary graph, or the sharp mass equality.
REASON: Essential source comparison is adequate for one actual-divisor compatibility attempt under EXPLORE; automatic local-to-global, flow and calibration imports fail their scope. This is a newly ready continuation requiring separate next-turn approval, not mathematics completed by this review.
LITERATURE_REASON: The invocation-start target had REVIEW_REQUIRED because general-graph radial stationarity and cross-component phase matching were outside the ready coordinate-torus audit; this review fills that essential scope comparison without repeating that audit.
SCOPE: Exactly TARGET for L847's actual entire G, original R,C, full omega and angular orientation; smooth real periodic u on T2; J_u=det(I-iDu) nowhere zero; Q_u=F(Phi_u)J_u and B(u)=mean|Q_u|. One bounded attempt may test constrained stationarity and actual-divisor phase compatibility, allowing failure. No positivity, connected nonzero locus, simple-zero or finite-contact census, exchange symmetry, prescribed collar, global phase, growth or RH premise is added. No flow, compactness, minimizer existence, higher signs or Xi transfer is covered.

## Completed comparison, 6 November 2026

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target is the implication in TARGET,
conditional on an already given smooth stationary graph. Its plausible
use is to rule out a regular stationary stall above the sharp threshold
needed in L868. Even a proof would leave existence of a stationary
graph, compactness or descent control, the unrestricted period problem,
higher mixed signs and Xi transfer unresolved. This review establishes
none of those mathematical claims.

### Sources inspected and their precise limits

Scott Lawrence and Yukari Yamauchi, *Convex optimization and contour
deformations*, arXiv:2311.13002v2, PDF dated 14 August 2024:
[II B, (11)-(16), pp3-4; VI A, (44)-(51), pp9-10;
Appendix B, (76)-(79), p13](https://arxiv.org/pdf/2311.13002v2).
The local calculation uses holomorphic density, a locally invertible
complex Jacobian and unrestricted real/imaginary contour variations.
It integrates by parts, multiplies by the Jacobian, and obtains
weighted constancy of effective phase. Zeros separate possibly
differently phased pieces. The torus setting is allowed in footnote1.
Only this necessary condition is relevant; its sufficiency wording
is not imported. The cosine model, for real 0<epsilon<1, is an
explicit generic comparison with cancellation; Appendix B's
pointwise modulus inequality assumes epsilon in [0,1]. Its proof
uses squared-modulus expansion and hyperbolic identities. This
model is not actual G or a two-variable radial graph. Reuse the
earlier strong-duality comparison: generalized real chains exceed
the fixed smooth graph class and supply no graph attainment.

Read the primary HTML derivation through (16) and the complete
Appendix B argument; the PDF supplies page numbering and version.
The HTML has formula-layout artifacts and a conflicting rendered date;
neither is a corrected formula or a source revision. Requested PDF
screenshots supplied no readable images, so no screenshot counts as
evidence. No new algebra or independent verification of the cosine
bound was undertaken here. Its explicit primary proof, rather than
the 2021 informal cosine explanation, is the retained comparison.

The target varies only real radial u. Therefore the unrestricted
source variation cannot simply be asserted available at general Du.
Any later application must check radial accessibility with the full
J_u and compact support in {Q_u!=0}. L878's Du=0 calculation is a
previously validated special case, not that general check. The source
does not identify the phases on different components for this F.

Lawrence and Yamauchi, *Normalizing Flows and the Real-Time Sign
Problem*, [arXiv:2101.05755v2, 15 January 2021,
IV B-C, pp5-7; IV D, pp7-8](https://arxiv.org/html/2101.05755v2#S4):
read the iteration (19)-(21), singular-development alternative,
fixed-point discussion, conditional polynomial-action argument and
cosine example. The iteration does not exclude singular degeneration.
A putative fixed point can retain differently phased pieces separated
by zeros. Global perfection uses a conjectured continuous family of
locally perfect manifolds and absence of finite action singularities
for polynomial actions. The cosine example illustrates creation of
canceling pieces at finite zeros. Its informal explanation is not
used as a separate bound proof. These are scoped source statements,
not a general smooth-contour convergence theorem. Here F has a
retained divisor, and no polynomial log-action or continuation family
is supplied. No smooth periodic stationary graph follows.

Reuse the inspected supporting inputs, rather than reprove them:

- Jiří Lebl, *Guide to Cultivating Complex Analysis*, v1.10,
  5 November 2026, [Theorem2.4.7 and finite-zero factorization proof,
  pp49-50](https://www.jirka.org/ca/ca.pdf#page=49), recorded in
  `2026-11-06-odd-divisor-contact-scope.md`. G is entire and
  G(0)>0 by L847, so is not identically zero. Its local finite-order
  factorization is available at every encountered zero, with the
  actual multiplicity retained. It gives no phase-matching theorem
  for a smooth graph and no finite pulled-back contact census.
- Victor Guillemin and Shlomo Sternberg, *Semi-classical analysis*,
  13 January 2010, [Sections13.13-13.14.1, pp449-455](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449),
  and the precise smooth-pullback comparison in
  `2026-11-06-finite-graph-mass-descent-audit.md`. Smooth graph
  variations on compact supports fit differentiation of pullbacks.
  No Moser existence result is imported. The actual first-variation
  expression and its radial consequences still require justification.
- The completed actual-G full-phase assessment's Lotay-Pacini
  comparison, CAG28(2020), Section9.1 Lemmas9.2-9.4, pp666-668,
  [published primary text](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cag/2020/0028/0003/CAG-2020-0028-0003-a005.pdf#page=60),
  is reused only for its nonzero-ambient-form/constant-phase scope.
  It cannot propagate phase across the retained zero divisor.

Full matching and supporting Mathlib coverage remain unchecked;
unknown availability is not absence. No new lemma, mathematical
script or independent reproof is needed for this source comparison.

### Local overlap, failures and searches

Used the supplied full overview and DAG first. Read L847's exact
G,R,C,F, graph orientation and full pullback/homotopy; L868's class
and period threshold; L878's hypotheses, supported coordinate-torus
variation and universal-bound argument. Its accepted audit is reused.
Read L864-L866 hypotheses and conclusions: their local ranks and
fiber conclusions assume real nonnegative density. Read L858-L860
hypotheses/conclusions to check the prescribed-collar/positivity
scope and the local germ/global-extension distinction. Their detailed
proofs were unnecessary because none is a sign premise for TARGET.

The product obstruction in L847 and its ATTEMPTS record concerns
nonnegative product graphs; it does not answer coupled signed
stationarity. The full-phase-two-period stop records compatible
ambient periods, so merely repeating winding numbers cannot supply
the missing alignment. L859/L860's conditional positive germs do
not produce a periodic graph; L864-L866's conclusions cannot be
applied after silently rotating each component to positivity.
C868c and L872/L873 remain scoped failures, not general route bans.
The current full-phase elliptic comparison concerns a controlled
linear inverse and unknown global seed, not the present conditional
stationary graph. No new nonlinear inverse is required or imported.

The bounded new queries were:

- `"locally perfect" "zeros" contours phase stationary`;
- `"holomorphic volume form" zeros stationary "totally real"`;
- `"Riemann" "radial graph" "phase"`;
- `"locally perfect" "zeros" "phase" multiplicity`;
- `"stationary" "holomorphic" "contour" "global" phase zeros`;
- `"totally real" "volume" "zeros" stationary phase`;
- `"perfect contours" "Riemann"`.

Exact-target searches led back to the inspected primary contour
papers; unrelated stationary-phase/dynamical results do not assess
this target. The 2021 proceedings/dissertation and 2024 review were
leads, not additional theorem inputs; their snippets are not evidence.
The older primary proof and the reused zero-factorization/variation
coverage suffice for the proposed bounded test. No essential source
access blocker remains. No novelty or impossibility claim follows
from this search. No cross-notebook theorem input was used.

### Prepared bounded attempt and decision test

Keep the exact TARGET, including every density zero and the global
stationarity quantifier. After separate approval, test whether the
actual product divisor and smooth angular graph constrain component
phases beyond the generic local-perfect result. The new mechanism
to test is compatibility of component phases across divisor contacts,
using their actual finite multiplicities and the squared diagonal,
then global periodic consistency. This is a proposed test, not an
established phase law, finite-cell decomposition or gluing theorem.

First justify any general-Du radial stationarity reduction using
the known local variational input. Then distinguish single-G,
simultaneous-G and diagonal contacts, including coincident factors,
nontransverse/nonisolated preimages and arbitrary actual finite
multiplicities. J is nowhere zero by TARGET, but no component
connectedness or density nonnegativity is assumed. No prescribed
collar, exchange symmetry or contact census may be added silently.

Continue if these checks yield actual global phase alignment and
the stated mass equality, or a rigorous actual-F stationary graph
with a strict mass gap. A local admissible mixed-phase obstruction
can instead disprove a proposed local propagation step, but cannot
by itself refute the global implication; record its limited scope.
A generic cosine example, formal jet or a changed entire function
is not an actual-F counterexample. Abandon an automatic alignment
mechanism if it needs a sign assumption, deletion of a divisor or
the retired ambient-period contradiction. If no conclusion follows,
save the exact compatibility condition still open before reassessing;
do not invoke infinite descent or compactness.

The constrained local variation is supporting specialization. The
proposed actual-divisor-to-global compatibility is the new central
mechanism relevant to the sharp L868 threshold, and justifies a
bounded proof_attempt/creative nomination. No successful mechanism
or result beyond checked sources is claimed. This literature turn
has outcome EXPLORATION; it does not spend or reset the mathematical
exploration budget. The newly ready assessment is subject to the
supervisor's separate approval next turn. PROOF and DAG are unchanged.

## Original nomination — preserved; source gate superseded above

## Exact target retained for source review

The proposed stationarity hypothesis means that for every smooth real
periodic v whose support is compactly contained in {Q_u!=0}, the
derivative at t=0 of B(u+t v) exists and is zero. This is a condition
to assess, not a derived characterization in this turn. The desired
conclusion is the equality B(u)=|M|, with M the original torus period.
All zeros of G and the full squared diagonal remain in the graph.
Nowhere-vanishing J_u is an explicit restriction on this test class,
not a new hypothesis on L868's certificates or the main graph problem.

Essential starting inputs are L847 for the full density and homotopy,
L878 for the accepted finite-descent result and its limits, and L868
for the downstream period use. L864-L866's contact results and the
full-phase source assessment are scoped comparisons. Before using a
contact result, check its actual hypotheses; a nonnegative-density
assumption cannot establish the missing phase alignment. No new lemma,
general-graph variation identity or contact calculation is established
by this nomination.

Plausible use: a positive result would exclude a regular stationary
stall above |M|; an admissible actual-F mixed-phase stationary graph
would identify a precise limitation of that strategy. Neither outcome
alone gives existence or compactness of minimizing graphs, a convergent
flow, a full-class period optimum, higher mixed signs or RH.

## Review and abandonment test

Read the relevant primary fixed-point/zero-separation cases before
larger source extracts, using the existing local source comparison.
Check stronger results and exact assumptions, then decide whether a
bounded actual-F test is covered. Distinguish generic mixed-phase
examples from an actual-G graph, and distinguish a nowhere-zero
ambient form from the retained density divisor. Do not approve an
argument that presupposes connected nonzero locus or nonnegativity.
If no actual-F phase-comparison mechanism survives these checks,
record that concrete obstruction to the proposed implication rather
than repeating an uncontrolled-flow or general-duality import.

This is a new, unapproved target prepared after one completed audit.
It requires a separate source turn. It is not additional literature
on the ready L878 audit. A creative proof nomination, if justified,
must follow the coverage decision and name its precise phase-contact
test; the present task is literature_comparison. Full matching and
supporting Mathlib coverage remain unchecked.
