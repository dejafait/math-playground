# Last-pair allocations in arbitrary cyclic order — source approval

TARGET: Test whether the endpoint/domain/J subsystem admits any cyclic ordering of L068's intact triples for an integer 2<=t<=9250245.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Six focused queries on Collatz block permutations, exact counts and constrained affine ordering; scoped comparison of L063/L067/L068, ready October 12–13 assessments, Attempts 027–031 and histories 201/221; no inspected theorem decides this guard-feasibility target.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997) equations (2)–(4), Lemma 2 and induction pp. 228–229, Lemma 4 and complete exchange proof p. 230; reread Kubo–Makino–Sakamoto (ISAAC 2024) scalar objective and Theorems 1/3 pp. 44:2–44:4; reused assessed Kawase–Makino–Seimi and rational-log/remainder coverage.
COMPARISON: Formal affine formulas cover prescribed words; scalar ordering admits positive slopes below one but does not characterize simultaneous own-input guards. L063/L067 cover fixed tails at t=0/1; L068 monotonicity is literal-order only.
GAP: Arbitrary-order feasibility for t>=2 remains unproved; changed-tail uniform root/domain control and guard rejection, or a certified permuted rational survivor, remain to be established.
REASON: This separate comparison supplies adequate machinery for one bounded attempt on the unchanged TARGET; changed finite applicability or exact witness verification still requires mathematics, with no general coding reproof or guard-order theorem assumed.
SCOPE: L055 complete indexed J,H table with L068 integer 2<=t<=9250245 tails; intact cyclic orders normalized with row 24 last, all endpoints, s>=540/11 and every non-strict own-input J guard; no H/seed, minimum, integrality or primitive/count-ray premises.
LITERATURE_REASON: The saved target changes the order quantifier and permits two varying tails; essential applicability was outside ready fixed-tail assessments and required this separate comparison.

## Proposal retained from step 221

The following paragraphs describe the proposal before approval. Their pending coverage statements are superseded by the separate comparison below.

The main gap is universal eventual descent. The proposed intermediate
target tests the order restriction left by the audited literal-family
exclusion. An exclusion would remove a larger family of possible actual
closed concatenations; a certified rational survivor would stop this
necessary-subsystem exclusion and identify the need for additional
arithmetic or guards. Neither outcome settles entry, other allocations,
unrestricted cycles, divergence or eventual descent.

Use L055's complete J,H table and L068's tails a_23=2+18t,
a_24=166504412-18t, other tails 2. Permute intact triples, keeping each
tail with its J,H pair and each outgoing triple with its own input.
Normalize cyclic order by putting row 24 last; do not assume that its
tail is the largest or its successor is a minimum. Require real shifted
junctions s>=540/11, every exact cyclic endpoint of C068a (1), and
every non-strict own-input J guard of C068a (2). Do not add H/seed,
minimum, integer-realization, primitive-count or count-ray premises.

Essential inputs for the later comparison are L055's indexed table,
L068's parameterization and literal classification, and the order-bound
arguments in L063 and L067. C068b supplies the audited actual-word
necessity bridge, not an arbitrary-order conclusion. The unchanged
counts do not justify carrying over a root bound or first-displacement
estimate: two tails vary, and a previously growing row may contract.
These are unresolved applicability questions, not premises.

The later attempt's discriminating test is either a uniform rigorous
guard rejection for every normalized order throughout 2<=t<=9250245,
or one exact rational cyclic tuple with certified domain and all own-input
J guards for a specified t and order. A finite unsuccessful search is
not exclusion; an unverified numerical survivor is not feasibility.
Preserve Attempts 027–031: modular cancellation does not supply real
guards, while one order's guard failure does not exclude all others.
Do not resume the stopped prime diagnostics under a different name.

No new mathematics, script, source retrieval, assessment approval or
claim of novelty was produced for this proposed continuation. Full
matching Mathlib coverage remains unchecked. The next invocation must
be literature-only because this target changes the assessed order scope.

## Separate literature comparison — step 222, 2026-10-14

The main gap remains universal eventual descent. The intermediate target
asks whether order rescues L068's rejected literal allocations. Exclusion
could later be transferred to a larger restricted actual-word family using
C068b's audited necessity bridge. A rational survivor would stop exclusion
by this necessary subsystem and identify a need for independent arithmetic
or additional guards. Entry, other allocations, unrestricted cycles,
divergence and eventual descent would remain unresolved in either case.

### Local hypotheses, duplicates and failures

Read L055's complete table/counts and exact construction, L051 hypotheses
(1)–(4), L063's proof through first-displacement coverage, L067's uniform
root and unchanged-prefix arguments, and L068's hypotheses, construction,
domain and literal boundary test. Reuse audited qualifications from the
ready October 12–13 assessments and history 201. Foundations 01 records
the exact universal statement and shortcut convention; the ready source
assessments checked the target, which this review leaves unchanged.

L063 assumes first-24 tails all 2. L067's multiplier check treats only
row 23's tail 20 and row 24's tail 166504394. Both justify growth of
every first-24 multiplier before bounding the cyclic root. Neither theorem
applies over the new interval without new justification. L068's parameter
dependence uses literal prefixes and row 23 immediately before row 24;
its decreasing row-24 margin is not an arbitrary-order result. No new
contraction threshold, root bound, margin or witness is derived here.
L055's unchanged count-dependent Lambda enclosure is eligible; its
order-dependent root values are not.

