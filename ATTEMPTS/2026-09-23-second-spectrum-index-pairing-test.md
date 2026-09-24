# Second-spectrum index pairing test — 2026-09-23

The gap is actual-theta all-degree mixed positivity. The intermediate target was a nonnegative double theta-series expansion for the unsplit second associated spectrum, with the two index orders paired. Its downstream use would be second-level positivity and a possible higher-level pattern; those further steps remain unresolved. The discriminating test was the large-frequency sign of each unordered index block: one negative block stops this termwise mechanism.

The whole overview, global DAG, checkpoint and existing changes were inspected and preserved. L234 supplies the finite-term boundary slopes but addresses the first spectrum, while L253 signs a different, non-autocorrelation remainder. Neither already computes the unsplit second-level cross blocks. L235 also warns against whole-line modular averaging, so no nonintegrable whole-line term expansion was used.

[L254](../lemmas/L254-second-spectrum-theta-index-pairing-obstruction.md) derives an absolutely convergent double series and proves every (1,m) unordered block for m≥2 is eventually negative. The exact modular cancellation removes the summed leading coefficient, rather than signing the individual blocks. This is new negative evidence for the specified pairing; arbitrary regroupings are not excluded. The attained result is not the required total bound Â₂(2x)≥0 for all x.

WHY IT FAILS: Positive half-line theta summands have boundary slopes of opposite signs. Their second-spectrum cross terms inherit the product of those slopes at high frequency, so simple exchange pairing cannot be nonnegative. Infinite modular cancellation is essential and has no established sign in this expansion. After the remainder split and this unsplit pairing test, stop this termwise decomposition continuation; no further formal rearrangement is justified without a concrete cancellation inequality.

One bounded test resolved as NEGATIVE; zero consecutive unresolved exploration turns. The next direction uses localized zero geometry to test a compact second-level inequality, a different mechanism from signing arithmetic summands. No RH candidate or disproof is obtained.
