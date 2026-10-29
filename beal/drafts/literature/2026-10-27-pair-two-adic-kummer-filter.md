# Full dyadic Jacobian Kummer image — source comparison

TARGET: Compute the full Q_2 Kummer image of L138's actual Jacobian and test one constraint independent of L140–L141.
CHECKED: 2026-10-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the real/eleven-adic and marked-octic dyadic assessments; inspected L138–L141, L137's exceptional-prime audit, ATTEMPTS/045,050,052,053-fixed-dyadic,061–063 and history/519. Searched Stoll Jacobian local-image/dyadic completeness, hyperelliptic Q2 descent algorithms, and exact coefficients 76835/Kummer and 67760/Jacobian; no inspected exact-instance answer was identified. Search failure does not establish novelty.
SOURCE_EVIDENCE: Read Stoll, Acta Arith. 98 (2001), DOI 10.4064/aa98-3-4, Lemmas 4.1,4.3,4.4 with stated proofs pp.250–251 and Section 6 pp.267–272 including full Lemmas 6.1/6.3 proofs, dyadic caveat and Lemma 6.4; Bruin–Stoll author manuscript dated 14 March 2008, 19 pages, Remark 2.1 p.3 and Section 4 pp.6–10 including full Lemma 4.4 proof, every SquareClasses/LocalImage step and termination/reciprocal explanations; Clark's 161-page notes, Proposition 2.5/unramified correspondence pp.63–64, Proposition 2.20 p.72 and Theorem 2.24/full proof p.73. Direct links and version qualifications below.
COMPARISON: Known theory supplies dyadic square-class certification, complete curve-image recursion and Jacobian generation/dimension saturation, including quadratic divisors. It does not compute this actual odd-model image or the simultaneous localization of the 39 saved supported classes. Stoll's odd-prime recursion alone is insufficient; Bruin–Stoll supplies its missing dyadic cases, not a replacement of the Jacobian image by a curve-point set.
GAP: Source coverage suffices; exact local field/coordinate certificates, actual divisor evaluations reaching the prescribed dimension, and simultaneous real/eleven/dyadic witness elimination remain instance work. No dyadic dimension, image, independence, rank gain or Beal exclusion is established in this review.
REASON: Fills essential missing coverage for the unchanged target and prepares one bounded reproduction of published local descent; a separate next-invocation approval precedes execution. No new mathematics, lemma or mathematical script is written.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; the prior audit covered a scalar quotient at three, and existing real/eleven-adic assessments did not approve dyadic Jacobian completeness or independence after both filters.
SCOPE: Exactly TARGET on L138's unchanged monic quintic, full square-class product with its rational factor, L139's supported norm kernel and the span of L140/L141's exactly 39 existing witnesses. Includes degree-at-most-two local divisors, dimension saturation or exhaustive chart closure, certified square-class/norm transport and simultaneous coefficient-kernel comparison. No new global witness box, global unit/class basis, backend availability probe, other prime or point classification.

## Relevance and stopping test

The main gap is still residual primitive Beal solutions. The narrower
rank route has upper bound rank Jac(B)(Q)<=7+c<=9, with c<=2, against
the sufficient threshold one. A complete dyadic image could impose
additional conditions on the supported norm kernel. An image calculation
alone does not imply such a gain: localization and independence from
the accepted real/eleven-adic conditions must be checked.

Essential inputs are L138's actual monic quintic, twist, rational point
and complete support; L139's ambient norm-kernel conventions; and
L140/L141's accepted constraints. L144 and ATTEMPTS/063 are contrasts,
not premises for dyadic square-class calculations. Preserve ATTEMPTS/062,
the saturation evidence and unfinished L108. No cross-notebook input.

Success requires a proved complete dyadic Jacobian image and an actual
supported product passing both accepted filters whose dyadic class is
outside that image. Source coverage now supplies a completeness method;
success of the instance calculation is untested. A certified partial
image cannot reject a class. If all simultaneous-compatible combinations
of the fixed witnesses pass, stop this finite witness test; do not infer
redundancy on the entire supported group. Unclosed charts, unattained
dimension or exceeded caps leave completeness unresolved. No larger
sampling run, new global box or backend preflight follows automatically.

## Precise primary inputs and qualifications

Import Michael Stoll, *Implementing 2-descent for Jacobians of
hyperelliptic curves*, Acta Arith. **98** (2001), 245–277,
[DOI 10.4064/aa98-3-4, publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83397).
Read the following passages for this target on 2026-10-27:

