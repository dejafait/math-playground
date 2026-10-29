# Permuted d35 minimum/successor guard obstruction — source comparison

TARGET: Test whether the J guard at a cumulative-product minimum or its immediate successor excludes every permutation of the d35 pair multiset over the full integer tail simplex.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Step520 ran the eight web queries below and a scoped local ordering/failure search; no inspected theorem supplies the specific two-guard dichotomy. The duplicate check found L075 and L084's audited independent O data through d35, changing route priority.
SOURCE_EVIDENCE: Inspected Halbeisen–Hungerbuehler(1997) sections2–3 Lemmas2/4/5 and relevant proof cases; Blanchard–Higham–Higham(2019-09-08) section4 equations(4.1)–(4.2); Kubo–Makino–Sakamoto(ISAAC2024) Theorems1/3 and neighborhood definition. Read L075's full criterion/proof and L084's conclusion and all-member O audit; reuse qualified analytic/integer-cycle comparisons below.
COMPARISON: Finite-affine and positive-sum machinery cover tools, not the successor verdict; scalar and rotation extrema do not supply simultaneous own-input exclusion. L075 already supplies an all-order criterion, and L084 records d35 O coverage independently of failed S/C/H tests; this existing route should precede creative duplication.
GAP: The cumulative-product-minimum/successor dichotomy remains unproved. EXPLORE licenses only its bounded test, not a theorem or novelty claim. Separately, d35 applicability of L075 and assembly with C107a remain unwritten and are not established by this literature turn.
REASON: Complete the changed-permutation-scope comparison; park the adjacent-guard mechanism in favor of preparing the existing independent-order criterion. Preserve its exact target for possible reopening if that route exposes a genuine missing premise.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED assessment lacked essential comparison for arbitrary permutations and the successor guard; previous literal-order coverage did not assess this scope.

## Proposed purpose and bounded test

Universal eventual descent is the main gap. The intermediate target is
exactly TARGET. Its plausible downstream use is removal of the literal
order restriction within this single pair multiset; arbitrary tables,
entry, actual-word transfer, unrestricted cycles and divergence would
remain unresolved. It is not a universal-descent criterion.

Keep the25 pairs of L055 with H0=5,H24=32670656 as intact J,H pairs,
but allow every permutation. Attach a nonnegative integer budget to
each outgoing row, sum B=9250245, a_i=2+18b_i; retain kappa=23/11,
all endpoints and closure, s_i>=540/11, and both original own-input
non-strict J/strict H guard families. No minimum junction, seed,
integer/residue/valuation realization or primitive-period premise is
available. Repetitions and every zero budget, including closing tail2,
must remain allowed. Any rotation must preserve pairs, tails and their
own inputs together.

The proposed new ingredient is the guard at a minimum of the finite
cumulative multiplier products and, when that row does not yield a
contradiction, the guard at its immediate chronological successor.
The unique low-J pair is the potential obstruction to simply reusing
L107's designated-index argument. This is a proposed test, not a claim
that the successor resolves it. The coupling and arbitrary order are
outside the completed audit's scope.

First compare exact known ordering hypotheses and proof cases, reusing
saved affine and finite-maximum coverage where applicable. Attempt027
is prime-specific and does not assess these real guards; do not replay
its arithmetic or infer novelty from this narrow search. No
cross-notebook result is proposed. Mathlib coverage remains unchecked.

If separately approved, a creative proof attempt should test a single
permutation-uniform minimum/successor dichotomy on the unchanged closed
tuple. Continue only with a rigorous bound covering all possible
minimum/successor pair types and the full allocation domain. An exact
admissible order/allocation defeating the proposed dichotomy, or a
required unavailable premise, is decisive evidence against this
mechanism, not against Collatz. Failure of a loose bound alone is only
exploration. Preserve partial reasoning and require a refined mechanism
or new input before repetition.

The intended later route is proof_attempt/creative, deep_research/max:
the obstruction is L107's order-sensitive exclusion of its exceptional
minimum index; the bounded test is whether the adjacent own-input guard
supplies a uniform contradiction when the minimum guard does not.
That nomination required the separate comparison completed below.

## Completed comparison — step520, 2026-10-26

The nomination above remains historical motivation. Universal eventual
descent is the main gap; TARGET and its conditional downstream use are
unchanged. No new inequality, allocation, counterexample, lemma or
mathematical program was produced.

### Discovery and inspected primary sources

Queries actually run:

- `Collatz rational cycles ordering permutations parity vectors Halbeisen Hungerbuhler Lemma 4 5`
- `Collatz cyclic affine maps minimum cumulative products successor bounds cycles`
- `Collatz "9250245" permutation guards`
- `Collatz rational cycles ordering permutations "minimum" "successor"`
- `Collatz cycle affine composition rearrangement ordering block permutations guard`
- `"Collatz" "rational" "ordering" cycles Halbeisen`
- `"Collatz" "cumulative products" minimum`
- `"Collatz" "adjacent" "guard" permutation`

