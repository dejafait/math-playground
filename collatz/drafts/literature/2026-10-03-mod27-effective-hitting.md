# Effective hitting time outside one residue class: literature assessment

TARGET: Determine whether the modulo-27 graph avoiding residue 20 yields explicit A>0, B>=0 and M>=2 such that every positive start n reaches 20 modulo 27 or {1,...,M} within ceil(A log(n)+B) shortcut steps, retaining the positive additive term.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The 2026-10-03 bounded screen covered exact modulo-27 hitting-time statements, quantitative sufficient sets, finite-path estimates and arithmetic loops; it found a directly relevant public reconstruction but no inspected statement of the requested explicit logarithmic constants; queries and scope are recorded below.
SOURCE_EVIDENCE: Read Monks et al., arXiv:1204.3904v2, section 6.1, Theorem 6.4 with proof and Proposition 6.5(a) with proof, pp. 17–18 and 22–25, https://arxiv.org/pdf/1204.3904v2; Sodelin's Sufficiency_Rank_Audit_2026-09-05.md, section 2, https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/sources/Sufficiency_Rank_Audit_2026-09-05.md; its checker, lines 14–67, https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/verification/mod27_rank_check.py; Rozier (2019), Lemma 1 with proof, pp. 2–3, https://math.colgate.edu/~integers/t8/t8.pdf.
COMPARISON: Known qualitative visitation and a concrete public certificate support this target; uniform time constants and phase-entry height estimates remain unstated in the inspected sources. Source comparison contradicts the preliminary assumption that residue 26 is visited at most once.
GAP: Check the sourced certificate and obtain explicit A,B,M for all positive starts, controlling the initial multiples-of-3 segment, the residue-26 arithmetic loop, and the positive affine offsets; no local quantitative bound is established.
REASON: Specialize the inspected stopping mechanism to quantitative time control, and independently check its certificate because the published transient argument needs qualification. No essential source is unread; the full target is ready for a mathematical attempt, without a novelty claim.
SCOPE: Positive integer shortcut orbits and verification or quantitative specialization of the sourced modular phase rank; no target-to-target descent, infinite graph-path realizability, or unexamined cycle theorem is assumed.
COVERED_TARGET: Verify the sourced modulo-27 phase rank on every positive shortcut step outside {1,2} and residue 20, retaining the +1 term and residue-26 valuation.
COVERED_TARGET: Extract explicit logarithmic stopping-time constants from the checked modulo-27 phase rank, controlling phase-entry heights and all arithmetic exit steps.

## Hypotheses

Use the shortcut map T in foundations/01-target-and-scope.md, on every
positive integer n. Let S be the positive integers congruent to 20
modulo 27. A, B, and the integer M must be independent of n. Time zero
is allowed for n already in S or the finite base set. The proposed bound
concerns the first visit to their union, not a strict decrease on every
step or at the first return to S.

An eventual transition to the graph on integers prime to 3 may be used
only with quantitative control of the preceding segment. Graph edges
describe possible integer steps, and a projected path must not be
mistaken for an actual positive orbit. The +1 in the odd shortcut rule
must remain in every finite-path height estimate.

## Conclusion

The target remains proposed, not proved. The source review is complete
enough for SPECIALIZE: a concrete existing certificate and the remaining
finite-time work are identified. This literature-only turn establishes
no constants, lemma, or complete Collatz candidate.

## Proof

This section records inspected statements and the discriminating test;
it is not a proof of the proposed bound. The pending recovery proposal
is preserved in the target and hypotheses. Its graph-only treatment of
transient states is qualified below.

### Inspected primary statements