- Section 4, pp.249–251: the monic squarefree odd-degree setup,
  Lemma 4.1's natural injection into the full algebra norm kernel,
  Proposition 4.2's local membership characterization, Lemma 4.3's
  branch evaluation and torsion count, and Lemma 4.4's local dimensions.
  For a finite extension F/Q_p the image dimension is
  m_F−1+d_F*g, with d_F=[F:Q_2] when p=2 and zero otherwise;
  m_F counts irreducible factors over F, not factors modulo p.
  The ambient norm kernel has twice this dimension. Lemma 4.4(1)
  cites Schaefer Proposition 2.4 or Milne Lemma I.3.3; its statement is
  imported from Stoll, not treated as an independently read proof there.
- Section 6, pp.267–268, including all of Lemma 6.1's proof: every
  Jacobian class is represented using prime divisors of degree at most
  g and the rational odd infinity. Thus curve points over Q_2 alone
  need not generate. Infinity has value one; branch divisors have the
  separately specified nonzero evaluations. Moving divisors does not
  remove these classes.
- Lemma 6.3 and its full proof, p.269: strict square-class constancy,
  branch-neighborhood and nonintegral-coordinate bounds include p=2.
  The trace/norm diagram and explanation pp.269–270 identify the
  image of a divisor obtained from an extension point with the norm
  of its evaluation. Use the algebra norm after base extension; do not
  substitute a scalar quotient.
- The complete discussion pp.270–272: stop as soon as authenticated
  divisor evaluations span the known image dimension; otherwise
  extensions through degree g may be needed. The displayed recursion
  itself is for odd p. On p.271 the dyadic modifications, including
  nonintegral x, leave details to the reader. Accordingly that code
  alone is not full implementation coverage. Lemma 6.4 p.272 lists
  all six ramified quadratic Q_2 extensions; include the unramified
  quadratic and Q_2 itself when exhausting degree-at-most-two fields.
  The alternative random-polynomial implementation is not a finite
  exhaustion certificate and is not the proposed method here.