The scoped search in October 14 family assessments and histories 210–221
found literal-family results and this proposal, not a completed all-order
interval verdict. The t=0/1 cases overlap L063/L067 and their assemblies
and are outside this test. Attempts 027–030 stop prime diagnostics;
Attempt 031 rejects one fixed old-allocation order by its own guard.
None decides this interval. Preserve these stops, both rational witnesses
and unfinished work; do not restart the stopped prime diagnostics.

### Primary sources and applicability

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arith. 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[published PDF](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
equations (2)–(4), Lemma 2, pp. 228–229: a nonempty binary word of
length N with K ones has phi_w(x)=(3^K x+varphi(w))/2^N and root
varphi(w)/(2^N-3^K). Read the length-one/appended-zero induction;
appended one is stated analogous. The finite formal words and unchanged
positive Lambda meet the nonzero-denominator requirement. Reuse L055/L068's
coordinate match without integer realization. Lemma 4, p. 230, requires
distinct equal-length/equal-one-count words and domination of every prefix
one count, and reverses numerator order. Read its complete bit-exchange
proof. Equal totals supply neither that premise nor simultaneous guard
feasibility. Reuse the earlier Lemma 5/Corollary 1 rotation comparison
without applying it.

Kubo–Makino–Sakamoto, *Composition Orderings for Linear Functions and
Matrix Multiplication Orderings*, ISAAC 2024, 44:1–44:14,
DOI 10.4230/LIPIcs.ISAAC.2024.44,
[published version](https://drops.dagstuhl.de/storage/00lipics/lipics-vol322-isaac2024/LIPIcs.ISAAC.2024.44/LIPIcs.ISAAC.2024.44.pdf):
reread the prescribed-real-input scalar objective (44:2), Theorem 1's
three cases/vector-angle definitions (44:3), and Theorem 3's adjacent-
interval neighborhood/local-global criterion (44:4). Increasing affine
means positive slope, including slopes below one; contraction does not
mean a decreasing function. These optimize the final composition, not
all intermediate guards at a cyclic root. Reuse the earlier reading of
proof cases (i)/(ii), 44:8–44:9. The published (iii) proof is omitted;
full version arXiv:2402.10451 remains unread and nonessential because
no extremizer algorithm or local/global theorem is imported. This is
scope comparison, not a parameter-specific theorem application.

Reuse [the October 12 assessment](2026-10-12-fixed-allocation-j-guard-order-rigidity.md)
for Kawase–Makino–Seimi, arXiv:1601.05480v1, Theorem 1, Definition 7,
Lemmas 9/10/14(b) and inspected exchange cases, and NIST DLMF 4.6.4
with L055's certified finite logarithm remainder bounds. No general
affine-composition, coding or logarithm theorem needs reproof. Only this
family's changed finite bounds/applicability or exact witness verification
need mathematical work. Full matching Mathlib coverage and external Lean
builds remain unchecked; supporting logarithm results do not prove TARGET.

### Discovery and approved bounded attempt

Queries actually run:

- `Collatz rational cycles block permutation halving exponents ordering affine fixed point constraints`
- `affine composition ordering cyclic fixed point intermediate constraints slopes contracting expanding`
- `"composition ordering" "constraints" "linear functions"`
- `"Collatz" "cyclic" "permutation" "Halbeisen"`
- `"Collatz" "397573379" "630138897"`
- `"affine" "composition ordering" "fixed point"`

Relevant hits returned already assessed scalar ordering papers. Exact-count
hits were cycle-count tables and speculative preprints, not inspected
matching theorems. Forums, secondary cycle descriptions and unrelated
permutation problems are not theorem inputs. Failed searches establish no
novelty. No essential source is blocked; the unread full-version lead
above is not required for the proposed finite test.

SPECIALIZE approves one bounded mathematical attempt on exactly TARGET.
Essential inputs are L055's full indexed table and audited count/log
enclosures, L051's endpoint/J formulas, L068's tails/literal classification,
and L063/L067's order-bound methods with their explicit hypothesis limits.
C068b is a possible downstream necessity bridge, not an arbitrary-order
premise. No cross-notebook input is required.

Seek either uniform rigorous guard rejection for every normalized order
throughout the integer interval, or one specified t/order with exact
rational closure, all 25 domain conditions and all 25 own-input J guards
certified. Keep tails with their J,H rows and outgoing rows with their
own inputs, including closure. Row 24 last is normalization, not an
assumption that its tail is largest or its successor is a minimum. Any
domain/minimum/growth claim must be justified before use. Do not add
H/seed, integer/parity/exact-valuation, primitive or count-ray premises.

Continue an exclusion comparison only with justified uniform bounds and
strict rejection margins covering every required case. Abandon that
sufficient comparison if an essential bound fails or a required margin is
nonpositive/inconclusive; this alone decides no feasibility. A certified
survivor stops exclusion of the whole subsystem. Finite search failure
is not exclusion; a numerical preview is not a witness. Save unfinished
reasoning and actual failed thresholds. New essential inputs or mechanisms
outside this scope require separate coverage, and completed results require
later critical audit.

Completed LITERATURE/NOVELTY_UNCHECKED, outcome EXPLORATION: new scope
comparison and ready coverage, not a mathematical verdict or advance
beyond checked sources. No lemma or mathematical script was changed or
run. The mathematical exploration count remains one since step 219.
