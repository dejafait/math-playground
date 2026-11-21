# Actual conjugate primitive signs — completed source comparison

TARGET: Test whether L882's zero-free radial interiors and two simple conjugate boundary zeros force alpha*beta>=0 or gamma*beta>=0 for L884's actual fixed-lift primitive vector.
CHECKED: 2026-11-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded searches for zero-free-domain primitive inequalities, boundary critical values, univalence, relative periods and xi antiderivatives; scoped duplicate/failure comparison completed. No matching product-sign theorem identified; exact queries and primary passages below. No novelty inference.
SOURCE_EVIDENCE: Pascu-Pascu Bull. Aust. Math. Soc.83 (2011) 210-219, Theorem1.1 p210, Proposition2.1 pp211-212, Theorem2.4 and full proof pp213-215, Corollary2.6 p215, https://doi.org/10.1017/S0004972710000468 ; Lagarias-Montague arXiv:1106.4348v3 (18 August 2011), (1.3), Theorem2.1 p5 and Section4 positivity case pp15-16, https://arxiv.org/pdf/1106.4348v3 ; reuse Lebl CA v1.10 Theorem2.4.7 pp49-50, Theorem4.3.3/Corollary4.3.4 pp100-101 and Theorem4.4.2/Proposition4.4.3 pp104-108 through L882/L883's inspected assessments, https://www.jirka.org/ca/ca.pdf ; Lawrence-Yamauchi 2311.13002v2 II B (9)-(16), https://arxiv.org/html/2311.13002v2#S2.SS2 , and its previously inspected VI A/Appendix B comparison. Qualifications below.
COMPARISON: Nonvanishing derivatives do not give global univalence; applicable criteria require convexity and derivative control missing here. Positivity of the ordinary xi antiderivative on the critical line is not a sign law for these three weighted C* primitives at nonreal G-zero labels. L884's necessary strict products and free-vector limits remain unchanged. No inspected result decides the constrained actual vector.
GAP: One bounded mathematical test must obtain a sign-controlled representation or estimate of at least one actual product using L883's full primitive series and L882's radial domains. No product sign, graph exclusion, uniform margin or actual-label counterexample is established.
REASON: Essential discovery and theorem comparison for the unchanged target are now adequate for a separate EXPLORE attempt with existing exact primitives and elementary complex-analysis tools; no inaccessible source is an essential input. Source-scope approval belongs to the next invocation, not to mathematics in this review.
LITERATURE_REASON: Changed target asks for an actual primitive-sign inequality under L882's radial-domain constraints; the ready L884 audit scope expressly excludes additional actual-label estimates.
SCOPE: L847's actual entire G and full form; L879 smooth real periodic stationary u with J nowhere zero; L882 matched eta=theta=conjugate(zeta)!=zeta, its fixed fibers and zero-free complementary interiors; L883 fixed lifts; accepted L884. Retain all other zeros, multiplicities, actual coefficients and d=0. No product graph, analytic u, new symmetry, graph existence or freely chosen primitive vector.

## Completed comparison — 7 November 2026

STEP_ID: 2026-11-07-actual-conjugate-primitive-source-review-64.
LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. The TARGET text is
unchanged. This is source preparation, with no new mathematical
result, lemma, script, reproof or actual-label estimate. The newly
ready assessment receives separate approval next turn.

### Exact scope and local duplicate check

Used the supplied full PROOF/DAG before detailed reads. Read L847's
full form and orientation, L879's hypotheses and phase/mass conclusion,
L882's hypotheses, matched branch and two-coordinate seed/count proof,
L883's actual primitive formula, and L884's signed-cell proof and formal
controls. Reuse their accepted audits; this is no new proof audit.
Read the three named ATTEMPTS below and the completed signed-cell
comparison. Searched the 6/7 November contact/primitive assessments
and attempt records for primitive boundary inequalities, univalence,
Noshiro-Warschawski and the newly found xi-integral paper. No local
solution of this changed target was identified in that scoped search.
No other notebook or mathematical input from one was used.

The exact vector, bilinear form and two thresholds remain those in
the original nomination below. L882 supplies particular radial
domains, not a zero-free disk of radius |zeta|, a convex domain, a
conjugation-invariant domain or a bound on the argument of G. None
of those stronger premises may be silently added. Stationarity and
J nonvanishing stay conditional; no actual nonreal label is supplied.

### Primary results inspected and applicability