Import Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370,
[DOI 10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8).
Fresh inspection used the [author-hosted manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
dated **14 March 2008**, 19 pages. Page numbers below refer to that
file, not the longer arXiv:0803.2052v2 used in the reused octic assessment.

Remark 2.1 p.3 explicitly uses the raw square-class algebra and unique
infinity for odd degree. Section 4 opens on p.6 with a characteristic-zero
complete discretely valued field, finite residue field, integral
squarefree f and its full irreducible factorization. Even residue
characteristic and ramified extensions are allowed; the odd-residue
shortcut of Lemma 4.3 is not used here.

Read Lemma 4.4's entire statement and proof pp.7–8. For irreducible g,
its coefficient-minimum inequality

    ord(g(x0+epsilon*pi^e)−g(x0)) > ord(g(x0))

certifies constant factor square class on the smaller disk
x0+pi^(e+ord(4))*O. The valuation is normalized in the base field of
the recursion; ord(4) must change when that field is ramified. Read all
SquareClasses steps and explanations pp.8–9: finite-ring square tests,
countdown after the last unresolved-factor transition, the constant
nonbranch disk with actual points, the single linear-factor branch
case, and refinement/termination. Read all LocalImage steps and
explanations pp.9–10: integral coordinates, reciprocal chart with
evaluation z(1−z*theta), branch initialization and separate infinity.
The resulting set is a **curve-point** image in raw square classes in
odd degree. Stoll's generation/trace and dimension results are still
required to obtain the Jacobian image; no equality of these objects
is assumed. This addresses the warning in the ready eleven-adic review.

Import Pete L. Clark, *Algebraic Number Theory II: Valuations, Local
Fields and Adeles*, [161-page author-hosted notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
accessed 2026-10-27, revision date unidentified. Proposition 2.5 and
the complete unramified correspondence pp.63–64 supply the unramified
extension case. Proposition 2.20/full proof p.72 splits valuation from
unit. Theorem 2.24/full proof p.73 is the Local Square Theorem over a
Henselian discretely valued field of characteristic different from two:
1+4*pi*O consists of squares. Together with Bruin–Stoll's explicit
finite-ring tests this covers dyadic equality certification. In later
execution keep even valuation and the unit class modulo 4*pi*O, with
the actual normalized ramification; residue-field units alone cannot
decide squareness. No exercise in these notes is presented as a proof.

These imports supply the general mathematics. Their application needs
new instance certificates, not a reproof of Hensel, divisor movement,
local duality or the published recursive algorithm. Full matching
Mathlib coverage of the algorithm and this instance was not checked;
unknown coverage is not evidence of absence.

## Instance comparison and duplicate/failure checks

L138 proves that the actual curve is monic, integral, squarefree of
odd degree five, gives the rational infinity and branch at r=9075,
and identifies the full algebra with Q×K using eta=−907500/(alpha−50).
These verify the cited polynomial hypotheses over Q_2 and every finite
extension used for divisors. The twist, theta image and rational factor
must remain exactly these. This review calculates no local factorization,
uniformizer, image dimension or branch value at two. L137's complete
exceptional-prime records can help certify the local field, but the
power order Z[alpha] may not replace its maximal order at two.

Reuse the ready marked-octic dyadic assessment only for its published
precision/chart tools. L122 concerns another curve, an even-degree point
set and a common-scalar quotient; its tables and images do not transfer.
ATTEMPTS/053-fixed-dyadic preserves the instructive failure that a class
already rejected at the real place proves no additional dyadic loss.
L140 and L141 saturate their respective tested quotients; neither
computes the dyadic image. L144 and ATTEMPTS/063 stop a norm-restricted
mixed quotient at three, not this full Jacobian tuple. ATTEMPTS/061's
dimension shortfall does not stop additional local filtering.

ATTEMPTS/050 exhausts its specified rational point/divisor box; it
does not exhaust the local Jacobian or this local-dimension saturation
method. ATTEMPTS/045 and 052 retain persistent global backend blockers.
The present comparison needs neither a backend probe nor complete
units/classes. Preserve those stops and unfinished L108. No source
checked supplies the exact dyadic instance or establishes novelty for it.

Actual queries included `Stoll Implementing 2-descent Jacobians
hyperelliptic curves 2 adic local image algorithm 6`, `hyperelliptic
Jacobian local image 2 descent Q2 Stoll dimension generators`,
`"76835" "Kummer"`, `"67760" "Jacobian"`, and `hyperelliptic 2 adic
local image Stoll Bruin algorithm LocalImage square classes`.
Schaefer's original proof and the underlying Krasner classification
are references behind the inspected statements, not separately read
sources. No further essential unread source is needed for the bounded
published-method reproduction below.

## Bounded execution contract for a later research invocation

1. Bind the complete relevant L138 model/transport, L139 conventions
   and L140/L141's 39 witness records. Reuse their proved support,
   signed norms and old local conditions. Certify local algebra maps,
   integer lattices, normalized valuations and square-class equality
   in every factor, including the rational coordinate. Certify the
   full factor count before applying Stoll's dimension theorem.
2. Evaluate actual branch classes and then certified local divisors,
   starting over Q_2. Retain exact coordinates or Hensel/finite-ring
   certificates of existence, nonzero evaluations and base transports.
   If their span attains the cited image dimension, that is a complete
   Jacobian image: there is no need to exhaust every point disk.
3. If not saturated, use the inspected dyadic recursion over the
   degree-at-most-two fields, with norms of evaluations for traced
   divisors. Include all branch/infinity cases and reciprocal disks
   when asserting exhaustive closure. Norms must be on the entire
   base-extended algebra, with ramification and possible splitting
   certified. Do not count a degree-two evaluation before tracing it
   into the original Q_2 algebra. Either dimension saturation or full
   certified exhaustion is mandatory before any exclusion claim.
4. On the 39-dimensional **coefficient** space, compute the joint
   kernel of the real quotient rows and eleven-adic quotient rows,
   then localize its basis at two modulo the complete Jacobian image.
   Reconstruct every claimed obstructing product in K and its signed
   inverse-norm rational component; verify both old local memberships
   and its dyadic nonmembership directly. This is feasible finite
   linear algebra and does not require the 39 global classes to be
   independent or generate all of V. A nonzero quotient row supplies
   the requested independent condition; zero only stops this pool.
5. Qualify any resulting ambient codimension by L139's ordinary class
   contribution and the already imposed L140/L141 conditions. Compare
   the resulting bound with one, without asserting Selmer equality,
   rank lower bounds, global realization or point control. Save full
   certificates and independent replay, including failures; a preview
   or producer/replay agreement alone is not a mathematical audit.

Caps for this single attempt: the fixed 39 global columns, matrices
at most 39 by 39 for their comparison, Q_2 and its seven quadratic
extensions only, at most 200000 processed recursion disks total,
depth at most 64 in normalized base-field digits, and at most 2^20
elements per finite residue-ring table. Rational exact intermediates
have at most 8192 numerator/denominator bits. Stop and save actual
versus required values at any exceeded cap; these are failure bounds,
not promises of feasible runtime or guaranteed saturation. A positive
result must include complete square-class equality/independence checks;
partial tables are insufficient. No program runs in this review.

The target remains an established descent specialization. No justified
independently specified creative central mechanism is prepared; the
discovery priority does not warrant relabeling this calculation creative.
This assessment is newly ready and requires the supervisor's separate
approval invocation before research. The literature outcome changes
source readiness only; the main proof and its rank bound are unchanged.
