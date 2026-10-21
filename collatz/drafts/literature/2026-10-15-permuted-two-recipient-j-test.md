# Two-recipient all-order endpoint/J test: source assessment

TARGET: Test whether the endpoint/domain/J subsystem admits any cyclic order of the two-recipient triples for an integer 1<=t<=9250244.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Focused web queries on cyclic affine block permutation/intermediate constraints and the changed-tail constant; reused the October 12–14 ordering searches and inspected the two-recipient literal assessment. No inspected theorem answers this changed-support all-order target.
SOURCE_EVIDENCE: Reused inspected Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemma 2 and induction pp. 228–229, Lemma 4 exchange proof p. 230; Kubo–Makino–Sakamoto (ISAAC 2024), Theorems 1/3 pp. 44:3–44:4 and inspected proof cases pp. 44:8–44:9; Kawase–Makino–Seimi arXiv:1601.05480v1 listed ordering cases and DLMF 4.6.4 as recorded in ready assessments. No primary proof was newly reopened.
COMPARISON: Audited L070 supplies literal infeasibility; L069 supplies an all-order method with a different row-22 tail. Formal affine composition applies, but scalar ordering theorems and those local conclusions do not imply this all-order guard verdict.
GAP: Prove changed-support order-uniform minimum/root control and all needed first-displacement rejections, or verify an exact feasible tuple; no new bound or verdict is established in this review.
REASON: Changed row-22 support required separate comparison; adequate primary machinery and local exact-log coverage permit one later bounded RESEARCH/REPRODUCTION attempt without general coding reproof.
SCOPE: Exactly TARGET with L055's 25 indexed pairs, all endpoints including closure, lower domain s>=540/11 and outgoing own-input non-strict J guards; no H/seed, growth, minimum-location, integrality or primitive/count-ray premise.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes the support outside the ready all-order last-pair assessment; the new comparison is essential, despite the recent literature balance.

## Gap, target and scope

Universal eventual descent remains the main gap. The intermediate test
concerns the 25 intact triples with a_22=20, a_23=2+18t,
a_24=166504394-18t, a_i=2 for i<22, and integer
1<=t<=9250244. Use L051's exact shifted endpoint and J-guard conventions
as displayed in L070, now in every cyclic order, keeping each outgoing
triple paired with its own input. Repeated periods and coincident
junctions are allowed. Both varying tails must be retained, including
the endpoint a_24=2. No changed-tail row is assumed to grow.

A uniform necessary-subsystem exclusion could broaden the restricted
allocation exclusion and later support a separately assessed L041
actual-word application. A verified feasible tuple would instead stop
uniform exclusion by this subsystem. Other allocations, entry,
unrestricted cycles, divergence and universal descent stay unresolved.

