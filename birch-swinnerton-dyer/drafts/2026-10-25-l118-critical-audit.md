# L118 critical audit — step 490

Completed audit. Approved target: audit L118's finite derived-height
formula for delta against Howard's exact Selmer conventions, tower
hypotheses and all localization and termination steps.

Main gap: rational rank versus arbitrary complex analytic order >= 2.
Intermediate threshold: retain the exact finite defect identity only if
the arithmetic comparison and every algebraic layer survive review.
Possible use: convert future arithmetic bounds on higher full-Selmer
layers into bounds on delta; Sha corank and analytic comparison remain
independent gaps. Repair or narrow any unsupported source application.

The supplied SPECIALIZE assessment predates this invocation. L118 and
L002 have been read fully, with foundations/03; recorded failures in
ATTEMPTS/002 and ATTEMPTS/031 are preserved. L019 remains a comparison,
not an input. Existing unfinished numerical work is untouched.

Verdict: PASS under the stated hypotheses. The complete proof and the
added bounded-error and fixed-index explanations are canonical in
[L118](../lemmas/L118-derived-height-augmentation-defect-accounting.md).
No new lemma or mathematical script was needed. This is REPRODUCTION,
not progress beyond the checked sources.

## Completed discriminating checks

- Tower: every bad prime is away from p and has nontrivial cyclotomic
  Frobenius with open decomposition subgroup; p is totally ramified.
- Conventions: the compact coefficient limit uses downward multiplication
  by p, and the discrete group uses inclusions; they are not conflated.
- Limits: finite comparison systems have Mittag--Leffler kernels.
  Bounded kernel/cokernel exponents suffice after rationalization at
  each fixed index, with no unjustified integral identification.
- Layers: localization of the actual X is exact, and T-killed layers
  rationalize over Z_p. The dimension statement does not assert a
  canonical identification of a height space with a module quotient.
- Termination: one finite-length module supplies a simultaneous cutoff.
  No uniformity in the height index for source error bounds is needed.
- Edge cases: zero module, excluded free summands, nonaugmentation
  support and finite/pseudo-null errors are all accounted for.
- Scope: full Selmer spaces are retained. Neither L003's conditional
  result nor L019's formal obstruction supplies a hidden premise.

Primary source reinspection: Howard, arXiv:1202.6343v1, Section 3 setup,
Propositions 3.4--3.5 and complete local cases, Section 4 equation (9),
Lemma 4.1 and Theorem 4.2 with proofs, Corollary 4.3 with proof,
printed pp.12--17. The finite-generation/cotorsion scope in
Greenberg, arXiv:math/9809206v1, Theorem 1.5 and preceding discussion,
printed p.5, matches foundations/03. These are imported arithmetic
inputs; their full original proofs are not newly reproved here.

The sole direct lemma input is L002, already represented in DAG.md.
PROOF.md's mathematical assembly is unchanged and was not edited.
No source blocker or failed proof case was found. No general rank
comparison, new BSD case or complete candidate follows from the audit.
