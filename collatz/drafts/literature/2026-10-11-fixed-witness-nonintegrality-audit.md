# Fixed-allocation nonintegrality: audit source coverage

TARGET: Critically audit L056's fixed-allocation nonintegrality proof, coordinate match and modular certificate.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the four targeted queries and duplicate/failure comparison in 2026-10-11-fixed-witness-integer-realization.md; inspected L056, L055's literal table/root, L020's affine-offset proof, L031's formal-composition qualification, Attempt 026 and histories 150–151. No new discovery search was needed for this unchanged allocation.
SOURCE_EVIDENCE: Reopened the published Halbeisen–Hungerbuehler (1997) PDF, section 1 p. 227 and section 2 pp. 228–229, Lemmas 1/2, equations (2)–(4), chronological convention and all printed Lemma 2 proof cases; existing affine coverage suffices for the proposed audit.
COMPARISON: Known finite affine coding covers the integer numerator, fixed root and composition order; only the local coordinate match and exact finite implementation evidence need independent verification. No new general theorem or novelty is asserted.
GAP: The later critical audit must independently verify L056's coordinate identity, every prime-five summand and the certificate implementation; this source comparison has not verified those claims.
REASON: SPECIALIZE approves one separate RESEARCH/REPRODUCTION proof audit of the literal allocation, using imported affine machinery without reproving general parity coding or enlarging the search.

SCOPE: Only L056's fixed ordered L055 allocation at K=397573379, N=630138897, n_0=s_0-23/11, its written modulo-five proof and bounded certificate through 10000; no new allocation, wider prime search or integer/parity sufficiency claim.
LITERATURE_REASON: The supervisor requires separate approval of the new L056 audit continuation; reopening the primary statement checks whether existing coverage includes its formal real-coordinate use and composition order, rather than renewing discovery on the ready allocation test.

## Gap, use and discriminating test

The main gap is universal eventual descent. The intermediate target is
an independent critical audit of L056's nonintegrality diagnostic for
L055's literal unshifted root. A sound diagnostic can eliminate that
one integer realization and identify arithmetic information omitted by
the real relaxation. It does not exclude all allocations with these
counts or supply a universal mechanism.

Coverage is now ready for the separate audit. Continue by independently
checking the complete written proof and finite load-bearing evidence.
Retain the diagnostic if those checks agree; repair a specific defect
if found, and suspend any unsupported conclusion if it cannot be repaired
within this fixed scope. A generator's success flags alone do not pass
the test. No expanded search follows automatically.

## Primary theorem and applicability

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[published PDF](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The inspected section 2 defines chronological binary compositions on
real inputs, with the last branch on the left. Equations (2)–(4) specify
the integer numerator, its explicit sum and concatenation. Lemma 2 gives
the affine map and fixed root. Its proof checks length one, then the
last-zero case; the last-one case is stated analogous. The printed
statement must be restricted to nonempty words for unique fixed roots.
Section 1 and Lemma 1 concern rational parity in the odd-denominator
domain; that parity conclusion is unnecessary here.

Use length N, odd-letter count K, and the same O/E conventions. The
local allocation is nonempty; L055 supplies a positive denominator.
The audit needs only the formal affine formula and the necessary
fixed-point equation for any actual integer realization. It must not
apply L031's two-word converse as a 25-word converse. L020's offset
and L031's explicit formal-identity qualification cover the compressed
single-word convention; L055's root definition supplies the coordinate
to match. No general coding reproof or new mathematical derivation is
needed in this source review. The specialized algebra is already written
in L056 and remains to be independently audited.

## Exact future audit scope

Read the full canonical L056 proof and L055's literal table/root.
Verify the unshifted n_0 match, all 25 numerator contributions with
chronological order, positive denominator, and the noncancellation
argument at 5. Inspect the complete relevant evidence in
`scripts/postspell-word-count/fixed-witness-integer-certificate.json`
and `scripts/postspell-word-count/fixed-witness-written-table-check.json`;
bounded previews alone are insufficient. Check the source/table match,
complete prime enumeration through 10000, empty failures and the full
exceptional-prime records, including the lifted quotient at 11.

Review `scripts/postspell-word-count/test_fixed_witness_integer.py`:
its named composition, binary powering, offset, sieve and trial-prime
routines correspond to the claimed audit checks. This turn inspected
only their scope, not their correctness. Independently verify division
by 11 using a lifted modulus, with 121 at p=11, and absence of nonunit
inversion. If reproducing the certificate, retain full evidence on disk
and report actual/required values and failures concisely. The proof's
prime-five argument is load-bearing; auxiliary prime coverage is also
a claim to verify, not an essential new theorem.

## Duplicates, failures and qualifications

The ready predecessor assessment contains the actual queries, precise
source comparison and distinction between inspected theorems and unread
count-pair/repository leads. Those leads remain unused. No failed search
establishes novelty. L056 is a local application of known machinery;
its audit is REPRODUCTION, not a new modular theorem.

Attempt 026 and L055's audited real witness remain intact. L054's failed
envelope and the real-system stop do not prohibit this arithmetic audit.
The earlier bounded integer test is completed; this audit neither repeats
it as discovery nor reopens another allocation. No cross-notebook input
is used. Full matching Mathlib coverage and external Lean builds remain
unchecked; unknown availability is not absence. Published qualifications
for the restricted actual-cycle exclusions remain inherited and are not
needed to apply integer-cycle estimates to arbitrary reals here.

Other allocations' parity, valuation, residue and primitive realization,
other count branches, universal entry, unrestricted cycles, divergence
and eventual descent remain unresolved. The restricted exclusion remains
through 24. This LITERATURE/EXPLORATION approval changes the next gate to
source-ready, but proves no mathematics and does not complete L056's
critical audit. Mathematical exploration usage remains unchanged.
