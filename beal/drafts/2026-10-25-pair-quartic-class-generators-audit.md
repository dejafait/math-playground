# L135 critical audit — work checkpoint

Approved target: Critically audit L135's Minkowski-bound class-group generator certificate, including exceptional-prime completeness and generation from bounded ideal representatives.
The supplied SPECIALIZE assessment is `drafts/literature/2026-10-25-pair-quartic-class-generators-audit.md`; it is reused without further literature work.

Main gap: elimination of all residual primitive Beal signatures. Intermediate target: authenticate the exact 32 prime-ideal generators in L135. A validated factor base can support class relations and supported descent, while units, ranks, points and recovery remain independent gaps. Accept only if the complete domains, exact arithmetic, source hypotheses and printed list agree; isolate any failure without using an unaudited conclusion.

Read L133's field identification, L134's accepted basis/discriminant and product table, full L135, both complete class programs and their accounting implementation. Reused the supplied source comparison and checked ATTEMPTS/019,045,058 and history/481: none duplicates this instance audit or forbids it. No cross-notebook input. Existing changes and unfinished L108 are preserved.

Before execution: the program review supports exhaustive monic-divisor tests and complete RREF-subspace enumeration. The regular-prime dimension argument uses the imported prime-factor theorem, including repeated factors; it does not infer rank from containment alone. The exceptional test uses the full maximal-order algebra. No correctness verdict yet: replay, input binding, complete output inspection and identification with the printed tables remain pending.

Planned additional arithmetic is one existing replay and a small audit supplement under the existing cumulative ledger/caps, with no regeneration of the producer certificate. The supplement will bind hashes to the audited order, inspect exact numeric types, and compare the entire final list against L135's displayed tables. Full proof and qualifications will remain canonical in L135.

## Completed audit

Accepted without mathematical correction. The full replay passes 1409026 checks, and the new `scripts/pair-genus-two/audit_quartic_class.py` supplement passes 353 statement/input-binding checks. The complete mathematical audit, exact hashes, exhaustive-domain arguments, printed-list identification and cumulative bounds are in `lemmas/L135-pair-quartic-class-group-generators.md`; full supplement evidence is `scripts/pair-genus-two/quartic-class-audit.json`. No producer regeneration, cap stop, failure or ledger reset occurred. This is local validation of a known-method specialization, with no new class relation or Beal conclusion. The sole continuation and its separate coverage gate are recorded in PROGRESS.md.
