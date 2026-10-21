# Fixed Q-relative calculation — working record

Step 373, 2026-10-20. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-Q-relative-P-local-seven-congruence.md`.
The main gap is arbitrary-curve rational-rank/complex-order equality.
The sole intermediate target is the approved depth-one coordinate of
Q=(1,0) relative to P=(0,0), on [0,1,1,-2,0] at seven.

Plan: exact original-model scalar chains and all seven differences,
with a separate translated-short-model replay and sequential scalar
checks. Retain every branch, denominator, intermediate point, primitive
projective reduction and reduced formal-parameter valuation on disk.
Compare [13]P against L081's audited value. Continue only if exactly
one difference is O or has parameter valuation at least two and all
others have valuation one. Otherwise stop without switching inputs.

Essential inputs are L030/L033 (model and reduction order), L081
(audited P input), and the local-quotient part of L083. L034 supplies
published point provenance, but no seven-saturation is assumed.
The downstream use is an explicit rational representative in the local
Kummer kernel; nonzero global quotient membership, zero rational
logarithm and arbitrary-curve rank equality remain independent gaps.
Relevant L081/L083 proofs, step-319 audit, L034's source qualifications
and ATTEMPTS/045 were read. No duplicate Q-relative value was found
in the scoped search. No order-route repair or iteration is authorized.

Completed: L096 records the exact outcome Q=4P modulo 7E(Q_7).
The full certificate and independent replay in
`scripts/Q-relative-seven-373/` pass all 23 rows, 91 distinct-chain
sequential additions and all seven candidate tests. Their t valuations
are (1,1,1,1,2,1,1). The complete Q scalar/parameter value, all candidate
valuation triples and unit residues, and the entire winning local
evidence were inspected with the bounded JSON inspector, using --full
for load-bearing values. No failed arithmetic or changed input occurred.
The canonical proof, limitations and next audit proposal are in L096
and the current checkpoint; this draft is no longer an unfinished attempt.
