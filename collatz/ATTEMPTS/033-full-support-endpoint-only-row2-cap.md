# Attempt033 — Endpoint-only full-support row2 cap

## WHY IT FAILS

[L106](../lemmas/L106-d35-full-support-row2-cap-counterexample.md) gives
an exact factored rational endpoint tuple at b0=b1=1,b2=12,
b24=9250231 and all other budgets zero, with all25 lower domains,
all original endpoints and closure, but s2>2^118>(4/11)2^112.
Thus the uniform endpoint-only cap is false; shifting budget into row2
creates a large reciprocal-prefix term excluded by L105's fixed-tail
triangle. The certificate has249 passing finite checks, with no failures;
the separate step506 audit in L106 now validates this exact endpoint-only
rejection, with1923 independent finite checks and no failures. This does not
assert any J/H guard, integer junction or actual Collatz word, and does
not refute full-guard infeasibility or universal descent. Abandon this
cap alone. A later exclusion needs additional guards or a materially
different independently testable target with separate source coverage;
failed sufficient estimates are not feasibility evidence. Preserve
Attempt032, L105 and both original-H witnesses.
