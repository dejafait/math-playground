# Attempt034 — L106's fixed endpoint tuple as a full-guard witness

## WHY IT FAILS

[C106a](../lemmas/C106a-l106-fixed-tuple-row3-guard-failure.md) proves
that the exact L106 tuple has s3<10^12, while its own row3 non-strict
J3=52 guard requires s3>=(4/11)2^208. The cut3 estimate retains all25
terms, the actual closing tail and the same chronological tuple.
The construction certificate passes92 finite checks. A separate critical
audit on 2026-10-26 confirms the same verdict without repair, with729
finite checks and the complete proof in C106a. Park this fixed-witness
full-guard route. The other49 guards
are untested and L106's endpoint-only cap counterexample remains valid.
Failure of this witness supplies no feasibility or exclusion conclusion
for other allocations and no Collatz resolution. Preserve Attempt032/033,
the original-H witnesses and unfinished work. Any new allocation search
or general support mechanism needs its own independently testable target
and coverage; changing the allocation alone does not remove this evidence.
