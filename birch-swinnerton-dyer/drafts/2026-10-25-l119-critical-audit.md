# L119 critical audit — step 494

Completed audit: **partial PASS; positive-rank normalization handoff held**.
Outcome NEGATIVE / RESEARCH / REPRODUCTION; actual task proof_audit.

Approved target: Critically audit L119's finite Selmer/height certificate using L001, L003 and audited L118, checking the sharp Kummer threshold, ordinary height normalization, absolute determinant error propagation, rational spanning and k=0 case.

The unchanged prior SPECIALIZE assessment is
[the critical-audit scope](literature/2026-10-25-finite-certificate-critical-audit.md).
Main gap: rational rank versus complex analytic order for arbitrary E/Q.
The intermediate target was correctness of the conditional finite-input
interface. Its possible use is removal of p-primary Sha and augmentation
defects for eligible inputs. The test was to retain the full interface
only if every arithmetic identification and elementary implication held.
It does not pass that full test: one source normalization is unresolved.

Read complete L119, L001, L003, L002, L118 and the step-490 audit, with
foundations/03/04 and the prior finite-certificate assessment. Checked the
relevant L019 statement/model and ATTEMPTS/002/031/034. Their weaker-data
obstructions are respected; ATTEMPTS/034 also warns against repeated
conditional-interface work after a successful audit. Existing numerical
failures and unfinished artifacts remain untouched.

## What passed and what failed

The full reasoning and exact failed formula comparison are canonical in
[L119](../lemmas/L119-finite-selmer-height-vanishing-certificate.md), in
particular its step-494 audit paragraph and equations (13)--(14).

- PASS: absolute point balls, polarization at odd p, integral scaling,
  column telescoping, scaling back with exponent N-ak, strict exclusion,
  optional scalar-ball conversion and the nonintegral boundary example.
- PASS: independence before the sharp Kummer chain; exact rational
  p-torsion correction; full Selmer upper bound; vanishing of every
  p-primary Sha element; full rational spanning without saturation.
- PASS: k=0, including the ordinary empty regulator and L003/L118.
- HOLD for k>0: identification of the computed q=-q_H pairing with
  the ordinary regulator convention used to invoke L003. The printed
  sigma differential equations have different constants if their E_2
  quantities are literally equated. The previous sign-only argument
  did not account for this. This is not a counterexample to the intended
  arithmetic height identification or to L119's full proposed conclusion.

## Source verification and limits

Reinspected Harvey arXiv:0708.3404v1, Theorems 1--3, printed pp.1--2;
Section 2.1 equation (2), p.3; Section 2.2 equation (3), p.4; Section 5
pp.11--12 including Lemma 8 and Proposition 9's statement. Reinspected
Stein--Wuthrich (2013), Section 3.5 p.1767, Sections 4/4.1 pp.1769--1771
and equation (4.1), and Section 4.4 p.1774. Precise primary URLs are in
L119 and foundations/04. This was verification of an approved audit
obligation, not a fresh literature assessment or new theorem import.

The arithmetic Kummer and characteristic-order inputs are reused from
the approved assessment and foundations; no original proof of them is
claimed. The newly needed reconciliation with the primary sigma/height
constructions has not been performed or approved here. It is isolated
as REVIEW_REQUIRED for the next turn, rather than hidden in a PASS.

Web PDF text was accessible. A local download for layout inspection
failed DNS resolution and produced no PDF; no local source capture or
image inspection is claimed. The displayed formula comparison uses the
web-extracted primary text. An original-layout/errata check is retained
in the pending source review before drawing a conclusion about the
intended canonical formulas.

No mathematical script or new lemma was needed. DAG.md is unchanged:
the direct mathematical inputs remain L001, L003 and L118. PROOF.md now
reflects the narrower audited state. Mathlib coverage remains not checked.
This audit supplies new negative evidence about the recorded handoff,
not progress beyond the arithmetic literature or a BSD candidate.
