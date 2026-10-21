# Rational boundary fibers — arithmetic source comparison

TARGET: Determine the rational boundary fibers of L107's quotient above s=0,1,infinity and their normalized −3 lifting classes.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared full L106/L107, prior quotient/construction/audit assessments, histories 365/368 and ATTEMPTS/045–046; searched rational Puiseux expansions/residue fields, normalization/completion, exact polynomial variants with Putz, and degree-495 boundary classifications; inspected the primary sources below, with no matching explicit boundary classification found.
SOURCE_EVIDENCE: Duval, Compositio Math. 70 (1989), Theorems 2–3 pp.127–132 and Theorem 4 with proof/regularity conditions pp.146–147; standing hypotheses pp.121–122 and conclusion p.152; Stacks 33.41.2 (0C1R), 10.153.4 (04GH), 58.2.2 (03QR), statements and proofs, retrieved 2026-10-20; reuse audited L106/L107 and their prior Kummer/cover assessments.
COMPARISON: Known rational Puiseux, normalization and finite-étale descent results supply the arithmetic method; they do not evaluate this quotient's boundary residue fields or normalized lifting classes. Geometric cycles or ordinary Puiseux coefficient fields alone do not supply that evaluation.
GAP: No essential source gap remains for this bounded specialization; complete arithmetic branch descent, exact rational-point selection and evaluated normalized unit classes are still uncomputed.
REASON: Approve the unchanged arithmetic target for a separate mathematical turn, importing the general results and proving only this model's expansions, descent and completeness; source readiness supplies no boundary result or novelty claim.
SCOPE: Exactly TARGET for the fixed minus-three twist and its quotient; retain every normalized point over all three branch values, with no open rational-point classification or integer elimination.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED because exact arithmetic boundary descent and residue-field identification lay outside the ready generic quotient/audit scope.

The main gap remains primitive integer elimination in both L095 systems
and compatibility of the remaining global factors. The proposed
intermediate target is complete rational boundary data on the audited
quotient, including whether any such point lifts to the fixed marked
curve. Potential use is identifying boundary points and available
rational base points for a subsequent rational-point method. No existence
of a rational boundary point or usefulness of a particular point method
is assumed.

Essential input IDs: L106 and L107, with their full canonical proofs and
certificates under scripts/global-fiber-genus/. L095 is downstream
context, not a premise of this arithmetic target. Geometric orbit counts
do not determine rational residue fields. Affine collisions must not be
counted as individual points on the normalization, and plugging zero or
infinity into z does not evaluate its normalized lifting class.

Continue only if exact arithmetic descent/normalization can account for
every geometric branch over each of 0,1,infinity and identify all rational
ones with their evaluated residue-unit classes. An unresolved residue
field or unaccounted branch prevents a completeness claim. If the method
needs unavailable arithmetic data or cannot distinguish the branches,
record that specific limitation and reassess a different concrete target.
This review supersedes the proposal's source gap, not its unperformed
calculation. It does not assert any boundary point or lifting value.

Both L095 power conditions, gcd/positivity, remaining global factors,
minus-eleven and all open rational-point classification remain unresolved.

## Primary results and applicability limits

