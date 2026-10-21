# L112 positive-rank certificate — critical-audit coverage

TARGET: Critically audit L112's exact Jacobian identification and non-torsion certificate.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-instance search and theorem comparison in drafts/literature/2026-10-21-marked-elliptic-rank-zero.md; read L112, relevant L111 hypothesis/origin passages, history/389 and ATTEMPTS/051; independently retrieved the three cited primary texts and inspected the exact audit-relevant statements. No new exact-rank or point-search target was introduced.
SOURCE_EVIDENCE: Fisher (2022), Section 2 p.2 equations (1)–(2); Milne (2006), I.4 Proposition 4.10 p.35 and perfect-field descent p.38 equation (9); Cremona corrected online second edition, III.3.1 pp.62–63 equation (3.1.2), III.3.3 Proposition 3.3.1 p.69 and its multiple test p.70, III.3.6 pp.89–90 equations (3.6.4)–(3.6.8), all directly inspected on 2026-10-21.
COMPARISON: The cited results cover the general Jacobian, rational-origin group identification, rational scaling, covariant map and torsion-integrality inputs; the remaining work is independent verification of L112's exact specialization and complete certificate evidence, not a reproof of those results or an exact-rank computation.
GAP: The numerical invariant evaluation, exact Q-scaling, witness, syzygy and nonintegral double have not been independently recomputed in this literature-only step; L112 remains awaiting critical mathematical audit.
REASON: Primary hypothesis comparison now supplies adequate coverage for the saved audit, including the nonminimal integral-model case and the distinction between a degree-four covariant map and the rational-origin identification.
LITERATURE_REASON: The newly proposed critical audit was REVIEW_REQUIRED; its exact source applicability required separate approval after the producer calculation. Existing ready rank-method coverage was reused, not replaced by repeated discovery.
SCOPE: Exactly TARGET, with L111/L112 and the existing elliptic-rank-witness certificate. Independent exact arithmetic and evidence replay are permitted for the audit; no new rank search, descent, marked-point method, point completeness or integer exclusion is covered.

## Gap, purpose and decision test

The main gap remains exclusion of positive primitive integer solutions
in the residual Beal signatures. The intermediate target is reliability
of L112's positive-rank claim on the exact L111 quotient. A successful
audit secures the reason to stop rank-zero finite elliptic-point
enumeration before selecting a different point-control mechanism.
Pass only if every essential identification and non-torsion check holds;
otherwise identify and repair or park the failed claim. Useful source
coverage is not an audit verdict or progress beyond the checked sources.

## Primary statements and applicability

Tom Fisher, *On binary quartics and the Cassels–Tate pairing*, Research
in Number Theory 8 (2022), article 74, Section 2 p.2, equations (1)–(2),
[DOI](https://doi.org/10.1007/s40993-022-00376-z),
[publication PDF](https://api.repository.cam.ac.uk/server/api/core/bitstreams/f35e7d09-f88e-4058-959d-b8153d7708cf/content):
for a binary quartic with nonzero discriminant, its smooth projective
genus-one curve has Jacobian Y²=X³−27IX−27J, with the displayed
coefficient formulas for I,J. This is an exact field-level identification,
not just a j-invariant comparison. Over Q there is no characteristic
exception. Audit the actual twisted coefficients and nonvanishing;
solubility, Selmer completeness and Sha vanishing are not additional
requirements of this Jacobian statement. The deeper pairing theorems
are not inputs.

J.S. Milne, *Elliptic Curves*, BookSurge 2006,
[author text](https://www.jmilne.org/math/Books/ectext6.pdf), I.4,
Proposition 4.10 p.35 and p.38 equation (9): on a nonsingular projective
genus-one curve with rational O, P maps to [P]−[O]. The perfect-field
passage explicitly descends the bijection using Galois equivariance.
Use Q and L111's smooth proper geometrically integral curve and origin.
The transferred group structure, rather than a bare bijection, is the
rank interface. The algebraically closed statement alone would not
supply the rational-field justification; both passages were read.

J.E. Cremona, *Algorithms for Modular Elliptic Curves*, second edition,
CUP 1997, corrected online edition,
[Chapter III](https://johncremona.github.io/book/fulltext/chapter3.pdf):
Section 3.1 pp.62–63 equation (3.1.2) permits rational coordinate changes
with nonzero scaling. Section 3.3 Proposition 3.3.1 p.69 requires an
elliptic curve over Q with equation y²=x³+ax²+bx+c and integer a,b,c;
every affine rational torsion point has integral coordinates. Minimality
is not a hypothesis. The p.70 discussion explicitly uses nonintegral
multiples as a test. Audit nonsingularity, integrality, the nonzero
multiple and its reduced denominator. Section 3.6 pp.89–90 equations
(3.6.4)–(3.6.8) provides covariants, their syzygy and a degree-four map
from the quartic to the displayed cubic. Audit the coefficient order,
denominators and scaling. This map is not asserted to identify the
chosen quartic origin with the cubic identity. No general theorem
requires reproof; only exact specialization requires arithmetic.

## Bounded independent audit contract

Inputs are L111, L112, the prior ready rank assessment, and
`scripts/pair-genus-two/elliptic-rank-witness-certificate.json`.
The audit must inspect complete load-bearing evidence, not infer
correctness from the producer's passing-check count. It should:

1. Verify L112 uses L111's actual twisted quartic and rational origin;
   independently recompute I,J and nonsingularity and check the claimed
   integral short model by invertible rational substitution.
2. Independently check the witness on that exact cubic and recompute
   its double, affine nonzero status and reduced nonintegral coordinate.
   Compare the full relevant certificate values and report discrepancies.
3. Check the claimed covariant specialization and syzygy separately
   from the Jacobian/rank transfer. A direct point check can make the
   covariant construction unnecessary for existence, but does not
   excuse an erroneous displayed identity; qualify or repair it.
4. Apply the cited torsion criterion only after its exact hypotheses
   are verified. Record an audit pass only when every essential input
   holds, otherwise specify the failed claim and its effect.

No arithmetic in this contract was executed in this source review.
No rank upper bound, generators, rational-point list or new search is
approved. A positive-rank audit still leaves marked lifts, degree-nine
root recovery, remaining factors, both L095 systems and minus-eleven
unresolved. L111's earlier audited construction is an input; this is not
a fresh audit of all its geometric dependencies.

## Reuse, failure comparison and limits

The prior exact-coefficient and standard-rank searches remain adequate
for this unchanged instance. This review is a reliability check of a
completed known-method specialization, so no new novelty search is
needed. ATTEMPTS/051 stops rank-zero enumeration, not all point methods;
ATTEMPTS/050 concerns a different genus-two bounded search and supplies
no obstruction to this audit. No fallback search, backend installation,
rank computation or certificate replay occurred. Unfinished L108 and all
producer evidence remain preserved.

The Washington PDF access failure in the prior assessment remains an
unread lead, not an input; the directly inspected sources above cover
this audit. No essential source is blocked. No cross-notebook input is
used. Mathlib coverage of the full exact-instance rank statement and
supporting identifications was not checked; no absence is inferred.
