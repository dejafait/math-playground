# Marked elliptic seminvariant sieve — inspection-cap stop

2026-10-25. The single fixed-sieve test yields an informative workload
negative. Signed-region coverage, conditional complete reconstruction,
and exact counts are canonical in
[L129](../lemmas/L129-marked-elliptic-seminvariant-sieve-workload.md).
The complete producer and verification certificates are
`scripts/pair-genus-two/seminvariant-workload-certificate.json` and
`scripts/pair-genus-two/seminvariant-workload-verification.json`.

WHY IT FAILS: Exact divisibility by 27 and square-image tests modulo
64,5,7,11,13 leave 216116 integer (a,p) pairs in type-one a=1,...,34
alone. Each would require inspection in the tested square-first
traversal, exceeding the unchanged 200000 cap before any b recovery.
One counting/verification execution costs 191963 units. The first ledger
omitted 204 inverse preparations; its repair and repeated execution
cost 383926 cumulatively, above the cap. Whole-step compliance is not
claimed, and no further mathematical run is justified here.
No square syzygies, quartics, classes or Selmer elements were counted.
The 2000000 expansion budget was not tested. This stops this fixed
sieve/per-p traversal only; it neither proves all sieves infeasible
nor refutes rank one or descent. No cap increase or sieve retuning
was tried. Preserve ATTEMPTS/050–053 and unfinished L108. A different
three-descent mechanism is proposed for separate source comparison;
no theorem coverage or instance feasibility is presumed for it.
