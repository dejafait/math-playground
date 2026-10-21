# Fixed witness integer test — working notes

Approved target: Test integer realization of L055's fixed 25-word rational witness using a denominator-divisibility obstruction at primes at most 10000.

The main gap remains universal eventual descent. This bounded test addresses
only the omission of integer realization from L055's real relaxation; an
obstruction could inform arithmetic constraints on later cycle work. Preserve
Attempt 026: nonintegrality would not invalidate its real-system witness.

Reuse the supplied SPECIALIZE assessment and its inspected primary
Halbeisen–Hungerbuehler Lemma 2/equation (4). Essential inputs: L055's
literal allocation/root, L020's integral block offset, L031's formal affine
convention, and L051 (1)–(4) defining the witnessed system. No new literature
or uncovered target is needed. The relevant local source comparison and
histories 146–150 record no completed modular test of this allocation.

Plan: represent each formal affine map by integer triple (A,C,Q), mapping
x to (Ax+C)/Q. Concatenate in chronological order using the imported rule;
binary powering of the OOEO, O and E triples avoids division by 11. Verify
each compressed word independently against L020 using modulus 11p before
exact division, including p=11. Match the total root C/(2^N-3^K) to the
unshifted n_0, never to s_0. Enumerate primes through 10000 by a sieve and
independent trial-division list. Save complete rows/residues and failures.

Continue to a canonical arithmetic diagnostic if p divides the integer
denominator but not the integer numerator; common factors do not count.
If no such prime occurs through 10000, stop this test with no integrality
verdict and no automatic enlargement. Parity, valuations, residues,
primitive realization, other allocations/branches, entry and divergence
remain unresolved for other allocations. Calculation completed: prime 5
already certifies nonintegrality, with denominator residue 0 and numerator
residue 4. The complete bounded test also finds obstructions at 431 and
5233; 1229 primes and 34422 cross-checks, no failures. The canonical full
proof is [L056](../lemmas/L056-fixed-witness-prime-five-nonintegrality.md);
complete evidence is
`scripts/postspell-word-count/fixed-witness-integer-certificate.json`.
This is a relevant local ADVANCE/REPRODUCTION under the prior assessment,
not mathematics claimed beyond the known affine/divisibility machinery.
The fixed integer allocation stops; preserve its real witness and pursue
the separately gated audit recorded in PROGRESS.md.
