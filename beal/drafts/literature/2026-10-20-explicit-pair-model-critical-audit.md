# Explicit pair model — critical-audit coverage

TARGET: Critically audit L110's explicit hyperelliptic model, inverse maps, transported s,z and exceptional charts.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-instance/Putz searches and duplicate comparison in 2026-10-20-pair-genus-two-explicit-model.md; compared L110's full proof, the L109 audit assessment, history/378 and the scaling/seven-adic failure records; supplementary model/twist searches produced no inspected matching certification.
SOURCE_EVIDENCE: Retrieved van Hoeij math/0203130v1 Sections 1–4 pp.1–4, Poonen ANTS-II author version dated 10 April 1996 Sections 2–3 pp.2–4, and Stacks 53.2.6 (0BY1), including its map-extension proof and 53.2.1–2 in Section 53.2; reused the primary normalized-unit coverage in the L109 audit assessment.
COMPARISON: General sources cover squarefree hyperelliptic presentations, inverse field maps and unique extension on normal proper curves; none inspected certifies L110's sextic, actual Q-form, scalar, marked constant or exceptional values. Exact instance verification remains necessary.
GAP: Independently audit the ordered auxiliary field, full swap fixed field, all exact identities and inverse maps, original s,z including −1/300, dense opens and normalized finite/infinity charts; no such independent audit is performed in this literature turn.
REASON: Essential audit-specific method coverage is now adequate for the unchanged target; specialize by independently verifying this instance in a separate research turn, importing the curve-model extension theorem rather than re-proving it.
SCOPE: Exactly TARGET for L109's audited Q-curve and marking and L110's proposed model; exact coefficient replay and field/local-ring proof audit are covered. Rational-point classification, degree-nine lifting, other twists and integer elimination are excluded.
LITERATURE_REASON: The saved critical-audit target was REVIEW_REQUIRED and outside the prior construction TARGET; this separate turn compares its Q-form, normalization and inverse-map obligations with the existing primary method coverage.

## Gap, relevance and bounded decision test

The main gap remains primitive positive integer exclusion for residual
Beal signatures. On this route rational-point control is unavailable,
and degree-nine rational-root recovery, compatible remaining factors and
both L095 integer power/gcd/positivity systems are independent gaps.
The intermediate target is verification of L110's explicit model with
the original scalar and marking. A reliable low-degree model could
support a later rational-point method; no feasibility of that method
is asserted here.

Continue if independent exact arithmetic and proof review establish the
same Q-function field, a squarefree degree-five/six presentation,
both inverse maps, the exact original s,z and the claimed proper charts.
Repair or withdraw any failing assertion. Matching invariants, the
producer's pass count and numerical tests do not meet the threshold.
A successful audit is neither rational-point determination nor integer
exclusion. This turn approves the test; it does not execute it.

## Primary statements and applicability

