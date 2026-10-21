# Fixed allocation: proposed J-guard order rigidity

TARGET: Determine whether L055's literal order is the only permutation of its first 24 intact triples, with row 24 fixed last, satisfying every J guard and all cyclic endpoints of L051.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Seven focused queries on Collatz block/exponent ordering, prefix dominance, exact counts and affine composition optimization; narrow duplicate/failure comparison in the fixed-allocation assessments, Attempts 027–031 and histories 174–177; no inspected theorem supplies this guard-rigidity verdict.
SOURCE_EVIDENCE: Reused assessed affine/logarithm coverage; reopened Halbeisen–Hungerbuehler (1997) Lemmas 1/2 pp. 228–229 and Lemmas 3/4/5/Corollary 1 pp. 229–231 with relevant proof cases; inspected Kawase–Makino–Seimi arXiv:1601.05480v1 Theorem 1, Definition 7, Lemmas 9/10/14(b), pp. 3, 6–8, 16, and their relevant exchange proofs; rechecked NIST DLMF 4.6.4 and its domain.
COMPARISON: Known affine formulas cover every prescribed nonempty word, while prefix-dominance and composition-ordering results optimize scalar quantities and do not characterize feasibility of all own-index J guards; L055 and L062 leave all-order uniqueness open.
GAP: The finite specialization still needs justified order-uniform cyclic-root bounds and a strict first-displaced-row guard comparison for every eligible row and prefix; these have not been derived or calculated in this turn.
REASON: This separate literature-only scope comparison approves one mathematical attempt on the unchanged TARGET using assessed affine/logarithm machinery; no new all-order theorem is assumed or proved.
SCOPE: Use exactly L055's intact indexed triples, K=397573379, N=630138897, tails 2 on rows 0–23 and 166504412 on row 24; permute only the first 24 triples, retain each outgoing triple's own junction, s_i>=540/11, all 25 exact L051 (4) endpoints with cyclic closure, and every non-strict J guard in L051 (3).
LITERATURE_REASON: All-order rigidity was outside the ready single-order assessment; compare its changed quantifier and essential ordering hypotheses once before mathematical work.

The main gap remains universal eventual descent. This proposed intermediate
target asks about order rigidity for one fixed allocation only. If the
literal order is forced, L056's recorded nonintegrality could subsequently
exclude integer realization for this allocation; that downstream assembly
is not part of the current audit or an established all-order result.

Essential inputs for assessment are L051 (3)–(4), L055's exact allocation,
literal witness and audited count-dependent Lambda interval, and L062's
audited fixed-order root/guard reasoning. L056 is the named downstream
arithmetic result only, not a premise proving rigidity. No cross-notebook
input is proposed. The fixed modular stops in Attempts 027–030 and the
fixed feasibility failure in Attempt 031 remain evidence, not bans on a
different, independently testable order-rigidity mechanism.

The contemplated discriminating test is whether the first row displaced
from literal order must violate its own J guard in the unique cyclic
endpoint tuple. The scope review must decide whether ready affine/logarithm
coverage suffices for that comparison or an additional known ordering
theorem is essential. No inequality for an untested order is derived or
approved in this file. A missing uniform bound, a failed required margin,
or an explicit different order satisfying this subsystem would stop that
sufficient comparison; it would not establish an integer cycle or full
real-system feasibility. A proof excluding all nonliteral orders would
retain the literal one and still leave the downstream arithmetic assembly
to be justified separately.

Unresolved assumptions include any needed order-uniform root control and
all first-displaced-row height comparisons. The independent H guards,
seed, integer/parity/exact-tail/primitive realization, different allocations,
entry, unrestricted cycles, divergence and universal descent are not
settled by this proposed necessary-subsystem test. Prior published and
unchecked Mathlib/build qualifications persist. This file was supplied as
REVIEW_REQUIRED; the separate source comparison below approves its unchanged
target without performing a wider calculation.

## Separate literature approval — 2026-10-12

Read L051's exact hypotheses (1)–(4), L055's allocation, rational
construction and guard verification, L062's complete fixed-order argument,
and L056's literal-order nonintegrality statement and coordinate match.
L055 and L062 certify particular orders only. Reuse their audited
count-dependent Lambda enclosure; their order-dependent root and prefix
bounds must be justified anew when used uniformly. No numerical certificate
was generated or used to assert a new-order verdict in this review.

### Inspected theorem hypotheses and comparison

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239, DOI
10.4064/aa-78-3-227-239,
[published PDF](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf):
section 2 equations (2)–(4), Lemmas 1/2, pp. 228–229, give chronological
affine composition and the fixed point for a nonempty binary word.
Here the word has length N and K ones; only its formal affine identity
is needed, using L055's shifted-coordinate match. No coding reproof or
integer realization is needed. Read the odd-denominator argument and the
length-one/last-bit-zero induction; the source states the one case analogous.

