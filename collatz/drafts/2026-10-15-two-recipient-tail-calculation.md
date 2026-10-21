# Two-recipient tail calculation — working record

Approved target: determine endpoint/domain/J feasibility in literal order
for integer 1<=t<=9250244, with a_22=20, a_23=2+18t,
a_24=166504394-18t, and all other tails 2.
Prior SPECIALIZE: `literature/2026-10-15-two-recipient-tail-j-feasibility.md`.
Essential inputs: L051 conventions, L055 indexed table and positive Lambda,
L064 affine construction and logarithm bounds; L068 is the method comparison.

Main gap is universal eventual descent. A uniform subsystem rejection
could later feed L041's actual-word necessity; no such bridge is assembled
here. Other supports/orders, integer realization, entry and divergence
remain unresolved. Test: one exact feasible tuple stops uniform J-only
exclusion; an all-interval strictly negative necessary margin proves it.

Unfinished calculation: fix the changed row-22 tail in the t=0 prefixes.
Write x=2^(-18t), C=C_24(0), A=sum_(j<24) eta_j/C_j(0), D=exp(Lambda)-1.
Then the formal root gives n_24(t)=eta_24/D+C*A*(1+D)*x/D,
so its own-input J margin decreases. At t=1 rows 22 and 23 both have
tail 20. Every first-24 multiplier should exceed 2; the same B upper
bound as L068 applies after that comparison is checked. The total
first-24 tail increment is 36, matching L068's t=2 prefix exponents,
but the B bound must be justified afresh. No verdict yet certified.

Completed: all 27 finite checks pass, and the exact parameter argument
rejects every admitted t at row 24. Full proof, citations, qualifications
and reproduction evidence are canonical in
[L070](../lemmas/L070-two-recipient-tail-j-infeasibility.md).
The unfinished reasoning above is preserved as the initial attempt.
No dependent bridge or broader support was investigated. Separate
critical audit is the proposed continuation, requiring scope approval.
