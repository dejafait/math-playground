# Proposed critical audit of the finite split-isogeny specialization

TARGET: Critically audit L142's finite Q-Galois kernels, reverse-map normalization and exact same-T redundancy claim.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the unchanged finite-kernel assessment and its primary theorem comparisons; this continuation checks the instance just written in L142, not a new kernel theorem, source search or descent implementation.
SOURCE_EVIDENCE: Docking https://arxiv.org/pdf/2108.09564v2 Lemma 4.1/proof p.6, Lemma 5.3 p.8, Section 5.2.2 pp.8–9 and Proposition 5.4 Case II/proof p.9; Bruin https://arxiv.org/pdf/math/0408069v2 Section 2.2 and Proposition 2.2/proof pp.4–5 through audited L127; Schaefer corrected https://arxiv.org/pdf/1507.08325v1 Section 2 pp.2–3 for the ordinary connecting construction. All three versioned URLs were opened successfully in recovery step 510; the essential statement ranges and Docking Case II proof were rechecked without broadening scope.
COMPARISON: Known theorems cover the finite branch kernels and abstract connecting sequence. L142 adds explicit labels, quotient-module identifications, the actual G norm coordinates and a point-level redundancy specialization; these instance arguments require critical checking, not a new general theorem.
GAP: Check the exact Q-action and both embedded kernels, the cover class and branch-divisor conventions, G versus F, the rational Abel basepoint, and all rational denominator/ramification cases; neither mixed-class nonredundancy nor arithmetic descent is covered.
REASON: The same finite hypotheses and techniques have adequate primary coverage for a bounded conceptual audit; recovery step 510 repairs the missing direct source URLs and confirms access. The exact saved audit target is ready for a later research invocation; no new target or mathematical claim is approved here.
SCOPE: Exactly TARGET, using L110/L111/L113/L127/L138 and the canonical L142 proof; no local or global image computation, new point search, backend probe, full descent or rank assertion.

## Audit boundary and evidence

Reuse
`2026-10-26-marked-split-isogeny-kernel-descent.md`, including its exact
citations, source qualifications, radical-index typo and F/G distinction.
The completed source comparison is adequate for this verification scope.
This document records source readiness for a later turn; it is not a report
that L142 has passed independent critical review.

## Recovery source verification, step 510

LITERATURE_REASON: The supervisor reported missing direct source URLs in this ready assessment; this narrowly scoped source check repairs that traceability defect, with no changed mathematical target or repeated discovery search.

The versioned PDFs above identify Docking's 24 July 2023 revision,
Bruin's 31 May 2006 revision and Schaefer's corrected 29 July 2015
posting. Docking's Lemma 4.1 proof, Lemma 5.3 and complete Proposition
5.4 Case II proof were inspected again: the inputs concern an unramified
double cover and its Prym; Case II uses the quartic/quadratic split.
The recorded radical-index warning remains applicable. Bruin Section
2.2 assumes a squarefree product of even-degree factors over the ground
field; Proposition 2.2 is the pullback identification used in L127.
Schaefer Section 2 defines the connecting map for an isogeny to a
Jacobian over a number field and identifies its kernel with the rational
isogeny image; function evaluation has additional representability and
injectivity requirements. These statements supply coverage, not a fresh
verification of the notebook's instance. The previous full proof review
is reused for Bruin; no new proof or product-target evaluation algorithm
is claimed. ATTEMPTS/062 was checked for the exact same-T stop and is
unchanged. No Mathlib search or mathematical calculation was performed.

The decisive audit checks are the equality of the actual degree-two
pullbacks on quartic branch differences, ker(p_B^*)=<epsilon>, the
two different three-dimensional permutation constructions, and the
identity j^(-1)(1−iota_*)=p_E,*. In particular do not substitute
2O_E for the quartic hyperelliptic fiber divisor, identify a geometric
kernel with its rational points, or assume a polarization convention.
Check the rational infinity point Z=55 and both T=2 signs. L138's
irreducible quartic transport supplies the missing R!=0 justification.

Accept only if these checks establish exactly L142's limited claims;
otherwise record and repair the precise failure. The duplicate stop
in ATTEMPTS/062 is local to the exact same-T point equations. The
abstract G-image condition has not been evaluated on independently
retained quotient classes, and vanishing does not make a Jacobian
class an Abel image. L141's existing bound, point control, degree-nine
and integer recovery, the L095 systems and all other residual Beal
signatures remain unresolved.

This is a conceptual audit because map directions, branch modules,
Prym transport and the point-versus-group implication interact. It is
not a candidate audit of a complete Beal argument. No new creative
mechanism is asserted; selecting one requires a concrete constraint
not automatic from the exact lift equations. Mathlib coverage remains
not checked, with no absence claim. No cross-notebook input is used.
