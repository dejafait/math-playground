# Attempt 040 — scalar-aware occurrence translation under unchanged caps

The approved scalar-only operand adapter passed the previous record-7 stop
on the unchanged 31-record proof, but stopped at zero-based axiom record 22.
Canonical preservation argument, precise source use and complete verification
qualifications are in [L097 §12](../lemmas/L097-source-resolution-occurrence-product-affine-abp-witness.md).

**WHY IT FAILS.** The unchanged Booleanity constructor supplies two 201-record
original-only operands to a nested L035 call, whose exact independent copy
ledger requires 10,500,818 records against the fixed 2,000,000 cap. Scalar
folding of source-tree translations does not prevent this suffix/prefix copy
cost. The retained outer graph covers 22 source lines and 469,893 records;
no complete K/H or partial-K polynomial acceptance exists. Full pending
operands, trace and independent receipts are in output-473 under
scripts/four-rule-extraction/. Stop this scalar-adapter/input/unchanged-constructor
combination without raising caps. A separate graph-path trimming test on the
exact failed operands is proposed for review, with no implementation or bound
derived here. Attempts 036–039 and all unfinished work remain preserved.
