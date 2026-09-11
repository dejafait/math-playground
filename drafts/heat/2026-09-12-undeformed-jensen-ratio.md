# Undeformed Jensen ratio — 2026-09-12

Checkpoint: inspected existing changes; L134 and L135 are completed and preserved. This step concerns only λ=0.

Candidate, not yet proved: set H=1/2, t=x+1/2, c=t+3i/2, r=1+sqrt(17)/2. Reflection sends the center to s=2-it. The reciprocal Dirichlet series bounds |ζ(2-it)| below; uniform vertical-strip Stirling bounds the center below by a constant times |t|^(5/2)exp(-π|t|/4). Reflect each point of the radius-2r disk individually to Re(s)≥1/2. Elementary Euler summation bounds ζ there polynomially, while Stirling preserves the same exponential decay up to a constant. Expected ratio O(|t|^(r+1)).

Resume by checking Euler summation, gamma exponents, bounded horizontal/vertical shifts, compact t, and which arguments fail to extend to nonzero λ. Do not use the candidate as a DAG input until audited.

Completed: L136 proves the candidate ratio and the full logarithmic unit-window count at λ=0. It also proves the stronger coarse absolute lower bound false on this slice. Uniform estimates on a nontrivial heat interval remain unproved.
