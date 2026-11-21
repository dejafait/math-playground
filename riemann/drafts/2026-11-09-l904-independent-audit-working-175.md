# L904 independent audit — working record, step175

Approved target: the fixed x=16,y=0 three-lobe budget only, under
`drafts/literature/2026-11-09-l904-independent-budget-audit-review.md`.
Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Audit object L904; essential inputs L019/L037/L312/L898 and the original
step135 program, its actual imports and complete certificate. L905 is
comparison only. No cross-notebook input, new allocation or grid change.

Read L904 and the original program in full, L037, L019, L898's first
normalization/domination subsection, and L312's invoked envelope,
theta-tail and trigonometric arguments. Read the actual interval class,
Machin routine, self-check and sine/cosine routine. The retained step135
history/ATTEMPTS record already stops equal shares; step139 concerns a
different Hall budget. Reuse approved source coverage; no new browsing.

Analytic audit so far: the determinant of (t,q)->(u,v) has absolute
value one; p^2 times the two Phi factors is t^2 times the K product.
Evenness and absolute Fubini give rho and A0=2M0M2. The origin half-lobe
is exactly B0; every full positive lobe is split only twice, by halves.
L019 domination gives absolute convergence of the full resource sum.
The finite-t product error is <=32 epsilon; its density integral is
<=64 epsilon T^3/3<512 epsilon/3. For t>=T and q<=5pi/32,
t-q/2>=27pi/64>0. Both product and normalization tail bounds follow
from exp(3)>20 and exp(2w)>=1+2w with the stated rounded-up exponents.
All three lobe errors and the two moment errors are present in code.

The exact pi grid ends at cosine zeros, so each cell has a single
cosine sign, beyond merely the sign of its integrated weight. Reflected
box endpoints and zero crossings in code match L904 (7). The code uses
real inclusion, not smoothness across the finite-head seam. L037's
contexts, exact sign operations, exp widening and fixed-integer Taylor
reduction implement the stated contracts. Full /result and /bounds
were inspected; no defect found yet. This is not a final audit verdict.

Completed: all 2207 cache entries, 160 cosine weights and 163840 boxes
were checked; exact-integer/Fraction reconstruction validates finite
sums, complete errors and division. The original fixed-grid replay is
identical in every field. All 4781 checks pass, with no failed check,
in `scripts/theta-marginal/l904-independent-audit-175.json`. The full
reconstructed rational upper endpoint was inspected. The strict interval
(-32/1000,-2/1000) survives. Full proof and audit are canonical in L904;
this working record is not a second proof. Originals are preserved.
Decimal/interpreter trust and the main positivity gap remain.
