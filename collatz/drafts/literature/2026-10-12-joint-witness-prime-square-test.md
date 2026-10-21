# Fixed common-zero root: prime-square source comparison

TARGET: Test L060's fixed two-transposition root modulo 25 and 185761 for a strict numerator/denominator valuation mismatch.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Three focused queries on Collatz rational-cycle prime-power integrality, exact K,N with 431, and two-transposition prime-square numerators; inspected L055 allocation, L056 affine coordinate proof, L060 fixed-order proof, L058 cancellation law, prior affine/valuation assessments and Attempts 027–029. No inspected theorem or local duplicate decides this order at either square.
SOURCE_EVIDENCE: Reused Halbeisen–Hungerbuehler (1997) section 2 equations (2)–(4), Lemma 2, pp. 228–229 and prior inspected induction cases; reopened pinned Mathlib PadicVal.Basic complete statements/proofs of padicValRat.defn (lines 181–200), Rat.num_or_den_zero_padicVal (342–350), and padicValInt_dvd_iff (633–644).
COMPARISON: Known affine composition and valuation cancellation cover the machinery; this fixed-order square-modulus evaluation is an implementation specialization, not a new general theorem. Rotation/gcd and real prefix-order comparisons do not supply its residues.
GAP: Neither square-modulus residue pair has been calculated; the bounded test may exclude this root's integrality or leave this precision inconclusive.
REASON: Essential coverage is adequate for a separate RESEARCH/REPRODUCTION calculation, without reproof or originality claims; this literature-only turn computes no new residues.
SCOPE: Only L060's swaps (0,8),(7,12), fixing row 24, unshifted numerator and unchanged denominator, at 25=5^2 and 185761=431^2; no order search or higher-power extension is preapproved.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes common-zero tests to valuation comparison at two prime squares; reuse ready affine and cancellation coverage while checking the new input scope.

## Relevance and existing evidence

The main gap remains universal eventual descent. The intermediate target
is TARGET. A strict denominator-over-numerator valuation gap excludes one
integer allocation and can inform later arithmetic diagnostics. Cancellation
at these primes cannot supply integrality or a universal allocation exclusion.

Essential inputs are L055's entire allocation, K=397573379, N=630138897
and positive Delta; L056's integral positive unshifted offsets and root
formula; L057's chronological permutation rule; and audited L060's order
and common zeros. The fixed chronological order is

```text
8 1 2 3 4 5 6 12 0 9 10 11 7 13 14 15 16 17 18 19 20 21 22 23 24
```

Keep every triple intact, a_i=2 for indices below 24 and a_24=166504412.
The root being tested is Phi_pi/Delta, not the shifted junction or B.
The separate calculation must justify its nonzero numerator using the
positive offsets/weights and its nonzero denominator using L055. No
permuted real-system guard is assumed.

Attempts 027–029 respectively stop uniform prime-five nonvanishing,
prime-five exclusion of the different swap (0,6), and joint nonvanishing
for the bounded two-transposition family. L058's equal valuations concern
(0,6), and L059's 431 exclusion also concerns that different order.
L060's common-zero witness leaves this square test unresolved. Targeted
searches of the joint-prime attempt/audit drafts and history 169 found only
the proposed square continuation. Preserve these stops and unfinished work;
a historical diagnostic stop does not decide this independent finite test.

## Precise reusable inputs

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Reuse the ready assessments
`drafts/literature/2026-10-11-joint-prime-two-transposition-test.md` and
`drafts/literature/2026-10-11-swapped-root-five-adic-cancellation.md`.
The imported identity concerns nonempty formal binary words, with last
branch composed on the left and nonzero fixed-point denominator. Here
length N and weight K stay unchanged. The inspected proof handles one
letter and appended zero, stating appended one analogous. We need only
the affine identity; rational parity realization is not imported. Canonical
applicability and compressed offsets already reside in L056/L057/L060.
No general reproof is warranted. Previously inspected Lemmas 4 and 9
compare real prefix ordering and cyclic-rotation gcds; neither decides the
new literal residues.

[Mathlib PadicVal.Basic, commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean):
`padicValRat.defn` requires prime p, nonzero q and q represented by integer
n/d. It gives the multiplicity difference; its proof cancels the common
factor of the reduced pair and checks finite multiplicities.
`padicValInt_dvd_iff` requires prime p and says p^e divides a exactly when
a=0 or e<=padicValInt p a; the proof reduces to absolute-value natural
number divisibility. `Rat.num_or_den_zero_padicVal` requires prime p;
coprimality makes at least one reduced multiplicity zero. Their complete
proofs and enclosing hypotheses were inspected. Zero inputs need separate
handling because valuation definitions default to zero there. This is
supporting coverage, not a formalization of the fixed allocation; no build
or full matching theorem was checked. The later calculation must certify
primality of each base before interpreting prime valuations, or state only
a divisibility contradiction without prime terminology.

## Search comparison

Queries actually run:

- `Collatz rational cycles numerator denominator prime power valuation parity word integrality`
- `Collatz "397573379" "630138897" "431"`
- `Collatz cycles two transpositions numerator modulo prime squares`

Search hits included the already known Halbeisen–Hungerbuehler PDF,
repository audits, forum rational-cycle examples and rotation swaps,
Knight's high-cycle work, a rational-cycle coprimality paper, and general
claimed Collatz resolutions. Only the reused primary affine assessment
and reopened official Mathlib implementation support this decision.
Other hits are unread leads, not theorem-level coverage or premises.
The prior real-order/rotation comparison remains adequate for its unchanged
scope; no theorem about high or extremal words is applied to this arbitrary
fixed order. No essential source is blocked. Failed discovery establishes
neither novelty nor absence of stronger results.

## Approved bounded calculation and stop test

A separate REPRODUCTION turn may compute the complete weighted integer
numerator and unchanged denominator at exactly the two square moduli.
Use unreduced integer exponents with modular repeated squaring. Check
compressed offsets by lifted exact division by 11 modulo 11m, or by a
justified unit inverse; independently cross-check against division-free
chronological affine composition. Include every row and the large tail.
Never invert Delta or cancel from a zero residue.

Apply the cited divisibility and cancellation rules with the existing
common-zero facts: a nonzero square residue certifies valuation one;
a zero square residue only certifies valuation at least two. A numerator
of valuation one paired with denominator divisible by p^2 certifies a
surviving denominator factor. Equal exact valuations one certify complete
cancellation at that prime only. Numerator divisibility by p^2 paired with
exact denominator valuation one also removes that denominator prime.
Two zero square residues leave the comparison unresolved. These are the
known rules to specialize, not new results calculated this turn.

Retain both full residue evaluations even if the first prime is decisive,
since the approved target names both. Save all 25 contributions and
composition states, exact allocation/order/counts, denominator powers,
nonzero/primality obligations, checks and failures in a full certificate.
Print only verdict, actual/required precision, failures and paths. Stop
at these two moduli regardless of outcome: no implicit higher-power test
or further order search is approved. A decisive exclusion remains local;
inconclusiveness ends this bounded diagnostic without claiming integrality.

Integer/parity/exact-tail/primitive realization, permuted real guards,
other orders/allocations, entry, unrestricted cycles, divergence and eventual
descent remain unresolved. Inherited source qualifications and unchecked
full Mathlib/build coverage persist. Mathematical exploration usage is zero
this literature turn; zero consecutive mathematical EXPLORATION is retained.
This completed source comparison is LITERATURE/EXPLORATION,
NOVELTY_UNCHECKED. The supervisor's separate approval precedes calculation.
