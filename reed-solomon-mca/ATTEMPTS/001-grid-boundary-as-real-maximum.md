# Adjacent-grid certificates as largest-real-radius answers

Reviewed 2026-09-25. The upstream ArkLib revision pinned by the official
companion project defines an adjacent safe/unsafe grid boundary and states
`GrandMcaResolution.sublevel_iff`. It does not claim that the safe grid point
is the largest safe real radius.

WHY IT FAILS: An automatic identification with the prize page's real maximum
loses the right-open portion of the last safe radius cell. The complete
[radius-cell proof](../lemmas/L001-affine-support-radius-cells.md) shows that
any nonempty proper safe set has no real maximum. The
[smooth-code witness](../lemmas/C001a-smooth-endpoint-witness.md) makes this
obstruction nonvacuous at rate 1/16 and error 2^-128. This rules out the
unqualified transfer, not the use of grid certificates once the intended
endpoint convention is explicitly settled. The July paper-to-model bridge
remains unverified; this is not a disproof of its intended mathematical target.
