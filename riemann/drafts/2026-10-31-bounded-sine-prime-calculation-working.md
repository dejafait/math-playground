# First-order bounded sine calculation: working checkpoint

Approved target: Test the first-order Taylor implementation of the bounded sine prime Peano dual, retaining both weighted remainders and all complete-chirp stationary terms.
Prior EXPLORE: literature/2026-10-31-bounded-sine-prime-peano-dual.md.
Inputs read: L574 Sections 1--5, C481a, C574a, L477 finite expansion/norms and audit, L316 (7). Source theorem imports remain as assessed; existing unfinished work preserved.

Main gap: actual-Xi positivity; intermediate target is the two sine dual budgets, relevant only to the fixed-square residual lower bound. Continue only with compatible fixed constants for both budgets; otherwise preserve the exact failure.

Unfinished reasoning saved before further estimation:
- For b=sin(epsilon P), exact compact Fubini gives integral U psi=L^2 integral_J D b; |psi|<=1. Taylor remainder bounded by epsilon^3 |B|^3/6 must be paid twice.
- Group A_sigma B^k for k<=3. Length M y^3<=T^(7/8); bounded block-prime multiplicity suggests coefficient norm O_k(L). This can pay density cubic costs by weighted Cauchy--Schwarz.
- Chirp cubic cost uses V's finite product form and weighted jet moments against |B(t)|^3, with t=x-u, |u|<=h. Jet weights lambda(x)-log n are variable: need finite summation by parts or an explicit expansion around L/2; no mean-square theorem for a variable vector by assertion.
- Full convolution of cos(t log p) gives sinc^2(h log p/2) cos(x log p); restriction to J differs on both boundary strips only. Bound these strips explicitly, do not discard them.
- The stationary minus mode has r=2pi nmp. L316 (7) gives 2theta(x)=x log(x/(2pi e))-pi/4+O(1/T). Gonek Lemma 2 with sigma=1/2 leaves a positive main term pi log(n/m)^2 sinc^2(log p/(2L)) for T<2pi nmp<=2T. The other sign has no saddle. All repeated products and endpoints remain.
- Crude complete stationary count: n>=X^2/(pM); count m in (X^2/(pn),2X^2/(pn)] is <=X^2/(pn)+1, and |log(n/m)|<=log p on that range. This suggests stationary sum <=(T/2) sum_p(log p)^3/p plus a power-saving error. Compare directly with L574's exact positive density main sum, not just its coarse c1.
- Need prove aggregate endpoint errors (group k=nmp, retain multiplicities via elementary divisor bound) are o(T L^3), and pay exact-theta error and strips. No cancellation of stationary main terms is presumed.

No result yet claimed. No scripts run.

Completion: the full argument, including both moments, all stationary terms, endpoint errors and fixed constants, is now canonical in `../lemmas/L575-bounded-sine-prime-peano-dual.md`. The preceding notes are the preserved unfinished checkpoint, not a substitute for that proof. Independent audit remains pending.
