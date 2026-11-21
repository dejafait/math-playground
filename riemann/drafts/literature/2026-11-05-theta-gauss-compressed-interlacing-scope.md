# Theta moment compression before interlacing — completed source comparison

TARGET: Assess source coverage and duplicates for replacing the degree-three theta/Laguerre average by two-node Gaussian quadrature in v=u^2 and testing common interlacing of the two resulting reference cubics.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step539 checked primary Gauss–Christoffel exactness and positive-node/weight results, searched exact Gaussian-quadrature/Jensen and Laguerre/common-interlacing phrases, and compared the named local theta/Favard/two-atom stops; queries and read limits below. No matching actual two-node interlacing certificate was located; no novelty inference.
SOURCE_EVIDENCE: Gautschi, Orthogonal Polynomials: Computation and Approximation (OUP2004), Sections1.1.1/1.2.2/1.4.1–2, Theorems1.6/1.19/1.45/1.46, pp1–3/7/20–23, with relevant complete proofs, primary book scan linked below; DLMF3.5(v), equations3.5.18/3.5.20_1, directly inspected. Reused DLMF Laguerre/MSS coverage and GORZ Theorem2 from the named ready assessments.
COMPARISON: Gaussian quadrature covers the positive infinite-support theta pushforward and finite cubic moment dependence, but does not imply common interlacing. L795's full-support and L796's common-Jensen-measure obstructions have different hypotheses. GORZ already covers central degree-three hyperbolicity, so the proposed test addresses a sufficient representation premise only.
GAP: Construct and certify the exact two-node rule from the actual moments, verify the coefficient identity and test the two reference cubics' common interlacing. None is calculated here; degree-uniform control and all-degree mixed positivity remain open.
REASON: Missing essential quadrature coverage is now supplied by precise standard citations. A single conventional finite applicability test is justified; neither a new quadrature theorem nor another low-degree hyperbolicity proof is needed.
SCOPE: Completed literature-only step539 for the unchanged TARGET. Original nomination below is historical and its pending-source language is superseded by the completed comparison. No new mathematical result, lemma or script; the separately specified finite continuation requires next-turn approval.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED lacked the essential arbitrary-measure Gaussian-quadrature theorem, especially unbounded support and nondegeneracy; existing Laguerre/MSS assessments did not supply it.

## Main gap, candidate comparison and bounded purpose

The main gap is actual-Xi all-degree mixed positivity. The intermediate
proposal is to decide whether a degree-dependent quadrature can make
the sufficient common-interlacing premise available at degree three,
despite its failure on the unbounded full theta support. A positive
result could motivate a separately assessed degree-dependent mechanism;
a negative result would stop this precise quadrature fallback. Known
low-degree hyperbolicity is not the sought new conclusion.

Three mechanisms were compared when selecting this continuation:

1. More endpoint/source work or automatic global Mellin import: L804's
   prescribed audit is complete. The global-import stop and the
   sufficient-class stop in
   `../../ATTEMPTS/2026-11-05-actual-xi-levy-sufficient-class-unpaid.md`
   leave the global and sign bridges unpaid. Another endpoint approval
   or inaccessible-supplement retry is not a discriminating next test.
2. Full-support interlacing or a common Favard realization: L795 and
   L796 retain their explicit obstructions. Repeating support pairs or
   the same recurrence cannot remove them. Generic Turan positivity is
   also insufficient by the recorded L772 countermodel, so it is not
   substituted for an interlacing hypothesis.
3. Selected proposal: replace the degree-three integral by a finite
   rule exact for its moment dependence, then test the resulting two
   cubics. This uses actual moments, not an arbitrary two-atom law and
   not a common orthogonality measure for all Jensen polynomials.
   Source comparison must first confirm that this distinction is
   mathematically legitimate and not already a recorded duplicate.

## Exact object for the separate review

Keep L795's definitions without changing the coefficient convention:

    dmu(u)=K(u)du/m_0,   m_j=integral_0^infinity u^(2j)K(u)du,
    P_3(x)=sum_(j=0)^3 (-1)^j binom(3,j)
                         [j!m_j/((2j)!m_0)] x^j,
    F_(3,u)(x)=[3!/(1/2)_3] L_3^(-1/2)(u^2 x/4).

The proposed measure in v is the pushforward of mu under v=u^2.
The question for a primary quadrature theorem is whether it supplies
two distinct positive nodes v_1,v_2 and positive weights w_1,w_2,
with sum one, reproducing its moments through degree three. The
later mathematical test would have to establish the exact identity

    P_3(x) =? w_1 F_(3,sqrt(v_1))(x)
                +w_2 F_(3,sqrt(v_2))(x)

