# Actual response zero count — source comparison

TARGET: Derive an eventual simple-zero counting law N_G([H,X])=(X/(2π))log(X/(2π))−X/(2π)+O_H(1) for the actual response G, using L368's nonvanishing carrier and Euler logarithm with closed-endpoint counts.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact real-part completed-zeta/shifted-xi counting searches and a Lagarias differenced-L-function follow-up; inspected primary phase-count proof cases and searched local lemmas, assessments, attempts and relevant October history for duplicates and failures.
SOURCE_EVIDENCE: Lagarias, Acta Arith. 120 (2005), 159–184, arXiv:math/0601653v2 (30 January 2006), Theorems 2.1 and 3.1 with §3 proof, PDF pp. 8–10, and Lemma 4.1(1) with proof, pp. 11–12; Xiannan Li, arXiv:0904.1051v1 (7 April 2009), §2 opening and concluding Remark; reused DLMF scalar coverage from 2026-10-05-gaussian-response-quadratic-sign.md and inspected L005, L366 (1), L368 (3)–(8).
COMPARISON: Known shifted-xi phase counting supplies the mechanism, but its stated count error is O(log X), counts both signs, and does not directly cover G's division by 5/2+it. Ready scalar inputs cover the prospective response-only specialization, not a proved G count.
GAP: Assemble a continuous full phase, bounded Euler-log correction, eventual strictly positive phase derivative, uniformly bounded integrated carrier error, simple zeros and exact closed-endpoint integer counting; these response-specific conclusions remain unproved in this review.
REASON: Approve one bounded reproduction of standard phase counting for the unchanged actual response; no critical-strip zero or actual-pair separation assumption is needed as a source premise.
LITERATURE_REASON: The saved next target is REVIEW_REQUIRED: response-only simple-zero counting with O_H(1) and closed endpoints was outside the prior quadratic-sign assessment.
SCOPE: Exactly L366's response G and L368's carrier on a positive eventual ray [H,infinity), H fixed and sufficiently large, X≥H, ordinary real zeros; distinct and multiplicity counts must agree there. No evaluated onset, F_0/G common-zero claim, signed S(t) comparison or actual-theta sign.

## Queries, primary statements and comparison

Queries submitted:

- `real part completed Riemann zeta function zeros sigma greater than one counting phase Ki Lagarias`
- `zeros real part xi(s) shifted Riemann xi zero counting O(1) gamma argument`
- `Lagarias Zero spacing distributions differenced L-functions arxiv 2005 Theorem 2.1`

Search snippets and secondary discussions were used only to locate primary
papers. No novelty conclusion follows from this bounded search.

