# Exact pure-power deweighting: recovered-response limitation

The canonical calculation is [L649](../lemmas/L649-exact-power-sum-deweighting-limitation.md).
It uses every spatial coefficient and every Blaschke factor, with the
original integer mass and the conjugated angle intact. It imports
Biro's theorem only after producing genuine repeated-node pure sums.

WHY IT FAILS: The exact map is a coisometry followed by the inverse
anchor normalization. Its sharp ambient recovery bound retains only
the already stopped full-inner-input response. Biro's bound is weaker
than the known zeroth pure sum M; even every recovered power sum
together gives energy o(exp(-n/16) D_single,n). The orthogonal kernel
component, which may hold most of the actual energy, is not controlled.
Ambient minimizers are not asserted to obey the original pole support
or positive integer residues. This stops this deweighting-plus-ambient-
norm mechanism, not the target, all nonlinear transfers, or RH. Any
continuation must use materially additional information about permitted
preimages, rather than repeat pure-sum identities or drop grid modes.
