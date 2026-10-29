# Derived-height accounting for the augmentation defect — proposed specialization

TARGET: Specialize Howard's derived-height filtration to express L002's augmentation defect delta as the sum of higher filtration dimensions for the classical cyclotomic Selmer module, without assuming finite Sha.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the full-Selmer assessment of 2026-10-04; targeted local searches in L003, L019 and L026 found no quantitative delta formula there; the 2026-10-25 height review identifies the exact rational-height duplicate and preserves prior failures.
SOURCE_EVIDENCE: Howard, arXiv:1202.6343v1 (2012-02-28), Section 4 setup, equation (9), Lemma 4.1, Theorem 4.2 and Corollary 4.3 with proofs, printed pp.15--17; these give the classical compact Selmer filtration and its module-theoretic dimensions without finite Sha.
COMPARISON: Howard supplies the filtration/radical and elementary-block information; L002 supplies delta as a localized length. Only their exact finite-sum specialization and classical compact/discrete identification remain; reproof of the height theorem is unwarranted.
GAP: The proposed delta identity has not been derived here; next work must justify tower hypotheses, identify Howard's X and augmentation coordinate, and check finiteness of the sum without confusing full Selmer with rational points.
REASON: This quantitatively measures the augmentation obstruction even when the first height degenerates, rather than repeating L003 or the failed radical-to-Sha surjection; it supplies no uniform vanishing or rational-rank theorem.
SCOPE: Only E/Q, odd good ordinary p, classical cyclotomic tower and its torsion Selmer dual; all Howard Section 4 hypotheses must be verified. No finite Sha, height nondegeneracy, residual surjectivity, complex-order comparison or rational-point basis is assumed.
LITERATURE_REASON: The quantitative full-Selmer target differs from the ready rational-height implication and the older radical-surjection review; its precise primary filtration/module statements were inspected during the current stronger-results comparison.

This newly written ready assessment needs separate next-turn approval.
It authorizes no mathematical work during the literature-only step that
created it. Proposed work is a standard-theorem specialization, classified
REPRODUCTION; it is not a claim of novelty.

## Exact source and remaining applicability work

Benjamin Howard, *Derived p-adic heights and p-adic L-functions*,
[arXiv:1202.6343v1](https://arxiv.org/pdf/1202.6343v1#page=15),
Section 4, printed pp.15--17 (PDF pp.15--17), is the inspected primary text.
Its setup requires ordinary reduction above odd p, p unramified in the
base field, ramification above p in the tower, and finite decomposition
of bad primes. Its X is explicitly the dual of the classical infinite
Selmer group. Lemma 4.1 compares finite-coefficient and compact classical
Selmer groups after rationalization using bounded errors. Equation (9)
and Theorem 4.2 give the higher filtration dimensions, whose successive
kernels are the derived heights. Corollary 4.3 describes augmentation
block multiplicities, includes a possible free part, and separates
cotorsion from conjectural nondegeneracy. All these statements and the
relevant proofs were read; no universal nondegeneracy is imported.

Essential inputs are L002 and its foundations/03 conventions, plus this
precise Howard theorem. Compare L003 only to avoid duplication and L019
only to preserve the rational-quotient limitation; neither is a new
mathematical premise. No cross-notebook input is proposed. Reuse the
source assessment
[2026-10-04](2026-10-04-cyclotomic-selmer-height-radical.md) for the
unchanged surrounding formalism.

The proposed threshold is an exact identity between delta and the sum
of dimensions of filtration levels indexed at least two, with eventual
vanishing proved from torsion and the relevant block decomposition.
This is a target, not an identity established in this literature turn.
Next work must check the cyclotomic finite-decomposition condition,
finite/pseudo-null errors, and the use of the canonical polarization.
It must explicitly handle the zero module and show that no contribution
away from augmentation or from a free part is silently discarded.

Continue only if these checks give a finite exact accounting of L002's
defect. Abandon or narrow the specialization if the Selmer conventions
or source hypotheses fail; do not replace a full Selmer filtration by
a Mordell--Weil filtration. Do not create a redundant lemma if the exact
accounting is found elsewhere locally. A successful result could turn
future bounds on higher heights into bounds on delta. The Sha corank s,
production of those arithmetic bounds, and comparison with complex
analytic order remain independent unresolved steps. No claim that such
bounds are presently available is made.

## Mathlib

Full matching arithmetic filtration theorem: not checked. Supporting
localized module classification and finite-sum results: not checked.
Howard is a source for the known arithmetic input, not a Mathlib match.
