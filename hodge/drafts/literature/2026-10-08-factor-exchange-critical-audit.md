# Factor-exchange exclusion — critical-audit coverage

TARGET: Critically audit L076's factor-exchange exclusion, including full tensor transpose and real-slope polystability.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L076, L071 hypotheses/audit passage, complete audited L072, history/158 and 169--170, ATTEMPTS/051 and ready factor-exchange/five-charge-audit assessments; reused their recorded exact-statement searches instead of repeating discovery.
SOURCE_EVIDENCE: Reinspected Stacks 01C8 statement, 01LA items 5--10, 02U4 Lemma 42.38.5 statement/full proof and Lemma 42.38.7/Definition 42.38.8, and 02UM character definition; reused inspected Hatcher Proposition 3.10/Theorem 3.11 pp. 210--212 and cross-product pp. 214--216, and audited L072 base-change/GRR coverage.
COMPARISON: General cup, Chern and isomorphism functorialities cover the audit framework; separately audited L072 covers the destination slice. None imports the full tensor and real-slope specialization verbatim, so an independent mathematical audit remains necessary.
GAP: Verify the full-space adjoint identity, integral pullback and torsion qualification, exact equivalence on all subsheaves/stable summands, and every retained L072 hypothesis. This source review gives no correctness verdict on L076.
REASON: Essential coverage is adequate for one separate REPRODUCTION audit of the unchanged target; no new preservation, inverse-transform or existence theorem is needed.
LITERATURE_REASON: The saved audit target was REVIEW_REQUIRED; this turn approves its source scope by reuse and targeted primary checking, without reopening discovery for the ready application.
SCOPE: Identical marked K3 factors/metrics, L071's full integral -tau_D with q-self-adjoint D on all H^2, integral c_1=0, actual locally free rank-two product slope-polystability at unchanged real Omega, pair (-10,-9), unrestricted initial higher characters and K-class.

## Gap, use and discriminating test

The main gap is universal primitive rational Hodge-class algebraicity.
The intermediate target is independent verification of L076's conditional
residual-pair exclusion. Its downstream use is to retain or correct the
removal of (-10,-9) from the bundle candidates; it supplies no cycle or
transverse transport. Continue with one mathematical audit under this
coverage. Retain the exclusion only if the full transpose, all-subsheaf
slope bridge and destination hypotheses survive; a mismatch requires
correction or narrowing. Source approval does not perform that test.

## Primary inputs and specialization obligations

Reuse [the application assessment](2026-10-08-sign-reversed-factor-exchange.md)
for Hatcher, *Algebraic Topology* (Cambridge, 2002), Proposition 3.10
and Theorem 3.11, printed pp. 210--212, cross-product definition p. 214
and graded product pp. 215--216 ([author-hosted PDF](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf#page=219)).
These passages were inspected in that review, not freshly retrieved here.
They cover cup naturality and graded commutativity over integral and
rational coefficients, not this particular tensor's invariance. The
audit must use L076's Theta convention and the full nondegenerate cup
pairing including the divisor block. Named Poincare duality and integral
Kunneth are standard inputs. Check the torsion-free K3/product qualification
in the rational-to-integral passage; assume no integral NS/T splitting.

[Stacks Lemma 17.14.3, Tag 01C8](https://stacks.math.columbia.edu/tag/01C8)
covers locally free pullback for a morphism of ringed spaces; its proof
is omitted there. [Section 26.24, Tag 01LA](https://stacks.math.columbia.edu/tag/01LA),
items 5--10, records quasi-coherent kernels, pullback and exterior operations.
Neither is a general stability-preservation theorem. Isomorphism sheaf
functoriality with its inverse is the named exact-equivalence input.
The separate audit must check coherence, torsion-freeness, determinants,
ranks and all subsheaves, then compare degree integrals at the actual
real polarization. Stable summands and equal slopes must be retained;
restriction stability or a rational replacement for h would not suffice.
This elementary specialization needs explicit applicability, not a new
stability theorem or a reproof of the imported general tools.

[Stacks Section 42.38, Tag 02U4](https://stacks.math.columbia.edu/tag/02U4),
Lemma 42.38.5, covers flat Chern-operation pullback for finite locally free
input in the locally-finite-type Chow setting. Its complete proof uses
the pulled-back projective bundle, tautological line, flat base change
and uniqueness of the Chern relation. The displayed statement repeats r
for bundle rank and relative dimension. For unambiguous coverage also use
the inspected Lemma 42.38.7 and Definition 42.38.8: Chern classes are
bivariant classes defined using finite locally free pullback under morphisms.
The audit should explain the scope or cite this formulation explicitly,
rather than imposing equality of bundle rank and relative dimension.
This is a source-notation qualification, not a mathematical correction
of L076 in this literature turn.

Named Serre GAGA puts the actual holomorphic bundle in the algebraic
setting on the smooth projective complex product. Keep cycle-class
compatibility and named integral topological Chern naturality distinct
from rational character polynomials. [Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM)
was reinspected for its definition, not unrelated tensor-product proofs.
The audit must retain integral c_1 and actual local freeness before L072.

## Local inputs, overlap, stops and limits

The complete canonical L072 proof and separate audit were read. Reuse
[its ready audit assessment](2026-10-08-sign-reversed-five-charge-critical-audit.md)
and history/158 for Stacks 0A1H/0BDH, Fulton second edition Theorem 15.2
and Example 15.2.8, and the changed-sign every-fibre bridge. No fresh GRR,
restriction or transform-preservation theorem is needed for this application.
Match L072's integer b domain, full fixed tensor, marked metric, rank,
local freeness, c_1 and product-polystability; keep initial higher characters
unrestricted. L071's hypotheses and integral-input audit passage were
checked for source scope, without rederiving their conclusions.

History/170 contains the completed exchange application; repeating it
would not establish a new pair exclusion. Its independent audit remains
distinct. ATTEMPTS/051 preserves the exhausted directional surface filter;
the application assessment records the orthogonal/projective index stops
and parked flat-index source blocker. This target reopens none of them.
No broad search or novelty claim is justified by the unchanged target.

Essential continuation inputs are L076, L071 and separately audited L072.
No opposite-fibre stability, inverse, reconstruction, existence, transport
or cross-notebook input is assumed. The flat (-10,-17) case, larger charges,
other representatives and universal Hodge gap remain unresolved.
Full matching and supporting Mathlib coverage is not checked; no absence
claim is made.

## Outcome

LITERATURE / EXPLORATION / NOVELTY_UNCHECKED: this previously uncovered
audit target is now SPECIALIZE for a separate REPRODUCTION proof audit.
This is source-scope approval with no new exclusion, correction or
correctness verdict. Mathematical exploration usage is zero; no
supervisor-counter reset is claimed. Lemmas, mathematical scripts, DAG
and PROOF are unchanged and prior unfinished work is preserved.