Lemma 4, p. 230, compares distinct binary words of equal length and equal
one count: domination of every prefix one count reverses their numerator
ordering. Its finite bit-exchange proof was read. Lemma 3's nonnegative
decreasing-weight hypothesis and prefix-sum induction were also inspected.
Lemma 5/Corollary 1, pp. 230–231, optimize the minimum numerator over
all parity-phase rotations; both maximal-deficit and balanced-word rotation
cases were read. Neither ordering hypothesis nor an extremal objective
implies the requested own-index guard characterization. A block permutation
cannot be admitted to Lemma 4 merely from its equal totals; every prefix
hypothesis would still require checking. No new such comparison is claimed.

Kawase–Makino–Seimi, *Optimal Composition Ordering Problems for Piecewise
Linear Functions*,
[arXiv:1601.05480v1](https://arxiv.org/pdf/1601.05480v1),
submitted 2016-01-21 (the retrieved PDF title page bears 2018-09-12):
Theorem 1, p. 3, treats real affine functions with nonnegative slopes and
a prescribed real input. It finds an order maximizing total or partial
composition. Read Definition 7 and Lemma 9's pairwise composition test,
p. 6; Lemma 10's all-pairs ordering hypothesis and inversion-exchange
proof, pp. 6–7; Definition 11 and Lemma 14(b), pp. 7–8, and its complete
appendix proof, p. 16, including slopes equal to one. For slopes greater
than one the pairwise ordering uses each affine map's fixed-point ratio.
This is a scalar optimization result, with no junction-dependent guard
constraints or uniqueness conclusion for feasible orders. It does not
decide TARGET. No algorithm, ratio ordering, full mixed-slope proof or
parameter-specific application is imported as an input to the next attempt.

[NIST DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4) gives the logarithm
odd-power expansion on Re(z)>=0, z!=0. Positive real arguments in this
test meet the domain. Reuse the rational enclosures and remainder proofs
already inspected in L055 and its audit; the series alone does not certify
a truncation error. General cycle-source qualifications remain those of
L051 and the ready fixed-count/permuted-guard assessments. No stronger
primitive threshold or integer-cycle hypothesis is imposed on reals.

Full matching Mathlib coverage is unchecked. Previously recorded supporting
real logarithm/exponential results do not certify this allocation's
all-order statement; external Lean builds are unchecked. No new lemma
or mathematical script was written in this literature-only step.

### Search and duplicate scope

Queries actually run:

- `Collatz cycles affine maps ordering permutation rearrangement Halbeisen Hungerbuhler`
- `Collatz cycle exponent sequence ordering uniqueness real fixed point bounds`
- `Collatz "permutation" "blocks" cycle ordering`
- `Collatz "prefix" "Lemma 4" Halbeisen Hungerbuhler`
- `affine functions optimal ordering composition fixed point rearrangement positive slopes`
- `"Collatz" "397573379" "630138897"`
- `"Collatz" "ordering" "Halbeisen" "cycles"`

Exact-count hits were continued-fraction tables and speculative
preprints; they were not inspected theorem inputs. Combinatorial block
permutation hits concerned permutations as maps rather than these Collatz
affine blocks. The general affine-ordering lead was inspected as above.
No failed search establishes novelty, and no essential source is blocked.

The local search was limited to fixed-allocation assessments dated October
11–12, Attempts 027–031 and histories 174–177. Attempts 027–030 stop
modular diagnostics; Attempt 031 rejects one real-feasibility candidate.
None proves this all-order target. Preserve those stops. This is a distinct
necessary-guard mechanism, with no reopening of exhausted prime tests.
The target page and exact universal statement were already inspected today
in the ready permuted-real-guard assessment and are reused unchanged.

### Approved bounded attempt and stopping test

SPECIALIZE now covers one proof attempt on the exact TARGET. Essential
inputs are L051 (3)–(4), L055's intact allocation, literal witness and
audited Lambda interval, and L062's fixed-order affine/root/guard method.
L056 is only the potential downstream arithmetic use. No cross-notebook
input is involved. This approval is scope coverage, not an all-order result.

Attempt to control the cyclic root uniformly and upper-bound the junction
at the first row displaced from literal order, retaining positive offsets
and all 25 endpoints including the large closing tail. For every possible
first displaced position and remaining row, a rejection requires a strictly
positive certified margin between the necessary J guard's left side and
an upper bound for its right side. Preserve the non-strict guard sign and
each outgoing row's input pairing. Neither L055's literal prefix lower
bounds nor L062's one-order upper bound may be silently substituted for
these uniform obligations. A full exhaustive permutation enumeration is
not required if a justified uniform bound covers every case.

Continue if those bounds and all required margins are established. Stop
this sufficient comparison if an essential uniform bound cannot be proved,
a required margin is nonpositive/inconclusive, or an explicit nonliteral
order is verified to satisfy the stated subsystem. A failed sufficient
bound alone does not refute rigidity. A subsystem witness need not satisfy
independent H/seed or integer-realization requirements. Broader allocations,
new essential theorems and downstream integer exclusion require their own
coverage. Any completed proof remains subject to a separate critical audit.

Completed kind/classification: LITERATURE/NOVELTY_UNCHECKED; outcome
EXPLORATION. The new evidence is theorem-level coverage and an actionable
scope decision, not a mathematical advance, a rigidity verdict or certified
originality. No mathematical exploration budget was spent.