before checking the common-interlacer intervals of the two cubics.
This question mark is deliberate: no theorem application, construction
or derivation is performed in this nomination. Retain the common
leading-sign convention required by MSS, endpoint equality and the
positivity of both weights. No approximate quadrature or dropped
theta tail can replace the requested polynomial identity.

L019/L021 supply the actual positive theta kernel and finite moments;
L795 fixes the exact average and the earlier full-support failure.
For a later finite test, L791's audited actual gamma(0),...,gamma(3)
intervals, as also used in L796, are the nominated numerical inputs.
They retain L778's analytic evaluator and software contracts. The
normalization gamma(j)=j!m_j/(2j)! must be kept; model matching and
model-root conclusions in L791 are not premises. The complete relevant
enclosures, rather than displayed decimal previews, must be inspected
before any certificate is used. None is loaded or replayed this turn.
No cross-notebook input is proposed.

Reuse existing primary Laguerre and MSS coverage while its hypotheses
match; inspect the missing Gaussian-quadrature theorem and its relevant
proof cases, including unbounded support and moment/nondegeneracy
requirements. Check known degree-three/low-degree Jensen overlap and
the targeted local two-atom/Favard histories. Do not reopen all earlier
source searches. Full matching Mathlib coverage is unchecked.

The source-review continuation test is a precise applicable theorem
plus a bounded actual-moment construction/interlacing test, or a
specific incompatibility/duplicate. It must not infer interlacing from
positive weights or assume the desired real roots. A later mathematical
test stops at an exact pair obstruction; a passing pair establishes
only this finite sufficient premise. No degree-uniform estimate,
all-degree representation, mixed-positivity implication or RH solution
follows. There is no justified creative proof attempt yet: the specific
new representation has unread essential coverage and no certified
degree-uniform sufficient-sign bridge. Assess it before allocating such
an attempt, rather than relabel this finite specialization as creative.

## Completed comparison — step539, 5 November 2026

The main gap remains actual-Xi all-degree mixed positivity. The intermediate
target is source coverage for exact finite moment compression followed by
a common-interlacing test. Its plausible downstream use is a diagnostic
for degree-dependent sufficient representations, avoiding the full-support
premise stopped by L795. The source gate is now paid; the proposed pair
test is still unpaid. No mathematical construction was executed here.

### Primary quadrature theorem and essential proof cases

Walter Gautschi, *Orthogonal Polynomials: Computation and Approximation*,
Oxford University Press, first edition 2004, ISBN0198506724,
[primary book scan](https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf):
Section1.1.1, pp.1–3, Definition1.1/Theorem1.6; Section1.2.2, p.7,
Theorem1.19; Sections1.4.1–2, pp.20–23, Theorems1.45–1.46 and
(1.4.4)–(1.4.7). Read these statements and their complete relevant proofs.
The setup is a finite positive measure with all moments finite and a
positive-definite polynomial inner product; infinite support suffices.
Bounded or unbounded support is explicitly allowed. The n-node Gauss
rule is exact through degree 2n−1. Nodes are distinct and interior to
the support's convex hull; weights are strictly positive. Existence
uses Gram–Schmidt, node location uses sign changes, exactness uses
polynomial division, and weight positivity uses squared Lagrange basis
polynomials. Those arguments require only finite polynomial integrals.
No smooth-function remainder, convergence of increasing rules or
moment-determinacy theorem is needed for this target. These are standard
inputs to cite, not to reprove.

