# Uniform multi-pair tail specialization: prepared1334, approved1335

TARGET: Construct a k-dimensional real polynomial space detecting k prescribed distinct nonreal conjugate reciprocal-node pairs, with a computable common degree and uniform strict negative bound from finite interpolation data and a stated square-tail majorant.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-statement and obstruction search in 2026-11-17-multiple-node-negative-subspace-review-1333.md, step1334; this target is precisely its missing quantitative specialization, not a changed zero-free or positivity claim.
SOURCE_EVIDENCE: Reuse full local L024/L025/L030/L032/C032a and review1333 proof coverage; Deng--Yang--Lu arXiv:2608.11520v1 Theorem3.4/full proof https://arxiv.org/html/2608.11520v1 ; Neiman MFAT19(2013) pp168--170 https://mfat.imath.kiev.ua/article/2013/02/nei2013.pdf ; Yafaev arXiv:1304.2677v1 Theorem5.5 and Theorems3.13--3.14/proof https://arxiv.org/pdf/1304.2677v1 . All three URLs reopened in approval1335; hypotheses rechecked as recorded below.
COMPARISON: Simultaneous finite-support inertia is known, and L032 already has an explicit one-pair degree/tail estimate. The proposed task supplies only the common-space quantitative extension; the inspected indefinite-moment and operator results do not state its explicit polynomial cutoff.
GAP: A common head, real linearly independent witnesses, off-diagonal tail control and an evaluated sufficient degree inequality for every nonzero coefficient vector remain unproved. No assertion of the requested bound is made in this assessment.
REASON: A bounded reproduction/specialization could certify several negative directions in a finite mixed-form diagnostic; a qualitative count or individually negative tests alone would not pass. Separate literature approval1335 repairs the direct-URL omission and approves this unchanged quantitative target for the next research invocation; no mathematics is performed in the approval.
SCOPE: Fixed k>=1, nonzero conjugation-invariant multiset with sum |beta_j|<infinity; k distinct nonreal conjugate pairs with finite positive multiplicities; arbitrary additional nodes, no uniform separation; L030's real algebraic-square form. No actual-Xi sign or finite global RH cutoff.

The source review and precise primary citations are in the completed
[review1333](2026-11-17-multiple-node-negative-subspace-review-1333.md).
This assessment contains only a proposed mathematical task. No new
multi-pair estimate was derived in preparing it.

The bounded test fixes the prescribed pairs w_i, conjugate(w_i) and
uses one radius below all their moduli, one finite set E of distinct
nodes outside it, their multiplicities, and an explicit supplied upper
bound on the sum of |beta| squared over the remaining multiset. The
research attempt must make all interpolation constants computable from
E; a disk supremum without an evaluated finite-data bound is inadequate.
It must output one degree threshold, one common polynomial space and a
strict negative inequality on its entire nonzero coefficient space,
including all mixed terms. L032's one-pair construction is available as
a template, not as a proof that its multiple witnesses span a negative
space. Target normalization may use the minimum prescribed multiplicity;
any chosen normalization must be explicit.

Continue only with that full inequality and degree threshold. Abandon
this diagnostic if the attempt needs unknown actual-Xi separation,
RH-equivalent signs, an uncontrolled matrix condition number or merely
an unspecified eventual degree. No additional source search is needed
under these hypotheses; changed hypotheses require a new assessment.

Essential local inputs: L024/L025 for actual-node summability and
moments, L030 for the exact convergent form, L032 for the assessed
isolator/tail template. C032a is a relevance constraint, never a
positivity premise. Multiplicity enters weights and tail mass; only
distinct nodes enter interpolation. No cross-notebook input.

Successful detection would remain conditional on prescribed nonreal
nodes and available tail data. Actual-Xi positivity, initialization,
singular blocks, analytic identification/realization and global coverage
remain unresolved. This is established-route specialization rather than
a creative central sign mechanism. Full matching Mathlib coverage is
unchecked. No theorem reproof is requested; any canonical result later
written must distinguish the known finite inertia from the quantitative
extension and justify all changes of weight or restriction.

## Separate approval and direct-source repair, step1335

LITERATURE_REASON: Supervisor recovery explicitly requires direct source URLs in the ready assessment; reuse prior adequate proof coverage and repair only that omission, without broadening the target or repeating discovery.

All three direct URLs in SOURCE_EVIDENCE were accessible on 2026-11-17.
Rechecked Deng--Yang--Lu v1 Section 3.2, Theorem 3.4 and its complete
proof: finite distinct conjugation-symmetric support, positive real
weights and equal positive weights on each conjugate pair, with matrix
order at least the number of distinct support points. Its Vandermonde
and congruence argument supplies inertia, not a quantitative tail margin.
This confirms the recorded weight/scope mismatch with L030, rather than
importing its positivity formulation.

Rechecked Neiman's Theorem 1.1 on printed p.170: membership in H_kappa
and biorthogonal bases are hypotheses. Rechecked Yafaev v1 Theorems
3.13--3.14 on printed p.14: bounded positive background sign-function
is a hypothesis; the proof on p.16 uses nonnegativity. Prior complete
perturbation-proof coverage and the discrete finite-rank comparison in
review1333 remain reused. No later Neiman proof or full Yafaev finite-rank
proof has newly been audited, and none is required as an imported result
for the proposed local interpolation specialization.

Decision remains SPECIALIZE under exactly the existing SCOPE and TARGET.
The source comparison is now approved separately from preparation.
This is a process repair, not new mathematical evidence or a new overlap
result. No additional essential source gap was identified for this bounded
attempt. The existing local input proofs must be loaded in the next
research turn before use; this approval supplies no multi-pair inequality.
Full matching Mathlib coverage remains unchecked. No lemmas or mathematical
scripts were changed, and actual-Xi positivity remains unresolved.