## Primary inputs and limitations

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239, DOI
10.4064/aa-78-3-227-239, [published PDF](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
section 2 equations (2)–(4), Lemma 2, pp. 228–229, supplies formal
chronological affine composition and its fixed point for a nonempty
binary word with nonzero denominator. Reuse the length-one and appended-zero
induction and stated analogous appended-one case inspected in the ready
[all-order assessment](2026-10-14-last-pair-permuted-j-feasibility.md).
L070 already records unchanged K,N and positive Lambda for this allocation;
permutation preserves totals. Thus the nonzero-denominator hypothesis is
covered. Coordinate matching for changed chronological orders still must
be justified; no integer or parity realization is imported. Lemma 4,
p. 230, additionally needs every-prefix domination to compare numerators;
equal totals alone do not give its premise or simultaneous guards.

Kubo–Makino–Sakamoto, *Composition Orderings for Linear Functions and Matrix
Multiplication Orderings*, ISAAC 2024, 44:1–44:14, DOI
10.4230/LIPIcs.ISAAC.2024.44, [published paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol322-isaac2024/LIPIcs.ISAAC.2024.44/LIPIcs.ISAAC.2024.44.pdf),
Theorems 1/3, pp. 44:3–44:4, optimize a scalar composition at a prescribed
real input. Reuse the inspected increasing-affine definitions and cases
(i)/(ii), pp. 44:8–44:9. They do not characterize all intermediate
own-input inequalities at a cyclic root. The omitted case-(iii) proof
and full arXiv version remain unread and nonessential: no optimizer or
local/global equivalence is imported. Positive slopes may contract;
contraction does not make an affine function decreasing.

Reuse Kawase–Makino–Seimi, arXiv:1601.05480v1, Theorem 1 p. 3,
Definition 7/Lemmas 9/10 pp. 6–7, Lemma 14(b) pp. 7–8 and its proof
p. 16, under the [October 12 assessment](2026-10-12-fixed-allocation-j-guard-order-rigidity.md).
Those prescribed-input scalar objectives likewise supply no guard verdict.
Reuse [DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4), positive-real domain,
and L055/L064's audited rational remainder and outward-rounding method.
General composition or logarithm results need no reproof. Full matching
Mathlib coverage is unchecked; no absence or Lean build is claimed.

## Local duplicates, failures and new obligations

Read L055's full indexed table, L070's exact scope/count passage and
L069's full minimum, rotation, first-displacement and literal-rejection
argument. L070 settles literal order only. L069 and its ready assessment
keep a_22=2, so its theorem is inapplicable unchanged. In particular its
claim that every preceding literal tail is 2 must be revisited when
position 23 is the first displacement: row 22 can now occur in that
prefix with tail 20. No replacement offset sign, margin or root bound
is derived here. The complete changed-support prefixes, closing edge,
positive domains and uniformity in t must be justified before using
any retained numerical comparison. L063's finite margins are eligible
only after matching their expressions, not by importing its rigidity theorem.

L055's count-dependent bounds can be reused; its literal root heights
cannot be transferred to arbitrary orders. L069's product/minimum method
is a candidate technique, not already proved for the new scope.
Attempts 026 and 031 were read: one preserves a real witness in a
specified older allocation, the other rejects one older permuted tuple.
Neither decides this target or bans this independent test. L070/C070a
and the local two-recipient histories supply no all-order duplicate.
All existing work and stops remain preserved; no cross-notebook input.

## Discovery and decision

Queries actually run in step 238:

- `Collatz rational cycles block permutation affine cyclic fixed point intermediate constraints halving exponents`
- `"Collatz" "166504394" "order"`
- `"Composition Orderings for Linear Functions" "fixed" constraints`
- `"Collatz" "permutation" "Halbeisen" "cycles"`

The exact-constant query gave no matching theorem. Other hits returned
already assessed primary affine/ordering papers and unreviewed repositories
or speculative claims, which were not used as mathematical evidence.
The 2022 3n+c generalization and arXiv:2101.04067 remain unread leads;
no theorem about this own-input guard system was inspected there.
No novelty follows from the search. No essential source is blocked.
Rechecked MathPrize's page dated 2021-07-07: the universal positive-integer
reaching-1 target remains as recorded in foundations; prize conditions
are separate. No foundation or argument change is needed.

One later SPECIALIZE/REPRODUCTION attempt may test exactly TARGET.
Essential inputs: L051 conventions, L055 full table/count/log bounds,
L069's all-order method and audited L070 literal exclusion; L063 only
if its finite comparison expressions are actually reused. Establish
uniform control before logarithms and account for every eligible first
displacement, every t and all cyclic cuts. Continue toward exclusion only
if all necessary sufficient comparisons are strict with the correct
non-strict guard sign. If a sufficient bound fails or a margin is
nonpositive/inconclusive, stop that comparison without inferring feasibility;
a verified feasible tuple stops uniform J-only exclusion. No broader
allocation or new mechanism is approved. This literature turn computed
no new bounds and made no lemma or mathematical-script changes.
