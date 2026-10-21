# Changed-tail survivor prime-five diagnostic: source approval

TARGET: Determine whether prime 5 survives in the reduced denominator of L065's exact j=23 unshifted cyclic root by comparing its numerator and denominator modulo 25.
CHECKED: 2026-10-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Two focused web queries on the exact changed tail/count and rational-cycle changed-word cancellation; inspected L055's complete table, L056's integer offset/composition and coordinate match, L058's cancellation rule, L064/L065's changed-tail root hypotheses, histories 193 and the recent survivor drafts, and Attempts 027–028. No inspected result decides this changed numerator.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), section 2, equations (2)–(4), Lemma 2 and relevant induction cases, pp. 228–229; reuse the pinned Mathlib valuation statement/proof assessment in 2026-10-11-swapped-root-five-adic-cancellation.md and L058's supporting citation.
COMPARISON: Known formal affine composition and prime-valuation cancellation apply with changed tails; the remaining work is a finite exact evaluation of this allocation, not a new general theorem. L058's denominator calculation has unchanged K,N, but no old numerator residue transfers.
GAP: The changed-tail chronological numerator modulo 25 and its independently verified coordinate/implementation match remain uncomputed; real feasibility supplies no integrality verdict.
REASON: Source hypotheses and duplicates now checked for the changed allocation, supporting one separate RESEARCH/REPRODUCTION calculation without a coding or valuation reproof.
SCOPE: Only L065's literal J,H order, a_23=20, a_24=166504394 and all other tails 2; unshifted n_0=s_0-23/11, K=397573379, N=630138897, modulus 25 only, no order or factor search.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes the allocation after L065's audit; check essential changed-tail applicability while reusing ready affine and valuation coverage.

## Relevance and decision test

The main gap is universal eventual descent. The intermediate target is
exactly TARGET. A surviving factor 5 would exclude integer realization
of this particular full real witness; cancellation would stop this
allocation-specific diagnostic. Neither verdict settles another allocation,
an unrestricted cycle or eventual descent.

Continue only with a verified comparison of the complete integer pair at
modulus 25. Stop after this tuple and modulus. If the evidence is insufficient,
record precisely the missing valuation information and stop rather than
extend precision or change factors. L058 already establishes Delta=5 modulo
25 for these same K,N: that denominator conclusion is reusable, subject to
an independent check in the forthcoming certificate. Thus its exact
prime-five valuation is already sourced locally; the changed numerator is
the unresolved input. No new residue is evaluated in this review.

## Primary input and applicability

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[published primary PDF](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
section 2, equations (2)–(4), Lemma 2, pp. 228–229.
The source composes chronological bits with the last branch on the left;
its integer numerator recursion and concatenation formula give the affine
map and fixed point. Read the one-letter case and appended-zero induction;
the printed appended-one case is stated analogous. Restrict to nonempty
words and nonzero fixed-point denominator. Only formal affine identities
are imported, without rational-parity conclusions; no general reproof is
needed. Rotation/gcd results do not evaluate the changed numerator.

Here the word is the 25-row chronological concatenation
(OOEO)^J_i O^H_i E^a_i. L064 gives its unchanged totals and positive
Lambda, hence a nonzero positive Delta=2^N-3^K, and identifies the unique
unshifted cyclic root. L065 fixes this exact tuple, with positivity.
L056's displayed compressed offset C_i depends on J_i,H_i, while its
row denominator uses D_i=4J_i+H_i+a_i. Its formal formula is explicitly
valid before itinerary realization; changing the final even tail changes
D_i and the chronological weights, so it requires recomputation of those
weights. L056's integrality justification uses 27=16 modulo 11, independent
of tails. All J_i,H_i are positive in L055's table. These are checks of
existing formula hypotheses, not a derivation of a changed-tail verdict.
The separate attempt must explicitly match its imported Phi/Delta to
L064's n_0 rather than s_0 or B alone, including the changed closing tail.

Reuse [the ready cancellation assessment](2026-10-11-swapped-root-five-adic-cancellation.md),
which inspected complete statements/proofs of `padicValRat.defn`,
`padicValInt_dvd_iff` and `Rat.num_or_den_zero_padicVal` in
[Mathlib PadicVal.Basic, commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean).
These require prime p and careful nonzero handling; integer divisibility
includes an explicit zero alternative. The rational valuation is the
difference of numerator/denominator valuations, with coprimality of the
reduced pair supplying the cancellation interpretation. Here p=5 is prime;
L064 supplies a positive denominator and the imported positive offsets
and weights supply a nonzero numerator. Check these in the attempt before
using the rule. Full matching Mathlib coverage for this tuple and verified
Lean computation remain unchecked; supporting declarations are not a
formalization of the allocation.

## Discovery, duplicates and failures

Queries actually run:

- `Collatz "166504394" "397573379"`
- `Collatz rational cycles changed parity word numerator denominator prime cancellation Halbeisen Hungerbuhler`

The exact query returned no demonstrated match to this tuple. The broader
query located the published primary paper and its publisher bibliographic
record. Generalization papers, repositories and a forum rational-cycle
example remain unread leads and are unused. No novelty inference follows
from these searches. Reuse the adequate affine and valuation assessments;
there is no essential source blocker.

The narrow local search of 2026-10-13 survivor assessments/drafts and recent
history found a proposed diagnostic, not a completed modular evaluation.
L056 concerns the original literal tails; L057–L061 concern different intact
orders of that old allocation. Attempt 027 stops uniform prime-five
nonvanishing for the old multiset; Attempt 028 stops prime-five exclusion
of its single swap. Neither is reopened or contradicted. L063/C063a's
fixed-allocation conclusions do not transfer to changed tails. L064/L065
and their audits establish real feasibility, not an integer realization.
Preserve all these stops and unresolved assumptions.

## Approved next-turn evidence

Use L055's entire literal J,H table, L065's actual tails and L064's exact
closure. Reuse L056's imported formula and L058's cancellation mechanism,
not their allocation-specific numerator residues. Evaluate all 25
chronological contributions and Delta modulo 25. Check the compressed
weighted sum against division-free chronological affine composition.
If division by 11 is used, verify its unit inverse modulo 25; never invert
Delta or cancel a common zero residue. Retain both changed rows, all prefix
lengths and suffix odd counts, complete contributions, both evaluations,
actual/required precision and failures in the certificate.

With the denominator's independently checked exact valuation one, apply
the cited rules: a numerator nonzero modulo 5 leaves a factor 5; a numerator
divisible by 5 removes that denominator factor, including a numerator zero
modulo 25. A zero square residue alone does not identify an exact numerator
valuation. Any conclusion must remain limited to this prime and allocation.
No arithmetic, new lemma, or mathematical script is produced this turn.

Integer junctions, parity/residue/exact-valuation and primitive-orbit
realization, other allocations, unrestricted cycles, divergence and
universal eventual descent remain unresolved. SPECIALIZE authorizes the
separate bounded calculation as REPRODUCTION; it does not claim novelty.
