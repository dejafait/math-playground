# Proposed two-survivor arithmetic scope

TARGET: Evaluate the complete unshifted affine numerator and denominator modulo 25 for both L079 survivors t=0,1, testing whether a factor 5 survives reduction.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the recorded rational-cycle affine/divisibility and changed-tail prime-power searches; targeted local comparison of L078, L079, L055 table, earlier survivor assessments and Attempts 027–031 found no certificate for this changed-H pair of allocations. No repeated broad discovery search.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemma 2 and all printed induction cases pp. 228–229; reopened pinned Mathlib PadicVal.Basic statements and complete proofs of padicValRat.defn, padicValInt_dvd_iff and Rat.num_or_den_zero_padicVal; reused ready assessments dated 2026-10-17 and 2026-10-11.
COMPARISON: Known chronological affine composition and prime-power cancellation cover the mechanism; audited L078 already supplies the normalized unshifted row-0 coordinate. Changed H values require fresh numerator evaluation for each t; no cited source or inspected local result supplies those residues.
GAP: Only the complete finite modulo-25 evaluations and their independent implementation checks remain for this target; neither survivor nondivisibility nor feasibility is established by this review.
REASON: Essential source coverage is sufficient for a later RESEARCH/REPRODUCTION calculation on exactly t=0,1 and modulus 25; no coding, divisibility or valuation theorem reproof is justified.

The original proposal below is preserved; its pending-review wording is superseded by the completed scope comparison appended below. This literature turn performs no calculation. Main gap:
universal eventual descent. The intermediate target is a bounded test of
one necessary arithmetic obstruction at each of the two remaining literal
allocations. If both numerator/denominator pairs prove nonintegrality,
they could discharge L078's survivor premise for this one table. An
inconclusive or cancelled factor stops this diagnostic for that survivor;
it supplies no integrality or feasibility conclusion. No new prime,
permutation, table or wider parameter search is proposed.

Essential input IDs: L079 (audited changed-table data), C077a (normalized
row-0 coordinate), L078 (complete chronological integer numerator and
positive denominator), and L055 solely for the explicit underlying table.
Only H_0=39 and H_24=32670622 differ; r=25, B=9250245. The two allocations
are b_0=...=b_22=0, b_23=t, b_24=B-t for t=0,1, with every actual
tail a_i=2+18b_i retained, including the closing edge. All numerator and
denominator residues must be freshly evaluated; their old-table values
are not assumptions. Essential unresolved premises are nondivisibility
for each survivor and all realization/feasibility conditions. No actual
word exclusion or universal-descent conclusion is part of this target.

The later scope comparison should reuse the ready primary records in
`2026-10-17-variable-table-survivor-divisibility.md` and narrowly relevant
earlier modular assessments. Read L078's exact formula and the needed
source proof cases before authorizing calculations. Attempts 026–031
remain stops for their original data and tested orders; a changed literal
table is independently testable, not a reopening of uniform prime
nonvanishing over the old permutations. No novelty claim is made.

The discriminating test is complete exact residues at 25, with each
coordinate identified as the normalized unshifted row-0 root. A divisor
certificate needs nonzero numerator modulo a divisor of the positive
denominator; valuation comparison must distinguish surviving factors
from cancellation. Common zero residues are not an integer-cycle verdict.
Stop after the two approved evaluations, preserve any failure, and leave
unresolved survivors for a separately assessed materially different test.

## Step 306 source comparison — 2026-10-18

SCOPE: Exactly TARGET, L079's changed-H table, r=25, B=9250245, tau=2, literal allocations t=0,1 and modulus 25 only; no larger modulus, new factor, permutation, table or feasibility test.
LITERATURE_REASON: The gate is REVIEW_REQUIRED because the prior data audit and conditional divisibility assessment exclude changed-table arithmetic; this comparison checks that essential specialization while reusing their ready primary coverage.

### Primary results and applicability

