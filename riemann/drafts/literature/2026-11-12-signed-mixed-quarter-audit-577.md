# Nomination: conceptual audit of the fixed mixed quarter comparison

TARGET: Critically audit C999m Sections12-17's fixed mixed-covariance quarter comparison, including complete input/output tails, exact finite-map connection and arithmetic, without assuming endpoint-complement coercivity.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse approved562/563 and completed561's exact mixed-form/Schur search, stronger-result comparison and scalar/derivative/response-prefix/automatic-factorization failures; inspect the specific step574/575 histories and C999m(41),(46),(48),(51),(58),(66),(71). No new broad search or novelty inference is made for auditing the same fixed test.
SOURCE_EVIDENCE: Reuse the primary proof cases actually inspected in ready562/approval563: Friedrich-Gunther-Klotz arXiv1708.01545v1 Definition4.1, Proposition5.4/Theorem6.1 and proofs pp5/9-10; Dritschel-Rovnyak arXiv0903.3639v1 LemmaA.1 and both proofs pp28-29; Behrndt et al. arXiv1403.5704v1 Proposition2.1 p4, Corollary3.5 p12 and nonnegative proof case p11; Teschl GSM99 author version12February2009 Theorems2.13/2.18 pp71-72/77; Li paper45 displayed v2 Sections4-5 (4.4)-(5.5). The inherited IEEE754/directed-Decimal and exact-entry contracts are canonical in C744v/w/z and C999k/l, rather than a new library-FFT theorem.
COMPARISON: These sources cover the weighted closed-form/covariance method, inverse order and conditional Schur assembly. They supply no fixed quarter constant, no saved-array accuracy, no endpoint-complement sign and no global RH inference; the local proof and entire relevant certificate evidence must be critically checked.
GAP: Independently check that Sections12-17 establish their claimed complete mixed-map bound under exactly the inherited contracts, with correct orientations, every input/output/low-mode correction and arithmetic allowance; detect any unpaid term, domain failure or invalid covariance combination.
REASON: Separate literature-only approval578 confirms the unchanged audit target is covered by reused561/562/563 and the reopened primary Schur cases. SPECIALIZE is ready for one REPRODUCTION conceptual audit; this approval does not verify the numerical proof or supply a mathematical advance.
SCOPE: Same ell=log(3)/2, independent complex endpoints, head2:511, tail n>=512, exact two moment corrections, original D/S/T/U, exact C999l predictor and fixed proxy, reference d0=6.14/fraction1/2/penalty256, K=65536 and J=32768, same quarter allocation. Audit only; no tuning, new predictor, reference change or complementary sign assumption.

This target is relevant to the L030-L032/C032a actual-Xi positivity gap
because a sound mixed-quarter estimate would pay one concrete interface
in a possible later Schur assembly. It leaves the independent comparison
F(0,y)>=||y||_tail^2/4, C744q margin, H2 slack/existence, non-neutral
coverage, whole-core/c_* and global transfer obligations unresolved.

The bounded test is to uphold or identify a specific defect in the
combined claimed quarter estimate. Inspect full load-bearing proof ranges
and evidence, not diagnostic eigenvalues, hash checks alone or JSON
previews. Recompute only meaningful required ledgers. Preserve all prior
failure evidence and distinguish source import, local specialization and
informal audit from formal verification. A repaired or rejected local
estimate is not a proof/disproof of RH.