M. van Hoeij, *An algorithm for computing the Weierstrass normal form
of hyperelliptic curves*, arXiv:math/0203130v1 (14 March 2002),
[Sections 1–4, pp.1–4](https://arxiv.org/pdf/math/0203130),
was retrieved again. Section 1 starts with an irreducible plane
polynomial over C and requires generators of the index-two rational
subfield and quadratic extension, square completion, square-factor
removal and coordinate expressions in both directions. Sections 2–3
address differential-based construction, and Section 4 exhibits both
maps for a different curve. This is method coverage, not a theorem
that a complex implementation preserves Q or L110's marked twist.
No backend or unread cited subroutine is assumed to have run. L110's
explicit elimination can instead be audited directly. Any justification
that this method applies over Q must check its actual rational
coefficients and field generation, rather than infer descent from the
complex presentation. No algorithm reproof is needed.

B. Poonen, *Computational aspects of curves of genus at least 2*,
ANTS-II, LNCS 1122 (1996), pp.283–306, author version 10 April 1996,
[Sections 2–3, author pp.2–4](https://math.mit.edu/~poonen/papers/ants2.pdf),
was retrieved again. The setting is a perfect field and smooth
projective geometrically irreducible curves; the hyperelliptic
presentation assumes characteristic different from two. The separable
quintic/sextic statement applies in genus two. Section 2 distinguishes
the singular plane closure from its nonsingular model, and describes
the two even-degree infinity branches by y/x^(g+1). Footnote 1 treats
the possible quotient-conic obstruction and its absence in even genus;
Section 3 gives the canonical-divisor construction. These facts justify
the form of the audit, not the computed equation or its scalar.
The audit must verify separability and the actual infinity chart.
The canonical construction need not be reproduced when explicit field
maps supply a different verified presentation.

[Stacks Theorem 53.2.6, tag 0BY1](https://stacks.math.columbia.edu/tag/0BY1),
primary HTML retrieved 2026-10-20, was read with its full proof.
For a field k it relates finitely generated transcendence-degree-one
fields to normal proper curves and their nonconstant maps. The proof
constructs the map on a nonempty open, extends it at DVRs and proves
uniqueness. The associated [Section 53.2, Lemmas 53.2.1–2](https://stacks.math.columbia.edu/tag/0BXX)
requires a proper target for extension and a normal source for the
rational-map/morphism identification. Use k=Q, a perfect field, and
verify the integral function fields and smooth proper models before
application. This supplies extension and uniqueness at excluded
coordinate values once the inverse field maps are verified. It does
not compute those values, make a singular plane model normal, or
assert that affine u,z,s remain regular at every proper point.

For the marked cover reuse the inspected Stacks 59.28.1 (03PK) and
58.11.2 (0BQL) coverage in
`2026-10-20-pair-only-quotient-critical-audit.md`: the root algebra of a
unit is etale when two is invertible, and a connected finite-etale
cover of a normal integral base is the normalization in its function
field. No new marked-cover theorem is needed. L109's audited even-order
and residue-unit rule remains the input. The audit must check transport
of z itself, and use that rule after even-order normalization; zero or
infinity cannot be substituted as a square-class value.

## Duplicate and failure comparison

Reuse the construction assessment's exact polynomial, A11/degree-55,
unordered-pair and Putz searches, with its source versions and scope.
The inspected Putz GFE/3511.m has the original polynomial but supplies
no matching pair-model maps. No claim about unread repository files
is made. Additional queries this turn were `"11" "52" "64" "genus"
"degree 55" curve hyperelliptic` and `"hyperelliptic" "birational"
"quadratic twist" verification maps function fields`. Returned generic
twist/moduli leads were not read or used as theorem evidence. Search
silence establishes no novelty. Broader point-method literature is
outside the target and was not pursued.

Compared the full L110 proof, its construction assessment and
history/378: this is a new independent audit obligation, not another
construction or an existing audit result. L109's ready audit covers
the input curve and normalized marking; its scope excludes L110's
explicit hyperelliptic presentation. ATTEMPTS/048 preserves L101's
scaling obstruction; ATTEMPTS/046-minus-three-joint-factor-at-seven.md
preserves L105's exact local witness. Neither stop is reopened by
checking this global model. L108's unfinished boundary decomposition
is independent and preserved. No cross-notebook input was read.

## Approved audit obligations and continuation

Essential inputs are audited L109 and unreviewed L110, with L109's
L106/L107 inputs inherited locally. Read the full relevant coefficient
evidence in `scripts/pair-genus-two/model-certificate.json` and producer
`model.py`, plus L109's full forget-root/audit evidence if its input
identification needs replay. None was executed or certified this turn.

Check the untwisted ordered auxiliary field separately from the
fixed-minus-three marked extension; nonconstant coordinates and every
generic cancellation; the exact swap action and generation of its
entire fixed field; squarefreeness; both defining relations and inverse
compositions; H1, H0 and the exact original z including −1/300.
Check nonempty dense opens and all normalization charts: finite
branch points, both geometric infinity points with their Q-residue
field, F=0, K=0, T=−2 and T=2. Verify the claimed cancellations and
values in the local rings and distinguish allowed poles from failures
of the proper isomorphism. Preserve v²=z and the boundary unit rule.
The complete relevant coefficients and both basis residuals are needed;
a bounded preview or reported pass count is insufficient.

Unresolved assumptions remain the unperformed L110 audit, rational-point
classification, degree-nine lifting, remaining-factor compatibility,
both L095 integer systems and the minus-eleven alternative. Mathlib
coverage is not checked; unknown coverage is not absence. No new lemma,
mathematical script, curve identity or independent audit result was
created by this source comparison.
