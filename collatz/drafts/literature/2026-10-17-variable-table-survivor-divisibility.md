# Proposed variable-table survivor divisibility criterion

TARGET: Assess a variable-table finite-survivor divisibility criterion for excluding integral row-0 roots after C077a.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Two targeted searches on rational-cycle numerator divisibility and prescribed parity-vector integrality; inspected the primary affine and rotation-gcd statements, compared L020/L031, L056/L066, C077a and L077 coordinate passages, prior assessments and Attempts 026–031. No inspected source supplies the table-specific survivor certificates.
SOURCE_EVIDENCE: Halbeisen–Hungerbuehler (1997), published section 2 equations (2)–(4), Lemmas 1/2 and all printed induction cases pp. 228–229; section 5 equation (13), Lemma 9 equations (14)–(15) and full proof p. 238; reused earlier modulus-independent affine assessments. Reopened MathPrize exact statement dated 2021-07-07.
COMPARISON: The integer affine pair, fixed-point formula and rotation-gcd integrality mechanism are known. The remaining work is explicit specialization to C077a normalized row 0 and universally quantified finite survivors, with separately supplied arithmetic certificates; L056/L066 already establish fixed-allocation precedents.
GAP: A later proof must match the complete chronological integer numerator to x_0-23/11 for each surviving t, retain positive integer denominator and prove the conditional certificate implication; neither this review nor the sources establish certificates for arbitrary tables.
REASON: Coverage supports one separate RESEARCH/REPRODUCTION specialization of known divisibility machinery, without new coding, uniform-prime claims, new-table search or an integer-realization converse.

## Original proposal

The proposal below is preserved; its pending-review wording is superseded
by the completed source comparison below.

The main gap remains universal eventual descent. The proposed intermediate
target is a conditional arithmetic test for the finite candidate range
left by audited C077a, with downstream use in excluding integral
row-0 roots for independently certified tables. It must retain C077a's
full simultaneous tests and indexed outgoing allocations, integer r>=3,
B,tau>=0, increasing integer J_i>=2 and integer H_i>=3. The potential
survivors satisfy 0<=t<=B and t<tau; none is presumed feasible.

Essential available input: C077a, including its normalized coordinate
x_0-23/11 at the actual input of indexed row 0. L077 supplies a
prospective uniqueness/coordinate comparison for each literal endpoint
tuple. Inspect the exact existing integer affine machinery in L020/L031
and the fixed-allocation applications L056/L066 only as needed for the
source comparison. These are leads, not asserted inputs to a proved new
criterion. Their detailed arithmetic was not read for this continuation.
Do not transfer their particular prime residues to a different table.

Reuse the construction and audit assessments' primary affine coverage
where applicable: Halbeisen–Hungerbuehler, *Optimal bounds for the length
of rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239, section 2 equations (2)–(4), Lemma 2,
pp. 228–229. Compare the exact formal-word hypotheses and nonzero
denominator condition before importing its fixed-point formula. Search
for the precise arithmetic criterion, stronger known coverage and
duplicates. Inspect essential primary statements/proof cases before
larger passages; do not reprove a sourced divisibility test.
Full matching Mathlib coverage is unchecked.

The review test is whether the existing affine formula and audited
normalization cover a conditional, finitely certifiable obstruction
for every remaining parameter without a new realization converse.
Verify which unshifted coordinate the integer numerator represents,
whether the denominator is a nonzero integer, and what a modular
certificate actually proves. A zero numerator residue at a denominator
factor is not itself an integrality or nonintegrality verdict. Empty
candidate ranges must need no survivor certificate; B=0/1 and final
tail 2 remain in scope. A failed sufficient arithmetic test must not
assert feasibility. No arithmetic calculation or new table is proposed
for the literature turn.

Continue to a later mathematical step only if that comparison supplies
precise coverage; otherwise record the missing hypothesis or source and
narrow the target. Attempts 026–031 and both rational witnesses remain
valid; no stopped uniform-prime diagnostic is reopened. Actual-word
application, other tables, survivor guard feasibility and universal
eventual descent remain separate unresolved tasks. This proposal neither
derives a new result nor grants readiness to the continuation.

## Step 294 source comparison — 2026-10-17

SCOPE: Exactly TARGET, with all simultaneous C077a tests, independent certificate constants, integer r>=3 and B,tau>=0, increasing integer J_i>=2, integer H_i>=3, and attached allocations; only a conditional row-0 nonintegrality criterion, with no new-table arithmetic or actual-word bridge.
LITERATURE_REASON: The saved arithmetic continuation was REVIEW_REQUIRED; the prior composition audit covered no variable-table survivor-divisibility statement. This comparison closes that essential coverage gap and reuses ready affine coverage.

### Primary coverage actually inspected

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[published paper](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf):
section 2 equations (2)–(4) define the integer numerator for chronological
binary words and concatenate it with later maps on the left. Lemma 2,
p. 229, gives the affine map and its unique fixed point. Restrict its
printed unrestricted wording to nonempty words and nonzero denominator.
Read the length-one and appended-zero induction cases; appended-one is
printed as analogous. Lemma 1's odd-denominator pseudo-cycle argument was
also read; only formal affine identities are needed here.

Section 5, p. 238, Lemma 9 assumes a nonzero word and positive denominator.
Its pairwise equation (14) uses a rotation ending in one; equation (15)
identifies the gcd of all rotated numerators with the numerator/denominator
gcd. Read the full proof: the ending-one relation uses division by three
and coprimality with three, and ending-zero rotation doubles the numerator.
The following nonperiodic-word criterion is unused. No primitive-word
hypothesis is needed for the imported affine identity.

