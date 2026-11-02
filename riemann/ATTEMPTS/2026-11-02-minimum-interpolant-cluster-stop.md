# Minimum-norm exact-recovery input: clustered-pole stop

The completed method obstruction is canonical in
[L646](../lemmas/L646-minimum-interpolant-cluster-response-stop.md).
It retains the full symbol, distinct poles, unit original residues and
one common pole set for all rotations. A separate conceptual audit on
2 November 2026 accepted the proof without a mathematical correction;
its full checks are canonical in L646, Proof Section 8.

WHY IT FAILS: Replacing the full Blaschke input by its minimum-H2-norm
interpolant at every pole optimizes only inputs recovering exactly the
unweighted logarithmic derivative. For m=floor(n/3) distinct poles
a_j=x+i*j*exp(-n^2), those interpolation conditions approach a confluent
space. A fixed angular arc in disk-unitary coordinates forces the
projection norm to stay >=1/63000, uniformly in the rotation beyond
L646's explicit onset. Thus the best normalized response in this class
is <=63000*n*exp(-lambda*n), lambda>47/1000>1/32. The full constant-input
response is >=m on the same family. This stops exact-recovery input
normalization, not the angular operator target, the later-grid sum,
other uses of the common polynomial, or RH. The cluster must be handled
through its actual positive-residue response rather than extra exact
interpolation conditions.
