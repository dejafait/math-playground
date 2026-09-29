# Attempt 018 — Mixed resolutions with insufficient slopes or divisor spans

Date: 2026-09-27. Outcome: two scoped exclusions; unrestricted mixed
resolutions and arbitrary compatible bundles remain unresolved.

The proposed change to the stopped single-polarization recipe allows
different line-bundle divisor classes and an arbitrary final twist.
The full necessary-condition proof is
[L027](../lemmas/L027-mixed-resolution-slope-and-divisor-rank-obstructions.md).

**WHY IT FAILS IN THE EXCLUDED CASES.** Without a final twist, anti-ample
terminal terms have negative slope, so a stable terminal bundle with
invariant c_1 cannot embed in them. With any twist, the normalized
second character still requires a divisor correction with a nonzero
cubic eigenvalue. That operator has rank at least three and cannot
come from original divisor classes spanning at most two dimensions
in either factor. The general twisted case instead must have at least
rank(E)+1 strictly positive terminal terms and sufficient divisor
spans. Passing these necessary tests is not a bundle construction or
an escape from the separate map-recovery obstruction.