Reuse `2026-10-17-variable-table-survivor-divisibility.md` and
`2026-10-11-swapped-root-five-adic-cancellation.md`, together with the
changed-tail precedent `2026-10-13-survivor-prime-five-diagnostic.md`.
Their recorded searches concern exact-count rational-cycle numerators,
prescribed parity vectors, divisibility and prime-adic cancellation.
This table stays within those mechanisms. No new terminology or broader
search is essential, and no failure to locate an exact certificate implies
novelty. Unread broader leads in those records remain unused.

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[primary paper](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
section 2, equations (2)–(4), Lemma 2, pp. 228–229, was reopened.
Read the chronological definition, numerator recursion, concatenation rule,
fixed-point statement and all printed induction cases: length one,
appended zero, and the printed assertion that appended one is analogous.
Use only the formal affine identity on real inputs and its fixed point
for a nonempty word with nonzero denominator. The paper's empty-word
wording is not imported. No itinerary converse or rotation-gcd theorem
is needed. The www URL timed out; the non-www primary URL succeeded,
so no essential source blocker remains.

The ready L078 proof and audit already identify its complete numerator
Phi(t) and Delta=2^N-3^K with the normalized **unshifted** root
x_0-23/11=s_z-23/11, where z carries indexed outgoing row 0.
Read its full formula/coordinate passages and audit. Its formal word is
the chronological concatenation of (OOEO)^{J_i} O^{H_i} E^{a_i(t)};
later maps act on the left. The present application changes no convention.
L079's hypotheses and certified totals give K=397573379, N=630138897
and positive Lambda. They meet the source's nonempty-word and nonzero
positive-denominator qualifications. L078's positive integral offsets
and weights cover the numerator's nonzero hypothesis without assuming
any actual orbit or feasible J guards.

The full 25-row J,H table was read from L055, with L079's replacements
H_0=39 and H_24=32670622. All other pairs remain literal. L079 and
C077a supply only the necessary survivor set {0,1}. Reusing L078's
already audited identity needs no new coordinate lemma. Its chronological
prefix exponents and offsets must be evaluated for the changed data,
including the closing tail. An unchanged total does not authorize reuse
of an old numerator or old intermediate prefix.

The supporting primary valuation implementation is
[Mathlib PadicVal.Basic](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean)
at commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953.
Reopened the statements and complete proofs of `padicValRat.defn`
(prime p and nonzero represented rational; cancellation via a common
factor), `padicValInt_dvd_iff` (prime p, with an explicit zero branch),
and `Rat.num_or_den_zero_padicVal` (prime p, reduced coprimality).
The latter two proofs reduce respectively to integer/natural divisibility
and coprimality. These support comparing powers of 5 in the two nonzero
integers and interpreting cancellation in the reduced fraction. Default
valuation at zero must not be confused with nondivisibility. Full matching
Mathlib coverage for the changed table is unchecked; no Lean build or
formal certificate is claimed. No general valuation reproof is needed.

### Duplicates, failures and finite evidence requirements

L056/L066 decide different literal inputs on the original H table.
L058 and L061 decide cancellation for specific old-table permutations.
Attempts 027–030 stop uniform nonvanishing or fully cancelled primes for
those fixed orders; Attempt 031 rejects one such order's real guards.
Their stops remain binding on those data, but do not decide this changed
literal table. This is an independently testable two-case target, not a
reopening of uniform prime nonvanishing. Both original rational witnesses
and unfinished work remain intact.

A later calculation must save every row's actual pair and tail, raw prefix
and suffix exponents, compressed offset and weighted contribution modulo
25, plus all chronological composition states. Evaluate Phi independently
by the imported compressed formula and division-free composition of the
formal O/E maps. Repeated squaring may handle long runs. Justify compressed
division by 11 using its unit inverse modulo 25, or use an integral lift;
never invert Delta. Retain the final even tail in N and the final map.
Recompute both denominator powers and Delta modulo 25 independently,
even though the total counts agree with earlier records. Modulo-5 evidence
may be obtained by reduction of these complete modulo-25 residues.

Apply only the cited prime-power divisibility/cancellation rules to the
actual observed residues. A nonzero residue modulo 5 determines valuation
zero; divisibility by 5 with nonzero residue modulo 25 determines valuation
one; zero modulo 25 supplies only a lower bound unless other already
justified information suffices. A smaller numerator valuation certifies
nonintegrality only with a strictly larger denominator valuation. Equal
exact valuations remove this prime from the reduced denominator. If the
available precision does not decide the comparison, record that limitation
and stop. These are known interpretation rules, not new table evaluations.
No numerator or denominator residue is newly computed in this review.

### Decision and continuation boundary

SPECIALIZE covers a separate RESEARCH/REPRODUCTION calculation of exactly
TARGET after the supervisor's separate approval of this changed assessment.
The concrete test is two complete agreeing evaluations at modulus 25,
with the correct unshifted coordinate and justified valuation verdicts.
If both yield nonintegrality, their certificates could discharge L078's
survivor premise for this table in later separately scoped work. Cancellation
or insufficient precision stops this diagnostic for the affected survivor;
no automatic larger modulus, new prime or parameter expansion is approved.
A mismatch between the independent evaluations is an implementation failure,
not a mathematical obstruction, and must be preserved and resolved within
this bounded target before claiming a verdict.

The main gap remains universal eventual descent. Survivor feasibility,
other tables, actual-word exclusion and the universal claim are not settled.
This source comparison is LITERATURE/EXPLORATION/NOVELTY_UNCHECKED: it
closes an essential coverage gap but proves no new mathematical input or
allocation exclusion. Mathematical exploration usage remains zero.
