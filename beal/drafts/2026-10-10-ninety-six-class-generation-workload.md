# 96a1 class-generation workload — working record

The approved target is the exact order-discriminant workload test in the
saved SPECIALIZE assessment. Essential inputs are L050's degree-twelve
field model and FNS Section 7.2's degree-36 compositum with integral
generator T satisfying T^3-4T^2-160T-1264. L032 identifies the retained
branch but is not an arithmetic input. The two monic equations make
U and T integral; the cited degree 36 makes U^i T^j (0<=i<12,0<=j<3)
a full-rank order basis. The planned certificate computes its trace
determinant and a conservative Minkowski cutoff using s<=18 and pi>3.

Continuation test: cutoff <=10^6 plus a rigorous ideal backend permits
considering enumeration; a larger order cutoff parks enumeration at that
cutoff only. Field discriminant/index, class/unit completeness and the
global Selmer upper image remain unresolved. No GRH or point/Selmer
equality is assumed. Existing arithmetic is preserved.

Completed: [L051](../lemmas/L051-ninety-six-order-class-generation-bound.md)
contains the applicability proof and exact discriminants. Full evidence
is in `scripts/ninety-six-class-generation/workload-certificate.json`.
The sufficient conservative integer cutoff is about 1.65*10^118,
versus the required enumeration cutoff 10^6. Exact integer inequalities
certify rounding; derivative resultants check the trace discriminants.

Decision: park enumeration at this order cutoff. This is an informative
negative workload result, not proof that the actual field cutoff exceeds
10^6 or that unconditional certification is impossible. No backend was
installed or full class-group run started. Actual signature and maximal
order index remain unresolved. PROOF.md stays unchanged because the
main argument has not changed.
