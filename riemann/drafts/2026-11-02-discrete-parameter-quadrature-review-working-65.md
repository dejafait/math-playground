# Prescribed-node quadrature source review — step 65, saved working notes

The following partial notes were saved before the review was completed.

Literature-only scope: the unchanged TARGET in
`drafts/literature/2026-11-02-discrete-parameter-positive-quadrature.md`.
No new mathematical result or weights have been derived.

Local inputs inspected: L666 hypotheses and (6); L673 hypotheses,
positive coefficients and exact residue remainder (Sections 1--2);
L680 hypotheses, scope and Section 3 attenuation. Reused the recorded
Moreau and ABR assessments. The rate-1/200 baseline and fixed-gauge
stop remain; the segment-positive exclusion is not a discrete-node
exclusion. The main gap remains actual-Xi mixed positivity.

Primary sources retrieved through the web tool:

- Bayer--Teichmann, arXiv:math/0502473v2 (4 May 2005), Theorem 1,
  Corollaries 1--2 and proofs, pp.2--4. General positive discretization
  selects support points; it does not prescribe these nodes or anchor.
- Glaubitz, arXiv:2108.02848v3 (26 May 2022), Theorem 3.5 and proof
  through (3.33), pp.11--12, with Lemma 3.4 proof. Need finish the
  positivity proof and inspect Section 4 analytic error hypotheses.
- Cala Rodriguez--Gonzalez-Vera--Jimenez Paiz, ETNA 9 (1999),
  pp.41--42: construction (2.2)--(2.3), positive weights and
  Theorem 2.2. Prescribed poles are different from prescribed nodes.
  Need finish the stated convergence/error scope screen.

Shell PDF retrieval failed on DNS; the web tool supplies the primary
PDFs, so this is not an essential source blocker. No inaccessible
theorem is being assumed.

Completion: the canonical literature assessment, PROGRESS.md and step-65
history now contain the final decision and routing. Completed Glaubitz's
positivity/error reads and the ETNA convergence screen; also inspected
Trefethen--Weideman Theorem 5.1 with its residue proof and Theorem 9.1
at statement level. Decision EXPLORE, outcome EXPLORATION: no matching
target theorem or new mathematical result. No calculation was performed.
