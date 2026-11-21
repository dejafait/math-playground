# Actual power inclusion failure — step581

The approved audit found a strict inward-rounded upper endpoint in an
actual atan(239) power call. Full hypotheses, exact integer proof and
qualifications are canonical in [L815](../lemmas/L815-polya-census-real-path-tail-bounds.md).
The complete arithmetic certificate is `../scripts/polya-census/audit-581.json`;
its replay intentionally returns exit status1. The original census is retained.

WHY IT FAILS: The returned power interval omits the13th power of its own
upper input endpoint. Consequently the advertised compositional inclusion
argument is invalid, and it cannot validate any of the thirteen event
exclusions depending on pi. This does not show that the actual Machin
value or a transform lies outside its final stored interval: the exact
(1/239)^13 remains enclosed. Stop at this failed arithmetic premise rather
than rerun the census. An independently certified aggregate pi enclosure
is a concrete different repair target; until then full-tail/trigonometric/
normalization/whole-cell audit and all thirteen exclusions remain unverified.
The separate fixed-cap cancellation failure and unresolved [6.5,40] persist.