Directly inspected [DLMF3.5(v)](https://dlmf.nist.gov/3.5#v), especially
[3.5.18](https://dlmf.nist.gov/3.5.E18) and
[3.5.20_1](https://dlmf.nist.gov/3.5.E20_1), accessed 5 November2026:
it also explicitly permits finite or infinite intervals and states
positive Christoffel weights and polynomial exactness. Its general
derivative-remainder display is unnecessary here. Gautschi's book
supplies the required proof cases and nondegeneracy qualifications.

### Applicability and the difference left to research

Use exactly L795's normalized law and its pushforward under v=u^2.
L019/L021 give positivity and finite moments of every order; L795
establishes full positive support and finite coefficientwise integration.
Thus the proposed pushforward meets the cited infinite-support measure
conditions; no compact-support assumption or deletion of the theta tail
is needed. Its moments are the specified m_j/m_0. These are checks of
existing inputs against the source hypotheses, not a new quadrature
construction or a sign theorem. The theorem is appropriate for n=2;
the later application must verify the exact cubic coefficient identity
in L795's convention. The quadrature orthogonal polynomial is in v
for the raw moment law; it is not the Jensen polynomial P_2 or P_3.
Confusing those objects would silently reinstate the failed Favard route.

Only L791's audited gamma(0),...,gamma(3) intervals, with the inherited
L778 evaluator/analytic/software contracts, are nominated for the later
certificate. L796 identifies their provenance and how to read them.
No numerical interval was used, loaded or replayed here. In particular
the approximate values in L791 are not certified inputs to this review.
Research must recover raw normalized moments using the exact factorial
convention, retain full selected intervals and bound every denominator.
No fitted Jacobi parameter, model root or unknown actual root is allowed
as a premise. The new continuation specifies the bounded calculation.

### Reused interlacing coverage, overlap and recorded failures

Reuse [the ready support-test assessment](2026-11-05-theta-laguerre-support-test.md)
and [its completed comparison](2026-11-05-theta-laguerre-mixture-interlacing.md).
They inspected DLMF18.5.12/13.2.2/Table18.3.1/18.2(vi) and MSS,
*Interlacing families II*, Annals182(2015),327–350,
[Definition3.1 and Lemma3.5, pp.331–333](https://www.cs.yale.edu/homes/spielman/PAPERS/Marcus_Spielman_Srivastava_IFII.pdf).
MSS's finite common-interlacing criterion remains the sufficient premise
to test; it does not follow from quadrature weights being positive.
For the cubics retain the common leading-sign convention by considering
both negatives when invoking its positive-leading-coefficient version.
Weak alternation includes endpoint equality. No continuous-family
extension, independence claim or rank-one realization is needed for
this finite pair. No reproof of the cited equivalence is justified.

Reuse [the low-degree comparison](2026-11-05-central-hermite-theta-gram.md):
Griffin–Ono–Rolen–Zagier, [1902.07321v2](https://arxiv.org/pdf/1902.07321v2),
Theorem2, already covers degrees1–8 at every nonnegative integer shift.
Its normalization comparison applies to L795's normalized P_3. Hence
proving only P_3 hyperbolic would duplicate a known conclusion. The
question here is whether this particular sufficient two-reference
premise holds; the cited theorem does not certify it.

Read L795's full normalization/support obstruction and L796's
hypotheses, exact recurrence and actual-data qualifications; checked
their corresponding ATTEMPTS records. L795 stops a single interlacer
for the unbounded collection of scales, not a finite exact rule chosen
from its moments. L796 stops common orthogonality for the Jensen
sequence, not quadrature orthogonality for raw v moments. These stops
are preserved. Also reused the source gates for actual-prefix Favard,
post-Favard representations, and the two-atom moment/Turan test. The
last constructs an arbitrary atomic counterlaw rather than compressing
the actual theta moments; it does not settle the present pair test.
L772 remains an obstruction comparison, not an actual-theta premise.
No cross-notebook theorem is used. Full matching Mathlib coverage is
unchecked; no absence claim or formal certification is made.

### Search record and decision test

Bounded external queries included `Gaussian quadrature positive Borel
measure infinite support moments 2n-1 orthogonal polynomials theorem
Gautschi`, `site.dlmf.nist.gov 3.5 Gaussian quadrature infinite interval
positive weights`, `"theta" "Gaussian quadrature" "Jensen" polynomials`,
`"Riemann" "Laguerre" "Gaussian quadrature" interlacing`,
`"Gaussian quadrature" "Jensen polynomials"`,
`"Laguerre" "common interlacing" "dilations"`, and
`"theta" "moment" "quadrature" "hyperbolicity"`.
The exact book-theorem-number search was unhelpful. Gautschi's 1996
author-hosted Acta Numerica survey was opened only at its introductory
material; subsequent passage fetches timed out. It is not the proof
authority here. The accessible 2004 primary book resolves that source
need. Search results about kinetic moment hyperbolicity and an
April2026 finite-strip preprint were not inspected and supply no input.
No failure to find a match establishes novelty.

Local phrase searches in the specified theta/Favard/two-atom assessments
and ATTEMPTS, followed by an exact quadrature/compression phrase search
in notebook-local literature/ATTEMPTS, located no earlier actual-moment
two-node interlacing certificate. This is a bounded duplicate check.

Decision: SPECIALIZE. Permit only one later exact moment construction
and finite pair test, detailed in
[the separate continuation assessment](2026-11-05-theta-gauss-two-node-test.md).
A strict incompatible interlacer gap stops this precise fallback. A
certified pass establishes only a finite sufficient premise; an interval
overlap that does not settle the test is inconclusive. Neither outcome
licenses a degree sweep or an all-degree sign conclusion. Creative
central-gap work is still blocked by the absence of a specified
degree-uniform sufficient bridge, not by a global ban on theta methods.
