# Moving-cutoff aggregation — completed scope comparison

TARGET: Assess whether the density, shell and fourth-moment inputs extend L483's aggregate bound to delta(T)=100 log log T/log T at the threshold B_{>=delta(T)}(T)=o(T(log T)^3).
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: New uniform-near-line density and weighted-kernel/Laguerre searches, plus the fixed-sector comparison and narrowly relevant failures, found no inspected direct theorem for this B sum; details in drafts/2026-10-29-moving-cutoff-source-review-notes.md. No novelty claim.
SOURCE_EVIDENCE: Chourasiya--Simonic arXiv:2507.15184v1 Corollary 1/(3), Table 1, Section 2.1 proof (10)--(11) and Section 4 closing perturbation https://arxiv.org/html/2507.15184v1; Bui--Hall v1 Theorem 3/Section 7 https://arxiv.org/html/2304.05178v1; reused Bellotti--Wong v2 Theorem 1.1 coverage https://arxiv.org/pdf/2412.15470v2 through L467. Exact ranges and retained import qualifications are in the source notes.
COMPARISON: The density corollary is uniform on a closed interval reaching 1/2, including its theorem's omitted near-line strip; the fixed-order continuous fourth moment and unit shells have no cutoff parameter. L483 displays kernel losses before fixing delta. These inputs cover an attempt, not its weighted conclusion.
GAP: Derive the complete aggregate bound for the height-dependent restriction and test coefficient 100 against all kernel losses, additive density remainders and padded-height factors. No moving-sector saving or optimal cutoff is proved.
REASON: The saved target changes sigma with height; inspected near-line proof cases resolve essential source coverage without deriving a new estimate. Nominate only this known-tool specialization for separate next-turn approval.
LITERATURE_REASON: The previous fixed-cutoff scope excluded a cutoff tending to zero; checking the density theorem's uniform near-line cases and explicit kernel parameter losses was essential before dependent mathematics.
SCOPE: Exact L471 B sum restricted by delta(T)=100 log log T/log T<=d_j<1/2, for sufficiently large real T with 0<delta(T)<=1/8; retain full multiplicities, one-copy quotients, coincident ordinates, clipped windows, endpoints and padded height 3T. No external half-plane premise or selected-amplitude hypothesis.
COVERED_TARGET: Test L483's aggregate-kernel bound at delta(T)=100 log log T/log T, retaining all density remainder terms, against B_{>=delta(T)}(T)=o(T(log T)^3).

The literature-only review is complete. Evidence is in
`drafts/2026-10-29-moving-cutoff-source-review-notes.md`. Source readiness
for the listed COVERED_TARGET is nominated; the supervisor's separate
next-turn approval precedes execution. No moving-cutoff estimate has
been derived or approved as a mathematical result.

Inputs: L018, L467, L471, L483 and the precise cited density and fourth
moment statements. Retain full m_j, one-copy F_j, clipped endpoints,
coincident ordinates and padded cumulative height 3T. Restrict to
sufficiently large real T so the cutoff is positive and at most 1/8,
inside the density theorem's uniform interval. No RH, spacing,
simplicity, external half-plane premise or selected amplitude bound
may enter. Full matching Mathlib coverage is unchecked. L483's separate
critical audit is still pending; none is silently claimed here.

A successful extension could narrow the uncontrolled sector toward the
critical scale, while still leaving smaller displacements, full negative
mass, all-height signs and higher positivity open. Continue only if the
complete later comparison proves the stated little-o; otherwise record
its loss or missing hypothesis and park this implementation. This is
known-tool development, not a prepared creative cancellation mechanism.
The historical procedural stop, L471's separate-pair loss, L475's
global-disk cost and the selected-energy gap are preserved and compared
in the source notes. No mathematical script or new lemma belongs to
this literature step.
