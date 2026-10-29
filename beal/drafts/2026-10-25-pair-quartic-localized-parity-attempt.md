# Localized parity calculation — saved attempt

2026-10-25. Approved target: determine the augmented parity rank after
adjoining e_1,e_26,...,e_31 to L136's complete relation matrix, and the
upper bound for Cl(O[1/330])/2. Prior SPECIALIZE coverage is
`literature/2026-10-25-pair-quartic-localized-parity.md`.

Inputs: L133's field, audited L134's maximal order, audited L135's
complete ordered prime lattices, and audited L136's complete 182 rows.
ATTEMPTS/059 stops the ordinary full-rank box; no relation search or
box enlargement is authorized here. Preserve unfinished L108.

Plan: bind both certificates and exact inverted-prime lattices, reconstruct
every parity row from accepted valuation vectors, record all ascending
elimination operations and input-combination witnesses, independently
replay and eliminate in reverse order with descending pivots. The fixed
domain is 189 rows of 32 bits; at most 20000 counted row XORs and 256-bit
witnesses, with no search. Save full certificates and failures to disk.

The test ends either way. Rank r gives only the upper bound 32-r;
failure of binding withholds the bound. Possible downstream descent use
requires support containing all primes above 2,3,5,11, which remains
unestablished. Units, descent, ranks, points, lifts, degree-nine recovery,
L095 systems and other signatures remain independent gaps.

Completed: [L137](../lemmas/L137-pair-quartic-localized-parity-bound.md)
records exact augmented rank 30 and localized dimension upper bound two.
Every added coordinate already lies in the original relation span, so
this supplies informative negative evidence against rank improvement.
The complete independent verifier passes 6739 checks. Full row operations,
combination identities, opposite-pivot elimination, exact input bindings
and seven short original-span witnesses are retained in the certificate
and verification files named in L137; no relation search was performed.

The first producer stopped on a record-schema comparison before elimination.
Its source/certificate are preserved. After selecting the matching p,
space_id and complete lattice fields, producer and verifier complete.
Cumulative row XORs 3134/20000, witness XORs 1400/20000, mask bits
189/256 and rows 189/189 have no cap stop; the ledger retains that initial
implementation failure. No old ledger was reset. ATTEMPTS/060 records the
stop, and a separate critical-audit target is proposed with REVIEW_REQUIRED.