This confirms the earlier comparison in
`2026-10-11-swapped-root-mod431-obstruction.md`; Lemma 9 was already
inspected locally, rather than a newly discovered arithmetic mechanism.
It concerns rotations of one binary word, not arbitrary tail redistribution.
It provides no missing residue for a new allocation. No general integrality
or rotation-gcd theorem should be reproved in the next step.

The [MathPrize statement](https://mathprize.net/posts/collatz-conjecture/),
dated 2021-07-07, still requires every positive integer to reach 1 under
even halving and odd 3n+1. The source and shortcut conventions agree as
recorded in foundations/01-target-and-scope.md. Prize adjudication supplies
no mathematical premise.

### Exact specialization obligations for the later attempt

C077a gives the normalized input x_0 at indexed row 0, and candidates
S={t integer: 0<=t<=B and t<tau}. Its order and early-support conclusions
must precede arithmetic. No existence or passing J guards follow for a
member of S. All C077a tests remain hypotheses, including L077 (3) when
tau>B. Independent order/support/cutoff certificates remain independent.

For each t the proposed word is the literal chronological concatenation
of (OOEO)^{J_i} O^{H_i} E^{a_i(t)}. The source convention identifies
length with C077a's N and odd-letter count with K. The word is nonempty
and has odd letters; C077a's positive Lambda supplies the source's
positive nonzero integer denominator 2^N-3^K. The source numerator must
be the integer numerator for this complete word, including its final tail.

L020 supplies the positive integral compressed row offset. L031 explicitly
distinguishes formal affine identities from actual-word hypotheses;
its two-word realization converse is unnecessary and is not imported for
variable r. L056 (1)–(3) and L066 (1)–(2) already match compressed
integer offsets to an unshifted cyclic coordinate in two fixed allocations.
L077 (7)–(9) supplies the variable-table unshifted recurrence and unique
endpoint root. The later specialization must show the source numerator's
quotient is precisely x_0-23/11 at the normalized cut. This review compares
those scopes; it does not write or verify that generalized calculation.

The proposed arithmetic premise is a certificate of nondivisibility of
the complete integer numerator by the integer denominator for EVERY t in S.
This may be expressed directly, or by an integer divisor d_t>1 of the
denominator at which the numerator is nonzero modulo d_t. Primality is
unnecessary for that sufficient modular certificate. Any compressed
evaluation involving division by 11 must justify integral division before
reduction, including at moduli sharing factors with 11; source binary
recursion is available instead. Never invert the denominator modulo a
nonunit. A common zero residue supplies no verdict without further evidence.
No new residue, valuation or certificate is produced in this review.

For S empty, in particular tau=0, C077a already leaves no feasible tuple;
no arithmetic certificate is required. Otherwise every candidate needs
coverage, including B=0/1, tau=1, tau=B and tau>B. At t=B the final tail
is 2 and remains in the full affine word. A failed sufficient modular
certificate means only that this certificate does not decide the root.
No converse, survivor feasibility or actual integer orbit is asserted.

### Searches, duplicates and preserved stops

Queries actually run:

- `Collatz rational cycles integer cycle numerator divisibility Halbeisen Hungerbuhler phi word fixed point`
- `Collatz prescribed parity vector integrality 2^n-3^k divisibility cycle`

The primary paper suffices for the general mechanism. Search snippets for
Presburger obstructions, the Sterin thesis, rational-cycle reformulations
and code repositories remain unread leads and are not essential inputs.
No novelty inference follows from search results. No new broader source
needs retrieval to state this conditional specialization.

Compared the exact local affine and coordinate passages above, the ready
fixed-witness assessment, the variable-table assembly assessment, and
Attempts 026–031. L056/L066 already exclude their particular literal roots;
the proposed variable-table wrapper is not an additional exclusion of them.
Attempts 027–030 stop uniform prime-five or joint-prime nonvanishing and
certify cancellation on specific orders. Those stops survive; neither prime
nor residue transfers to new tables. Attempt 026 preserves rational real
feasibility, while Attempt 031 rejects a different permuted guard system.
A known divisibility criterion does not close these independent gaps.

### Decision and discriminating test

SPECIALIZE permits one later REPRODUCTION proof attempt for exactly TARGET:
import the source formula, check the normalized coordinate and denominator,
and assemble a conditional certificate criterion over S. The concrete
threshold is coverage of every member of S; a single omitted candidate,
coordinate mismatch or unsupported denominator hypothesis stops the proposed
assembly and must be recorded. Empty S needs no certificate. No new-table
search, fixed-prime extension, H/seed argument or actual-word application is
covered. A general coding reproof has no justification here.

Main gap: universal eventual descent remains open. The intermediate target
could make C077a's necessary reduction usable with independently certified
arithmetic inputs on later tables, but certificate production, new-table
applicability, survivor guard feasibility and the actual-word bridge remain
separate unresolved tasks. Both rational witnesses are preserved.

Full matching Mathlib coverage is not checked. Existing finite affine,
integer divisibility and valuation support does not establish a matching
variable-table assembly theorem; unknown availability is not absence.

Outcome: LITERATURE / EXPLORATION / NOVELTY_UNCHECKED. This is a new scope
comparison with known coverage, not a new lemma or verified integer
exclusion. No lemmas or mathematical scripts were modified and no
mathematical exploration turn was spent. The newly completed assessment
requires the supervisor's separate next-turn approval before mathematics.
