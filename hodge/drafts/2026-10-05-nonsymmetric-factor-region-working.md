# Working note — variable factor filter

The ready SPECIALIZE assessment is
`drafts/literature/2026-10-04-nonsymmetric-factor-polystability-region.md`.
The bounded target is the saved necessary filter, not bundle existence.
L051's product splitting exclusion and curvature restriction passage
are independent of the pure point coefficients.

Write m=-(a+4), n=-(b+4). A stable locally free factor requires
m or n at least four by section vanishing and K3 Riemann--Roch.
For a split slope-zero factor, the exact metric gives line classes
Z k, k=(-4,-2,1,2), k^2=-14, so its second Chern number is 14r^2.
Thus zero or an integer at least four survives these surface tests;
this is not stable bundle existence. L050's mn=6 modulo 12 removes
zero and four. Expected final non-exclusion set: m,n>=5 and
mn=6 modulo 12. Smallest total is eleven, at (5,6) and its reversal,
equivalently corrections (-9,-10) and (-10,-9).

This saved intermediate reasoning was completed in the canonical
[L052 proof](../lemmas/L052-nonsymmetric-factor-polystability-region.md),
with an exact arithmetic certificate under scripts/cubic-kahler/.
It is an archived working note, not the current checkpoint.
No holomorphic product bundle or transverse direction was established.
Existing work was preserved.