Primary links reused from the approved assessment:
[Friedrich-Gunther-Klotz](https://arxiv.org/pdf/1708.01545v1),
[Dritschel-Rovnyak](https://arxiv.org/pdf/0903.3639v1),
[Behrndt et al.](https://arxiv.org/pdf/1403.5704v1),
[Teschl](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
[Li, paper45 displayed v2](https://rstation.ai/problems/riemann_hypothesis/papers/45).
No new external passage is claimed to have been opened in this nomination.

Full matching Mathlib coverage is unchecked, not asserted absent. The
future audit should be REPRODUCTION and conceptual_audit: the delicate
points are directional input covariance versus norm sums, exact/proxy
predictor cancellation, adjoint action, and disjoint-input versus
same-column error accounting. This is not a new creative mechanism or
an RH candidate audit. Essential review of the new combined bound takes
precedence over manufacturing a creative target to satisfy a schedule.


## Separate source approval — step578, 12 November 2026

The invocation-start nomination577 is now separately approved for its exact
TARGET and SCOPE. No target, predictor, reference, cutoff, quarter allocation
or mathematical claim is changed. This completes a source gate only;
STEP_OUTCOME is STALLED because the source decision repeats adequate prior
coverage rather than adding a mathematical input or informative obstruction.
LITERATURE_REASON: The supervisor requires separate approval of the newly
nominated audit of the combined Sections12-17 argument; reuse adequate
coverage rather than repeat discovery or invoke mathematics in this turn.

### Primary cases actually reopened

[Friedrich–Gunther–Klotz, arXiv1708.01545v1](https://arxiv.org/pdf/1708.01545v1),
Definition4.1 printed p5, Definitions4.4-4.5 p6,
Proposition5.4 pp9-10 and Theorem6.1 p10 were inspected again.
The PDF has internal date30July2018. Positive type requires a
square-root range inclusion. Proposition5.4 assumes nonnegative diagonals
and contraction factorization; its proof constructs the contraction
from square roots, and conversely factors the block through a positive
contraction block. Theorem6.1 also requires a nonnegative Schur remainder;
its reverse proof bounds the square-root inverse action by the other
diagonal to obtain the contraction. These are form-level criteria, not
a source of the independent complement sign.

[Dritschel–Rovnyak, arXiv0903.3639v1,21March2009](https://arxiv.org/pdf/0903.3639v1),
LemmaA.1 printed pp28-29 and its complete proof were reopened.
It concerns a bounded Hilbert-space block and a closed subspace.
Nonnegative diagonals and a contraction between their square roots
characterize positivity. The forward factorization and converse
positive-square-root/partial-isometry construction were inspected.
It supplies neither raw-unbounded-diagonal applicability nor the fixed
quarter constant. LemmaA.2 already assumes positivity.

Reuse the inspected inverse-order/closed-form proof cases and exact
versions in561 and562's separate approval563: Behrndt et al.
Proposition2.1, Theorem3.4's nonnegative case and Corollary3.5;
Teschl Theorems2.13/2.18. Reuse Li paper45 displayed v2 Sections4-5,
(4.4)-(5.5) only as method coverage. These sources were not reopened
this turn. No source constants, numerical certificate or complementary
sign are imported. No reproof is warranted. Full matching Mathlib
coverage remains unchecked.

### Scope comparison and retained failures

Read C999m's hypotheses and Sections12/17's stated combination interfaces,
including(46),(72)-(73), solely to compare source scope, without auditing
their validity. The new finite-map connection uses the already assessed
explicit-entry/dot-product method. An essential new FFT accuracy theorem
would fall outside this approval. Histories574/575 explicitly retain
full inverse-output and direct-action error obligations and deny that
saved-array agreement proves accuracy. Reuse561's specific scalar,
derivative, response-prefix and automatic-factorization failure comparison;
none globally bans a signed mixed-map audit. No broad rediscovery search
or novelty claim is needed for this unchanged target.

The next mathematical step must inspect the complete relevant proof and
certificate evidence for Sections12-17, with Sections1-11's audited
interfaces and C744v/w/z, C999j/k/l contracts retained. In particular,
verify directional covariance versus norm addition, disjoint input
columns versus shared low corrections, exact/proxy cancellation,
adjoint orientation and all finite-error/tail charges. Hashes and flags
alone cannot discharge these obligations. Passing means a sound local
mixed-quarter estimate under its explicit contracts. An unpaid term,
invalid domain specialization or unjustified covariance inference defeats
the claimed comparison until repaired; it is not an off-line zeta zero.
The independent complement lower bound, whole-core/c_*, C744q, H2,
non-neutral coverage and global transfer remain open. This essential
audit remains the next target; no justified creative mechanism is
manufactured to meet a scheduling preference.
