# Fixed or polynomial normalized strict slack cannot pay the cone budget

The canonical proof is
[C673b](../lemmas/C673b-normalized-strict-action-repair-cost.md),
with exact constants in
`scripts/one-sided-hankel/positive-cone-repair-cost-certificate.json`.
This result has not yet had its separate critical audit.

WHY IT FAILS: on L673's exact admissible phase sequence, a zero-anchor
functional with actions at least ||Pi_(2n)W_a||_2 costs at least
exp(11n/1000) eventually. Thus a fully paid repair at the proposed
exp(n/100)*n^C budget requires slack <=exp(-n/1000)*n^C. The same
positive witness rules out fixed or polynomial normalized strict margin
in the final separator, independently of a triangle-norm budget.
The fixed 10^(-8) floor from the finite screen cannot be kept at all n.

This does not refute the rate-1/100 cone bound or exclude exact zero
actions, exponentially shrinking slack, or a different direct dual.
It says nothing about original unit residues, H, Xi or RH. Preserve
the finite screen and its uncertified signs. Park this fixed-slack
variant; a new primal gauge is an independently testable continuation.
