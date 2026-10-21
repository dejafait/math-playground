# Fixed eleven-adic ideal basis search — parked

2026-10-16. The [attempt](../drafts/2026-10-16-fixed-eleven-ideal-attempt.md)
and [certificate](../scripts/separated-eleven-unit/fixed-ideal-certificate.json)
record one reduced basis of (Q_8 R_8) intersect Z[k,t], with exact
membership, unimodularity and two agreeing norms for all 36 elements.
All 77 checks pass; no element has the required absolute norm 121.

WHY IT FAILS: None of the prescribed 36 candidates generates the fixed
ideal, so the supported-unit correction and parity stages were not
reached. The smallest tested absolute norm is 4,435,693,858,496,483,
but this is not a lower bound for arbitrary elements of that ideal.
An integral-order intersection and its reduced basis do not enumerate
all maximal-order generators. Principality and the existence of a
separating supported unit remain unresolved. With three exploration
attempts spent and no new restriction, park this search without adding
candidates; move to an independently testable local-image target after
its source assessment. ATTEMPTS/032–035 remain unchanged.
