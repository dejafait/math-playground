# 2026-10-14 — First capped p=7 Kurihara residue is zero

STEP_ID: BSD-2026-10-14-225-conductor389-capped-kurihara-zero

Completed the approved single implementation/replay in
[L064](../lemmas/L064-conductor389-capped-kurihara-zero.md).
Complete capped eligibility selects (113,281); both least primitive roots
are 3. Full independent replay gives residue zero on all 31360 unit terms
and 319804 path segments, with exact weighted sum -1365. The retained
reports and four qualified rejection fixtures are under
`scripts/conductor389-kurihara/`. Original inputs and unfinished work remain
preserved. This is RESEARCH/REPRODUCTION and an informative NEGATIVE for
the capped nonzero-input test, not new mathematics beyond known methods.

[ATTEMPTS/032](../ATTEMPTS/032-conductor389-first-capped-kurihara-zero.md)
records the stop: no L063 exponent follows, and no other pair or depth is
tested. A separately gated critical audit is the sole continuation;
its new assessment remains REVIEW_REQUIRED. No Selmer quotient,
localization, rational membership or arbitrary-curve rank gap is closed.
