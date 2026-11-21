# Neutral arithmetic tail audit — working record, step 232

Approved startup target and SPECIALIZE scope are unchanged; the supplied
assessment is reused. Source: bramble_trace paper 18, current URL labeled
v3, 22 October 2026; /v3 suffix inaccessible, unsuffixed version retrieved.
Inspected exact definitions, (3)--(8), and complete (36)--(40).

Checks in progress: primitive F_m has integer values j(m-j)/(2m), so
0<=F_m<=m/8 and |K_m(t)|<=m/(8t^2). For the inner product linear in
its first entry, every T_u and K_u in the second entry is conjugated.
The neutral tail identity uses Q(u) directly; representer q not used.
The j=1 jump equals -sum c_m/m, and including it cancels the constant
jump under Mobius inversion at every m>=2. Weighted Cauchy--Schwarz
appears to retain exactly 3 sqrt(2) zeta(3/2) K^(5/2), without log K.

Pending: write the complete endpoint/convergence proof and check the
final coefficient norm estimate. No full residual estimate, density,
representer, signs, contraction or RH conclusion is contemplated.
All preexisting changes are preserved; no mathematical script needed.

Completed: both estimates pass with the stated constants. Full proof and
qualifications are canonical in L729; see history step 232. This file
retains the preliminary reasoning only and is not a current checkpoint.
