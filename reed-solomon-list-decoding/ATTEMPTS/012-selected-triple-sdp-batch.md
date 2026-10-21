# Selected triple SDP batch — stopped as a sufficient threshold certificate

WHY IT FAILS: The complete exact rational primal witness in
[L022](../lemmas/L022-selected-triple-sdp-primal-limitation.md) satisfies
all constraints of the approved selected Schrijver batch, with objective
more than 1.383 times the required threshold, even after flooring.
Independent reconstruction checks every scalar/pair row, coefficient
and PSD congruence, including the singular complement block's zero row.
Therefore optimization of this same batch cannot certify index 956.
The optimum and feasibility for omitted blocks remain unknown; this
witness is neither a packing nor an unsafe RS list. A test of the same
explicit assignment against both full (0,0) blocks is a materially
larger constraint diagnostic, proposed for separate scope approval.
Full certificates and the independent audit are under
`scripts/finite-support/selected-triple-sdp-*.json`.
