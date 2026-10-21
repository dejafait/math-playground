# Attempt 016 — Small logarithmic coalescence clocks

The cover with both shortcut clocks at most C log(n)+B, for fixed
0<C<1/log(12) and B>=0, is obstructed on 47 modulo 243 by
[L027](../lemmas/L027-subcritical-log-height-residue47-coalescence-obstruction.md).
This stops precisely those coefficients, rather than every full-height
clock. Attempts 014–015 retain their separate scopes and evidence.

## WHY IT FAILS

L027 selects L026 roots above its strict size threshold with a uniform
upper height of 4*12^L. For every stated fixed C,B, all sufficiently
large selected roots have their logarithmic clock below L. L026 then
excludes every smaller positive residue-20 companion on both actual
paths, including zero clocks. The roots are unbounded, so finite base
exceptions cannot repair this cover. The positive coefficient slack
is essential to the comparison; endpoint and larger coefficients are
unresolved. This supplies no nonconvergent start or universal descent
estimate. Independent critical review on 2026-10-05 found no defect;
the complete audit is recorded in canonical L027. The stop retains
exactly the stated subcritical scope.

## Subsequent endpoint decision, 2026-10-06

The endpoint question left open by that subcritical proof is now
obstructed by [L028](../lemmas/L028-endpoint-log-height-residue47-coalescence-obstruction.md),
whose separate critical audit found no defect. This extends the stopped
cover coefficients to C=1/log(12), for every fixed B>=0, while
preserving the historical L027 argument and its stated scope. The
canonical endpoint proof retains both actual paths, offsets, zero clocks
and strict order against the original root. Larger coefficients remain
unresolved; the stop is neither nonconvergence nor a global research ban.

## Subsequent strict-coefficient audit, 2026-10-07

[L033](../lemmas/L033-subcritical-log-six-coalescence-obstruction.md)
extends the obstruction to every fixed 0<C<1/log(6), B>=0.
Its separate critical audit found no defect; the canonical proof and
audit retain L028's guarded horizon, strict height comparison and both
actual clocks. The coefficient 1/log(6) itself remains unresolved.
This preserves the earlier stops and does not revive Attempt 020's
unproved digit forcing. No nonconvergent root or universal descent
conclusion follows.