Mihai N. Pascu and Nicolae R. Pascu, *Neighbourhoods of univalent
functions*, Bull. Aust. Math. Soc. **83** (2011), 210-219,
[Theorem1.1 p210; Proposition2.1 pp211-212; Theorem2.4 pp213-215;
Corollary2.6 p215](https://doi.org/10.1017/S0004972710000468).
The first criterion requires analyticity on a convex domain and
Re f'>0. The stronger perturbation theorem assumes nonconstant
analytic f, convex D, univalent analytic g and
|f'-g'|<=K(g,D), where K is the infimum of absolute secant quotients.
Read its entire proof, including the equality case: minimum modulus
forces the auxiliary secant function constant, reducing to a linear
g and a strict derivative inequality unless f is linear. Read the
compact-subdomain qualification in Proposition2.1 and its boundary
counterexample. L882 gives neither convexity nor either derivative
bound. Global univalence, even if separately obtained, is not the
requested bilinear sign. The introductory exponential example only
warns against identifying local with global univalence; it is not a
counterexample satisfying L882 or actual G. No theorem is imported
as a sign premise. [Direct primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A86D1D7480059DF7EB6ABABA82F9BA90/S0004972710000468a.pdf/neighbourhoods_of_univalent_functions.pdf).

Jeffrey C. Lagarias and David Montague, *The Integral of the Riemann
xi-function*, arXiv:1106.4348v3, 18 August 2011; journal reference
Comment. Math. Univ. St. Pauli **60** (2011), 143-169.
Read [(1.3), Theorem2.1 p5, and Section4 pp15-16](https://arxiv.org/pdf/1106.4348v3).
For real deformation parameter the integrated family has finitely
many real zeros; for parameter <=0 only the origin remains. The
parameter-zero case proves integral_0^t Xi(x) dx>0 for real t>0.
Its positivity proof pairs successive sine lobes against the positive
decreasing real theta kernel; the <=0 extension preserves that
monotonicity. These are ordinary antiderivatives on a real parameter
line. They do not sign L884's three weighted increments at nonreal
labels. Using the lobe argument here requires a new representation
and its own monotonicity proof. Theorem2.2's value-set statement was
inspected only for scope; its full proof is not coverage or an input.
No primitive substitution or new specialization was derived today.

Reuse the inspected standard results in
`2026-11-07-contact-cell-relative-period-test.md`: Lebl, *Guide to
Cultivating Complex Analysis*, v1.10, 5 November 2026,
[Theorem4.3.3/Corollary4.3.4 pp100-101](https://www.jirka.org/ca/ca.pdf#page=100)
and [Theorem4.4.2/Proposition4.4.3 pp104-108](https://www.jirka.org/ca/ca.pdf#page=104).
Holomorphic primitives require a simply connected domain; the log
corollary requires nonvanishing there. Laurent series converge on
compact subannuli, and a nonzero residue requires a tracked log term
rather than a single-valued C* primitive. Proposition4.4.3's proof is
an exercise in the source, not a read proof. L883 has already checked
and evaluated these tools for the exact weighted increments; use that
formula rather than reprove Laurent theory. No sector or sign bound
comes from existence of a holomorphic logarithm. A log of G at its
boundary zeros is not allowed.

Reuse `2026-11-06-stationary-graph-phase-components.md` for
Lawrence-Yamauchi, *Convex optimization and contour deformations*,
arXiv:2311.13002v2, 14 August 2024, [II B (9)-(16), VI A (44)-(51)
and Appendix B (76)-(79)](https://arxiv.org/pdf/2311.13002v2).
Reopened the zero-separated-component passage and cosine-model
discussion; retain the prior full Appendix B proof comparison and
its real parameter range 0<=epsilon<=1. It supplies no actual-G
primitive sign law. The generic model is not an L882 counterexample.
The stronger analytic-continuation assertion is explicitly conjectural
in Section II.3 and is not an existence premise here. Merry's Stokes
input is reused only through audited L883, with no fresh derivation.

No full matching or supporting Mathlib search was needed for this
comparison; coverage remains unchecked, not absent.

### Search record, unread leads and access limits

Queries issued (including unproductive combinations):

- `holomorphic primitive zero free starlike domain boundary zeros univalent derivative nonvanishing Noshiro Warschawski`;
- `Riemann xi function primitive values at zeros integral inequalities conjugate zeros`;
- `"holomorphic" "relative periods" "zeros" sign`;
- `"Convex optimization and contour deformations" "one-dimensional" zeros`;
- `"Noshiro" "Warschawski" theorem convex Re derivative pdf`;
- `"zero-free" "primitive" "univalent"`;
- `"holomorphic" "boundary zeros" "primitive"`;
- `"xi" "primitive" "conjugate" "zeros" integral`;
- `"holomorphic" "primitive" "boundary zeros" sign inequality`;
- `"zero-free" "starlike domain" "argument" primitive`;
- `"Riemann" "weighted integrals" "xi" zeros primitive`.

Search snippets and claimed RH proofs are not theorem inputs.
Cowling-Royster, *Some applications of the Weierstrass mean value
theorem*, J. Math. Soc. Japan13(1961), pp104ff, was a promising
Noshiro-Warschawski lead, but its primary PDF fetch timed out and an
alternate URL failed. It remains unread; Pascu-Pascu supplies an
accessible primary treatment of the exact criterion and stronger
comparison, so this is not an essential blocker. Romik's xi paper
at the returned author URL gave 404; no theorem from it was used.
Translation-surface relative-period search hits concern different
compact differential/stratum hypotheses and were not read as inputs.
The broader boundary-conformal, 2026 positive-derivative and
multidimensional-univalence hits are unread leads with additional
premises, not coverage. PDF screenshot calls yielded no readable
images in this tool session; the cited complete proof ranges were
read as primary extracted text, not inferred from image previews.

### One bounded mathematical continuation after separate approval

EXPLORE covers exactly TARGET, with a concrete test using actual
primitive data: substitute L883's convergent series or weighted arc
integrals into one of the two products and seek a sign-controlled
paired integral, retaining its finite polar terms and full residue
increment. Use the actual G and the specified radial domains; compare
any proposed sign kernel with the actual zero/domain constraints.
The sine-lobe source supplies a possible comparison mechanism only;
its monotonicity hypothesis has not been checked for such a kernel.
No coefficient or kernel identity has been derived in this review.

The decisive threshold is a rigorous >=0 value for alpha*beta or
gamma*beta on the conditional actual-label range, including equality.
A smaller rigorously specified range may be useful if every unhandled
label is stated. No finite numerical search for nonexistent supplied
off-real labels, free-vector substitution, or replacement of G is
approved. Any infinite expansion or contour change needs the existing
compact/convergence hypotheses checked, with a proved remainder if
truncated; an absolute upper bound alone supplies no product sign.

Continue only on a sign-controlled representation or estimate using
the actual data, or an informative obstruction to that proposed
representation. Stop this bounded mechanism if it requires unproved
convexity, a derivative half-plane bound, kernel monotonicity or a
zero-free disk, or recovers only the known total/common-line algebra.
Preserve that obstruction rather than repeat generic source searches.
No claim that such a representation exists is made. No mathematical
exploration turn was spent today.

Nominate proof_attempt/creative, deep_research/max, after separate
source-scope approval: the precise obstruction is simultaneous
sign control of the actual weighted conjugate periods, which could
exclude L879's matched stationary branch toward L868. This is an
unproved actual-function mechanism, not routine specialization of
univalence or of the ordinary xi-integral positivity result. The main
gap, other branches, graph existence, compactness, sharp bound and
Xi transfer remain unresolved. Additional new techniques outside this
stated scope require REVIEW_REQUIRED.

## Original nomination — historical, missing review discharged above

The main gap remains L030-L032/C032a all-degree actual-Xi mixed
positivity. The proposed intermediate target would exclude one
conditional stationary branch in L879 by contradicting L884's strict
signs, potentially narrowing the graph problem toward L868. It would
leave other label branches, existence and compactness, the sharp bound,
higher signs and Xi transfer unresolved. No complete route is claimed.

Use exactly L884's actual vector
v=-i[H(conjugate(zeta))-H(zeta)+i(b-a)r], w=2pi*r-v,
with a<b<a+2pi and r=(a0,a1,a2), and its definitions of alpha,beta,gamma.
The threshold sought is a proved nonnegative value of at least one
of the two products, including equality. Numerical evidence, an
uncontrolled series truncation or a bound on a freely chosen v would
not meet it. No calculation or estimate of these values was made in
the audit or this nomination.

The potentially relevant additional mechanism is control of the
actual primitives by a zero-free radial domain with exactly the two
simple conjugate zeros on its boundary, rather than free period
algebra. First search exact and stronger statements under standard
terminology for holomorphic primitives, zero-free domains, boundary
zeros and signed relative periods. Retrieve primary hypotheses and
essential proof cases for any relevant lead before using it. Reuse
the approved stationarity, factorization, Stokes and primitive
coverage; rereading them alone cannot approve the new sign estimate.
No uninspected named theorem is offered as an input here.

Preserve the limitations in
`ATTEMPTS/2026-11-07-boundary-fiber-count-only-limit-55.md`,
`ATTEMPTS/2026-11-07-contact-cell-conjugate-label-limit-57.md` and
`ATTEMPTS/2026-11-07-signed-cell-period-algebra-limit-61.md`.
They stop repetition of counts, common-line reality and free-vector
algebra. They are not counterexamples to the actual-label assertion
or global bans on relative-period methods. The signed-cell assessment
did not cover an inequality on the constrained primitive vector.

Continue only if the source comparison gives an applicable import or
a concrete, separately testable estimate using actual primitive data
or the radial-domain information. Abandon this proposed mechanism if
it only recovers the existing total/common-line conditions or needs
an unproved positivity, graph-existence or stronger-domain premise.
Record that specific obstruction; do not repeat a generic review or
infer novelty from failed searches. If a rigorous smaller range is
the available result, state its exact range and the unhandled labels.

The immediate next turn is literature_comparison, standard/high. A
later mathematical route must be selected after that comparison;
this document approves neither a new mechanism nor a calculation.
Mathlib full matching and supporting coverage for this changed
target has not been checked. This is not an absence claim.
