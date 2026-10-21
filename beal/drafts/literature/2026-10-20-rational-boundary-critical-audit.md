# Rational boundary classification — critical audit source coverage

TARGET: Critically audit L108's rational boundary classification and normalized lifting value, including zero-fiber descent and infinity residue fields.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused boundary and L107 audit assessments; read full L108 and audited L097, L107 normalized-lifting proof, boundary attempt and history 370; compared the exact audit obligations with the primary normalization, Hensel, descent and Kummer results below.
SOURCE_EVIDENCE: Stacks current primary HTML, retrieved 2026-10-20: 33.41.2 (0C1R), 10.153.4 (04GH), 58.2.2 (03QR), 59.28.1 (03PK), statements and proofs; 10.153.9 (04GM) statement/full Newton proof, 10.153.2 uniqueness and 10.153.3(2) with its 8=>2 proof (04GE); reuse L097 Milne v5.10 Proposition 1.16 pp.12–13 and prior L107 coverage.
COMPARISON: The inspected results cover the complete-local and arithmetic-descent methods needed to audit L108; none verifies this model's rational exclusions, support-algebra presentation, quotient uniformizer or infinity stabilizers. Full nonrational boundary decomposition is outside the claimed result.
GAP: No essential source gap remains for the exact critical audit; independent verification of L108 and complete relevant certificate replay remain undone.
REASON: Approve the separate audit using existing coverage plus explicit Hensel hypotheses; this is source readiness, not a mathematical audit verdict or a new boundary theorem.
SCOPE: Audit the exact rational boundary assertion, its actual quotient local parameters, slope residue obstruction, entire infinity descent and stated limits; do not require or invent the unfinished nonrational field decomposition.

The main gap remains both L095 integer systems and compatibility of the
remaining global factors. The audited input sought is L108's rational
boundary calculation, potentially useful as boundary/base-point data in
a later rational-point method. No open point bound or integer elimination
is part of this continuation.

Essential input IDs: L097 and L107, with L106 available only as L107's
existing geometric input. The object of the proposed audit is the full
canonical L108 proof, not a certificate preview. Its finite evidence is
scripts/global-fiber-genus/rational-boundary-certificate.json, produced by
scripts/global-fiber-genus/rational_boundary.py. Retain all 495 labels,
all cycle categories, all five infinity arithmetic orbits and the exact
valuation/unit calculations when checking evidence.

Questions requiring a separate critical review include whether rational
boundary points really force the finite-coordinate residues used at zero
and one; whether the split quadratic at zero yields a residue in E, with
no hidden constant extension; whether the all-zero branch has actual
quotient parameter r and exact unit 1/4; and whether infinity's common
scale disappears under division by r and the leading-pair stabilizer
really determines the entire residue field. Check that the finite-étale
support algebras at one have the asserted meaning without an unproved
octic Galois-group claim. A missed branch, extra residue extension or
incorrect local parameter fails the claimed rational classification.

Unresolved and excluded from the audit's success criterion: all open
rational points; the individual nonrational fields not computed in L108;
both L095 power/gcd/positivity systems; remaining global factors;
minus-eleven; all other Beal signatures. The stronger original full
residue-field continuation test is honestly incomplete. A successful
audit verifies only the stated rational boundary result.

## Primary coverage and exact applicability

LITERATURE_REASON: The newly selected critical audit was REVIEW_REQUIRED; its rational descent, actual quotient parameter and infinity residue-field assertions require explicit comparison before mathematical verification.

Reuse `drafts/literature/2026-10-20-quotient-rational-boundary-fibers.md`
and `drafts/literature/2026-10-20-unmarked-quotient-critical-audit.md`.
Their exact-instance searches found no inspected matching classification;
this does not establish novelty. Duval's algorithm is unnecessary here:
L108 uses complete local algebras, not a newly certified plane presentation.

[Stacks 33.41.2 (0C1R)](https://stacks.math.columbia.edu/tag/0C1R)
requires a reduced Nagata curve and a closed point. It identifies completed
normalization with integral closure and a product of complete DVRs.
The audit must retain L107's actual function field and all its branches;
an affine collision is insufficient. [10.153.4 (04GH)](https://stacks.math.columbia.edu/tag/04GH)
splits finite algebras over a henselian local base. Finiteness and the
completed base must be justified before invoking it.

[10.153.9 (04GM)](https://stacks.math.columbia.edu/tag/04GM),
statement and Newton proof, makes complete local rings henselian.
[10.153.2–3 (04GE)](https://stacks.math.columbia.edu/tag/04GE)
supply uniqueness and lifting for a simple residual root, including
nonmonic polynomials through 10.153.3(2). These cover the formal power
series and split quadratic used in L108 after the stated constant
extensions. The audit must check each derivative, exact coefficient
field and descent action; existence of a lift alone does not establish
a quotient uniformizer or exhaust the branches. The rational-point
hypothesis at zero must precede the asserted residue in E. The split
three-adic valuation obstruction then requires its own exact arithmetic
check, rather than an extra general source or an octic Galois group.

[58.2.2 (03QR)](https://stacks.math.columbia.edu/tag/03QR)
identifies étale field schemes with continuous Galois sets, using fixed
fields of stabilizers in its inverse construction. Apply it to reduced
normalized boundary support in characteristic zero, keeping ramification
multiplicities separately. Infinity requires proving that the full series
stabilizer equals the leading-pair stabilizer; geometric orbit lengths
alone do not prove the asserted arithmetic fields. At one the finite
étale support presentations must be checked as Galois sets, without
assuming their uncomputed splitting or an octic permutation group.

[59.28.1 (03PK)](https://stacks.math.columbia.edu/tag/03PK)
requires the root exponent to be invertible and adjoins a root of a unit
as a finite free étale cover. Reuse audited L107's completed split/nonsplit
unit cases with exponent two and characteristic-zero residue fields.
The audit must verify r is the actual quotient uniformizer, ord(z) is
even and the stated unit is its exact residue. Neither raw z at a
collision nor a discriminant representative substitutes for that unit.

L097's existing audited Eisenstein input suffices for the octic; no
reproof is justified. The mathematical audit should independently inspect
all 495 labels, every cycle category, every infinity orbit and every
load-bearing certificate value together with the unbounded local proof.
No certificate was run or verified in this literature turn. Mathlib full
matching and supporting coverage remains not checked; no absence claim.

Local overlap/failure controls: L108 already records the calculation,
so the next task is verification, not duplicate construction. The boundary
attempt and history 370 explicitly preserve the incomplete nonrational
field decomposition. ATTEMPTS/045 and ATTEMPTS/046-minus-three-joint-factor-at-seven.md,
as assessed in the reused reviews, concern independent parked mechanisms;
no new read or reopening of them is needed. No cross-notebook input is used.

Outcome: LITERATURE / EXPLORATION / NOVELTY_UNCHECKED. Coverage is ready
as SPECIALIZE for the unchanged TARGET; L108 remains unaudited. No lemma,
mathematical script, PROOF.md or DAG.md was changed, and no new mathematical
result or Beal exclusion is claimed.
