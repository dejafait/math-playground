# Fixed row0 unit test — step484 working record

Approved scope: the exact Next action in the pre-existing SPECIALIZE
assessment `literature/2026-10-25-d35-row0-unit-allocation-feasibility.md`.
Main gap: universal descent; this test concerns only one literal real
allocation. No minimum, seed or integer realization is available.

Prospective decisive comparison: rotate the exact shifted affine root to
row1, retaining every endpoint including row24 and row0. Write
c_i=3^(3J_i+H_i)/2^(4J_i+H_i+a_i), eta_i as in L055, and
D=2^N/3^K-1. Then n1=B1/D, where B1 is the positive sum of
eta_i divided by the chronological prefix products at cut1. The first
24 prefixes use rows1,...,23; the last term is eta0*c0*exp(Lambda).
Try c_i>2 for rows1,...,23 and c0<1/1000. Certified
0<Lambda<1 gives exp(Lambda)<=1/(1-Lambda). Seek B1<5,
D>1e-10, hence s1<60000000000, below row1's J threshold
(4/11)*2^60. These are proposed bounds, not yet certified results.

Continue if all symbolic identities and rational bounds check; otherwise
preserve the failed comparison and report uncertainty. The test may end
after one violated necessary constraint. Ready sources: L055's table,
finite affine specialization and log enclosure method; L041 is needed
only for interpretation, not for this real-system feasibility verdict.
Attempt032 and both original witnesses remain untouched. All prior
uncommitted work is being preserved.

Completed: L104's exact cut1 root cap rejects row1's J guard. The
certificate has 170 passing finite checks and no failures. Full proof
and qualifications are canonical in `lemmas/L104-d35-fixed-row0-unit-exclusion.md`;
finite evidence is `scripts/postspell-word-count/d35-row0-unit-certificate.json`.
No other allocation or constraint verdict was attempted. The proposed
bounds above are now established for this one allocation; separate
critical audit remains pending.
