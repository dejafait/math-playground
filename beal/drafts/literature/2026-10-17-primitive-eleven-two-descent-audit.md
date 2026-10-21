# Exact primitive eleven-adic image — audit source coverage approved

TARGET: Critically audit L085's exact primitive eleven-adic two-descent image, including uniform square classes, both common-scalar whole-fiber realizations and every embedding.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-family discovery and stronger-result comparison in 2026-10-17-primitive-eleven-two-descent-image.md; compared the full L085 source interface with the ready L073 audit assessment, history/276 and ATTEMPTS/033; reopened the three primary sources below. No repeated broad discovery or novelty claim.
SOURCE_EVIDENCE: Reinspected BPT arXiv:2001.02263v3 Section 1 p.3 and Lemma 1.3/Remark 1.4 p.4; Bruin–Stoll 14 March 2008 manuscript Section 2/Remark 2.1 p.3; Clark 161-page notes Theorem 1.79 p.58 and Proposition 2.9/Corollary 2.10 p.65 including the latter proof. Reused inspected Bruin–Stoll Section 9, Section 4 and FNS Section 7.2 equation (7.4) coverage from the construction assessment.
COMPARISON: Full odd-degree Kummer classes, local image sizes and complete-DVR lifting cover this exact audit at all three base factors. The correlated two-class answer and full-fiber realizations are specializations requiring independent arithmetic/proof review; no cited theorem alone imports that answer.
GAP: No essential source blocker remains for the unchanged audit. Uniform containment, exact realizations, embeddings and all certificate arithmetic still require critical verification; global independence and dimension improvement remain outside scope.
REASON: Approve one REPRODUCTION proof_audit next turn on exactly TARGET; this separate source comparison approves coverage and does not verify L085.

Essential local inputs: L033/L034's full map, L041's entire base algebra
and simultaneous scalar witnesses, L042's uniform rescaling and derivative
table, L044's complete primitive scalar exclusion, and L069/L073's fixed
cubic generator, roots and Kummer conventions. No cross-notebook input.

Review the exact alpha lift, (X−c0)/121 residues 9 and 2, strict
2<5/2 separation, square normalization in both M and L, smooth-root
classes, every embedding and rational-factor permutation. For the new
residue-ten realization check the Hensel equation at x=621, reconstruction
of s, and the full degree-ten Eisenstein factor's identification with L.
The certificate has finite arithmetic evidence only; uniform proof is
required. No assumption of subgroup closure, global independence,
class-kernel vanishing or full-rank control is allowed.

If approved, the audit may reuse existing primary source coverage without
unnecessary browsing. Additional source work needs an actual uncovered
hypothesis. Mathlib full and supporting coverage has not been checked.

## Completed source comparison — 2026-10-17

LITERATURE_REASON: The newly specified audit was REVIEW_REQUIRED; compare its exact source interfaces once, reusing the construction assessment's adequate discovery rather than repeating searches for the same target.
SCOPE: Exactly TARGET, with L033/L034, L041/L042/L044 and L069/L073; fixed theta, entire ordered base algebra, one common primitive scalar, full unit square classes and every embedding. No L084 independence calculation or global arithmetic target is approved.

The preceding review checklist is retained as the mathematical audit
specification. Its request for separate approval is satisfied by this
section. No mathematical audit, new derivation or certificate execution
was performed in this literature turn.

### Primary hypotheses and scope

Barrera Salazar–Pacetti–Tornaría, *On 2-Selmer groups and quadratic
twists of elliptic curves*, Math. Res. Lett. 28 (2021), 1633–1659,
[arXiv:2001.02263v3, 17 September 2020](https://arxiv.org/pdf/2001.02263v3),
Section 1 p.3 and Lemma 1.3/Remark 1.4 p.4 were reopened.
The cubic is monic and square-free in characteristic different from two;
the local size lemma assumes a finite extension of Qp. It does not require
the later containment conditions, good reduction or an irreducible cubic.
Products use the full rings of integers. This covers L073's unrestricted
baseline at each base factor. It does not prove anything about correlation
under a common scalar, or subgroup closure of a restricted image.

Bruin–Stoll, *Two-cover descent on hyperelliptic curves*, Math. Comp.
78 (2009), 2347–2370,
[14 March 2008 manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Section 2/Remark 2.1 p.3 was reopened. Odd degree uses the full algebra
modulo squares, with the stated root-point and infinity prescriptions.
Reuse the construction assessment's inspected genus-one interface in
Section 9 p.15 and local constancy methods in Section 4, including Lemma
4.4 and its proof. That algorithm needs its coefficient inequalities and
full factorization; it does not automatically preserve a correlated
modular fiber. The proposed audit checks the direct uniform argument,
rather than assuming the local algorithm computes this restricted set.

Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields
and Adeles*, [161-page notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
no identified revision date: Theorem 1.79 p.58 requires completeness,
integral coefficients and the strict Newton inequality. Proposition 2.9
and Corollary 2.10 p.65 identify the DVR, residue field, irreducibility
and integral closure for a monic Eisenstein polynomial. The proposition's
proof was reread. Reuse Theorem 1.75/Remark 1.76 p.57 coprime-factor
coverage from the construction assessment. These cover the square-root,
tenth-root and factor-lifting methods only after their concrete
hypotheses have been checked in the actual fields. Repeated residue
factors alone do not identify a completion.

FNS, *The generalized Fermat equation with exponents 2, 3, n*,
Compositio Math. 156 (2020), 77–113,
[10 June 2019 final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2 equation (7.4): reuse the construction assessment's inspected
full modular-map and fiber-transport coverage; not reopened this turn.
Neither its GRH-dependent global Selmer calculation nor its dyadic
Lemma 7.6 proves an eleven-adic restricted image. No additional theorem
from that paper is needed for this audit.

### Duplicate, failure and continuation test

The full L085 proof and history/276 record a construction pending audit,
not a duplicate completed audit. The L073 audit covers the unrestricted
baseline, not L085's common-scalar set. The exact-family searches and
stronger conditional FNS comparison are already recorded in the ready
construction assessment; their target and hypotheses have not changed.
There is no basis for a new broad search or a claim of originality.
ATTEMPTS/033's odd full-local class remains valid and does not forbid
reviewing a smaller primitive set. The previously assessed stops in
ATTEMPTS/014,034–037 are retained; no unit search or class backend is
reopened.

Main gap: positive primitive integer emptiness. Intermediate target:
independent critical audit of L085. Plausible downstream use: a later,
separately assessed comparison of this local subgroup with localization
of L084's primitive containing space. Current bounds remain unchanged.
Continue if the audit verifies uniform containment and both exact entire
fibers, with the same scalar and every identification; on a failed claim,
record and repair the precise failure before relying on the local list.
Stop a later filtering use if that comparison proves redundancy. No
independent global condition, class-kernel vanishing, rank bound or
integer lifting follows from source approval.

The audit must independently check the alpha lifts, valuation
normalizations and strict 2<5/2 comparison, square-unit residues in M and
L, smooth-root classes, both Hensel constructions, all modular
reconstruction denominators and the complete degree-ten factor at the
residue-ten scalar. Read the complete relevant certificate values if
used; finite arithmetic alone does not verify the uniform proof.
Mathlib full matching and supporting coverage remains not checked.
