# Proposed separate audit of the variable-response empty-cell theorem

TARGET: Critically audit L384's actual-response empty-cell specialization against the complete shifted-S moment errors, variable-phase run bound and one-sided endpoint count balance.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the unchanged exact occupancy comparison and scoped duplicate/failure checks in drafts/literature/2026-10-10-variable-response-cell-occupancy.md; the new canonical L384 is the result to audit, with no changed grid, zero convention or moment hypothesis.
SOURCE_EVIDENCE: Trudgian, Acta Arith. 148(3) (2011), DOI 10.4064/aa148-3-2, Theorem 5.1 and complete Theorems 5.2–5.3 proofs pp. 242–244, Hardy phase (7)–(9) p. 227, and (35), Theorem 4.1, (36) pp. 237–238 were inspected; original Tsang Theorem 4 proof remains unread and no stronger uniformity is asserted.
COMPARISON: The imported continuous moments and strip-count formula cover unchanged hypotheses; ordinary Gram-cell occupancy is only the mechanism comparison, while the actual variable phase and exact complete-cell balance require independent local verification.
GAP: Source scope is approved for the exact saved audit; the mathematical audit of L384 remains undone, including all moving-endpoint and fixed-C error qualifications.
REASON: Separate literature approval confirms reusable coverage for a completed specialization; neither a correctness verdict nor endpoint nonvanishing is established.
LITERATURE_REASON: Supervisor required separate approval of the newly saved L384 audit scope; compare its essential source hypotheses with the existing coverage, without expanding that coverage.
SCOPE: Exact actual response G, complete cells contained in every sufficiently high [T,2T], all strip zeros with full multiplicity, right-continuous N and S, fixed C/log T shift, only m=1,2 and H=T; no RH, common-zero control or physical discriminant premise.

The separate literature approval is complete. This is ready coverage for
the exact TARGET, not an audit verdict. No new literature theorem is
imported beyond the previously approved assessment.
The primary citation is [Trudgian's published version](https://www.impan.pl/shop/publication/transaction/download/product/82370);
Tsang's theorem is used as reproduced there, not as a proof personally
checked. Titchmarsh (1986), pp. 212–213 and Theorem 9.4, is the precise
named count/growth input as recorded in that source.

Essential input IDs: L384, L366, L368, L372. L379 fixes compatible Hardy
notation but is not a mathematical dependency of L384; its absolute-margin
failure and L383's fixed-correlation failure remain preserved contrasts.

The audit should independently check:

- beta+eta is bounded on the same continuous branch as the full phase,
  and (5)–(7) give uniform spacing and a complete-cell count at moving T.
- The right-continuous formula extends the off-ordinate count correctly;
  a zero at a run's left endpoint cancels and every right-endpoint
  multiplicity belongs to exactly one half-open cell.
- The one-zero run residual has absolute value at most one, including
  both run endpoints, and every nonexceptional h-window lies in a run.
- The exceptional-set bound includes both incomplete boundary intervals
  and the h-window extension; the original moment errors give constants
  independent of C before its single fixed choice. No fixed-C o(1)
  error is introduced.
- The Cauchy–Schwarz surplus yields a fixed positive kappa, and the exact
  balance d_T=P_T-Z_T=O(log T) forces c>0 without estimating multiplicities
  in incomplete boundary cells or assuming endpoint nonvanishing.

Continue if these obligations validate the stated theorem. Repair a
specific covered defect with its hypotheses explicit; if a load-bearing
input fails without a justified repair, preserve the failure and narrow
the conclusion. Left-endpoint zeros, strict products, the Wronskian use,
global mixed positivity, L367's total margin, common-zero counts, low
indices, heights above forty and endpoint arithmetic margin remain
unresolved. No matching full Mathlib theorem has been checked.

## Separate coverage approval — 2026-10-10

Compared the full canonical L384 with the prior occupancy assessment,
L372's phase construction, and the scoped source/failure records. L384 is
the result being audited, not a duplicate theorem to derive again. The
L379 absolute-margin and L383 correlation stops concern different tests.
No changed hypothesis requires renewed discovery; the original scoped
search evidence is reused without any novelty inference.

Reopened the published primary paper only to check the essential cited
statement and cases: Theorem 5.1, complete Theorems 5.2–5.3 proofs,
pp. 242–244, and (35)–(36)/Theorem 4.1, pp. 237–238. The stated shift
range includes the proposed shift for sufficiently large T; the length
range includes H=T with a=3/4. The source itself chooses a sufficiently
large fixed shift constant. Use Theorem 5.1's complete error, rather than
the simplified expression (42), whose logarithm differs. The strict-count
notation and right-limit definition still require the local convention
check. No original Tsang proof was retrieved or claimed checked.

These checks confirm existing coverage, not new mathematics or a stronger
source result. The completed step is STALLED / LITERATURE /
NOVELTY_UNCHECKED: approval clears the process gate while leaving the
mathematical verdict open. The subsequent audit is RESEARCH /
REPRODUCTION under SPECIALIZE. Repair only defects inside this covered
scope; a stronger missing input must receive separate review.
