# Fixed-slice motion audit — 2026-09-11

Checkpoint: L125 matches the exact E alternative in L067, not necessarily
(H-b)S. Assume finite positive strip supremum and simple nonreal zeros.
Imaginary-axis zeros are absent because the theta integral there has the
strictly positive factor cosh(bu). L063 supplies full reciprocal squares.
Thus selected velocities have limsup at most -1/H. Attainment is separate.

Resume by writing the precise conditional lemma and auditing the supremum
quantifiers. Candidate obstruction (to be verified before promotion):
b_n(t)=1-1/n-t+4t(1-exp(-n²t²)), n≥2. Each derivative at zero is -1,
but for t>0 the supremum is 1+3t. This is an abstract analytic family,
not a heat solution. It isolates failure of uniform first-order control,
even with branches all defined on one interval. A sufficient missing
condition is an upper envelope H(t0+h)≤H(t0)-h/H(t0)+o(h), uniformly
covering all zeros; fixed-point existence statements do not supply it.

Completed: the candidate was verified analytically and the audited result
is stored in lemmas/L126-fixed-slice-motion-selection-and-supremum-obstruction.md.
This draft's resume instruction is superseded by PROGRESS.md.
