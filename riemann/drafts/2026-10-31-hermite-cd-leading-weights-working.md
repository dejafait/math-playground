# Complete Hermite discriminant: saved bounded calculation

Approved target: the highest two diagonal-CD weights of the actual P_N.
Inputs: L018–L020 and L564; the unchanged ready assessment is
`literature/2026-10-31-hermite-cd-cone-leading-coefficient-test.md`.

Set m=2N>=4, b=b_m>0, c=b_(m-2)>0. Writing
P_N=A t^m+B t^(m-2)+lower terms gives
A=(-1)^N 2^m b and B/A=-[m(m-1)+c/b]/4.
The complete D(P_N) has highest coefficients m A^2 and
2(m-3)AB. Terms below degree m-2 in P_N contribute only at degree
<=2m-6 in D, so this includes all relevant mixed terms.

For K_j=sum_(ell=0)^j H_ell^2/(2^ell ell!), its leading
coefficient is k_j=2^j/j!, and its next coefficient is
-j(j-2)k_j/2. The distinct even degrees make these kernels a basis.
Thus lambda_(m-1)=m A^2/k_(m-1)>0, while
lambda_(m-2) k_(m-2)=-(m-3)A^2 c/(2b)<0.
No coefficient asymptotic is needed: the obstruction holds for every
N>=2. This is a calculation to be fully written and checked, not an
Xi sign theorem or a claim that D(P_N) itself is negative.

Completed: the full proof and source qualifications are canonical in
L565. The N=2 normalization check gives weights 768 b_4^2 and
-64 b_4 b_2. The separate stop record retains the certificate's scope;
independent auditing is pending. Current routing is only in PROGRESS.md.

2026-10-31 audit completion: the approved finite replay passes without
repair. The full audit, including the direct N=2 polynomial and kernel
check, is canonical in L565. The pending-audit sentence above records
the earlier state; no unfinished derivation was discarded. The cone
stop remains specific to nonnegative diagonal-CD coordinates.
