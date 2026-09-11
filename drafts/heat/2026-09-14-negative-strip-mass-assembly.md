# Negative-strip mass assembly — 2026-09-14

Checkpoint: the cutoff was traced back to L188, where R=C N^(3/2)
for a fixed positive constant bounding all original displacements.
It is not merely an unspecified O(N^(3/2)) upper bound. Put
L=N^(3/2), q=min(C,1)/2 and W=floor(qL). Eventually
qL/2<=W<=min(R,L). L211 preserves full-core occupancy at this W.
Hence ell>=2W>=qL. Choose eta=min(q,exp(-2^25)) and delta=1/10.
The injective map (a,b,c,d) -> (a,b,c,d,floor(sqrt(abcd))+1)
should give C_N(eta,delta)>(3/131072)(t/48)^2 N³ by L202
and L211. Resume by checking every L198 hypothesis and recording
the resulting lower bound; do not infer a signed-total lower bound.

Completed: the hypothesis audit and both mass bounds are stored in
`lemmas/L212-negative-central-strip-mass-lower-bound.md`. The fixed
cutoff permits the stated W, and every counted tuple retains all exact
endpoints. No signed-total conclusion is asserted.
