# Fixed rational witness: integer realization — source comparison

TARGET: Test integer realization of L055's fixed 25-word rational witness using a denominator-divisibility obstruction at primes at most 10000.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Four targeted queries on rational fixed points, parity integrality, modular obstructions and exact K,N; inspected L020/L031/L051/L055, Attempt 026 and relevant histories 146–149. No completed modular test of this allocation found; exact-count hits do not establish matching allocation coverage.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), published section 1 p. 227 and section 2 pp. 228–229, equations (2)–(4), Lemmas 1/2 and complete relevant proof text; reused prior fixed-count assessment for unchanged affine coverage. Precise citation below.
COMPARISON: General affine numerator, denominator and concatenation rules are known. L055 supplies the allocation; bounded exact modular evaluation is an implementation specialization, with no new integrality theorem or novelty claim.
GAP: A separate research turn must match the imported integer numerator to unshifted n_0 and compute divisibility with justified cancellation and exceptional-prime handling; no modular obstruction has been calculated.
REASON: Coverage supports one separate RESEARCH/REPRODUCTION calculation importing known formulas, verifying the local coordinate match and avoiding a general coding reproof.

Essential local inputs are L055's exact 25-row table and factored cyclic
root, and L051 (1)–(4) for the scope of the real relaxation. Reuse the
general affine-coding source notes from
`drafts/literature/2026-10-11-twenty-five-fixed-count-tail-budget.md`
where adequate; inspect only the primary hypotheses/proof cases needed
to compare the new divisibility target. Compare local recorded failures
and integer-closure conventions narrowly before approving mathematics.
No cross-notebook result is proposed.

The main gap is universal eventual descent. This intermediate target
would diagnose an arithmetic constraint omitted by the real witness,
potentially informing later integer-cycle work. It concerns only this
fixed allocation, not every allocation with the same counts and not
all 25-word cycles. Nonintegrality would preserve, not overturn, the
audited real-system feasibility and Attempt 026. Integrality by itself
must not be taken to establish input parities, exact valuations, residue
membership, primitive-cycle realization or a counterexample to Collatz.

After separate coverage approval, the proposed discriminating test is
to seek a rigorous modular obstruction to divisibility at primes at most
10000, using exact modular powers and justified denominator handling.
Continue on a certified obstruction, or record that this finite test
supplies no verdict and stop it without inferring integrality or enlarging
the search automatically. This is source-covered for a separate attempt, not a computed result. Integer realization, other
count branches, entry, divergence and universal descent remain open.

SCOPE: Only L055's literal 25-row table/tails, K=397573379, N=630138897, unshifted n_0=s_0-23/11 and primes at most 10000; no allocation search or parity/valuation/primitive-cycle conclusion.

## Primary statement and proof cases

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[published PDF, pp. 227–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Section 1 uses g_0(x)=x/2, g_1(x)=(3x+1)/2 and rationals with odd
reduced denominator. Section 2 orders bits chronologically, composing
the last branch on the left. Lemma 2 gives, for nonempty binary w,
the map (3^k x+phi(w))/2^l and fixed point phi(w)/(2^l-3^k).
Equations (2)/(3) define the integer numerator and (4) concatenates it.
Here l=N,k=K; exclude the empty word despite printed unrestricted wording.
Read the one-letter case and last-bit-zero induction; last-bit-one is
stated analogous. Lemma 1 explains rational parity consistency for closed
formal orbits in the odd-denominator domain. No general reproof is needed.

## Applicability and proposed certificate

Use exactly (OOEO)^{J_i} O^{H_i} E^{a_i} in L055's printed order.
L055 establishes its formal recurrence and unique root. L020's integral
single-word offset and L031's formal-composition discussion support the
implementation; the latter's two-word conclusion is not a 25-word theorem.
The next calculation must match the source integer pair to n_0, not shifted
s_0 or rational B alone. No new coordinate conversion is derived here.

Use the imported integer recursion/concatenation convention. If the
compressed L020 offset is used, justify division by 11 also at p=11,
either avoiding division through integer recursion or using sufficient
lifted modulus before exact division. Never invert a nonunit or round a
quotient. Check or explicitly dispose of primes 2 and 3 using the imported
denominator convention. Verify complete prime enumeration through 10000
and all reported residues, retaining the literal allocation and exceptions.

For an unreduced integer pair, an obstruction requires a prime dividing
the denominator but not the numerator. A prime dividing both gives no
verdict at that precision; cancellation cannot be ignored. The research
turn must give the elementary integer-divisibility justification and verify
its compressed implementation against the imported formulas. This is a
future evidence specification, not proof or computation of nonintegrality.

## Search, duplicates and failures

Queries actually run:

- `Halbeisen Hungerbuhler Optimal bounds length rational Collatz cycles Lemma 2 pdf`
- `Collatz cycles fixed parity vector integer divisibility 2^l 3^n numerator`
- `Collatz "397573379" "630138897"`
- `Collatz prescribed parity vector integrality modular obstruction denominator primes`

The primary paper covers the general construction. Exact-count hits include
*Bit-Position Dynamics and a Lower Bound for Collatz Cycle Length*
(vixra:2504.0141v1) and a ResearchGate stopping-time manuscript: only
snippets inspected, without demonstrated match to L055's allocation.
Presburger-obstruction and repository leads remain unread and unused.
No essential source blocker remains. Search failure is not novelty evidence.

Attempt 026 stops real-system exclusion; Attempt 025/L054 stops its weaker
upper envelope. Neither stops this arithmetic question. L031 already
records closure/divisibility for two words, so report the proposed work
as reproduction on another fixed input. Relevant histories 147–149 and
fixed-count assessments leave this test unperformed. No global modular
research ban follows from prior failures or unread leads. Universal entry,
other allocations/cycles, divergence and eventual descent remain open.

## Mathlib and route decision

Full matching Mathlib coverage and external Lean builds remain unchecked;
unknown availability is not absence. Existing exact-target and shortcut
convention coverage is reused without expansion.

SPECIALIZE supports a separate bounded REPRODUCTION calculation, subject
to the supervisor's separate approval of this newly completed assessment.
This step is LITERATURE/EXPLORATION, NOVELTY_UNCHECKED: actionable source
coverage, no mathematical advance, lemma, mathematical script or calculation
budget usage. Stop on a certified obstruction or exhaustive absence through
10000; no obstruction gives no integrality verdict or automatic enlargement.
Any actual-orbit conclusion requires its own justification and review.
