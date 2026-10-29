# Marked elliptic raw quartic enumeration — over-cap stop

2026-10-25. The approved feasibility test reached a rigorous workload
negative before enumeration. Exact normalization and counts are in
[L128](../lemmas/L128-marked-elliptic-quartic-workload.md), with certificate
`scripts/pair-genus-two/elliptic-quartic-workload-certificate.json`.

WHY IT FAILS: After minimal normalization and justified omission of the
larger dyadic pair, the raw region has 3834148 rows versus the 200000
cap. Its type-one subregion 1<=a<=16 already has at least 2199936
triples versus the 2000000 cap. This stops the unsieved implementation,
not descent or the rank-one possibility. It says nothing about surviving
integral quartics, proper classes or locally soluble coverings. Do not
repeat the same loops or enlarge their caps automatically. A traversal
through syzygy-admissible seminvariants must independently establish
coverage and bounded workload. ATTEMPTS/050–052 and unfinished L108
remain preserved.