J. C. Lagarias, *Zero spacing distributions for differenced L-functions*,
Acta Arithmetica 120(2) (2005), 159–184, DOI 10.4064/aa120-2-4,
[arXiv v2 PDF](https://arxiv.org/pdf/math/0601653v2):
Theorem 2.1(1), pp. 8–9, covers simplicity/interlacing for constant-angle
shifted-xi projections when |h|≥1/2, unconditionally. Theorem 3.1(1),
pp. 9–10, counts |Im s|≤T with the Riemann–von Mangoldt main terms and
O(log T). Its proof uses a continuous logarithm in a zero-free half-plane,
phase levels modulo π, Stirling's formula and an integer-count discrepancy
at most two. Read the complete §3 proof, equations (3.2)–(3.5) and the
final discrepancy bound. Lemma 4.1(1), pp. 11–12, and its proof give
bounded ζ′/ζ for h>1/2 by absolute Euler-product differentiation.
Here the right line corresponds to h=2. G has a variable factor 1/v,
v=5/2+it, inside the real projection, so these are comparison inputs,
not a direct G theorem. The stated O(log T) also falls short of O_H(1).
Do not reuse global monotonicity or global simplicity without the
response-specific check. The weaker-range RH-dependent cases are unused.

Xiannan Li, *The argument of the Riemann ξ function off the critical line*,
[arXiv:0904.1051v1](https://arxiv.org/html/0904.1051v1), §2 opening and
concluding Remark, supplies a second primary comparison: real-projection
zeros are phase levels π/2 modulo π, and in Re s>1 bounded ζ′/ζ makes
the eventual phase increase unconditional. Its general theorem allows
an exceptional set; that theorem is not imported for G. Read these proof
cases and the introductory counting comparison; the exceptional-set
construction and its Selberg estimates are unnecessary here. Ki's paper
is an unread bibliographic lead, not an essential input to this direct
specialization, and no theorem is attributed to it from a snippet.

The prospective proof should use the already audited scalar formulas,
not copy incidental algebraic expressions from the paper extracts.
Reuse the complete gamma/Euler-product comparison in
`drafts/literature/2026-10-05-gaussian-response-quadratic-sign.md`:
[DLMF 25.2.1/11](https://dlmf.nist.gov/25.2),
[5.11.1–2 and §5.11(ii)](https://dlmf.nist.gov/5.11), and
[5.15.8–9](https://dlmf.nist.gov/5.15).
Their domains are Re v>1 and a closed gamma sector away from the
negative real axis. L368's arguments have fixed real part 1/4 and stay
in |arg s|≤3π/4 at large height. That ready assessment records DLMF
v1.2.8, 15 September 2026. The section URLs were retrieved again as
reference locations; no new scalar theorem or reproof is needed.

## Local evidence, duplicates and failures

Read L005 in full, L366's hypotheses and response convention (1),
and L368's carrier proof (3)–(8). L368 supplies a nonvanishing smooth
carrier Qb, a positive modulus, uniform right-line zeta bounds and
carrier phase derivative with O(t^−2) error. L005 supplies the absolute
Euler logarithm on the actual right half-plane; use its specified branch,
not an arbitrary principal argument. These are established local inputs,
not conclusions newly derived in this literature turn.

The search for `N_G`, response counting and phase counting in local
lemmas, literature assessments, attempts and history found no existing
actual-response count proof. Relevant count occurrences in L371 concern
its explicit counterexample. Read the retained failure and prior
interlacing source-review checkpoint: common multiple F_0 zeros defeat
the generic distinct-count inference. The original actual-pair source
blocker involves unconditional signed arithmetic fluctuation, which is
not required for this G-only target and remains blocked. L365's
fixed-positive-regulator stop is unrelated and unchanged. No sibling
notebook or cross-notebook theorem was read.

## Bounded later specialization and stopping test

The main gap remains global actual-theta mixed positivity and L367's
total signed margin relative to its remainder. An eventual G count could
provide a reference count for a future actual-family comparison. Success
would leave the F_0/G relation, L370's signed arithmetic residual, higher
low-index signs, heights above forty and endpoint arithmetic margin open.

A later RESEARCH turn may perform exactly the saved target. It should
use L368 (3)–(8), L005 and L366 (1), and import the scalar named results
by citation. Only the family-specific assembly and elementary endpoint
counting need proof. Obligations, not newly established results:

- Construct a single smooth phase for the complete nonzero carrier,
  including the Euler-log phase; retain its bounded correction uniformly
  along the whole ray.
- Bound the full phase derivative, not just the carrier derivative,
  and exhibit a common finite onset of strict positivity. The existing
  uniform zeta jet and reciprocal bounds are ready inputs.
- Control the integrated carrier error uniformly in X. Do not integrate
  a mere bounded zeta phase derivative over a growing interval to claim
  a bounded phase correction: use the absolute Euler logarithm itself.
- Check every real zero is a transverse cosine-phase crossing on that
  ray, with positive amplitude. Never divide by G or assume its simplicity.
- Count the integer phase levels using ceiling/floor expressions that
  include both H and X when either is a zero. Show an X-independent
  rounding error, and keep the fixed H contribution inside O_H(1).

Continue if these obligations yield the exact requested leading terms
and an error bounded independently of X without any critical-strip
premise. If an obligation fails or only O(log X) is obtained, record that
specific mismatch and park/narrow this certificate; do not claim the
requested count from its main term alone. H may be unevaluated. Neither
an effective threshold nor constant-term refinement is authorized as an
additional target. This assessment does not derive or certify the count.

## Mathlib and outcome

Full matching response count and phase-level coverage: **not checked**.
Supporting Euler-product/nonvanishing coverage is inherited from L005,
including `riemannZeta_eulerProduct_exp_log` and its
[documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log).
Unknown full coverage is not evidence of absence.

Completed kind: LITERATURE; classification: NOVELTY_UNCHECKED;
outcome: EXPLORATION. The evidence is a new adequate theorem-level
comparison and prospective SPECIALIZE coverage, not a mathematical count,
new sign range, RH candidate or advance beyond inspected sources.
The next mathematical specialization should be REPRODUCTION. The newly
ready assessment receives separate supervisor approval next turn.
No lemmas, mathematical scripts, PROOF.md or DAG.md were modified.