Results supplied the sources below and uninspected parity discussions,
claimed proofs and formalizations; none of the latter is an input.
Search absence is not novelty evidence. Rechecked the precise
[MathPrize statement](https://mathprize.net/posts/collatz-conjecture/),
page dated2021-07-07: every positive integer eventually reaches1 under
even halving and odd3n+1. Prize adjudication supplies no mathematical
premise.

**Affine and rotation ordering.** Halbeisen and Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica78(1997),227–239, DOI10.4064/aa-78-3-227-239,
[author PDF](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf),
sections2–3, Lemmas2/4/5, published pp.229–231 (PDF pp.3–5).
Lemma2 gives finite binary-word affine composition and its fixed point;
inspected length-one, appended-zero and printed analogous-one cases.
Use composition only: shifted-block matching and denominator sign remain
local obligations; rational coding supplies no integer realization.
Lemma4 requires distinct equal-length/equal-one-count binary words with
domination at every prefix; read its finite exchange proof. Lemma5
identifies the maximum, over words, of the minimum numerator over
rotations via a ceiling mechanical word. Read both the maximizing
staircase rotation and comparison with all rotations of that word,
including equality. Equal block totals do not establish prefix
domination; an extremal cycle minimum does not identify the proposed
cumulative-product minimum or successor. These results do not prove
TARGET. No general coding or ordering reproof is justified.

**Finite positive sums.** Blanchard, Higham and Higham, *Accurate
Computation of the Log-Sum-Exp and Softmax Functions*, MIMS EPrint2019.16,
author version2019-09-08,
[section4 equations(4.1)–(4.2), printed p.8](https://eprints.maths.manchester.ac.uk/2728/1/paper.pdf).
Rechecked the maximum-shift argument for finite real inputs, ties and
n=1. It bounds log-sum-exp between the maximum and maximum+log n.
This covers L107's25 positive terms after handling the shift separately,
not a successor cap. Import it without reproof; floating-point stability
is not an exact-arithmetic certificate.

**Scalar composition.** Kubo, Makino and Sakamoto, *Composition Orderings
for Linear Functions and Matrix Multiplication Orderings*, ISAAC2024,
44:1–44:14, DOI10.4230/LIPIcs.ISAAC.2024.44,
[Theorems1/3, pp.44:3–44:4](https://drops.dagstuhl.de/storage/00lipics/lipics-vol322-isaac2024/LIPIcs.ISAAC.2024.44/LIPIcs.ISAAC.2024.44.pdf).
Rechecked all three Theorem1 cases and Theorem3's increasing-function
hypothesis and adjacent-interval-swap neighborhood. These characterize
scalar minimum compositions and local/global equivalence for that
neighborhood. Reuse the case-(i)/(ii) proof comparison in
`2026-10-14-last-pair-permuted-j-feasibility.md` and
`2026-10-17-full-allocation-cyclic-order-rigidity.md`; no optimizer theorem
is imported. A cyclic root changes with order and every intermediate
guard has its own input; scalar optimality is not TARGET. Case(iii)'s
full-version proof remains unimported and nonessential.

Reuse the qualified primary-source comparison in
`2026-10-26-row2-guard-positive-row0-row1-full-support.md` for
Simons–de Weger, *Theoretical and computational bounds for m-cycles of
the3n+1-problem*, Acta Arithmetica117(2005),51–70,
[sections1.2,2.1–2.2, Lemmas4/6/7](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
Its integer-orbit/local-minimum and global-height premises are absent;
25 rows need not be25 orbit minima. Import no conclusion. The saved
Knight2026 publisher-preview lead remains an unread theorem, not a
premise or essential blocker to this finite test. Reuse the positive-real
DLMF scope and audited denominator enclosure in L107's assessment only
after matching totals. No fresh analytic bound was calculated. Matching
and supporting Mathlib coverage for the new dichotomy remain unchecked.

### Route-changing local overlap and failures

Read L107's full minimum-prefix argument and qualifications and L055's
complete table. L107's literal b0>=1 premise cannot be transferred to
a permuted exceptional minimum. Its affine/maximum tools are reusable;
permutation applicability and successor control still need proof.

The targeted local search found the independent order route. Read L075's
full statement/proof, L084's conclusion and all-member O audit, and
L097's d34 application. L075's sufficient criterion is independent of
support and fixed-root cap tests. L084 reports no O failure through d35:
its d>=5 S failures and d>=34 C/H failures do not reject the independent
O package; O failures start at d36. L097 is a d34 precedent, not d35.

This source-scope finding is not a new d35 application or assembly with
C107a. No d35 order lemma was found in the scoped assessments/DAG.
The existing family certificates' `/tables/34/O` and
`/reconstructed_tables/34/O` were located with the JSON inspector;
only labeled previews were viewed, not verified complete records.
A later application must use L084's full audited mathematical input and
inspect complete records wherever relied on; previews are not proof.

Attempts027–030 concern modular diagnostics on other fixed data.
Attempts032–034 and L106/C106a retain their sufficient-package,
endpoint-cap and fixed-witness stops. Attempt035 rejects repeated
unchanged approvals, not this changed ordering comparison. No stop was
erased or enlarged to a global ban; no cross-notebook input was read.

### Decision and test

EXPLORE covers a later finite-affine/maximum attempt at TARGET without
claiming a result known or original. Park it now because L075/L084 offer
a more direct route to its intended order-gap use. All-guard exclusion
would not by itself prove this particular two-guard dichotomy.

The separate nomination `2026-10-26-d35-independent-cyclic-order.md`
requires approval before the changed mathematical application. If that
route exposes a missing premise, preserve it before reopening TARGET.
Then retain the original test: cover every minimum/successor pair type,
tie, wrap, zero budget, closing tail2 and repeated period, or exhibit an
exact admissible two-guard counterexample/missing premise. A counterexample
defeats this mechanism only; failure of a loose cap is inconclusive.
Do not reprove known machinery or create a creative target to duplicate
an existing order criterion.
