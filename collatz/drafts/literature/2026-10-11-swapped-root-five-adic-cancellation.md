# Swapped-root prime-power cancellation: source comparison

TARGET: Determine whether the reduced denominator of L057's swapped-order root is divisible by 5.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Six targeted queries on rational Collatz affine formulas, prime-adic cancellation, exact K,N, modular composition and Mathlib valuations; inspected local L055 allocation, L056/L057 affine proofs, relevant assessments, history 157 and Attempt 027. No inspected theorem decides this fixed order.
SOURCE_EVIDENCE: Reused fixed-witness/permutation source assessments and reopened Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemma 2 and its printed induction cases, pp. 228–229; inspected Mathlib PadicVal.Basic statements and complete proofs of padicValRat.defn, padicValInt_dvd_iff and Rat.num_or_den_zero_padicVal at commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953.
COMPARISON: Chronological affine composition and rational valuation cancellation are known; their finite application to one specific order needs exact residues and implementation verification, not a new general lemma.
GAP: Compare numerator and denominator powers of 5 for the unshifted root; common divisibility modulo 5 leaves this comparison unresolved, and the bounded cap may be inconclusive.
REASON: Essential valuation coverage is now adequate for a separate RESEARCH/REPRODUCTION calculation; no higher-power residue or new mathematical result is computed in this literature turn.
SCOPE: Only L057's intact-triple swap (0,6), fixed K=397573379 and N=630138897, unshifted affine numerator and Delta, exact moduli 5^e for 1<=e<=8; stop at a decisive comparison or the cap, with no other order, factor or real-system test.

## Relevance and local overlap

The main gap remains universal eventual descent. The intermediate target
is exactly TARGET. A surviving factor 5 would exclude integer realization
of this single order and could inform later allocation obstructions.
Complete cancellation would end this diagnostic without proving integrality.
An undecided comparison at the cap ends the bounded attempt as inconclusive;
no automatic enlargement is approved.

L055 supplies all 25 indexed triples and positive Delta; its real-system
witness is for the literal order. L056 supplies the integral unshifted
single-word offsets and coordinate match. L057 supplies exactly the order
6,1,2,3,4,5,0,7,...,24 and common divisibility by 5. The tail 166504412
stays attached to index 24; the other tails are 2. No permuted real-system
witness is assumed.

The narrowly searched fixed-allocation drafts, assessments and histories
150–157 contain no completed higher-power test of this root. History 157
and the audit assessment explicitly leave it uncovered. Attempt 027 stops
uniform modulo-five nonvanishing, not this fixed-order cancellation
question. L056's literal-order exclusion remains valid. Neither a renamed
uniform test nor a new order search is proposed. The previous mathematical
exploration count stays one; this literature turn spends none of that budget.

## Primary coverage and qualifications

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Lemma 2 and equations (2)–(4) give the integer numerator, chronological
concatenation and fixed point for a nonempty binary word with nonzero
denominator. The last branch acts on the left. The printed proof checks
one letter and an appended zero; the appended-one case is stated analogous.
We import the affine identity only. Here length is N, odd-letter count is
K, and L055's Delta is positive and unchanged by rearranging intact triples.
The general coding theorem needs no reproof. Reuse the prior permutation
assessment's inspected Lemma 9, p. 238: its rotation/gcd comparison does
not evaluate this particular numerator's prime-five valuation.

[Mathlib PadicVal.Basic, pinned source](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean)
provides `padicValRat.defn`: for prime p, nonzero rational q represented
by integer n/d, its valuation is the difference of the two multiplicities.
The proof passes to reduced numerator/denominator and cancels their common
factor. `padicValInt_dvd_iff` says p^e divides a exactly when a=0 or
e<=padicValInt p a, assuming p prime; its proof uses the integer absolute
value and natural-number divisibility theorem. `Rat.num_or_den_zero_padicVal`
uses coprimality of a reduced fraction to give zero valuation for at least
one member. All three complete proofs were inspected. The zero branch
matters: these valuations default to zero at zero. With nonzero inputs,
the standard cancellation rule tests survival by comparing their valuations.
This is supporting general coverage, not a formalization of L057's exact
allocation or a verified Lean calculation. No build was run.

The next attempt must justify the nonzero numerator from the retained
positive offsets and positive weights, and use L055 for Delta>0 before
applying these results. It must identify Phi_pi/Delta as the unshifted
root by imported composition, never replace it by s_0 or B. These are
applicability obligations for the separate attempt, not newly proved
mathematics in this source review.

## Search record and comparison

Queries actually run:

- `Halbeisen Hungerbuhler optimal bounds length rational Collatz cycles 1997 pdf`
- `Collatz rational cycle numerator denominator p adic valuation cancellation`
- `site.mathlib.org padicValRat div padicValInt`
- `Collatz "397573379" "630138897" denominator`
- `Collatz rational cycles numerator gcd denominator "5" valuation cancellation`
- `Collatz affine composition modulo prime powers prescribed parity vector integrality`

The first search locates the published primary paper. The Mathlib search
led to the official documentation and its pinned primary implementation,
not reliance on mirror snippets. Exact-count results include a continued-
fraction table and stopping-time manuscripts; snippets do not demonstrate
coverage of this order. A rational-cycle audit repository and forum rotation
swaps, prime-adic systems manuscripts and broad claimed Collatz resolutions
remain unread leads and are unused. The assessment reuses adequate affine
coverage rather than treating every search hit as an essential dependency.
No novelty follows from failure to find an exact-input result. No essential
source remains blocked for this finite application.

## Approved bounded evidence specification

A separate REPRODUCTION attempt may evaluate both integer expressions
modulo 5^e for 1<=e<=8, retaining all 25 triples and chronological terms.
Use exact modular powers without reducing exponents by the old modulo-five
period. If using the compressed offset's division by 11, verify its unit
inverse at each modulus; alternatively use integer affine composition
without division. Do not invert Delta or cancel from a zero residue.
Cross-check the compressed weighted numerator against direct chronological
composition using repeated squaring of the imported affine triples.

The certificate must retain the complete allocation, order, exact counts,
moduli, both residues, all comparison checks and failures. A first nonzero
residue modulo 5^(d+1), with zero residue modulo 5^d, certifies valuation d
for a nonzero integer. An exact denominator valuation d can be compared
with numerator divisibility by 5^d without determining a larger numerator
valuation. A certified smaller numerator valuation while the denominator
is divisible by its next power also decides survival without a complete
denominator valuation. These are applications of the cited divisibility
and cancellation rules, not newly discovered valuation theorems.

Stop immediately once sufficient evidence decides survival or complete
prime-five cancellation. If the retained evidence through e=8 does not
separate the possibilities, report the remaining valuation bounds honestly
and stop this diagnostic. Save full certificates to disk and print only
actual/required precision, verdict, failures and artifact paths. Any
claimed new exclusion needs a canonical lemma with full applicability and
proof, followed by a later critical review. This turn writes neither that
lemma nor a mathematical script.

Integer/parity/valuation/primitive realization, guards after permutation,
other factors/orders/allocations, entry, unrestricted cycles, divergence
and universal descent remain unresolved. Published qualifications remain.
This completed step is LITERATURE/EXPLORATION, NOVELTY_UNCHECKED: new
source comparison makes the bounded implementation ready but proves no
allocation exclusion. The supervisor separately approves this changed
assessment before invoking its calculation.
