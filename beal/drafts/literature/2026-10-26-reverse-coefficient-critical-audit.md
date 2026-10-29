# Critical audit of the reverse coefficient specialization

TARGET: Critically audit L143's quartic formula for every rational G-connecting class, including the product-cycle, finite-pairing and scalar-quotient identifications.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the prior reverse-isogeny-quartic-class-representation assessment and the split-kernel assessment; L142's separate audit and ATTEMPTS/062 fix the embeddings and stopped same-T shortcut. No changed theorem hypothesis or new search is needed for an audit of the resulting specialization.
SOURCE_EVIDENCE: Bruin–Poonen–Stoll https://math.mit.edu/~poonen/papers/genus3.pdf Section 4 Remark 4.1/Proposition 4.2 pp.6–8, Remark 6.5/Definition 6.7 p.16, Section 6.3.1 p.17, equation (8)/Proposition 6.10 and proof pp.18–20; Schaefer corrected https://arxiv.org/pdf/1507.08325v1 Proposition 2.7 and proof pp.9–10. Essential hypotheses and pairing/representation passages were rechecked during the specialization; the prior assessment retains the complete descent proof review.
COMPARISON: Known generalized descent covers the proposed product datum and its cycle/cohomology comparison. L143's instance-specific map identification, coverage of every rational target class and exact scalar conventions require critical verification; this assessment does not accept that proof.
GAP: Independently audit the embedded finite-map equality and rational-cycle surjectivity, then the coefficient injection and odd-model comparison; correct any failure before relying on L143 for further descent.
REASON: Separate literature approval completed on 2026-10-26 under the supervisor's literature-only gate; reused coverage supports the unchanged conceptual audit, whose instance-specific proof checks remain unperformed.
SCOPE: Audit or repair only L143's stated representation theorem for the actual L142 maps and origins, with its declared evaluation conventions; no Selmer computation, additional rank bound, class enumeration or new mixed exclusion mechanism.

## Reused sources and instance scope

The full bibliographic records and source comparison are in
`2026-10-26-reverse-isogeny-quartic-class-representation.md`.
Bruin–Poonen–Stoll's 74-page author manuscript supplies a fake datum
div(f)=2β−D×Δ, its Cartier-dual torsion map, comparison on degree-zero
cycles, and the exact coefficient/Brauer sequence. Its generality
includes B×E. Schaefer's rational-point case supplies rational divisor
representatives on each factor. No source states the exact marked
instance; L143 supplies that specialization, which remains unaudited.

The audit must verify, rather than presume:

- Actual branch divisors and both infinity fibers in the product datum;
  the origin O_E is not a branch point and H_E is not assumed to be 2O_E.
- Coverage of all Jac(B)(Q)×E(Q) by rational degree-zero cycles and
  safe movement of support, including constants at the fixed basepoints.
- The finite branch-pairing calculation and its identification with F
  restricted to A[2] under exactly L142's map ι, not an unspecified
  automorphism of the three-dimensional module.
- The direction δ_G=F_*δ_2 from the actual composite GF=[2].
- The diagonal μ_2 quotient, exact coefficient injection, and the
  distinction between its image and the entire H¹ group.
- The scalar in X−η, degree-zero cancellation and exceptional-support
  conventions in the comparison to L138; the odd rational component
  must not be erased from the original Kummer map.

Continue only if the theorem holds for every rational target class,
or record a precise correction or missing hypothesis. Preserve
ATTEMPTS/062: exact same-T points are an automatic vanishing check,
not evidence of extra pruning. This audit does not assert rational
Abel-image membership, full Selmer images, point control or Beal
integer recovery. L139–L141 are comparison bounds only.

Essential inputs are L143, audited L142/L127, L110/L111/L113's actual
curves and maps, and L138's quartic transport. No cross-notebook
input is proposed. Mathlib coverage remains unchecked. A creative
mixed exclusion is not yet justified by the representation interface
alone: nonredundancy on independently retained candidate classes is
still unknown. The required conceptual audit is the sole next target.

## Separate source approval — 2026-10-26, step 514

LITERATURE_REASON: The supervisor required separate approval of this newly
saved continuation. This review checks its source coverage; it does not
perform the mathematical audit or enlarge its target.

Reopened the linked primary PDFs, retaining the versions specified above.
Read Bruin–Poonen–Stoll Section 4 pp.6–8, Section 6.1 p.13,
Remark 6.5/Definition 6.7 p.16, Sections 6.3.1–6.3.3 pp.17–20,
and the complete Proposition 6.10 proof. The pairing comparison uses
Albanese–Picard duality. Definition 6.7 allows a variety; it requires
invertible n, nonempty finite étale Δ and the displayed divisor datum.
Proposition 6.10 compares evaluation on cycles, not automatically every
rational Albanese class. Corollary 6.11 retains the cycle-image qualifier.
Equation (8) provides the coefficient injection, not surjectivity onto
the whole cohomology group. The proof checks choice independence,
diagram (11), its pairing triangle and the cohomology comparison.

Read Schaefer Proposition 2.7 and its complete proof, printed pp.9–10
(PDF page 10). Its general conclusion concerns representatives modulo
the isogeny. The proof's rational-point case explicitly supplies a
degree-zero divisor for every rational Jacobian class over that field.
L143 cites this stronger special case; the audit must use that case,
rather than silently strengthen the general proposition.

Local scope comparison: inspected L143 in full and ATTEMPTS/062.
No duplicate new theorem is proposed. Retain SPECIALIZE: the existing
assessment already supplies the essential coverage. The next audit must
check L143's particular product cycles and embedded map against L142,
including its finite pairing argument; source approval accepts neither.
It must also check the scalar and odd-coordinate conventions against
L138. No missing primary source was identified for this bounded task.
No new lemma, proof calculation, source-theorem reproof or Mathlib claim
was made. This repeat approval is STALLED as research progress.

Continuation test remains unchanged: accept only after the formula is
verified for every rational target class; otherwise preserve a precise
failed identification or missing hypothesis. The potential use is an
interface for a later independently tested mixed-class constraint.
ATTEMPTS/062 still blocks extra pruning on exact same-T pairs.