Monks, Monks, Monks and Monks, *Strongly sufficient sets and the
distribution of arithmetic sequences in the 3x+1 graph*,
[arXiv:1204.3904v2](https://arxiv.org/pdf/1204.3904v2), uses our shortcut
map. Section 6.1 defines the residue graphs. Theorem 6.4, pp. 22–23,
states that divergent positive orbits and nontrivial positive cycles
meet S. Its proof removes several residues before bounding red-edge
frequency by one half. Proposition 6.5(a), pp. 23–25, gives a
simple-cycle criterion for forward sufficiency, with a closed-walk
decomposition argument. These supply qualitative support, not the
requested time constants.

There is a source qualification: p. 22 treats residue 26 as occurring
at most once. The public audit below reports a repeated-residue witness.
Its removal therefore needs arithmetic control. This concerns the
displayed argument, not a disproof of the hitting theorem.

The [version record](https://arxiv.org/abs/1204.3904v2) identifies v2 as
2012-04-20; the retrieved PDF title page says November 27, 2024. Retain
that discrepancy and versioned URL. Pages above use printed numbers.
No correction notice was located in the bounded screen.

Olivier Rozier, *Parity Sequences of the 3x+1 Map on the 2-adic Integers
and Euclidean Embedding*, INTEGERS 19 (2019), A8,
[Lemma 1 and proof, pp. 2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2),
provides the standard finite-parity congruence and affine iterate formula,
including its additive term. This confirms the adequate coverage in the
[September 26 assessment](2026-09-26-current-target.md). It supplies
finite-word arithmetic, not the requested avoidance bound. Checking the
original one-step rules directly is sufficient for the proposed
certificate; rederiving the general identity would be redundant.

### Directly relevant public reconstruction

Sodelin's [*Two exact theorem imports and a ranked reconstruction*,
section 2](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/sources/Sufficiency_Rank_Audit_2026-09-05.md)
proposes a stopped rank with core weights (16,28,49), contraction
20/21, an initial multiples-of-3 phase, and a v_2(n+1) phase for
residue 26 followed by residue 13. Its stopping set is S union {1,2}.
It reports 53 to 80 as a repeated-residue witness and arbitrary loop
lengths from 27*2^e-1. These are cited observations, not new calculations
here. The note explicitly leaves subsequent target returns open.

This is an informal original certificate, not a verified local input.
Read section 2 in full and the relevant
[checker source, lines 14–67](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/verification/mod27_rank_check.py#L14).
The latter specifies the residue-height table, exact coefficient tests
retaining +1, and exit edges. Also inspected its finite regressions;
they cannot justify the universal claim. Neither artifact states the
desired A,B constants. Verification and quantitative extraction remain
future work; no source code was executed or copied into local scripts.

Provenance: both live `main` files were read on 2026-10-03. The note is
dated 2026-09-05 and declares input revision
`b6eee8594714adc3b51d5005dd0b4ed8a76412e8`; that is not a confirmed
revision of the note itself. Public commit lookup failed, and shell
retrieval was blocked by DNS. Browser-accessible bodies suffice for
this review; no immutable snapshot is claimed.

### Search record and coverage decision

Queries executed on 2026-10-03:

- `Collatz modulo 27 20 strongly sufficient effective hitting time logarithmic Monks`
- `Collatz directed graph sufficient arithmetic progression explicit bound hitting time parity cycles`
- `"Collatz" "20" "27" "hitting time"`
- `"Collatz" "20 modulo 27" bound`
- `"Collatz" "strongly sufficient" "finite" "bound"`
- `finite directed graph all cycles contract affine maps quantitative termination bound logarithm`
- `"Collatz" "20 mod 27" "bound"`
- `"Collatz" "logarithmic" "sufficient sets"`
- `"Collatz" "modulo 27" "log" "hitting"`
- `"Collatz" "20/21" "rank"`
- `"Monks" "26" "27" erratum`
- `"Collatz" "hitting time" "arithmetic progression"`
- `"Collatz" "logarithmic hitting" "27"`
- `"Collatz" "20 modulo 27" "time"`

The closest usable new hit was the public reconstruction above.
General termination hits concerned other systems or probabilistic
claims; no matching deterministic theorem was imported from them.
Stronger Collatz claims, unrelated residue-hitting statistics, and the
audit's separate Ansari sieve discussion are unread leads or outside
this target and are not assumed. Monks' asymptotic parity-frequency
references are not needed for direct phase-certificate verification.
No essential unread source forces SOURCE_BLOCKED. Provenance lookup
failure also does not block that explicit test.

This is a bounded screen, not evidence of originality. IMPORT would
overstate coverage of the exact bound. SPECIALIZE is appropriate because
a concrete stopping mechanism is specified and the remaining work is
to check its arithmetic and make its time control explicit. A successful
local core-rank proof would reproduce the source. Only the precise
finite-time difference may remain outside the statements checked, which
would still not certify novelty.

The [MathPrize target](https://mathprize.net/posts/collatz-conjecture/),
page dated 2021-07-07, was reread: every positive integer must reach 1
under the unshortened map. The research target and local shortcut
convention are unchanged.

### Continuation or abandonment test

Keep the exact saved target as the sole Next action. Its mathematical
attempt should check the sourced modular table and all-integer
coefficient inequalities, account for the multiples-of-3 prefix and
arithmetic exit phase, and bound each phase's length using its entry
height. Retain the positive additive term throughout. This prescribes a
test; it does not claim the certificate or extraction succeeds.

Continue if this yields explicit verified A>0, B>=0 and M>=2 independent
of n with the stated shortcut-time bound. A failed exact edge or an
uncontrolled phase transition is an informative obstruction to preserve.
Do not keep a graph-only proof that deletes the residue-26 loop or
silently treats it as a fixed-length transient. Abandon this certificate
if its checks fail without a specific repair; Collatz research continues.
No graph enumeration, constants, new path inequality, or new integer
witness was derived this turn.

The downstream use is a quantitative reduction of unrestricted forward
excursions to S and a finite base set. Convergence of the base set and
descent or another terminating mechanism for repeated visits to S would
still need proof. Hitting S is not universal eventual descent. The old
three-block theorem and depth-11 paired screen concern a different gap
and do not improve this target. Attempts 001/003 exclude time bounds
common to all starts; the proposed bound grows with n. Attempts
007/008 concern endpoint density and inverse uniqueness, neither of
which is assumed in this forward graph proposal.

Completed-step outcome: NEGATIVE. Source comparison changes the test by
exposing an arithmetic phase missing from the preliminary graph-only
reduction. It also identifies a sourced replacement to verify. This is
a literature finding, classified NOVELTY_UNCHECKED, not a newly proved
mathematical result or a repeated stop review. Mathematical exploration
usage is unchanged. No complete candidate appeared and no scheduler
counter was reset.

## Mathlib

Full effective hitting-time target: **not checked**. Supporting finite
directed-graph, cycle, affine-map, and logarithm results: **not checked**.
The source link above is a mathematical citation, not library coverage.