Dominique Duval, *Rational Puiseux expansions*, Compositio Mathematica
70(2) (1989), 119–154, version of record,
[journal record](https://www.numdam.org/item/CM_1989__70_2_119_0/),
[primary scanned PDF](https://www.numdam.org/item/CM_1989__70_2_119_0.pdf).
Read the standing characteristic-zero, monic, absolutely irreducible
bivariate hypotheses, Theorem 2's series-field factorization proof,
and Theorem 3 with its residue-map proof (pp.127–132). Theorem 3
identifies arithmetic places, ramification and residue fields from
Galois orbits of rational Puiseux parametrizations. Theorem 4 and its
proof (pp.146–147) establish the rational algorithm's completeness;
conditions R1–R3 control ramification, coefficient-field stabilization
and branch separation. The conclusion (p.152) discusses primitive
squarefree extensions of the setup, but is not used as a fully stated
replacement theorem. Read the rational-versus-classical examples on
p.133: ordinary series coefficients can require a larger field than
the residue field. A primitive plane presentation, if used, must be
proved to represent the actual quotient function field and meet the
stated hypotheses; the present multivariate invariant equations do not
automatically constitute that presentation. No degree-495 complexity or
successful implementation is inferred from the theorem.

[Stacks Lemma 33.41.2, tag 0C1R](https://stacks.math.columbia.edu/tag/0C1R),
current primary HTML, statement and proof: for a reduced Nagata curve,
normalization is finite and completed normalization is a product of
complete DVRs, the integral closure of the completed reduced local
ring. Finite-type curve models over Q satisfy the Nagata requirement;
the correct reduced closure/function field must still be retained.
This supports computing normalized branches through complete local
algebras, rather than identifying an affine collision with a unique
normalized point. It neither computes residue fields nor permits
discarding components. Its proof uses the normalization/local-ring and
completion results cited there; no claim that completion is smooth is
needed or made.

[Stacks Lemma 10.153.4, tag 04GH](https://stacks.math.columbia.edu/tag/04GH),
statement and proof, splits a finite algebra over a henselian local
ring into its local factors. Use only after establishing finiteness
and identifying the relevant completed base. This supports keeping all
arithmetic factors, not selecting one formal expansion and calling it
the whole fiber.

[Stacks Lemma 58.2.2, tag 03QR](https://stacks.math.columbia.edu/tag/03QR),
statement and proof, reconstructs an étale scheme over a field from
its continuous absolute-Galois set; an orbit has the field fixed by a
point stabilizer. Applied to the reduced boundary support in
characteristic zero, this covers residue-field descent and rational
point selection. A ramified fiber itself need not be reduced or étale;
its multiplicities must be recorded separately. One must compute the
actual arithmetic action on normalized branches, not substitute the
geometric monodromy group or three arbitrary branch representatives.

Reuse the primary cover and Kummer coverage in
`drafts/literature/2026-10-20-minus-three-unmarked-quotient.md` and
`drafts/literature/2026-10-20-unmarked-quotient-critical-audit.md`.
In particular Stacks 59.28.1 (03PK) and audited L107 supply the
normalized unit test once a rational point and its local parameter
are identified. Neither another Kummer reproof nor a new genus
calculation is needed. Supporting and matching Mathlib coverage for
this arithmetic boundary classification is not checked; no absence
claim is made.

## Concrete obligations for the separate specialization

Use the existing rational model, not just its geometric twist over an
algebraic closure. Either construct a qualifying plane presentation
for rational Puiseux computation, or explicitly justify an equivalent
complete-local-algebra computation using the cited normalization and
descent results. In both cases prove that all branches of L107's
function field, and only those branches, are retained. The general
theorems are imported inputs, not new claims to reprove.

Treat the three base parameters s, s−1 and 1/s, with suitable finite
coordinate charts at infinity. Retain ramification multiplicities,
coefficient-field conjugacy and every branch in colliding-root cases.
Audited L107 provides the geometric completeness checks: 99 branches
of index five over zero; 168 of index one and 109 of index three over
one; 45 of index eleven at infinity. These are existing data, not
arithmetic field degrees. Every base fiber must retain degree 495
when ramification and residue degrees are combined. The previous
1000-label cap remains applicable to finite label enumeration; it
does not assert a bound on algebraic arithmetic complexity.

For each rational normalized point, specify a genuine quotient local
uniformizer and the exact nonzero residue of z after removing its
even order. Apply L107's square-class criterion to that residue.
Keep this normalized unit class distinct from its discriminant
representative −12 times that unit. A Puiseux parameter on a covering
field is not automatically a quotient uniformizer. A finite prefix is
sufficient only with a proved separation/stabilization bound and exact
leading coefficient, not a precision sample or numerical approximation.
Stop the completeness claim on any unaccounted branch, unproved
residue field, unresolved descent action or uncertified leading term.

## Duplicate checks, searches and outcome

Read full canonical L106/L107, the quotient construction and critical
audit assessments, and targeted histories 365/368. Local searches of
the relevant 2026-10-20 drafts, literature and histories find boundary
enumeration only as the saved proposal; the previous work proves a
generic criterion. Existing certificates contain geometric cycles,
not a ready arithmetic descent classification. No certificate replay
was needed or performed in this source review.

Queries included “Newton Puiseux rational branches residue fields
Duval rational Puiseux expansions theorem”, normalization of completed
curve local rings, exact polynomial variants with Putz/rational, and
degree-495 quotient boundary points. Exact-instance queries returned
no inspected matching theorem; that is not evidence of novelty.
Putz's map identification and special-coefficient limitations are reused
from `drafts/literature/2026-10-20-global-rational-quadratic-fiber-genus.md`;
no new thesis classification is imported. Poteaux's author-hosted
ISSAC paper and later algorithm papers appeared as search leads but
are not needed theorem inputs and were not fully inspected. Secondary
discussions and snippets are not evidence for any conclusion here.

ATTEMPTS/045 preserves its blocked class-group execution route;
ATTEMPTS/046-minus-three-joint-factor-at-seven.md preserves the exact
local witness. Neither blocks this independent boundary arithmetic
test. No sibling notebook or cross-notebook theorem was read.

Outcome: LITERATURE / EXPLORATION / NOVELTY_UNCHECKED. The new source
comparison makes the unchanged target ready as SPECIALIZE. It proves
no model-specific theorem and makes no claim beyond the checked
literature. No lemma, mathematical script, PROOF.md or DAG.md changed.
