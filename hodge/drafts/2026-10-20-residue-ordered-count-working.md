# Residue ordered-count working checkpoint

2026-10-20, approved target: Bound the number of ordered opposite coincidences in terms of L138's fixed parameters using the residue-value map at each normalization fibre.

The supplied SPECIALIZE assessment is reused. Relevant L120/L121 proofs,
L137 parameters, L138 bound/audit and ATTEMPTS/070,078 have been inspected.
Existing unfinished work is preserved. No external discovery or script is needed.

Planned canonical argument: for A=O_{Z,z} and C=(nu_*O_B)_z,
Chinese remainder at the r distinct maximal ideals gives C onto k^r.
A maps to diagonal constants, and its action on the target factors
through k=A/m=C (the complex numbers). Thus Q_z=C/A maps A-linearly
onto k^r/k diagonal; finite length gives length_A(Q_z)>=r-1.
If d_z=r_z-1 and D=sum d_z, then D<=Lambda and the ordered reduced
count is sum(d_z^2+d_z)<=D^2+D<=Lambda^2+Lambda. Substitute L138,
using the integer floor of its fixed bound. Empty partitions are allowed.

Saved pre-completion plan, now superseded by canonical L139: write the complete specialization and qualifications in
L139, update only the actual argument overview and ID-only DAG, record
history/checkpoint and a separately reviewable audit continuation, then
run the hodge-scoped documentation checker. No minimal-defect equality,
normality, CM, coherent vanishing or contradictory lower bound is used.
