# Coefficient interval below 1/log(6) — scope reviewed

TARGET: Determine whether audited L028's guarded root selection excludes smaller positive residue-20 companions with both shortcut clocks at most C log(n)+B for every fixed 0<C<1/log(6) and B>=0, on unbounded roots n in 47 modulo 243.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Three changed-coefficient/exact-cylinder/coalescence queries found no matching inspected external theorem; reused earlier logarithmic and endpoint searches, without a novelty inference. Queries and discovery-only hits are recorded below.
SOURCE_EVIDENCE: Read complete canonical L028 proof and critical audit, L027 hypotheses and representative-selection passage, Attempt 016 and endpoint-audit records; reused inspected Rozier (2019) Definition 1/Lemma 1 and proof, pp. 2–3, named CRT, and Sodelin/LaDue comparisons in the ready logarithmic and endpoint assessments.
COMPARISON: L028 proves guarded exclusion through L for roots above 4^L and selects roots below 163*6^L; its stated clock conclusion is only 1/log(12). L027 supplies a strict-slack comparison at a different exponential height. The larger strict interval is not a recorded theorem, but its essential arithmetic coverage is ready.
GAP: A separate research turn must justify the arbitrary-real-C,B horizon comparison using L028's existing selection, with integer clocks and unbounded roots; no new anchor proof or small-representative distribution assertion is required. The endpoint 1/log(6) and universal descent remain unresolved.
REASON: Approve one short quantitative specialization of the audited height envelope. This review establishes coverage and overlap only, not the extended clock theorem or certified originality.
SCOPE: Exactly TARGET using L028's proved guarded horizon exclusion and selected roots, L>=6, fixed real C,B, natural logarithms, positive residue-20 companions strictly below the original root, both actual shortcut paths and both zero clocks. Endpoint equality, new congruences, improved heights and distribution forcing are outside scope.
LITERATURE_REASON: The coefficient range exceeds the earlier explicitly covered 1/log(12) range; this separate review compares the changed hypothesis before mathematics and reuses adequate primary coverage.

## Main gap, use and discriminating test

Universal eventual descent remains the main gap. A smaller residue-20
companion coalescing with an original root could transfer convergence to
that root. A stronger obstruction to short clocks would limit such
least-root certificate routes. Neither a cover nor convergence of any
selected root is assumed. Other cylinders, longer clocks and a universal
terminating mechanism remain independent gaps.

The intermediate target is exactly TARGET. Approve a subsequent research
attempt to compare C log(n_L)+B with L for all sufficiently large integer
L, for each fixed pair of real parameters in the stated range. Use the
existing roots rather than retuning the CRT class. Seek an explicit
justified threshold or a complete limiting argument, keeping all guards.
Continue if the upper height permits both clocks to fit the proved
horizon and the lower height still guarantees unboundedness. Otherwise
stop this specialization and identify the failed comparison. Samples
and fixed rational examples cannot settle the real-parameter claim.
No such comparison or extended conclusion is derived in this turn.

## Local theorem and duplicate/failure comparison

L028, section “Reduced slopes give the smaller size guard” through
“Controlled CRT selection and the endpoint clock”, proves exclusion
through horizon L under n>4^L, L>=6, n=47 modulo 3^(L+4), and
81n+97=0 modulo 2^(L+1). Its selected roots satisfy
4^L<n_L<163*6^L, are odd, lie in 47 modulo 243 and have
v_2(n_L+1)=4. These are existing proved statements, including the
guarded horizon result within its proof, not new deductions here.
The complete audit retains actual paths, signed-anchor qualifications,
offsets, slope equality, both zero clocks and strict original-root order.

The essential local input is L028. L026's anchor argument and L025's
offset estimate enter through that audited theorem. Do not apply L026's
statement with n>4^L in place of its n>12^L hypothesis or repeat its
anchor proof. A later canonical specialization must cite L028's guarded
proof passage explicitly rather than silently claiming the extended
clock conclusion is already its statement.

L027 proves the narrower coefficient range below 1/log(12); L028 states
that range's endpoint. Attempt 016 preserves those exact stops and does
not ban larger coefficients. The overlap for smaller coefficients is
known coverage, not a new discovery. The unrecorded larger interval
requires only the proposed horizon specialization, subject to proof.

Attempt 020 and the small-CRT assessment target the endpoint 1/log(6)
using a smaller representative assertion for every B. L032's unresolved
zero-run property supplies no selection theorem. The present strict
coefficient target does not assume that property, equidistribution or
any newly small representative. Preserve that stop and finite evidence.
The endpoint remains outside scope.

## Reused primary coverage and new bounded search

Reuse `2026-10-05-residue47-log-height-coalescence.md` and
`2026-10-05-residue47-endpoint-log-coalescence.md`, whose hypotheses,
relevant proof cases and inspected/unread distinctions were checked.
No changed parity or CRT assumption is introduced; unchanged external
passages were not fetched again.

Olivier Rozier, *Parity Sequences of the 3x+1 Map on the 2-adic Integers
and Euclidean Embedding*, INTEGERS 19 (2019), A8,
[Definition 1, Lemma 1 and proof, pp. 2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2),
provides finite parity coding, including the signed-anchor domain used
inside L028. The named Chinese Remainder Theorem supplies the existing
coprime-modulus class. Neither requires reproof or a new application in
the proposed clock comparison. L028's quantitative envelope is the
local audited input; published parity coding alone is not a time bound.

The reused assessments compare Sodelin's informal live-main
[B-S20-ANCESTOR-DEPTH-OBSTRUCTION-001](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/lemmas/Bounded_Ancestor_Depth_Obstruction.md),
read 2026-10-05, statement and relevant proof/scope lines 8–74:
bounded ancestors are obstructed but general coalescence is left open.
They also inspect Mark D. LaDue,
[arXiv:1709.02979v3](https://arxiv.org/pdf/1709.02979v3#page=3),
2017-11-15, Lemma 3.1 and Theorems 3.2/4.1, pp. 3–5, both actual
parity cases. Its specified adjacent companion and initial-run clock
do not give the required smaller residue-20 companion assertion.
These are comparisons, not imported matching theorems. Laurent's
optional separation theorem and the inaccessible adjacent-pair manuscript
remain unnecessary to this already guarded specialization.

Executed changed-scope queries:

- `Collatz coalescence "log(6)"`
- `Collatz "coalescence" "47" "243"`
- `Collatz logarithmic coalescence smaller ancestor lower bound`

Returned OEIS constants, stochastic coalescence, average stopping-time
and claimed block-growth leads were discovery-only hits; no theorem
text from them was inspected or used. The Sodelin refined-ancestor hit
concerns different valuation certificates already compared locally.
No matching conclusion was established by these queries; failed searches
establish neither absence nor novelty. The source target was rechecked
on 2026-10-06 in the reused small-CRT assessment: every positive integer
reaches 1 under the original map. No cross-notebook theorem was read
and no essential source is blocked.

## Qualifications and completion

Full Mathlib coverage for this coefficient interval and supporting real
logarithm comparisons is **not checked**. Unknown coverage is not absence;
no Lean check or formal verification is claimed.

Completed work is LITERATURE/NOVELTY_UNCHECKED, outcome EXPLORATION:
changed-scope coverage is ready, without a mathematical advance or derived
clock bound. No lemma, mathematical script, certificate, overview argument
or DAG row was changed. The next turn defaults to the approved mathematical
specialization; no calculation-budget reset is claimed.
