# Nine-union fourth-support reduction — working attempt

Started 2026-10-08 under the pre-existing SPECIALIZE assessment
`literature/2026-10-08-nine-union-fourth-support-incidence.md`.

Main gap: arbitrary sixteen-count equality, with global interval 11/q–16/q
and allowable count fifteen. Approved intermediate target: exact reduced
fourth-support incidence for L041 tau=1 local triples, arbitrary labels,
weights and original finite parameters. Downstream use: count or exclude
additional errors without determinant-only zero-kernel blindness.
Continue if all quotient ranks, recovered weights and finite-chart gates
are necessary and sufficient; abandon this reduction if it only restates
moments, loses an exceptional rank or assumes unjustified descent.
Inputs: L010, L041, audited L042; L016 analytic antecedent only.

Working derivation saved before final proof:
Write supports {h,d,y1,y2}, {h,d,z1,z2}, {h,w1,w2,w3}.
Let a=gamma1-gamma0, rho=(gamma2-gamma0)/a, t=(T-gamma0)/a;
rho!=0,1. Normalize syndrome by a/lambda. Put Y=sum c_y v_y,
Z=sum c_z v_z. Its singleton part is (1-t)Y/(1-rho)+t Z/rho.
The h and d coefficients are c_h[(1-t)p/(1-rho)+t q/rho]
and c_d[(1-t)r/(1-rho)+t(1-r)/rho].
For K quotient the four support recurrences by C_K=(F_K(v_h),F_K(v_d)),
whose rank is the number of {h,d} missing from K. A rational left-kernel
basis gives y_K,z_K; projected incidence is
rho(1-t)y_K+(1-rho)t z_K=0.
One zero vector forces an excluded t=0 or 1; independent nonzero vectors
are inconsistent. Two nonzero proportional vectors z_K=mu y_K give
D=rho-(1-rho)mu and t=rho/D; D=0 has no finite solution, mu=-1
is precisely the excluded third parameter. The proportionality constant
is in F_97, even when rho and weights are not.
The two zero vectors occur exactly for K={y1,y2,z1,z2}: injectivity
on at most eight moment columns proves y_K=0 iff {y1,y2} subset K,
and the analogous statement for z_K. This is the unique universal system.
At an isolated candidate, multiply the normalized syndrome by D:
Z-mu Y+c_h(q-mu p)v_h+c_d[1-(1+mu)r]v_d.
Recover rational required absent-column coefficients beta using the first
m rows of C_K, m=0,1,2; compare them with the displayed actual coefficients.
Recover all four fourth weights by the first four moment Vandermonde.
Universal system requires both h,d coefficients zero; it gives
D*=r+rho-1!=0, t*=rho*r/D*, r*q=(1-r)*p, and nonzero singleton weights.

Still to check in the canonical proof: all zero-rank conventions,
necessity/sufficiency of recovery, signs and actual scaling lambda/(a D),
parameter exclusions in both branches and same-support failure. No count,
chart descent or completion is asserted. No script/certificate is needed
for these symbolic linear-algebra identities.

Final result: the complete reduced necessity/sufficiency proof, including
rank zero, the unique universal support, all recovered weights and
same-support failure, is saved in
[L043](../lemmas/L043-nine-union-fourth-support-incidence.md).
The symbolic check of the universal specialization rho=2, r=-z/c_d
recovers L016's finite parameter 2z/(z-c_d), its absent-h equation and
its nonzero four singleton weights. This is a consistency check only;
L016's finite count is not an input. No mathematical script was used.
All denominator and third-parameter exclusions were checked algebraically.
The continuation test is met, but separate critical audit remains required.
This is local progress using known machinery, with no claimed improvement
beyond the sources checked or on the global count. Thirteen additional
parameters, arbitrary-family extraction and ABF26 identification remain open.
